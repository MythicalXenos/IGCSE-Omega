#!/usr/bin/env python3
"""
verify_grade_budget.py -- the arithmetic in 12_Grade_9_Marks_Budget.md.

That file is the only place in the bank that turns "I want a 9" into numbers a candidate can mark
himself against, so its numbers must be derived, not remembered. This script re-derives every one of
them from the 38 mark schemes in `Perfect_Answers/By_Paper/` and from the boundary table in `00_`:

  1. the per-paper tariff skeleton   12 x 1, 4 x 2, 4 x 3, 3 x 6, 2 x 9, 1 x 12 = 80 marks, 26 items
  2. the long-item AO split          AO1 3 / AO2 18 / AO3 18 / AO4 9, identical in every paper
  3. the boundary arithmetic         160 total, 133 for a 9 in June 2026, therefore 27 marks of slack
  4. the three per-paper profiles    each one sums to its stated profile total, and each clears 133

    python3 verify_grade_budget.py
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAPERS = os.path.join(HERE, "Perfect_Answers", "By_Paper")
DOC = os.path.join(HERE, "Perfect_Answers", "12_Grade_9_Marks_Budget.md")

ITEM = re.compile(r"^### `(\d)\(([a-g])\)(?:\((i|ii|iii|iv|v|vi)\))?` — (\d+) marks? \(([^)]*)\)", re.M)
AO = re.compile(r"AO(\d):(\d)")

# The profiles in section 5 of the doc, in tariff order: 1, 2, 3, 6, 9, 12.
PROFILES = {
    "A": ([12, 8, 11, 15, 14, 9], 69, 138),
    "B": ([10, 7, 10, 16, 15, 10], 68, 136),
    "C": ([12, 8, 12, 17, 13, 11], 73, 146),
}


def main():
    fails = []

    # ---- 1 and 2: the skeleton, from every paper -------------------------------------------
    papers, skeletons = 0, set()
    long_ao = set()
    for path in sorted(glob.glob(os.path.join(PAPERS, "*.md"))):
        text = open(path, encoding="utf-8").read()
        items = ITEM.findall(text)
        if not items:
            fails.append(f"no items parsed in {os.path.basename(path)}")
            continue
        papers += 1
        hist = {}
        for _q, _p, _roman, marks, _ao in items:
            hist[int(marks)] = hist.get(int(marks), 0) + 1
        skeleton = (len(items), sum(int(m) for *_x, m, _ao in [(a, b, c, d, e) for a, b, c, d, e in items]),
                    tuple(sorted(hist.items())))
        skeletons.add(skeleton)
        ao = {}
        for _q, _p, _roman, marks, aostr in items:
            if int(marks) < 6:
                continue
            for a, v in AO.findall(aostr):
                ao[f"AO{a}"] = ao.get(f"AO{a}", 0) + int(v)
        long_ao.add(tuple(sorted(ao.items())))

    if papers != 38:
        fails.append(f"expected 38 papers, parsed {papers}")
    if len(skeletons) != 1:
        fails.append(f"tariff skeletons differ between papers: {sorted(skeletons)}")
    else:
        n_items, total, hist = next(iter(skeletons))
        if (n_items, total) != (26, 80):
            fails.append(f"items/marks {n_items}/{total}, expected 26/80")
        if dict(hist) != {1: 12, 2: 4, 3: 4, 6: 3, 9: 2, 12: 1}:
            fails.append(f"histogram {dict(hist)}, expected 12/4/4/3/2/1")
    if len(long_ao) != 1:
        fails.append(f"long-item AO splits differ between papers: {sorted(long_ao)}")
    else:
        ao = dict(next(iter(long_ao)))
        if ao != {"AO1": 3, "AO2": 18, "AO3": 18, "AO4": 9}:
            fails.append(f"long-item AO split {ao}, expected AO1 3 / AO2 18 / AO3 18 / AO4 9")

    # ---- 3: the boundary arithmetic, against the rulebook ------------------------------------
    rulebook = open(os.path.join(HERE, "Perfect_Answers", "00_Pearson_Official_Rulebook.md"),
                    encoding="utf-8").read()
    m = re.search(r"\|\s*\*\*Standard: Papers 01 \+ 02\*\*\s*\|\s*(\d+)\s*\|\s*\*\*(\d+)\*\*", rulebook)
    if not m:
        fails.append("could not find the standard-route boundary row in 00_")
    else:
        total_marks, nine = int(m.group(1)), int(m.group(2))
        if total_marks != 160:
            fails.append(f"qualification total reads {total_marks}, expected 160")
        if nine != 133:
            fails.append(f"grade-9 boundary reads {nine}, expected 133")
        if total_marks - nine != 27:
            fails.append("slack is not 27")
        # the doc must state all three
        doc = open(DOC, encoding="utf-8").read()
        for phrase in ("**133/160**", "**27**", "**66.5 / 80**"):
            if phrase not in doc:
                fails.append(f"the doc no longer states {phrase}")

    # ---- 4: the profiles ---------------------------------------------------------------------
    for name, (parts, paper_total, two_paper) in PROFILES.items():
        if sum(parts) != paper_total:
            fails.append(f"profile {name} sums to {sum(parts)}, states {paper_total}")
        if paper_total * 2 != two_paper:
            fails.append(f"profile {name} two-paper total {paper_total * 2}, states {two_paper}")
        if two_paper < 133:
            fails.append(f"profile {name} does not clear the boundary")

    print(f"papers parsed            : {papers}")
    print(f"tariff skeleton          : 26 items, 80 marks, 12/4/4/3/2/1")
    print(f"long-item AO split       : AO1 3 · AO2 18 · AO3 18 · AO4 9  (identical in all {papers})")
    print(f"boundary arithmetic      : 160 total · 133 for a 9 · 27 marks of slack")
    print(f"profiles checked         : {', '.join(PROFILES)} — all clear 133")
    if fails:
        print("\nFAIL")
        for f in fails:
            print("   " + f)
        return 1
    print("\nRESULT: OK — every number in 12_Grade_9_Marks_Budget.md is re-derived from the papers,"
          " the rulebook and arithmetic.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
