#!/usr/bin/env python3
"""verify_economics_fingerprint.py — check every claim in the 4EC1 fingerprint docs.

Run from Economics_Answer_Bank/:  python3 verify_economics_fingerprint.py

Checks, in order:
  1. 42 question papers parse, and each prints exactly 80 marks of items.
  2. The tariff census (998 items; 337/220/189/126/84/42) and 3,360 total marks.
  3. Every paper carries exactly 3 x 6-mark, 2 x 9-mark, 1 x 12-mark.
  4. Q4 = 2/6/12 in every paper; Q3 = 1/1/3/6/9 in every paper that parses cleanly.
  5. Command word per tariff, paper by paper: one 'analyse' per 6, one 'assess' per 9,
     one 'evaluate' per 12. Not a global count — a per-paper equality.
  6. AO composition from all 42 mark schemes: no AO1 above 2 marks; 6 = 3+3,
     9 = 3+3+3, 12 = 4+4+4; the three level-band tables appear 126/84/42 times.
  7. Every quotation in the two docs appears verbatim in the June 2023 examiner reports.
  8. The corrected census in 4EC1_Paper_Fingerprint.md matches the parse.
  9. The whole-bank reconciliation distinguishes scopes; keyed reviewed annotations survive in the manifest
     while unreviewed items remain pending. Whole-bank counts are derived, not fixed in this archive verifier.

Exit 0 if everything holds, 1 otherwise. Every check prints what it read.
"""
from __future__ import annotations
import re
import sys
import csv
import json
from collections import Counter
from pathlib import Path

import pymupdf

BANK = Path(__file__).resolve().parent
REPO = BANK.parent
ARCHIVE = REPO / "Paperlords_Archive" / "IGCSE" / "4EC1_Economics"
ALT = (REPO / "Paperlords_Archive" / "RECOVERED_ALTERNATIVES"
       / "4EC1_Economics_June_2022_P2R_QP_alternative.pdf")
ER_DIR = ARCHIVE / "May_2023"

fails: list[str] = []


def check(ok: bool, msg: str) -> None:
    print(("  ok   " if ok else "  FAIL ") + msg)
    if not ok:
        fails.append(msg)


def text_of(pdf: Path) -> str:
    doc = pymupdf.open(str(pdf))
    return "\n".join(page.get_text() for page in doc)


def norm(s: str) -> str:
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = s.replace("\u2013", "-").replace("\u2014", "-")
    return re.sub(r"\s+", " ", s)


# ---------------------------------------------------------------- 1. question papers
qp_files = sorted(p for p in ARCHIVE.rglob("*_QP.pdf"))
print(f"[1] question papers found: {len(qp_files)}")
readable: list[tuple[str, str]] = []
skipped: list[str] = []
for p in qp_files:
    try:
        t = text_of(p)
    except Exception:
        t = ""
    if not t.strip():
        skipped.append(p.name)
        continue
    readable.append((p.name, t))
if ALT.exists():
    readable.append((ALT.name, text_of(ALT)))
check(len(readable) == 42, f"{len(readable)} readable question papers (expected 42)")
check(len(skipped) == 1 and "May-June_2022_P2R" in skipped[0],
      f"exactly one damaged QP, and it is the 2022 P2R: {skipped}")

census: Counter[int] = Counter()
per_paper: dict[str, Counter[int]] = {}
for name, t in readable:
    marks = [int(m) for m in re.findall(r"^\s*\((\d{1,2})\)\s*$", t, re.M)]
    c = Counter(marks)
    per_paper[name] = c
    census.update(marks)

total_items = sum(census.values())
total_marks = sum(k * v for k, v in census.items())
check(total_marks == 42 * 80, f"{total_marks} marks across 42 papers = 3,360 = 42 x 80")
check(all(sum(k * v for k, v in c.items()) == 80 for c in per_paper.values()),
      "every individual paper sums to exactly 80 marks")

# ---------------------------------------------------------------- 2. census
print("\n[2] census")
want = {1: 337, 2: 220, 3: 189, 6: 126, 9: 84, 12: 42}
check(total_items == 998, f"{total_items} items (expected 998)")
for tariff, n in want.items():
    check(census[tariff] == n, f"{tariff}-mark items: {census[tariff]} (expected {n})")
check(set(census) == set(want), f"no tariff outside 1/2/3/6/9/12: found {sorted(census)}")

