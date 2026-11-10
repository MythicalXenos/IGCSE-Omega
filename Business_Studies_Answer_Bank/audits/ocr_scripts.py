#!/usr/bin/env python3
"""
ocr_scripts.py -- read the scanned candidate script facsimiles inside a Pearson
examiner report, so the bank can be checked against what candidates actually wrote.

The examiner reports print each script as an embedded image. Those images are the
only primary evidence of the script wording; the surrounding text is only the
examiner's comment and the mark. This tool pulls the widest image(s) off the page
that carries each question's commentary and runs OCR on them, then writes the raw
text plus a word-level gloss.

Usage:
    python3 audits/ocr_scripts.py <corpus-key> <question>        # e.g. 4BS1_01R_2506 2(d)
    python3 audits/ocr_scripts.py <corpus-key> --all             # whole report

Output: audits/corpus/ocr/<key>_<question>.txt  (raw OCR, page by page)
Prints nothing that should be quoted; see WARNING in the header of each dump.
"""
import os
import re
import sys

import numpy as np
import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PDF_DIR = os.path.join(ROOT, "Sources/Official_Pearson/Full_Examiner_Reports")
OUT_DIR = os.path.join(HERE, "corpus", "ocr")

# a script facsimile is a wide, page-width image; logos are ~200px wide
MIN_WIDTH = 500
QHEAD = re.compile(r"Question\s+(\d)\s*\(\s*([a-g])\s*\)", re.I)

_ocr = None


def ocr():
    global _ocr
    if _ocr is None:
        from rapidocr_onnxruntime import RapidOCR
        _ocr = RapidOCR()
    return _ocr


def page_scripts(page, doc):
    """widest embedded images on the page, in reading order"""
    out = []
    for img in page.get_images(full=True):
        xref, w = img[0], img[2]
        if w < MIN_WIDTH:
            continue
        pix = pymupdf.Pixmap(doc, xref)
        if pix.n - pix.alpha >= 4:
            pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
        arr = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
        res, _ = ocr()(arr)
        if not res:
            continue
        lines = [r[1] for r in res]
        out.append((xref, pix.width, pix.height, "\n".join(lines)))
    return out


def starts_heading(text, q=None):
    """True if the page opens a question section (heading within the first ~90 chars)"""
    head = text[:90].replace("\n", " ")
    m = QHEAD.search(head)
    if not m:
        return None
    if q is None:
        return (m.group(1), m.group(2).lower())
    return (m.group(1), m.group(2).lower()) == (q[0], q[1])


def question_pages(doc, q=None):
    """pages whose text names the question (heading or commentary mention)"""
    pages = []
    for i, page in enumerate(doc):
        t = page.get_text()
        if q is None:
            if QHEAD.search(t):
                pages.append(i)
        elif re.search(r"Question\s+" + re.escape(q[0]) + r"\s*\(\s*" + re.escape(q[1]) + r"\s*\)", t, re.I):
            pages.append(i)
    return pages


def section_pages(doc, q):
    """the question's opening page plus every following page up to the next section"""
    anchor = None
    for i, page in enumerate(doc):
        h = starts_heading(page.get_text())
        if h == (q[0], q[1]):
            anchor = i
            break
    if anchor is None:
        return question_pages(doc, q)
    pages = [anchor]
    for j in range(anchor + 1, len(doc)):
        if starts_heading(doc[j].get_text()) is not None:
            break
        pages.append(j)
    return pages


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 1
    key = sys.argv[1]
    pdf = os.path.join(PDF_DIR, key + "_ER_full.pdf")
    if not os.path.exists(pdf):
        print("no PDF for", key, "->", pdf)
        return 2
    doc = pymupdf.open(pdf)
    os.makedirs(OUT_DIR, exist_ok=True)

    if sys.argv[2] == "--all":
        targets = [None]
        name = key + "_ALL"
    else:
        q = re.sub(r"[^0-9a-g]", "", sys.argv[2].lower())
        targets = [(q[0], q[1])]
        name = f"{key}_{q[0]}{q[1]}"

    chunks = []
    for q in targets:
        pages = section_pages(doc, q) if q else question_pages(doc, None)
        if not pages:
            print("question not printed in report:", q)
            continue
        for i in pages:
            page = doc[i]
            scripts = page_scripts(page, doc)
            if not scripts:
                continue
            chunks.append(f"\n===== PAGE {i + 1} =====")
            for n, (xref, w, h, text) in enumerate(scripts, 1):
                chunks.append(f"\n--- script image {n} on page {i + 1} (xref {xref}, {w}x{h}) ---\n{text}")

    out = os.path.join(OUT_DIR, name + ".txt")
    header = (
        "# RAW OCR of scanned script facsimiles -- MACHINE OUTPUT, NOT A TRANSCRIPT.\n"
        "# Do not quote. Character-level errors are frequent (see the gloss pass).\n"
        f"# source: {os.path.basename(pdf)}\n"
        f"# target: {sys.argv[2]}\n"
    )
    with open(out, "w") as f:
        f.write(header + "\n".join(chunks) + "\n")
    print(out, len(chunks), "blocks")
    for c in chunks:
        print(c[:1500])
    return 0


if __name__ == "__main__":
    sys.exit(main())
