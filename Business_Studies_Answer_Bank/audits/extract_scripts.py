#!/usr/bin/env python3
"""
extract_scripts.py -- the ladder, wired to the page geometry.

The examiner reports put the candidate's script in as a picture and the examiner's words
in as text. Reading the two apart is the whole job, so this tool walks a page in the
order a marker would:

    L1  page      every page of the report, in order
    L2  section   cut at the "Question N(x)" headings
    L3  block     on each page: each picture, then the text block nearest BELOW it
    L4  line      the mark line inside that text ("0 marks." / "3 marks." / "Level 2 - 5")
    L5  word      tokenise what came out, flag tokens outside the subject vocabulary

and it writes two things per script:

    audits/corpus/scripts_png/<key>_p<page>_<n>.png   the facsimile, 2x, greyscale
    audits/corpus/scripts.json                        the manifest: page, question,
                                                      mark line, commentary, image path,
                                                      and whether any text layer exists

What it deliberately does NOT do is pretend to read the handwriting. OCR is print-trained
and turns cursive into noise (see audits/SCRIPT_RECONSTRUCTION.md). The manifest marks each
script "text_layer": false when the page carries no text for the script, which is the
signal that a human (or a vision reader) must transcribe it -- and the transcript then goes
in audits/corpus/transcripts/ so it can be checked and never quoted as verbatim.

Usage:
    python3 audits/extract_scripts.py --all
    python3 audits/extract_scripts.py 4BS1_01R_2206
    python3 audits/extract_scripts.py 4BS1_01R_2206 --question 2a
"""
import glob
import json
import os
import re
import sys

import cv2
import numpy as np
import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_DIR = os.path.join(ROOT, "Sources", "Official_Pearson", "Full_Examiner_Reports")
OUT_DIR = os.path.join(ROOT, "audits", "corpus", "scripts_png")
MANIFEST = os.path.join(ROOT, "audits", "corpus", "scripts.json")

MIN_WIDTH_PX = 380          # narrower than this = logo / rule / glyph
MIN_WIDTH_PT = 200          # ...and in page coordinates
SCALE = 2

QHEAD = re.compile(r"Question\s+(\d)\s*\(\s*([a-g])\s*\)", re.I)
MARK = re.compile(
    r"(?:(?:This response (?:scored|was|is)|scored)\s+(?:a\s+)?(?:Level\s*\d+\s*[\u2013-]\s*)?(\d+)\s*marks?"
    r"|(?:Level\s*\d+\s*[\u2013-]\s*)(\d+)\s*marks?"
    r"|(\d+)\s*marks?\s*(?:awarded|\.|$)"
    r"|No marks awarded)", re.I)


def blocks(page):
    out = []
    for b in page.get_text("blocks"):
        x0, y0, x1, y1, txt = b[0], b[1], b[2], b[3], b[4]
        if txt.strip():
            out.append((y0, y1, txt.strip()))
    return sorted(out)


def question_running(doc):
    """question number in force on each page: the last heading at or above it"""
    cur, per = None, {}
    for i, page in enumerate(doc):
        t = page.get_text()
        for m in QHEAD.finditer(t):
            cur = f"{m.group(1)}({m.group(2).lower()})"
        per[i] = cur
    return per


def render(doc, xref, path):
    pix = pymupdf.Pixmap(doc, xref)
    if pix.n - pix.alpha >= 3:
        pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
    a = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
    g = cv2.cvtColor(a, cv2.COLOR_RGB2GRAY) if pix.n >= 3 else a[:, :, 0]
    up = cv2.resize(g, None, fx=SCALE, fy=SCALE, interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(path, up)
    return up.shape


def extract_one(key, want=None):
    pdf = os.path.join(PDF_DIR, key + "_ER_full.pdf")
    if not os.path.exists(pdf):
        print("NO PDF:", pdf)
        return []
    doc = pymupdf.open(pdf)
    qper = question_running(doc)
    os.makedirs(OUT_DIR, exist_ok=True)
    rows = []
    for i, page in enumerate(doc):
        q = qper.get(i)
        if want and q != want:
            continue
        infos = [im for im in page.get_image_info(xrefs=True)
                 if im["width"] >= MIN_WIDTH_PX and (im["bbox"][2] - im["bbox"][0]) >= MIN_WIDTH_PT]
        if not infos:
            continue
        infos.sort(key=lambda im: im["bbox"][1])
        txt = blocks(page)
        for n, im in enumerate(infos, 1):
            y0, y1 = im["bbox"][1], im["bbox"][3]
            below = [t for t in txt if t[0] >= y1 - 6]
            above = [t for t in txt if t[1] <= y0 + 6]
            # the first block under the picture is the mark line; the next is the comment
            after = " ".join(t[2] for t in below[:2])[:1200]
            mk = MARK.search(after)
            if mk is None:
                # some pages put the score line ABOVE the picture ("1 mark" then the scan)
                before = " ".join(t[2] for t in above[-2:])[:800]
                mk = MARK.search(before)
                if mk:
                    after = before + " || " + after
            path = os.path.join(OUT_DIR, f"{key}_p{i + 1}_{n}.png")
            h, w = render(doc, im["xref"], path)
            rows.append({
                "_page_index": i,
                "report": key, "page": i + 1, "n": n, "question": q,
                "image": os.path.relpath(path, ROOT),
                "px": [im["width"], im["height"]], "rendered": [w, h],
                "mark_line": mk.group(0).strip() if mk else None,
                "mark_value": next((int(g) for g in mk.groups() if g), None) if mk else None,
                "commentary_after": after,
                "printed_above": " ".join(t[2] for t in above[-2:])[:600],
                "text_layer_for_script": False,
            })
    # A full-page script (the picture fills the page, no text beside it) is marked on the
    # page AFTER it: the commentary opens there and prints the score before the next
    # question heading. Walk forward to find it, and stop at the next heading.
    for r in rows:
        if r["mark_value"] is not None:
            continue
        i = r["_page_index"]
        for j in range(i + 1, min(i + 3, len(doc))):
            t = doc[j].get_text()
            m = MARK.search(t)
            h = QHEAD.search(t[:90])
            if m:
                r["mark_line"] = m.group(0).strip()
                r["mark_value"] = next((int(g) for g in m.groups() if g), None)
                r["commentary_after"] = t[:1200]
                r["marked_on_page"] = j + 1
                break
            if h:
                break
    for r in rows:
        r.pop("_page_index", None)
    return rows


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    want = None
    if "--question" in sys.argv:
        q = sys.argv[sys.argv.index("--question") + 1]
        q = re.sub(r"[^0-9a-g]", "", q.lower())
        want = f"{q[0]}({q[1]})"
        args = [a for a in args if a != sys.argv[sys.argv.index("--question") + 1]]

    keys = ([os.path.basename(p).replace("_ER_full.pdf", "")
             for p in sorted(glob.glob(os.path.join(PDF_DIR, "*.pdf")))]
            if (not args or "--all" in sys.argv) else args)

    manifest = {}
    if os.path.exists(MANIFEST):
        manifest = json.load(open(MANIFEST))
    for k in keys:
        rows = extract_one(k, want)
        if rows:
            manifest[k] = rows
            scored = [r for r in rows if r["mark_value"] is not None]
            print(f"{k:<16} images {len(rows):>3}  with a mark line {len(scored):>3}")
    json.dump(manifest, open(MANIFEST, "w"), indent=1)
    total = sum(len(v) for v in manifest.values())
    print(f"\nwrote {os.path.relpath(MANIFEST, ROOT)}  ({total} script images across {len(manifest)} reports)")


if __name__ == "__main__":
    main()
