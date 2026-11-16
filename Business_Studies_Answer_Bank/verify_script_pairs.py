#!/usr/bin/env python3
"""
verify_script_pairs.py -- two falsifiers for the script manifest.

`audits/corpus/scripts.json` says, for each picture in each examiner report, which score line belongs
to it. Every "this is a 6/6" claim in the bank is downstream of that pairing, so it needs a check
that does not depend on how the pairing was made.

Two checks, both of which can only fail:

  1. THE LINE MUST BE ON THE PAGE IT CLAIMS. Every recorded score line is looked up in the text layer
     of `marked_on_page` (or the picture's own page). A pairing that invented, paraphrased or
     misplaced a line fails here.

  2. THE MARK MUST BE POSSIBLE. The question paper prints the tariff. A script cannot score 12 on a
     6-mark question. Where the manifest exceeds the paper's tariff, either the pairing is wrong or
     Pearson's report prints a score above the tariff -- and the second is a fact worth knowing, so
     the handful of known cases are listed below rather than silently tolerated.

    python3 verify_script_pairs.py
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "audits"))
import pymupdf      # noqa: E402
import qp_stems     # noqa: E402

ROOT = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.join(ROOT, "audits", "corpus")
PDF_DIR = os.path.join(ROOT, "Sources", "Official_Pearson", "Full_Examiner_Reports")

SESSION = {"2206": "May-June_2022", "2306": "May_2023", "2406": "May-June_2024",
           "2506": "May-June_2025", "2606": "June_2026"}

# Score lines Pearson prints ABOVE the tariff of the question they are printed under. Read by eye:
# each one says "2 marks" (or "02 mark.") for a question the paper prints as (1). They are left as
# printed -- the manifest must never edit Pearson -- and they are listed so that a NEW one is a
# failure rather than a silent pass.
ABOVE_TARIFF_AS_PRINTED = {
    ("4BS1_01R_2506", 6, "1(d)"),
    ("4BS1_01R_2506", 17, "2(b)"),
    ("4BS1_01R_2606", 14, "2(b)"),
    ("4BS1_01_2406", 15, "2(b)"),
}


def paper_of(key):
    m = re.match(r"4BS1_(0[12]R?)_(\d{2})(\d{2})", key)
    if not m:
        return None
    comp, yy, mm = m.group(1), m.group(2), m.group(3)
    folder = SESSION.get(yy + mm)
    if not folder:
        return None
    return f"4BS1_{folder}_P{comp[1]}{'R' if comp.endswith('R') else ''}"


def main():
    data = json.load(open(os.path.join(CORPUS, "scripts.json"), encoding="utf-8"))
    docs = {k: pymupdf.open(os.path.join(PDF_DIR, k + "_ER_full.pdf")) for k in data}
    missing, impossible, allowed, checked, tariff_checked = [], [], [], 0, 0
    for key, rows in data.items():
        doc = docs[key]
        pid = paper_of(key)
        stems = qp_stems.stems_for(pid) if pid else {}
        for r in rows:
            if r.get("mark_value") is None:
                continue
            checked += 1
            page = r.get("marked_on_page") or r["page"]
            text = re.sub(r"\s+", " ", doc[page - 1].get_text())
            if re.sub(r"\s+", " ", r["mark_line"]) not in text:
                missing.append((key, r["page"], page, r["mark_line"]))
            tariff = (stems.get(r["question"]) or {}).get("marks")
            if tariff is None:
                continue
            tariff_checked += 1
            if r["mark_value"] > tariff:
                if (key, page, r["question"]) in ABOVE_TARIFF_AS_PRINTED:
                    allowed.append((key, page, r["question"], r["mark_value"], tariff))
                else:
                    impossible.append((key, page, r["question"], r["mark_value"], tariff,
                                       r["mark_line"]))
    print(f"pairings with a mark : {checked}")
    print(f"checked against the paper's printed tariff : {tariff_checked}")
    print(f"score lines NOT found on the page they claim : {len(missing)}")
    for m in missing[:10]:
        print("   ", m)
    print(f"marks above the paper's tariff, known and read : {len(allowed)}")
    for a in allowed:
        print(f"    {a[0]} p{a[1]} Q{a[2]}: report prints {a[3]}, paper prints {a[4]}")
    print(f"UNEXPLAINED marks above tariff : {len(impossible)}")
    for i in impossible:
        print("   ", i)
    ok = not missing and not impossible
    print("\nRESULT: OK — every pairing cites a line that exists on the page it names, and no mark"
          " exceeds its question's tariff except where Pearson's own report does."
          if ok else "\nRESULT: FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
