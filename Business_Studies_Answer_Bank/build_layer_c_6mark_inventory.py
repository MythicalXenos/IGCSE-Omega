#!/usr/bin/env python3
"""Build the Layer C 9-mark inventory: one row per block, with its real stem.

The block file carries a stem for most blocks, but the 2019, 2020 and Nov 2021
papers do not print Q1's questions in the mark scheme at all, and the P2 papers
of 2024/2025 are inconsistent. Where the mark scheme has no stem, the question
text is taken from `4BS1_Question_Instances.csv` -- which is fine for CONTENT
(rule 120 forbids using it for counts only).

Writes layer_c_9mark_inventory.csv.
"""
import csv
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
BLOCKS = HERE / "layer_c_9mark_blocks.txt"
INSTANCES = HERE / "4BS1_Question_Instances.csv"
OUT = HERE / "layer_c_9mark_inventory.csv"

STEM = re.compile(r"(?:Question Number|Q\.\s*No\.)\s*(.*?)\s*"
                  r"(?:Indicative content Mark|Answer Mark)")
# A real stem carries a command word. Without this test the head-walk happily
# returns the PREVIOUS question's calculation workings, which read like a stem
# until you notice they say "Award 1 mark for correctly substituting numbers".
COMMAND = re.compile(
    r"\b(Analyse|Analyze|Assess|Discuss|Explain|Evaluate|Justify|Calculate"
    r"|State|Outline|Give|Identify|Describe|Complete|Do you think|Which)\b", re.I)
SESS = {  # block-file name -> instances-file name
    "May-June 2019": "MayJune 2019", "May-June 2020": "MayJune 2020",
    "May-June 2021": "MayJune 2021", "May-June 2022": "MayJune 2022",
    "May-June 2024": "MayJune 2024", "May-June 2025": "MayJune 2025",
    "May 2023": "May 2023", "June 2026": "June 2026",
    "November 2021": "Nov 2021", "November 2023": "Nov 2023",
    "November 2024": "Nov 2024", "November 2025": "Nov 2025",
}


def main() -> int:
    parts = re.split(r"\n={78}\n=== (.+?)\n={78}\n",
                     BLOCKS.read_text(encoding="utf-8"))[1:]
    blocks = list(zip(parts[0::2], parts[1::2]))

    rows = list(csv.DictReader(INSTANCES.open(encoding="utf-8-sig")))
    by_paper = {}
    for r in rows:
        if r["Mark value"] == "9":
            by_paper.setdefault((r["Session"], r["Paper"]), []).append(
                r["Prompt/context excerpt (text extraction)"].strip())

    used, out = set(), []
    for i, (head, body) in enumerate(blocks, 1):
        session, paper, q = [x.strip() for x in head.split("|")]
        m = STEM.search(body)
        stem = m.group(1).strip() if m else ""
        src = "mark scheme"
        if len(stem) < 15 or not COMMAND.search(stem):
            key = (SESS.get(session, session), paper)
            pool = [s for s in by_paper.get(key, []) if (key, s) not in used]
            stem, src = (pool[0], "instances CSV") if pool else ("*** UNKNOWN ***", "-")
            if pool:
                used.add((key, pool[0]))
        out.append(dict(n=i, session=session, paper=paper, question=q,
                        stem=stem, stem_source=src))

    with OUT.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0]))
        w.writeheader()
        w.writerows(out)

    unknown = [r for r in out if r["stem"] == "*** UNKNOWN ***"]
    print(f"blocks            : {len(out)}")
    print(f"stems from MS     : {sum(1 for r in out if r['stem_source'] == 'mark scheme')}")
    print(f"stems from CSV    : {sum(1 for r in out if r['stem_source'] == 'instances CSV')}")
    print(f"still unknown     : {len(unknown)}  -> blocks {[r['n'] for r in unknown]}")
    print(f"wrote {OUT.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
