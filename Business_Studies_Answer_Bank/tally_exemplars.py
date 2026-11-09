#!/usr/bin/env python3
"""Verify the verified-exemplar register, and flag anything unregistered.

WHY THIS EXISTS
---------------
The bank carried hand-written counts ("the bank now holds six 9/9s") sitting
directly above a list of fourteen. A hand-written total is an assertion; a
derived total is evidence.

The first version of this script simply counted *headings* that name a mark.
That was worse than useless in a subtle way: it printed **17 / 14 / 4** against a
register of **19 / 15 / 2**, because it also counted

  * rule sections that discuss "THE 9/9" or "THE 12/12" without printing one,
  * cross-references to a script whose transcript lives in another file, and
  * repeated references to the same script.

A count that is wrong in a *new* way every time it is run is not evidence either.

WHAT IT DOES NOW
----------------
1. **Parses the register itself** — `09_Verified_Tally.md` — and treats it as
   the source of truth: one row per distinct full-mark script, each with a
   canonical `file:line`.
2. **Checks every row resolves** — the file exists and the line it names carries
   the mark token. A register row pointing at nothing is a broken claim.
3. **Scans the whole bank for script-bearing headings and matches them to the
   register.** A heading is *script-bearing* if it names a question label
   (`Q2(f)`, `Q4(c)`) or one of the register's case studies. Everything else is
   narrative and is ignored — that is the restatement filter, and it is why this
   script no longer counts a rule heading as a lost script.
4. **Prints any heading that is script-bearing and NOT accounted for by the
   register.** That list is the only thing worth reading. An empty list means
   the register is complete against the bank's own prose.

Exit code is 0 when the register verifies and 1 when it does not, so this can be
run as a check rather than read as a report.

Run from Business_Studies_Answer_Bank/:  python3 tally_exemplars.py
"""
import re, sys, pathlib, collections, json

ROOT = pathlib.Path(__file__).parent / "Perfect_Answers"
REGISTER = ROOT / "09_Verified_Tally.md"
TOKEN = re.compile(r"(?<![\d/])(3/3|6/6|9/9|12/12)(?![\d/])")
ROW = re.compile(r"^\|\s*\d+\s*\|(.+)\|\s*`([^`]+?):(\d+)`\s*\|\s*$")
QLABEL = re.compile(r"\bQ\s?(\d)\s?\(([a-z])\)")
RULEY = re.compile(r"^\s*(?:\d+\.|#{2,4}\s*\d+\.)|ANATOMY|WHAT THIS|HOW TO|THE TEST|"
                   r"REQUIRED FEATURES|NON-NEGOTIABLE|CHECKLIST", re.I)


def parse_register():
    """Return [(tariff, label_text, file, line)] from the register's tables."""
    rows, tariff = [], None
    for line in REGISTER.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^##\s*(12|9|6|3|2|1)\s*MARKS?\b", line)
        if m:
            # 3 joined the register on 14 Oct 2026 (four June 2026 Explain
            # scripts). It was left out of this regex at first, which made this
            # script print TOTAL: 40 while verify_coverage_claims.py printed 44
            # from the same file - two checks disagreeing about the same data is
            # exactly the failure this script exists to prevent.
            # 1 and 2 joined on 14 Oct 2026, when the archive was found to print
            # 80 marked scripts for the tier the register had dismissed as
            # "Pearson publishes no scripts". They are held, not modelled - but a
            # row that nothing verifies is not evidence, so they are parsed and
            # resolved by the same code as every other row.
            tariff = {"1": "1/1", "2": "2/2", "3": "3/3", "6": "6/6",
                      "9": "9/9", "12": "12/12"}[m.group(1)]
            continue
        if line.startswith("## "):
            tariff = None
        if tariff and (rm := ROW.match(line)):
            label, f, ln = rm.group(1), rm.group(2).strip(), int(rm.group(3))
            rows.append((tariff, label, f, ln))
    return rows


