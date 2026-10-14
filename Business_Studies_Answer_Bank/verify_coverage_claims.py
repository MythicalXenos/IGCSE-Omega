#!/usr/bin/env python3
"""Do the bank's coverage CLAIMS agree with the derived register?

WHY THIS EXISTS
---------------
The bank states which tariff x paper combinations hold a full-mark script in at
least three places, in prose and in table cells:

  * `06_External_Source_Library.md` — the "what is actually still missing" grid;
  * `00_Pearson_Official_Rulebook.md` — the route-by-route statement;
  * `External_Exemplars/2019-06_P1_Official_Exemplar_Booklet.md` — the row about
    which routes are held.

`tally_exemplars.py` proves the REGISTER is complete. Nothing checked that the
prose agrees with it — and on 14 Oct 2026 one of these claims was found to be
wrong in two ways at once: it said "no verified 9/9 **in any series**" while the
grid directly above it said Paper 2R was held twice, and it cited the May 2023
Paper 2 script as Q3(e) when the 7/9 was Q2(f) and Q3(e) had scored 5/9.

**A claim spread across three files is the same failure mode as a total
maintained by hand: it drifts, and every copy agrees with the others only
because they were all typed the same day.** So: derive the truth from the
register, read the claims, and fail on disagreement.

WHAT IT CHECKS
--------------
  1. every tariff x paper cell in `06_`'s grid matches the register count;
  2. no sentence anywhere says a full-mark script does not exist "in any
     series" / "anywhere" for a tier that has one — the phrase "in any series"
     is only true when NO paper holds one;
  3. every `Qn(x)` attached to a full-mark or best-held claim carries the LABEL
     THAT TARIFF USES — a 9-mark claim can only cite 2(f) or 3(e), a 6-mark claim
     1(g), 3(d) or 4(b), a 12-mark claim 4(c).

WHAT IT DOES NOT CHECK, AND THE REASON (found by trying to write it)
-------------------------------------------------------------------
It cannot confirm that a 7/9 was scored on the question a claim cites. **On
14 Oct 2026 `06_` cited "7/9 (May 2023 P2 Q3(e), IKEA)" when the 7/9 was Q2(f)
and Q3(e) had scored 5/9** — and no check here can see that, because **both
labels are real questions of that tariff on that paper.** Only the per-series
mark records distinguish them, and those live in tables whose formats differ
between files (one series file carries 17 such rows, another carries none and
records its marks in prose). **A claim that names a mark and a question must be
read against the series file by hand when it changes** — which is what happened,
and what fixed it.

Run from Business_Studies_Answer_Bank/:  python3 verify_coverage_claims.py
Exit 0 when every claim agrees with the register, 1 otherwise.
"""
import collections
import csv
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve()
BANK = HERE.parent / "Perfect_Answers"
REGISTER = BANK / "09_Verified_Tally.md"

TIERS = {
    12: "Evaluate",
    9: "Justify",
    6: "Analyse",
}
PAPERS = ["P1", "P1R", "P2", "P2R"]


def register_counts():
    """(tariff, paper) -> how many FULL-MARK scripts the register holds.

    Read from the register's own numbers, never from its prose: the section
    headings and the row `P · Q` cells are the data, and `tally_exemplars.py`
    proves every row resolves to a real file and mark token.
    """
    lines = REGISTER.read_text(encoding="utf-8").splitlines()
    tier, counts = None, collections.Counter()
    for line in lines:
        m = re.match(r"^##\s+(\d+)\s+MARKS", line)
        if m:
            tier = int(m.group(1))
            continue
        # ⚠️ THE TIER MUST BE CLEARED AT ANY OTHER SECTION HEADING. This loop used
        # to leave `tier` set until the next tier heading, so every row in every
        # section AFTER "## 3 MARKS" was counted as a 3-mark row. It was invisible
        # for as long as the register's last section was a tier - and on 14 Oct
        # 2026 the 1- and 2-mark sections were added below it, and this check
        # immediately reported the register as holding 49 three-mark scripts when
        # it holds 44. The eight "stale total" FAILs it printed were its own bug,
        # not the bank's. `tally_exemplars.py` had this reset all along; this
        # function did not.
        if line.startswith("## "):
            tier = None
        if tier and re.match(r"^\|\s*\d+\s*\|", line):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            r = re.search(r"\b(P\dR?)\b", cells[2])
            if r:
                counts[(tier, r.group(1))] += 1
    return counts