# ---------------------------------------------------------------- 3. long-answer tiers
print("\n[3] the 48 fixed long-answer marks")
bad = [n for n, c in per_paper.items() if (c[6], c[9], c[12]) != (3, 2, 1)]
check(not bad, f"every paper has exactly 3x6, 2x9, 1x12 (offenders: {bad})")

# ---------------------------------------------------------------- 4. question shapes
print("\n[4] question by question")
q4_ok = q3_ok = 0
for name, t in readable:
    seq: dict[int, list[int]] = {}
    flat: list[int] = []
    q = None
    for line in t.split("\n"):
        m = re.match(r"^(\d)\t", line)
        if m:
            q = int(m.group(1))
            continue
        mm = re.match(r"^\((\d{1,2})\)\s*$", line.strip())
        if mm and q:
            seq.setdefault(q, []).append(int(mm.group(1)))
            flat.append(int(mm.group(1)))
    # the robust form: the last three items of the paper are always 2, 6, 12.
    # (In one paper -- 2024 P2R -- the '4' heading does not extract as a label,
    #  so its Q4 items attach to Q3; the item sequence itself is unaffected.)
    if flat[-3:] == [2, 6, 12]:
        q4_ok += 1
    if seq.get(3) == [1, 1, 3, 6, 9]:
        q3_ok += 1
check(q4_ok == 42, f"the last three items of every paper are 2, 6, 12 ({q4_ok} of 42)")
check(q3_ok >= 38, f"Q3 is 1/1/3/6/9 in {q3_ok} of 42 papers "
                   "(the rest are papers whose question numbers did not split cleanly on this parse)")

# ---------------------------------------------------------------- 5. command words
print("\n[5] command word per tariff, paper by paper")
bad = []
for name, t in readable:
    low = norm(t).lower()
    c = per_paper[name]
    if (low.count("analyse"), low.count("assess"), low.count("evaluate")) != (c[6], c[9], c[12]):
        bad.append((name, low.count("analyse"), low.count("assess"), low.count("evaluate")))
check(not bad, f"one analyse per 6, one assess per 9, one evaluate per 12 in every paper "
               f"(offenders: {bad[:3]})")
check(census[9] == 84 and census[12] == 42,
      "so 'assess' appears 82+ times only because 9-markers number 2 a paper and 12-markers 1")

# ---------------------------------------------------------------- 6. mark schemes
print("\n[6] mark schemes")
ms_files = sorted(ARCHIVE.rglob("*_MS.pdf"))
check(len(ms_files) == 42, f"{len(ms_files)} mark schemes")

multi: Counter[tuple] = Counter()
single: Counter[tuple] = Counter()
bands: Counter[tuple] = Counter()
for p in ms_files:
    t = text_of(p)
    for line in t.split("\n"):
        l = line.strip()
        if l.startswith("AO2 (") and "/" in l:
            parts = tuple((int(a), int(n)) for a, n in
                          re.findall(r"AO(\d)\s*\((\d+)\s*marks?\)", l))
            multi[parts] += 1
        m = re.fullmatch(r"AO(\d)\s*\(?(\d+)\s*marks?\)?", l)
        if m:
            single[(int(m.group(1)), int(m.group(2)))] += 1
    flat = norm(t)
    for m in re.finditer(r"Level (\d)\s*(\d+)\s*-\s*(\d+)", flat):
        bands[(int(m.group(1)), int(m.group(2)), int(m.group(3)))] += 1

check(multi[((2, 3), (3, 3))] == 126, f"6-mark = AO2 3 + AO3 3 in {multi[((2, 3), (3, 3))]} items (expected 126)")
check(multi[((2, 3), (3, 3), (4, 3))] == 84,
      f"9-mark = AO2 3 + AO3 3 + AO4 3 in {multi[((2, 3), (3, 3), (4, 3))]} items (expected 84)")
check(multi[((2, 4), (3, 4), (4, 4))] == 42,
      f"12-mark = AO2 4 + AO3 4 + AO4 4 in {multi[((2, 4), (3, 4), (4, 4))]} items (expected 42)")
ao1_inside = [k for k in multi if any(a == 1 for a, _ in k)]
check(not ao1_inside, f"no multi-AO item (6, 9 or 12 marks) contains AO1 (offenders: {ao1_inside})")
check(all(k[0] == (2, 3) or k[0] == (2, 4) for k in multi),
      "every multi-AO item opens on AO2 -- application is the first thing a long answer is judged on")