def resolve(rows):
    """Every register row must point at a real file and a line carrying the mark."""
    bad = []
    for tariff, label, f, ln in rows:
        path = ROOT / f
        if not path.exists():
            # register also cites files by a shortened name (e.g. "2023-05_Series…md")
            hits = list(ROOT.rglob(f.split(":")[0])) if "/" not in f else []
            if not hits:
                bad.append((tariff, label, f, ln, "file not found"))
                continue
            path = hits[0]
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        # LOOK MOSTLY BACKWARD, AND EIGHT LINES OF IT. A mark statement introduces
        # the response beneath it: `2023-06_P2_IKEA.md` announces "3/3 x2" in one
        # heading and quotes the two scripts under it, and the second-pass table
        # states "3/3" in its column header with six responses below. A ±4 window
        # read those two rows as unresolved - a false alarm that would train the
        # reader to ignore the section it protects.
        window = lines[max(0, ln - 8): ln + 4]
        # a row may be sourced to a heading that states the mark in words
        # ("Level 3 – 6 marks — FULL MARKS") rather than as "6/6".
        # The figure pattern is derived from the row's OWN tariff rather than
        # from the global TOKEN. TOKEN is deliberately fixed at 3/6/9/12 because
        # it drives the bank-wide heading scan; deriving it here is what lets the
        # 1- and 2-mark rows resolve without widening that scan.
        n = int(tariff.split("/")[0])
        figure = re.compile(rf"(?<![\d/]){re.escape(tariff)}(?![\d/])")
        words = re.compile(rf"(?<![\d/]){n}(?![\d/])\s*marks?\b", re.I)
        if not any(figure.search(w) or words.search(w) for w in window):
            bad.append((tariff, label, f, ln, "no mark token near that line"))
    return bad


def register_labels(rows):
    """Question labels and case names the register knows about."""
    labels, names = set(), set()
    for tariff, label, f, ln in rows:
        for q in QLABEL.findall(label):
            labels.add((tariff, f"q{q[0]}{q[1]}"))
        for tok in re.split(r"[^A-Za-z]+", label):
            if len(tok) > 3 and tok[0].isupper():
                names.add(tok.lower())
    return labels, names


