#!/usr/bin/env python3
"""Layer D — do the Chain Bank's 380 block→entry mappings point at the RIGHT entry?

WHY THIS EXISTS
---------------
Every tier already has a coverage script that proves its blocks are **covered** —
that each block number appears in the map, and that each mapped entry number
exists in `10_Chain_Bank.md`. Both checks pass, and both are blind to this:

    the map could point at the WRONG ENTRY and every check would still pass.

That is not hypothetical. The bank has already been bitten four times by a label
absorbing a block it does not describe (entry 176, the Spud Bros block, the
Ocean Vibes block, the 5b over-claim), and once by an MS/QP question-paper swap
that silently re-labelled a whole series. **A mapping is evidence only if it is
checked against the block's own content.**

WHAT IT DOES
------------
For every mapping in the 6-, 9- and 12-mark tiers it compares the block's
OFFICIAL indicative content — read from the mark-scheme-derived inventory, which
the coverage scripts never touch — against the text of the entry the map claims
covers it, and scores the overlap. Then it prints the weakest mappings.

  * a high score is not proof, but a very low one is a **contradiction**;
  * the score is computed over words of five letters or more, which is the
    vocabulary a chain is actually built from.

Run from Business_Studies_Answer_Bank/:  python3 verify_chain_bank_anchors.py
Exit code 0 when nothing scores below the contradiction floor, 1 otherwise.
"""
import csv
import importlib.util
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
BANK = HERE / "Perfect_Answers" / "10_Chain_Bank.md"
FLOOR = 0.30          # below this, a mapping contradicts its block
WORRY = 0.45          # between FLOOR and this, read it by hand

STOP = set("""the and for that with this from have been which will would could
their there these those about into over other others also more most much than
then when what where while your you're they them its it's not but can may might
should must need needs using used use one two three four five six seven eight
nine ten make makes made give gives given such some same very only both each
business businesses customer customers answer answers question questions
option options however therefore because""".split())


def toks(text) -> set:
    if not isinstance(text, str):
        text = "" if text is None else str(text)
    words = re.findall(r"[a-z]{5,}", text.lower())
    return {w for w in words if w not in STOP}


def load_map(script: str):
    """Import a coverage script and return its COVERED dict (never runs main())."""
    spec = importlib.util.spec_from_file_location(script[:-3], HERE / script)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.COVERED


def bank_entries() -> dict:
    """entry number -> its full text, from '## N.' to the next '## '."""
    text = BANK.read_text(encoding="utf-8")
    heads = [(int(m.group(1)), m.start()) for m in re.finditer(r"^## (\d+)\.", text, re.M)]
    out = {}
    for i, (n, start) in enumerate(heads):
        end = heads[i + 1][1] if i + 1 < len(heads) else len(text)
        out[n] = text[start:end]
    return out


def block_text(path: str) -> dict:
    """block number -> the block's own INDICATIVE CONTENT, from the block dump.

    The block dump is the mark scheme's own words, and it is the same file the
    inventory was built from — so this is the strongest available statement of
    what a block is about. The level descriptors at the end are identical on
    every block and are cut, because boilerplate overlap would flatter every
    score equally.
    """
    text = (HERE / path).read_text(encoding="utf-8")
    parts = re.split(r"\n={78}\n=== (.+?)\n={78}\n", text)[1:]
    out = {}
    for i, body in enumerate(parts[1::2], 1):
        cut = re.split(r"Level\s*Mark\s*Descriptor|Level 1\b", body)[0]
        out[i] = cut
    return out


def rows_of(path: str) -> dict:
    with open(HERE / path, encoding="utf-8-sig") as fh:
        return {int(r["n"]): r for r in csv.DictReader(fh)}


def norm(x: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (x or "").lower()).strip()


def cited(stem: str, entry: str) -> bool:
    """Does the entry actually CITE this block's question?

    This is the bank's own evidence standard: every entry opens with
    `**Asked:**` and `**Also asked:**` lines that quote the question verbatim.
    A stem phrase found there is proof of the mapping; vocabulary overlap, which
    a synthesized model answer can dilute, is only a hint.
    """
    ns = norm(stem)
    if len(ns.split()) < 6:
        return False
    words = ns.split()
    for start in (0, max(0, len(words) - 12)):
        probe = " ".join(words[start:start + 9])
        if len(probe.split()) >= 7 and probe in norm(entry):
            return True
    return False


