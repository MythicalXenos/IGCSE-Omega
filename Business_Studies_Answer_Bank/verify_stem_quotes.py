#!/usr/bin/env python3
"""Does the bank ever QUOTE a question stem the paper does not contain?

WHY THIS EXISTS
---------------
**Five stems in this bank have been found disagreeing with the papers**, all in
`05_Constructed_12mark_Models.md` (batch 1). The fifth — *"becoming a franchisor"*
against the paper's *"operating as a franchise"* — survived an earlier correction
pass because **the model printed beneath it was right**. The lesson: **a stem check
must compare the printed question, not the answer**, and it has to run over the
whole bank rather than over the file where the last one was found.

WHAT IT DOES
------------
1. Reads the three inventories derived from the mark schemes (6-, 9- and 12-mark),
   which carry each block's **stem as the scheme prints it**.
2. Scans every `.md` file in `Perfect_Answers/` for the bank's citation form —

       **Asked:** *"…stem…"* — **May–June 2023 P1, 1(g)**
       **Also asked:** *"…stem…"* — June 2022 P2 4(b)

3. Normalises both texts and scores them.
4. Prints every citation whose score falls below the floor, plus a count of
   citations it could **not** resolve to a known block — because a checker that
   silently skips what it cannot parse is worse than none.

Score is the **best of two measures**, and both are needed:

  * `SequenceMatcher` on normalised text — catches a stem quoted with different
    words but the same shape;
  * **keyword overlap on words of five letters or more** — catches the case this
    script was written for and its first version MISSED: **an option-style quote
    that belongs to the other Justify on the same paper.**
    `"Option 1: increase special offers…"` scores 18% by sequence against the
    2(f) content and **82%** against the 3(e) content; the sequence ratio alone
    never lifted it above the floor, because both texts are short and share
    "Option 1 / Option 2".

**Read the lowest scores first.** A low *sequence* score with a high *keyword*
score against the SAME block is just a paraphrase and is fine.

Run from Business_Studies_Answer_Bank/:  python3 verify_stem_quotes.py
Exit 0 when nothing is below the floor, 1 otherwise.
"""
import csv
import difflib
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
PA = HERE / "Perfect_Answers"
FLOOR = 0.60            # below this, a quoted stem is not the printed one
PAPER_FLOOR = 0.50      # below this, NO question on the named paper resembles the quote
NEAR = 0.90             # this high, the citation IS the question's wording - so it must match
# Every near-miss was read by hand on 14 Oct 2026 and none was a slip. They fall
# into four kinds, all legitimate:
#   * the bank's own "·" between Option 1 and Option 2, where the scheme runs them
#     together, or a stem quoted from the lead-in sentence onwards;
#   * the scheme's PDF artefacts - "e- commerce", "off-the job", "complete AND
#     application form" - where the bank has silently repaired an extraction fault,
#     which rule 124 requires;
#   * the scheme paraphrasing the question paper ("the proximity to materials" for
#     the paper's "proximity of material"); the bank quotes the paper;
#   * a clarifying bracket the bank adds openly - "(Premier Inn)".
# So the list is an ADVISORY that must stay the size it was reviewed at. A NEW one
# fails the run: that is exactly the shape of the "Analyse WHY Kraft Heinz" slip,
# which sat unnoticed because 0.97 similarity read as "resolved".
NEAR_REVIEWED = 29
# A quote carrying an ellipsis or a square bracket is an EDITED quote, and the bank
# marks its edits openly. Those are excluded: the rule is about unmarked slips.
EDITING = re.compile(r"\u2026|\.\.\.|\[|\]")
SHOW = 25               # how many of the weakest to print

