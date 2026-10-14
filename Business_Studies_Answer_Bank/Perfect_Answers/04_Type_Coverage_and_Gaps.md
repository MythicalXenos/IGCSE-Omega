# 04 — TYPE COVERAGE AND GAPS

An honest account of what this bank contains and what it does not. Read this before trusting the bank to be complete.

---

## The full taxonomy

> ### 🚨 CORRECTION — 14 October 2026. THE TABLE BELOW IS A QUESTION-PAPER VIEW, NOT A CENSUS.
> **Everything in it comes from text-extracted question papers, and that extraction under-detects NON-CONSTANTLY.** The 3/6/9/12 rows have since been **re-derived from the mark schemes** and are shown in bold at the bottom of the table. **The 1- and 2-mark rows have now been re-derived as well, and they were wrong too** — which this file previously said they were not.
>
> **The derived population, from all 38 mark schemes, every paper reconciling to 80 marks:**
>
> | Tariff | Parts | Marks | Per paper | The part |
> |---|---|---|---|---|
> | **1 mark** | **456** | 456 | **12** | MCQ · define · state · identify |
> | **2 marks** | **152** | 304 | **4** | calculate one figure · outline one |
> | **3 marks** | **152** | 456 | **4** | **1(f) · 2(c) · 2(d) · 2(e)** |
> | **6 marks** | **114** | 684 | **3** | **1(g) · 3(d) · 4(b)** |
> | **9 marks** | **76** | 684 | **2** | **2(f) · 3(e)** |
> | **12 marks** | **38** | 456 | **1** | **4(c)** |
> | **ALL TARIFFS** | **988** | **3040** | **26** | = 38 × 80 marks ✅ |
>
> **The CSV's own subtotals were 328 one-mark and 106 two-mark items. Derived from the mark schemes: 456 and 152.** So the question-paper extraction **under-detects the 1- and 2-mark tiers by 128 and 46 parts** — the same fault, in the tiers where it was assumed not to matter. **Rebuild with `python3 ../build_layer_c_tariffs.py`, which now prints this distribution and the check that proves it: 988 parts and 3040 marks across 38 papers.**
>
> **What this does NOT change:** the **1- and 2-mark tiers still need no models** — for those the mark scheme *is* the perfect answer. **The 380 governed blocks and the whole of Layer C stand.** What changes is only **how many of them there are**, and therefore any percentage in this file computed against 696.

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
**111 / 86 / 48 / 17 is WITHDRAWN — 152 / 114 / 76 / 38 replaces it.**

⚠️ **AND SO IS THE CLAIM THAT THE CSV IS "STILL USEFUL FOR THE 1- AND 2-MARK ITEMS".**
It is not. Derived from the mark schemes, the 1- and 2-mark tiers hold
**456 parts (12 per paper) and 152 parts (4 per paper)** — the CSV reports
**328 and 106**. The extraction misses **128 one-mark parts and 46 two-mark
parts**, i.e. **220 marks of the 760** those tiers carry. **The 696-row count is
a question-paper view of the papers, useful for reading prompts; it is not a
count of anything.** For any count, read the mark scheme (rule 120).

### Why the four bold rows are the whole game

The 3, 6, 9 and 12-mark questions are **380 of the 988 parts** — and they carry **60 of the 80 marks on every paper (75%)**, because the 1-mark MCQ and define items are single marks while a single evaluate is worth twelve.

On every paper (80 marks total), the tariff breakdown is **exactly this — derived, not estimated:**

| Tariff | Parts per paper | Marks per paper |
|---|---|---|
| 1-mark items | **12** | **12** |
| 2-mark items | **4** | **8** |
| 3-mark Explain | **4** | **12** |
| 6-mark Analyse | **3** | **18** |
| 9-mark Justify | **2** | **18** |
| 12-mark Evaluate | **1** | **12** |
| | **26 parts** | **80 marks** |

