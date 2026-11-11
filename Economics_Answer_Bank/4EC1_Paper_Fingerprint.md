# 4EC1 — the paper fingerprint

**What this file is:** an archive-only structural census, measured from every question paper and
mark scheme in the 42-paper Paperlords archive. It does not include the separately supplied January
2023 P1R QP/MS and is not the whole currently available question-bank denominator. The reconciled
local/incoming scope is 43 paper/variant documents, 1,022 parts and 3,440 marks; see
`Whole_Bank_Reconciliation.md` and `Whole_Bank_Question_Manifest.csv`. Nothing in this archive
fingerprint is estimated. Every number below is re-derived by `verify_economics_fingerprint.py`, which
fails if a single paper in the archive stops matching.

**Sources (all in this repository):**

| Source | Count | Path |
|---|---|---|
| Question papers | 42 | `Paperlords_Archive/IGCSE/4EC1_Economics/*/*_QP.pdf` |
| Mark schemes | 42 | `Paperlords_Archive/IGCSE/4EC1_Economics/*/*_MS.pdf` |
| Examiner reports | 3 | `Paperlords_Archive/IGCSE/4EC1_Economics/May_2023/*_ER.pdf` |

**One file is damaged, not missing.** `4EC1_Economics_May-June_2022_P2R_QP.pdf` has a broken object
table (8 readers fail on it: *Object 87 0 not defined*). Two independent recovered copies sit in
`Paperlords_Archive/RECOVERED_ALTERNATIVES/` and `.../Recovered_Alternatives/`; both parse to the same
23 items and 80 marks, so the census below counts that paper from the recovered copy. **This is a
property of the downloaded file, not of Pearson's paper.**

---

## 1. The census

| | Count |
|---|---|
| Papers | **42** (13 sessions × 2 papers, plus R variants) |
| Items | **998** |
| Marks | **3,360** — and that is exactly 42 × 80 |

| Tariff | Items | Marks |
|---|---|---|
| **1** | 337 | 337 |
| **2** | 220 | 440 |
| **3** | 189 | 567 |
| **6** | 126 | 756 |
| **9** | 84 | 756 |
| **12** | 42 | 504 |

**There is no 4-mark, 5-mark, 8-mark or 20-mark item anywhere in 42 papers.** The tariff set is
`1, 2, 3, 6, 9, 12` and nothing else.

---

## 2. The skeleton never moves for the long answers

**Every paper is four questions of 20 marks, 80 marks, 1 hour 30 minutes.**

| Question | Structure | Fixed? |
|---|---|---|
| **Q1** | short items, ending in a **6** | the **6** is fixed; the short items above it are not |
| **Q2** | short items, ending in a **9** | the **9** is fixed |
| **Q3** | `1 · 1 · 3 · 6 · 9` | **fixed in 41 of 42 papers** |
| **Q4** | `2 · 6 · 12` | **fixed in 42 of 42 papers** |

So **3 six-markers, 2 nine-markers, 1 twelve-marker — 48 of the 80 marks — sit in the same place in
every paper ever set.** The remaining 32 marks are made of 1-, 2- and 3-mark items, and only their
mix varies:

| Short-answer shape | Papers | Where |
|---|---|---|
| `7 × 1 · 5 × 2 · 5 × 3` | 21 | **every Paper 2**, and Paper 1 from 2024 |
| `10 × 1 · 5 × 2 · 4 × 3` | 11 | Paper 1, 2019 – May 2023 |
| `8 × 1 · 6 × 2 · 4 × 3` | 10 | Paper 1, 2024 onwards |

**Practical consequence:** in the last 10 minutes you always know what Q4 looks like — a 2-mark
calculation, a 6-mark *Analyse*, a 12-mark *Evaluate*. You never need to spend reading time working
out where the big marks are.

---

## 3. What each mark value is made of — the AO map

Taken from the AO statement printed at the head of every marked item in all 42 mark schemes.

