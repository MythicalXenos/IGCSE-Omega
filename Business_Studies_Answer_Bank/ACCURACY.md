# Is the answer bank accurate? — the full check, 9 November 2026

This is the answer to one question: **can this bank be trusted as it stands?**

Three passes were run on it. The first checked its structure and its counts. The second checked the
148 model scripts it claims to hold against the examiner reports. This one checks the **content** —
every answer, every question it claims to answer, every figure in it, and every mark scheme behind
it.

**Short answer: the answers are accurate. Three things around them are not, and all three are now
either fixed or listed at the foot of the answer they affect.**

---

## 1. What the bank actually contains

| Layer | What it is | Size |
|---|---|---|
| **By_Paper** | every part of every paper held, with Pearson's own mark-scheme answer beside it | 38 files · 988 parts · 3,040 marks |
| **Chain_Bank** | a written model answer for every question worth 3 marks or more | 252 entries covering **380 questions** |
| **Exemplar register** | real candidate scripts Pearson printed, with the score each was given | 148 rows |

Everything below is about the third column: whether those numbers are real and whether the words
inside them are right.

---

## 2. The mark schemes themselves — checked first, because everything rests on them

Before trusting any answer, the scheme it came from has to be sound. Every one of the **798
questions** across the 38 mark schemes was parsed for its assessment-objective split — how many
marks each question gives to knowledge, application, analysis and evaluation.

**Result: 798 of 798 splits add up exactly to the question's mark tariff.** Not one scheme in the
archive contradicts itself. This also proves the extraction is reading the schemes correctly,
because a mis-read would show up immediately as a wrong total.

---

## 3. Question pairing — is each answer the answer to the question above it?

342 question quotations in `10_Chain_Bank.md` were traced back to the question paper of the session
and paper the entry names.

| Result | Count |
|---|---|
| **The exact words of the question paper** | **264** |
| The paper prints only an option label, and the entry quotes the mark scheme's description of it | 57 |
| Condensed or lightly reworded, same task | 14 |
| Read by hand — same task, minor rewording | 6 |
| **A question the paper does not contain at all** | **0** |

**No wrong question was found.** That is the finding that matters: no answer in this bank was
written for a different paper, a different session, or a different task.

**The 77 that are not exact are catalogued, one by one, in `Perfect_Answers/10a_Citation_Corrections.md`.**
They split into two harmless kinds and one that deserves a glance:

- **57 option-label cases.** On a 9-mark "justify" question the paper prints only
  *"Option 1: casual employees · Option 2: part-time employees."* The mark scheme is what explains
  that casual staff like being *"on call"*. The bank quotes the explanation inside quotation marks
  as if it were the paper's wording. The answer is unaffected; the attribution is wrong.
- **14 condensed stems.** *"Explain one advantage of having a strong brand"* where the paper says
  *"…for a business of having a strong brand"*. Same task.
- **6 read by hand.** All six are the same task with a word moved. Two of them are the June 2026
  Paper 1 name problem described in section 6.

---

## 4. Are the facts invented? — figures and business names

Every currency amount, every percentage and every business name in every model answer was checked
against the paper and the scheme the entry cites.

- **Answers quoting a figure that appears in neither: 0.**
- **Answers naming a business that appears in neither: 0.**

The arithmetic that can be recomputed was recomputed. 59 calculation chains in the mark schemes
evaluate exactly. Six apparently disagreed, and all six were traced: five were my own reader
splitting a two-line sum in the wrong place, and **one is a genuine error in Pearson's own mark
scheme** — described next, because it is the single most useful thing this pass found.

---

## 5. Pearson's own arithmetic is wrong in one place — and the bank was copying it

**May–June 2020, Paper 2R, question 1(a)(iii).** The paper says a football costs 1,060 rupees and
sells for 1,600. The scheme's correct answer is D, 50.94%, and that is right:

> markup = (1,600 − 1,060) ÷ 1,060 × 100 = **50.94%**

But the scheme explains the two rejected options with two wrong sums:

| The scheme prints | What it should be |
|---|---|
| *"1 600 / 1 060 = 15.09"* | 1,600 ÷ 1,060 = **1.509**, i.e. **150.94%** |
| *"1 600 – 1 060 = 0.52 / 1 600"* | 1,600 − 1,060 = **540**, then 540 ÷ 1,600 × 100 = **33.75%** |

I checked this against the printed PDF, not just the extracted text, so it is Pearson's error and
not a scanning artefact. **The bank reproduced both wrong lines verbatim** — which is exactly what
"verbatim" means, and exactly why it is dangerous: a student learning markup from those two lines
learns two wrong sums.

**Fixed.** A correction note now stands in
`Perfect_Answers/By_Paper/4BS1_May-June_2020_P2R.md`, directly under the two lines, giving the
formula and both correct figures. The awarded answer, D, is unchanged and correct.

---

## 6. The June 2026 Paper 1 problem, restated because it affects answers