def claimed_grid():
    """`06_`'s grid: (tariff, paper) -> the cell's own words."""
    text = (BANK / "06_External_Source_Library.md").read_text(encoding="utf-8")
    rows = {}
    for line in text.splitlines():
        m = re.match(r"^\|\s*\*\*(Analyse|Justify|Evaluate)\s*\((\d+)\)\*\*\s*\|", line)
        if not m:
            continue
        tariff = int(m.group(2))
        cells = [c.strip() for c in line.strip().strip("|").split("|")][1:]
        for paper, cell in zip(PAPERS, cells):
            rows[(tariff, paper)] = cell
    return rows


# The label a tariff uses. Derived from the qualification, not typed: every
# 4BS1 paper prints its governed parts in the same slots (see
# build_layer_c_tariffs.py). If a claim cites a label outside its tier's set, the
# claim is about a different question.
TIER_LABELS = {
    12: {"4(c)"},
    9: {"2(f)", "3(e)"},
    6: {"1(g)", "3(d)", "4(b)"},
    3: {"1(f)", "2(c)", "2(d)", "2(e)"},
}
# a claim citation, e.g. "**(May 2023 P2 Q3(e)**" or "7/9 (May 2023 P2 Q3(e)"
# Deliberately loose: the bank writes both "7/9 (May 2023 P2 Q3(e), IKEA)" and
# "**May 2023 P2 Q2(f)** (IKEA, ...)". Requiring a bracket before the paper matched
# ONE citation out of the six present - a near-empty parse inside a check that
# printed OK, which is the exact failure this bank has recorded twice. The line
# filter (tier mark + a held/none/best-held word) is what scopes it.
CLAIM_CITE = re.compile(r"\b(P\dR?)\s*Q\s*(\d)\s*\(\s*([a-z])\s*\)")


def label_claims():
    """(file, tier, paper, question label) for every citation in coverage prose."""
    out = []
    for f in sorted(BANK.rglob("*.md")):
        text = f.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            tier, pos = None, None
            m = re.search(r"\b(\d+)/9\b", line)
            if m:
                tier, pos = 9, m.start()
            m = re.search(r"\b(\d+)/12\b", line)
            if m:
                tier, pos = 12, m.start()
            else:
                m = re.search(r"\b(\d+)/6\b", line)
                if m:
                    tier, pos = 6, m.start()
            if tier is None:
                continue
            # THE CUE MUST SIT NEXT TO THE NUMBER, not anywhere on the line.
            # This filter began as a whole-line search, and a 900-character
            # paragraph of prose can contain both an "N/6" and, hundreds of
            # characters away, an unrelated "held" - which is exactly how a
            # true sentence about a layout trap was reported as claiming a
            # 6-mark full mark for a 3-mark question. 120 characters keeps
            # every real claim, because a real one is written as a phrase
            # ("no verified 9/9 for Paper 2R", "the best held is 11/12").
            cue = re.search(r"held|none|no verified|best held|gap", line, re.I)
            if not cue or not (pos - 120 <= cue.start() <= pos + 120):
                continue
            for c in CLAIM_CITE.finditer(line):
                out.append((f.relative_to(BANK), tier, c.group(1).upper(),
                            f"{c.group(2)}({c.group(3)})"))
    return out


