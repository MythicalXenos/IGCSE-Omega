#!/usr/bin/env python3
"""Derive the word-collision cluster total from the cluster table itself.

WHY THIS EXISTS
---------------
**The collision total has drifted three times, because it was incremented by hand
in four different files.**

    rule 74's table                 13 terms
    rule 78 says "now 15"           +2, but one of the two ("secondary sector")
                                      is ALREADY row 5 of rule 74
    rule 109's summary says "19"     the right total, but it names
                                      "current liabilities", which is not a row
                                      in the table above it
    `08_` and the Nov 2025 addendum  say "19 → 22", adding "trade bloc ·
    say "19 → 22"                    job production · share capital" — and TWO
                                      of those three were already in rule 74

**Every one of those figures was correct when it was typed, and none of them
survived the next addition.** That is the same failure mode as the coverage
tables and the exemplar register, and it has the same cure: **one table, one
count, derived.**

The count is the number of rows in the table under
`## 74. ... THE WORD-COLLISION CLUSTER` in `06_External_Source_Library.md`.
Nothing else is authoritative; every other mention in the bank points here.

Run from Business_Studies_Answer_Bank/:  python3 verify_collision_cluster.py
Exit code 0 when the file's stated total equals the table's row count, 1 when not.
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / "Perfect_Answers" / "06_External_Source_Library.md"
STATED = re.compile(r"THE CLUSTER STANDS AT \*\*(\d+)\*\*")


def table_rows(text: str) -> list:
    """Data rows of the table under rule 74's heading."""
    m = re.search(r"^## 74\. .*?THE WORD-COLLISION CLUSTER(.*?)(?=\n## 75\.)",
                  text, re.S | re.M)
    if not m:
        sys.exit("rule 74's heading was not found — the anchor text has changed")
    rows = []
    for line in m.group(1).splitlines():
        if not line.startswith("|") or set(line) <= set("|-: "):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 3 or cells[0].lower().startswith("term"):
            continue
        rows.append(cells)
    return rows


def main() -> int:
    text = SRC.read_text(encoding="utf-8")
    rows = table_rows(text)
    terms = [r[0] for r in rows]

    print("=" * 70)
    print("WORD-COLLISION CLUSTER — derived from rule 74's table")
    print("=" * 70)
    for i, r in enumerate(rows, 1):
        print(f"  {i:>2}. {re.sub(r'[*`]', '', r[0]):<26} read as: "
              f"{re.sub(r'[*`]', '', r[1])[:44]}")

    dupes = sorted({t for t in terms if terms.count(t) > 1})
    print(f"\n  rows (the cluster total) : {len(rows)}")
    print(f"  duplicate terms          : {dupes if dupes else 'none'}")

    stated = STATED.search(text)
    if not stated:
        print("\n  !! the file does not state a total. It must — one line, derived.")
        return 1
    n = int(stated.group(1))
    print(f"  stated in the file       : {n}")
    ok = (n == len(rows)) and not dupes
    print("\nRESULT:", "OK — the stated total is the row count."
          if ok else f"FAIL — the file says {n}, the table has {len(rows)} rows. "
                     "Fix the number, or the table, but do not leave them apart.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
