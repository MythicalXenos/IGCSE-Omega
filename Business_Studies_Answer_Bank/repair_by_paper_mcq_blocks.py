#!/usr/bin/env python3
"""Repair the three `By_Paper/` files that disagree with the mark schemes.

Found by `verify_by_paper.py` — the check that compares `By_Paper/` against the
tariff table derived from all 38 mark schemes. Three files, two defects:

**DEFECT 1 — six collapsed MCQ items (May-June 2024 P2 and P2R), content and all.**
The scheme prints the six one-mark multiple-choice items as:

    1 (a) (i)   AO1 - 1 mark ...
    1 (a)
    (ii)
    AO1 - 1 mark ...

— the roman numeral broken onto its own line. The generator matched the marker
but then took **one block per `1 (a)` group**, so it read **six `AO1 - 1 mark`
runs as a single 6-mark item** (`### 1(a)(i) — 6 marks (AO1:1, AO1:1, AO1:1,
AO1:1, AO1:1, AO1:1)`).

**Five items vanished and one was mis-tariffed — and the two errors cancel in
the paper total** (six 1-mark items out, one 6-mark item in). That is why the
file's own 80-mark check passed: **a check that only sums marks cannot see a
six-for-one substitution.** Only the independent item count catches it.

**The content went with them.** On the file as committed, P2 and P2R each held
**one** `The only correct answer is` and **three** distractor lines, where the
mark scheme prints **six** and **eighteen** — so **five MCQs' official answers
were absent from the file while the "6 marks" heading still counted their
marks.** The repair reconstructs all six from the mark-scheme PDFs, pairing each
`Q. No.` stem with the item that FOLLOWS it (the extractor prints the stem after
the answer, so the stem beneath an item belongs to the next one).

**DEFECT 2 — a missing withdrawn item (May-June 2019 P2R).**
`1(a)(iii)` is not a normal question. Pearson's mark scheme prints an erratum
against it: an error in the multiple-choice distractors meant **every candidate
was awarded the mark**. It therefore carries a mark but **no AO label**, and the
generator — which looked for an AO line to know an item had started — walked
past it. That is the paper that sums to **79**.

This script reconstructs both from the mark-scheme PDFs. It is **idempotent**:
if a heading is already split, it reports `already correct` and writes nothing.

Run from Business_Studies_Answer_Bank/:  python3 repair_by_paper_mcq_blocks.py [--check]
"""
import argparse
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
BY_PAPER = HERE / "Perfect_Answers" / "By_Paper"
MS_DIR = HERE.parent / "Paperlords_Archive" / "IGCSE" / "4BS1_Business_Studies" / "May-June_2024"
MS_2019 = (HERE.parent / "Paperlords_Archive" / "IGCSE" / "4BS1_Business_Studies"
           / "May-June_2019" / "4BS1_Business_Studies_May-June_2019_P2R_MS.pdf")

ROMAN = "i{1,3}|iv|v|vi|vii"
# `1 (a) (i)` or `1 (a) \n(ii)` — the numeral may be on its own line
MARK = re.compile(rf"1\s*\(a\)\s*\(?\s*({ROMAN})\s*\)?(?=\s|AO|A[O0])")
STEM = re.compile(r"Q\.\s*No\.\s*(.+?)\s*Answer\s*Mark", re.S)
AOLINE = re.compile(r"A[O0]\s*[1-4]\s*[-=\u2013\u2014]\s*1\s*marks?", re.I)
DISTRACTOR = re.compile(r"\s(?=[A-D]\s*[\u2013-]\s*(?:is )?not the correct)")


def ms_text(path: pathlib.Path) -> str:
    import pypdf
    raw = "".join((p.extract_text() or "") for p in pypdf.PdfReader(str(path)).pages)
    return raw.replace("\u00a0", " ")


def tidy(s: str) -> str:
    """One line per thought: the answer sentence, then one line per distractor."""
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"\s*\(\d+\)\s*$", "", s).strip()          # trailing (1)
    parts = [p.strip() for p in DISTRACTOR.split(s) if p.strip()]
    return "\n\n".join(parts)


def split_mcq_region(text: str, start: int, end: int):
    """Return [(roman, stem, body)] for the six MCQ items in a region."""
    region = text[start:end]
    marks = list(MARK.finditer(region))
    stems = list(STEM.finditer(region))
    out = []
    for k, m in enumerate(marks):
        stop = marks[k + 1].start() if k + 1 < len(marks) else len(region)
        body = region[m.end():stop]
        # the AO label opens the item; the stem that FOLLOWS it belongs to the
        # NEXT item, because the extractor prints the stem after the answer
        lead = AOLINE.search(body)
        if lead:
            body = body[lead.end():]
        body = re.split(r"Q\.\s*No\.", body)[0]
        stem = ""
        prior = [s for s in stems if s.start() < m.start()]
        if prior:
            stem = re.sub(r"\s+", " ", prior[-1].group(1)).strip()
        out.append((m.group(1), stem, tidy(body)))
    return out


