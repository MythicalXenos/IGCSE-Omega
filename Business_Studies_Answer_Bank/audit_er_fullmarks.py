#!/usr/bin/env python3
"""AUDIT — every full-mark script the archived examiner reports PRINT, against the register.

WHY THIS EXISTS
---------------
The bank became aware, on 14 October 2026, that its exemplar sweeps are
**pattern-driven**: each one searches for a phrasing it has already catalogued
("This response IS a Level 3", "gained a Level 3", "was Level 3"). May 2023
prints its marks a fourth way, in a bare line:

    This response scored 3 marks.

No sweep had ever been written for that phrasing, and **three May 2023 Explain
scripts printed in full went unread until a human happened to sweep for the score
line instead of the pattern.** That is not a safe way to find missing work.

So this script inverts the question. It does not look for a phrasing. It asks the
report a question every report can answer: **which scripts did you award full
marks to?** Then it asks the register whether the bank has each one.

HOW IT WORKS
------------
1. Reads all five 4BS1 examiner reports in the local archive.
2. Walks each page's text in reading order, tracking the most recent
   `Question N (x)` heading, and records every mark statement:
   `This response scored N marks`, `This response was awarded N marks`,
   `This response gained N marks`, `Total: N marks`.
3. Decides FULL MARKS by the invariant question skeleton — 1(f) 3 · 1(g) 6 ·
   2(c) 3 · 2(d) 3 · 2(e) 3 · 2(f) 9 · 3(d) 6 · 3(e) 9 · 4(b) 6 · 4(c) 12 — so
   "scored 6" on a 9-mark Justify is correctly read as a near-miss.
4. Counts printed full-mark scripts per (paper, part) and compares with the
   register's rows for the same (tier, paper, question).

⚠️ WHAT IT CANNOT SEE. The candidate scripts themselves are IMAGES; only the
score line and the examiner's comment exist as text. A report that prints a
script **without** a score statement is invisible here, and so is a script whose
score is stated in yet another phrasing. **Zero unbanked means "no un-banked
full-mark script the text layer can prove", not "no un-banked script".**

Run from Business_Studies_Answer_Bank/:  python3 audit_er_fullmarks.py
It is a REPORT, not a pass/fail check: it exits 0 while it is printing findings,
and it exits 1 only if the register cannot be parsed at all. **When every printed
full-mark script is banked, this becomes check 23 and the target is zero.**
"""
from __future__ import annotations
import collections
import pathlib
import re
import sys

import pymupdf

HERE = pathlib.Path(__file__).resolve().parent
ARCHIVE = HERE.parent / "Paperlords_Archive" / "IGCSE" / "4BS1_Business_Studies"
REGISTER = HERE / "Perfect_Answers" / "09_Verified_Tally.md"

# The invariant skeleton. If a paper ever prints a different part structure,
# verify_by_paper.py fails first - this table is a mirror of that check.
TARIFF = {"1f": 3, "1g": 6, "2c": 3, "2d": 3, "2e": 3, "2f": 9,
          "3d": 6, "3e": 9, "4b": 6, "4c": 12}

QHEAD = re.compile(r"Question\s*(\d)\s*\((\w)\)", re.I)
STATEMENT = re.compile(r"(?:This response (?:scored|was awarded|gained)\s*(\d+)\s*marks?"
                       r"|Total:\s*(\d+)\s*marks?)", re.I)
# file-name session -> the register's own wording for that series
SERIES = {"May_2023": "2023", "June_2026": "2026", "May-June_2019": "2019",
          "May-June_2020": "2020", "May-June_2021": "2021", "May-June_2022": "2022",
          "May-June_2024": "2024", "May-June_2025": "2025"}


def scan_report(path: pathlib.Path):
    """Every mark statement in reading order, with the question it belongs to."""
    doc = pymupdf.open(path)
    current, found = None, []
    for page_no, page in enumerate(doc, 1):
        text = page.get_text()
        events = ([(m.start(), "Q", (m.group(1), m.group(2).lower())) for m in QHEAD.finditer(text)]
                  + [(m.start(), "S", int(m.group(1) or m.group(2))) for m in STATEMENT.finditer(text)])
        for _pos, kind, value in sorted(events):
            if kind == "Q":
                current = value
            elif current:
                part = f"{current[0]}{current[1]}"
                full = TARIFF.get(part) == value
                found.append({"page": page_no, "part": part, "mark": value, "full": full})
    return found


