#!/usr/bin/env python3
"""Layer C — 9-mark Justify coverage, checked against the derived topics.

Checked in BOTH directions every run:
  * every block in the derived inventory (76, from the mark schemes) must map to
    an entry, or it prints as REMAINING;
  * every entry number named here must exist as a heading in 10_Chain_Bank.md,
    or it prints as a DANGLING reference.

Written because a topic LABEL absorbed a block it did not describe: entry 176 was
headed "venture capital vs a bank loan" and listed a block whose actual pair was
venture capital vs CROWDFUNDING. The label looked right and the block was wrong.
So the map below is keyed on BLOCK NUMBER, and `--audit` prints each block's real
option pair from the inventory next to the entry it is claimed by.

Run from Business_Studies_Answer_Bank/.
"""
import argparse
import csv
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
BANK = HERE / "Perfect_Answers" / "10_Chain_Bank.md"
TOPICS = HERE / "layer_c_9mark_topics.csv"

# block number -> entry number in 10_Chain_Bank.md
COVERED = {
    # ---- sources of finance: entries 175-187, the first cluster ----------
    1: 185, 4: 178, 12: 179, 22: 181, 31: 180, 38: 178, 46: 181,
    62: 182, 65: 186, 69: 177, 73: 176,
    # ---- promotion: entries 188-195, 202-204 ----------------------------
    5: 202, 17: 188, 18: 189, 24: 190, 27: 191, 37: 204, 39: 192,
    53: 193, 59: 194, 61: 195, 67: 204, 75: 203,
    # ---- pricing: entries 196-201 ---------------------------------------
    7: 196, 15: 197, 25: 198, 35: 199, 43: 197, 64: 197,
    66: 200, 70: 199, 71: 201,
}

EXPECTED_BLOCKS = 76


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--audit", action="store_true",
                    help="print every covered block with its real option pair")
    args = ap.parse_args()

    rows = list(csv.DictReader(TOPICS.open(encoding="utf-8")))
    bank = BANK.read_text(encoding="utf-8")
    entries = {int(m.group(1)) for m in re.finditer(r"^## (\d+)\.", bank, re.M)}

    by_n = {int(r["n"]): r for r in rows}
    remaining = [r for r in rows if int(r["n"]) not in COVERED]
    dangling = sorted({e for e in COVERED.values() if e not in entries})
    orphan = sorted(b for b in COVERED if b not in by_n)

    print("9-MARK JUSTIFY — COVERAGE")
    print("-" * 58)
    print(f"blocks in the tier        : {len(rows)}  (expected {EXPECTED_BLOCKS})")
    print(f"blocks covered            : {len(COVERED)}")
    print(f"REMAINING                 : {len(remaining)}")
    print(f"distinct option pairs     : {len({r['topic'] for r in rows})}")
    if len(rows) != EXPECTED_BLOCKS:
        print(f"*** BLOCK COUNT DRIFTED from {EXPECTED_BLOCKS}")
    if dangling:
        print(f"\n*** DANGLING entry references: {dangling}")
    if orphan:
        print(f"*** Block numbers not in the inventory: {orphan}")

    if args.audit:
        print("\nAUDIT — each covered block's REAL option pair against its entry")
        print("-" * 58)
        for b in sorted(COVERED):
            r = by_n.get(b)
            if not r:
                continue
            print(f"  block [{b:>2}] -> entry {COVERED[b]}   {r['session']} {r['paper']}")
            print(f"        topic: {r['topic']}")
            print(f"        O1: {r['option_1'][:86]}")
            print(f"        O2: {r['option_2'][:86]}")

    if remaining:
        print("\nREMAINING BLOCKS")
        print("-" * 58)
        for r in remaining:
            print(f"  [{r['n']:>2}] {r['session']:<15}{r['paper']:<4}{r['question']:<6} "
                  f"{r['topic'][:64]}")
    return 1 if (dangling or orphan or len(rows) != EXPECTED_BLOCKS) else 0


if __name__ == "__main__":
    sys.exit(main())
