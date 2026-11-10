#!/usr/bin/env python3
"""
read_script.py -- cut one report page into readable images of the script it carries.

The reports print each marked script as a picture, so the text layer cannot help. A page render
resamples that picture; extracting the picture itself does not. This tool pulls Pearson's own
embedded image out of the PDF, stretches it to ~2x with contrast normalisation, and slices it into
overlapping bands, which is the closest thing to reading the page by eye.

    python3 audits/read_script.py 4BS1_01R_2506 34            # writes /tmp/rs_*.png
    python3 audits/read_script.py 4BS1_01R_2506 25 26         # several pages, numbered

Output is written outside the repo on purpose: these are rendered rasters of Pearson's page and do
not belong in Git. Read them with an image viewer, transcribe into audits/corpus/transcripts/.
"""
import io
import os
import sys

import pymupdf
from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_DIR = os.path.join(ROOT, "Sources", "Official_Pearson", "Full_Examiner_Reports")


def bands(img, parts=2, overlap=0.08):
    w, h = img.size
    step = h / parts
    for i in range(parts):
        top = max(0, int(i * step - h * overlap))
        bot = min(h, int((i + 1) * step + h * overlap))
        yield i + 1, img.crop((0, top, w, bot))


def main():
    key, pages = sys.argv[1], [int(x) for x in sys.argv[2:]]
    pdf = os.path.join(PDF_DIR, key + "_ER_full.pdf")
    if not os.path.exists(pdf):
        sys.exit(f"no stored report for {key}")
    doc = pymupdf.open(pdf)
    for page in pages:
        p = doc[page - 1]
        imgs = p.get_images(full=True)
        if not imgs:
            print(f"page {page}: no embedded image (the script, if any, is text or absent)")
            continue
        # the largest image is the script; the small ones are logos and rules
        best = max(imgs, key=lambda im: im[2] * im[3])
        pil = Image.open(io.BytesIO(doc.extract_image(best[0])["image"])).convert("L")
        pil = ImageOps.autocontrast(pil, cutoff=2)
        w, h = pil.size
        scale = 2.0 if w < 1200 else 1.5
        pil = pil.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
        parts = 2 if pil.size[1] < 2400 else 3
        for n, b in bands(pil, parts):
            out = f"/tmp/rs_{key}_p{page}_{n}.png"
            b.save(out)
            print(out, b.size)


if __name__ == "__main__":
    main()
