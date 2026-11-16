#!/usr/bin/env python3
"""CHECK 25 — the below-full-mark scripts the reports print, against the bank.

WHY THIS EXISTS
---------------
The archive's five examiner reports print **151 marked scripts**. Until now the
bank guarded two of the three classes into which they fall:

    check 23   the 37 FULL-MARK scripts      "Pearson printed it, so it exists"
    check 24   the 80 scripts on 1-/2-mark parts   the pairs, with a 0 beside the 1
    ----       the 34 BELOW-FULL-MARK scripts ... nothing. Unchecked.

**This is the third time the same blind spot has been found in a different
category, and the third time it was found by asking what the reports PRINT
rather than by reading the bank.** Check 23 was written because a phrasing no
sweep knew had hidden eleven scripts. Check 24 was written because the register
said the tier had no printed scripts at all. Both times the lesson written into
the file was "ask the reports what they print" - and both times the guard that
came out of it covered only the slice of the printed scripts that the immediate
finding was about.

⚠️ THAT IS THE POINT OF THIS CHECK, AND IT IS WORTH STATING PLAINLY: a guard
built from one finding protects against that finding. The three classes are
exhaustive — every statement in the five reports is a full mark, a 1-/2-mark
part, or a below-full mark on a governed part — so with this check the whole
printed population is covered, and a fourth category cannot appear.

WHY BELOW-FULL MATTERS MORE THAN IT SOUNDS
------------------------------------------
`03_Calibration_Below_Full_Marks.md` is built on the finding that the near-misses
teach the most: the 11/12 next to the 6/12 on one question, the 8/9 that used
"it depends" as a hedge and lost the top mark, the 4/6 that applied nothing.
**A near-miss that Pearson printed and the bank did not transcribe is exactly
the material a candidate needs and cannot get anywhere else.** So the target
here is zero, like check 23's.

HOW A TRANSCRIPT IS MATCHED
---------------------------
Deliberately strict, because the bank has been burned by loose matching twice:

  * the score must appear as `mark/tier` (e.g. `4/12`), and
  * the question label (`Q4(c)`) must sit within 10 lines of it, and
  * the session must be visible — the year in the citing file's NAME, or in the
    window around the score.

Requiring all three is what stops a `4/12` in a June 2024 file from answering
for a May 2023 `Q4(c)`. Loose matching is how a paper-blind key made this bank's
checks lie three separate times.

⚠️ DUPLICATES ARE COLLAPSED AND REPORTED. A report sometimes states the same
script's mark twice on one page (`2023 P2R Q1(g)`, 4/6, p. 14). That is one
script, not two, so statements are deduplicated on
(year, paper, part, mark) — and any collapse is printed, because a silent
collapse would understate the printed population.

Run from Business_Studies_Answer_Bank/:  python3 audit_below_fullmarks.py
Exits 0 when every below-full printed script resolves, 1 when one does not.
"""
from __future__ import annotations
import collections
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import audit_er_fullmarks as audit  # noqa: E402  (shares the score grammar + TARIFF)

BANK = HERE / "Perfect_Answers"
WINDOW = 6

# ==============================================================================
# WHY THE WINDOW IS SIX AND THE FILENAME COUNTS AS CONTEXT
# ------------------------------------------------------------------------------
# The first version of this check used a window of 10 lines and accepted a match
# if the score, the label and the year all appeared in it. **It could not fail.**
# Sabotaging it - deleting the bank's transcript of the May 2023 P1R 4/12 - left
# the script reporting 32 of 32, because a 2019 coverage-table row in `04_` that
# contains `4/12` and `Q4(c)` sat two lines above a row mentioning the year 2023.
# **One spurious hit is enough to make a gap invisible.** (This is the same
# failure the bank has recorded twice before in other checks: a citation that is
# similar is not a citation that is right.)
#
# Two corrections, both measured against the bank's real conventions rather than
# guessed:
#
#   * SESSION and PAPER may be evidenced by the FILE NAME as well as the window.
#     That is how the bank actually writes: `| **Q3(d) 6-mark Analyse** | ...
#     — 2/6 (PDF 29) ...` names neither session nor paper on the line, because
#     the file is called `2026-06_P1R_SpudBros.md`. The filename is part of the
#     citation, so it is part of the evidence.
#
#   * THE WINDOW IS 6. Measured, not chosen: at ±5 one 2026 script fails to
#     resolve, at ±6 none does. A larger window would have re-admitted the
#     spurious 2019 row, so 6 is the tightest width at which every genuine
#     transcript is still recognised.
#
# ⚠️ THE SABOTAGE IS THE ONLY PROOF THAT MATTERS HERE: deleting a real transcript
# must FAIL. Re-run it after any change to this function.
#
# A THIRD CORRECTION, AND THE ONE THAT MADE THE SABOTAGE WORK. The first version
# searched the WHOLE bank, and a spurious hit kept rescuing a deleted transcript:
# `09_Verified_Tally.md` line 193 is a narrative about the 3-mark register that
# happens to contain `2/3`, `P2R` and `2023` inside one window. **Its hit made a
# real gap invisible.** Two candidate cures were measured against the bank:
#
#     search the whole bank, demand session+paper ..... 1 spurious hit survived
#     search session-named files only ................. 4 genuine gaps surfaced
#
# The four gaps were REAL — the only four below-full-mark scripts in the archive
# nobody had transcribed (`2023-05_Series_P2_and_P2R_Two_Mark_Explain.md` now
# holds them). **A rule that finds real work is the right rule.** So a transcript
# counts only when it sits in a FILE THAT NAMES ITS SESSION
# (`2023-0…`, `2026-0…`) — which is where this bank keeps transcripts by its own
# convention — and the paper is matched with a boundary-corrected pattern,
# because `\bP1R\b` silently never matches `2026-06_P1R_SpudBros.md`: an
# underscore is a word character, and this trap has now cost this bank twice.
# ==============================================================================

