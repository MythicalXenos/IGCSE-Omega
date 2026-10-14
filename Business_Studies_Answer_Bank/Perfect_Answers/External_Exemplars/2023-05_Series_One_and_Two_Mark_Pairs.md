# THE 1- AND 2-MARK TIER — the archive prints 80 scripts for it, and the bank held none

**Why this file exists.** `09_Verified_Tally.md`'s headline table read:

> *"1- and 2-mark items — n/a: **the mark scheme IS the perfect answer; Pearson publishes no scripts**"*

**The first half is right and the second half is false.** Mark schemes are still the perfect answer for this tier — a model answer would be redundant — **but Pearson prints marked 1- and 2-mark scripts by the dozen, each with a ResultsPlus comment, and the bank held none of them.** The claim was corrected on 14 Oct 2026 the moment `audit_er_fullmarks.py` (check 23) could see the score statement: **80 scripts attributed to 1- and 2-mark parts across the five archived reports**, including a **0-and-1 pair for nearly every part** of June 2026 P1R.

**This is the largest tier in the qualification** — 456 of 3040 marks, twelve parts per paper — **and the one tier where the mark scheme cannot tell you the most important thing: what a 0 looks like.** A scheme lists what earns the mark. The examiner's comment on a rejected script says what was *not* enough, in the candidate's own words.

---

## WHAT THE FIVE REPORTS PRINT — derived, not counted by hand

`audit_er_fullmarks.py` walks every page in reading order and attributes each score statement to the most recent `Question N (x)` heading. Run it for the live table. **Page = the page the score statement is on.**

| Paper | Scripts on 1-/2-mark parts | by part (page = score) |
|---|---|---|
| **Jun 2026 P1R** | **20** | 1b: p4=0, p4=1 · 1c: p5=0, p5=1 · 1d: p6=0, p6=1 · 1e: p7=2, p8=1 · 2a: p13=0, p13=1 · 2b: p14=0, p14=1 · 3a: p24=0, p24=1 · 3b: p25=1, p25=2 · 3c: p27=1, p28=2 · 4a: p37=1, p38=2 |
| **May 2023 P1R** | **10** | 1b: p4=1 · 1c: p5=1 · 1d: p6=1 · 1e: p7=2 · 2a: p11=1 · 2b: p12=0 · 3a: p19=1 · 3b: p20=2 · 3c: p22=1 · 4a: p29=2 |
| **May 2023 P1** | **12** | 1b: p5=0 · 1c: p6=1 · 1d: p7=1, p8=0 · 1e: p9=2, p10=1 · 2a: p14=1 · 2b: p15=0 · 3a: p24=1 · 3b: p25=2 · 3c: p26=2 · 4a: p32=2 |
| **May 2023 P2R** | **19** | 1b: p4=0, p5=1 · 1c: p6=0, p6=1 · 1d: p7=0, p8=1 · 1e: p9=2 · 2a: p15=0, p16=1 · **2b: p17=0, p17=1** · **3a: p29=0, p29=1** · 3b: p30=0, p31=2 · 3c: p32=1, p33=2 · 4a: p41=1, p42=1 |
| **May 2023 P2** | **19** | 1b: p4=0, p6=1 · 1c: p7=0, p9=0 · 1d: p10=1, p11=0 · 1e: p12=1, p14=1 · 2a: p21=0, p23=0 · 2b: p24=0 · 3a: p38=0 · 3b: p40=0 · **3c: p42=2, p44=1** · **4a: p51=2, p53=1** |

⚠️ **A statement is attributed to the most recent question heading in reading order, and these reports print the score line at the FOOT of the page BEFORE the script** — so a handful of foot-of-page statements attach to the wrong heading. **The page lists above are the safe index; treat the part labels as strongly-indicated, not certified, until each page is read.**

---

# PAPER 2R — THREE MATCHED PAIRS, ALL OF THEM ONE-MARK

