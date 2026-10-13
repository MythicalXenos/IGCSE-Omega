# 04 — TYPE COVERAGE AND GAPS

An honest account of what this bank contains and what it does not. Read this before trusting the bank to be complete.

---

## The full taxonomy

Automatically detected across **38 archived 4BS1 question papers** (May/June 2019 – June 2026, including R variants):

| Marks | Detected type | Instances | % of 696 |
|---|---|---|---|
| 1 | MCQ / selection | 147 | 21.1% |
| 1 | Define | 91 | 13.1% |
| 1 | State / identify | 82 | 11.8% |
| 1 | Other one-mark item *(check prompt)* | 7 | 1.0% |
| 1 | Numerical / MCQ calculation | 1 | 0.1% |
| 2 | Calculate | 72 | 10.3% |
| 2 | Outline one | 30 | 4.3% |
| 2 | State / identify | 4 | 0.6% |
| 3 | **Explain one** | **152** | **40.0%** of governed |
| 6 | **Analyse / assess** | **114** | **30.0%** of governed |
| 9 | **Justify a choice** | **76** | **20.0%** of governed |
| 12 | **Evaluate** | **38** | **10.0%** of governed |
| | **GOVERNED TOTAL** | **380** | **across all 38 papers** |

⚠️ **These are NOT the CSV's numbers.** Read them from the mark schemes with
`python3 ../build_layer_c_tariffs.py`, which validates every paper against the
80-mark total — **38 of 38 papers sum to exactly 80.**

The CSV in the row below it reports **111 / 86 / 48 / 17** for the same four
tariffs. Every one is low, the 12-mark worst of all, because the CSV is built
from *question-paper text extraction* and that under-detects non-constantly.
**111 / 86 / 48 / 17 is WITHDRAWN — 152 / 114 / 76 / 38 replaces it.** The
696-row item count itself is still useful for the 1- and 2-mark items, which is
what the other rows of that table describe; rebuild those with
`python3 ../build_question_inventory.py`.

### Why the four bold rows are the whole game

The 3, 6, 9 and 12-mark questions are **380 of the 696 items** — and they carry **60 of the 80 marks on every paper (75%)**, because the 1-mark MCQ and define items are single marks while a single evaluate is worth twelve.

On a Paper 1 (80 marks total), the tariff breakdown is roughly:

| Tariff | Items per paper | Marks per paper |
|---|---|---|
| 1- and 2-mark items | 20 | **20** |
| 3-mark Explain | **4** | **12** |
| 6-mark Analyse | **3** | **18** |
| 9-mark Justify | **2** | **18** |
| 12-mark Evaluate | **1** | **12** |
| | **30 items** | **80 marks** |

**Identical on all 38 papers.** The skeleton never varies: **1(f) = 3 · 1(g) = 6 · 2(c)(d)(e) = 3 · 2(f) = 9 · 3(d) = 6 · 3(e) = 9 · 4(b) = 6 · 4(c) = 12** — that is 60 marks — and the remaining **20 marks** are the 1- and 2-mark items above them.

**So the four governed tariffs are worth 60 of the 80 marks (75%), not "54".** This bank's verified exemplars concentrate exactly there, which is the correct allocation of effort. Reproduce the skeleton with `python3 ../build_layer_c_tariffs.py`.

---

## Coverage status by type

### ✅ Fully covered — verified full-mark exemplar available

| Tariff | Type | Verified exemplar | Score |
|---|---|---|---|
| 3 | Explain one | June 2019 P1 Q1(f) — increase gross profit margin | **3/3** |
| 3 | Explain one | June 2019 P1 Q2(d) — above-the-line promotion | **3/3** |
| 6 | Analyse | June 2019 P1 Q1(g) — satisfying customer needs | **6/6** |
| 6 | Analyse | June 2019 P1 Q4(b) — usefulness of profitability ratios | **6/6** |
| 6 | Analyse | June 2019 P1R Q1(g) — customer satisfaction | **6/6** |
| 9 | Justify | June 2019 P1 Q3(e) — source of finance | **9/9** |
| 12 | Evaluate | June 2024 P1 Q4(c) — importance of marketing to PPS | **12/12** |