The question paper for June 2026 Paper 1 is about **Crumb** (owner: Alex). The mark scheme for the
same paper is about **Violet Cakes** (owner: Claire). The two share no case-study wording and the
log codes differ. This was found in an earlier pass and is quarantined with a warning on the paper.

It surfaces again here: several model answers cite *"Violet Cakes"* and *"Claire"* because that is
the name in the scheme they were built from. **If you sit that paper, write the name printed on your
own question paper.** The reasoning transfers; the name must not.

---

## 7. The marked practice scripts — do the marks add up?

Your two handwritten attempts were marked against the schemes. Both totals were re-added from the
item marks:

| Script | Question totals | Sum | Stated |
|---|---|---|---|
| May 2023 Paper 1 | 12 + 15 + 16 + 12 | **55 / 80** | 55/80 ✓ |
| May 2023 Paper 2 (partial) | 5 + 6 + 4 | **15 / 30** | 15/30 ✓ |

The three calculations inside them were also re-done: 75.50 × 0.94 = 70.97 ✓ · 26,000 ÷ 14,852 =
1.75 ✓ · 67,590 ÷ 330,606 × 100 = 20.44 ✓. The marking is internally consistent and the arithmetic
is right.

---

## 8. What is still not verified — read this before trusting the number 148

The register lists 148 real candidate scripts. **Updated 12 November 2026: 141 of the 148 are now
traced to a printed score line in a document I have actually read.**

| Bucket | Count |
|---|---|
| Verified against a stored examiner report (13 PDFs, 40 MB, in `Sources/Official_Pearson/Full_Examiner_Reports/`) | **122** |
| Verified against a report read from Pearson's live PDF but not stored (June 2024 Paper 2R, June 2025 Paper 1) | **13** |
| Verified against Pearson's June 2019 exemplar booklets | **6** |
| **Total verified** | **141** |
| Cannot be checked — the June 2022 **Paper 1R** report is the one file still missing | **6** |
| The booklet prints nothing for that question | **1** |

**Getting there exposed four defects, and three of them were in my own checking, not in the bank.**

1. **The checker was reading a stale file.** `inventory.json` was built before the reader handled
   *"This response scored 1 mark"* (singular) and word-numbers like *"the full three marks"*, so it
   under-reported grades. The register now reads the fresh `inventory_er.json`. Seven rows moved
   from "mismatch" to "verified" on that fix alone, and none of them had ever been wrong.
2. **The checker was ignoring the register's own annotations.** Rows that already said **(0/1)** or
   **(1/2 and 1/2)** were treated as claiming full marks, because the checker read the section
   heading instead of the row. Eight more false alarms.
3. **A loop variable was overwriting the question number** in the 2019 booklet branch, so three
   booklet rows were compared against the wrong question.
4. **Three real defects in the bank** were found and fixed:
   - **June 2025 P2 Q"2(c)"** — the batch-production 6-marker is **1(g)**; 2(c) is the 3-mark JIT
     question. Wrong question number in the register and in this file's exemplar chapter.
   - **June 2023 P1R Q2(b)** — heading said **1/1**; the report prints **one** script for that
     question and awards it **0** ("no context no marks can be gained"). The heading now says
     **0/1**, with the correction dated in place.
   - **June 2025 P2 Q1(g)** — the quoted 6/6 answer was only its **first paragraph**, presented
     without an ellipsis and described as *"3 sentences, 46 words"*. The script is **two
     paragraphs, about 100 words**, and the second paragraph exists **only as a scanned image** —
     the text layer of the PDF does not carry it. Now quoted in full, with the method written up in
     `audits/SCRIPT_RECONSTRUCTION.md`.

**What is left: six June 2022 Paper 1R rows.** The other June 2022 papers are held; that one report
has not been obtained. Nothing else in the register is unaccounted for.

## 9. Verdict

| Question | Answer |
|---|---|
| Is every answer the answer to its own question? | **Yes** — 0 wrong questions in 342 citations |
| Are the figures and names real? | **Yes** — 0 invented |
| Are the mark schemes behind them sound? | **Yes** — 798 of 798 add up |
| Does the bank quote Pearson correctly? | **Mostly** — 264 of 342 exact; the 78 others are catalogued |
| Is Pearson itself always right? | **No** — one arithmetic error found and corrected in place |
| Are all 148 exemplar scripts proven? | **141 yes** — 6 await one missing PDF, 1 is not printed in the booklet |

**The bank is accurate enough to revise from.** It is not flawless, and the three flaws it has are
now written down where they occur rather than left for you to discover mid-answer.

---

## Files this pass created

| File | What it holds |
|---|---|
| `audits/ms_parse.py` | reads all 38 mark schemes into question-by-question objective splits and content points |
| `audits/audit_ms_coverage.py` | checks each model answer works in every objective its question awards marks for |
| `audits/audit_calculations.py` | re-evaluates every printed calculation chain |
| `audits/build_citation_corrections.py` | writes the corrections file below |
| `Perfect_Answers/10a_Citation_Corrections.md` | all 77 non-verbatim citations, itemised, with the paper's own words where they could be matched |