| Tariff | AO composition | Occurrences | Verdict |
|---|---|---|---|
| **1** | AO1 **or** AO2, 1 mark | 272 AO1 · 67 AO2 | knowledge *or* application, examiner's choice |
| **2** | AO1 **or** AO2, 2 marks | 113 AO1 · 88 AO2 | same split |
| **3** | **AO2 only**, 3 marks | 189 of 189 | **never AO1** |
| **6** | **AO2 3 + AO3 3** | 126 of 126 | no AO1, **no AO4** |
| **9** | **AO2 3 + AO3 3 + AO4 3** | 84 of 84 | no AO1 |
| **12** | **AO2 4 + AO3 4 + AO4 4** | 42 of 42 | no AO1 |

**The single most important line in this table: there is no AO1 above 2 marks.** Knowledge is bought
only by 1- and 2-mark items. Everything from 3 marks up is application, analysis and evaluation.

This is the **opposite** of 4BS1 Business, where the 12-marker carries AO1 3 marks and therefore pays
for a definition. In Economics a definition inside a 12-mark answer is worth nothing, and Pearson says
so in the report:

> *"Many candidates often start the 'Analyse' questions with a definition of the key economic term in
> the question and this is not necessary as there are no knowledge marks available."*
> — June 2023, 4EC1/02, Examiner's Report

---

## 4. Two different marking machines inside one paper

| Tariff | How it is marked | Evidence |
|---|---|---|
| **1, 2, 3** | **Point marking.** The scheme prints *"Award 1 mark for identifying… 1 mark for developing… 1 mark for the response being in context"* and lists acceptable answers | 189 three-mark items all AO2; schemes are explicit |
| **6, 9, 12** | **Level of response.** The scheme prints *"Indicative content"* — a bullet list that is **not** a checklist — followed by a three-band descriptor table | 126 + 84 + 42 descriptor tables |

**The level bands, from all 42 schemes:**

| Tariff | Level 1 | Level 2 | Level 3 |
|---|---|---|---|
| **6** | 1–2 | 3–4 | 5–6 |
| **9** | 1–3 | 4–6 | 7–9 |
| **12** | 1–4 | 5–8 | 9–12 |

And the descriptors are **not written per question**:

> *"The descriptor tables for questions with the command words 'analyse', 'assess' and 'evaluate' do
> not change between questions with the same command word or between exam series."*
> — June 2023, 4EC1/01R, Examiner's Report

So there are exactly **three** descriptor tables to learn for the whole qualification, and the
indicative content is illustration, not requirement. A response that hits every bullet but reads as a
list still lands in Level 2 — because Level 3 asks for *"excellent selectivity and organisation"* and
a *"coherent and logical"* chain of reasoning, not for coverage.

---

## 5. Why this changes how you answer

| If you are told… | You now know… | So do… |
|---|---|---|
| *"3 marks, Explain"* | AO2 only, point marked, identify + develop + context | three sentences: the point, the mechanism, the context. **No definition** |
| *"6 marks, Analyse"* | AO2 3 + AO3 3, level marked, **no AO4** | one side only, developed chains. **No conclusion — it earns nothing** |
| *"9 marks, Assess"* | AO2 3 + AO3 3 + AO4 3, level marked | two developed sides applied to the data. **No separate conclusion needed** |
| *"12 marks, Evaluate"* | AO2 4 + AO3 4 + AO4 4 | two sides **and** a supported judgement. Evaluate the policy in the question *before* alternatives |

The examiner reports put the same four rows in their own words — see
`4EC1_Command_Words_Verified.md`, where each statement is quoted and checked against the PDF.

---

## 6. Correction to the legacy inventory

Earlier versions of the guide described a line-based tally of **671 items** (262 / 173 / 98 / 60 / 42 /
36), totaling only 2,072 marks. That tally is not a census. The current workbook independently has
671 question-type rows (P1 225, P1R 128, P2 202, P2R 116); those rows are also incomplete and must not
be confused with the older tariff tally. The complete archive-only QP/MS parse is **998 parts / 3,360
marks across 42 archive pairs**, as measured in §1. The current local/incoming scope adds the January
2023 P1R source and is **1,022 parts / 3,440 marks across 43 papers/variants**. See
`Whole_Bank_Reconciliation.md` for the source reconciliation and the manifest. The `verify_economics_fingerprint.py`
checks the 42-paper archive census, including the invariant that each archive paper totals 80; it does
not verify the extra incoming January 2023 P1R or the whole-bank visual classification.

*This correction does not touch the guide's technique content, its script evidence or its 12-mark
model — those were read by eye and stand or fall on their own quotes.*
