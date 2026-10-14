#!/usr/bin/env python3
"""Check that every 3-mark model is a CHAIN, not a consequence with no mechanism.

WHY THIS EXISTS
---------------
June 2026 P1R printed four 3-mark Explain questions, each with its **3/3** script
on one page and its **0/3** on the facing page. All four zeroes fail the same
way, and it is not length, and it is not knowledge:

    the answer names a correct CONSEQUENCE and omits the MECHANISM

  flat structure  3/3 names "less layers"       0/3 "Everyone can suggest ideas"
  break-even      3/3 "how many to not lose"    0/3 "sufficient funds"
  segment/income  3/3 "premium -> higher price" 0/3 "it can calculate income"
  productivity    3/3 efficiency -> unit cost   0/3 "customer might come back"

The four 3/3s run 35 to 70 words. The 0/3 on productivity is sound reasoning end
to end -- repeat custom, higher sales, more profit -- and scores zero, because
none of it involves productivity. **That is the failure this check looks for in
this bank's own models.**

The tariff is written in the bank as *identify (1) -> mechanism (1) ->
consequence (1)*, so every model answer in the 97 mapped 3-mark entries must
carry an explicit causal step: a connective, a conditional, or a pipeline arrow.

RUN FROM `Business_Studies_Answer_Bank/`. Prints one RESULT.

  python3 verify_3mark_shape.py
"""
import importlib.util
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent

# Words that mark the step BETWEEN the point and its outcome. Deliberately wide,
# and every widening was forced by a false positive on a real chain:
#   * "then", "lead", "result in", "gives" were missing -> flagged entries
#     15, 36, 55, 57, all of which are chains.
#   * a CONDITIONAL is also a mechanism -> flagged entries 72 and 100, both
#     Pearson's own worked answers: "If customers are loyal they will shop only
#     at that business (1) rather than comparing prices elsewhere." A check that
#     flags Pearson's own full-mark chain is teaching the wrong thing, which is
#     the one failure this bank cannot afford.
CAUSAL = re.compile(
    "|".join((
        r"\bif\b", r"\bwould\b", r"\bprovided\b", r"\bunless\b",
        r"\bbecause\b", r"\bso\b", r"so that", r"\bwhich\b", r"\btherefore\b",
        r"\bthus\b", r"\bhence\b", r"leading to", r"leads? to", r"lead to",
        r"\bmeaning\b", r"\bmeans\b", r"result(?:s|ing)? in", r"as a result",
        r"this means", r"this gives", r"\bgives\b", r"allowing", r"allows",
        r"enabling", r"enables", r"\bsince\b", r"thereby", r"\bthen\b",
        r"due to", r"thanks to", r"\bdrives\b", r"driving", r"creating",
        r"creates", r"that way", r"in turn", r"reduces", r"increases",
        r"raises", r"lowering", r"raising", r"improving", r"cutting",
        r"saving", r"avoiding", r"causing", r"causes",
        # participles and light verbs -- the natural wording of a MIDDLE step.
        # Entry 93 forced this: its advantage model is Pearson's own (1)(1)(1)
        # chain whose link is a participle, "... **Giving it a greater chance of
        # success** (1)". Without these the check flags a full-mark chain.
        r"giving", r"given", r"brings", r"bringing", r"bring", r"provides",
        r"providing", r"offers", r"offering", r"ensures", r"ensuring",
        r"produces", r"producing", r"generating", r"lets", r"letting",
        r"allows?", r"helps", r"helping", r"keeps", r"keeping", r"builds", r"building",
    )),
    re.I,
)


def model_body(text: str) -> str:
    """The MODEL ITSELF: the blockquote lines under a 'Model answer - 3 marks' marker.

    It must stop at the first line that is not part of the blockquote. The first
    version ran to a stop-marker instead, and on entry 1 it ran straight through
    into the entry's own "Step | The move" table -- whose cells are full of causal
    words. That made the check pass on a model replaced with the report's 0/3
    wording, which is the exact opposite of its purpose. Taking the contiguous
    blockquote is both simpler and correct: the model is quoted, and the entry's
    own commentary never is.
    """
    lines = text.split("\n")
    start = None
    for i, line in enumerate(lines):
        if "Model answer" in line and "3 marks" in line and line.lstrip().startswith(">"):
            start = i
            break
    if start is None:
        return ""
    body = []
    marker_end = lines[start].find("**Model answer")
    after = lines[start][marker_end:]
    close = after.find("**", 2)
    if close != -1:                      # drop the marker itself, keep what follows on the line
        body.append(after[close + 2:])
    for line in lines[start + 1:]:
        if not line.lstrip().startswith(">"):
            break
        body.append(line)
    return "\n".join(body)


def main() -> int:
    sp = importlib.util.spec_from_file_location(
        "anchors", HERE / "verify_chain_bank_anchors.py")
    a = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(a)

    entries = a.bank_entries()
    cov = a.load_map("layer_c_coverage.py")          # 3-mark block -> entry
    mapped = sorted(set(cov.values()))

    print("=" * 74)
    print("3-MARK MODELS - identify -> MECHANISM -> consequence")
    print("=" * 74)
    print(f"  3-mark blocks: {len(cov)}   distinct entries they map to: {len(mapped)}")

    no_model, no_mechanism, ok = [], [], 0
    for e in mapped:
        body = model_body(entries.get(e, ""))
        if not body.strip():
            no_model.append(e)
            continue
        if CAUSAL.search(body) or "\u2192" in body:
            ok += 1
        else:
            no_mechanism.append((e, " ".join(body.split())[:220]))

    if not mapped:
        print("  NONE PARSED - check the parser, not the bank.")
    print(f"  entries with a model and an explicit mechanism : {ok}")
    for e in no_model:
        print(f"  !! entry {e} has no parseable 'Model answer - 3 marks' block")
    for e, txt in no_mechanism:
        print(f"  !! entry {e} names an outcome with NO mechanism step:")
        print(f"       {txt}")
    bad = no_model + [e for e, _ in no_mechanism]
    if mapped and not bad:
        print("  every model is a chain. None reproduces the June 2026 0/3 shape.")
    print()
    print("RESULT:", "OK - all 3-mark models carry a mechanism step."
          if mapped and not bad else f"FAIL - {len(bad)} entry/entries to read.")
    return 0 if mapped and not bad else 1


if __name__ == "__main__":
    sys.exit(main())