# Session-named transcript files: the bank's convention (2023-05_…, 2026-06_…).
SESSION_FILE_PREFIX = {"2019": "2019-", "2020": "2020-", "2021": "2021-",
                       "2022": "2022-", "2023": "2023-", "2024": "2024-",
                       "2025": "2025-", "2026": "2026-"}


def paper_pattern(paper):
    """`P1R` must match inside `2026-06_P1R_SpudBros` — so no `\b`."""
    return re.compile(rf"(?<![A-Za-z0-9]){re.escape(paper)}(?![0-9A-Za-z])")


def printed_below_full():
    """[(key, statements)] for every below-full-mark script on a governed part.

    key = (year, paper, part, mark); statements = the (page) occurrences found.
    """
    out = collections.OrderedDict()
    for pdf in sorted(audit.ARCHIVE.glob("*/*ER.pdf")):
        year = audit.SERIES.get(pdf.parent.name, "?")
        paper = "P" + pdf.stem.split("_")[-2].replace("P", "")
        found, _gaps = audit.scan_report(pdf)
        for f in found:
            tier = audit.TARIFF.get(f["part"])
            if tier is None or f["mark"] == tier:
                continue        # 1-/2-mark parts and full marks are other checks
            key = (year, paper, f["part"], f["mark"])
            out.setdefault(key, []).append(f["page"])
    return out


def bank_docs():
    return {md: md.read_text(encoding="utf-8", errors="replace").splitlines()
            for md in sorted(BANK.rglob("*.md"))}


def find_transcript(docs, year, paper, part, mark, tier):
    """[(file, line)] for every place the bank holds this script.

    A hit needs FOUR things, and they may draw on the file name as well as the
    text: the score, the question label, the session, and the paper. Requiring
    all four is what stops a `4/12` from a June 2019 table row answering for a
    May 2023 script two lines below it.
    """
    score = f"{mark}/{tier}"
    label = f"Q{part[0]}({part[1]})"
    prefix = SESSION_FILE_PREFIX.get(year)
    if prefix is None:
        return []
    pap = paper_pattern(paper)
    hits = []
    for md, lines in docs.items():
        if not md.name.startswith(prefix):
            continue        # a transcript lives in a file that names its session
        for i, line in enumerate(lines):
            if score not in line:
                continue
            window = "\n".join(lines[max(0, i - WINDOW): i + WINDOW + 1])
            if label not in window and f"Q{part[0]} ({part[1]})" not in window:
                continue
            if not pap.search(window) and not pap.search(md.name):
                continue
            hits.append((str(md.relative_to(BANK)), i + 1))
    return hits


def main() -> int:
    printed = printed_below_full()
    if not printed:
        print("PARSE FAILED — the reports yielded no below-full statements.")
        print("That is this script failing, not the bank.")
        return 1

    docs = bank_docs()
    if len(docs) < 20:
        print(f"PARSE FAILED — only {len(docs)} markdown files read.")
        return 1

    statements = sum(len(v) for v in printed.values())
    collapsed = statements - len(printed)

    print("=" * 78)
    print("BELOW-FULL-MARK SCRIPTS THE REPORTS PRINT vs THE BANK'S TRANSCRIPTS")
    print("=" * 78)
    print(f"  reports scanned            : {len(list(audit.ARCHIVE.glob('*/*ER.pdf')))}")
    print(f"  below-full statements found : {statements}")
    if collapsed:
        print(f"  collapsed as duplicates     : {collapsed}"
              f"   (same script's mark stated twice on one page)")
    print(f"  distinct below-full scripts : {len(printed)}")
    print()

    missing = []
    for (year, paper, part, mark), pages in printed.items():
        tier = audit.TARIFF[part]
        hits = find_transcript(docs, year, paper, part, mark, tier)
        if hits:
            continue
        missing.append(((year, paper, part, mark, tier, pages), hits))

    print("=" * 78)
    print(f"COVERAGE — {len(printed) - len(missing)} of {len(printed)}"
          f" below-full printed scripts are transcribed")
    print("=" * 78)
    if not missing:
        print("  every one resolves: the score, the label, the session and the paper are")
        print(f"  all present, within {WINDOW} lines or in the citing file's own name.")
    for (year, paper, part, mark, tier, pages), hits in missing:
        print(f"  GAP  {year} {paper} Q{part[0]}({part[1]}) {mark}/{tier}"
              f" — report p. {', '.join(str(p) for p in pages)}  NOT TRANSCRIBED")
    print()

    if missing:
        print("RESULT: FAIL — a script Pearson printed is not transcribed in this")
        print("        bank, or is transcribed without naming its session or paper.")
        print()
        print("  Each of these is a marked answer to a governed question, printed in")
        print("  full in a report the archive already holds. Transcribe it and cite it")
        print("  from `03_Calibration_Below_Full_Marks.md` or the session's exemplar file.")
        return 1

    print("RESULT: no gap — every below-full-mark script the reports print is banked,")
    print("        and every transcript names its own session.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