def main() -> int:
    counts = register_counts()
    grid = claimed_grid()
    problems = []

    print("=" * 74)
    print("COVERAGE CLAIMS vs THE REGISTER — full-mark scripts by tariff and paper")
    print("=" * 74)
    print(f"  register: {sum(counts.values())} rows read  "
          f"({', '.join(f'{n} x {t}-mark' for t, n in sorted(collections.Counter(k[0] for k in counts.elements()).items()))})")
    print()
    print(f"  {'tariff':<10}" + "".join(f"{p:>26}" for p in PAPERS))
    for tier in (6, 9, 12):
        cells = []
        for p in PAPERS:
            n = counts[(tier, p)]
            claim = grid.get((tier, p), "(no cell)")
            # "still none" / "none published" = not held.
            # "best held is 11/12" = ALSO not held - the word "held" appears in a
            # phrase that says no FULL-mark script is held, and reading it as a
            # claim of one is a false alarm that would train the reader to ignore
            # the check.
            low = claim.lower()
            if "best held" in low or "⚠️" in claim or "none" in low:
                held = False
            else:
                held = "✅" in claim or "held" in low
            ok = held if n else not held
            cells.append(f"{n:>3} {claim[:16]:<17}{'' if ok else '  ← MISMATCH'}")
            if not ok:
                problems.append(f"{tier}-mark {p}: register holds {n}, grid says {claim!r}")
        print(f"  {TIERS[tier]+' ('+str(tier)+')':<10}" + "".join(f"{c:>26}" for c in cells))

    # ---- "in any series" phrasing ------------------------------------------
    print()
    print("=" * 74)
    print('ABSOLUTE CLAIMS — "no full-mark script ... in any series"')
    print("=" * 74)
    any_phrases = re.compile(r"no (?:verified )?(?:full-mark |)\d+/\d+[^.]{0,60}(?:in any series|anywhere|any series)", re.I)
    hits = 0
    for f in sorted(BANK.rglob("*.md")):
        for line in f.read_text(encoding="utf-8", errors="replace").splitlines():
            for m in any_phrases.finditer(line):
                hits += 1
                phrase = m.group(0)
                tier = int(re.search(r"(\d+)/\d+", phrase).group(1))
                # Work on the CLAIM'S OWN SENTENCE, not the whole line. A
                # correction note sits in a later sentence on the same line, so
                # testing the whole line both skips live claims and scopes them to
                # the wrong papers. (Both of those happened while writing this.)
                # The window runs from the sentence boundary BEFORE the phrase to
                # the one after it. A correction note puts its marker before the
                # quoted phrase ("This bullet previously read \"no verified 9/9 ...\""),
                # so a forward-only window cannot see it and the correction is
                # reported as a live error.
                head = line[:m.start()]
                prev = list(re.finditer(r"[.!?](?=\s|[*_])", head))
                start_at = prev[-1].end() if prev else 0
                tail = line[m.start():]
                # A sentence ending in markdown ("in any series.**") has a period
                # followed by '*', not whitespace - matching only "\.\s" runs the
                # window on into the NEXT sentence and picks up its Paper 1 mention.
                stop = re.search(r"\.(?=\s|[*_])", tail)
                sentence = line[start_at: m.start() + (stop.end() if stop else len(tail))]

                # A CORRECTION NOTE NECESSARILY QUOTES THE WRONG WORDING. The bank
                # records its own past errors, so a bare phrase match reports the
                # correction as the error - but ONLY when the correction is in the
                # sentence the phrase sits in.
                # Two ways a sentence can be RECORDING a claim rather than making
                # one, and both are needed: an explicit marker ("previously read",
                # "was wrong"), or the phrase sitting INSIDE QUOTATION MARKS - which
                # is how this bank quotes a claim it is correcting. The first run of
                # this rule flagged its own correction note in 08_ because the marker
                # was there but the test looked at the gap between two quotes.
                quoted = (line[:m.start()].count('"') % 2 == 1
                          or line[:m.start()].count("\u201c") > line[:m.start()].count("\u201d"))
                if quoted or re.search(r"previously read|used to read|This said|was wrong"
                                       r"|was not updated|no longer read|this row was written"
                                       r"|this bullet|\bsaid\b|\bread\b|\bclaim(?:ed)?\b|\bwrote\b"
                                       r"|\bworded\b|\bphrased\b|\bquoted\b", sentence, re.I):
                    print(f"  SKIP {f.name}: {phrase[:60]!r} (a recorded past claim, quoted in its correction)")
                    continue

                # If the claim NAMES papers, it is scoped to them: "no 12/12 for
                # Paper 2 or Paper 2R" is TRUE even though Paper 1 holds two. Only
                # an unscoped "anywhere" is a claim about the whole bank. `\b` after
                # the number is what keeps "Paper 2" out of "Paper 2R".
                named = [pp for pp in ("P1R", "P2R", "P1", "P2")
                         if re.search(rf"Paper\s*{pp[1:]}\b", sentence)]
                scope = named or PAPERS
                bad = [pp for pp in scope if counts[(tier, pp)]]
                flag = "OK  " if not bad else "FAIL"
                scope_txt = f"scoped to {','.join(named)}" if named else "UNSCOPED"
                print(f"  {flag} {f.name}: {phrase[:70]!r} ({scope_txt})")
                if bad:
                    have = ", ".join(f"{counts[(tier, pp)]} on {pp}" for pp in bad)
                    problems.append(f"{f.name}: claims no {tier}-mark full mark for "
                                    f"{'/'.join(bad)}, but the register holds {have}")
    if not hits:
        print("  none found.")

    # ---- rule 3: does the label belong to the tariff the claim is about? -----
    print()
    print("=" * 74)
    print("TARIFF vs LABEL — a claim's Q number must be one that tariff uses")
    print("=" * 74)
    cites = label_claims()
    bad_labels = [(f, tier, paper, q) for f, tier, paper, q in cites
                  if q not in TIER_LABELS[tier]]
    print(f"  coverage citations carrying a question label: {len(cites)}")
    if len(cites) < 5:
        print(f"  ⚠️ only {len(cites)} parsed — that is too few for this bank: CHECK THE PARSER.")
        problems.append(f"the citation parser found only {len(cites)} labels; it should find "
                        f"every Q number in the coverage prose")
    for f, tier, paper, q in bad_labels:
        print(f"  FAIL {f} — a {tier}-mark claim cites {paper} Q{q}, "
              f"but a {tier}-mark question is {sorted(TIER_LABELS[tier])[0]}-style")
        problems.append(f"{f}: {tier}-mark claim cites {paper} Q{q}")
    if cites and not bad_labels:
        print("  every label belongs to the tariff of its claim.")

    # ---- total claims: "19 x 6/6" anywhere must be the register's own count ---
    # The grid check above reads cells; a TOTAL in a sentence is a different claim
    # and nothing was reading it. 06_ said "(19 x 6/6 ...)" while the register held
    # 23 - the same class of stale summary this bank has now caught in six places.
    print()
    print("=" * 74)
    print("STATED TOTALS - every 'N x T/T' anywhere in the bank against the register")
    print("=" * 74)
    total = collections.Counter()
    for (tier, _paper), n in counts.items():
        total[tier] += n
    total_claims, total_bad = 0, []
    # SCAN THE WHOLE ANSWER BANK, NOT ONLY Perfect_Answers/. The register is
    # quoted in the top-level README too, and this section originally walked
    # Perfect_Answers/ alone - so a stale total in a README that no check
    # covered would have survived every run. Found while sweeping the totals
    # after the May 2023 scripts were banked.
    for f in sorted(BANK.parent.rglob("*.md")):
        text = f.read_text(encoding="utf-8", errors="replace")
        for i, line in enumerate(text.splitlines(), 1):
            for m in re.finditer(r"(?<![\d/])(\d+)\s*[x\u00d7]\s*(3|6|9|12)/(?:3|6|9|12)\b", line):
                # A QUOTED total is a recorded past claim, not a live one - the same
                # rule the absolute-claims section uses. `09_` quotes its own old
                # totals precisely so the drift stays visible ("the bank now holds
                # six 9/9s" above a list of fourteen), and those must not be read as
                # current statements.
                before = line[:m.start()]
                if before.count('"') % 2 or before.rfind("\u201c") > before.rfind("\u201d"):
                    continue
                n, tier = int(m.group(1)), int(m.group(2))
                if n == tier and n in (3, 6, 9, 12) and "3/3" not in m.group(0):
                    pass
                total_claims += 1
                if total[tier] and n != total[tier]:
                    # ⚠️ THIS LINE CRASHED FOR ANY FILE OUTSIDE Perfect_Answers/.
                    # When this section was widened to scan the whole answer bank
                    # (14 Oct 2026, to catch a stale total in the top-level
                    # README), `f.relative_to(BANK)` raised for those files - and
                    # it raised INSIDE the failure branch, so the effect was that
                    # this check could not report a mismatch in any file it had
                    # just been widened to cover. A check must fail with a
                    # message, never with a traceback.
                    try:
                        where = str(f.relative_to(BANK))
                    except ValueError:
                        where = str(f.relative_to(BANK.parent))
                    total_bad.append((where, i, m.group(0).strip(), tier, n))
    print(f"  total claims found: {total_claims}   mismatching: {len(total_bad)}")
    if not total_claims:
        print("  NONE PARSED - check the parser, not the bank.")
    for where, i, claim, tier, n in total_bad:
        print(f"  FAIL {where}:{i} says {claim!r}; the register holds {total[tier]} at {tier} marks")
        problems.append(f"{where}:{i} states {n} at {tier} marks; register holds {total[tier]}")
    if total_claims and not total_bad:
        print("  every stated total equals the register's count.")
        print(f"    (3/3 = {total[3]}, 6/6 = {total[6]}, 9/9 = {total[9]}, 12/12 = {total[12]})")

    # ------------------------------------------------------------------
    # WITHDRAWN FIGURES — a retracted number must never look current.
    #
    # Five times now a superseded total has been found alive in a file that no
    # check read (06_:1925, 08_:417, both READMEs, the reader-facing guide) -
    # every one of them found by eye. The bank is allowed to RECORD a number it
    # has withdrawn; what it must never do is STATE one. So: if a retired figure
    # appears, its neighbourhood must say so.
    #
    # Keyed on the PHRASES the bank actually used, never on bare numbers: 111 is
    # also a grade-9 boundary, 86 is also a currency answer, 48 and 17 are also
    # boundary marks. A check that flags the boundary tables would be ignored
    # within a week - and a check that is ignored is worse than none.
    # ------------------------------------------------------------------
    print()
    print("=" * 74)
    print("WITHDRAWN FIGURES - every retired number must be standing next to its correction")
    print("=" * 74)
    RETIRED = [
        (re.compile(r"\b977\s+items"), "the pre-repair item total (true: 988)"),
        (re.compile(r"\b595\s+one- and two-mark"), "the pre-repair 1+2-mark count (true: 608)"),
        (re.compile(r"\b443\s*\+\s*152"), "the pre-repair 1-mark breakdown (true: 456 + 152)"),
        (re.compile(r"\b382\s+level-based"), "the pre-repair governed count (true: 380)"),
        (re.compile(r"\b696\s+standalone question-mark lines"), "the extraction's item count"),
        (re.compile(r"\b696-row\b"), "the extraction's item count"),
        (re.compile(r"%\s+of\s+696\b"), "a percentage against the withdrawn population"),
        (re.compile(r"\b328\s+one-mark"), "the extraction's one-mark count (true: 456)"),
        (re.compile(r"\b106\s+two-mark"), "the extraction's two-mark count (true: 152)"),
        (re.compile(r"\b111\s+three-mark"), "the extraction's 3-mark count (true: 152)"),
        (re.compile(r"\b86\s+six-mark"), "the extraction's 6-mark count (true: 114)"),
        (re.compile(r"\b48\s+nine-mark"), "the extraction's 9-mark count (true: 76)"),
        (re.compile(r"\b17\s+twelve-mark"), "the extraction's 12-mark count (true: 38)"),
    ]
    # A retired figure is safe when the reader is told it is retired. The window is
    # generous because a markdown table cannot carry a paragraph: 04_ announces the
    # withdrawal in a boxed block and then prints the % of 696 column beneath it.
    TELLS = ("withdrawn", "superseded", "corrected", "used to say", "no longer",
             "previously", "retracted", "under-detect", "not the csv", "recorded",
             "old figure", "old count", "old total", "\u26a0\ufe0f")
    WINDOW = 12
    retired_hits, retired_bad = 0, []
    for f in sorted(BANK.parent.rglob("*.md")):
        lines = f.read_text(encoding="utf-8", errors="replace").splitlines()
        for i, line in enumerate(lines, 1):
            for pat, what in RETIRED:
                if not pat.search(line):
                    continue
                retired_hits += 1
                lo, hi = max(0, i - 1 - WINDOW), min(len(lines), i + WINDOW)
                if not any(t in " ".join(lines[lo:hi]).lower() for t in TELLS):
                    retired_bad.append((str(f.relative_to(BANK.parent)), i, pat.search(line).group(0), what))
    print(f"  retired figures found: {retired_hits}   unmarked: {len(retired_bad)}")
    if not retired_hits:
        print("  NONE PARSED - check the registry, not the bank.")
    for where, i, found, what in retired_bad:
        print(f"  FAIL {where}:{i} states {found!r} with no correction nearby - {what}")
        problems.append(f"{where}:{i} states the withdrawn {found!r} as if current")
    if retired_hits and not retired_bad:
        print("  every retired figure in the bank is standing next to its correction.")

    print()
    if problems:
        print("=" * 74)
        print(f"CLAIMS THAT DISAGREE WITH THE REGISTER — {len(problems)}")
        print("=" * 74)
        for p in problems:
            print("  " + p)
    print("RESULT:", "OK — every coverage claim agrees with the register."
          if not problems else f"FAIL — {len(problems)} claim(s) contradict the register.")
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
