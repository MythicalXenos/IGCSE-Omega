#!/usr/bin/env python3
"""Layer C coverage check for the 12-mark Evaluate bank (the last tier).

38 blocks - one 4(c) per paper, 38 papers. Carried by entries 228-252 of
`Perfect_Answers/10_Chain_Bank.md`.

Reads `layer_c_12mark_inventory.csv` (built by `build_layer_c_12mark_inventory.py`
from `layer_c_12mark_blocks.txt`) and checks the map BOTH ways:

  * every block has an entry (nothing missed)
  * every entry number claimed exists as a heading in the chain bank
    (nothing dangling - the failure mode that let Batch 5b over-claim)

Block numbers are positional: index into the block file, ordered by session then
by paper (P1R, P1, P2R, P2 - the archive's file-name sort). **Regenerating the
block file keeps that order** - verified after the May/June 2024 MS label fix by
diffing the `===` header lines (0 differences).

Run from Business_Studies_Answer_Bank/ (NOT from Perfect_Answers/).
"""
import csv
import re
import sys
from pathlib import Path

BANK = Path(__file__).resolve().parent
TOPICS = BANK / "layer_c_12mark_inventory.csv"
CHAIN = BANK / "Perfect_Answers" / "10_Chain_Bank.md"

# block number -> entry number in 10_Chain_Bank.md
COVERED = {
    # ---- 228-230: the scaffold, quality and TQM -------------------------
    2: 229, 14: 229, 22: 229,
    35: 230,
    # ---- 231: location, the largest family (4 papers) -------------------
    8: 231, 9: 231, 21: 231, 31: 231,
    # ---- 232-233: research ----------------------------------------------
    6: 232, 19: 232,
    26: 233, 32: 233,
    # ---- 234-235: marketing and promotion -------------------------------
    17: 234, 20: 234,
    5: 235, 34: 235,
    # ---- 236-237: the market --------------------------------------------
    3: 236, 12: 236, 24: 236,
    7: 237, 18: 237,
    # ---- 238-239: measuring success -------------------------------------
    11: 238, 13: 238,
    36: 239,
    # ---- 240-241: social objectives and public relations ---------------
    1: 240, 33: 240,
    25: 241,
    # ---- 242-246: orientation, segmentation, structure, franchise ------
    4: 242,
    30: 243,
    10: 244,
    38: 245,
    37: 246,
    # ---- 247-252: finance, motivation, communication -------------------
    15: 247,
    27: 248,
    29: 249,
    23: 250,
    28: 251,
    16: 252,
}


def main() -> int:
    argv = sys.argv[1:]
    rows = list(csv.DictReader(TOPICS.open(encoding="utf-8")))
    total = len(rows)
    covered = [b for b in COVERED if b <= total]
    missing = [b for b in range(1, total + 1) if b not in COVERED]
    orphan = sorted(b for b in COVERED if b > total)

    text = CHAIN.read_text(encoding="utf-8")
    entries = {int(m.group(1)) for m in re.finditer(r"^## (\d+)\.", text, re.M)}
    dangling = sorted({e for e in COVERED.values() if e not in entries})

    print("12-MARK EVALUATE — COVERAGE")
    print("-" * 58)
    print(f"blocks in the tier        : {total}  (expected 38)")
    print(f"blocks covered            : {len(covered)}")
    print(f"REMAINING                 : {len(missing)}")
    if missing:
        print("  blocks with no entry yet:")
        for b in missing:
            r = rows[b - 1]
            print(f"    [{b:2d}] {r['Session']:14s} {r['Paper']:4s} {r['Topic'][:34]:34s} {r['Stem'][:60]}")
    print(f"entries claimed           : {len(set(COVERED.values()))} distinct")
    print(f"dangling entries          : {dangling if dangling else 'none'}")
    print(f"orphan block numbers      : {orphan if orphan else 'none'}")

    if "--audit" in argv:
        print()
        print("AUDIT — each covered block's own stem beside the entry claiming it")
        print("-" * 58)
        for b in sorted(COVERED):
            if b > total:
                continue
            r = rows[b - 1]
            print(f"  block [{b:2d}] -> entry {COVERED[b]}   {r['Session']} {r['Paper']}")
            print(f"        {r['Stem'][:104]}")
        return 0

    return 1 if (missing or dangling) else 0


if __name__ == "__main__":
    sys.exit(main())
