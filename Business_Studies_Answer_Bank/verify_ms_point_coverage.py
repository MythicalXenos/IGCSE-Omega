#!/usr/bin/env python3
"""Layer D — does each entry actually CARRY the points the mark scheme awards?

WHY THIS EXISTS
---------------
Every existing check looks the OTHER way round.

  * the coverage scripts prove each block is MAPPED to some entry;
  * `verify_chain_bank_anchors.py` scores a block's whole indicative content
    against the entry, to catch a mapping that points at the wrong entry;
  * `verify_stem_quotes.py` proves the citation names the right question.

None of them can see this: **the right entry, pointing at the right question,
that simply fails to use one of the mark scheme's own awarded points.** A
whole-content score cannot show it — an entry with 90% of a block's vocabulary
still hides the 10% it dropped, and on a 9-mark Justify the dropped point may be
the only AO4 route in the scheme.

WHAT IT DOES
------------
For every mapping, it splits the block's OFFICIAL indicative content into its
individual bullet points — closing a point with its continuation lines — and
asks, for each point, whether ANY of the words that point is built from appear
anywhere in the entry.

The test is deliberately blunt: it flags a point only when **not one** of its
content words (five letters or more, minus stopwords and numbers) appears in the
entry. Paraphrase cannot trigger it, and it does not try to score quality. **A
zero is not a judgement about the answer: it is a question — "is this point in
here under any wording at all?"**

Run from Business_Studies_Answer_Bank/:  python3 verify_ms_point_coverage.py
Writes no files. Exit code 0 unless a block's points are wholly absent from the
entry that claims it, in which case exit 1 and the points are printed verbatim.
"""
import importlib.util
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent

# Reuse the anchor check's loaders: they already know how to read the coverage
# maps, the block dumps and 10_Chain_Bank.md's entries, and two parsers for the
# same file is how the two of them drift apart.
_spec = importlib.util.spec_from_file_location("anchors", HERE / "verify_chain_bank_anchors.py")
anchors = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(anchors)

STOP = anchors.STOP | {
    "level", "marks", "mark", "credit", "awarded", "candidate", "candidates",
    "response", "responses", "point", "points", "valid", "accept", "allow",
    "example", "examples", "including", "include", "included", "such", "other",
    "others", "must", "should", "could", "would", "there", "these", "those",
    "which", "where", "while", "their", "them", "they", "then", "than", "that",
    "this", "with", "without", "when", "what", "have", "having", "been", "being",
}


def bullets(block_text: str):
    """The block's indicative content, one entry per mark-scheme point.

    Points in these dumps are separated by '•'; a point runs to the next '•'.
    Continuation lines belong to the point above them, which is why this splits
    on the separator rather than on newlines.
    """
    cut = re.split(r"Level\s*Mark\s*Descriptor|Level 1\b", block_text)[0]
    return [p.strip() for p in re.split(r"•", cut) if p.strip()]


def content_words(text: str):
    return {w for w in re.findall(r"[a-z]{5,}", (text or "").lower()) if w not in STOP}


def main() -> int:
    entries = anchors.bank_entries()

    # The three level-based tiers map BLOCK NUMBERS (from the derived inventory)
    # to entry numbers, and their indicative content is the mark-scheme dump.
    #
    # The 3-mark tier is built the other way round: it maps a canonical TOPIC to
    # an entry, and one row of `layer_c_3mark_master.csv` is one block, carrying
    # the scheme's own worked answer. So block n -> row n -> its topic -> entry.
    tiers = []
    for tier, script, block_file in (
        ("6-mark", "layer_c_6mark_coverage.py", "layer_c_6mark_blocks.txt"),
        ("9-mark", "layer_c_9mark_coverage.py", "layer_c_9mark_blocks.txt"),
        ("12-mark", "layer_c_12mark_coverage.py", "layer_c_12mark_blocks.txt"),
    ):
        tiers.append((tier, anchors.load_map(script), anchors.block_text(block_file)))

    total_points = 0
    absent = []          # (tier, block, entry, point)
    for tier, covered, blocks in tiers:
        seen = set()
        for n, entry_no in sorted(covered.items()):
            text = blocks.get(n, "")
            entry = entries.get(entry_no, "")
            if not text or not entry:
                continue
            for point in bullets(text):
                words = content_words(point)
                if len(words) < 4:
                    continue          # too short to test without crying wolf
                key = (tier, point)
                if key in seen:
                    continue
                seen.add(key)
                total_points += 1
                if not (words & content_words(entry)):
                    absent.append((tier, n, entry_no, point))

    # 3-mark blocks, last, because this tier's mapping is by topic.
    with open(HERE / "layer_c_3mark_master.csv", encoding="utf-8") as fh:
        import csv as _csv
        rows3 = list(_csv.DictReader(fh))
    covered3 = anchors.load_map("layer_c_coverage.py")
    seen3 = set()
    for i, row in enumerate(rows3, 1):
        topic = row.get("canonical_topic", "")
        entry_no = covered3.get(topic)
        entry = entries.get(entry_no, "") if entry_no else ""
        text = row.get("ms_worked_answer", "")
        if not entry or not text:
            continue
        for point in bullets(text):
            words = content_words(point)
            if len(words) < 4:
                continue
            key = (point,)
            if key in seen3:
                continue
            seen3.add(key)
            total_points += 1
            if not (words & content_words(entry)):
                absent.append(("3-mark", i, entry_no, point))

    by_entry = {}
    for tier, n, entry_no, point in absent:
        by_entry.setdefault((tier, entry_no), []).append((n, point))

    print("=" * 74)
    print("MS POINT COVERAGE — is every awarded point present in the mapped entry?")
    print("=" * 74)
    print(f"  indicative points tested      : {total_points}")
    print(f"  points absent from their entry: {len(absent)}")
    print(f"  entries affected              : {len(by_entry)}")
    print()
    print("  ('absent' = not one content word of the point appears anywhere in the")
    print("   entry. It is a question to read, not a verdict on the answer.)")
    print()

    if by_entry:
        print("=" * 74)
        print(f"READ THESE — {len(by_entry)} entries with points the scheme awards and")
        print("the entry may not carry. Worst first.")
        print("=" * 74)
        for (tier, entry_no), items in sorted(by_entry.items(), key=lambda kv: -len(kv[1]))[:20]:
            head = entries.get(entry_no, "").splitlines()[0][:66]
            print(f"\n  entry {entry_no}  [{tier}]  {head}")
            print(f"    {len(items)} point(s) absent — blocks {sorted({b for b, _ in items})}")
            for b, point in items[:3]:
                print(f"      block [{b}] {re.sub(chr(10), ' ', point)[:104]}")

    print()
    print("RESULT:", "OK — every awarded point is at least named in its entry."
          if not absent else
          f"REVIEW — {len(absent)} awarded point(s) are absent from the entry mapped to them, "
          f"across {len(by_entry)} entries. Read them; the entry may still answer them "
          f"in its own wording.")
    return 0 if not absent else 1


if __name__ == "__main__":
    sys.exit(main())
