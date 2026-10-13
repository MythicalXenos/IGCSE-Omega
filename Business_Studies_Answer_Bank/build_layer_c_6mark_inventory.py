#!/usr/bin/env python3
"""Build the Layer C 6-mark inventory: one row per block, with its real stem.

WHY THIS FILE EXISTS, AND WHY IT WAS REWRITTEN
----------------------------------------------
The 6-mark inventory (`layer_c_6mark_inventory.csv`) is the index the 6-mark
coverage map is keyed on — block number -> entry number. It had **no builder**:
the file named `build_layer_c_6mark_inventory.py` was a copy of the *9-mark*
builder, wrote `layer_c_9mark_inventory.csv`, and filtered `Mark value == "9"`.

Two consequences, both of which had to be repaired:

1. **The inventory could not be reproduced**, so its May-June 2024 block numbers
   stayed frozen to a dump made BEFORE the two misnamed mark schemes were
   renamed. After the rename the dump order flips (P1R sorts before P1), so the
   inventory and the block file disagreed about which block was which — and the
   coverage map was then "corrected" against the stale paper labels instead of
   against the content, which broke six mappings.
2. Stems ran on into the next heading. One bleed ("... to NOF Indica t ive
   content Mark 1 (g) AO2 = 3 marks ...") is why the same block scored 23%
   against the entry it correctly belongs to.

The block number is an index into the block file's order. **Rebuilding renumbers
May-June 2024's six blocks**, so the coverage map must be re-keyed at the same
time — `verify_chain_bank_anchors.py` is what proves the result either way.

Run from Business_Studies_Answer_Bank/:  python3 build_layer_c_6mark_inventory.py [--check]
`--check` writes nothing and reports whether the committed CSV would change.
"""
import argparse
import csv
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
BLOCKS = HERE / "layer_c_6mark_blocks.txt"
OUT = HERE / "layer_c_6mark_inventory.csv"
INSTANCES = HERE / "4BS1_Question_Instances.csv"

STEM = re.compile(r"(?:Question Number|Q\.\s*No\.)\s*(.*?)\s*"
                  r"(?:Indicative content Mark|Answer Mark)")
# The stem must stop at the question's own mark label. Without this, May-June
# 2021's fragmented text layer ("Indica t ive content Mark 1 (g) AO2 = 3 marks")
# is carried into the stem and pollutes everything scored against it.
TRIM = re.compile(r"\s*(?:Indica\s*t\s*ive|Indicative|Mark\s+\d\s*\([a-z]\)|A[O0]\s*[1-4]\s*=).*$",
                  re.S | re.I)
COMMAND = re.compile(
    r"\b(Analyse|Analyze|Assess|Discuss|Explain|Evaluate|Justify|Calculate"
    r"|State|Outline|Give|Identify|Describe|Complete|Do you think|Which)\b", re.I)
SESS = {
    "May-June 2019": "MayJune 2019", "May-June 2020": "MayJune 2020",
    "May-June 2021": "MayJune 2021", "May-June 2022": "MayJune 2022",
    "May-June 2024": "MayJune 2024", "May-June 2025": "MayJune 2025",
    "May 2023": "May 2023", "June 2026": "June 2026",
    "November 2021": "Nov 2021", "November 2023": "Nov 2023",
    "November 2024": "Nov 2024", "November 2025": "Nov 2025",
}


def build() -> list[dict]:
    parts = re.split(r"\n={78}\n=== (.+?)\n={78}\n",
                     BLOCKS.read_text(encoding="utf-8"))[1:]
    blocks = list(zip(parts[0::2], parts[1::2]))

    rows = list(csv.DictReader(INSTANCES.open(encoding="utf-8-sig")))
    by_paper = {}
    for r in rows:
        if r["Mark value"] == "6":
            by_paper.setdefault((r["Session"], r["Paper"]), []).append(
                r["Prompt/context excerpt (text extraction)"].strip())

    used, out = set(), []
    for i, (head, body) in enumerate(blocks, 1):
        session, paper, q = [x.strip() for x in head.split("|")]
        m = STEM.search(body)
        stem = TRIM.sub("", m.group(1).strip()).strip() if m else ""
        src = "mark scheme"
        if len(stem) < 15 or not COMMAND.search(stem):
            key = (SESS.get(session, session), paper)
            pool = [s for s in by_paper.get(key, []) if (key, s) not in used]
            stem, src = (pool[0], "instances CSV") if pool else ("*** UNKNOWN ***", "-")
            if pool:
                used.add((key, pool[0]))
        stem = TRIM.sub("", stem).strip()
        out.append(dict(n=i, session=session, paper=paper, question=q,
                        stem=stem, stem_source=src))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="write nothing; report whether the committed CSV would change")
    args = ap.parse_args()

    out = build()
    unknown = [r for r in out if r["stem"] == "*** UNKNOWN ***"]
    print(f"6-mark blocks            : {len(out)}  (expected 114)")
    print(f"stems from the MS        : {sum(1 for r in out if r['stem_source'] == 'mark scheme')}")
    print(f"stems from the CSV       : {sum(1 for r in out if r['stem_source'] == 'instances CSV')}")
    print(f"stems UNKNOWN            : {len(unknown)}")
    for r in unknown:
        print(f"   {r['session']} {r['paper']} {r['question']}")

    bad = []
    if len(out) != 114:
        bad.append(f"blocks: {len(out)} (expected 114)")
    if unknown:
        bad.append(f"{len(unknown)} block(s) with an unknown stem source")
    print()
    print("RESULT:", "OK — 114 six-mark blocks, every stem sourced." if not bad
          else "FAIL — " + "; ".join(bad))
    if bad:
        return 1

    if args.check:
        old = list(csv.DictReader(OUT.open(encoding="utf-8")))
        diff = [(a["n"], a["session"], a["paper"], a["question"], a["stem"][:44], b["stem"][:44])
                for a, b in zip(old, out)
                if (a["session"], a["paper"], a["question"], a["stem"]) !=
                   (b["session"], b["paper"], b["question"], b["stem"])]
        print(f"\nrows that differ from the committed CSV: {len(diff)}")
        for d in diff[:12]:
            print(f"   [{d[0]:>3}] {d[1]} {d[2]} {d[3]}  {d[4]!r} -> {d[5]!r}")
        return 0

    with OUT.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0]))
        w.writeheader()
        w.writerows(out)
    print(f"\nwrote {OUT.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
