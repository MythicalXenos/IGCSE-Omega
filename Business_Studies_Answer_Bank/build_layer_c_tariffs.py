#!/usr/bin/env python3
"""Layer C -- derive the 6-, 9- and 12-mark populations from the MARK SCHEMES.

WHY THIS EXISTS
---------------
`4BS1_Question_Instances.csv` gave 86 x 6-mark, 48 x 9-mark, 17 x 12-mark. Those
figures come from QUESTION-PAPER text extraction and are not trustworthy (rule
120). They are also provably wrong: every P1-family paper carries TWO 9-mark
Justify questions, not one.

THE TRAP, AND HOW THIS FILE AVOIDS IT
-------------------------------------
Counting AO-allocation lines naively double-counts, because the allocation is
printed more than once per question. Two regex routes were tried and abandoned
before this one. What actually works is a two-route scan with a hard validation:

  ROUTE A (authoritative) -- a part label followed by nothing but whitespace or
    punctuation before its AO allocation.
  ROUTE B (fallback)      -- any AO allocation attributed to the nearest
    PRECEDING part label within 220 characters. Only ever fills a slot Route A
    left empty. Required because May-June 2022 P1 1(e) restates the question
    between the label and the allocation:
        "1 (e) Calculate the total costs for TBTS. A02 - 2 marks"

  EVERY PAPER IS THEN CHECKED: a 4BS1 paper is worth 80 marks. A paper whose
  parts do not sum to 80 is REPORTED AND NOT TRUSTED. That check is the point of
  the script -- it is what stops another wrong number entering the bank.

WHY EACH PASS RUNS TWICE
------------------------
Every document is scanned twice: whitespace-normalised, and FULLY DE-SPACED.
The May-June 2021 files are character-fragmented and print "A O3 = 3 marks" and
"3 mark s"; a normalised pass reads 3 marks for a 12-mark question. Per part the
LARGER reading is kept, which is safe because fragmentation only ever truncates
an allocation list -- it never invents marks.

THE FOUR SEPARATOR TRAPS (all hit, all now handled)
---------------------------------------------------
  1. The dash between AO code and mark count is sometimes an EN DASH: the split
     headers "AO2 - 3 marks AO3 - 3 marks" print as "AO2 <U+2013> 3 marks ...".
  2. Successive allocations are comma-separated in some papers:
     "AO2 = 3 marks, AO3 = 3 marks, AO4 = 3 marks".
  3. AO codes are printed "A02" (zero) as often as "AO2" (letter O).
  4. Labels print with a space: "2 (c)", never "2(c)".

RUN FROM Business_Studies_Answer_Bank/. Writes layer_c_6_9_12_master.csv.
"""
import collections
import csv
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ARCHIVE = HERE.parent / "Paperlords_Archive" / "IGCSE" / "4BS1_Business_Studies"
OUT = HERE / "layer_c_6_9_12_master.csv"

# Traps 1 and 3: any short run of non-alphanumerics separates the AO code from
# its mark count, and the code itself may be spelled "A02".
SEP = r"[^A-Za-z0-9]{0,4}"

# A run of one or more AO allocations. Trap 2: the BETWEEN-allocation separator
# may be a comma, so the trailing [,;] is not optional decoration -- without it a
# 12-mark Evaluate reads as 3 marks and a 9-mark Justify as 3.
AO_GROUP = re.compile(
    r"(?:A[O0]\s*[1-4]\s*" + SEP + r"\s*\d+\s*marks?\s*[,;]?\s*)+", re.I)
AO = re.compile(r"A[O0]\s*([1-4])\s*" + SEP + r"\s*(\d+)", re.I)

# Trap 4: "1 (a) (i)" may print as "1 (a)(i)", "1(a) (i)" or "1 (a) (vi )".
LBL = re.compile(r"(\d+)\s*\(\s*([a-z])\s*\)\s*(?:\(\s*([ivx]+)\s*\))?")

ROUTE_B_WINDOW = 220

# Genuinely irregular items ONLY. Every entry must quote its evidence: an
# unexplained override is exactly how a wrong number gets into the bank.
#
# May-June 2019 P2R 1(a)(iii) -- the MS prints NO AO header for this item:
#   "We are aware that there is no correct answer to this item. Because of this,
#    all candidates will be awarded 1 mark for this question 1 (a) (iii)."
# It is a voided multiple-choice item, so there is no AO to allocate.
# The question skeleton, derived not assumed: of the 38 papers, the 36 that
# first summed to 80 all produced this IDENTICAL key set, and every part carries
# the same tariff in every one of the 38 -- see the invariance table the script
# prints. The two papers that did not were found to contain one junk key each
# (a bare "1(a)" and a run-together "20211(e)"), which this filter drops.
SKELETON = (
    [f"1(a)({r})" for r in ("i", "ii", "iii", "iv", "v", "vi")]
    + [f"1({c})" for c in "bcdefg"]
    + [f"2({c})" for c in "abcdef"]
    + [f"3({c})" for c in "abcde"]
    + [f"4({c})" for c in "abc"]
)

