# 00 — PEARSON OFFICIAL RULEBOOK (IGCSE Business 4BS1)

**Source:** [International GCSE Business assessment support page](https://qualifications.pearson.com/en/news-policy/subject-updates/business/international-gcse-business-assessment-support-page.html) — Pearson Qualifications, page dated **26 August 2026**.

**Audit status (10 Nov 2026): this is a legacy compilation, not a Pearson-issued rulebook.** It quotes and paraphrases Pearson pages and examiner commentary; source passages and interpretations have not all been checked in this audit. Its broad claims are not automatically rules. The official Issue 2 specification, the exact QP and identity-matched MS take precedence; see [`../P2_Preparation_Handoff.md`](../P2_Preparation_Handoff.md). In particular, the current specification says an Explain question does not require context, so the old blanket claim that naming a business always makes context compulsory is withdrawn.

Quoted passages are intended as Pearson wording, but each quotation’s source/page should be checked before reuse. Commentary from one paper must not be generalised into a universal rule without corroboration.

---

## How to use this legacy compilation

This file is a locator for claims and source excerpts, not the rule itself. For current scope and command-word requirements, use Pearson’s specification. For a particular answer, use that exact question paper and identity-matched mark scheme. The statements below were edited where this audit found overreach; unreviewed passages remain unverified.

---

# Legacy archive tariff summary — corpus-derived, not independently reconciled

The table below is a script-generated historic count, not a description guaranteed for every current or future paper. It has not been visually reconciled item-by-item in this audit.

| Tariff | Parts | Marks | Per paper | Where it sits |
|---|---|---|---|---|
| **1 mark** | **456** | 456 | **12** | MCQ · define · state · identify |
| **2 marks** | **152** | 304 | **4** | calculate one figure · outline one |
| **3 marks — Explain** | **152** | 456 | **4** | **1(f) · 2(c) · 2(d) · 2(e)** |
| **6 marks — Analyse** | **114** | 684 | **3** | **1(g) · 3(d) · 4(b)** |
| **9 marks — Justify** | **76** | 684 | **2** | **2(f) · 3(e)** |
| **12 marks — Evaluate** | **38** | 456 | **1** | **4(c)** |
| **TOTAL** | **988** | **3040** | **26** | **38 × 80 ✅** |

> **This is a generated corpus summary, not a prescribed paper template.** Its tariff and question-position counts are not a future-paper guarantee and must not guide prediction. The official specification requires 80 marks and four compulsory questions of 20 marks each; it does not promise this internal item breakdown. Use the printed paper in front of you for its exact tariff and AO requirements.
>
> The legacy archive count of 988 tariff items / 3040 marks across 38 papers is a script-derived corpus statistic. It has not been independently reconciled item-by-item in this audit and should not be used as a coverage or frequency claim.
>
> **Reproduce it:** `python3 build_layer_c_tariffs.py` prints the full distribution and the 80-mark check.

> ### ⚠️ THE SCOPE OF THESE TOTALS — stated, because it is not the whole qualification's history
> **988 / 3040 is the count for the 38 papers whose mark schemes this bank holds** — every Summer series from 2019 to 2026 (four papers each, except June 2024 P2R and June 2026 P1/P2/P2R which were never published) and the November series of 2020, 2021, 2023, 2024 and 2025.
>
> **The qualification's history contains at least one more paper: November 2022, Paper 01R.** Pearson's own assessment-support page (retrieved 14 Oct 2026) prints a **notional Paper 1R** boundary row for **Nov 2022 — grade 9 = 49/80** — and **no Nov 2022 row** for the qualification, Paper 1, Paper 2 or Paper 2R. **That series ran as a 1R sitting only.** Its mark scheme is not in the archive and no search has retrieved it, so it is **not** in the totals above: with it, they would be **39 papers · 1014 parts · 3120 marks · 390 governed**.
>
> **So read "the whole qualification" as "the whole held qualification".** A count is only as complete as the source set it was derived from, and that set is a **fact about the archive**, not about the exam board. *(This scoping was added after the Nov 2022 1R paper was found on Pearson's boundary tables — the bank had recorded "the November series runs only Papers 01 and 02", which is true of every November series except that one.)*

⚠️ **The question-paper extraction under-detects every tier.** It reports 111 / 86 / 48 / 17 for the 3/6/9/12 tiers (withdrawn) **and 328 / 106 for the 1- and 2-mark tiers** — against **456 / 152** derived. **Non-constant loss: it cannot be corrected with a fudge factor.** For any count, read the mark scheme.

---

# DEFINE (1 mark)

> *"Define questions assess **AO1**.*
> *For 'Define' questions candidates are required to define a term from the specification content and show they have a clear understanding of the term."*

**Confirmed by the examiner reports** (`External_Exemplars/`): the three documented failures are giving **examples** instead of a definition, **using the word being defined**, and defining a **related but different term**.

**Practical test:** if your definition would still make sense with the term removed and replaced by a synonym you invented, you have defined it. If it says "X is the X-ing of X", you have not.

---

# STATE (1 mark)

> *"State questions assess **AO2**.*
> *Candidates should give an answer, **no longer than a sentence**, referring to a piece of contextual information from which they must select the answer. **One piece of context is sufficient.***
> *Answers to 'state' questions **must** have context in the response otherwise they will not gain the mark.*
> *Using the name of the business is **not** application (AO2) as the name of the business is used in the question.*"

### 🎯 The definitive statement of the context rule

> *"If the question contains a business name then the response **always** requires context."*

**And the four — only four — routes to a context mark:**

> *"Candidates can choose to **name the products/services the business offers**, they could choose to **name competitors in the same industry** or they could **state the industry the business operates in** to provide a contextualised response."*

### "No longer than a sentence"

Pearson is explicit that a State answer should be **one sentence**. This is a 1-mark question. Structure it:

```
[correct business point]  +  [one concrete noun from the case]
```

| ✗ 0 marks | ✓ 1 mark |
|---|---|
| "Can Culleretes would have to pay its workers more" | "…pay its **chefs** more" |
| "customers will buy their products" | "customers will buy **dog coats and dog leads**" |
| "increase in sales and market share" | "…**toys**" |
| "employees need induction to know the job" | "…when **selling furniture**" |

**Five independent confirmations across five papers.** The context noun is the whole mark.

---

# CALCULATE (2 marks)

> *"Centres should encourage candidates to include their working out as often candidates gained a mark for their calculation despite their final answer being incorrect…*
> *Centres must remind candidates that if the question states **'to 2 decimal places'** then this is the expectation to gain full marks for the question."*

### ⚠️ The most important mechanic in this section

> *"**If the answer is correct on the answer line, the examiner will automatically give 2 marks. The workings are only ever looked at if the answer on the answer line is incorrect.** Thus, very few candidates ever get 1 mark. This only happens when the workings are right, but the answer on the answer line is wrong.*
>
> *Centres should be aware that examiners are advised to take the answer provided by candidates **on the final answer line** therefore if the final answer is not to 2 decimal places the candidates will not gain access to the full marks **even if the answer to 2 decimal places is in the working out**. The answer provided by a candidate on the answer line is viewed as their **final response** to the question so that is what is marked."*

### 🎯 How calculation marking actually works

| Situation | Marks | Why |
|---|---|---|
| Correct answer **on the answer line** | **2** | Workings never inspected |
| Correct answer written only in the workings, wrong/blank on the line | **1 or 0** | **The answer line is what is marked** |
| Correct method, wrong answer **on the line** | **1** | Workings rescue it |
| Correct answer in workings but **to 1 d.p.**, and 2 d.p. was required | **1** | The line is marked, not the workings |
| Nothing correct | **0** | — |

**The practical protocol:**
1. **Always write your final answer on the dotted answer line** — not just inside the working.
2. **Copy it accurately.** The examiner takes the line as your final answer.
3. **Obey the decimal places** the question specifies.
4. Show workings anyway — they are your insurance if the line is wrong.

> **Examiner Tip (verbatim):** *"The formula in words is not required, nor are there any awardable marks for it. Candidates should be encouraged to save time by **not** including the formula in words."*
>
> **Examiner Tip (verbatim):** *"Always round to the required number of decimal places otherwise full marks cannot be attained."*

**Formula provision:** the current specification Appendix 4 states that its listed formulae are provided in Paper 1 and Paper 2 examinations. Do not assume that every useful relationship or calculation is printed as a formula, but also do not teach learners to memorise formulas that Pearson provides. Apply the figures and interpret the result.

---

# OUTLINE (2 marks)

> *"'Outline' questions are **AO2** (Application) questions.*
> *An 'Outline' question is **similar to a 'State' question** where candidates have to put their response in the context of the business.*
> *'Outline' questions require a point to score 1 mark. **To score two marks, there has to be development of the method and the existence of application somewhere within the response.**"*

### How to find application

> *"To provide application — **think about the market the business operates in, or the products that it sells, or simply just use a word or phrase from the case study.**"*

> **Examiner Tip (verbatim):** *"Only **one** reference to context is required in an 'outline' question."*

**Structure:** point **(1)** + development **and** one contextual noun **(1)**.

*Worked example (Jun 2024 P1R):* "questionnaires and ask how the **pet grooming service** has helped the customers' pet" → **2/2**. Rewriting "pet grooming service" as "products" → **1/2**.

---

# EXPLAIN (3 marks)

> *"An 'explain' question **does not need to be in context as there are no AO2 marks available**.*
> *Candidates gain a mark for **identifying one factor**. Centres are encouraged to teach candidates that for 'Explain' questions they **only need to explain one** as opposed to listing many.*
> *Candidates should then add some development to their answer to gain two or three marks.*
> *Candidates should **not repeat the question at the start of their answer**. It wastes time."*

### Concise development, without a sentence quota

The quoted examiner advice against over-elaboration is useful time-management guidance for its cited Explain questions, not a rule that answers must contain exactly three sentences. The specification asks for a fact with two further expansion points; these can expand one another or develop the same fact. Match the actual response to the MS and stop when the required reasoning is complete.

### A distinction the bank did not previously hold

> *"Questions that ask to explain **an advantage or disadvantage** need a **different technique** to those that ask candidates to explain **a method or way**."*

| Question form | Technique |
|---|---|
| "Explain one **advantage/disadvantage** of X" | Identify the benefit/harm → **chain it to a consequence for the business** (ideally financial) |
| "Explain one **method/way** to do X" | Name the method → **explain how it works** → its effect |

This is why the June 2022 P2R response that named "job rotation" for a *method* question scored 2/3, while "explain one advantage of lower interest rates" responses needed to reach **survival/profit** for 3/3.

---

# ANALYSE (6 marks)

> *"'Analyse' questions are testing two of the Assessment Objectives… **AO2 'Application'** and **AO3 'Analysis'**. Thus, to be successful, candidates need to demonstrate both of these skills within their answer. **There are no AO1 marks.**"*

> *"Examiners will look at the response **'holistically'**, to see if candidates have applied their knowledge to the scenario and if they have analysed the information. Examiners will then make a decision as to where the response **'best fits'** into the Levels."*

> *"candidates who provide an extended answer but do not apply this answer to the context are **not allowing themselves to move into the top of level 2**… **Unless responses for 'analyse' questions are in the context of the given business scenario candidates will find it difficult to access to higher marks.**"*

### Examiner commentary on context (apply to its cited paper/question)

> *"**Context must be woven throughout the entire response, appearing in all paragraphs, and should demonstrate variety rather than mere repetition.**"*

This is a Pearson examiner comment recorded for a particular series/question, not a universal paragraph-count or context-placement rule. For any response, apply the exact QP/MS descriptors: relevant application is needed where AO2 is assessed, and its depth/consistency matters to the level. Do not infer that every paragraph needs a distinct case noun, or that a fixed number of chains is required.

> *"**Listing many reasons, without the development, will not achieve the higher levels.**"*

That comment supports developing relevant reasoning; it does not set a universal required number of points.

---

# JUSTIFY (9 marks)

> *"The 'Justify' questions are marked in the same way as the 'Analyse' questions, but candidates now have to include **'Evaluative' (Assessment Objective 4)** comments…*
> *Some learners show clear knowledge of the two options but are unaware **there are no AO1 marks available** for these questions. Candidates who simply show knowledge of one or both options with no application, analysis or evaluation would gain **no marks**."*

### Whether to address one option or both

Pearson reports from some series state that both options need not be discussed and a full-mark response can focus on one; the May 2024 P1/P1R reports also include full-mark responses taking both routes. This confirms both approaches can work in those papers, not that a fixed route is required for every question. Follow the exact QP/MS, make the required recommendation, and ensure the response earns the assessed AO4 through supported evaluation.

### ⭐ How to earn AO4 without covering both options

> *"Candidates may access AO4 marks by offering **drawbacks to the same option for which they have given the advantages**. AO4 may also be provided by offering **direct contrasting points between the options**."*

**This resolves a genuine tension.** You do not need a second option to earn evaluation — you need to **turn on your own choice**. This is exactly what the verified 9/9 in `02_Verified_Exemplars.md` did (*"However, if the retailer uses crowdfunding… loss of control"*).

### Examiner Tips (verbatim) — the practical mechanics

> *"Ensuring that **'linking words/terms' such as 'thus', 'therefore', 'because' or 'this leads to'** allows more connected writing and development of answers. This is **vitally important** for answers that require extended writing."*

> *"Candidates should **avoid only repeating their previous arguments in their conclusion**."*

> *"Candidates should be encouraged to write effective conclusions when answering a 'justify' question. It allows them to gain the AO4 marks available… Centres should take time with students to practise writing **a detailed judgment based on the points discussed**."*

> **The cohort diagnosis (verbatim):** *"Candidates in general **are failing** to 'Make a judgement, providing a clear justification based on a thorough evaluation of business information and issues relevant to the choice made' which is AO4 in the specification and mark scheme."*

### 🎯 The linking-words technique

AO3 asks for **"logical chains of reasoning"**. Pearson names the mechanical way to produce them:

> **thus · therefore · because · this leads to**

If your sentences are not joined by these words, you are likely **listing**, not chaining. This is the cheapest, most mechanical AO3 upgrade available.

---

# EVALUATE (12 marks)

> *"Centres are reminded that this is **the only level-based question in the paper which is equally weighted across all four assessment objectives**… AO1 – knowledge, AO2 – Application, AO3 – Analysis and AO4 – Evaluation."*

> *"A Level 3 answer has **good context throughout the response as well as a balanced argument with a clear evaluation**."*

### The two documented reasons candidates underperform

> *"Those who perform less well than expected on this question do so for **one of two reasons**.*
> *Firstly, candidates provide a **generic answer with no application to the case study**.*
> *Secondly, candidates do not provide a **thorough judgment relating back to any issues that may occur for the business in the case study**, or they **do not balance their conclusion**, therefore limiting their evaluation."*

These are examples of weaknesses described for the cited paper; they do not establish that knowledge is irrelevant to every 12-mark question. Use that question’s AO allocation and level descriptors.

### ⭐⭐ The single most actionable 12-mark tip in the bank

> **Examiner Tip (verbatim):** *"It is recommended that the points of evaluation (AO4) should be **as detailed as the AO3 points**. Too often, candidates write **far too much for AO3 and leave insufficient space for a sound judgement**."*

This is advice about balancing development and judgement in the cited report, not a word/paragraph budget. The mark scheme allocates marks by assessment objective and judges the response against its descriptors; it does not prescribe a word share or number of paragraphs. A supported judgement may be integrated or separately stated if it answers the question.

### Other rules (verbatim)

> *"**Do not repeat the question at the start of your answer.** It does not score any marks and wastes valuable time."*

> *"Some candidates are using **bullet points or numbered format**, this will not allow them to gain the higher-level marks because they may not have analysed or evaluated the points made."*

> *"it is worth pointing out to candidates that this question **does carry the most marks and they should allow sufficient time to answer it**."*

---

# APPLICATION (AO2) — apply the specification and item-specific mark scheme

The quoted commentary below is Pearson guidance from a particular source; its broad phrasing must not override the qualification specification’s command-word definitions. In the current specification, **State** asks for a contextual response and **Outline** requires two linked contextual points; **Explain** is expressly not contextual. Define, give, identify and calculate follow their respective command definitions. Extended questions should use business context when AO2 is assessed, at the depth described by that question’s MS.

> *"If the question contains a business name then the response always requires context."*

Use the current command word, AO allocation and matching MS as the authority. Do not apply a blanket “business name means context at every tariff” rule.

---

# EVALUATION (AO4) — Pearson's own summary

> *"For the **justify and evaluate** questions students are required to 'Make a judgement, providing a **clear justification based on a thorough evaluation** of business information and issues relevant to the choice made. (AO4)'*
> *Students **must always provide a balanced assessment. Failing to provide developed counterbalance means it is extremely unlikely the candidate can reach the top level** in the mark scheme. **The counterbalance should be as equally developed as the points of analysis.***
> *It is advised that centres give guidance to candidates on **how to write a justification**… **Too few students are satisfying AO4 criteria in the longer questions**."*

The quoted “balanced assessment” language is examiner guidance in its source context, not a prescribed 50/50 word or paragraph split. For each response, read the relevant QP and MS: evaluation is awarded for the supported judgement the task requires, not a fixed counterpoint quota.

---

# AO2/AO3/AO4 BY TARIFF — the complete table

Compiled from this page plus the mark schemes in `By_Paper/`.

| Tariff | Command | AO1 | AO2 | AO3 | AO4 | Context required? | Conclusion required? |
|---|---|---|---|---|---|---|---|
| **1** | Define | **1** | — | — | — | No | No |
| **1** | State | — | **1** | — | — | ✅ **Yes** | No |
| **2** | Calculate | — | **2** | — | — | No | No |
| **2** | Outline | — | **2** | — | — | ✅ **Yes** | No |
| **3** | Explain | **3** | — | — | — | ❌ No | No |
| **6** | Analyse | — | **3** | **3** | — | ✅ Throughout | No |
| **9** | Justify | — | **3** | **3** | **3** | ✅ Throughout | ✅ Yes |
| **12** | Evaluate | **3** | **3** | **3** | **3** | ✅ Throughout | ✅ Yes |

> **Read the AO1 column.** Knowledge earns marks in only **two** places: the 1-mark Define and the 3-mark Explain. At 6, 9 and 12 marks, AO1 is worth **nothing** except the 3 marks inside the 12-marker.

---

# ROAD MAP — where Pearson says the full-mark examples are

This page lists, per tariff, **which examiner reports contain full-mark candidate answers**. This is the definitive answer to "do full marks exist for a given tariff, and where?"

### Analyse (6 marks)

| Paper 1 | Paper 1R | Paper 2 | Paper 2R |
|---|---|---|---|
| May 2022, 2023, 2024, 2025 | May 2022, 2023, 2024, 2025, **2026** | May 2022, 2023, 2024, 2025, **2026** | May 2022, 2023, **2026** |

### Justify (9 marks)

| Paper 1 | Paper 1R | Paper 2 | Paper 2R |
|---|---|---|---|
| May 2022, 2023, 2024 | May 2022, 2023, 2024, 2025 | May 2022, **2026** | May 2023, 2025, **2026** |

> **"The May 2024 Paper 1 and Paper 1R Examiners' Reports include two full[-]mark candidate answers. One has achieved full marks by considering both options, and the other has achieved full marks by considering just one option."**

### Evaluate (12 marks)

| Paper 1 | Paper 1R | Paper 2 | Paper 2R |
|---|---|---|---|
| May 2022, 2023, 2024 | May 2022, 2024 | — | — |

> **Note:** Pearson records **no** full-mark 12-mark example for Paper 2 or Paper 2R. **All four verified 12/12s in this bank are Paper 1** — **June 2024 P1 (PPS)**, **May/June 2023 P1 (Irsi Chocolatier)**, **June 2022 P1R (Can Culleretes)** and **June 2022 P1 (TBTS)**. **The best held *Paper 2* Evaluate is 10/12 (IKEA, May 2023) and the best *Paper 2R* 10/12 (M&M, May 2023)**; the best 1R is 11/12 (June 2026 P1R, Spud Bros). **The Paper 2 / 2R cell is permanent** — no full-mark example has ever been published there. *(This note said "both" and named two until 12 Nov 2026; the count is four.)*

### ⚠️ Sessions named here that are NOT yet in the archive or the harvest

Pearson lists **May 2026** throughout. The archive's newest papers are labelled *June 2026*. **These are almost certainly the same series** — and it means **examiner reports for the 2026 series exist**, in several papers where no full-mark example previously existed:

| Target Pearson names for 2026 | Held? |
|---|---|
| **Paper 1R Analyse** | ✅ **HELD** — the **June 2026 P1R** report was found on disk in the archive (48 pp) and harvested: a **6/6 Analyse** (Spud Bros sponsorship) and an **8/9 Justify**. *"May 2026"* and *"June 2026"* are the same series. |
| **Paper 2 Analyse** | ❌ **not held** — no June 2026 P2 report is in the archive or retrievable |
| **Paper 2R Analyse** | ❌ **not held** |
| **Paper 2 Justify** | ❌ **not held** |
| **Paper 2R Justify** | ❌ **not held** — though **a Paper 2R 9/9 is already banked twice** (May 2023 M&M · June 2025 Rabanne), so the gap is one of *paper* only, not of technique |

⚠️ **This list was written when none of the 2026 reports had been found, and it was still headed "not yet in the archive" long after the first one was. Checked against the register on 14 Oct 2026 — one of the five is held, four are not.** **A gap list is a claim about the archive, and the archive changes; re-derive it with `tally_exemplars.py` and the coverage scripts rather than trusting the headings.**

---

# GRADE BOUNDARIES

Since 2019 these have been **linear**, set on the total of both papers out of **160**.

> ## ⚠️ READ THIS BEFORE USING ANY NUMBER BELOW
> **The same subject has had a grade-9 boundary of 84/160 and of 137/160 — in the same qualification.** Nov 2021 needed **84**; June 2026 needed up to **137**. The boundary is set to hold the standard, not to hold the marks, so **an old paper's boundary tells you nothing about yours except that you should not be comforted by it.** A mock marked against a 2021 boundary would tell you that you have a 9 when you do not.
>
> **Use the most recent series. That is the whole point of this section.**
>
> **Provenance:** every row is read from Pearson's own published grade-boundary PDF. Rows marked ✅ were **re-read and confirmed on 14 Oct 2026**; rows marked 📄 are **corroborated by the published documents but not re-fetched this session.** No row here is estimated. **Sources are listed at the end of the section.**

## Overall boundaries — June 2026 (the series to aim at)

| Route | Max | **9** | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Standard: Papers 01 + 02** | 160 | **133** | 124 | 115 | 103 | 92 | 81 | 70 | 59 | 48 |
| **Regional: Papers 01R + 02R** | 160 | **137** | 129 | 122 | 110 | 98 | 87 | 72 | 58 | 44 |

> ### 📄 A SERIES WITH NO MOCK VALUE AT ALL — November 2022
> **November 2022 ran a Paper 01R sitting and nothing else** (Pearson's assessment-support page, retrieved 14 Oct 2026: a notional **Paper 1R** row for Nov 2022, and no row for the qualification, Paper 1, Paper 2 or Paper 2R). **Its notional grade 9 was 49/80** — against **68/80** in June 2026. **Read beside the other old sittings on the same page (notional Paper 1 / Paper 2): Nov 2021 = 41 and 43 · Nov 2020 = 46 and 44 · May 2019 = 57 and 54** — so 49 is not the lowest of the modern era, it is the fourth-lowest of the six old sittings, and **Nov 2021's 41 is**. *(Claiming the superlative before reading the rows is exactly the error this bank keeps catching; the correct statement is the comparison, not the medal.)* It is still the trap this section warns about: a paper from that sitting marked against its own boundary would flatter a candidate by nearly **twenty marks**. **The paper is also the one 4BS1 paper this bank does not hold** — see the scope note at the top of this file.

> ⚠️ **The two routes are NOT the same, and the gap is not a constant.** In **June 2026 the regional route needed 4 marks more for a 9** (137 v 133); in **June 2025 both routes needed exactly 130.** **Check which route you are entered for, and never assume last year's gap.** The `1C/2C` rows are identical to `01/02` and `1CR/2CR` to `01R/02R`.

## 🎯 Notional component boundaries — the numbers for a MOCK

*A mock is one paper, so the qualification boundary — which needs both — cannot mark it. These are Pearson's own component-level boundaries, published for exactly this purpose.*

**June 2026** ✅

| Paper | Max | **9** | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Paper 01** | 80 | **68** | 63 | 59 | 53 | 47 | 41 | 35 | 30 | 25 |
| **Paper 01R** | 80 | **68** | 64 | 61 | 55 | 49 | 43 | 36 | 29 | 22 |
| **Paper 02** | 80 | **65** | 60 | 56 | 50 | 45 | 40 | 34 | 28 | 23 |
| **Paper 02R** | 80 | **69** | 65 | 61 | 55 | 49 | 44 | 36 | 29 | 22 |

**June 2025** ✅ — for comparison, one series back

| Paper | Max | **9** | 8 | 7 |
|---|---|---|---|---|
| Paper 01 | 80 | 65 | 60 | 56 |
| Paper 01R | 80 | 65 | 61 | 57 |
| Paper 02 | 80 | 65 | 60 | 56 |
| Paper 02R | 80 | 65 | 61 | 57 |

**Every series, grade 9, per paper** — transcribed from Pearson's assessment-support page (retrieved 14 Oct 2026), which publishes a **notional component table for every series**; the two series held as PDFs (June 2026, June 2025) are marked ✅ and **agree with these figures exactly**.

| Series (Pearson's label) | Paper 1 | Paper 1R | Paper 2 | Paper 2R |
|---|---|---|---|---|
| **May 2026** ✅ | **68** | **68** | **65** | **69** |
| Nov 2025 | 66 | — | 67 | — |
| **May 2025** ✅ | **65** | **65** | **65** | **65** |
| Nov 2024 | 65 | — | 67 | — |
| May 2024 | 65 | 71 | 68 | 68 |
| Nov 2023 | 68 | — | 64 | — |
| May 2023 | 68 | 68 | 64 | 69 |
| **Nov 2022** | — | **49** | — | — |
| May 2022 | 54 | 58 | 54 | 59 |
| Nov 2021 | 41 | — | 43 | — |
| Nov 2020 | 46 | — | 44 | 48 |
| May 2019 | 57 | 57 | 54 | 56 |

*"—" means Pearson publishes no row, not that the paper did not exist.* **November 2022 is the one row with a single paper** — a Paper 1R sitting, no qualification-level boundary published for it (see the note at the head of this file). **The `P2R` row for Nov 2020 exists while the `P1R` row does not** — the page omits it, so **do not infer a Nov 2020 Paper 1R figure by subtraction**; the qualification figure (97) is published and the component is not.

> ### ✅ THE ADDITIVITY CHECK — exact for 2023–2026, and WRONG for 2019 and 2022
> **Checked across every series where both components and the qualification boundary are published — 17 pairs:**
>
> | Series | Route | Components | Sum | Published | |
> |---|---|---|---|---|---|
> | Nov 2021 | standard | 41 + 43 | 84 | **84** | ✅ |
> | Nov 2020 | standard | 46 + 44 | 90 | **90** | ✅ |
> | May 2022 | standard | 54 + 54 | 108 | **111** | ❌ **3 out** |
> | May 2022 | regional | 58 + 59 | 117 | **114** | ❌ **3 out, the other way** |
> | May 2019 | standard | 57 + 54 | 111 | **113** | ❌ **2 out** |
> | May 2019 | regional | 57 + 56 | 113 | **111** | ❌ **2 out, the other way** |
>
> **Every series from 2023 onwards adds exactly, at grade 9 — 11 of 11.** **4 of the 17 checkable pairs do not: May 2019 and May 2022, in either direction, by 2 to 3 marks.** *(Nov 2021 and Nov 2020 also add exactly; the four failures are the two oldest sittings that published both routes.)* So: **the sum check is a good check on recent papers and must not be trusted on old ones** — a notional component boundary is a *derived* number, and in those two sittings Pearson's qualification boundary is simply not the sum of its parts. *(An earlier version of this file said "if a number you have found does not add up like this, it is the wrong number" — that rule would have told you correct 2019 and 2022 numbers were wrong. The rule is now the table above.)* At **other grades** the standard route can be **1 out** from rounding — June 2026 grade 8: 63 + 60 = 123 against a published 124.
>
> **The cross-check that did pass, and is worth more than the sum check: Pearson's support page and the PDFs agree on all 18 published qualification-level grade-9 boundaries of this qualification's history, and on all four June 2026 and all four June 2025 component figures.** Two independently published sources, written years apart, agreeing to the mark — that is the strongest corroboration this file's boundary data has had.

## Trend — the whole series history, so the drift is visible

| Series | Max | **9** | 8 | 7 | 6 | 5 | 4 | 3 | Source |
|---|---|---|---|---|---|---|---|---|---|
| **Jun 2026 · standard** | 160 | **133** | 124 | 115 | 103 | 92 | 81 | 70 | ✅ |
| **Jun 2026 · regional** | 160 | **137** | 129 | 122 | 110 | 98 | 87 | 72 | ✅ |
| Nov 2025 · standard | 160 | **133** | 122 | 111 | 95 | 79 | 64 | 55 | 📄 |
| Jun 2025 · standard | 160 | **130** | 121 | 112 | 101 | 90 | 80 | 69 | ✅ |
| Jun 2025 · regional | 160 | **130** | 122 | 114 | 101 | 89 | 77 | 66 | ✅ |
| Nov 2024 · standard | 160 | **132** | 121 | 110 | 95 | 80 | 65 | 55 | 📄 |
| Jun 2024 · standard | 160 | **133** | 123 | 113 | 101 | 89 | 77 | 68 | 📄 |
| Nov 2023 · standard | 160 | **132** | 121 | 111 | 96 | 81 | 67 | 57 | 📄 |
| Jun 2023 · standard | 160 | **132** | 121 | 111 | 96 | 81 | 67 | 57 | 📄 |
| Jun 2023 · regional | 160 | **137** | 127 | 117 | 104 | 92 | 80 | 69 | 📄 |
| Jun 2022 · standard | 160 | **111** | 100 | 90 | 77 | 64 | 51 | 42 | 📄 |
| Jun 2022 · regional | 160 | **114** | 105 | 97 | 84 | 71 | 59 | 49 | 📄 |
| **Nov 2021** | 160 | **84** | 71 | 58 | 46 | 34 | 23 | 18 | 📄 |
| **Nov 2020** | 160 | **90** | 77 | 64 | 50 | 37 | 24 | 20 | 📄 |
| Jun 2019 · standard | 160 | **113** | 101 | 90 | 76 | 62 | 48 | 40 | 📄 |
| Jun 2019 · regional | 160 | **111** | 101 | 91 | 77 | 63 | 49 | 40 | 📄 |

> ### ⭐ THE TREND IS THE POINT, AND IT IS NOT GRADUAL
> **84 → 111 → 132 → 133.** The grade-9 boundary roughly **doubled in seven years**, and it **jumped 21 marks in a single year** between June 2022 (111) and June 2023 (132). Nothing about that is a change in how hard the papers are; it is a change in how well the field performs against a standard that is held fixed. **Three consequences for you:**
> 1. **Boundaries are near their ceiling** — the last four series sit within 5 marks of each other (130–137). **Assume ~83–86% for a 9, i.e. ~133/160.**
> 2. **A mock on a 2019–2022 paper should be marked against the modern boundary, not the paper's own.** A 2019 paper's own boundary would award a 9 for 113/160 — **50 marks a paper too generous.**
> 3. **The November series runs Papers 01/02 only** — no regional versions — so an R-entered candidate has no November fallback on the standard papers.
>
> ### ⚠️ THE ONE SENTENCE THAT MATTERS MOST
> Grade boundaries are published by Pearson for each series and route; consult the official boundary document for the relevant sitting. Do not infer a student’s likely grade from a generic mark budget, nor attribute a boundary difference to one AO or tariff without evidence. The item-level resource audit is not a learner-readiness or grade prediction.

### Sources (Pearson publications, all `qualifications.pearson.com`)

| Document | Path |
|---|---|
| Assessment support page — qualification **and notional component** boundaries for every series, and the exemplar booklets | `/en/news-policy/subject-updates/business/international-gcse-business-assessment-support-page.html` |
| Grade boundaries, June 2026 | `/content/dam/pdf/Support/Grade-boundaries/International-GCSE/grade-boundaries-june-2026-international-gcse.pdf` |
| Notional component, June 2026 | `/content/dam/pdf/Support/Grade-boundaries/International-GCSE/grade-boundaries-june-2026-notional-component-international-gcse.pdf` |
| Grade boundaries, June 2025 | `/content/dam/pdf/Support/Grade-boundaries/International-GCSE/grade-boundaries-june-2025-int-gcse.pdf` |
| Notional component, June 2025 | `/content/dam/pdf/Support/Grade-boundaries/International-GCSE/grade-boundaries-june-2025-notional-component-int-gcse.pdf` |
| Grade boundaries, Nov 2025 | `/content/dam/pdf/Support/Grade-boundaries/International-GCSE/2511-international-gcse-subject-grade-boundaries.pdf` |
| Older series | `2111_intGCSE_(9-1)_Subject_Grade_Boundaries_V2.pdf` · `2206-intgcse-9-1-subject-grade-boundaries.pdf` · `2306-intgcse-9-1-subject-grade-boundaries.pdf` · `2311-intgcse-9-1-subject-grade-boundaries.pdf` · `1906-ig-9-1-subject-grade-boundaries.pdf` |

> ⚠️ **The filename never follows one pattern.** It has been `grade-boundaries-june-2026-international-gcse.pdf`, `grade-boundaries-june-2025-int-gcse.pdf`, `2511-international-gcse-subject-grade-boundaries.pdf` and `2206-intgcse-9-1-subject-grade-boundaries.pdf` **in the same folder.** Three guesses failed on 14 Oct 2026 before the right names were found. **404 on one spelling is not absence** — and while you are guessing, a search engine that has already indexed the PDF will hand you the row in one query.

---

# Safe takeaways from the current specification and bounded source checks

This compilation formerly called a long list of derived statements “Official”. That label was too strong. The following are grounded in the current specification and/or the specific sources checked in this audit; each individual QP/MS still takes precedence:

| Command/demand | Safe guidance |
|---|---|
| State | Give a response in the context of the information supplied. Mentioning only the business name from the prompt may not provide meaningful application. No universal sentence count. |
| Outline | Two linked points about the concept/issue, placed in context. |
| Explain | A fact with two further expansion points; the current specification says this does not require case context. No fixed sentence count. |
| Calculate | Calculate from the given data; workings should be given. Some MSs award full marks for a correct answer without working; check the item’s scheme and requested precision. |
| Analyse | Extended response exploring/developing a concept in context. The sampled level-based schemes assess application and analysis; follow the exact AO split/levels. |
| Justify | Recommend one of the two options using the information. Reports show full-mark routes discussing one or both options; neither format is compulsory. |
| Evaluate | Extended response using specification knowledge to reach a supported conclusion about the business situation. A distinct conclusion paragraph, word share, “it depends” phrase or bullet rule is not prescribed by the specification. |

Pearson report comments about context, bulleting, answer length and balance are specific to their cited paper/questions unless independently confirmed. Never translate them into a universal quota.
