#!/usr/bin/env python3
"""
er_marks.py -- read every examiner report held on disk and record the mark printed for each script.

The reports do not share one phrasing, so this handles all of the forms actually observed:

    This response scored 3 marks.          (May/June 2023, June 2026)
    This response was Level 3 - 6 marks.   (May/June 2023 P2R)
    This is a Level 3 response - 6 marks.  (May/June 2023 P2)
    Level 2 - 5 marks                     (June 2024, June 2025)
    1 mark.  /  0 marks.  /  3 marks.     (June 2022)
    1 mark awarded for ...                (June 2025)

Each capture is attributed to the nearest question heading above it. Prints the per-report table
so a wrong attribution can be seen, then writes audits/corpus/inventory_er.json.
"""
import os, re, sys, json, glob, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS = os.path.join(ROOT, "audits", "corpus")

HEAD = re.compile(r"Question\s+(\d)\s*[\(\s]\s*([a-g])\s*\)?", re.I)
MARK = re.compile(
    r"This response (?:scored|was|is)\s+(?:a\s+)?(?:Level\s*\d+\s*[\u2013-]\s*)?(\d+)\s*marks?"
    r"|This is a Level\s*\d+ response\s*[\u2013-]\s*(\d+)\s*marks?"
    r"|Total:\s*(\d+)\s*marks?"
    r"|Level\s*\d+\s*[\u2013-]\s*(\d+)\s*marks?"
    r"|(?:^|\n)\s*(\d+)\s*marks?\s*(?:awarded|\.|$)"
    r"|(?:^|\n)\s*(\d+)\s*marks?[\s.]*(?:$|\n)"
    r"|(?:was |were )?(?:awarded|gained|given) (?:the )?(?:full )?(\d+) marks?"
    r"|(?:was |were )?(?:awarded|gained|given) (?:just )?(?:one|two|three) marks?"
    r"|(?<!worth )(?<!for )(?<!of )(?<!available )\.\s*(\d+)\s*marks?\b"
    r"|No marks awarded", re.I | re.M)
NOTE = re.compile(r"of a Level\s*\d+ mark|marks available|marks are available", re.I)

REPORTS = {
    "4BS1_01_2206":  ("Jun 2022", "P1"),
    "4BS1_01R_2206": ("Jun 2022", "P1R"),
    "4BS1_02R_2206": ("Jun 2022", "P2R"),
    "4BS1_01_2306":  ("May/Jun 2023", "P1"),
    "4BS1_01R_2306": ("May/Jun 2023", "P1R"),
    "4BS1_02_2306":  ("May/Jun 2023", "P2"),
    "4BS1_02R_2306": ("May/Jun 2023", "P2R"),
    "4BS1_01_2406":  ("Jun 2024", "P1"),
    "4BS1_01R_2406": ("Jun 2024", "P1R"),
    "4BS1_02_2406":  ("Jun 2024", "P2"),
    "4BS1_01R_2506": ("Jun 2025", "P1R"),
    "4BS1_02_2506":  ("Jun 2025", "P2"),
    "4BS1_02R_2506": ("Jun 2025", "P2R"),
    "4BS1_01R_2606": ("Jun 2026", "P1R"),
}


WORDS = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
         "six": "6", "seven": "7", "eight": "8", "nine": "9", "twelve": "12"}


def scan(path):
    t = open(path, encoding="utf-8", errors="ignore").read()
    # the reports write "the full three marks" as often as "3 marks"
    t = re.sub(r"\b(" + "|".join(WORDS) + r")\b(?=\s+marks?\b)",
               lambda m: WORDS[m.group(1)], t, flags=re.I)
    heads = [(m.start(), f"{m.group(1)}({m.group(2)})") for m in HEAD.finditer(t)]
    out = collections.defaultdict(list)
    for m in MARK.finditer(t):
        if NOTE.search(m.group(0)):
            continue
        v = next((g for g in m.groups() if g), None)
        if v is None:
            continue
        q = None
        for pos, h in heads:
            if pos < m.start():
                q = h
        if q:
            out[q].append(int(v))
    return {k: sorted(set(v), reverse=True) for k, v in out.items()}


def main():
    inv, rows = {}, []
    for name, (session, paper) in REPORTS.items():
        p = os.path.join(CORPUS, name + "_ER.txt")
        if not os.path.exists(p):
            print(f"  {name:<16} corpus missing")
            continue
        q = scan(p)
        inv[name] = q
        n = sum(len(v) for v in q.values())
        print(f"  {name:<16} {session:<13} {paper:<4} questions {len(q):>2}  distinct marks {n:>3}")
        rows.append((name, q))
    json.dump(inv, open(os.path.join(CORPUS, "inventory_er.json"), "w"), indent=1)
    print(f"\nwrote audits/corpus/inventory_er.json  ({len(inv)} reports)")


if __name__ == "__main__":
    main()