def register_parts():
    """(year, tier, paper, question) -> count, from the register's own rows.

    SESSION-AWARE, and that is the whole point. The first version of this
    function keyed on (tier, paper, question) alone, and the run it produced was
    a lie: it reported ONE un-banked script when there were ELEVEN, because a
    printed May 2023 P1R Q2(c) was "found" by the register's June 2026 P1R row
    for Q2(c). **A paper-blind key three times over — the audit built to catch
    exactly that failure reproduced it.** The series column is read now.
    """
    rows = collections.Counter()
    tariff = None
    for line in REGISTER.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^##\s*(3|6|9|12)\s*MARKS", line)
        if m:
            tariff = f"{m.group(1)}/{m.group(1)}"
            continue
        if line.startswith("## "):
            tariff = None
        if tariff and re.match(r"^\|\s*\d+\s*\|", line):
            # columns: [0]="" [1]=# [2]=series [3]=P · Q [4]=topic [5]=citation
            series = line.split("|")[2]
            label = line.split("|")[3]
            y = re.search(r"(20\d\d)", series)
            q = re.search(r"Q(\d)\((\w)\)", label)
            p = re.search(r"\bP(\d)(R?)\b", label)
            if y and q and p:
                rows[(y.group(1), tariff, f"P{p.group(1)}{p.group(2)}", f"{q.group(1)}{q.group(2)}")] += 1
    return rows


def main() -> int:
    reg = register_parts()
    if not reg:
        print("REGISTER PARSE FAILED - check the parser, not the bank.")
        return 1

    print("=" * 78)
    print("PRINTED FULL-MARK SCRIPTS vs THE REGISTER — every archived examiner report")
    print("=" * 78)

    all_unbanked, total_printed, total_banked = [], 0, 0
    for pdf in sorted(ARCHIVE.glob("*/*ER.pdf")):
        found = scan_report(pdf)
        fulls = [f for f in found if f["full"]]
        year = SERIES.get(pdf.parent.name, "")
        paper = "P" + pdf.stem.split("_")[-2].replace("P", "")  # ..._P1R_ER -> P1R
        printed = collections.Counter(f["part"] for f in fulls)
        pages = collections.defaultdict(list)
        for f in fulls:
            pages[f["part"]].append(f["page"])
        print()
        print(f"  {pdf.name}")
        print(f"    mark statements: {len(found)}   FULL MARK: {len(fulls)}")
        for part, count in sorted(printed.items()):
            tier = f"{TARIFF[part]}/{TARIFF[part]}"
            banked = reg.get((year, tier, paper, part), 0)
            status = "ok " if banked >= count else "GAP"
            total_printed += count
            total_banked += min(banked, count)
            print(f"      {status} {part:<4} {tier:<6} printed {count}   register {banked}"
                  f"   (report p. {', '.join(str(p) for p in pages[part])})")
            if banked < count:
                all_unbanked.append((pdf.parent.name, paper, part, tier, count - banked,
                                     pages[part]))

    print()
    print("=" * 78)
    print(f"UNBANKED PRINTED FULL-MARK SCRIPTS — {sum(u[4] for u in all_unbanked)}")
    print("=" * 78)
    if not all_unbanked:
        print("  none — every full-mark script the text layer can prove is in the register.")
    for series, paper, part, tier, n, pages in all_unbanked:
        print(f"  {series} {paper} {part} ({tier}) — {n} script(s) printed, not banked"
              f"   [report p. {', '.join(str(p) for p in pages)}]")
    print()
    print(f"  printed full-mark scripts: {total_printed}   matched in the register: {total_banked}")
    print()
    if not all_unbanked:
        print("RESULT: no gap the text layer can prove.")
        return 0

    # ======================================================================
    # THIS SCRIPT USED TO EXIT 0 WHILE IT FOUND GAPS. It reported the eleven
    # May 2023 full-mark scripts for two runs without ever failing the suite,
    # because it was written as a report and every sweep that read it treated
    # "found something" as information. Twelve checks in this bank had already
    # been taught the opposite lesson — a check that cannot fail is not a
    # check. Promoted to check 23 on 14 Oct 2026, once the gap it named was
    # closed and the target could be stated as zero.
    #
    # If this now fails, the run is telling you an archived examiner report
    # PRINTS a full-mark script the register does not hold. Bank it: transcribe
    # the question, the mark scheme, the script and the examiner comment into
    # External_Exemplars/, add the register row with a heading citation within
    # eight lines, and re-run. Do not lower the expectation — Pearson printing
    # a script is proof that the script exists.
    # ======================================================================
    print()
    print("=" * 78)
    print("FAIL — ARCHIVED EXAMINER REPORTS PRINT FULL-MARK SCRIPTS THE REGISTER LACKS")
    print("=" * 78)
    for series, paper, part, tier, n, pages in all_unbanked:
        print(f"  {series} {paper} {part} ({tier}) — {n} script(s) printed, not banked"
              f"   [report p. {', '.join(str(p) for p in pages)}]")
    print()
    print(f"  {sum(u[4] for u in all_unbanked)} script(s) to bank.")
    print()
    print("  Each one is a script Pearson awarded FULL marks to, printed in a report")
    print("  the archive already holds. Transcribe it into External_Exemplars/ and")
    print("  register it — see the note above this block for the procedure.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
