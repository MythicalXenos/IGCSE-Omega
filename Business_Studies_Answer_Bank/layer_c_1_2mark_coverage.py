#!/usr/bin/env python3
"""CHECK 24 — the 1- and 2-mark tier: what the reports PRINT vs what the bank has.

WHY THIS EXISTS
---------------
`audit_er_fullmarks.py` (check 23) proves that every **full-mark** script the
archive prints is banked. This tier has no full marks to count — the questions
are worth one and two marks, the mark scheme is the answer, and what the reports
print is **a credited script beside a rejected one**. So check 23's target of
zero is the wrong target here.

What matters here is **how much of the tier is transcribed**, and that is a
number that drifts the moment a file is added. It drifted in this bank's own
hands on 14 October 2026:

    "67 of the 80 printed 1- and 2-mark scripts are not transcribed"   (typed)
    ... the true figure at that moment was 37 of 80 not transcribed.

The typed number was never wrong when it was written. It was simply never
re-derived, and three files were added after it.

⚠️ AND THE COUNT IS SESSION-AWARE, BECAUSE THE FIRST DRAFT OF THIS SCRIPT'S
LOGIC WAS NOT. Keyed on (paper, part) alone, it reported ten **May 2023 Paper 1R**
questions as banked when the register's rows for them were **June 2026 Paper 1R** —
1(b), 1(c), 1(d), 1(e), 2(a), 2(b), 3(a), 3(b), 3(c), 4(a) exist on BOTH papers.
The corrected key is **(year, paper, part)**, which is the same cure
`audit_er_fullmarks.py` needed, for the same reason. **A paper-blind key makes a
check lie — this is now the fourth time in this bank.**

WHAT IT CHECKS
--------------
1. Every register row in the 1- and 2-mark tables names a session, a paper and a
   part, and it must match a question the reports actually print.
2. No two rows may claim the same (year, paper, part) — that is a double-count.
3. The remaining worklist is printed, so open item 6 in `08_` is read, not typed.

Exit 0 when the register is consistent (it does NOT require the tier to be
finished — an unfinished tier is a worklist, not a failure, and the run prints
how much is left). Exit 1 on a dangling or duplicated row, or on a parse that
saw nothing.

Run from Business_Studies_Answer_Bank/:  python3 layer_c_1_2mark_coverage.py
"""
from __future__ import annotations
import collections
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import audit_er_fullmarks as audit  # noqa: E402  (shares the score grammar)

REGISTER = HERE / "Perfect_Answers" / "09_Verified_Tally.md"
BANKED_FILES = ("One_and_Two_Mark_Pairs", "One_Mark_Pairs", "Two_Mark_Set",
                "P2R_One_and_Two_Mark_Set")
ROW = re.compile(r"^\|\s*\d+\s*\|")
QP = re.compile(r"\bP(\d)(R?)\s*Q(\d)\s*\((\w)\)")
YEAR = re.compile(r"\*\*(May/Jun|Jun|May|Nov|Jan)\s*(\d{4})\*\*")


def printed_tier():
    """{(year, paper, part): count} for every 1-/2-mark script the reports print."""
    out = collections.Counter()
    for pdf in sorted(audit.ARCHIVE.glob("*/*ER.pdf")):
        year = audit.SERIES.get(pdf.parent.name, "?")
        paper = "P" + pdf.stem.split("_")[-2].replace("P", "")
        found, _gaps = audit.scan_report(pdf)
        for f in found:
            if f["part"] not in audit.TARIFF:      # 1- and 2-mark parts only
                out[(year, paper, f["part"])] += 1
    return out


def register_rows():
    rows = []
    for line in REGISTER.read_text(encoding="utf-8").splitlines():
        if not ROW.match(line) or not re.search("|".join(BANKED_FILES), line):
            continue
        q, y = QP.search(line), YEAR.search(line)
        if q and y:
            rows.append(((y.group(2), f"P{q.group(1)}{q.group(2)}",
                          f"{q.group(3)}{q.group(4).lower()}"), line))
    return rows


def main() -> int:
    printed = printed_tier()
    rows = register_rows()
    problems = []

    print("=" * 78)
    print("THE 1- AND 2-MARK TIER — printed scripts vs the bank's transcripts")
    print("=" * 78)
    print(f"  reports scanned : {len(list(audit.ARCHIVE.glob('*/*ER.pdf')))}")
    print(f"  printed scripts : {sum(printed.values())} on 1-/2-mark parts")
    print(f"  register rows   : {len(rows)} question(s) with a banked transcript")

    if not printed:
        print("\n  ⚠️ NO PRINTED SCRIPTS PARSED — that is the parser failing, not the tier.")
        return 1
    if not rows:
        print("\n  ⚠️ NO REGISTER ROWS PARSED — check the parser and BANKED_FILES.")
        return 1

    seen = collections.Counter(k for k, _ in rows)
    for key, n in seen.items():
        if n > 1:
            problems.append(f"{(key)} is claimed by {n} register rows — a double-count")
            print(f"\n  FAIL  {key} appears in {n} rows")
    for key, line in rows:
        if key not in printed:
            problems.append(f"{(key)} has a register row but the reports print no such script")
            print(f"\n  FAIL  {key} is not a 1-/2-mark question in any archived report")
            print(f"        {line[:100]}")

    covered = sum(n for k, n in printed.items() if k in seen)
    remaining = sorted((k for k in printed if k not in seen))

    print()
    print("=" * 78)
    print(f"COVERAGE — {covered} of {sum(printed.values())} printed scripts are transcribed")
    print("=" * 78)
    by_series = collections.Counter()
    for (year, paper, _part) in remaining:
        by_series[(year, paper)] += 1
        print(f"  {year} {paper:<4} Q{_part[0]}({_part[1]}) — "
              f"{printed[(year, paper, _part)]} script(s)")
    print()
    if by_series:
        print("  remaining by paper: " + " · ".join(
            f"{y} {p} ×{n}" for (y, p), n in sorted(by_series.items())))
    print()
    print(f"  BANKED  : {covered}")
    print(f"  REMAIN  : {sum(printed.values()) - covered}")
    print()
    print("  ⚠️ An unfinished tier is a WORKLIST, not a failure — this check fails")
    print("     only on a dangling or duplicated register row. Open item 6 in `08_`")
    print("     must quote THIS number, not a typed one.")
    print()
    print("RESULT:", "OK — every banked row matches a printed script, and none is counted twice."
          if not problems else f"FAIL — {len(problems)} register row(s) disagree with the reports.")
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
