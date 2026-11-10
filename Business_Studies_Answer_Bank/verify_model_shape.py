#!/usr/bin/env python3
"""Check every governed model against the SHAPE its tariff requires.

There are four governed tariffs and each has a shape the mark schemes and the
examiner reports state, not a style preference:

    3-mark Explain   identify (1) -> MECHANISM (1) -> consequence (1)
                     Four June 2026 P1R 0/3 answers all fail by naming a correct
                     consequence and omitting the mechanism.
    6-mark Analyse   one developed point with interconnected strands (AO2+AO3).
    9-mark Justify   a choice, both sides, and a NAMED CONDITION (rule 91).
                     Every 8/9 in the bank fails on the condition, not the prose.
    12-mark Evaluate AO1/AO2/AO3/AO4 at 3 marks each - the evaluation is woven
                     through, and a 10/12 is "limited judgements" (rule 83).

This script reads the blockquote that IS the model (never the entry's own
commentary about it) and checks that shape. Run from
`Business_Studies_Answer_Bank/`; prints one RESULT per tier.

  python3 verify_model_shape.py

WHY THE BLOCKQUOTE RULE IS IN HERE, NOT JUST IN THE CODE
-------------------------------------------------------
The first version of the 3-mark check read "everything from the marker to a
stop-word", which ran through into the entry's own "Step | The move" table - and
that table is full of causal vocabulary. It therefore PASSED on a model replaced
with the report's own 0/3 wording, "Everyone can suggest ideas." Reading only the
contiguous blockquote is what makes the check mean anything.
"""
import importlib.util
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent

# ---------------------------------------------------------------------------
# The model, and only the model.
# ---------------------------------------------------------------------------
# 3-, 6- and 9-mark entries open a blockquote with "**Model answer — N marks**".
# 12-mark entries open theirs with the label itself inside a blockquote heading.
MARKERS = {
    3: re.compile(r"Model answer[^\n]*3 marks"),
    6: re.compile(r"Model answer[^\n]*6 marks"),
    9: re.compile(r"Model answer[^\n]*9 marks"),
    12: re.compile(r"CONSTRUCTED GRADE 9 TARGET"),
}

# Words that mark the step BETWEEN a point and its outcome. Wide on purpose, and
# every widening was forced by a false positive on a real chain:
#   * "then", "lead", "result in", "gives" were missing -> flagged entries
#     15, 36, 55, 57, all chains.
#   * a CONDITIONAL is a mechanism -> flagged entries 72 and 100, Pearson's own
#     worked answers ("If customers are loyal they will shop only at that
#     business (1) ...").
#   * a PARTICIPLE is a mechanism -> flagged entry 93, also Pearson's own
#     ("Giving it a greater chance of success (1)").
CAUSAL = re.compile("|".join((
    r"\bif\b", r"\bwould\b", r"\bprovided\b", r"\bunless\b", r"\bbecause\b",
    r"\bso\b", r"so that", r"\bwhich\b", r"\btherefore\b", r"\bthus\b",
    r"\bhence\b", r"leading to", r"leads? to", r"lead to", r"\bmeaning\b",
    r"\bmeans\b", r"result(?:s|ing)? in", r"as a result", r"this means",
    r"this gives", r"\bgives\b", r"allowing", r"allows", r"enabling",
    r"enables", r"\bsince\b", r"thereby", r"\bthen\b", r"due to",
    r"thanks to", r"\bdrives\b", r"driving", r"creating", r"creates",
    r"that way", r"in turn", r"reduces", r"increases", r"raises", r"lowering",
    r"raising", r"improving", r"cutting", r"saving", r"avoiding", r"causing",
    r"causes", r"giving", r"given", r"brings", r"bringing", r"bring",
    r"provides", r"providing", r"offers", r"offering", r"ensures",
    r"ensuring", r"produces", r"producing", r"generating", r"lets",
    r"letting", r"allows?", r"helps", r"helping", r"keeps", r"keeping",
    r"builds", r"building", r"otherwise", r"rather than", r"instead",
)), re.I)

# The 9-mark gate, rule 91 — the named condition.
CONDITION = re.compile(
    r"\b(condition|provided|as long as|only if|unless|assuming|so long as|"
    r"depends on|depend on|if it|if the|if they|if this)\b", re.I)

# The 12-mark gate, rules 82/83 — a woven judgement.
JUDGEMENT = re.compile(
    r"\b(however|depends|although|on the other hand|whereas|judgement|"
    r"overall|unless|provided|balance|but if|limited|extent|likely)\b", re.I)


def models(text: str, tier: int):
    """Every MODEL blockquote in an entry: contiguous '>' lines from its marker."""
    lines = text.split("\n")
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        if line.lstrip().startswith(">") and MARKERS[tier].search(line):
            body, k = [], i
            while k < len(lines) and lines[k].lstrip().startswith(">"):
                body.append(lines[k])
                k += 1
            out.append("\n".join(body))
            i = k
        else:
            i += 1
    return out


def main() -> int:
    sp = importlib.util.spec_from_file_location(
        "anchors", HERE / "verify_chain_bank_anchors.py")
    a = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(a)
    entries = a.bank_entries()

    tiers = (
        (3, "layer_c_coverage.py",
         lambda m: CAUSAL.search(m) or "\u2192" in m,
         "an explicit MECHANISM step (identify -> mechanism -> consequence)"),
        (6, "layer_c_6mark_coverage.py",
         lambda m: len(CAUSAL.findall(m)) >= 2,
         "at least two chain links (one point, developed strands)"),
        (9, "layer_c_9mark_coverage.py",
         lambda m: bool(CONDITION.search(m)),
         "a NAMED CONDITION in the judgement (rule 91)"),
        (12, "layer_c_12mark_coverage.py",
         lambda m: len(JUDGEMENT.findall(m)) >= 3 and len(m.split()) >= 120,
         "a woven judgement - >=3 evaluation markers and >=120 words (rules 82-83)"),
    )

    problems = []
    for tier, mapfile, test, what in tiers:
        cov = a.load_map(mapfile)
        mapped = sorted(set(cov.values()))
        print("=" * 74)
        print(f"{tier}-MARK MODELS - must carry {what}")
        print("=" * 74)
        print(f"  blocks: {len(cov)}   distinct entries: {len(mapped)}")

        total, thin = 0, []
        for e in mapped:
            ms = models(entries.get(e, ""), tier)
            if not ms:
                thin.append((e, "no model blockquote found"))
                continue
            total += len(ms)
            for m in ms:
                if not test(m):
                    thin.append((e, " ".join(m.split())[:170]))
                    break
        print(f"  models parsed: {total}")
        if not mapped:
            print("  NONE PARSED - check the parser, not the bank.")
            problems.append(f"{tier}-mark: the map parsed nothing")
        for e, txt in thin:
            print(f"  !! entry {e}: {txt}")
            problems.append(f"{tier}-mark entry {e}")
        if mapped and not thin:
            print(f"  all {len(mapped)} entries pass.")
        print()

    print("=" * 74)
    print("RESULT:", "OK - every governed model has the shape its tariff requires."
          if not problems else f"FAIL - {len(problems)} entry/entries to read.")
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