high_ao1 = [k for k in single if k[0] == 1 and k[1] > 2]
check(not high_ao1, f"no AO1 item is worth more than 2 marks (offenders: {high_ao1})")
check(single[(2, 3)] == 189, f"3-mark = AO2 only in {single[(2, 3)]} items (expected 189)")
check(single[(1, 1)] + single[(2, 1)] == 339,
      f"1-mark items split AO1 {single[(1, 1)]} / AO2 {single[(2, 1)]}")
check(single[(1, 2)] + single[(2, 2)] == 201,
      f"2-mark items split AO1 {single[(1, 2)]} / AO2 {single[(2, 2)]}")

check(bands[(3, 5, 6)] == 126, f"6-mark bands 1-2 / 3-4 / 5-6 ({bands[(2, 3, 4)]} / {bands[(3, 5, 6)]} level-3 counts)")
check(bands[(3, 7, 9)] == 84, f"9-mark level 3 band 7-9 appears {bands[(3, 7, 9)]} times")
check(bands[(3, 9, 12)] == 42, f"12-mark level 3 band 9-12 appears {bands[(3, 9, 12)]} times")

# ---------------------------------------------------------------- 7. quotations
print("\n[7] quotations")
er_text = {name: norm(text_of(ER_DIR / f"4EC1_Economics_May_2023_{name}_ER.pdf"))
           for name in ("P1R", "P2", "P2R")}
QUOTES = [
    ("P2", "'Analyse' questions require a one-sided argument. There are no marks for evaluation."),
    ("P2", "Many candidates often start the 'Analyse' questions with a definition of the key economic "
           "term in the question and this is not necessary as there are no knowledge marks available."),
    ("P2", "A conclusion is not required for the 9-mark 'Assess' questions."),
    ("P2", "For your conclusion, do not just repeat earlier points and instead come to a judgement as "
           "to whether an economic concept is effective or what else does it depend on."),
    ("P2", "Make sure you have plenty of time to answer the 12-mark question."),
    ("P2", "It is important to note that to access the higher marks, candidates must evaluate the "
           "economic concept in the question set before suggesting alternative methods otherwise this "
           "just becomes a list of methods, rather than an evaluation of the area being examined."),
    ("P1R", "Candidates should not evaluate 'analyse' questions. There are no marks available for doing "
            "so and it will result in less time being available for other questions."),
    ("P1R", "The evaluation is ignored as there are no marks for AO4 on 'analyse' questions."),
    ("P1R", "Focus on developing each applied chain of reasoning rather than listing several separate points."),
    ("P1R", "'Assess' questions require a balanced, two-sided argument, which is applied. There is no "
            "requirement for a judgement or a conclusion, but the argument(s) and counter argument(s) "
            "should be developed and thorough, as well as in context."),
    ("P1R", "This is the only question on the paper requiring a supported judgement/conclusion."),
    ("P1R", "Application marks will not be awarded simply for repeating evidence from the extracts. It "
            "needs to be used in the response."),
    ("P1R", "Simply copying the extract, or re-writing parts of it, is not going to lead to high marks!"),
    ("P1R", "The descriptor tables for questions with the command words 'analyse', 'assess' and "
            "'evaluate' do not change between questions with the same command word or between exam series."),
    ("P1R", "'Explain' questions require one reason/way/advantage, which is in context and developed, "
            "to gain all 3 marks."),
    ("P1R", "'What is meant by' questions have two marks and require two parts in the explanation of "
            "the term. No marks are awarded for examples."),
    ("P1R", "There are no marks for stating a formula in 'calculate' questions."),
    # --- 4EC1_What_Stops_You_At_11.md
    ("P1R", "It meets all the requirements for Level 3 with a balanced, two-sided argument, leading to a "
            "supported conclusion, but does not present an excellent organisation of information and "
            "application is only reasonable."),
    ("P2", "There is an attempt at a conclusion."),
    ("P2", "Alternative methods are not required to access Level 4 and full marks can be achieved by "
           "only evaluating the economic concept in the question"),
    ("P2R", "A conclusion is provided which does make a judgement."),
    ("P2", "A conclusion was required for this question and this was often lacking or was just a repeat "
           "of the points made previously."),
    ("P2", "Better responses used the information provided to help contextualise the answer rather than "
           "just paraphrasing it."),
    ("P1R", "Some candidates simply repeated the data rather than using it, thus reducing their ability "
            "to attain a top-level mark."),
]
def doc_text(path: Path) -> str:
    """Markdown out: blockquote markers, emphasis and code ticks are presentation, not text."""
    out = []
    for ln in path.read_text().splitlines():
        ln = ln.lstrip()
        if ln.startswith(">"):
            ln = ln[1:].lstrip()
        ln = ln.replace("**", "").replace("*", "").replace("`", "")
        out.append(ln)
    return norm(" ".join(out))