def report(entries, tier: str, pairs, floor=FLOOR):
    print("=" * 74)
    print(f"{tier} — {len(pairs)} mappings scored against the block's OFFICIAL content")
    print("=" * 74)
    flagged = []
    for n, entry_no, block_txt, extra in sorted(pairs):
        entry = entries.get(entry_no, "")
        head = entry.splitlines()[0][:58] if entry else "(MISSING)"
        if extra and cited(extra, entry):        # extra carries the stem for this tier
            continue                              # the entry quotes the question - mapping proven
        bt, et = toks(block_txt), toks(entry)
        flagged.append((len(bt & et) / max(1, len(bt)), n, entry_no, head))
    flagged.sort()
    print(f"  mappings PROVEN by the entry quoting the question: "
          f"{len(pairs) - len(flagged)} of {len(pairs)}")
    print(f"\n  {'weakest 8 of the rest':<46}  overlap")
    for score, n, entry_no, head in flagged[:8]:
        print(f"  block [{n:>3}] -> entry {entry_no:<3} {head:<58} {score:6.1%}")
    hard = [f for f in flagged if f[0] < floor]
    print(f"\n  below the contradiction floor ({floor:.0%}): {len(hard)}")
    for score, n, entry_no, head in hard:
        print(f"    !! block [{n:>3}] -> entry {entry_no:<3} {head}  {score:.1%}")
    print()
    if not flagged:
        print("  every mapping scores above the worry line.")
    hard = [f for f in flagged if f[0] < floor]
    print(f"\n  below the contradiction floor ({floor:.0%}) : {len(hard)}")
    print(f"  worth reading by hand ({FLOOR:.0%}–{WORRY:.0%}) : {len(flagged) - len(hard)}\n")
    return hard


def main() -> int:
    entries = bank_entries()
    print(f"Chain Bank: {len(entries)} entries\n")
    hard_all = []

    b6 = block_text("layer_c_6mark_blocks.txt")
    m6 = load_map("layer_c_6mark_coverage.py")
    r6 = rows_of("layer_c_6mark_inventory.csv")
    pairs = [(n, m6[n], f"{r6[n]['stem']} {b6.get(n, '')}", str(r6[n]["stem"]))
             for n in sorted(m6) if n in r6]
    hard_all += report(entries, "6-MARK ANALYSE", pairs)

    m9 = load_map("layer_c_9mark_coverage.py")
    r9 = rows_of("layer_c_9mark_inventory.csv")
    b9 = block_text("layer_c_9mark_blocks.txt")
    pairs = [(n, m9[n],
              " ".join([str(r9[n].get(k, "")) for k in ("stem", "option_1", "option_2", "ao4_judgement")]
                       + [b9.get(n, "")]),
              str(r9[n]["stem"])) for n in sorted(m9) if n in r9]
    hard_all += report(entries, "9-MARK JUSTIFY", pairs)

    m12 = load_map("layer_c_12mark_coverage.py")
    with open(HERE / "layer_c_12mark_inventory.csv", encoding="utf-8-sig") as fh:
        r12 = {i + 1: r for i, r in enumerate(csv.DictReader(fh))}
    b12 = block_text("layer_c_12mark_blocks.txt")
    pairs = [(n, m12[n],
              " ".join([str(r12[n].get(k, "")) for k in ("Stem", "Topic", "AO1", "AO2", "AO3", "AO4")]
                       + [b12.get(n, "")]),
              str(r12[n]["Stem"])) for n in sorted(m12) if n in r12]
    hard_all += report(entries, "12-MARK EVALUATE", pairs)

    print("=" * 74)
    for _s, n, e, head in hard_all:
        print(f"  !! block [{n}] -> entry {e}  {head}")
    print("RESULT:", "OK — no mapping contradicts its block's official content."
          if not hard_all else "REVIEW the mappings above.")
    return 0 if not hard_all else 1


if __name__ == "__main__":
    sys.exit(main())
