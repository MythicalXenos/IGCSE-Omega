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


def phrases(a: str, b: str, n: int = 9) -> int:
    """How many n-word sequences the two texts share VERBATIM.

    The overlap score below is a bag of keywords, and for a 9-mark entry it
    under-reports badly: the model is written on one case and quotes the other
    blocks' own phrases, so it can share thirty-nine-word sentences with a block
    and still score 39% on keyword overlap. A mapping that shares 11 such phrases
    is covered; the score alone cannot say so.
    """
    def grams(t):
        w = re.findall(r"[a-z0-9']+", t.lower())
        return {" ".join(w[i:i + n]) for i in range(max(0, len(w) - n + 1))}
    return len(grams(a) & grams(b))


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
    print(f"\n  {'weakest 8 of the rest':<46}  overlap  9-word phrases shared")
    for score, n, entry_no, head in flagged[:8]:
        ent = entries.get(entry_no, "")
        shared = phrases(next((p[2] for p in pairs if p[1] == entry_no), ""), ent)
        print(f"  block [{n:>3}] -> entry {entry_no:<3} {head:<58} {score:6.1%}   {shared:>3}")
    hard = [f for f in flagged if f[0] < floor]
    print(f"\n  below the contradiction floor ({floor:.0%}): {len(hard)}")
    for score, n, entry_no, head in hard:
        print(f"    !! block [{n:>3}] -> entry {entry_no:<3} {head}  {score:.1%}")
    print()
    if not flagged:
        print("  every mapping scores above the worry line.")
    hard = [f for f in flagged if f[0] < floor]
    # THE BAND MUST BE THE BAND. This printed `len(flagged) - len(hard)` - everything
    # above the floor - under a label that said "30%-45%", so an 81.2% mapping was
    # counted as "worth reading by hand". A count that does not match its own label
    # is the failure this bank keeps finding in its prose; it had one in its code.
    band = [f for f in flagged if floor <= f[0] < WORRY]
    print(f"\n  below the contradiction floor ({floor:.0%}) : {len(hard)}")
    print(f"  worth reading by hand ({FLOOR:.0%}–{WORRY:.0%}) : {len(band)}")
    for score, n, entry_no, head in band[:12]:
        ent = entries.get(entry_no, "")
        shared = phrases(next((p[2] for p in pairs if p[1] == entry_no), ""), ent)
        verdict = "covered - shares the scheme's own phrases" if shared >= 5 else "READ THIS ONE"
        print(f"    block [{n:>3}] -> entry {entry_no:<3} {head}  {score:.1%}  "
              f"({shared} shared 9-word phrases) {verdict}")
    if len(band) > 12:
        print(f"    … and {len(band) - 12} more in the band")
    print()
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

    # ---- every cited question is either OWNED by its entry or pointed at ----
    # An entry's "Also asked" line tells the reader "this question is this topic; write
    # it this way". When the cited question is a SIBLING topic owned by a different
    # entry, the reader is being sent to the wrong chains - the Kaizen entry citing the
    # Kraft Heinz waste question, whose chains live in the entry on using resources
    # effectively. 12 citations did this. All 12 now name the entry that owns the
    # question ("see entry 154"), which is what entry 163 already did. A citation with
    # no pointer and no ownership is the failure this catches.
    print("=" * 74)
    print("CITED QUESTIONS — every one is owned by its entry, or names the entry that owns it")
    print("=" * 74)
    owner = {}
    for tier, script in (("6", "layer_c_6mark_coverage.py"),
                         ("9", "layer_c_9mark_coverage.py"),
                         ("12", "layer_c_12mark_coverage.py")):
        for blk, ent in load_map(script).items():
            owner[(tier, blk)] = ent
    covered = {}
    for (tier, blk), ent in owner.items():
        covered.setdefault(ent, set()).add((tier, blk))
    inv = {}
    for tier, fname in (("6", "layer_c_6mark_inventory.csv"),
                        ("9", "layer_c_9mark_inventory.csv")):
        with open(HERE / fname, encoding="utf-8-sig") as fh:
            for i, r in enumerate(csv.DictReader(fh), 1):
                inv[(r["session"], r["paper"], r["question"].replace(" ", ""))] = (tier, i)
    sessions = {"june 2026": "June 2026", "may-june 2019": "May-June 2019",
                "may-june 2020": "May-June 2020", "may-june 2021": "May-June 2021",
                "may-june 2022": "May-June 2022", "may 2023": "May 2023",
                "may-june 2024": "May-June 2024", "may-june 2025": "May-June 2025",
                "nov 2020": "November 2020", "nov 2021": "November 2021",
                "june 2021": "May-June 2021", "nov 2023": "November 2023",
                "nov 2024": "November 2024", "nov 2025": "November 2025",
                "june 2022": "May-June 2022", "june 2024": "May-June 2024",
                "june 2025": "May-June 2025", "june 2019": "May-June 2019"}
    cite = re.compile(r'\*"([^"]{15,200}?)"\*\s*[\u2014\u2013-]{1,2}\s*\*{0,2}'
                      r'([A-Za-z0-9\u2013\u2014\- ]{4,26}?)\*{0,2}\s+(P\dR?)[,. ]*(\d\s*\(\w\))?')
    cited, pointed, unexplained = 0, 0, []
    for ent, txt in sorted(bank_entries().items()):
        for m in cite.finditer(txt):
            quote, sess_raw, paper, qn = m.groups()
            if not qn:
                continue
            sess = next((v for k, v in sessions.items() if k in sess_raw.lower()), None)
            if not sess:
                continue
            cited += 1
            blk = inv.get((sess, paper, qn.replace(" ", "")))
            if not blk or blk in covered.get(ent, set()):
                continue
            # A pointer is a pointer whether or not the number is bolded: entry 163
            # writes "see entry 164", entry 183 "*(see entry 179)*", and the ten added
            # on 14 Oct 2026 "see **entry 157**". Strip the markdown, then look.
            after = txt[m.end():m.end() + 260].replace("*", "")
            if "see entry" in after or "full answer" in after:
                pointed += 1
                continue
            unexplained.append((ent, sess, paper, qn, quote[:56]))
    print(f"  citations naming a session, paper and question: {cited}")
    print(f"  sibling citations carrying a pointer to the owning entry: {pointed}")
    if not cited:
        print("  NONE PARSED — check the parser, not the bank.")
        hard_all.append(("CITE", 0, 0, "no entry citation parsed"))
    for ent, sess, paper, qn, quote in unexplained:
        print(f"  !! entry {ent} cites {sess} {paper} {qn} — owned by entry "
              f"{owner.get(inv[(sess, paper, qn.replace(' ', ''))], '?')} — with no pointer")
        hard_all.append(("CITE", 0, ent, "citation of " + quote + " needs a see-entry-N pointer"))
    if cited and not unexplained:
        print("  every one either belongs to its entry or names the entry that owns it.")

    # ---- the labelling contract: every model answer carries its own label ----
    # The file declares its batches ("Batches 1 and 2 were CONSTRUCTED throughout")
    # and that is how entries 1-49 came to sit under a batch heading with no label
    # on the entry itself. That is not enough in a file that mixes all three kinds:
    # a reader looking at one entry cannot see which batch range it falls in. 49
    # model answers were unlabelled until 14 Oct 2026; every one is labelled now.
    print("=" * 74)
    print("LABELLING — every model answer carries its own label")
    print("=" * 74)
    cb = (HERE / "Perfect_Answers" / "10_Chain_Bank.md").read_text(encoding="utf-8")
    ok_label = ("`[CONSTRUCTED GRADE 9 TARGET]`", "`[OFFICIAL MARK-SCHEME WORKED ANSWER]`")
    model_lines = [l for l in cb.split("\n") if re.match(r"^> \*\*Model answer", l)]
    unlabelled = [l for l in model_lines if not any(t in l for t in ok_label)]
    print(f"  model-answer lines: {len(model_lines)}   carrying their own label: "
          f"{len(model_lines) - len(unlabelled)}")
    if not model_lines:
        print("  NONE PARSED — check the parser, not the bank.")
        hard_all.append(("LABEL", 0, 0, "no model-answer line parsed"))
    for l in unlabelled:
        print(f"  !! {l[:88]}")
        hard_all.append(("LABEL", 0, 0, l[:60]))
    if model_lines and not unlabelled:
        print("  none unlabelled.")

    print("=" * 74)
    for _s, n, e, head in hard_all:
        print(f"  !! block [{n}] -> entry {e}  {head}")
    print("RESULT:", "OK — no mapping contradicts its block's official content."
          if not hard_all else "REVIEW the mappings above.")
    return 0 if not hard_all else 1


if __name__ == "__main__":
    sys.exit(main())