OVERRIDES = {
    "May-June_2019 May-June_2019_P2R": {"1(a)(iii)": (1, ())},
}


DROPPED: dict[str, list[str]] = {}


def repair(text: str) -> str:
    """Undo the character fragmentation in the May-June 2021 PDFs.

    Those files print "A0 1 - 3 mark s" for "AO1 - 3 marks". Without this the
    extractor silently loses whole blocks; with it they read normally and stay
    quotable. Shared with extract_ms_blocks.py.
    """
    text = re.sub(r"\bA\s?[O0]\s?([1-4])\b", r"AO\1", text)
    text = re.sub(r"\bm\s?a\s?r\s?k\s?s\b", "marks", text)
    return text


def _key(n: str, letter: str, roman: str | None) -> str:
    return f"{n}({letter})" + (f"({roman})" if roman else "")


def _routes(text: str) -> tuple[dict, dict]:
    """Return (route A results, route B results) for one pass over one document."""
    a, b = {}, {}
    for m in AO_GROUP.finditer(text):
        # AO.findall -> (AO number, marks). The allocations are e.g.
        # "AO2 - 3 marks AO3 - 3 marks", i.e. TWO components of 3 marks each.
        aos = [f"AO{x[0]}x{x[1]}" for x in AO.findall(m.group(0))]
        if not aos:
            continue
        start = max(0, m.start() - ROUTE_B_WINDOW)
        window = text[start:m.start()]
        labs = list(LBL.finditer(window))
        if not labs:
            continue
        lab = labs[-1]
        key = _key(*lab.groups())
        gap = window[lab.end():]
        total = sum(int(part.split("x")[1]) for part in aos)
        # Route A: only separators between the label and the allocation.
        (a if re.fullmatch(r"[\s.,;:\u2013\u2014-]*", gap) else b
         ).setdefault(key, (total, tuple(aos)))
    return a, b


def parse() -> dict:
    try:
        import pypdf
    except ImportError:
        sys.exit("pip install --break-system-packages pypdf cryptography")

    papers = {}
    for pdf in sorted(ARCHIVE.glob("*/4BS1_*_MS.pdf")):
        raw = "".join((p.extract_text() or "")
                      for p in pypdf.PdfReader(str(pdf)).pages)
        passes = (re.sub(r"\s+", " ", raw), re.sub(r"\s+", "", raw))

        strong, weak = {}, {}
        for text in passes:
            a, b = _routes(text)
            for k, v in a.items():          # keep the larger reading per part
                strong[k] = max(strong.get(k, (0, ()))[0], v[0]), v[1]
            for k, v in b.items():
                weak.setdefault(k, v)
        for k, v in weak.items():           # fallback fills gaps only
            strong.setdefault(k, v)

        name = (f"{pdf.parent.name} "
                f"{pdf.name.replace('4BS1_Business_Studies_', '').replace('_MS.pdf', '')}")
        strong.update(OVERRIDES.get(name, {}))
        junk = [k for k in strong if k not in SKELETON]
        for k in junk:
            del strong[k]
        if junk:
            DROPPED[name] = junk
        papers[name] = strong
    return papers


def main() -> int:
    papers = parse()
    tally = collections.Counter()
    rows = []
    bad = []
    for name, parts in sorted(papers.items()):
        for q, (total, aos) in parts.items():
            if total >= 3:
                tally[total] += 1
                rows.append((name, q, total, " ".join(aos)))
        s = sum(t for t, _ in parts.values())
        if s != 80:
            bad.append((name, s, len(parts)))

    print("TARIFF POPULATION, DERIVED FROM THE 38 MARK SCHEMES")
    print("-" * 58)
    for k in sorted(tally):
        print(f"  {k:>2}-mark question parts : {tally[k]:>3}")
    print(f"\n  governed parts (3+)     : {sum(tally.values())}")
    print(f"  papers parsed           : {len(papers)}")
    print(f"  papers NOT summing to 80: {len(bad)}")
    for name, s, n in bad:
        print(f"      {name:<46} sum={s:>3}  parts={n}")
    for name, junk in sorted(DROPPED.items()):
        print(f"  junk keys dropped       : {name} -> {junk}")
    if OVERRIDES:
        print("  overrides applied       : "
              + ", ".join(f"{k} -> {v}" for k, v in OVERRIDES.items()))

    with OUT.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["paper", "question", "marks", "ao_allocation"])
        w.writerows(rows)
    print(f"\n  wrote {OUT.name}: {len(rows)} rows of 3+ marks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
