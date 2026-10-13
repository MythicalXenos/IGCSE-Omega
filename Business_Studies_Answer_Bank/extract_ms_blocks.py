#!/usr/bin/env python3
"""Dump VERBATIM question blocks from the 4BS1 mark schemes, by tariff.

WHY THIS EXISTS
---------------
Every Layer C batch needs the mark scheme's own wording for a whole tier --
indicative content, the "Award 1 mark for ..." topic phrase, the AO bullets and
the NB notes. Doing that with grep does not work: the PDF text layer breaks
terms across lines ("test marke ting", "public rela tions"), and the May-June
2021 files fragment characters ("A0 1 - 3 mark s"). Two batches were built off
throwaway heredocs, and a sandbox re-seed would have lost the extractor.

USAGE
-----
    python3 extract_ms_blocks.py 6            # 6-mark Analyse  -> layer_c_6mark_blocks.txt
    python3 extract_ms_blocks.py 9            # 9-mark Justify
    python3 extract_ms_blocks.py 12           # 12-mark Evaluate
    python3 extract_ms_blocks.py 3            # 3-mark Explain
    python3 extract_ms_blocks.py 6 --show 4   # header only, print blocks 5-8

RUN FROM Business_Studies_Answer_Bank/.

HOW IT FINDS A BLOCK
--------------------
It reuses the validated machinery from build_layer_c_tariffs.py: parts are
located from their AO allocations, never from a question-paper text dump. A
block runs from its part label to the start of the next part, so the text
between them -- all the indicative content -- comes out intact.
"""
import argparse
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from build_layer_c_tariffs import (ARCHIVE, AO, AO_GROUP, LBL,  # noqa: E402
                                   ROUTE_B_WINDOW, SKELETON, repair)

LABELS = {3: ["1(f)", "2(c)", "2(d)", "2(e)"],
          6: ["1(g)", "3(d)", "4(b)"],
          9: ["2(f)", "3(e)"],
          12: ["4(c)"]}


def blocks_for(pdf: pathlib.Path, tier: int) -> list[tuple[str, str]]:
    import pypdf
    raw = repair(re.sub(r"\s+", " ", "".join(
        (p.extract_text() or "") for p in pypdf.PdfReader(str(pdf)).pages)))
    session = pdf.parent.name.replace("_", " ")
    paper = re.search(r"(P\dR?)_MS", pdf.name).group(1)

    # EVERY part label carrying an AO allocation, in document order -- whatever
    # its tier. Blocks are cut at the next part of ANY tier, not the next part of
    # the SAME tier: cutting on the same tier alone runs 1(g) all the way through
    # question 2 and yields a 5 KB block instead of the 600 characters wanted.
    spans = []
    for m in AO_GROUP.finditer(raw):
        total = sum(int(x[1]) for x in AO.findall(m.group(0)))
        start = max(0, m.start() - ROUTE_B_WINDOW)
        window = raw[start:m.start()]
        labs = list(LBL.finditer(window))
        if not labs:
            continue
        key = f"{labs[-1].group(1)}({labs[-1].group(2)})" + (
            f"({labs[-1].group(3)})" if labs[-1].group(3) else "")
        if key in SKELETON:
            spans.append((start + labs[-1].start(), key, total))
    spans.sort()

    seen, out = set(), []
    for i, (pos, key, total) in enumerate(spans):
        if key in seen or total != tier:
            continue                      # first printing of a part wins
        seen.add(key)
        end = spans[i + 1][0] if i + 1 < len(spans) else len(raw)
        # Pull the block's OWN question stem in from the front. In the mark
        # scheme table the stem sits immediately before the part label, so
        # cutting at the label alone leaves every question text stranded at the
        # tail of the PREVIOUS block -- and the question wording is exactly what
        # an entry needs. Back up to the nearest "Question Number" heading.
        head = pos
        back = raw[max(0, pos - 600):pos]
        for marker in ("Question Number", "Indicative content Mark"):
            cut = back.rfind(marker)
            if cut != -1:
                head = min(head, max(0, pos - 600) + cut)
        body = raw[head:end].strip()
        # The tail is the NEXT question's stem, because that stem sits between
        # this block's content and the next part label. Drop it -- the next
        # block carries it as its own head, so keeping it here just duplicates it.
        tail = body.rfind("Question Number")
        if tail > len(body) - 200:
            body = body[:tail].strip()
        out.append((f"{session} | {paper} | {key}", body))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("tier", type=int, choices=[3, 6, 9, 12])
    ap.add_argument("--show", type=int, default=0,
                    help="print only the Nth block (0 = write the whole file)")
    args = ap.parse_args()

    rows = []
    for pdf in sorted(ARCHIVE.glob("*/4BS1_*_MS.pdf")):
        rows += blocks_for(pdf, args.tier)

    expected = len(LABELS[args.tier]) * 38
    flag = "OK" if len(rows) == expected else f"*** EXPECTED {expected} ***"
    print(f"{args.tier}-mark blocks: {len(rows)}   {flag}")

    if args.show:
        head, body = rows[args.show - 1]
        print(f"\n===== {head} =====\n{body}")
        return 0

    out = HERE / f"layer_c_{args.tier}mark_blocks.txt"
    with out.open("w", encoding="utf-8") as fh:
        fh.write(f"# {args.tier}-MARK QUESTION BLOCKS, VERBATIM FROM THE 4BS1 MARK SCHEMES\n")
        fh.write(f"# {len(rows)} blocks. Regenerate: python3 extract_ms_blocks.py {args.tier}\n")
        fh.write("# Each block runs from its part label to the start of the next part.\n\n")
        for head, body in rows:
            fh.write(f"\n{'=' * 78}\n=== {head}\n{'=' * 78}\n{body}\n")
    print(f"wrote {out.name}  ({out.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
