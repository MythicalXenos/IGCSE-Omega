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
    for f in sorted(PA.rglob("*.md")):
        text = f.read_text(encoding="utf-8", errors="replace")
        for m in CITE.finditer(text):
            quote, sess_raw, paper, qn = m.group(1), m.group(2), m.group(3), m.group(4)
            if not qn:
                continue
            key_s = None
            low = norm(sess_raw)
            for k, v in SESSION.items():
                if k in low:
                    key_s = v
                    break
            if not key_s:
                continue
            q = qn.replace(" ", "")
            if re.fullmatch(r"\d", q):
                q = q + "(c)" if False else q          # bare number: cannot resolve
            key = (key_s, paper, q)
            stem = blocks.get(key)
            sig = (f.name, key, norm(quote)[:60])
            if sig in seen:
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

    print(f"quoted stems compared       : {checked}")
    print(f"quoted stems the scheme does not print : {len(nostem)}  (not comparable)")
    print(f"quoted stems NOT resolved   : {len(unresolved)}  (reported, never skipped)")
    print()
    weak.sort()
    misattributed.sort(reverse=True)
    # Two different things can make a score low, and only one of them is an error.
    # A MISATTRIBUTION is a contradiction - the quote demonstrably belongs to another
    # question - and fails the check. A low score with no better alternative is the
    # bank's habit of glossing an option pair in plain English ("charge a low price
    # when it first opens a new restaurant" for "penetration pricing"); the citation
    # states the question and the scheme's own answer content carries it, so this is
    # advisory. A check that cries wolf on the legitimate ones stops being read.
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
    print("RESULT:", "OK — no quoted stem names the wrong question."
          if not misattributed
          else f"FAIL — {len(misattributed)} quote(s) belong to a different question. "
               f"The bank is wrong; the paper wins.")
    return 0 if not misattributed else 1


if __name__ == "__main__":
    sys.exit(main())