def render(tag: str, items) -> str:
    blocks = []
    for roman, stem, body in items:
        head = f"### `1(a)({roman})` — 1 mark (AO1:1)\n\n"
        q = f"**Question:** {stem}\n\n" if stem else ""
        blocks.append(head + q + "**Official mark scheme answer:**\n\n"
                      "AO1 - 1 mark\n\n" + body + "\n")
    return "\n".join(blocks)


def repair_2024(tag: str, text_by_file: dict, check: bool) -> bool:
    md = BY_PAPER / f"4BS1_May-June_2024_{tag}.md"
    s = md.read_text(encoding="utf-8")
    if "six collapsed" in s or not re.search(r"1\(a\)\(i\)` — 6 marks", s):
        if not re.search(r"### `1\(a\)\(i\)` — 6 marks", s):
            print(f"  {md.name:<34} already correct — nothing to do")
            return False
    raw = text_by_file[tag]
    start = raw.rfind("Q. No.", 0, raw.find("1 (a) (i)"))
    end = raw.find("1 (b)")
    items = split_mcq_region(raw, start, end)
    assert [r for r, _s, _b in items][:6] == ["i", "ii", "iii", "iv", "v", "vi"], items
    new_block = render(tag, items)
    old = re.search(r"### `1\(a\)\(i\)` — 6 marks.*?(?=### `1\(b\)`)", s, re.S)
    assert old, md.name
    s2 = s[:old.start()] + new_block + "\n" + s[old.end():]
    s2 = re.sub(r"\*\*Items:\*\*\s*\d+", f"**Items:** {len(re.findall(r'^### ', s2, re.M))}", s2)
    if check:
        print(f"  {md.name:<34} WOULD repair — {len(items)} MCQ items recovered")
        return True
    md.write_text(s2, encoding="utf-8")
    print(f"  {md.name:<34} repaired — {len(items)} MCQ items recovered, "
          f"{len(re.findall(r'^### ', s2, re.M))} items now")
    return True


def repair_2019p2r(text: str, check: bool) -> bool:
    md = BY_PAPER / "4BS1_May-June_2019_P2R.md"
    s = md.read_text(encoding="utf-8")
    if "1(a)(iii)`" in s:
        print(f"  {md.name:<34} already correct — nothing to do")
        return False
    raw = ms_text(MS_2019)
    m = re.search(r"1 \(a\) \(iii\)\s*(.+?)\(1\)", raw, re.S)
    assert m, "1(a)(iii) erratum not found in the 2019 P2R mark scheme"
    errata = re.sub(r"\s+", " ", m.group(1)).strip()
    block = (
        "### `1(a)(iii)` — 1 mark (no AO — see note)\n\n"
        "**Question:** *withdrawn item — see the mark scheme note*\n\n"
        "**Official mark scheme answer (verbatim, an ERRATUM not an answer):**\n\n"
        f"{errata}\n\n"
        "> ### ⚠️ WHY THIS ITEM HAS NO AO LABEL\n"
        "> **It carries a mark and tests nothing.** Pearson withdrew it after an error "
        "in the multiple-choice distractors and awarded the mark to every candidate.\n"
        ">\n"
        "> **This is the reason the paper sums to 79 on every arithmetic check that "
        "reads AO labels** — a parser looking for `AO1 - 1 mark` to know an item has "
        "begun walks straight past it. **The paper is 80 marks; the missing mark was "
        "ours.** The same fact is recorded as an explicit override in "
        "`build_layer_c_tariffs.py`, and it is the one paper in the archive whose "
        "mark total does not reconcile without it.\n"
    )
    anchor = "### `1(a)(iv)`"
    assert s.count(anchor) == 1, "anchor for the insertion is ambiguous"
    s2 = s.replace(anchor, block + "\n" + anchor, 1)
    s2 = re.sub(r"\*\*Items:\*\*\s*\d+", f"**Items:** {len(re.findall(r'^### ', s2, re.M))}", s2)
    s2 = re.sub(r"\*\*Marks in this paper:\*\*\s*\d+", "**Marks in this paper:** 80", s2)
    if check:
        print(f"  {md.name:<34} WOULD insert the 1(a)(iii) erratum")
        return True
    md.write_text(s2, encoding="utf-8")
    print(f"  {md.name:<34} repaired — 1(a)(iii) erratum inserted, "
          f"{len(re.findall(r'^### ', s2, re.M))} items now")
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="report only; write nothing")
    args = ap.parse_args()
    print("By_Paper repairs" + (" (check only)" if args.check else ""))
    print("-" * 74)
    changed = 0
    text2024 = {t: ms_text(MS_DIR / f"4BS1_Business_Studies_May-June_2024_{t}_MS.pdf")
                for t in ("P2", "P2R")}
    for tag in ("P2", "P2R"):
        changed += repair_2024(tag, text2024, args.check)
    changed += repair_2019p2r(None, args.check)
    print("-" * 74)
    print(f"files {'that would change' if args.check else 'changed'}: {changed}")
    if not args.check and changed:
        print("\nNow re-run:  python3 verify_by_paper.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
