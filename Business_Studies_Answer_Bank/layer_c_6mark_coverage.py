#!/usr/bin/env python3
"""Layer C — 6-mark Analyse coverage, checked against the derived inventory.

WHY THIS EXISTS
---------------
The 3-mark tier was tracked by a `COVERED` map and that map drifted: Batch 5b
was recorded as covering twelve blocks when it covered eight, and four blocks
sat uncovered until the block file was read against the entry list by hand.
**A hand-carried coverage claim is how a question quietly goes missing.**

So the map below is checked in BOTH directions every run:
  * every block in the derived inventory (114, from the mark schemes) must map to
    an entry, or it is printed as REMAINING;
  * every entry number named here must actually exist as a heading in
    `10_Chain_Bank.md`, or it is printed as a DANGLING reference.

Run from Business_Studies_Answer_Bank/. Never re-type the totals by hand.
"""
import csv
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
BANK = HERE / "Perfect_Answers" / "10_Chain_Bank.md"
INV = HERE / "layer_c_6mark_inventory.csv"

# block number -> entry number in 10_Chain_Bank.md
COVERED = {
    # June 2026 — entries 101-112, in block order
    **{b: 100 + b for b in range(1, 13)},
    # May-June 2019
    13: 113, 14: 114, 15: 115, 16: 116, 17: 117, 18: 118, 19: 119,
    20: 128, 21: 129, 22: 130, 23: 131, 24: 111,
    # May-June 2020
    25: 120, 26: 131, 27: 121, 28: 122, 29: 123, 30: 124,
    31: 125, 32: 117, 33: 126, 34: 131, 35: 120, 36: 127,
    # May-June 2021
    37: 132, 38: 117, 39: 115, 40: 133, 41: 134, 42: 135,
    # May-June 2022
    43: 136, 44: 129, 45: 137, 46: 138, 47: 139, 48: 118,
    49: 122, 50: 140, 51: 141, 52: 108, 53: 114, 54: 142,
    # May-June 2024
    55: 118, 56: 143, 57: 123, 58: 139, 59: 144, 60: 145,
    61: 116, 62: 146, 63: 147, 64: 111, 65: 135, 66: 148,
    # May-June 2025
    67: 149, 68: 150, 69: 151, 70: 152, 71: 150, 72: 153,
    73: 108, 74: 154, 75: 142, 76: 155, 77: 156, 78: 127,
    # May 2023
    79: 139, 80: 157, 81: 144, 82: 125, 83: 117, 84: 158,
    85: 129, 86: 159, 87: 160, 88: 161, 89: 162, 90: 114,
}


def main() -> int:
    rows = list(csv.DictReader(INV.open(encoding="utf-8")))
    total = len(rows)
    bank = BANK.read_text(encoding="utf-8")
    entries = {int(m.group(1)) for m in re.finditer(r"^## (\d+)\.", bank, re.M)}

    remaining = [r for r in rows if int(r["n"]) not in COVERED]
    dangling = sorted({e for e in COVERED.values() if e not in entries})
    orphan = sorted({b for b in COVERED if b > total})

    print("6-MARK ANALYSE — COVERAGE")
    print("-" * 58)
    print(f"blocks in the tier        : {total}")
    print(f"blocks covered            : {total - len(remaining)}")
    print(f"REMAINING                 : {len(remaining)}")
    print(f"entries written (1-100 3-mark + 6-mark) : {len(entries)}")
    if dangling:
        print(f"\n*** DANGLING entry references: {dangling}")
    if orphan:
        print(f"*** Block numbers past the end of the inventory: {orphan}")

    if remaining:
        print("\nREMAINING BLOCKS")
        print("-" * 58)
        for r in remaining:
            print(f"  [{r['n']:>3}] {r['session']:<15}{r['paper']:<4}{r['question']:<6} "
                  f"{r['stem'][:88]}")
    return 1 if (dangling or orphan) else 0


if __name__ == "__main__":
    sys.exit(main())
