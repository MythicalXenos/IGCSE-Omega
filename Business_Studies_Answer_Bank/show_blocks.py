#!/usr/bin/env python3
"""Print Layer C mark-scheme blocks with the boilerplate stripped.

Every mark-scheme block ends with the SAME four level descriptors for its
tariff. Across 114 six-mark blocks that is well over half the file, and it says
nothing about the question. This prints the part that does: the stem, the AO2
application points and the AO3 chains.

    python3 show_blocks.py 6 12 26      # blocks 12..26 of the 6-mark file
    python3 show_blocks.py 9 --all
"""
import argparse
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent

# The descriptor table is identical in every block of a tariff. Cut it.
BOILER = re.compile(r"Level Mark Descriptor.*$", re.S)


def load(tier: int) -> list[tuple[str, str]]:
    f = HERE / f"layer_c_{tier}mark_blocks.txt"
    if not f.exists():
        sys.exit(f"missing {f.name} -- run: python3 extract_ms_blocks.py {tier}")
    parts = re.split(r"\n={78}\n=== (.+?)\n={78}\n", f.read_text(encoding="utf-8"))[1:]
    return [(h, BOILER.sub("", b).strip()) for h, b in zip(parts[0::2], parts[1::2])]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("tier", type=int, choices=[3, 6, 9, 12])
    ap.add_argument("start", nargs="?", type=int, default=1)
    ap.add_argument("end", nargs="?", type=int, default=1)
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()

    rows = load(args.tier)
    lo = 1 if args.all else max(1, args.start)
    hi = len(rows) if args.all else min(len(rows), args.end)
    print(f"{len(rows)} blocks of {args.tier} marks; showing {lo}-{hi}\n")
    for i in range(lo, hi + 1):
        head, body = rows[i - 1]
        print(f"\n{'#' * 76}\n# [{i}] {head}\n{'#' * 76}\n{body}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