def scan(heading_only=True):
    out = []
    for f in sorted(ROOT.rglob("*.md")):
        for i, line in enumerate(f.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if not line.lstrip().startswith("#"):
                continue
            if "not counted" in line:
                continue
            tok = TOKEN.search(line)
            if not tok:
                continue
            out.append((tok.group(1), str(f.relative_to(ROOT)), i, line.strip("# ").strip()))
    return out


# ==============================================================================
# CITATION AGREEMENT — the file a row cites must belong to the session the row
# names. Added 14 Oct 2026, after the eleven May 2023 scripts were banked: a
# probe asked whether ANY check would notice a register row whose stated session
# disagreed with the file it cites, and only audit_er_fullmarks.py did - and it
# only looks at five reports. A row reading "Jun 2024" while pointing into a
# 2023-05 file would have passed every one of the other twenty-two checks.
#
# ⚠️ THE MONTH RULE IS DELIBERATELY LOOSE, AND HERE IS WHY. Pearson runs one
# "May/June" series and the archive folder names it May_2023 while the register
# names it Jun 2023 - both are correct names for the same series, so a probe
# that demanded an exact month match reported 14 false mismatches, every one of
# them in the May 2023 files. May and June are therefore the same session here;
# any other month difference, or any year difference, is a real disagreement.
#
# The paper rule only fires where both sides state a paper: the row ("P2R Q1(f)")
# and the enclosing level-1 section of the cited file ("# PAPER 2R"). A row is
# never failed for citing a file that does not section its scripts by paper.
# ==============================================================================
CITE_DATE = re.compile(r"(20\d\d)-(\d\d)(?!\d)")
CITE_SESSION = re.compile(r"\b(May/Jun|Jun|May|Nov|Jan)\s*(20\d\d)\b")
CITE_PART = re.compile(r"\bP(\d)(R?)\s*Q\s*(\d)\s*\(\s*([a-z])\s*\)")
CITE_PAPER_SECTION = re.compile(r"^#\s+PAPER\s+(\d)(R?)\b")
SERIES_MONTHS = {"05": "mayjune", "06": "mayjune", "01": "jan", "11": "nov"}


def citation_agreement(rows):
    """[(severity, message)] for every row whose citation contradicts the row."""
    out, seen_ses, seen_paper = [], 0, 0
    for tariff, label, f, ln in rows:
        path = ROOT / f
        if not path.exists():
            hits = list(ROOT.rglob(f))
            if not hits:
                continue
            path = hits[0]

        sm = CITE_SESSION.search(label)
        dm = CITE_DATE.search(path.name)
        if sm and dm:
            seen_ses += 1
            want_m = {"Jan": "01", "May": "05", "Jun": "06", "Nov": "11"}.get(sm.group(1), "")
            same_series = sm.group(1) == "May/Jun" or SERIES_MONTHS.get(dm.group(2)) == SERIES_MONTHS.get(want_m)
            if sm.group(2) != dm.group(1) or not same_series:
                out.append(("session",
                            f"{f} — row {ln} says {sm.group(0)} but cites {path.name} "
                            f"({dm.group(0)})"))

        pm = CITE_PART.search(label)
        if pm:
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
            section = None
            for line in reversed(lines[: max(0, ln - 1)]):
                sec = CITE_PAPER_SECTION.match(line)
                if sec:
                    section = (sec.group(1), sec.group(2))
                    break
            if section:
                seen_paper += 1
                if section != (pm.group(1), pm.group(2)):
                    out.append(("paper",
                                f"{f} — row {ln} says P{pm.group(1)}{pm.group(2)} "
                                f"but the script sits under PAPER {section[0]}{section[1]}"))
    return out, seen_ses, seen_paper


def main():
    rows = parse_register()
    bad = resolve(rows)
    labels, names = register_labels(rows)
    counts = collections.Counter(t for t, *_ in rows)

    print("=" * 78)
    print("REGISTER — 09_Verified_Tally.md")
    print("=" * 78)
    for t in ("3/3", "6/6", "9/9", "12/12"):
        print(f"  {t}: {counts[t]} rows")
    print(f"  TOTAL: {sum(counts.values())}")
    print()
    if bad:
        print("!! ROWS THAT DO NOT RESOLVE")
        for t, label, f, ln, why in bad:
            print(f"   {t}  {f}:{ln}  ({why})  {label[:60]}")
    else:
        print("OK  every register row resolves to a real file and a real mark token.")

    print()
    print("=" * 78)
    print("CANDIDATE HEADINGS FOUND IN THE BANK")
    print("=" * 78)
    unaccounted, narrative, matched = [], 0, 0
    for tariff, f, ln, txt in scan():
        qs = QLABEL.findall(txt)
        key = f"q{qs[0][0]}{qs[0][1]}" if qs else None
        if key and (tariff, key) in labels:
            matched += 1
            continue
        named = {t.lower() for t in re.split(r"[^A-Za-z]+", txt) if len(t) > 3}
        if named & names:
            matched += 1
            continue
        if RULEY.search(txt) or not key:
            narrative += 1
            continue
        unaccounted.append((tariff, f, ln, txt))

    print(f"  matched to a register row : {matched}")
    print(f"  narrative / rule headings : {narrative}   (ignored — the restatement filter)")
    print(f"  UNACCOUNTED               : {len(unaccounted)}")
    for tariff, f, ln, txt in unaccounted:
        print(f"    !! {tariff}  {f}:{ln}  {txt[:90]}")

    # ---- the file's own totals, against its own rows -----------------------
    # `09_` was written BECAUSE hand-incremented totals had drifted five times.
    # On 14 Oct 2026 its headline table had drifted too: it said 6-mark = 19
    # while the table below it held 23, and it had no 3-mark row at all, because
    # a tier can be added to the body of a file without the summary following it.
    # This is the check that makes that impossible: every total the file states
    # must equal the number of rows the file has.
    print()
    print("=" * 78)
    print("THE FILE'S OWN TOTALS — every stated total against the rows that back it")
    print("=" * 78)
    text = REGISTER.read_text(encoding="utf-8")
    stated = {}
    m = re.search(r"## HEADLINE COUNT\n(.*?)\n\n", text, re.S)
    if not m:
        stated_bad = ["09_ has no HEADLINE COUNT table — parser or file has changed"]
        print("  !! could not find the HEADLINE COUNT table")
    else:
        stated_bad = []
        for cell, tariff in re.findall(r"\|\s*\*\*(12|9|6|3|2|1)-mark \w+\*\*\s*\|\s*\*\*(\d+)\*\*", m.group(1)):
            key = f"{int(cell)}/{int(cell)}"
            stated[f"{cell}-mark"] = (int(tariff), counts[key])
        for tier, (paper, truth) in stated.items():
            flag = "ok " if paper == truth else "FAIL"
            print(f"  {flag} headline {tier:<9} says {paper:>3}   rows in the register: {truth:>3}")
            if paper != truth:
                stated_bad.append(f"the headline table's {tier} count is {paper}; the register has {truth}")
        missing = [t for t in ("1-mark", "2-mark", "3-mark", "6-mark", "9-mark", "12-mark")
                   if t not in stated]
        if missing:
            print(f"  FAIL headline table has no row for: {missing}")
            stated_bad.append(f"the headline table omits {missing} — a tier can be added to the body without following the summary")

    # section headings: "## 6 MARKS — **23 scripts**"
    for cell, paper in re.findall(r"^## (12|9|6|3|2|1) MARKS? — \*\*(\d+) scripts?\*\*", text, re.M):
        key = f"{int(cell)}/{int(cell)}"
        ok_s = int(paper) == counts[key]
        print(f"  {'ok ' if ok_s else 'FAIL'} section heading {cell} MARKS says {paper:>3}   "
              f"rows under it: {counts[key]:>3}")
        if not ok_s:
            stated_bad.append(f"the {cell}-mark section heading says {paper}; it holds {counts[key]} rows")

    # the prose count of rows that resolve: "All N rows resolve"
    for paper in re.findall(r"\*\*All (\d+) rows resolve", text):
        ok_r = int(paper) == sum(counts.values())
        print(f"  {'ok ' if ok_r else 'FAIL'} prose says {paper} rows resolve   "
              f"rows: {sum(counts.values())}")
        if not ok_r:
            stated_bad.append(f"the prose says {paper} rows resolve; there are {sum(counts.values())}")

    # ---- headings that STATE a full mark must resolve to a register row ----
    # A heading is what a reader skims and what a pattern matches, so a heading
    # that states "6/6" has made a claim. On 14 Oct 2026 one read
    # "## 6/6 - wait, 5/6 - P2 Q4(b) ... Level 3, 5 marks": the paper awarded 5,
    # and the heading led with 6. Every other full-mark heading in the bank
    # resolved to a register row; that one resolved to nothing, which is the
    # signal.
    print()
    print("=" * 78)
    print("FULL-MARK HEADINGS — every heading stating a full mark against the register")
    print("=" * 78)
    HEAD = re.compile(r"^(#{2,5})\s*.*?\b(\d{1,2})/(\d{1,2})\b.*$")
    # PAPER-AWARE keys, built from the register rows themselves. `register_labels()`
    # builds two-tuples of (tier, question) with no paper, which is right for its
    # own job but wrong here: it would let a P1R heading be satisfied by a P1 row.
    reg_keys = set()
    for _t, _label, _f, _ln in rows:
        _q = re.search(r"Q(\d)\((\w)\)", _label)
        _p = re.search(r"\bP(\d)(R?)\b", _label)
        if _q and _p:
            reg_keys.add((f"{_t}", f"P{_p.group(1)}{_p.group(2)}", f"q{_q.group(1)}{_q.group(2)}"))
    heading_rows, heading_bad = 0, []
    for f in sorted(ROOT.rglob("*.md")):
        for i, line in enumerate(f.read_text(encoding="utf-8", errors="replace").split("\n"), 1):
            if not line.lstrip().startswith("#"):
                continue
            h = HEAD.match(line)
            if not h:
                continue
            a, b = int(h.group(2)), int(h.group(3))
            if a != b or b not in (3, 6, 9, 12):
                continue
            q = QLABEL.search(line)
            pp = re.search(r"\bP(\d)(R?)\b", line)
            if not (q and pp):
                continue
            heading_rows += 1
            key = (f"{b}/{b}", f"P{pp.group(1)}{pp.group(2)}", f"q{q.group(1)}{q.group(2)}")
            if key not in reg_keys:
                heading_bad.append((str(f.relative_to(ROOT)), i, line.strip()[:96]))
    print(f"  headings stating a full mark with a paper and a question: {heading_rows}")
    if not heading_rows:
        print("  NONE PARSED - check the parser, not the bank.")
        stated_bad.append("the full-mark heading scan parsed nothing")
    for f, i, txt in heading_bad:
        print(f"  !! {f}:{i}")
        print(f"       {txt}")
        stated_bad.append(f"{f}:{i} states a full mark that no register row backs: {txt[:70]}")
    if heading_rows and not heading_bad:
        print("  every one resolves to a register row.")

    # ---- every full-mark HEADING must be CITED BY ITS OWN ROW -------------
    # THE CHECK THAT WOULD HAVE CAUGHT THE 3-MARK UNDER-COUNT OF 14 OCT 2026.
    #
    # The register held FOUR 3-mark rows while the bank held THIRTY-TWO, and
    # every check passed. The reason: a heading was "matched" to a row on
    # (tariff, question) alone, so `2022-06_P1_TBTS.md` Q2(c) - a June 2022
    # Paper 1 answer - was quietly satisfied by the June 2026 P1R row for Q2(c).
    # A PAPER-BLIND KEY AGAIN; the same mistake verify_coverage_claims.py had
    # already had to fix once.
    #
    # A citation cannot be paper-blind. So: if a heading announces a full mark,
    # a register row must point at it, within eight lines. Anything else is
    # either a narrative heading or a cross-reference to a script registered
    # elsewhere, and both are listed in EXEMPT below, with the reason, so a
    # reader can see that the exception was considered rather than missed.
    print()
    print("=" * 78)
    print("CITATION OF FULL-MARK HEADINGS — a heading must be pointed at by its own row")
    print("=" * 78)
    # Exemptions are keyed by a FRAGMENT OF THE HEADING, not by line number. The line-number
    # form drifted every time a file above the heading was edited, and a stale line number
    # turns a considered exemption into a false alarm -- which is the failure mode this whole
    # bank has been burned by twice.
    EXEMPT = {
        # narrative headings - they state a mark to TALK about it, not to claim it
        ("02_Verified_Exemplars.md", "perfect 3/3"): "narrative",
        ("02_Verified_Exemplars.md", "perfect 6/6"): "narrative - the 'throughout' test",
        ("02_Verified_Exemplars.md", "Both routes score 9/9"): "narrative - both routes to 9/9",
        ("02_Verified_Exemplars.md", "'throughout'"): "narrative",
        ("02_Verified_Exemplars.md", "separate 9/9 from 7/9"): "narrative",
        ("02_Verified_Exemplars.md", "19/9"): "narrative",
        ("02_Verified_Exemplars.md", "perfect 9/9"): "narrative",
        ("External_Exemplars/2019-06_P2_Official_Exemplar_Booklet.md", "5/6"): "narrative",
        ("External_Exemplars/2019-06_P2_Official_Exemplar_Booklet.md", "2/6"): "narrative",
        ("External_Exemplars/2023-05_Series_Irsi_AudeRose_IKEA_MM.md", "9/9 comment"): "narrative",
        ("External_Exemplars/2023-05_Series_Irsi_AudeRose_IKEA_MM.md", "separates 6/6"): "narrative",
        ("External_Exemplars/2023-05_Series_Irsi_AudeRose_IKEA_MM.md", "level-phrasing"): "umbrella heading",
        # cross-references - the same script is transcribed twice and a row has ONE source
        ("02_Verified_Exemplars.md", "three sentences"): "second transcription (Cadbury:156)",
        ("02_Verified_Exemplars.md", "Café Pinch"): "second transcription",
        ("02_Verified_Exemplars.md", "FOUR FULL-MARK VERDICTS"): "umbrella over the four May 2023 9/9s",
        ("02_Verified_Exemplars.md", "second **12/12**"): "same script as the May 2023 12/12",
        ("02_Verified_Exemplars.md", "a second **12/12**"): "same script as the May 2023 12/12",
        ("02_Verified_Exemplars.md", "and it has NO conclusion"): "register row 2, cited in External_Exemplars",
        # 16_ is a COMPARISON of the five registered 12/12s: its headings name the count
        # on purpose and the scripts are registered at rows 1-4 of the 12-mark table.
        ("16_Five_Verified_Twelve_Markers.md", "five verified 12/12s"): "umbrella over register rows 1-4",
        ("16_Five_Verified_Twelve_Markers.md", "What no 12/12 does"): "rule heading, not a script",
        ("16_Five_Verified_Twelve_Markers.md", "checked across all five"): "rule heading, not a script",
        ("External_Exemplars/2025-06_Series_CCT_Starbucks_Rabanne.md", "CCT"): "same script as 02_Verified_Exemplars.md",
        # the June 2025 pair is registered at its canonical transcription in
        # 02_Verified_Exemplars.md: row 17 (Four Fitness 6/6, :879) and row 15 (Rabanne
        # 9/9, :840). The addendum and the CCT file both re-transcribe them, and a row
        # has one canonical source.
        ("External_Exemplars/2025-06_Second_Pass_Addendum.md", "TENTH VERIFIED"): "umbrella over register row 17",
        ("External_Exemplars/2025-06_Second_Pass_Addendum.md", "Four Fitness"): "register row 17, cited at 02_Verified_Exemplars.md:879",
        ("External_Exemplars/2025-06_Second_Pass_Addendum.md", "SEVENTH VERIFIED"): "register row 15, cited at 02_Verified_Exemplars.md:840",
        ("External_Exemplars/2025-06_Series_CCT_Starbucks_Rabanne.md", "A. June 2025 P2"): "register row 19, cited at 02_Verified_Exemplars.md:426",
        ("02_Verified_Exemplars.md", "second 9/9 on the same paper"): "register row 14, cited at 2024-06_P1R_Cafe_Pinch.md:24",
        ("02_Verified_Exemplars.md", "model Justify answer"): "register row 13, cited at 2024-06_P1R_Cafe_Pinch.md:9",
    }

    def exempted(rel, heading):
        for (f, frag), why in EXEMPT.items():
            if rel.endswith(f) and frag.lower() in heading.lower():
                return why
        return None

    # Files whose headings discuss marks rather than claim them.
    NARRATIVE_FILES = {
        "00_Pearson_Official_Rulebook.md", "01_Mark_Tariff_Playbook.md", "04_Type_Coverage_and_Gaps.md",
        "05_Constructed_12mark_Models.md", "06_External_Source_Library.md", "07_Official_Exam_Scope.md",
        "08_Completion_Map.md", "09_Verified_Tally.md", "10_Chain_Bank.md", "README.md",
    }
    cited = collections.defaultdict(list)
    for _t, _label, _f, _ln in rows:
        cited[pathlib.Path(_f).name].append(_ln)
    seen_head, cited_head, exempt_head, uncited = 0, 0, 0, []
    for f in sorted(ROOT.rglob("*.md")):
        if f.name in NARRATIVE_FILES:
            continue
        for i, line in enumerate(f.read_text(encoding="utf-8", errors="replace").split("\n"), 1):
            if not line.lstrip().startswith("#") or "not counted" in line:
                continue
            if not TOKEN.search(line):
                continue
            seen_head += 1
            rel = str(f.relative_to(ROOT))
            near = [c for c in cited[f.name] if abs(i - c) <= 8]
            # A HEADING THAT ANNOUNCES MORE THAN ONE SCRIPT NEEDS MORE THAN ONE ROW.
            # `2023-06_P2_IKEA.md:132` reads "3/3 x2" and covers two scripts; with
            # a single citation in range, deleting the other row changed nothing -
            # the sabotage passed. The multiplier is the count the heading states.
            mult = re.search(r"[x\u00d7]\s*(\d)\b", line)
            need = int(mult.group(1)) if mult else 1
            if len(near) >= need:
                cited_head += 1
            elif exempted(rel, line):
                exempt_head += 1
                print(f"  -- exempt: {rel}:{i} — {exempted(rel, line)}")
            else:
                uncited.append((rel, i, line.strip()[:88],
                                f"{len(near)} citation(s) in range, heading implies {need}"))
    print(f"  headings stating a full mark: {seen_head}")
    if not seen_head:
        print("  NONE PARSED - check the parser, not the bank.")
        stated_bad.append("the full-mark citation scan parsed nothing")
    print(f"  cited within 8 lines by a register row : {cited_head}")
    print(f"  exempted, with the reason recorded     : {exempt_head}")
    print(f"  UNCITED                                : {len(uncited)}")
    for rel, i, txt, why in uncited:
        print(f"    !! {rel}:{i}  {txt}")
        print(f"       {why}")
        stated_bad.append(f"{rel}:{i} states a full mark that no register row cites: {txt[:60]}")

    print()
    print("=" * 78)
    print("CITATION AGREEMENT — the session and paper a row names vs the file it cites")
    print("=" * 78)
    cite_bad, seen_ses, seen_paper = citation_agreement(rows)
    print(f"  rows whose session was checked against a dated filename : {seen_ses}")
    print(f"  rows whose paper was checked against a PAPER section    : {seen_paper}")
    if seen_ses == 0 or seen_paper == 0:
        print("  ⚠️ one of those counts is zero — THAT IS THE PARSER FAILING, not the bank.")
        cite_bad.append(("parser", "the citation-agreement check parsed nothing"))
    for kind, msg in cite_bad:
        print(f"  FAIL {kind}: {msg}")
    if not cite_bad:
        print("  every dated citation is from the session its row names, and every papered one")
        print("  sits under the PAPER section its row names.")
    for kind, msg in cite_bad:
        stated_bad.append(f"citation disagrees with its row — {msg}")

    # ------------------------------------------------------------------
    # THE TRANSCRIPTS INVENTORY — every full-mark script named in that table must have
    # a REGISTER ROW for its own sitting, paper and question.
    #
    # This is the failure that cost two 12/12s on 12 Nov 2026. The transcripts README
    # listed `4BS1_01R_2206_4c.md` as 12/12 from the day the folder was created, and
    # this script never saw it: it scans HEADINGS, and that file is a TABLE. A register
    # that reads only one shape of evidence cannot claim to be complete.
    #
    # The key is sitting + paper + question. The file name alone would fail whenever a
    # script is transcribed in two places (the register has one canonical source); and
    # (tariff, question) alone is the PAPER-BLIND key this bank has already been bitten
    # by twice — Q2(c) of one paper satisfied by a row for Q2(c) of another.
    print()
    print("=" * 78)
    print("TRANSCRIPTS INVENTORY - every full-mark script named there has a register row")
    print("=" * 78)
    SITTING = {"1906": ("Jun", "2019"), "2001": ("Jan", "2020"), "2206": ("Jun", "2022"),
               "2305": ("May", "2023"), "2306": ("Jun", "2023"), "2406": ("Jun", "2024"),
               "2506": ("Jun", "2025"), "2606": ("Jun", "2026")}
    known = set()
    for _tier, _label, _f, _ln in rows:
        parts = [q.strip() for q in _label.split("|")]
        if len(parts) < 2:
            continue
        series, pq = parts[0], parts[1]
        my = re.search(r"(20\d\d)", series)
        mp = re.match(r"P(\d)(R?)\s*Q(\d)\(([a-h])\)", pq)
        if not (my and mp):
            continue
        month = "May" if "May/" in series else ("Jan" if "Jan" in series else "Jun")
        known.add((month, my.group(1), f"P{mp.group(1)}{mp.group(2)}", f"{mp.group(3)}{mp.group(4)}"))
    inv = ROOT.parent / "audits" / "corpus" / "transcripts" / "README.md"
    inv_rows, inv_bad = 0, []
    if inv.exists():
        for i, line in enumerate(inv.read_text(encoding="utf-8").split("\n"), 1):
            m = re.match(r"^\|\s*`([^`]+)`\s*\|([^|]*)\|([^|]*)\|([^|]*)\|", line)
            if not m:
                continue
            fname, score_col = m.group(1).strip(), m.group(4)
            tok = re.search(r"(?<![\d/])(\d+)/(\d+)(?![\d/])", score_col)
            if not tok or tok.group(1) != tok.group(2):
                continue
            inv_rows += 1
            fm = re.match(r"4BS1_(\d\d)(R?)_(\d{4})_(\d)([a-h])", fname)
            if not fm:
                inv_bad.append((i, fname, tok.group(0), "the filename carries no sitting/question key"))
                continue
            if fm.group(3) not in SITTING:
                inv_bad.append((i, fname, tok.group(0), f"sitting {fm.group(3)} not in the key table"))
                continue
            month, year = SITTING[fm.group(3)]
            key = (month, year, f"P{int(fm.group(1))}{fm.group(2)}", f"{fm.group(4)}{fm.group(5)}")
            if key not in known:
                inv_bad.append((i, fname, tok.group(0),
                                f"no register row for {month} {year} "
                                f"P{int(fm.group(1))}{fm.group(2)} Q{fm.group(4)}({fm.group(5)})"))
    print(f"  full-mark rows in the inventory : {inv_rows}")
    if not inv_rows:
        print("  NONE PARSED - check the parser, not the bank.")
        stated_bad.append("the transcripts inventory scan parsed nothing")
    for i, fname, tok, why in inv_bad:
        print(f"    !! README.md:{i}  {fname} listed as {tok} — {why}")
        stated_bad.append(f"transcripts README:{i} lists {fname} as {tok}: {why}")
    if inv_rows and not inv_bad:
        print("  every full-mark transcript has a register row for its own sitting, paper and question.")

    # ------------------------------------------------------------------
    # THE SCRIPT MANIFEST — every script the archived reports print at its part's
    # FULL tariff must be a register row, keyed on paper + question.
    #
    # This check should have existed from the start; its absence cost THREE 12/12s.
    # The register was built by sweeping the bank's PROSE, which can only find scripts
    # somebody had already written about. `audits/corpus/scripts_merged.json` is the
    # extraction of every marked script the reports print, with its score, and
    # `By_Paper/` knows every part's tariff. Asked together, "which full-mark scripts
    # exist?" has an answer that does not depend on prose at all.
    #
    # Keyed on PAPER + QUESTION, never on tariff or question alone — the paper-blind
    # key that has produced false passes in this bank three times.
    print()
    print("=" * 78)
    print("THE SCRIPT MANIFEST - every script printed at full marks has a register row")
    print("=" * 78)
    MANIFEST = ROOT.parent / "audits" / "corpus" / "scripts_merged.json"
    SESSION_OF = {"2206": "May-June_2022", "2306": "May_2023", "2406": "May-June_2024",
                  "2506": "May-June_2025", "2606": "June_2026"}
    TARIFF = {}
    for f in sorted((ROOT / "By_Paper").glob("*.md")):
        fm = re.match(r"4BS1_(.+)_(P\dR?)$", f.stem)
        if not fm:
            continue
        for q, mk in re.findall(r"^### `(\d\([a-h]\))`[^\n]*?(\d+) marks?",
                                f.read_text(encoding="utf-8"), re.M):
            TARIFF[(fm.group(1), fm.group(2), q)] = int(mk)
    REG_KEYS = set()
    for _tier, _label, _f, _ln in rows:
        parts = [q.strip() for q in _label.split("|")]
        if len(parts) < 2:
            continue
        pq = re.match(r"P(\d)(R?)\s*Q(\d)\(([a-h])\)", parts[1])
        if pq:
            REG_KEYS.add((f"P{int(pq.group(1))}{pq.group(2)}", f"{pq.group(3)}({pq.group(4)})",
                          int(_tier.split("/")[0])))
    checked, missing_full = 0, []
    if MANIFEST.exists() and TARIFF:
        for report, scripts in json.loads(MANIFEST.read_text()).items():
            rm = re.match(r"4BS1_(\d\d)(R?)_(\d{4})$", report)
            if not rm or rm.group(3) not in SESSION_OF:
                continue
            paper = f"P{int(rm.group(1))}{rm.group(2)}"
            session = SESSION_OF[rm.group(3)]
            for sc in scripts:
                v = sc.get("mark_value") or 0
                mk = TARIFF.get((session, paper, sc["question"]))
                if mk is None or v != mk or mk not in (1, 2, 3, 6, 9, 12):
                    continue
                checked += 1
                if (paper, sc["question"], mk) not in REG_KEYS:
                    missing_full.append((report, paper, sc["question"], mk))
        print(f"  full-mark scripts found in the manifest : {checked}")
        if not checked:
            print("  NONE PARSED - check the parser, not the bank.")
            stated_bad.append("the script-manifest scan parsed nothing")
        # a script may be DECLARED in the "BODY NOT YET HELD" ledger instead of registered;
        # declared is honest, unlisted is not. The ledger is parsed, not trusted.
        ledger = REGISTER.read_text(encoding="utf-8")
        declared = set()
        for lm in re.finditer(r"^\|\s*`(4BS1_[0-9A-Z_]+)`\s*\|\s*P(\d)(R?)\s*(\d)\(([a-h])\)\s*\|", ledger, re.M):
            declared.add((f"P{int(lm.group(2))}{lm.group(3)}", f"{lm.group(4)}({lm.group(5)})"))
        pending = [(r, p, q, v) for (r, p, q, v) in missing_full if (p, q) in declared]
        missing_full = [(r, p, q, v) for (r, p, q, v) in missing_full if (p, q) not in declared]
        print(f"  declared in the ledger, body not yet held : {len(pending)}")
        for report, paper, q, v in missing_full:
            print(f"    !! {report} {paper} {q} is printed at {v}/{v} and no register row holds it")
            stated_bad.append(f"{report} prints a {v}/{v} at {q} that the register does not hold")
        for report, paper, q, v in pending:
            print(f"    .. declared, body pending: {report} {paper} {q} {v}/{v}")
        if checked and not missing_full:
            print("  every full-mark script in the manifest has a register row.")
    else:
        print("  SKIPPED - manifest or By_Paper/ not found")
        stated_bad.append("the script-manifest check could not run")

    print()
    print("=" * 78)
    ok = not bad and not unaccounted and not stated_bad
    if stated_bad:
        for pr in stated_bad:
            print(f"  !! {pr}")
    print("RESULT:", "OK — the register is complete against the bank's own prose, and every "
                     "total it states equals the rows that back it."
          if ok else "FAIL — see the rows above. Fix the register, not this script.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