**A pair is worth more than a script.** May 2023 P2R prints the **same question, same paper, both scores**, one above the other, with a comment on each — and on **p6, p17 and p29 the two answers are on ONE page**. **These are the bank's first `[VERIFIED CANDIDATE EXEMPLAR]` entries for the 1- and 2-mark tier.**

## ⭐ `[VERIFIED CANDIDATE EXEMPLAR]` — **1/1 and 0/1** · Q1(c) *Define the term qualitative market research* — report p. 6

**Question (verbatim):** *"(c) Define the term **qualitative market research**."* **(1)**

**Official mark scheme (verbatim, P2R MS p. 6):** *"1 (c) · AO1 - 1 mark. Award 1 mark for a correct definition of qualitative market research.*
> • *Information about attitudes, beliefs and intentions (1)*

*(1)"*

**The 0-mark script (verbatim):**

> *"Qualitative market research is doing market research based on numerial figuers and factors other than numerical figuers and data. fore example the satisfaction of customers."*
> *(the candidate's own words: "numerial figuers" ×2, "fore")*

**Examiner comment (verbatim):** *"Candidate has made a valid point about market research but it is not a definition of qualitative market research."*

**The 1-mark script (verbatim):**

> *"Bussiness loolss the attitude and Beliefs of the customers."*
> *(read at 420 dpi: "Bussiness", and a word that reads as "loolss"/"looks" — the letter shapes are ambiguous, the sentence is not)*

**Examiner comment (verbatim):** *"This response demonstrates accurate knowledge of qualitative market research."*

**Cohort commentary (verbatim):** *"This define question was not as well answered with nearly three quarters of the cohort not gaining the mark available. Some candidates appeared to have confused the different types of market research. It is well worth candidates ensuring that they know the different types."*

🔬 **The pair is the whole lesson, and it is humbling.** The 0-mark answer is **46 words, structured, grammatical, gives a definition-shaped sentence and an example** — and it is worth **nothing**, because it defines the *other* type of research. The 1-mark answer is **8 words, misspelt twice, breaks the definition's grammar** — and it is worth **the mark**, because *"attitude and Beliefs"* is the mark scheme's own content.

> **Mark scheme:** *"Information about **attitudes, beliefs** and intentions"* → **1-mark script:** *"the **attitude and Beliefs** of the customers."*

⚠️ **And note what the 0-mark script got wrong, because it is a trap:** it wrote *"based on numerial figuers… other than numerical figuers"* — a definition of **quantitative** research in the negative. **"Three quarters of the cohort" lost this mark; the examiner's diagnosis is that candidates confused the types.** Learn the four types as four one-line definitions and nothing else.

---

## ⭐ `[VERIFIED CANDIDATE EXEMPLAR]` — **1/1 and 0/1** · Q2(b) *State one reason why M&M could dismiss an employee* — report p. 17

**Question (verbatim):** *"(b) State **one** reason why **M&M** could dismiss an employee."* **(1)**

**Official mark scheme (verbatim, P2R MS p. 11):** *"2 (b) · A02 - 1 mark. Award 1 mark for a reason why M&M could dismiss an employee **in the context of the business**.*
> • *M&M might dismiss an employee who continually arrives late on the tractor production line (1)*
> • *M&M may dismiss an employee in the sales department of tractors, whose absence has caused a loss of orders (1)*

*NB Do not accept a reason that is not in the context of M&M. Accept any other appropriate response. (1)"*

**The 0-mark script (verbatim):**

> *"less hard work and dosent helps the customers to see whab they wants."*

**Examiner comment (verbatim):** *"This candidate has given a very valid point about an employee who does not help customers with what they want. **This response could relate to any business and therefore the candidate did not gain a mark.**"*

**The 1-mark script (verbatim):**

> *"The employee is not productive enough, e.g. they are too slow at applying tyres to the cars."*

**Examiner comment (verbatim):** *"This candidate gained the mark available because they referred to the candidate being too slow at **applying tyres to the car**. Thus relating it back to the scenario."*

**Cohort commentary (verbatim):** *"Another 'State' question which again was not well answered, with nearly three quarters of the cohort not gaining the mark available. Again as mentioned, it was probably because the candidates had not put their response in context of M&M. It is well worth reiterating again that 'State' question needs to be in the context of the scenario, a number of candidates are being disadvantaged by not using this skill."*

🔬 **"This response could relate to any business" is the examiner stating the exact test**, and it kills an answer that is *business-sensible*. The 0-mark script's reason — *doesn't help customers* — is a legitimate reason a business dismisses someone. **It fails on one thing only: no M&M, no tractors, no tyres.**

⭐ **The 1-mark script is the shortest complete answer in the bank: 15 words, and it spends 7 of them on the context.** *"not productive enough"* is the reason — **and then the candidate adds an example that is entirely from the scenario.** Compare the scheme's own credited content: *"continually arrives late on the tractor production line"*. **The candidate's tyres and the scheme's tractor line are doing the same job.**

⚠️ **The report says this 1-mark answer contains a slip: *"they referred to the candidate being too slow"*** — the examiner wrote *candidate* where he meant *employee*. **The comment is about the answer, not about the person; read comments as instructions, not as praise.**

---

## ⭐ `[VERIFIED CANDIDATE EXEMPLAR]` — **1/1 and 0/1** · Q3(a) *Define the term autonomy* — report p. 29

**Question (verbatim):** *"**(a)** Define the term **autonomy**."* **(1)**

**Official mark scheme (verbatim, P2R MS p. 17):** *"3 (a) · A01 - 1 mark. Award 1 mark for a correct definition of autonomy.*
> • *Giving workers the authority to make choices and decisions about the way they work (1)*

*(1)"*

**The 1-mark script (verbatim):**

> *"Autonomy is when workers have the ability to make there own decisions and ideas in a business."*

**Examiner comment (verbatim):** *"This is a good example of how we would expect candidates to respond to this question."*

**The 0-mark script (verbatim):**

> *"Making a job more challenging by giving employees more responsibility."*

**Examiner comment (verbatim):** *"An example of a response which did not gain a mark."*

**Cohort commentary (verbatim):** *"Another 'Define' question where candidates were asked to define the term autonomy. This question was not well answered by the majority of candidates with only a quarter of the cohort gaining the mark available."*

🔬 **⚠️ THE HARDEST PAIR IN THIS FILE, AND THE ONE TO ACTUALLY REMEMBER. Read both answers again: the one that scored ZERO is the better English, the better business thinking and the more useful sentence.**

| | 1 mark | 0 marks |
|---|---|---|
| script | *"workers have the ability to **make there own decisions** and ideas in a business"* | *"Making a job more **challenging** by giving employees more **responsibility**."* |
| the scheme's words | *"workers the authority to make **choices and decisions**"* ✓ | — |
| the scheme's words it misses | — | the credited version is **decision-making authority**, not job design |

**The 0-mark answer describes JOB ENRICHMENT** — *"making a job more challenging by giving more responsibility"* is close to the textbook definition of one motivational job-design method. **It is a good answer to a different question, and on a 1-mark Define that is worth nothing.**

⭐ **What the 1-mark answer does instead: it names the WORKERS as the subject and the DECISIONS as the thing they hold.** *"workers have the ability to make their own decisions."* That is the marker's test — **who has the authority, over what.**

**Note also:** the 1-mark answer's *"there own"* (for *their*) and *"and ideas"* — two slips, **1/1**. The 0-mark answer contains no error at all. ⚠️ This is the cleanest proof in the bank that **a 1-mark question is marked for matching the definition, not for quality of expression.**

---

# PAPER 2 — TWO CALCULATION PAIRS, ALL OF THEM TWO-MARK

**Paper 2 prints both sides of every calculation question too** — a 2/2 and a 1/2 for Q3(c) and for Q4(a). **These four are the only marked calculation scripts the bank holds**, and between them they isolate the exact boundary of the answer-line rule.

## ⭐ `[VERIFIED CANDIDATE EXEMPLAR]` — **2/2 and 1/2** · Q3(c) *IKEA bonus calculation* — report pp. 43–44

**Stem (verbatim from the report):** *"IKEA is keen to reward long-serving employees. An employee who has worked with IKEA for 10 years is given a bonus of 7.5% on top of their annual earnings of 177 070 SEK."*
**Question (verbatim):** *"(c) Calculate, to two decimal places, the bonus this employee would receive. You are advised to show your working."* **(2)**

**Official mark scheme (verbatim, P2 MS p. 17):** *"3 (c) · A02 - 2 marks*
> *177 070 x 0.075 (1)*
> *= 13 280.25 (1)*

*Award 1 mark for correctly substituting numbers into formula. **Award full marks for correct numerical answer without working.** (2)"*

**The 2/2 script (verbatim — the working is read from the 200 dpi page render and the native scan):**

> *"177 070 ÷ 100 = 1770.7"*
> *"17◊0.7 × 7.5 = 13280.25"* *(the second character of "1770.7" is overwritten; the arithmetic gives 1770.7)*
> *"177070 − 13280.25"* *(written and not completed)*
> **Answer line: `13 280.25 SEK`**

**Examiner comment (verbatim):** *"This response shows how the candidate has worked out the bonus for the employee."*

**The 1/2 script (verbatim):**

> *"177 070 ·"*
> *"7.5/100 > 0.075"*
> *"0.075 × 177 070 = 1328025"*
> **Answer line: `13280.2 SEK`**

**Examiner comment (verbatim):** *"This response only gained 1 mark, as the final answer on the dotted lines has only one decimal point, even though the correct answer is higher up. Care should be taken to ensure that the correct answer is placed on the dotted lines."*

**Cohort commentary (verbatim, on the 2/2 page):** *"Another calculation question where candidates should be encouraged to show their workings. Just over a third of the cohort did not gain a mark on this question, with two fifths gaining the two marks available."*

🔬 **⚠️ EXTRAORDINARY, AND THE MOST IMPORTANT THING IN THIS FILE: THE 1/2 CANDIDATE DID THE HARDER ARITHMETIC CORRECTLY AND STILL LOST A MARK — AND SO DID THE 2/2, FOR THE SAME REASON IN MIRROR IMAGE.**

| | 2/2 (p. 43) | 1/2 (p. 44) |
|---|---|---|
| method | divide by 100, **then** × 7.5 | convert to a decimal, *then* × 177 070 |
| the answer it reaches | **13 280.25** ✓ | **13 280.25** ✓ |
| where it writes it | working line, **complete, two decimals** | working line, complete |
| the answer **line** | `13 280.25 SEK` ✓ | `13280.2 SEK` ✗ |
| what the examiner credited | everything | **one mark** |
| why | — | *"the final answer on the dotted lines **has only one decimal point**, even though **the correct answer is higher up**"* |

**Both candidates can do the calculation. The mark turned on the last digit of one line.** ⚠️ **And note the 1/2 candidate is doing it the more sophisticated way** — decimal conversion then multiplication, versus the 2/2's two-step percentage route — **and the mark scheme's own content is the 2/2's route** (`177 070 x 0.075`). **Method was not the issue; the answer line was.**

⭐ **The examiner's instruction is the mark: *"Care should be taken to ensure that the correct answer is placed on the dotted lines."*** — and it is the same rule the bank already holds from **June 2026 P1R Q3(c)** in `External_Exemplars/2026-06_P1R_SpudBros.md:266`, where a wrong answer line cost the final mark and the workings were read only to rescue one. **Two series, two papers, two questions, one rule.**

⚠️ **The read of the 1/2 answer line, stated honestly:** at native scan resolution it reads `13280·2 SEK`. **The examiner's comment settles what it must say** — *"has only one decimal point"* — and the working above it shows the full `13280.25`. **Where a glyph is ambiguous and the examiner describes it in words, the examiner's words are the better evidence.**

---

## ⭐ `[VERIFIED CANDIDATE EXEMPLAR]` — **2/2 and 1/2** · Q4(a) *IKEA inventory percentage decrease* — report pp. 52–53

**Stem (verbatim):** *"IKEA continually reviews the products it makes to meet the demands of its customers. Changing the design of bedroom furniture to meet the needs of a couple setting up home or of parents refurbishing their children's bedroom. Figure 3 shows the value of IKEA's inventory for 2019 and 2020."* *(Figure 3: **2019 — 4.3** · **2020 — 3.7**, € billions)*
**Question (verbatim):** *"(a) Calculate, to two decimal places, the percentage decrease in inventories from 2019 to 2020. You are advised to show your working."* **(2)**

**Official mark scheme (verbatim, P2 MS p. 21):** *"4 (a) · A02 - 2 marks*
> *4.3 – 3.7 = 0.6 (1)*
> *0.6 ÷ 4.3 x 100 = 13.95 (1)*

*Award 1 mark for correctly substituting numbers into formula. **Award full marks for correct numerical answer without working.** (2)"*

**The 2/2 script (verbatim):**

> *"4.·3̶ − 3.7 = 0.6"* *(a correction struck over the first figure's decimal)*
> *"0.6 / 4.3 × 100 = 13.45"* *(written "13·45")*
> **Answer line: `13.45 %`**

**Examiner comment (verbatim):** *"The candidate has clearly shown how they have worked the answer out **gaining the 2 marks available**."*

**The 1/2 script (verbatim):**

> *"4.3 − 3.7 = 0.6"*
> **Answer line: `0.60 %`**

**Examiner comment (verbatim):** *"This response only gained 1 mark as **only the first part of the calculation is shown**."*

**Cohort commentary (verbatim, on the 2/2 page):** *"Another calculate question and as previously mentioned, candidates should be encouraged to show their workings on all calculation questions. If the actual answer is wrong then candidates could gain a mark for the working out. Two fifths of the candidates gained the mark available on this question. **Candidates should be encouraged to double check the requirements of the question as some candidates only worked out parts of the question and missed full marks because they did not complete all of the calculations required from the question.**"*

🔬 **This pair separates the two marks cleanly, and it also carries a warning about the 2/2.**

> **Mark scheme:** `4.3 – 3.7 = 0.6 (1)` · `0.6 ÷ 4.3 x 100 = 13.95 (1)`
> **1/2 script:** `4.3 − 3.7 = 0.6` — **the first line of the scheme, and nothing else.** · Answer line `0.60 %`

**The 1/2 candidate stopped exactly at the first award line.** *"Only the first part of the calculation is shown"* — and the answer line repeats the first step's result (`0.60`, from `0.6`) with a % sign on it, **which is a percentage of nothing.** ⚠️ **The mark was earned and then abandoned.**

⚠️ **And the 2/2's first line: `4.·3̶ − 3.7 = 0.6` — the candidate struck a correction over a digit and still scored full marks.** Same series, same paper, same question: **struck-out working costs nothing** (rule 55's family). The examiner read through the correction.

🔬 **⚠️ THE 2/2's FINAL ANSWER IS `13.45`, NOT THE SCHEME'S `13.95` — and it was awarded 2/2, with the examiner writing that the candidate "clearly shown how they have worked the answer out".** Both `13.95` (the scheme) and `13.45` (this script) appear in the same family of numbers; **the digit in the tens is written unmistakably as a 4 in the 200 dpi render and in the native scan.** ⚠️ **Read this as the report printing it, not as an arithmetic claim:** the credit is visible, the comment is explicit (*"gaining the 2 marks available"*), and **the report chose to print this script as its worked example of a full-mark calculation.** *(An earlier pass at this page read the written figure with the image's diagonal correction line crossing it; the current read is from the 832×968 native scan at 6× magnification, where the correction line is clearly separate from the digit.)*

⭐ **The cohort commentary is the examiner telling the cohort the fix, in the same words as the 1/2's comment:** *"some candidates only worked out **parts** of the question and missed full marks because they did not complete all of the calculations required."*

---

# WHAT THESE HAVE ESTABLISHED

1. **"Pearson publishes no scripts for 1- and 2-mark items" was false** — and it was stated in `09_`'s headline table where every reader looks first. The tier has **80 printed scripts across five reports**, and the archive has printed a **0-and-1 pair for nearly every part of June 2026 P1R**.
2. **⭐ For a 1-mark State question, the context IS the answer.** *"less hard work and dosent helps the customers"* is a valid business reason and earns nothing; *"too slow at applying tyres to the cars"* earns the mark. The examiner's own test: **could this sentence be about any business?**
3. **⭐ For a 1-mark Define question, the mark scheme's word-level content decides — and a *better* answer can score zero.** Job enrichment is not autonomy. *"attitude and Beliefs"* is qualitative research. **Match the credited wording; do not improve on it.**
4. **⭐ On a calculation, the FINAL VALUE AT THE PRECISION THE QUESTION NAMES is the mark** — **not the arithmetic, and not the dotted line.** Two candidates did the arithmetic correctly and one line cost the second mark — **in both directions**: a **correct** value written incompletely (`13280.2` for `13280.25`) and a **complete** calculation stopped one step short (`0.6`, then `0.60 %`). ⚠️ **Corrected 14 Oct 2026, after the rest of May 2023 was read: the dotted line is a RECOMMENDATION, not a requirement — this series' own 2/2 scripts include one that leaves it blank while the examiner writes *"Although the answer is not on the dotted lines it is correct and therefore gained the two marks available"*, and Paper 2's Q1(e) pair loses its marks to rounding with the answer line involved in neither case *(see `2023-05_P2_One_and_Two_Mark_Set.md`).* Write the final value, at the precision the question names, somewhere the examiner can find it — every time.**
5. **Struck-out work and corrections cost nothing** — the 2/2 script in the last pair carries a visible correction through its own first line.
6. **A 0-mark comment is the only place the examiner says what was not enough.** Mark schemes list what earns; these comments state the rejection reason (*"could relate to any business"* · *"not a definition of"* · *"only the first part"*).

---

# THIS FILE'S PLACE IN THE FINISHED TIER

**Five exemplar sections here cover ten printed scripts — and every one of them is transcribed, because on 14 Oct 2026 the tier closed: all 80 scripts the five reports print are in the bank** *(derived, not typed — `layer_c_1_2mark_coverage.py` reads the reports and the register: **BANKED 80 / REMAIN 0**)*. The other three harvest files are named in `09_`'s 1-mark section.

⚠️ **Two of this file's questions — P2R Q3(c) and P2R Q4(a) — are also set out question by question in `2023-05_P2R_One_and_Two_Mark_Set.md`, which is where the register's rows point.** They appear here because this was the file that first read them, **beside the 1-mark pairs that taught the same lesson on the same pages.**

⚠️ **What this file claimed and the rest of the series corrected:** **item 4 above** — *"the answer on the dotted line is the mark"*. **Paper 2R's Q3(c) 2/2 leaves the line blank and is paid in full, and Paper 2's Q1(e) pair loses its marks to rounding with the answer line involved in neither case.** The rule is the final value at the precision the question names, written where the examiner can find it. **Corrected the same day, in place.**

**Where the rules already live:** `01_Mark_Tariff_Playbook.md:330` (*"'State' questions are AO2… there must be some evidence of application or context"*) · `06_External_Source_Library.md:78` (*"All 'State' questions require candidates to include context"*) · `00_Pearson_Official_Rulebook.md:66` (*"State questions assess AO2"*). **This file adds the scripts those rules were written from — including the ones that lost the mark.**

---

**Sources.** `Paperlords_Archive/IGCSE/4BS1_Business_Studies/May_2023/4BS1_Business_Studies_May_2023_{P2,P2R}_{ER,MS}.pdf`. Report pages as marked above; mark-scheme pages named per question. **Every script above was read from a 200 dpi page render, and every ambiguous glyph (the p6 word, the p44 answer line, the p52 corrected first figure) was re-read from the page's native scan at 4–6× magnification before being written down.**