**Identical on all 38 papers.** The skeleton never varies: **1(f) = 3 · 1(g) = 6 · 2(c)(d)(e) = 3 · 2(f) = 9 · 3(d) = 6 · 3(e) = 9 · 4(b) = 6 · 4(c) = 12** — that is 60 marks — and the remaining **20 marks** are the 1- and 2-mark items above them.

**So the four governed tariffs are worth 60 of the 80 marks (75%), not "54".** This bank's verified exemplars concentrate exactly there, which is the correct allocation of effort. Reproduce the skeleton with `python3 ../build_layer_c_tariffs.py`.

---

## Coverage status by type

### ✅ Fully covered — verified full-mark exemplar available

| Tariff | Type | Verified exemplar | Score |
|---|---|---|---|
| 3 | Explain one | **44 scripts, June 2019 → June 2026** — e.g. Jun 2019 P1 Q1(f) gross profit margin · Jun 2022 P1 Q2(c) flat structure · Jun 2023 P2 Q2(c) cash flow forecasting (×2) · Jun 2024 P2 Q2(e) job-advert information (×2) · **Jun 2026 P1R ×4, each with its 0/3 on the facing page** | **3/3 ×35** |
| 6 | Analyse | June 2019 P1 Q1(g) — satisfying customer needs | **6/6** |
| 6 | Analyse | June 2019 P1 Q4(b) — usefulness of profitability ratios | **6/6** |
| 6 | Analyse | June 2019 P1R Q1(g) — customer satisfaction | **6/6** |
| 9 | Justify | June 2019 P1 Q3(e) — source of finance | **9/9** |
| 12 | Evaluate | June 2024 P1 Q4(c) — importance of marketing to PPS | **12/12** |

