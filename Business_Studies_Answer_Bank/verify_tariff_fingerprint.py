#!/usr/bin/env python3
"""
verify_tariff_fingerprint.py -- the AO composition of every tariff, from all 38 mark schemes.

`15_Tariff_Fingerprint.md` claims that the tariff in brackets predicts the assessment objectives and
the command word. That claim is only worth making if it is derived, so this script reads the AO label
and the question stem of all 988 items in `Perfect_Answers/By_Paper/` and prints:

    tariff | items | AO totals | AO per paper | command words in the stem

and then checks the six claims in the file against what it printed:

  1. every 3-mark item is AO1 only, and every one is an "Explain"
  2. every 6-mark item is AO2 + AO3, with no AO1 and no AO4, and every one is an "Analyse"
  3. every 9-mark item is AO2 + AO3 + AO4, with no AO1, and every one is a "Justify"
  4. every 12-mark item is AO1 + AO2 + AO3 + AO4, and every one is an "Evaluate"
  5. every 2-mark item is AO2 only
  6. the per-paper AO totals of the long tariffs are constant; the 1-mark split is not

    python3 verify_tariff_fingerprint.py
"""
import collections
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAPERS = os.path.join(HERE, "Perfect_Answers", "By_Paper")
DOC = os.path.join(HERE, "Perfect_Answers", "15_Tariff_Fingerprint.md")

ITEM = re.compile(
    r"^### `(\d)\(([a-g])\)(?:\((i|ii|iii|iv|v|vi)\))?` — (\d+) marks? \(([^)]*)\)\n\n"
    r"\*\*Question:\*\*\s*(.+)$", re.M)
AO = re.compile(r"AO(\d):(\d)")

# MARKS, not items: a 9-mark item carries 3 AO2 marks, 3 AO3 and 3 AO4.
EXPECT_AO = {
    2: {"AO2": 304},
    3: {"AO1": 456},
    6: {"AO2": 342, "AO3": 342},
    9: {"AO2": 228, "AO3": 228, "AO4": 228},
    12: {"AO1": 114, "AO2": 114, "AO3": 114, "AO4": 114},
}
EXPECT_VERB = {3: "explain", 6: "analyse", 9: "justify", 12: "evaluate"}


def verb(stem):
    words = re.sub(r"^[\x00-\x1f\s]+", "", stem).strip().split()
    return words[0].rstrip(".,:").lower() if words else "?"


def main():
    fails = []
    ao_total = collections.Counter()
    per_paper_long = collections.defaultdict(set)
    verbs = collections.defaultdict(collections.Counter)
    items = 0
    one_mark_profiles = collections.Counter()

    for path in sorted(glob.glob(os.path.join(PAPERS, "*.md"))):
        text = open(path, encoding="utf-8").read()
        long_ao = collections.Counter()
        one_ao = collections.Counter()
        for _q, _p, _roman, marks, aostr, stem in ITEM.findall(text):
            marks = int(marks)
            items += 1
            verbs[marks][verb(stem)] += 1
            pairs = AO.findall(aostr)
            for a, v in pairs:
                ao_total[(marks, "AO" + a)] += int(v)
                if marks >= 6:
                    long_ao["AO" + a] += int(v)
            if marks == 1:
                for a, v in pairs:
                    one_ao["AO" + a] += int(v)
        if long_ao:
            per_paper_long[tuple(sorted(long_ao.items()))].add(os.path.basename(path))
        if one_ao:
            one_mark_profiles[tuple(sorted(one_ao.items()))] += 1

    if items != 988:
        fails.append(f"parsed {items} items, expected 988")

    # --- 1-5: AO composition and verb, tariff by tariff --------------------------------------
    for tariff, expected in EXPECT_AO.items():
        got = {k[1]: v for k, v in ao_total.items() if k[0] == tariff}
        if got != expected:
            fails.append(f"{tariff}-mark AO totals {got}, expected {expected}")
        if tariff in EXPECT_VERB:
            want = EXPECT_VERB[tariff]
            others = {v: c for v, c in verbs[tariff].items() if v != want}
            if others:
                fails.append(f"{tariff}-mark items not starting '{want}': {others}")

    # --- 6: long tariffs constant per paper, 1-mark split not --------------------------------
    if len(per_paper_long) != 1:
        fails.append(f"long-tariff AO split differs between papers: {sorted(per_paper_long)[:3]}")
    if len(one_mark_profiles) < 2:
        fails.append("the 1-mark AO split is constant across papers, contrary to the doc")

    # --- the doc must state the findings it claims ------------------------------------------
    doc = open(DOC, encoding="utf-8").read()
    for phrase in ("AO1 274 · AO2 181", "AO2 304", "AO1 456", "AO2 342 · AO3 342", "no AO1, no AO4", "no AO1",
                   "AO1 114 · AO2 114 · AO3 114 · AO4 114", "7 AO1 + 5 AO2", "P1R 1(vi)"):
        if phrase not in doc:
            fails.append(f"the doc no longer states {phrase!r}")

    # --- print ---------------------------------------------------------------------------------
    print(f"items read : {items}")
    print(f"{'tariff':>6} {'items':>6}  {'AO totals':38} {'command words'}")
    for t in sorted(verbs):
        got = {k[1]: v for k, v in sorted(ao_total.items()) if k[0] == t}
        ao = "  ".join(f"{k} {v}" for k, v in sorted(got.items())) or "—"
        vb = ", ".join(f"{k} {v}" for k, v in verbs[t].most_common(4))
        print(f"{t:>6} {sum(verbs[t].values()):>6}  {ao:38} {vb}")
    print("\nper-paper long-tariff AO split : " +
          (" · ".join(f"{k}" for k in [dict(next(iter(per_paper_long)))] )))
    print("1-mark AO profiles across papers : " +
          " · ".join(f"{dict(k)} x{v}" for k, v in one_mark_profiles.most_common()))

    if fails:
        print("\nFAIL")
        for f in fails:
            print("   " + f)
        return 1
    print("\nRESULT: OK — every claim in 15_Tariff_Fingerprint.md is derived from the 988 items:"
          " 3/6/9/12 each carry one fixed AO set and one command word, and the 1-mark split varies.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
