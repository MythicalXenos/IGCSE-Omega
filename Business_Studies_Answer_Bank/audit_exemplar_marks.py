#!/usr/bin/env python3
"""Derive the mark distribution of every exemplar printed in a source file.

WHY THIS EXISTS
---------------
The June 2019 exemplar booklet's closing coverage table was written by hand and
claims **two** 9/9 Justify scripts. Reading the two booklets gives ONE
(June 2019 P1 Q3(e)); the P2 booklet's four Justify scripts are 7/9, 4/9, 6/9
and 5/9. The table also miscounts the 3-mark row by one.

That is the same failure mode as every other hand-written total in this bank:
a number typed once, never re-derived. This script derives the numbers from the
file's own headings instead, so the table can be regenerated rather than
remembered.

USAGE
-----
    python3 audit_exemplar_marks.py <file.md> [<file2.md> ...]
    python3 audit_exemplar_marks.py --all-2019

It prints, for each question section: the exemplar headings found and the mark
each one states, then the distribution by tariff.

It reads HEADINGS ONLY (`### ...`). A heading is counted when it names an
exemplar and states a mark. Multipliers are understood ("two more", "x3").
"""
import re, sys, pathlib, collections

SECTION = re.compile(r"^#\s+(Q\d.*)$")
HEADING = re.compile(r"^#{2,4}\s+.*?Exemplar.*?\*\*(?:Level\s*\d\s*[–-]\s*)?(\d+)\s*marks?\*\*", re.I)
MULT = re.compile(r"[×x]\s*([2-5])\b")
TARIFF = {
    3: "3-mark Explain", 6: "6-mark Analyse", 9: "9-mark Justify", 12: "12-mark Evaluate",
}


def tariff_of(section, mark):
    """Prefer the section's own tariff (it states it); fall back on the mark."""
    m = re.search(r"\((\d+)\s*marks?\)", section or "")
    if m and int(m.group(1)) in TARIFF:
        return int(m.group(1))
    if mark in TARIFF:
        return mark
    # 1- and 2-mark items have no levels; treat by mark
    return mark


def scan(path):
    rows, section = [], None
    for i, line in enumerate(pathlib.Path(path).read_text(encoding="utf-8").splitlines(), 1):
        sm = SECTION.match(line)
        if sm:
            section = sm.group(1)
        hm = HEADING.search(line)
        if hm:
            mark = int(hm.group(1))
            mult = MULT.search(line)
            rows.append((section, mark, int(mult.group(1)) if mult else 1, i,
                         line.strip("# ").strip()))
    return rows


def main(argv):
    if "--all-2019" in argv:
        root = pathlib.Path(__file__).parent / "Perfect_Answers" / "External_Exemplars"
        files = [root / "2019-06_P1_Official_Exemplar_Booklet.md",
                 root / "2019-06_P2_Official_Exemplar_Booklet.md"]
    else:
        files = [pathlib.Path(a) for a in argv[1:]]
    grand = collections.Counter()
    for f in files:
        rows = scan(f)
        print("=" * 78)
        print(f"{f.name}  —  {len(rows)} exemplar headings")
        print("=" * 78)
        by_section = collections.OrderedDict()
        for section, mark, mult, ln, txt in rows:
            by_section.setdefault(section or "(no section)", []).append((mark, mult, ln, txt))
        for section, items in by_section.items():
            tar = tariff_of(section, items[0][0])
            marks = []
            for mark, mult, ln, txt in items:
                marks += [f"{mark}/{tar}"] * mult
                print(f"  L{ln:<5} {marks[-1]:<8} {txt[:88]}")
            print(f"  -> {section}: {', '.join(marks)}")
            for mark, mult, ln, txt in items:
                grand[(TARIFF.get(tar, f"{tar}-mark"), mark)] += mult
    print("=" * 78)
    print("DISTRIBUTION (tariff · mark · count) — derives the coverage table")
    print("=" * 78)
    for tar in ["3-mark Explain", "6-mark Analyse", "9-mark Justify", "12-mark Evaluate"]:
        row = {m: c for (t, m), c in grand.items() if t == tar}
        if not row:
            continue
        shown = ", ".join(f"{m}/{tar.split('-')[0]} ×{row[m]}" for m in sorted(row, reverse=True))
        print(f"  {tar:<18} {sum(row.values()):>2} exemplars   {shown}")
    print()
    print("Cross-check: every row of the coverage table should be reproducible from")
    print("the lines above. If a table in a file disagrees with this output, the")
    print("TABLE is wrong — it is the one that was typed by hand.")


if __name__ == "__main__":
    main(sys.argv)