*(The three 6-mark full-markers were confirmed by the source notes and examiners' comments; the June 2019 P1R 6/6 is confirmed as "Level 3 – 6 marks" in the same booklet.)*

**All four high-value tariffs have at least one verified full-mark exemplar, and all four are transcribed in full with examiner commentary in `02_Verified_Exemplars.md`.**

### ⚠️ Partially covered — real scripts, but below full marks

These are genuinely useful calibration (and are quoted in `03_Calibration_Below_Full_Marks.md`), but **they are not perfect answers and must not be presented as such**:

| Tariff | Question | Score(s) |
|---|---|---|
| 3 | June 2019 P1 Q1(f) — gross profit margin | 1/3 |
| 3 | June 2019 P1 Q2(d) — above-the-line promotion | 1/3 |
| 6 | June 2019 P1 Q1(g) — satisfying customer needs | 2/6 |
| 6 | June 2019 P1 Q3(d) — usefulness of break-even analysis | 4/6, 2/6 |
| 6 | June 2019 P1 Q4(b) — profitability ratios | 2/6 |
| 6 | June 2019 P1R Q1(g) — customer satisfaction | 3/6 |
| 9 | June 2019 P1 Q2(f) — motivation option | 7/9, 4/9 |
| 9 | June 2019 P1 Q3(e) — source of finance | 3/9 |
| 9 | May 2023 P2 Q3(e) — bonus vs job enrichment (IKEA) | 5/9 |
| 12 | June 2019 P1 Q4(c) — primary market research | 10/12, 4/12 |
| 12 | May 2023 P2 Q4(c) — demographic segmentation (IKEA) | 10/12 |
| 3/6/9/12 | June 2019 P2 selected pages — technology (3/3 ✅), public relations (5/6, 3/6), job production (2/3), pricing (7/9, 4/9), research (6/9, 5/9), factory location (8/12, 7/12), Kaizen (5/6, 4/6) | mixed |

**The June 2019 Paper 2 booklet contains one further verified full-mark script** — P2 Q1(f), *explain one impact of technology*, **3/3** — catalogued in the source notes but not yet transcribed into this bank.

### ❌ Not covered by verified scripts

| Type | Instances | Why |
|---|---|---|
| **All 1-mark types** (MCQ, define, state) | **328** | Pearson does not publish exemplar scripts for 1-mark items. The **mark scheme answer is the perfect answer** — there is nothing to model beyond it. |
| **2-mark types** (calculate, outline) | **106** | Same. For *calculate*, the MS gives the worked figures and states *"Award full marks for correct numerical answer without working."* For *outline*, the MS convention is identify (1) + context (1). |
| Remaining 3/6/9/12 variations | — | Only a small subset of the 262 high-value items has a published exemplar. Pearson publishes exemplars for a handful of questions per paper, not all of them. |

---

## The honest gap statement

**This bank does not contain a verified candidate script for every question type and variation.** That would require Pearson to publish full-mark exemplars for all 696 items across 38 papers, which it does not do.

What it does contain:

1. **Verified full-mark exemplars for all four high-value tariffs** (3, 6, 9, 12), transcribed in full with the examiner's reasoning — so you can see exactly what the top band looks like.
2. **A complete, mechanical playbook** (`01_Mark_Tariff_Playbook.md`) derived from the actual mark schemes and level descriptors, covering **all 696 items** by type, even where no exemplar exists.
3. **Calibration scripts with named deficiencies** across every tariff, which teach the same lessons from the opposite direction.
4. **Real candidate scripts as page images** (`Exemplar_Scans/`).

**What is missing, and what would fill it:** `[CONSTRUCTED GRADE 9 TARGET]` answers for the remaining high-value variations — written from the QP, mark scheme and examiner guidance, and clearly labelled as constructed. These are **not** included in this first build. They are the next phase of work, and they must never be described as official or examiner-marked.

---

## How to use this bank without being misled

- A **`[VERIFIED CANDIDATE EXEMPLAR]`** tells you *"this exact script got this exact mark"*. Trust it as evidence of the standard.
- A **`[CONSTRUCTED GRADE 9 TARGET]`** tells you *"this is engineered to satisfy the mark scheme"*. It is a target, not proof. **None appear in this build.**
- For **1- and 2-mark items**, ignore exemplars entirely and go to the mark scheme — the MS *is* the perfect answer.
- The mark scheme is always primary for accepted content. Examiner reports and exemplars show how the criteria are *applied*; they are not the only valid wording. The mark schemes repeatedly state: *"Accept any other appropriate response."*

## Rebuilding and extending

```bash
cd Business_Studies_Answer_Bank
python3 build_question_inventory.py      # regenerate the 696-item inventory
python3 make_docx.py                     # regenerate the guide DOCX
```

The searchable text index makes any mark scheme or examiner report greppable:

```bash
cd ../../Paperlords_Archive
python3 search_paperlords.py --subject Business --type MS "Level 3"
python3 search_paperlords.py --subject Business --session "2024" --type ER "evaluate"
```