SESSION = {
    "may-june 2019": "May-June 2019", "may 2019": "May-June 2019",
    "summer 2019": "May-June 2019",
    "may-june 2020": "May-June 2020", "may 2020": "May-June 2020",
    "may-june 2021": "May-June 2021", "may 2021": "May-June 2021",
    "may-june 2022": "May-June 2022", "may 2022": "May-June 2022",
    "may-june 2023": "May 2023", "may 2023": "May 2023",
    "may-june 2024": "May-June 2024", "may 2024": "May-June 2024",
    "may-june 2025": "May-June 2025", "may 2025": "May-June 2025",
    "june 2019": "May-June 2019", "june 2020": "May-June 2020",
    "june 2021": "May-June 2021", "june 2022": "May-June 2022",
    "june 2023": "May 2023", "june 2024": "May-June 2024",
    "june 2025": "May-June 2025", "june 2026": "June 2026",
    "november 2020": "November 2020", "nov 2020": "November 2020",
    "november 2021": "November 2021", "nov 2021": "November 2021",
    "november 2023": "November 2023", "nov 2023": "November 2023",
    "november 2024": "November 2024", "nov 2024": "November 2024",
    "november 2025": "November 2025", "nov 2025": "November 2025",
}

# ⚠️ The label is followed by markdown that varies: `**Asked:** *"..."*` and
# `**Also asked:** *"..."*` both occur, and the italic marker comes AFTER a space.
# A pattern that expects the quote immediately after the spaces silently matches
# nothing at all - which is how the first version of this script reported a clean
# bill of health with **zero** citations checked. Always print the checked count.
CITE = re.compile(
    r"(?:Also asked|Asked)[:*.\s_>]*"                       # the label + markdown
    r"[\"\u201c](.+?)[\"\u201d]"                            # the quoted stem
    r"[^\n]{0,240}?"                                        # connective prose, same line
    r"\*{0,2}([A-Z][A-Za-z0-9\u2013\u2014\- ]{2,22}?)"        # session words (June 2026)
    r"\s+(P\dR?)\b[,. ]*(\d\s*\(\w\))?"                  # paper (+question)
    ,
    re.S)


def keywords(t: str) -> set:
    """Words a chain is actually built from — five letters or more, minus filler."""
    drop = {"option", "which", "these", "should", "choose", "justify", "business"}
    return {w for w in re.findall(r"[a-z]{5,}", norm(t))} - drop


def overlap(a: str, b: str) -> float:
    ka = keywords(a)
    return len(ka & keywords(b)) / max(1, len(ka))


def similarity(a: str, b: str) -> float:
    return max(difflib.SequenceMatcher(None, norm(a), norm(b)).ratio(),
               overlap(a, b))


def norm(t: str) -> str:
    t = (t or "").replace("\u2019", "'").replace("\u2018", "'")
    t = t.replace("\u2013", "-").replace("\u2014", "-")
    t = re.sub(r"\s+", " ", t).strip().lower()
    t = re.sub(r"^evaluate|^analyse|^assess|^justify|^discuss", "", t).strip()
    return t.rstrip(" .")


def plain(t: str) -> str:
    """`norm` with markdown emphasis and code ticks removed.

    The bank bolds the topic inside a quoted stem ("Explain one advantage of being
    a **sole trader**"). That is emphasis, not wording, and it made 39 correct
    quotes look like near-misses. This is for the SUBSTRING test only.
    """
    return norm(re.sub(r"[*_`]", "", t or ""))


