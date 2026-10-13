#!/usr/bin/env python3
"""Derive the verified-exemplar tally from the bank's own markdown.

WHY THIS EXISTS
---------------
The bank carried hand-written counts ("the bank now holds six 9/9s") sitting
directly above a list of fourteen. A hand-written total is an assertion; a
derived total is evidence. This script does not assert anything — it extracts
every heading that claims a verified full mark against a script, applies any
multiplier the heading itself states ("two more", "x3"), and prints the count
with the file and line for every entry so any row can be checked.

Entries are deduplicated by (tariff, question label) where a question label can
be read from the heading; otherwise by file:line. Repeated *references* to an
exemplar elsewhere in the bank are not counted, because only headings are read.

Run from Business_Studies_Answer_Bank/:  python3 tally_exemplars.py
"""
import re, pathlib, collections

ROOT = pathlib.Path(__file__).parent / "Perfect_Answers"
TOKEN = re.compile(r"(?<![\d/])(6/6|9/9|12/12)(?![\d/])")
CLAIM = re.compile(
    r"✅|🏆|\bawarded\b|\bscored\b|\bgained\b|Level 3\s*[–-]\s*\d|VERIFIED|"
    r"FULL[- ]MARK|full marks", re.I)
ABSENCE = re.compile(
    r"not held|no verified|❌|no full[- ]mark|not covered|beyond the|"
    r"not the|is missing|are missing|gap\b", re.I)
MULT = [(re.compile(r"\b(two|three|four|five)\s+more\b|×\s*([2-5])|\bx\s*([2-5])\b", re.I), None)]

def multiplier(text):
    m = re.search(r"\b(two|three|four|five)\s+more\b", text, re.I)
    if m:
        return {"two":2,"three":3,"four":4,"five":5}[m.group(1).lower()]
    m = re.search(r"[×x]\s*([2-5])\b", text)
    return int(m.group(1)) if m else 1

entries = []
for f in sorted(ROOT.rglob("*.md")):
    for i, line in enumerate(f.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        if not line.lstrip().startswith("#"):
            continue
        if not TOKEN.search(line) or not CLAIM.search(line) or ABSENCE.search(line):
            continue
        tariff = TOKEN.search(line).group(1)
        entries.append((tariff, str(f.relative_to(ROOT)), i,
                        multiplier(line), line.strip("# ").strip()))

# Deduplicate: same script described in two files (e.g. an exemplar file and the
# addendum). Key on the tariff plus a normalised question label if one is present.
seen, deduped = set(), []
for tariff, f, ln, mult, txt in entries:
    label = re.sub(r"[^a-z0-9]", "", txt.lower())[:60]
    key = (tariff, label)
    if key in seen:
        continue
    seen.add(key)
    deduped.append((tariff, f, ln, mult, txt))

totals = collections.Counter()
for tariff, f, ln, mult, txt in deduped:
    totals[tariff] += mult

print("=" * 78)
print("VERIFIED FULL-MARK EXEMPLARS — derived, not asserted")
print("=" * 78)
for tariff in ("6/6", "9/9", "12/12"):
    sub = [e for e in deduped if e[0] == tariff]
    print(f"\n### {tariff}  —  {len(sub)} entries, {totals[tariff]} scripts\n")
    for t, f, ln, mult, txt in sub:
        flag = f"  [x{mult}]" if mult > 1 else ""
        print(f"  • {f}:{ln}{flag}")
        print(f"      {txt[:135]}")
print()
print("=" * 78)
for tariff in ("6/6", "9/9", "12/12"):
    print(f"  {tariff}: {totals[tariff]}")
