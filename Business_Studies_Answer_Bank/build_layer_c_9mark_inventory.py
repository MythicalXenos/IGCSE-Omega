#!/usr/bin/env python3
"""Build the Layer C 9-mark inventory: one row per Justify block, with its OPTIONS.

WHY THIS IS BUILT FROM THE OPTIONS RATHER THAN THE STEM
-------------------------------------------------------
Every 9-mark question in this qualification uses the same single framing:

    "Justify which one of these two options X should choose."

So the FRAMING is constant and carries no information. **What varies -- and what
an entry actually has to answer -- is the OPTION PAIR.** That pair, plus the
scheme's AO4 counter-arguments for each option, is printed inside the mark-scheme
block itself, for all 76 blocks, regardless of whether the stem came through.

The stem is recovered where the mark scheme prints it. Where it does not, the
question is reconstructed from the options -- and marked as reconstructed, because
this bank does not present a reconstruction as a quotation.

Do NOT pair blocks against `4BS1_Question_Instances.csv` positionally: that file
under-detects 9-mark questions on 19 of the 38 papers (rule 120), so block N and
CSV row N are not the same question. That mistake produced 20 blank stems.

Writes layer_c_9mark_inventory.csv.
"""
import csv
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
BLOCKS = HERE / "layer_c_9mark_blocks.txt"
OUT = HERE / "layer_c_9mark_inventory.csv"

STEM = re.compile(r"(?:Question Number|Q\.\s*No\.)\s*(.*?)\s*"
                  r"(?:Indicative content Mark|Answer Mark)")
COMMAND = re.compile(r"\b(Justify|Analyse|Analyze|Assess|Evaluate|Discuss|Explain)\b", re.I)
# "Option 1 – wording" / "Option 1: wording" / "Option 1 - wording"
OPT = re.compile(r"Option\s*([12])\s*[:\u2013\u2014-]\s*(.*?)(?=\s*Option\s*[12]\s*[:\u2013\u2014-]|$)", re.I)


def main() -> int:
    parts = re.split(r"\n={78}\n=== (.+?)\n={78}\n", BLOCKS.read_text(encoding="utf-8"))[1:]
    blocks = list(zip(parts[0::2], parts[1::2]))

    out = []
    for i, (head, body) in enumerate(blocks, 1):
        session, paper, q = [x.strip() for x in head.split("|")]
        m = STEM.search(body)
        stem = m.group(1).strip() if m else ""
        if len(stem) < 15 or not COMMAND.search(stem):
            stem = ""

        # The block is: header, then the AO2 section, then AO3, then AO4.
        # Split on the AO SECTION MARKERS that follow the header -- taking the
        # LAST occurrence of "AO2" instead lands inside a bullet and returns an
        # empty section, which is how this first came out with zero options.
        # The level descriptors repeat the AO markers ("...to the business
        # context. (AO2)") and the block then runs on into the NEXT question, so
        # the document holds many AO2/AO3/AO4 strings. The real content sections
        # are the FIRST run of them. Take that, and stop before the repeat.
        cut_pt = len(body)
        level = body.find("Level Mark Descriptor")
        if level > 0:
            cut_pt = level
        body = body[:cut_pt]
        first_bullet = body.find("\u2022")
        hdr = re.search(r"[^|]*\d\s*marks?",
                        body[:first_bullet if first_bullet > 0 else 200])
        rest = body[hdr.end():] if hdr else body

        cuts = list(re.finditer(r"\bA[O0]\s*([234])\b", rest))
        sections, seen = {}, set()
        for j, c in enumerate(cuts):
            num = int(c.group(1))
            if num in seen:          # a repeat = the descriptors have begun
                break
            seen.add(num)
            end = cuts[j + 1].start() if j + 1 < len(cuts) else len(rest)
            sections[num] = rest[c.end():end].strip()

        opts = {}
        for om in OPT.finditer(sections.get(2, "")):
            opts[int(om.group(1))] = om.group(2).strip().rstrip(".")
        ao4 = sections.get(4, "").strip()

        out.append(dict(n=i, session=session, paper=paper, question=q,
                        stem=stem, stem_source="mark scheme" if stem else "RECONSTRUCTED",
                        option_1=opts.get(1, ""), option_2=opts.get(2, ""),
                        ao4_judgement=" ".join(ao4.split())))

    with OUT.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0]))
        w.writeheader()
        w.writerows(out)

    n_opt = sum(1 for r in out if r["option_1"] and r["option_2"])
    n_ao4 = sum(1 for r in out if len(r["ao4_judgement"]) > 40)
    print(f"blocks                  : {len(out)}")
    print(f"stems printed by the MS : {sum(1 for r in out if r['stem'])}")
    print(f"blocks with BOTH options: {n_opt}")
    print(f"blocks with AO4 content : {n_ao4}")
    if n_opt < len(out):
        print("  no options found on blocks:",
              [r["n"] for r in out if not (r["option_1"] and r["option_2"])])
    print(f"wrote {OUT.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
