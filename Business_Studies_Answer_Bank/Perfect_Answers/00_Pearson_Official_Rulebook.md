# 00 — PEARSON OFFICIAL RULEBOOK (IGCSE Business 4BS1)

**Source:** [International GCSE Business assessment support page](https://qualifications.pearson.com/en/news-policy/subject-updates/business/international-gcse-business-assessment-support-page.html) — Pearson Qualifications, page dated **26 August 2026**.

**This is Pearson's own published guidance for 4BS1, organised by command word.** It is the most authoritative document in this bank: it is the awarding body telling candidates exactly how its own papers are marked. Where anything else in this bank disagrees with this page, **this page wins.**

Everything in quotation marks below is Pearson's wording, verbatim.

---

## Why this page matters

Everything else in this bank — exemplars, examiner reports, calibration — is *evidence* of how marking works. **This page is the rule.** It:

- states the AO allocation for every command word
- states what earns and loses marks, per tariff
- confirms (independently) several rules this bank had inferred from examiner comments
- corrects one rule the bank had stated only partially

---

# THE PAPER — what is actually on it, derived from all 38 mark schemes

**Before any rule about a command word, know the population it applies to.** These figures are **derived**, not counted from question papers: every part of every one of the 38 archived papers is reconstructed from its **mark scheme**, and each paper is required to sum to **80 marks**. **38 of 38 do.**

| Tariff | Parts | Marks | Per paper | Where it sits |
|---|---|---|---|---|
| **1 mark** | **456** | 456 | **12** | MCQ · define · state · identify |
| **2 marks** | **152** | 304 | **4** | calculate one figure · outline one |
| **3 marks — Explain** | **152** | 456 | **4** | **1(f) · 2(c) · 2(d) · 2(e)** |
| **6 marks — Analyse** | **114** | 684 | **3** | **1(g) · 3(d) · 4(b)** |
| **9 marks — Justify** | **76** | 684 | **2** | **2(f) · 3(e)** |
| **12 marks — Evaluate** | **38** | 456 | **1** | **4(c)** |
| **TOTAL** | **988** | **3040** | **26** | **38 × 80 ✅** |

> **The skeleton never varies.** Twelve one-mark items, four two-mark items, four Explain, three Analyse, two Justify, one Evaluate — **on every paper, in the same question positions.** 1(f)=3 · 1(g)=6 · 2(c)(d)(e)=3 · 2(f)=9 · 3(d)=6 · 3(e)=9 · 4(b)=6 · 4(c)=12.
>
> **The four governed tariffs carry 60 of the 80 marks (75%)**, and the 1- and 2-mark tiers carry the other 20. **Those 380 governed blocks are what this bank models; for the 608 parts of 1 and 2 marks the mark scheme itself is the perfect answer.**
>
> **Reproduce it:** `python3 build_layer_c_tariffs.py` prints the full distribution and the 80-mark check.

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

**Note:** the formulae sheet is printed at the front of every paper. Pearson notes *"some formulas are provided at the front of the paper"* — but **not all**. Break-even and percentage change must be recalled.

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

### ⚠️ The over-writing rule — confirmed authoritatively

> **Examiner Tip (verbatim):** *"There is no need to overelaborate when answering questions. 'Explain' questions, for instance, **should only require three sentences to answer the question. Anything more is not required and wastes time.**"*

**This confirms the finding from three marked scripts in the June 2022 series**, where candidates scoring **3/3** were told they had *"explained this benefit with more than two links of reasoning so has wasted some time when there are only 3 marks available."*

**Three sentences = identify + two developments. Then stop.**

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

### ⭐ Examiner Tip — the best single sentence on context in the entire bank

> *"**Context must be woven throughout the entire response, appearing in all paragraphs, and should demonstrate variety rather than mere repetition.**"*

Two requirements, both easy to fail:

| Requirement | Failure mode |
|---|---|
| **throughout** — in *all* paragraphs | naming the business once in the opening sentence |
| **variety** — not the same anchor repeated | using the word "toys" in every paragraph |

**And:** *"**Listing many reasons, without the development, will not achieve the higher levels.**"* — for a 6-marker, two well-developed, **linked** chains beat four undeveloped points.

---

# JUSTIFY (9 marks)

> *"The 'Justify' questions are marked in the same way as the 'Analyse' questions, but candidates now have to include **'Evaluative' (Assessment Objective 4)** comments…*
> *Some learners show clear knowledge of the two options but are unaware **there are no AO1 marks available** for these questions. Candidates who simply show knowledge of one or both options with no application, analysis or evaluation would gain **no marks**."*

### ✅ The both-options question — settled definitively

> *"**Candidates do not have to consider both options in their response. Candidates can achieve the full marks only considering the one option.**"*

> *"There is **no requirement** for candidates to discuss both options. Often when they do this they are **not able to justify each option in depth** in the time allocated for the question."*

> *"The **May 2024 Paper 1 and Paper 1R** Examiners' Reports include two full[-]mark candidate answers. One has achieved full marks by considering **both** options, and the other has achieved full marks by considering **just one** option. Candidates can take **either** route."*

**Both routes score 9/9. Pick one and go deep.**

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

**Both are execution failures, not knowledge failures.** Pearson is explicitly saying the 12-marker is lost on context and judgement, not content.

### ⭐⭐ The single most actionable 12-mark tip in the bank

> **Examiner Tip (verbatim):** *"It is recommended that the points of evaluation (AO4) should be **as detailed as the AO3 points**. Too often, candidates write **far too much for AO3 and leave insufficient space for a sound judgement**."*

**Read that as a word budget.** AO3 = 3 marks, AO4 = 3 marks. They are **equal**. If you have written four paragraphs of analysis and one line of conclusion, you have allocated your marks wrongly — even if everything you wrote was good.

**The practical target:**

| Component | Marks | Share of the answer |
|---|---|---|
| AO1 knowledge | 3 | ~25% |
| AO2 application | 3 | throughout (context in every paragraph) |
| AO3 analysis | 3 | ~35% |
| **AO4 evaluation** | **3** | **~35–40%** |

**Most candidates write AO3 and AO1, and treat AO4 as the closing sentence. That is where the 10/12 lives.**

### Other rules (verbatim)

> *"**Do not repeat the question at the start of your answer.** It does not score any marks and wastes valuable time."*

> *"Some candidates are using **bullet points or numbered format**, this will not allow them to gain the higher-level marks because they may not have analysed or evaluated the points made."*

> *"it is worth pointing out to candidates that this question **does carry the most marks and they should allow sufficient time to answer it**."*

---

# APPLICATION (AO2) — Pearson's own summary

> *"**If the question contains a business name then the response always requires context.***
> *Context is crucial to gain the top marks… Any question which refers to a specific business should give answers that are in the context of that business. This should be remembered when answering **the one mark 'state' questions**…*
> *Candidates can choose to name the **products/services** the business offers, they could choose to name **competitors** in the same industry or they could **state the industry** the business operates in…*
> *The high tariff questions ('analyse', 'justify' and 'evaluate') **also** require context."*

**Universal rule: if a business is named in the question, context is required — at every tariff, including 1 mark.**

---

# EVALUATION (AO4) — Pearson's own summary

> *"For the **justify and evaluate** questions students are required to 'Make a judgement, providing a **clear justification based on a thorough evaluation** of business information and issues relevant to the choice made. (AO4)'*
> *Students **must always provide a balanced assessment. Failing to provide developed counterbalance means it is extremely unlikely the candidate can reach the top level** in the mark scheme. **The counterbalance should be as equally developed as the points of analysis.***
> *It is advised that centres give guidance to candidates on **how to write a justification**… **Too few students are satisfying AO4 criteria in the longer questions**."*

**Note "counterbalance should be as equally developed as the points of analysis"** — the same 50/50 principle restated.

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

> **Note:** Pearson records **no** full-mark 12-mark example for Paper 2 or Paper 2R. The verified 12/12 in this bank is from **June 2024 Paper 1**.

### ⚠️ Sessions named here that are NOT yet in the archive or the harvest

Pearson lists **May 2026** throughout. The archive's newest papers are labelled *June 2026*. **These are almost certainly the same series** — and it means **examiner reports for the 2026 series exist**, in several papers where no full-mark example previously existed:

- **Paper 1R Analyse** — 2026
- **Paper 2 Analyse** — 2026
- **Paper 2R Analyse** — 2026
- **Paper 2 Justify** — 2026
- **Paper 2R Justify** — 2026

**These are the highest-value unharvested targets in the whole project.** They are the newest papers, and several fill gaps where no verified full-mark exemplar currently exists for that tariff-and-paper combination.

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

> ✅ **A check you can run yourself, on any series, and which passed on every one tested:** the two component boundaries **add to the qualification boundary.** June 2026 regional: 68 + 69 = **137** ✅. June 2025: 65 + 65 = **130** ✅. On the standard route they add to within ±1 (the scaling rounds), e.g. 68 + 65 = 133 ✅ at grade 9, but 63 + 60 = 123 against a published 124 at grade 8. **If a number you have found does not add up like this, it is the wrong number.**

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
> The grade-9 boundary is around **133/160 — so roughly 68/80 on Paper 1 and 65/80 on Paper 2.** **A "comfortable 8" performance — say 120/160 — is 13 marks short of a 9, and those 13 marks live almost entirely in AO4 evaluation.** That is why `10_Chain_Bank.md` spends its largest tier on 9- and 12-mark evaluation and why the 3-mark answers are capped at three sentences: **the marks that separate 8 from 9 are won in the last two tariffs, not in the first two.**

### Sources (Pearson publications, all `qualifications.pearson.com`)

| Document | Path |
|---|---|
| Grade boundaries, June 2026 | `/content/dam/pdf/Support/Grade-boundaries/International-GCSE/grade-boundaries-june-2026-international-gcse.pdf` |
| Notional component, June 2026 | `/content/dam/pdf/Support/Grade-boundaries/International-GCSE/grade-boundaries-june-2026-notional-component-international-gcse.pdf` |
| Grade boundaries, June 2025 | `/content/dam/pdf/Support/Grade-boundaries/International-GCSE/grade-boundaries-june-2025-int-gcse.pdf` |
| Notional component, June 2025 | `/content/dam/pdf/Support/Grade-boundaries/International-GCSE/grade-boundaries-june-2025-notional-component-int-gcse.pdf` |
| Grade boundaries, Nov 2025 | `/content/dam/pdf/Support/Grade-boundaries/International-GCSE/2511-international-gcse-subject-grade-boundaries.pdf` |
| Older series | `2111_intGCSE_(9-1)_Subject_Grade_Boundaries_V2.pdf` · `2206-intgcse-9-1-subject-grade-boundaries.pdf` · `2306-intgcse-9-1-subject-grade-boundaries.pdf` · `2311-intgcse-9-1-subject-grade-boundaries.pdf` · `1906-ig-9-1-subject-grade-boundaries.pdf` |

> ⚠️ **The filename never follows one pattern.** It has been `grade-boundaries-june-2026-international-gcse.pdf`, `grade-boundaries-june-2025-int-gcse.pdf`, `2511-international-gcse-subject-grade-boundaries.pdf` and `2206-intgcse-9-1-subject-grade-boundaries.pdf` **in the same folder.** Three guesses failed on 14 Oct 2026 before the right names were found. **404 on one spelling is not absence** — and while you are guessing, a search engine that has already indexed the PDF will hand you the row in one query.

---

# Summary of what this page establishes

| # | Rule | Status |
|---|---|---|
| 1 | State = AO2; **one sentence**; context mandatory; **naming the business is not context** | Official |
| 2 | Four context routes: products/services · competitors · industry · type of business | Official |
| 3 | **Only the answer line is marked** on calculations; workings are only consulted if the line is wrong | Official |
| 4 | 2 decimal places is a hard requirement, and the answer **line** must show it | Official |
| 5 | The formula in words earns nothing — don't write it | Official |
| 6 | Outline = State + development; **one** context reference suffices | Official |
| 7 | Explain needs **no** context (no AO2 marks); **three sentences**; more wastes time | Official |
| 8 | Explain needs a **different technique** for advantage/disadvantage vs method/way | Official |
| 9 | Analyse = AO2+AO3, **no AO1 marks** | Official |
| 10 | Context must be **woven throughout, in all paragraphs, varied** | Official |
| 11 | Justify: **both options not required**; both routes score full marks | Official |
| 12 | **AO4 can be earned by drawbacks to your own chosen option** | Official |
| 13 | Use linking words — *thus, therefore, because, this leads to* | Official |
| 14 | 12-mark: **AO4 must be as detailed as AO3** | Official |
| 15 | 12-mark: no bullets; don't repeat the question; allow the most time | Official |
| 16 | Grade 9 ≈ **65–68/80** per paper | Official |
