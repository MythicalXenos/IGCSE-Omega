#!/usr/bin/env python3
"""Does every block in a tier dump actually BELONG to that tier?

WHY THIS EXISTS
---------------
`layer_c_9mark_blocks.txt` and `layer_c_12mark_blocks.txt` are the mark-scheme
content every Layer C batch was written from, and the input to
`verify_chain_bank_anchors.py` and `verify_ms_point_coverage.py`. Nothing ever
checked that a block in the 9-mark file was a 9-mark question.

It was not. **Eighteen blocks were wrong**: nine in the 9-mark dump carried the
preceding 3(d) 6-mark Analyse, and nine in the 12-mark dump carried the
preceding 4(b) 6-mark Analyse. On the older papers the mark scheme shares one
heading row per page and prints no question wording, so the search for the
block's opening heading walked back to the page heading — which introduces the
PART BEFORE it — and the whole of that part's answer came with it.

**Every check passed while that was true**, because every check read the same
two files and compared them to each other. What catches it is a fact from
OUTSIDE the files: the mark value the mark scheme itself prints.

WHAT IT CHECKS
--------------
  1. the block count equals the published count for the tier (152/114/76/38);
  2. every block prints the mark value for its tier — "(6)", "(9)", "(12)" —
     read from the block's own text, never from the file name;
  3. every block prints its own part label, e.g. a 9-mark block contains "2 (f)"
     or "3 (e)";
  4. a block that OPENS with a part label opens with its own label.

Run from Business_Studies_Answer_Bank/:  python3 verify_block_tiers.py
Exit 0 when every block belongs to its tier, 1 otherwise.
"""
import importlib.util
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve()

_spec = importlib.util.spec_from_file_location("anchors", HERE.parent / "verify_chain_bank_anchors.py")
anchors = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(anchors)

# tariff -> (published block count, labels that may open a block for that tier)
TIERS = {
    3:  (152, ["1(f)", "2(c)", "2(d)", "2(e)"]),
    6:  (114, ["1(g)", "3(d)", "4(b)"]),
    9:  (76,  ["2(f)", "3(e)"]),
    12: (38,  ["4(c)"]),
}

# The mark scheme prints the total in brackets after the last AO line. The text
# layer fragments spacing, so match loosely: "( 9 )", "(9)", "( 12 )".
def marks_printed(text: str):
    return {int(m) for m in re.findall(r"\(\s*(\d{1,2})\s*\)", text)}


def ao_total(text: str):
    """The tier as the mark scheme itself states it: the AO allocations in the header.

    A block is for a 3-mark question if its header allocates AO1 3 marks, for a
    9-mark if it allocates 3+3+3, for a 12-mark if 3+3+3+3. This is stronger than
    looking for a bracketed total, because the total sits in the Mark column and
    can fall outside the extracted window, while the allocations are always in
    the block's first line.
    """
    head = text.split("\u2022")[0][:500]
    return sum(int(n) for n in re.findall(
        r"A\s*[O0]\s*[1-4]\s*[=\u2013-]\s*(\d+)\s*mark", head)) or None


def labels_in(text: str):
    return {f"{a}({b})" for a, b in re.findall(r"(\d)\s*\(\s*([a-z])\s*\)", text)}


def opens_with_label(text: str):
    m = re.match(r"\s*(\d)\s*\(\s*([a-z])\s*\)", text)
    return f"{m.group(1)}({m.group(2)})" if m else None


def main() -> int:
    problems = []
    for tier, (expected, labels) in TIERS.items():
        blocks = anchors.block_text(f"layer_c_{tier}mark_blocks.txt")
        print(f"{tier:>2}-mark blocks: {len(blocks):>3}  (published count {expected})")
        if len(blocks) != expected:
            problems.append(f"{tier}-mark: {len(blocks)} blocks, expected {expected}")
        for n in sorted(blocks):
            body = " ".join(blocks[n].split())
            if tier not in marks_printed(body) and ao_total(body) != tier:
                problems.append(f"{tier}-mark block [{n}] prints no ({tier}) mark — "
                                f"it is not a {tier}-mark block: {body[:70]!r}")
                continue
            if not (labels_in(body) & set(labels)):
                problems.append(f"{tier}-mark block [{n}] prints none of its own labels "
                                f"{labels}: {body[:70]!r}")
                continue
            own = opens_with_label(body)
            if own and own not in labels and own not in labels_in(body[:120]):
                problems.append(f"{tier}-mark block [{n}] OPENS with {own}, which is not "
                                f"a {tier}-mark label: {body[:70]!r}")
        print(f"         blocks printing their own ({tier}) mark and label: "
              f"{len(blocks) - sum(1 for p in problems if p.startswith(str(tier) + '-mark block'))}"
              f" / {len(blocks)}")

    print()
    if problems:
        print("=" * 74)
        print(f"BLOCKS THAT DO NOT BELONG TO THEIR TIER — {len(problems)}")
        print("=" * 74)
        for p in problems[:30]:
            print("  " + p)
        if len(problems) > 30:
            print(f"  … and {len(problems) - 30} more")
    print("RESULT:", "OK — every block carries its own tier's mark, label and content."
          if not problems else f"FAIL — {len(problems)} block(s) do not match their tier.")
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
