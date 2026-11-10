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

        # RE-ANCHOR (added after the block extractor started backing up to the
        # nearest real stem heading): a block now OPEN includes the tail of the
        # previous question, whose own "Level Mark Descriptor" and "(AO2)"
        # markers are the ones a naive read finds first. Take the LAST heading
        # whose following text actually yields a usable run of AO sections.
        def _sections(seg):
            cut = seg.find("Level Mark Descriptor")
            if cut > 0:
                seg = seg[:cut]
            fb = seg.find("\u2022")
            h = re.search(r"[^|]*\d\s*marks?", seg[:fb if fb > 0 else 200])
            rest = seg[h.end():] if h else seg
            c = list(re.finditer(r"\bA[O0]\s*([234])\b", rest))
            sec, seen = {}, set()
            for j, cc in enumerate(c):
                num = int(cc.group(1))
                if num in seen:
                    break
                seen.add(num)
                end = c[j + 1].start() if j + 1 < len(c) else len(rest)
                sec[num] = rest[cc.end():end].strip()
            return sec

        anchor, sections = -1, {}
        # MJ2021 fragments the heading ("Quest ion Number") - allow the spaces.
        for m0 in re.finditer(r"(?i)(?:q\s*u\s*e\s*s\s*t\s*i\s*o\s*n\s*n\s*u\s*m\s*b\s*e\s*r"
                              r"|q\.\s*n\s*o\.)", body):
            sec = _sections(body[m0.end():])
            if len(sec) >= 2:
                anchor, sections = m0.start(), sec
        if not sections:
            # A block that must not be contaminated by the part above it starts at
            # its OWN row label and carries no heading ("2 (f) AO2 = 3 marks ...
            # AO4 = 3 marks ... Option 1 ..."). It still has every section - the
            # scheme's own AO allocations - so parse from the start of the block.
            # Requiring a heading is what silently emptied 19 rows of this CSV.
            sections = _sections(body)
        stem = ""
        if anchor >= 0:
            sm = STEM.search(body[anchor:])
            if sm:
                stem = sm.group(1).strip()
        if len(stem) < 15 or not COMMAND.search(stem):
            stem = ""

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
    bad = []
    if len(out) != 76:
        bad.append(f"blocks: {len(out)} (expected 76)")
    if n_opt != len(out):
        bad.append(f"{len(out) - n_opt} block(s) missing an option")
    if n_ao4 != len(out):
        bad.append(f"{len(out) - n_ao4} block(s) with no AO4 content")
    print()
    print("RESULT:", "OK — 76 nine-mark blocks, all with both options and AO4 content."
          if not bad else "FAIL — " + "; ".join(bad))
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())