def load_blocks():
    """(session, paper, question) -> stem, from the three derived inventories."""
    out = {}
    with open(HERE / "layer_c_6mark_inventory.csv", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            out[(r["session"], r["paper"], r["question"])] = r["stem"]
    with open(HERE / "layer_c_9mark_inventory.csv", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            # 34 of the 76 nine-mark schemes print NO stem - they show the two
            # options and nothing else. Those cannot be checked against the scheme,
            # and must be counted separately rather than scored as mismatches.
            out[(r["session"], r["paper"], r["question"])] = r["stem"]
    with open(HERE / "layer_c_12mark_inventory.csv", encoding="utf-8-sig") as fh:
        for r in csv.DictReader(fh):
            out[(r["Session"], r["Paper"], r["Part"].replace(" ", ""))] = r["Stem"]

    # THE 3-MARK TIER WAS NOT LOADED AT ALL, so every 3-mark citation came back
    # "could not resolve" and was never actually compared. Its inventory
    # (`layer_c_3mark_master.csv`) has no stem column — the stem is printed in the
    # block dump, between the heading and the "Answer Mark" column labels, and only
    # on the blocks where the scheme prints it. The rest are left empty and counted
    # as not-comparable, exactly like the 34 nine-mark schemes that print options only.
    dump = (HERE / "layer_c_3mark_blocks.txt")
    if dump.exists():
        parts = re.split(r"\n={78}\n=== (.+?)\n={78}\n", dump.read_text(encoding="utf-8"))
        for head, body in zip(parts[1::2], parts[2::2]):
            bits = [x.strip() for x in head.split("|")]
            if len(bits) != 3:
                continue
            sess, paper, label = bits
            m = re.search(r"(?i)Question\s*Number|Q\.\s*No\.", body)
            stem = ""
            if m:
                seg = body[m.end():]
                cut = re.search(r"Answer\s+Mark|Indicative\s+content\s+Mark|Indicative\s+Content\s+Mark", seg)
                stem = " ".join(seg[:cut.start() if cut else len(seg)].split())
            out[(sess, paper, label.replace(" ", ""))] = stem
    return out


def main() -> int:
    blocks = load_blocks()
    with_stem = {k: v for k, v in blocks.items() if v.strip()}
    print(f"blocks known                   : {len(blocks)}")
    print(f"  of which the scheme PRINTS a stem : {len(with_stem)}")
    print(f"  of which it does not              : {len(blocks) - len(with_stem)}"
          f"  (cannot be checked against the scheme)")

    seen, unresolved, nostem, weak, checked = set(), [], [], [], 0
    misattributed = []
    near_miss = []
    paper_only = []
    found = 0
    dupes = 0
    for f in sorted(PA.rglob("*.md")):
        text = f.read_text(encoding="utf-8", errors="replace")
        for m in CITE.finditer(text):
            found += 1
            quote, sess_raw, paper, qn = m.group(1), m.group(2), m.group(3), m.group(4)
            key_s = None
            low = norm(sess_raw)
            for k, v in SESSION.items():
                if k in low:
                    key_s = v
                    break
            if not key_s:
                continue
            if not qn:
                # THE BANK CITES MOST 3-MARK QUESTIONS BY SESSION AND PAPER ONLY.
                # Skipping those (the original behaviour) left ~126 citations
                # entirely unchecked - the largest single blind spot in this check.
                # With no claimed part there is nothing to contradict, but there is
                # still a fact to test: does ANY question on the named paper read
                # like the quote? If none does, the citation names the wrong paper.
                paper_only.append((f.relative_to(PA), (key_s, paper), quote))
                continue
            q = qn.replace(" ", "")
            if re.fullmatch(r"\d", q):
                q = q + "(c)" if False else q          # bare number: cannot resolve
            key = (key_s, paper, q)
            stem = blocks.get(key)
            sig = (f.name, key, norm(quote)[:60])
            if sig in seen:
                dupes += 1
                continue
            seen.add(sig)
            if stem is None:
                unresolved.append((f.relative_to(PA), key, quote[:70]))
                continue
            if not stem.strip():
                nostem.append((f.relative_to(PA), key, quote[:70]))
                continue
            checked += 1
            score = similarity(quote, stem)
            if score >= FLOOR:
                # A VERY HIGH score means the citation is not a paraphrase - it is
                # quoting the question's own words. If the wording then differs by a
                # word, the quote is wrong even though it "resolved": **"Analyse WHY
                # Kraft Heinz could benefit from reducing its waste" scored 0.97
                # against the scheme's "Analyse HOW ..." and passed every run of this
                # check for weeks.** The floor of 0.30 is for recognising the
                # question; this rule is for checking the quote.
                if score >= NEAR and plain(quote) not in plain(stem) and not EDITING.search(quote):
                    near_miss.append((score, f.relative_to(PA), key, quote, stem))
                continue
            # DIAGNOSIS: does the quote match a DIFFERENT question on the same paper?
            # Four errors of this kind have been found - the second Justify on a paper
            # (3(e)) logged as the first (2(f)) - so the check names the question the
            # quote actually belongs to instead of leaving the reader to guess.
            best = None
            for (s2, p2, q2), stem2 in blocks.items():
                if (s2, p2) != (key[0], key[1]) or not stem2.strip() or q2 == key[2]:
                    continue
                sc2 = similarity(quote, stem2)
                if best is None or sc2 > best[0]:
                    best = (sc2, q2)
            # Require BOTH a clear margin and a genuinely strong match. A plain-English
            # gloss of the RIGHT question can score ~37% against an unrelated one;
            # flagging that would be noise, and noise is what stops a check being read.
            if best and best[0] > max(score + 0.15, 0.60):
                misattributed.append((best[0] - score, f.relative_to(PA), key, best,
                                      score, quote))
            else:
                weak.append((score, f.relative_to(PA), key, quote, stem))

    print(f"citations found by the parser : {found}   (this is coverage: it is how many the")
    print(f"                                          check sees, so a parser failure is visible)")
    print(f"quoted stems compared       : {checked}")
    print(f"quoted stems the scheme does not print : {len(nostem)}  (not comparable)")
    print(f"quoted stems NOT resolved   : {len(unresolved)}  (reported, never skipped)")
    print(f"quote+key duplicates folded : {dupes}  (the same citation written twice in one file)")
    print()
    weak.sort()
    misattributed.sort(reverse=True)

    # ---- citations that name a paper but no question number ------------------
    # Most of these are 3-mark Explain questions, and the schemes are split on
    # whether they print the question's wording at all. **Eight of the 38 papers
    # print no 3-mark wording anywhere** - all four May-June 2019 papers and all
    # four May-June 2020 papers. (Nov 2021 P1 is a ninth for the P1/P2 pair; the
    # count is per paper, and it is derived below rather than typed.) On those, a
    # citation cannot be checked and must be counted as not comparable, NOT as a
    # failure. On the other 30 papers the wording is printed, and a quote that
    # resembles none of it is a real signal.
    THREE = {"1(f)", "2(c)", "2(d)", "2(e)"}
    no_match, paper_proven, paper_blind = [], 0, 0
    for f, (sess, paper), quote in paper_only:
        best = (0.0, None, "")
        printable3 = False
        for (s2, p2, q2), stem in blocks.items():
            if (s2, p2) != (sess, paper):
                continue
            if q2 in THREE and stem.strip():
                printable3 = True
            if not stem.strip():
                continue
            sc = similarity(quote, stem)
            if sc > best[0]:
                best = (sc, q2, stem)
        if best[0] >= PAPER_FLOOR:
            if best[0] >= NEAR and plain(quote) not in plain(best[2]) and not EDITING.search(quote):
                near_miss.append((best[0], f, (sess, paper, best[1]), quote, best[2]))
            paper_proven += 1
        elif printable3:
            no_match.append((best[0], f, f"{sess} {paper}", quote, best[1]))
        else:
            paper_blind += 1
    # Two different things can make a score low, and only one of them is an error.
    # A MISATTRIBUTION is a contradiction - the quote demonstrably belongs to another
    # question - and fails the check. A low score with no better alternative is the
    # bank's habit of glossing an option pair in plain English ("charge a low price
    # when it first opens a new restaurant" for "penetration pricing"); the citation
    # states the question and the scheme's own answer content carries it, so this is
    # advisory. A check that cries wolf on the legitimate ones stops being read.
    print()
    print("=" * 74)
    print(f"NEAR-MISS QUOTES — {len(near_miss)}: the citation is that question, but the wording differs")
    print("=" * 74)
    if not near_miss:
        print("  none — every high-similarity quote is the scheme's own wording.")
    for score, f, key, quote, stem in sorted(near_miss, reverse=True):
        diff = [w for w in plain(quote).split()
                if w not in set(plain(stem).split())]
        print(f"  {score:.3f}  {f}  {key[0]} {key[1]} {key[2] if len(key) > 2 else ''}")
        print(f"       bank : {quote[:110]}")
        print(f"       MS   : {stem[:110]}")
        print(f"       words the scheme does not have: {diff[:8]}")
    if len(near_miss) > NEAR_REVIEWED:
        print(f"  !! {len(near_miss)} near-misses against {NEAR_REVIEWED} reviewed on 14 Oct 2026 "
              f"— {len(near_miss) - NEAR_REVIEWED} NEW one(s). Read the diffs above: a new "
              f"near-miss is how a wording slip looks.")
    elif len(near_miss) < NEAR_REVIEWED:
        print(f"  note: {NEAR_REVIEWED - len(near_miss)} fewer than the reviewed set — "
              f"a quote was fixed or removed. Lower NEAR_REVIEWED to match.")
    else:
        print(f"  all {NEAR_REVIEWED} are the reviewed set (separators, PDF repairs, the "
              f"scheme paraphrasing the paper, an open bracket) — none is a new slip.")
    print()

    print("=" * 74)
    print(f"MISATTRIBUTED QUOTES — {len(misattributed)}")
    print("=" * 74)
    if not misattributed:
        print("  none — every citation names a question that question paper actually has.")
    for margin, f, key, best, score, quote in misattributed:
        print(f"  {f}  {key[0]} {key[1]}")
        print(f"       citation names {key[2]}, but the text matches {best[1]} "
              f"({best[0]:.0%} against {score:.0%}) — margin {margin:+.0%}")
        print(f"       quote: {re.sub(chr(10), ' ', quote)[:100]}")
    print()
    print("=" * 74)
    print(f"CITATIONS WITH NO QUESTION NUMBER — {len(paper_only)} checked against their paper")
    print("=" * 74)
    print(f"  of {len(paper_only)}: {paper_proven} proven (a question on that paper reads like "
          f"the quote), {paper_blind} not comparable")
    # Which papers print no 3-mark wording at all — derived, then reported, so the
    # number can never be a stale claim in a message (see 08_: a figure inside a
    # correction note is still a claim).
    blind = sorted({(s2, p2) for (s2, p2, q2), stem in blocks.items()
                    if q2 in THREE and not stem.strip()
                    and not any(v.strip() for (a, b, c), v in blocks.items()
                                if (a, b) == (s2, p2) and c in THREE)})
    print(f"  ({paper_blind} of the {len(paper_only)} sit on one of the {len(blind)} papers that print "
          f"NO 3-mark question wording at all: "
          + ", ".join(f"{x} {y}" for x, y in blind) + ")")
    if not no_match:
        print("  no citation names a paper whose printed 3-mark wording it fails to resemble.")
    for score, f, where, quote, q2 in sorted(no_match):
        print(f"  {score:5.1%}  {f}  {where} — no question on that paper matches")
        print(f"          quote: {re.sub(chr(10), ' ', quote)[:96]}")
        print(f"          closest on that paper is {q2}")

    print()
    print(f"ADVISORY — {len(weak)} quotes below the floor with no better alternative")
    print("  (plain-English glosses of option pairs; the citation and scheme content "
          "both carry them):")
    for score, f, key, quote, stem in weak[:10]:
        print(f"  {score:5.1%}  {key[0]} {key[1]} {key[2]}  {re.sub(chr(10), ' ', quote)[:66]}")
    if len(weak) > 10:
        print(f"  … and {len(weak) - 10} more")
    print()
    if unresolved:
        print()
        print("=" * 74)
        print(f"COULD NOT RESOLVE — {len(unresolved)} (first 10)")
        print("=" * 74)
        for f, key, quote in unresolved[:10]:
            print(f"  {f}  {key}  {re.sub(chr(10),' ',quote)[:80]}")

    print()
    problems = (len(misattributed) + len(no_match)
                + max(0, len(near_miss) - NEAR_REVIEWED))
    print("RESULT:", "OK — no quoted stem names the wrong question, and every "
                     "high-similarity quote is verbatim."
          if not problems
          else f"FAIL — {len(misattributed)} quote(s) belong to a different question, "
               f"{len(no_match)} name a paper with no question like them, and "
               f"{len(near_miss)} quote a question with the wrong wording. The bank is wrong.")
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