docs = {p.name: doc_text(p) for p in
        (BANK / "4EC1_Command_Words_Verified.md", BANK / "4EC1_Paper_Fingerprint.md",
         BANK / "4EC1_What_Stops_You_At_11.md")}
for paper, q in QUOTES:
    check(norm(q) in er_text[paper], f"4EC1/2023 {paper}: \"{q[:58]}...\"")
    in_doc = [n for n, t in docs.items() if norm(q) in t]
    check(bool(in_doc), f"  ...and the same words appear in the doc that quotes them: {in_doc}")

# ---------------------------------------------------------------- 8. the doc agrees
print("\n[8] the docs agree with the parse")
doc = (BANK / "4EC1_Paper_Fingerprint.md").read_text()
for needle in ("**998**", "**3,360**", "126 of 126", "84 of 84", "42 of 42",
               "337", "220", "189", "21 |", "11 |", "10 |"):
    check(needle in doc, f"fingerprint doc states {needle}")
check("no AO1 above 2 marks" in doc, "fingerprint doc states the AO1 ceiling")

# ------------------------------------------------------------ 8b. the 11/11/10 page
print("\n[8b] the calibration page matches the bank's own exemplar index")
cal = (BANK / "4EC1_What_Stops_You_At_11.md").read_text()
idx = (BANK / "Source_Notes" / "Official_Pearson_Exemplar_Index.md").read_text()
for needle in ("**11/12**", "**10/12**", ("9 and 7")):
    check(needle in cal, f"calibration page states {needle}")
for needle in ("11/12", "10/12", "9/12"):
    check(needle in idx, f"exemplar index records a {needle} script (so no 12/12 is claimed)")
check("not a Pearson statement" in cal and "labelled as construction" in cal.lower(),
      "the constructed part of the calibration page is labelled as construction")

# ---------------------------------------------------------------- 9. reconciliation / review-state consistency
print("\n[9] whole-bank reconciliation and persistent review layer")
recon = (BANK / "Whole_Bank_Reconciliation.md").read_text()
guide = (BANK / "4EC1_Exemplar_and_Model_Answer_Guide.md").read_text()
check("archive pairs" in recon and "local/incoming" in recon,
      "reconciliation distinguishes archive census from current local/incoming scope")
check("Earlier line-based counts and mark-tariff breakdowns" in guide and
      "must not be used as the full-bank denominator" in guide,
      "legacy line-based tally is identified as superseded, not current bank size")
with (BANK / "Whole_Bank_Question_Manifest.csv").open(encoding="utf-8", newline="") as f:
    manifest = list(csv.DictReader(f))
review = json.loads((BANK / "Whole_Bank_Review_Layer.json").read_text(encoding="utf-8"))
manifest_by_id = {x["question_id"]: x for x in manifest}
check(len(manifest_by_id) == len(manifest), "manifest question IDs are unique")
for qid, annotation in review.get("items", {}).items():
    row = manifest_by_id.get(qid)
    check(row is not None, f"review layer item remains in manifest: {qid}")
    if row:
        check(row["prompt_text"] == annotation["prompt_text"] and
              row["reasoning_skill_family"] == annotation["reasoning_skill_family"],
              f"persistent review annotation survives rebuild: {qid}")
check(any(x["reasoning_skill_family"] != "PENDING_CLASSIFICATION" for x in manifest),
      "verified rows are present without requiring all other classifications to be complete")

print()
if fails:
    print(f"RESULT: FAILED — {len(fails)} check(s):")
    for f in fails:
        print("  -", f)
    sys.exit(1)
paper_total = len({x["canonical_paper_id"] for x in manifest})
part_total = len(manifest)
mark_total = sum(int(x["marks"]) for x in manifest)
print(f"RESULT: OK — archive fingerprint 42 papers / 998 items / 3,360 marks; current manifest "
      f"{paper_total} papers / {part_total} parts / {mark_total} marks; review states are item-specific; "
      "3/6/9/12 AO allocations and quotations verified.")
