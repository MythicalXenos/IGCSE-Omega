#!/usr/bin/env python3
"""
script_images.py -- dump the scanned script facsimiles for one question as PNGs.

The examiner reports print each candidate script as a scanned image. Handwriting
defeats OCR (rapidocr is print-trained), so the reliable route is to write each
facsimile out as a 2x PNG and read it as an image.

Usage:
    python3 audits/script_images.py <corpus-key> <question> [--all-questions]

Example:
    python3 audits/script_images.py 4BS1_01R_2506 2(d)

Outputs PNGs in audits/corpus/scripts_png/ and prints, per page, the examiner's
commentary text (which carries the marks) so each image can be tied to a score.
"""
import os
import re
import sys

import cv2
import numpy as np
import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ocr_scripts import PDF_DIR, QHEAD, section_pages, starts_heading  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "corpus", "scripts_png")
MIN_WIDTH = 500
SCALE = 2


def dump(key, q):
    pdf = os.path.join(PDF_DIR, key + "_ER_full.pdf")
    if not os.path.exists(pdf):
        print("NO PDF HELD for", key)
        return []
    os.makedirs(OUT_DIR, exist_ok=True)
    doc = pymupdf.open(pdf)
    pages = section_pages(doc, q) if q else list(range(len(doc)))
    written = []
    for i in pages:
        page = doc[i]
        text = page.get_text().strip()
        wide = [im for im in page.get_images(full=True) if im[2] >= MIN_WIDTH]
        if not wide:
            continue
        print(f"\n===== PAGE {i + 1} =====")
        print(text[:1200])
        for n, im in enumerate(wide, 1):
            xref = im[0]
            pix = pymupdf.Pixmap(doc, xref)
            if pix.n - pix.alpha >= 3:
                pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
            a = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
            g = cv2.cvtColor(a, cv2.COLOR_RGB2GRAY) if pix.n >= 3 else a[:, :, 0]
            up = cv2.resize(g, None, fx=SCALE, fy=SCALE, interpolation=cv2.INTER_CUBIC)
            tag = f"{q[0]}{q[1]}" if q else "ALL"
            path = os.path.join(OUT_DIR, f"{key}_{tag}_p{i + 1}_{n}.png")
            cv2.imwrite(path, up)
            written.append(path)
            print(f"  [image] {path}")
    return written


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    key = sys.argv[1]
    if len(sys.argv) >= 3 and sys.argv[2] != "--all-questions":
        q = re.sub(r"[^0-9a-g]", "", sys.argv[2].lower())
        out = dump(key, (q[0], q[1]))
        print(f"\n{len(out)} image(s)")
        return 0
    # every question the report prints
    pdf = os.path.join(PDF_DIR, key + "_ER_full.pdf")
    doc = pymupdf.open(pdf)
    seen = []
    for page in doc:
        h = starts_heading(page.get_text())
        if h and h not in seen:
            seen.append(h)
    for q in seen:
        dump(key, q)
    return 0


if __name__ == "__main__":
    sys.exit(main())
