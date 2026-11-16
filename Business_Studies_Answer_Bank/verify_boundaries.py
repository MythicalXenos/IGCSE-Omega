#!/usr/bin/env python3
"""Check the boundary data in `00_` against its two sources, and check the
additivity rule against itself.

WHY THIS EXISTS
---------------
The boundary section is the one part of the bank a student acts on directly: it
decides whether a mock score is a 9. It is also the part most exposed to a
transcription slip, because every number in it is typed by hand from a PDF or a
web page, and a wrong number here is invisible -- it looks exactly like a right
one.

This script holds the source data (Pearson's published figures, transcribed
14 Oct 2026) and requires `00_` to agree with it in both tables:

  * the NOTIONAL COMPONENT table (grade 9, per paper, per series)
  * the TREND table (qualification grade 9, per series and route)

It then derives the additivity relationship and requires the file to claim
exactly what the numbers do -- which is NOT what an earlier version of the file
claimed. See the printout.

RUN FROM `Business_Studies_Answer_Bank/`. Prints one RESULT.

  python3 verify_boundaries.py
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
RULEBOOK = HERE / "Perfect_Answers" / "00_Pearson_Official_Rulebook.md"

# ---------------------------------------------------------------------------
# SOURCE DATA -- Pearson, retrieved 14 Oct 2026.
#   qualification: grade 9 out of 160, (standard, regional); None = not published
#   components:    grade 9 out of 80, (P1, P1R, P2, P2R);      None = not published
# Pearson labels the summer series by exam month ("May 2026"); this bank labels
# it "Jun 2026". SERIES_MAP carries that translation, so a name mismatch can
# never pass silently as a missing row.
# ---------------------------------------------------------------------------
QUALIFICATION = {
    "May 2026": (133, 137), "Nov 2025": (133, None), "May 2025": (130, 130),
    "Nov 2024": (132, None), "May 2024": (133, 139), "Nov 2023": (132, None),
    "May 2023": (132, 137), "May 2022": (111, 114), "Nov 2021": (84, None),
    "Nov 2020": (90, 97), "May 2019": (113, 111),
}
COMPONENTS = {
    "May 2026": (68, 68, 65, 69), "Nov 2025": (66, None, 67, None),
    "May 2025": (65, 65, 65, 65), "Nov 2024": (65, None, 67, None),
    "May 2024": (65, 71, 68, 68), "Nov 2023": (68, None, 64, None),
    "May 2023": (68, 68, 64, 69), "Nov 2022": (None, 49, None, None),
    "May 2022": (54, 58, 54, 59), "Nov 2021": (41, None, 43, None),
    "Nov 2020": (46, None, 44, 48), "May 2019": (57, 57, 54, 56),
}
SERIES_MAP = {"Jun 2026": "May 2026", "Jun 2025": "May 2025", "Jun 2024": "May 2024",
              "Jun 2023": "May 2023", "Jun 2022": "May 2022", "Jun 2019": "May 2019"}

# The additivity relationship, derived from the data above, nothing typed.
exact, off = [], []
for series, (std, reg) in QUALIFICATION.items():
    p1, p1r, p2, p2r = COMPONENTS[series]
    for route, (a, b, pub) in (("standard", (p1, p2, std)), ("regional", (p1r, p2r, reg))):
        if a is None or b is None or pub is None:
            continue
        (exact if a + b == pub else off).append((series, route, a + b, pub))


def num(cell: str):
    """A markdown table cell -> int, or None for an em-dash."""
    cell = cell.replace("*", "").replace("✅", "").replace("📄", "").strip()
    if cell in ("", "—", "-"):
        return None
    m = re.search(r"\d+", cell)
    return int(m.group()) if m else None


def rows(table: str):
    """Every data row of a markdown table body."""
    out = []
    for line in table.split("\n"):
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or set("".join(cells)) <= set("-: "):
            continue
        if cells[0].lower().startswith(("series", "paper")):
            continue        # the header row is not data
        out.append(cells)
    return out


def main() -> int:
    text = RULEBOOK.read_text(encoding="utf-8")
    problems = []

    # ---- 1. the notional component table -----------------------------------
    m = re.search(r"\*\*Every series, grade 9, per paper\*\*.*?\n(\|.*?)\n\n", text, re.S)
    if not m:
        print("!! could not find the notional component table in 00_ — parser or file has changed.")
        return 1
    nt = rows(m.group(1))
    print("=" * 74)
    print("NOTIONAL COMPONENT TABLE — 00_ against Pearson's published figures")
    print("=" * 74)
    print(f"  rows parsed: {len(nt)}")
    seen = set()
    for cells in nt:
        label = re.sub(r"[✅📄]", "", cells[0].replace("*", "")).split("(")[0].strip()
        src = SERIES_MAP.get(label, label)
        if src not in COMPONENTS:
            problems.append(f"notional table row {label!r} is not a series Pearson publishes")
            continue
        seen.add(src)
        got = [num(c) for c in cells[1:5]]
        want = list(COMPONENTS[src])
        if got != want:
            problems.append(f"notional {label}: 00_ says {got}, Pearson publishes {want}")
            print(f"  FAIL {label:<10} 00_ {got}  Pearson {want}")
    missing = set(COMPONENTS) - seen
    if missing:
        problems.append(f"series missing from the notional table: {sorted(missing)}")
    print(f"  series published by Pearson: {len(COMPONENTS)}   present in 00_: {len(seen)}")
    if not problems:
        print("  every row agrees.")

    # ---- 2. the trend (qualification) table --------------------------------
    m = re.search(r"\| Series \| Max \| \*\*9\*\*.*?\n(\|.*?)\n\n", text, re.S)
    if not m:
        print("!! could not find the trend table in 00_ — parser or file has changed.")
        return 1
    tr = rows(m.group(1))
    print()
    print("=" * 74)
    print("TREND TABLE — 00_ against Pearson's published qualification boundaries")
    print("=" * 74)
    print(f"  rows parsed: {len(tr)}")
    checked = 0
    for cells in tr:
        label = cells[0].replace("*", "").strip()
        route = "regional" if "regional" in label else "standard"
        series = SERIES_MAP.get(label.split("·")[0].strip(), label.split("·")[0].strip())
        if series not in QUALIFICATION:
            problems.append(f"trend row {label!r} is not a series Pearson publishes")
            continue
        want = QUALIFICATION[series][0 if route == "standard" else 1]
        if want is None:
            continue
        got = num(cells[2])
        checked += 1
        if got != want:
            problems.append(f"trend {label}: 00_ says {got}, Pearson published {want}")
            print(f"  FAIL {label:<24} 00_ {got}  Pearson {want}")
    print(f"  rows compared against a published qualification boundary: {checked}")
    if not problems:
        print("  every row agrees.")

    # ---- 3. the additivity rule, as the file states it ---------------------
    print()
    print("=" * 74)
    print("ADDITIVITY — does 00_ claim what the numbers actually do?")
    print("=" * 74)
    print(f"  pairs where both components and the qualification boundary are published: "
          f"{len(exact) + len(off)}")
    print(f"    components sum EXACTLY to the boundary : {len(exact)}")
    for s, r, tot, pub in exact:
        print(f"      {s:<10} {r:<9} sums to {tot:>3} = published {pub}")
    print(f"    components do NOT sum                 : {len(off)}")
    for s, r, tot, pub in off:
        print(f"      {s:<10} {r:<9} sums to {tot:>3} ≠ published {pub}  ({tot - pub:+d})")
    fail_series = sorted({row[0] for row in off})
    print(f"  every failure is in: {fail_series}")

    # The sentences `00_` must carry, BUILT FROM THE DERIVED NUMBERS. Typing them
    # in by hand is how "18 pairs" and "14 of 14" got into the file -- both wrong.
    modern = [row for row in exact + off if int(row[0][-4:]) >= 2023]
    wanted = [
        (f"**Every series from 2023 onwards adds exactly, at grade 9 — "
         f"{len(modern)} of {len(modern)}.**", "the modern-series result"),
        (f"**{len(off)} of the {len(exact) + len(off)} checkable pairs do not: "
         f"May 2019 and May 2022, in either direction, by 2 to 3 marks.**",
         "the overall result"),
    ]
    for phrase, why in wanted:
        if phrase not in text:
            problems.append(f"00_ does not state the derived result ({why}). It must read exactly:\n"
                            f"        {phrase}")
    if fail_series != ["May 2019", "May 2022"]:
        problems.append(f"the failing series changed: {fail_series} — the file's wording must change too")
    print()
    if problems:
        print("=" * 74)
        for pr in problems:
            print(f"  !! {pr}")
    print("RESULT:", "OK — both boundary tables agree with Pearson, and the additivity "
                     "rule in the file is the one the numbers support."
          if not problems else f"FAIL — {len(problems)} disagreement(s).")
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
