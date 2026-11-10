#!/usr/bin/env python3
"""
ocr_er_scripts.py -- make the scripts inside the examiner reports machine-readable.

WHY
    In 4BS1 examiner reports the candidate scripts are RASTER IMAGES; the text layer carries only
    the examiner's commentary. So a bank that quotes 148 scripts cannot be checked by text search.
    This OCRs the script pages once and caches them, so script quotations can be fuzzy-matched
    against the page they claim to come from.

WHAT IT WRITES
    audits/corpus/ocr/<report>.json   {page_number: [line, line, ...]}

USAGE
    python3 audits/ocr_er_scripts.py            # all reports not yet cached
    python3 audits/ocr_er_scripts.py --force    # redo
"""
import os, sys, json, glob
import fitz
from rapidocr_onnxruntime import RapidOCR

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "Sources", "Official_Pearson", "Full_Examiner_Reports")
OUT = os.path.join(ROOT, "audits", "corpus", "ocr")
os.makedirs(OUT, exist_ok=True)


def script_pages(doc):
    """Pages that carry a candidate script: a scored line plus more than one image."""
    keep = []
    for i, p in enumerate(doc):
        t = p.get_text()
        if ("This response" in t or "scored" in t or "ResultsPlus" in t) and len(p.get_images()) >= 2:
            keep.append(i)
    return keep


def main():
    ocr = RapidOCR()
    for f in sorted(glob.glob(os.path.join(SRC, "*.pdf"))):
        name = os.path.basename(f)[:-4]
        dst = os.path.join(OUT, name + ".json")
        if os.path.exists(dst) and "--force" not in sys.argv:
            print("cached ", name)
            continue
        doc = fitz.open(f)
        pages = script_pages(doc)
        data = {}
        for i in pages:
            pix = doc[i].get_pixmap(dpi=200)
            tmp = f"/tmp/_ocr_{os.getpid()}.png"
            pix.save(tmp)
            res, _ = ocr(tmp)
            data[i + 1] = [r[1] for r in (res or [])]
            print(f"  {name} p{i+1}: {len(data[i+1])} lines")
        json.dump(data, open(dst, "w"), indent=1)
        print("wrote ", dst, len(pages), "pages")


if __name__ == "__main__":
    main()
