# The marks budget — what a grade 9 actually costs

**Purpose:** this file converts *"I want a 9"* into **an arithmetic target you can mark yourself
against**, using only numbers that can be re-derived from Pearson's own documents. Every figure here
is checked by `../verify_grade_budget.py`; if a number in this file drifts, that script fails.

---

## 1. The two numbers

| | Value | Source |
|---|---|---|
| Qualification total | **160** (two papers × 80) | Pearson, 4BS1 — two compulsory 80-mark papers |
| Grade 9 boundary, June 2026, standard route | **133/160** | `00_Pearson_Official_Rulebook.md`, boundaries table |
| Therefore: **marks you may lose across both papers** | **27** | 160 − 133 |
| Per paper, on average | **66.5 / 80** | 133 ÷ 2 |

> **Read that as permission, not as slack.** You do not need full marks on anything. You need to stop
> losing marks in **whole blocks** — which, as section 4 shows, is the way candidates actually lose
> them.

⚠️ **The regional route costs more in some sessions** — June 2026: **137/160** on the regional route
against 133 on the standard route; June 2025: **130 for both**. **Check which route you are entered
for.** Every figure in this file is the standard route unless it says otherwise.

---

## 2. Every paper is the same 26 questions — verified, 38 of 38

| Tariff | How many per paper | Marks |
|---|---|---|
| 1 mark | **12** | 12 |
| 2 marks | **4** | 8 |
| 3 marks | **4** | 12 |
| 6 marks (Analyse) | **3** | 18 |
| 9 marks (Justify) | **2** | 18 |
| 12 marks (Evaluate) | **1** | 12 |
| **Total** | **26** | **80** |

`verify_by_paper.py` re-derives this from all 38 mark schemes, and `verify_grade_budget.py` re-derives
it again here. **Four questions of 20 marks each; no paper deviates.** So a technique you learn on
Question 1 is worth exactly as much on Question 4.

---

## 3. Where the marks actually are — and the surprising part

Every paper's six long items carry a **fixed** assessment-objective split, and it is identical in all
38 papers:

| Item | AO1 | AO2 | AO3 | AO4 | Total |
|---|---|---|---|---|---|
| 3 × 6-mark Analyse | — | 3 each = **9** | 3 each = **9** | — | 18 |
| 2 × 9-mark Justify | — | 3 each = **6** | 3 each = **6** | 3 each = **6** | 18 |
| 1 × 12-mark Evaluate | **3** | 3 | 3 | 3 | 12 |
| **All six** | **3** | **18** | **18** | **9** | **48** |

The other **32 marks** (the 12 one-mark, four two-mark and four three-mark questions) are AO1/AO2.

> ## 🎯 THE NUMBER THAT SHOULD CHANGE HOW YOU REVISE
> **AO4 — evaluation — is worth 9 marks per paper, 18 in the whole qualification.**
> **AO3 — analysis — is worth 18 per paper, 36 across the two.**
>
> **So "get better at evaluation" is worth at most 18 marks, and you are allowed to lose 27.** What
> you cannot afford is a **zero on a whole question**, because one 12-mark question is worth 15% of a
> paper and one 9-mark question zeroed costs more than every AO4 mark in the qualification.

---

## 4. What candidates actually lose, measured on marked scripts

Each row is a real script in this archive, with the marks it moved. **This is the budget in practice.**