*(The three 6-mark full-markers were confirmed by the source notes and examiners' comments; the June 2019 P1R 6/6 is confirmed as "Level 3 – 6 marks" in the same booklet.)*

**All four high-value tariffs have at least one verified full-mark exemplar, and all four are transcribed in full with examiner commentary in `02_Verified_Exemplars.md`.** **The 3-mark tier grew from three exemplars to seven on 14 Oct 2026 — the four June 2026 ones are in `External_Exemplars/2026-06_P1R_SpudBros.md`, each with its 0/3 partner on the facing page.**

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

**The June 2019 Paper 2 booklet contains one further verified full-mark script** — P2 Q1(f), *explain one impact of technology*, **3/3** — ✅ **and it IS transcribed: it is in `External_Exemplars/2019-06_P2_Official_Exemplar_Booklet.md` with the response verbatim, the examiner's comment verbatim, and the three marks decomposed element by element.** *(This line said "not yet transcribed" — it was stale; the booklet harvest carried it in.)* **Its examiner comment is the finding worth keeping: *"A number of responses tended to give two impacts of technology as opposed to one, and the consequence of this was that they could not gain the full marks available."***

### ❌ Not covered by verified scripts

| Type | Instances | Why |
|---|---|---|
| **All 1-mark types** (MCQ, define, state) | **456** *(derived)* | **Nothing to model: the mark scheme answer IS the perfect answer.** ⚠️ **This row said 328 and "Pearson does not publish exemplar scripts for 1-mark items" — both wrong, corrected 14 Oct 2026.** 328 is the *withdrawn extraction count* (the true derived figure is 456); and Pearson **does** print scored 1-mark scripts — June 2026 P1R, May 2023 P1/P1R/P2/P2R — usually as 0/1 versus 1/1 pairs. **What those pairs teach is the context trap, not the content**: on a State question the answer is right and the mark is lost for not applying it. That is already rule territory (`01_`), so the scripts stay unrendered by choice — but not because they do not exist. |
| **2-mark types** (calculate, outline) | **152** *(derived)* | Same, and **the count is likewise corrected from the withdrawn extraction figure of 106.** For *calculate*, the MS gives the worked figures and states *"Award full marks for correct numerical answer without working."* For *outline*, the MS convention is identify (1) + context (1) — and June 2026 P1R prints a worked 1/2 versus 2/2 **outline** pair where the only difference is the context sentence. |
| Remaining 3/6/9/12 variations | — | Only a small subset of the **380** governed blocks has a published exemplar. *(This said 262 — a withdrawn figure.)* Pearson publishes exemplars for a handful of questions per paper, not all of them. |

---

## The honest gap statement

**This bank does not contain a verified candidate script for every question type and variation.** That would require Pearson to publish full-mark exemplars for **all 988 parts across 38 papers**, which it does not do. *(This said "696 items", which is the question-paper extraction's row count, not the number of parts — see the warning at the top of this file.)*

What it does contain:

1. **Verified full-mark exemplars for all four high-value tariffs** (3, 6, 9, 12), transcribed in full with the examiner's reasoning — so you can see exactly what the top band looks like.
2. **A complete, mechanical playbook** (`01_Mark_Tariff_Playbook.md`) derived from the actual mark schemes and level descriptors, covering **all 988 parts** by type, even where no exemplar exists.
3. **Calibration scripts with named deficiencies** across every tariff, which teach the same lessons from the opposite direction.
4. **Real candidate scripts as page images** (`Exemplar_Scans/`).

**What was missing, and what filled it:** `[CONSTRUCTED GRADE 9 TARGET]` answers for the remaining high-value variations, written from the QP, mark scheme and examiner guidance and clearly labelled as constructed. Those were the next phase, and **that phase is done** — the models now live in **`10_Chain_Bank.md`**, which is canonical, with `05_Constructed_12mark_Models.md` as earlier worked models on the same topics. They must never be described as official or examiner-marked; **no score is claimed for any of them.**

**What remains missing — and it is not all fillable.** Layer C is closed at 152/152 · 114/114 · 76/76 · 38/38, but three full-mark cells are still open and one is permanent: **no verified 12/12 exists for Paper 2 or Paper 2R** (both bank 12/12s are Paper 1, and Pearson names the June 2022 and June 2024 *Paper 1* reports as the 12-mark exemplar sources). See `08_Completion_Map.md` for the live position; do not restate these counts elsewhere.

---

## How to use this bank without being misled

- A **`[VERIFIED CANDIDATE EXEMPLAR]`** tells you *"this exact script got this exact mark"*. Trust it as evidence of the standard.
- A **`[CONSTRUCTED GRADE 9 TARGET]`** tells you *"this is engineered to satisfy the mark scheme"*. It is a target, not proof, and **no score is ever claimed for one.** These **are** in this build: the constructed models in `10_Chain_Bank.md` and `05_Constructed_12mark_Models.md` carry the label. *(This line used to say "None appear in this build", written before they were written — the fourth stale claim of the Layer D audit.)*
- For **1- and 2-mark items**, go to the mark scheme first — the MS *is* the perfect answer, **so no model is needed**. ⚠️ **But do not skip the reports: they print marked scripts for this tier too** — **80 across the five archived reports, each with an examiner comment**, including **0-versus-1 pairs for every 1- and 2-mark part of June 2026 P1R** and, in May 2023, the same part printed at **0 and at 1** side by side. **What a 0 looks like is the one thing the mark scheme cannot tell you** — and it is the whole reason these are worth reading. *(Derived by `audit_er_fullmarks.py`.)*
- The mark scheme is always primary for accepted content. Examiner reports and exemplars show how the criteria are *applied*; they are not the only valid wording. The mark schemes repeatedly state: *"Accept any other appropriate response."*

## Rebuilding and extending

```bash
cd Business_Studies_Answer_Bank
python3 build_question_inventory.py      # regenerate the 696-row QUESTION-PAPER view
                                         #   (an extraction of the QPs, not a count of
                                         #    the parts: it under-detects the 1- and
                                         #    2-mark tiers. For the population, use
                                         #    build_layer_c_tariffs.py)
python3 make_docx.py                     # regenerate the guide DOCX
```

The searchable text index makes any mark scheme or examiner report greppable:

```bash
cd ../../Paperlords_Archive
python3 search_paperlords.py --subject Business --type MS "Level 3"
python3 search_paperlords.py --subject Business --session "2024" --type ER "evaluate"
```
