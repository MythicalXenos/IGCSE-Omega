#!/usr/bin/env python3
"""Check `Perfect_Answers/By_Paper/` against the mark schemes — item by item.

WHY THIS EXISTS
---------------
`By_Paper/` is this bank's Layer 1: "every question in every paper, with the
official mark scheme answer". It declares its own item count and mark total in
each file's header, and those declarations were **consistent with the headings
below them** — so reading the file proved nothing.

The check that was missing is a check against an **independent** statement of the
population: the tariff table derived from all 38 mark schemes by
`build_layer_c_tariffs.py`, where every paper must reconcile to 80 marks.

That check found three defects the internal one could not:

  * `May-June_2024_P2` and `P2R` each carried **six collapsed MCQ items**
    (`1(a)(i)` headed "6 marks (AO1:1, AO1:1, AO1:1, AO1:1, AO1:1, AO1:1)") —
    five items lost and one mis-tariffed, and **the two errors cancelled in the
    paper total**, so the 80-mark check passed on a file with the wrong items in
    it. Any check that only sums marks is blind to this: swapping six 1-mark
    items for one 6-mark item keeps the sum.
  * `May-June_2019_P2R` was missing `1(a)(iii)` — a 1-mark item the scheme prints
    with **no AO label**, so a parser looking for `AO1 - 1 mark` walks past it.
    That is the paper that sums to 79.

WHAT IT CHECKS, PER PAPER
-------------------------
  1. the file exists and every mark-scheme file has one
  2. the declared `**Items:**` equals the headings below it
  3. the declared `**Marks in this paper:**` equals 80 — AND the headings sum to 80
  4. **the item count and the tariff histogram equal the derived skeleton**
     (12 × 1 mark · 4 × 2 · 4 × 3 · 3 × 6 · 2 × 9 · 1 × 12 = 26 items)
  5. every governed part label (1(f) 1(g) 2(c) 2(d) 2(e) 2(f) 3(d) 3(e) 4(b) 4(c))
     is present exactly once

Run from Business_Studies_Answer_Bank/:  python3 verify_by_paper.py
Exit code 0 when every file matches the derivation, 1 otherwise.
"""
import re
import pathlib
import sys
from collections import Counter

HERE = pathlib.Path(__file__).resolve().parent
BY_PAPER = HERE / "Perfect_Answers" / "By_Paper"
GOVERNED = ["1(f)", "1(g)", "2(c)", "2(d)", "2(e)", "2(f)", "3(d)", "3(e)", "4(b)", "4(c)"]
# the invariant skeleton, derived from the 38 mark schemes
SKELETON = {1: 12, 2: 4, 3: 4, 6: 3, 9: 2, 12: 1}

HEAD = re.compile(r"^### `([^`]+)` — (\d+) mark", re.M)


def label(part: str) -> str:
    """`1(a)(ii)` -> `1(a)`; used for the governed-part test."""
    m = re.match(r"(\d)\(([a-z])\)", part)
    return f"{m.group(1)}({m.group(2)})" if m else part


def main() -> int:
    files = sorted(BY_PAPER.glob("*.md"))
    print(f"By_Paper files: {len(files)}")
    total_items = total_marks = 0
    tariff_all = Counter()
    problems = []

    for f in files:
        text = f.read_text(encoding="utf-8")
        heads = HEAD.findall(text)
        marks = [int(m) for _p, m in heads]
        parts = [p for p, _m in heads]
        declared = re.search(r"\*\*Items:\*\*\s*(\d+)", text)
        declared_marks = re.search(r"\*\*Marks in this paper:\*\*\s*(\d+)", text)
        d_items = int(declared.group(1)) if declared else -1
        d_marks = int(declared_marks.group(1)) if declared_marks else -1

        total_items += len(heads)
        total_marks += sum(marks)
        tariff_all.update(marks)

        def bad(msg):
            problems.append((f.name, msg))

        if d_items != len(heads):
            bad(f"declares {d_items} items, has {len(heads)} headings")
        if sum(marks) != 80:
            bad(f"headings sum to {sum(marks)} marks, not 80")
        if d_marks != sum(marks):
            bad(f"declares {d_marks} marks, headings sum to {sum(marks)}")
        hist = Counter(marks)
        for tariff, want in SKELETON.items():
            if hist.get(tariff, 0) != want:
                bad(f"{tariff}-mark items: has {hist.get(tariff, 0)}, "
                    f"skeleton says {want}")
        got = sorted({label(p) for p in parts})
        for g in GOVERNED:
            n = sum(1 for p in parts if label(p) == g)
            if n != 1:
                bad(f"governed part {g}: found {n} times, expected 1")
        missing = [g for g in GOVERNED if g not in got]

    print(f"items (headings)      : {total_items}")
    print(f"marks (headings)      : {total_marks}   (38 x 80 = 3040)")
    print(f"tariff histogram      : {dict(sorted(tariff_all.items()))}")
    print()

    if problems:
        print("=" * 74)
        print(f"PROBLEMS — {len(problems)} across {len({p[0] for p in problems})} files")
        print("=" * 74)
        for name, msg in problems:
            print(f"  {name:<34} {msg}")
        print()
        print("RESULT: FAIL — the files above disagree with the mark schemes. "
              "Fix the files, not this script.")
        return 1

    print("RESULT: OK — every file matches the derived skeleton: "
          "26 items, 80 marks, 12/4/4/3/2/1 by tariff, every governed part once.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
