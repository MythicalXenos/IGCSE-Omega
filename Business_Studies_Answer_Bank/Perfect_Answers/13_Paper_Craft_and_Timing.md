# Paper craft — the 90 minutes, measured

**Why this file exists:** every technique in this bank is worthless if the paper is not finished.
This file turns the cover page's own instructions into a **clock**, and prices the mistakes that are
about *time* rather than knowledge. Every figure is re-derived by `../verify_paper_craft.py`.

---

## 1. What Pearson actually prints on the cover

Quoted from the June 2024 Paper 1 question paper, page 1 (the wording is identical on all 38
archived papers — the verifier checks the two numbers on every one):

> *"**Time: 1 hour 30 minutes**"*
> *"The total mark for this paper is **80**."*
> *"**The marks for each question are shown in brackets – use this as a guide as to how much time to
> spend on each question.**"*
> *"Answer **all** questions."*
> *"**Try to answer every question.**"*
> *"Calculators may be used."*

> ## 🎯 THE ONE SENTENCE ON THE COVER THAT IS A MARKING INSTRUCTION
> **"Use [the marks] as a guide as to how much time to spend on each question."** Pearson is telling
> you the exchange rate. It is **90 minutes for 80 marks = 1.125 minutes per mark (67.5 seconds)**.

---

## 2. The clock, by question

| Question | Tariff | Time at 67.5 s/mark | Running total |
|---|---|---|---|
| Q1 (a)–(g) | 20 marks | **22½ min** | 22½ |
| Q2 (a)–(f) | 20 marks | **22½ min** | 45 |
| Q3 (a)–(e) | 20 marks | **22½ min** | 67½ |
| Q4 (a)–(c) | 20 marks | **22½ min** | **90** |

At item level, within any question:

| Item | Time |
|---|---|
| 1-mark MCQ / define / state | **~1 min** |
| 2-mark calculate / outline | **~2¼ min** |
| 3-mark explain | **~3½ min** |
| 6-mark analyse | **~6¾ min** |
| 9-mark justify | **~10 min** |
| 12-mark evaluate | **~13½ min** |

> ### ⚠️ THE ARITHMETIC THAT MATTERS
> The twelve 1-mark items and four 2-mark items are **20 marks — a quarter of the paper — and cost
> under 21 minutes**. If you spend 2 minutes on a 1-mark "state" question you are subsidising it with
> marks from the 12-marker: **five minutes lost there is five minutes off Q4(c).**
>
> **The 9- and 12-markers are 30 marks between them and need nearly 34 minutes.** They are the only
> questions where the clock is a real constraint, and they are the ones candidates reach last.

---

## 3. The plan the bank recommends (this is the bank's method, not Pearson's)

- **0:00–0:03** — read the Q1 case, then answer Q1 in order. Do **not** read the whole paper first;
  the cases are independent and you will not remember the last one anyway.
- **Keep the running totals above.** If you are past **45 minutes at the end of Q2**, you are behind —
  stop writing long answers to 2- and 3-mark questions and move.
- **Leave 5 minutes**: aim to finish Q4(c) at **85 minutes**, not 90. The reserve is for the things
  that are cheap and certain — see §4.
- **Do not go back to "improve" a 3-marker.** A 3-mark explain at 2/3 is worth one mark; the same
  minute spent checking a calculation is worth one mark *and* you already did the work.

---

## 4. Where five spare minutes buy the most

| Ranked action | Why it is worth doing | Evidence |
|---|---|---|
| **1. Check every calculation's decimal places and units** | A correct answer rounded to the wrong d.p. **loses the mark**, and the examiner says so in as many words | June 2024 P1R Q3(c): *"provided their final answer to one decimal place so therefore cannot access the full marks"* |
| **2. Check every "state" answer has one piece of context** | 1 mark each, 12 of them; *"Just one piece of context will suffice"* | June 2024 P1 Q2(a): a correct answer scored **0** for lack of context |
| **3. Check the 12-marker has a decision, and says what it depends on** | the only place 3 AO4 marks sit together | `12_Grade_9_Marks_Budget.md` §4 |
| **4. Check nothing is blank** | a blank 12-marker is 15% of the paper; *"Try to answer every question"* | the cover page |

---

## 5. Two facts from marked scripts that change how you use the space

1. **You may write past the printed lines.** The 11/12 on June 2025 P1R Q4(c) finishes its conclusion
   **below the paper's own "TOTAL FOR PAPER = 80 MARKS" banner**, and the 8/9 on Q2(f) writes through
   *"(Total for Question 2 = 20 marks)"*. **Both were marked.** No rule of the paper stops you
   continuing on the ruled space beneath the line.
2. **Longer is not better, and the strongest 6-mark in this bank is short.** The verified **6/6** on
   June 2025 P1R Q3(d) is **two short paragraphs with no conclusion**. A 6-mark Analyse has **no AO4
   marks at all**, so there is nothing for a conclusion to earn.

---

## 6. What the clock does *not* excuse

Three faults in `03_Calibration_Below_Full_Marks.md` happened *because* the candidate was rushing, and
all three cost more than the time they saved:

| Fault | Cost | What it saved |
|---|---|---|
| answering the question that was **not** asked (CCT Q2(f): "measure success" read as "choose an option") | **9 marks** | seconds |
| a conclusion that **restates** instead of deciding | **1 mark** | a sentence |
| a 12-marker conclusion that decides but names **no condition** | **1 mark** | a clause |

> **A five-second re-read of the stem is the highest-return action available in the exam hall.** The
> single largest documented loss in this archive — nine marks — was not a knowledge failure, a timing
> failure or a writing failure. It was a **reading** failure.

---

*Checked by `../verify_paper_craft.py`: 38 of 38 archived question papers print **1 hour 30 minutes**
and **80 marks**, the time-per-mark arithmetic is re-derived, and the per-question running totals sum
to 90 minutes.*
