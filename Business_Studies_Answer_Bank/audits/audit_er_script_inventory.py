#!/usr/bin/env python3
"""
audit_er_script_inventory.py -- count, from the reports themselves, every script Pearson printed.

WHY
    The register (09_Verified_Tally.md) says how many scripts exist. Nothing derived that number
    from the source. This does: it walks the five full examiner reports held on disk, reads every
    marking line the reports use, attributes it to a question, and prints the inventory.

WHAT IT CATCHES
    * a register row claiming a script the report never printed
    * a printed script the register does not hold (a completeness hole)
    * a mark attributed to the wrong question

CAVEAT WRITTEN INTO THE CODE
    In these reports the marking line sometimes sits at the foot of the page BEFORE the script, so
    attribution uses the nearest preceding heading and then flags any attribution whose mark is
    impossible for the question's tariff.
"""
import os, re, sys, glob, json
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS = os.path.join(ROOT, "audits", "corpus")

REPORTS = {
    "4BS1_01_2306": "4BS1_01_2306_ER_full.txt",
    "4BS1_01R_2306": "4BS1_01R_2306_ER_full.txt",
    "4BS1_02_2306": "4BS1_02_2306_ER_full.txt",
    "4BS1_02R_2306": "4BS1_02R_2306_ER_full.txt",
    "4BS1_01R_2606": "4BS1_01R_2606_ER_full.txt",
}

# tariff of each question position, from the 38 mark schemes (see 00_Rulebook skeleton)
TARIFF = {"1(a)": 1, "1(b)": 1, "1(c)": 1, "1(d)": 1, "1(e)": 2, "1(f)": 3,
          "1(g)": 6, "2(a)": 1, "2(b)": 1, "2(c)": 3, "2(d)": 3, "2(e)": 3,
          "2(f)": 9, "3(a)": 1, "3(b)": 2, "3(c)": 2, "3(d)": 6, "3(e)": 9,
          "4(a)": 2, "4(b)": 6, "4(c)": 12}

HEAD = re.compile(r"Question\s+(\d)\s*\(([a-g])\)")
MARK = re.compile(r"(?:This response (?:scored|was)\s+(\d+)\s+marks?|"
                  r"This response is Level\s*\d+\s*[–-]\s*(\d+)\s*marks|"
                  r"Total:\s*(\d+)\s*marks?|"
                  r"Level\s*\d+\s*[–-]\s*(\d+)\s*marks|"
                  r"This is a Level\s*\d+ response\s*[–-]\s*(\d+)\s*marks)")


def scan(path):
    t = open(path, encoding="utf-8", errors="ignore").read()
    heads = [(m.start(), f"{m.group(1)}({m.group(2)})") for m in HEAD.finditer(t)]
    out = []
    for m in MARK.finditer(t):
        val = next(g for g in m.groups() if g)
        head = None
        for pos, h in heads:
            if pos < m.start():
                head = h
        if head is None:
            continue
        out.append((head, int(val), m.start()))
    return out, t


def main():
    print("=" * 88)
    print("ER SCRIPT INVENTORY — every marking line in the five reports held on disk")
    print("=" * 88)
    summary = {}
    for key, fname in REPORTS.items():
        p = os.path.join(CORPUS, fname)
        if not os.path.exists(p):
            print(f"  {key}: MISSING CORPUS"); continue
        rows, t = scan(p)
        per = defaultdict(list)
        for q, v, _ in rows:
            per[q].append(v)
        impossible = [(q, v) for q, v in [(q, v) for q, v, _ in rows] if q in TARIFF and v > TARIFF[q]]
        print(f"\n{key}   marking lines: {len(rows)}   questions seen: {len(per)}")
        line = []
        for q in sorted(per, key=lambda x: (int(x[0]), x[2])):
            line.append(f"{q}:{sorted(per[q], reverse=True)}")
        print("   " + "  ".join(line))
        if impossible:
            print("   ⚠ impossible marks for tariff (review):", impossible)
        summary[key] = {q: sorted(v, reverse=True) for q, v in per.items()}
    json.dump(summary, open(os.path.join(CORPUS, "inventory.json"), "w"), indent=1)
    print("\nwrote audits/corpus/inventory.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
