#!/usr/bin/env python3
"""
verify_paper_craft.py -- the timing arithmetic in 13_Paper_Craft_and_Timing.md.

The claim that matters is Pearson's own: **1 hour 30 minutes for 80 marks**, and the cover page
telling candidates to spend time in proportion to the marks. Everything in that file follows from
those two numbers, so both are read out of all 38 archived question papers rather than remembered.

    1. all 38 QPs print "1 hour 30 minutes" and "total mark for this paper is 80"
    2. 90 minutes / 80 marks = 1.125 min per mark, and the four 20-mark questions consume it evenly
    3. the per-tariff times in the file are those arithmetic results, not typed-in numbers
    4. the running quarter totals sum to 90

    python3 verify_paper_craft.py
"""
import glob
import os
import re
import sys

import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
ARCHIVE = os.path.join(os.path.dirname(HERE), "Paperlords_Archive", "IGCSE", "4BS1_Business_Studies")
DOC = os.path.join(HERE, "Perfect_Answers", "13_Paper_Craft_and_Timing.md")

# 2021-2022 papers print the duration as a bare "1 hour 30 minutes" in the header grid, later
# ones as "Time: 1 hour 30 minutes". Both are the same claim.
TIME = re.compile(r"(?:Time\s*:?\s*)?(\d+)\s*hour[s]?\s*(\d{1,2})?\s*minutes?", re.I)
TOTAL = re.compile(r"total mark for this paper is\s*(\d+)", re.I)

EXPECT_TARIFF = {1: 1.125, 2: 2.25, 3: 3.375, 6: 6.75, 9: 10.125, 12: 13.5}


def main():
    fails = []
    files = sorted(glob.glob(os.path.join(ARCHIVE, "*", "*_QP.pdf")))
    ok, times = 0, set()
    for f in files:
        try:
            doc = pymupdf.open(f)
        except Exception as exc:                                   # noqa: BLE001
            fails.append(f"{os.path.basename(f)}: cannot open ({exc})")
            continue
        head = "".join(doc[i].get_text() for i in range(min(3, len(doc))))
        t = TIME.search(head)
        m = TOTAL.search(head)
        if not t:
            fails.append(f"{os.path.basename(f)}: no time on the cover")
            continue
        if not m:
            fails.append(f"{os.path.basename(f)}: no total-marks line")
            continue
        hours, minutes = int(t.group(1)), int(t.group(2) or 0)
        times.add((hours, minutes))
        if int(m.group(1)) != 80:
            fails.append(f"{os.path.basename(f)}: total {m.group(1)}, expected 80")
        ok += 1

    if len(files) != 38:
        fails.append(f"expected 38 question papers, found {len(files)}")
    if times != {(1, 30)}:
        fails.append(f"paper durations found: {sorted(times)}, expected only 1h30")

    # --- the arithmetic ---------------------------------------------------------------------
    rate = 90 / 80
    if abs(rate - 1.125) > 1e-9:
        fails.append(f"minutes per mark is {rate}")
    for tariff, expected in EXPECT_TARIFF.items():
        if abs(tariff * rate - expected) > 1e-9:
            fails.append(f"{tariff}-mark question costs {tariff * rate} min, expected {expected}")
    if abs(4 * 20 * rate - 90) > 1e-9:
        fails.append("four 20-mark questions do not consume 90 minutes")

    # --- the doc must state them ------------------------------------------------------------
    doc_text = open(DOC, encoding="utf-8").read()
    for phrase in ("1 hour 30 minutes", "80", "1.125 minutes per mark", "67.5 seconds",
                   "22½ min", "**~13½ min**", "**~6¾ min**"):
        if phrase not in doc_text:
            fails.append(f"the doc no longer states {phrase!r}")

    print(f"question papers read     : {ok} of {len(files)}")
    print(f"duration on every cover  : 1 hour 30 minutes")
    print(f"total marks every paper  : 80")
    print(f"exchange rate            : {rate:.3f} min per mark = {rate * 60:.1f} s")
    print(f"four 20-mark questions   : 22.5 min each = 90")
    print(f"per tariff (min)         : " +
          " · ".join(f"{k}→{v:g}" for k, v in EXPECT_TARIFF.items()))
    if fails:
        print("\nFAIL")
        for f in fails:
            print("   " + f)
        return 1
    print("\nRESULT: OK — the clock in 13_Paper_Craft_and_Timing.md is Pearson's own, read off all 38"
          " question papers, and every derived time recomputes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
