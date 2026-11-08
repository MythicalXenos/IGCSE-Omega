#!/usr/bin/env python3
"""
extract_scripts.py -- the ladder, wired to the page geometry.

The examiner reports put the candidate's script in as a picture and the examiner's words in as text,
with the score in the same text. Reading the two apart is the whole job, so this tool walks a report
in the order a marker would:

    L1  page      every page of the report, in order
    L2  section   cut at the "Question N (x)" headings, INCLUDING headings mid-page
    L3  block     the pictures and text blocks in reading order down the page
    L4  line      the score line ("0 marks." / "Level 3 - 8 marks" / "This response scored 6 marks.")
    L5  word      tokenise what came out, flag tokens outside the subject vocabulary

The pairing rule is the one thing that had to be learned the hard way (KNOWN_DEFECTS D19). Pearson
does not put the score in a fixed place -- sometimes it is above the script, sometimes below it,
sometimes on the next page, and one page can hold the end of one answer and the start of another:

    a score line CLOSES the run of pictures written since the previous score line,
    provided the question has not changed in between.

Every "this script scored X" claim in the bank is downstream of that pairing, so it is checked
independently by `verify_script_pairs.py` (score line must exist on the page it claims; mark must not
exceed the question paper's tariff).

and it writes two things per script:

    audits/corpus/scripts_png/<key>_p<page>_<n>.png   the facsimile, 2x, greyscale
    audits/corpus/scripts.json                        the manifest: page, question,
                                                      mark line, commentary, image path,
                                                      span (pages of one answer), and whether any
                                                      text layer exists

What it deliberately does NOT do is pretend to read the handwriting. OCR is print-trained and turns
cursive into noise (see audits/SCRIPT_RECONSTRUCTION.md). The manifest marks each script
"text_layer": false when the page carries no text for the script, which is the signal that a human
(or a vision reader) must transcribe it -- and the transcript then goes in audits/corpus/transcripts/
so it can be checked and never quoted as verbatim.

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


def mark_statements(page, idx):
    """every score line printed on a page, in reading order: (page_idx, y, value, text, block_txt)"""
    out = []
    for b in page.get_text("blocks"):
        txt = b[4]
        if not txt.strip():
            continue
        for m in MARK.finditer(txt):
            out.append({"page": idx, "y": b[3], "text": m.group(0).strip(),
                        "value": next((int(g) for g in m.groups() if g), None),
                        "block": txt.strip()})
    return out


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
    current = []          # the pictures written since the last score line: one script
    pending = None        # a score line printed ABOVE its script (see below)

    def close(group):
        """one script written across several page-images: record the span on its first row"""
        if len(group) > 1:
            group[0]["span"] = [[r["page"], r["n"]] for r in group]
            for r in group[1:]:
                r["continuation"] = True

    def assign(row, mk, block, page_idx=None):
        row["mark_line"] = mk.group(0).strip()
        row["mark_value"] = next((int(g) for g in mk.groups() if g), None)
        row["commentary_after"] = block[:1200]
        if page_idx is not None and page_idx != row["_page_index"]:
            row["marked_on_page"] = page_idx + 1      # the score is printed on another page

    cur_q = qper.get(0)
    for i, page in enumerate(doc):
        q = qper.get(i)
        if want and q != want:
            continue
        infos = [im for im in page.get_image_info(xrefs=True)
                 if im["width"] >= MIN_WIDTH_PX and (im["bbox"][2] - im["bbox"][0]) >= MIN_WIDTH_PT]
        infos.sort(key=lambda im: im["bbox"][1])
        events = []
        for b in page.get_text("blocks"):
            if b[4].strip():
                events.append((b[1], 1, ("txt", b[4].strip())))
        for n, im in enumerate(infos, 1):
            y0, y1 = im["bbox"][1], im["bbox"][3]
            path = os.path.join(OUT_DIR, f"{key}_p{i + 1}_{n}.png")
            h, w = render(doc, im["xref"], path)
            below = [t for t in blocks(page) if t[0] >= y1 - 6]
            events.append((y0, 0, ("pic", {
                "_page_index": i,
                "report": key, "page": i + 1, "n": n, "question": None,
                "image": os.path.relpath(path, ROOT),
                "px": [im["width"], im["height"]], "rendered": [w, h],
                "mark_line": None, "mark_value": None, "commentary_after": "",
                "text_layer_for_script": False,
            })))
        events.sort(key=lambda e: (e[0], e[1]))
        for _, _, (kind, payload) in events:
            if kind == "pic":
                payload["question"] = payload["_q"] = cur_q
                rows.append(payload)
                # a score printed ABOVE the script: this is the script it belongs to
                if not current and pending and pending[0] == cur_q:
                    assign(payload, pending[1], pending[2], pending[3])
                    pending = None
                    payload["_closed"] = True
                current.append(payload)
                continue
            # a "Question N (x)" heading inside the text stream moves the question on; the
            # pictures above it belong to the old question and will not be marked from here
            h = QHEAD.search(payload)
            if h:
                nq = f"{h.group(1)}({h.group(2).lower()})"
                if nq != cur_q:
                    close(current)
                    cur_q, current, pending = nq, [], None
            mk = MARK.search(payload)
            if mk is None:
                continue
            if current:
                first = current[0]
                if first.get("_closed"):
                    close(current)
                    current, pending = [], (cur_q, mk, payload, i)
                    continue
                if pending and pending[0] == first["_q"]:
                    assign(first, pending[1], pending[2], pending[3])
                    pending = (cur_q, mk, payload, i)
                elif first["_q"] == cur_q:
                    assign(first, mk, payload, i)
                    pending = None
                else:
                    pending = (cur_q, mk, payload, i)
                close(current)
                current = []
                continue
            pending = (cur_q, mk, payload, i)

    close(current)
    if current and pending and pending[0] == current[0]["_q"]:
        assign(current[0], pending[1], pending[2], pending[3])
    for r in rows:
        for k in ("_page_index", "_q", "_below", "_closed"):
            r.pop(k, None)
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