| Documented fault | Cost | The script it was measured on |
|---|---|---|
| **Answering the wrong task** — arguing "should CCT *pursue* satisfaction" when the stem says "*measure* the success of the business" | **9 → 0** on a 9-mark Justify | June 2025 P1R Q2(f), `audits/corpus/transcripts/4BS1_01R_2506_2f_0.md` |
| **A conclusion that restates the argument** | **9 → 8** | June 2026 P1R Q2(f) |
| **A conclusion that decides but names no condition** | **12 → 11** | June 2025 P1R Q4(c) (11/12) |
| **The "it depends" phrase with no condition named** | **9 → 8** | June 2025 P1R Q2(f) (8/9) |
| **One option instead of both on a Justify** | **no cost** — explicitly allowed | June 2024 P1R Q2(f) 9/9, and Pearson's own words: *"candidates were not required to consider both options"* |
| **No conclusion paragraph at all on a 12-marker** | **no cost** — verified | the 12/12 in `02_Verified_Exemplars.md` |
| **Round a calculation to the wrong number of decimal places** | loses the mark, even with correct working | June 2024 P1R Q3(c): *"provided their final answer to one decimal place so therefore cannot access the full marks"* |
| **A "state" answer with no context** | **1 → 0** | June 2024 P1 Q2(a): *"A good response but for the lack of context cannot access the AO2 mark"* |

> ### 🔬 WHAT THIS TABLE SAYS WHEN YOU READ IT DOWN
> **Four of the eight entries are losses of one or two marks. One is a loss of nine.** The
> disproportionate risk is **not** weak evaluation, and it is not knowledge — it is **answering a
> different question from the one printed**, and **misreading a tariff's job** (a 9-mark Justify is
> not a 12-mark Evaluate; a 6-mark Analyse has no AO4 at all).
>
> **A grade 9 is therefore mostly a discipline target, not a knowledge target** — which is good news
> on the timeline you have.

---

## 5. Three per-paper profiles that reach 133 — do the arithmetic yourself

Never count your own paper out of 80 as a percentage. Count it **by tariff**. These three profiles all
clear the boundary, and each one is a different bet:

| | 1-mark (12) | 2-mark (8) | 3-mark (12) | 6-mark (18) | 9-mark (18) | 12-mark (12) | Paper /80 | **Two papers /160** |
|---|---|---|---|---|---|---|---|---|
| **A · solid everywhere** | 12 | 8 | 11 | 15 | 14 | 9 | **69** | **138** ✅ |
| **B · strong long answers, sloppy short ones** | 10 | 7 | 10 | 16 | 15 | 10 | **68** | **136** ✅ |
| **C · one 9-mark zeroed, otherwise excellent** | 12 | 8 | 12 | 17 | 13 | 11 | **73** | **146** ✅ |

**Profile C is the point.** Even **losing an entire 9-mark question to zero**, a candidate who is
otherwise at Level 3 on everything still clears 133 with 13 marks to spare. **What no profile
survives is a habit that costs marks on every question** — a missing context sentence costs 1 mark on
each of 20 short questions, which is 20 marks, more than every AO4 mark in the qualification.

> ### 🎯 THE TWO HABITS THAT PAY FOR THEMSELVES
> 1. **One contextual sentence in every answer, including 1-mark "state" questions.** Pearson's own
>    wording: *"Just one piece of context will suffice."*
> 2. **Read the stem for its verb and its object before writing.** *Justify* → choose. *Analyse* →
>    chains, no judgement needed. *Evaluate* → both sides **and** a weighing judgement. *Explain* →
>    mechanism. **The tariff tells you the shape; the stem tells you the task.**

---

## 6. What is NOT in this budget

- **No AO4 marks in a 6-mark Analyse.** *"AO2 = 3 marks, AO3 = 3 marks. There is NO AO4."* A
  conclusion on a 6-marker earns nothing and costs time. (The 6/6 in `2025-06_P1R_CCT.md` has no
  conclusion and opens *against* its own point.)
- **No knowledge marks on a 9-mark Justify.** *"There are no knowledge marks available for this
  question."* Defining both options is worth zero.
- **No marks for length, spelling or handwriting.** Verified repeatedly, including on 9/9 scripts
  full of errors.
- **No marks for the phrase "it depends".** Four scripts in this bank use it and lose a mark; one
  12/12 does not use it at all.

---

*Arithmetic checked by `../verify_grade_budget.py`. Boundary figures from
`00_Pearson_Official_Rulebook.md`; tariff and AO skeleton re-derived from all 38 mark schemes in
`By_Paper/`.*
