# 09 — THE VERIFIED REGISTER

**One row per distinct FULL-MARK script.** The bank previously carried hand-written totals — *"the bank now holds six 9/9s"* above a list of fourteen, and a coverage table labelled *"6 × 9/9"* above eight names. **Both were wrong.**

A hand-written total is an assertion; a register is evidence. Rebuild the audit at any time:

```bash
cd Business_Studies_Answer_Bank
python3 tally_exemplars.py        # exit 0 = the register verifies, exit 1 = it does not
```

> ### 🔬 WHAT THAT SCRIPT ACTUALLY DOES — and why it was rewritten
> **It parses this file's own tables and checks them**, rather than counting prose:
>
> 1. **Every register row must resolve** — the file exists and the line it names carries the mark, in figures (`6/6`) or in words (*"Level 3 – 6 marks — FULL MARKS"*). ✅ **All 148 rows resolve.** ⚠️ **The 1- and 2-mark sections joined on 14 Oct 2026 and are verified by the same code** — the figure pattern is derived from each row's own tariff, so a `1/1` row is checked for a `1/1`, not for a `3/3`.
> 2. **It then scans the whole bank for script-bearing headings** — a heading that names a question label (`Q2(f)`) or one of the register's case studies — and checks each one against the register. ✅ **66 matched, 36 narrative, 0 unaccounted.**
> 3. **And it checks that the file a row cites belongs to the session the row names** — because until 14 Oct 2026 nothing did. A probe asked what would happen if a row reading *"Jun 2024"* pointed into a `2023-05` file: `tally_exemplars.py` was silent, `verify_coverage_claims.py` was silent, `verify_paper_coverage.py` was silent — **only the new check 23 noticed, and it reads five reports.** So a row may no longer cite across sessions: the month in the filename must be the month the row names, **with May and June deliberately treated as the same series** (Pearson's one May/June sitting; the archive folders say May, the register says Jun — a stricter rule reported 14 false alarms, all in the May 2023 files). **A row that states a paper must also cite a script sitting under that paper's own `# PAPER n` section**, which is checked wherever the cited file sections its scripts by paper. **Both rules sabotage-tested: one flipped session or one flipped paper fails the run; renaming the row's session to the file's May passes.** ⚠️ **The counts are printed — *"rows whose session was checked against a dated filename: 69"* — because a rule that silently checks nothing is this bank's oldest failure mode, and the session rule only fires where the filename carries a date.**
>
> 4. **Everything else is filtered out as narrative.** That is the restatement filter: a rule section called *"THE 9/9 JUSTIFY — six required features"* **is not a script**, and a cross-reference to a transcript held in another file **is not a second script**.
>
> ⚠️ **The previous version of this script counted headings, and printed 17 / 14 / 4 against this register's 19 / 15 / 2** — it counted rule sections, cross-references and repeats. **A total that is wrong in a new way each time it is run is not evidence either.** The rewrite is why the rule above exists: **if this script and this table ever disagree, the script says so in the exit code and prints the offending heading.**
>
> **Two genuine defects came out of the first run of the rewritten script, both in this file:** the June 2019 canonical sources were written as `2023-05_Series…md` — **a truncated filename with an ellipsis, which resolves to nothing** — and two rows pointed at headings that state the mark in words. **Both fixed; the filenames are now exact.**

---

## HEADLINE COUNT

| Tariff | Distinct scripts |
|---|---|
| **12-mark Evaluate** | **2** |
| **9-mark Justify** | **15** |
| **6-mark Analyse** | **25** |
| **3-mark Explain** | **47** *(Jun 2019 ×3 · Jun 2022 ×10 · Jun 2023 ×16 · Jun 2024 ×8 · Jun 2025 ×6 · Jun 2026 ×4)* |
| **1-mark items** | **36** *(May/Jun 2023 ×24 — **P2 ×6** · **P1R ×6 · P1 ×6** · Jun 2026 ×6 · Jun 2024 ×6)* |
| **2-mark items** | **23** *(May/Jun 2023 ×16 — **P2 ×4** · **P2R ×4** · **P1R ×4 · P1 ×4** · Jun 2026 ×4 · Jun 2024 ×3)* |
| **TOTAL** | **148** *(the four governed tiers = **89**; the rest are the 1- and 2-mark script pairs the reports print)* |

> ### ⚠️ THIS TABLE DRIFTED, AND THE CHECK NOW MAKES THAT IMPOSSIBLE
> On **14 Oct 2026** this table said **6-mark = 19** while the section below it held **23**, and it had **no 3-mark row at all** — the June 2026 P1R tier had been added to the body of the file without the summary following it. **The prose above said *"All 36 rows resolve"* against 44 rows.**
>
> **`tally_exemplars.py` now reads this table, every section heading, and that prose sentence, and fails if any stated total disagrees with the rows that back it.** The register was created *because* hand-incremented totals had drifted five times; **its own headline had become the sixth place, which is why the check reads the file's summaries and not only its rows.**
>
> ### 🚨 AND ON THE SAME DAY IT DRIFTED AGAIN, IN THE OPPOSITE DIRECTION — the 3-mark row said **4** when the bank held **32**
> **Six sessions of verified 3/3s sat in the harvest files, fully transcribed, uncounted.** The section had been written for the June 2026 batch, and nothing compared it with what the older files said they held. **Worse: the check reported *0 unaccounted*, because it matched headings to rows on (tariff, question) — and `2022-06_P1_TBTS.md` Q2(c) matched the June 2026 P1R row for Q2(c).** A paper-blind key again. **Both failures are now impossible: the row count is derived from the rows, and a heading must be cited by its OWN row, within eight lines, or the run fails.** **Three of them were found within the hour, by sweeping the May 2023 reports for the string `scored 3 marks` rather than for a level phrasing — see `2023-05_Series_3mark_Sweep.md`.**
>
> ### 🚨 THEN THE SAME TECHNIQUE TURNED UP ELEVEN MORE — AND EVERY SWEEP THE BANK OWNED HAD MISSED THEM
> **`audit_er_fullmarks.py` asked the five archived reports a question every one of them can answer — *which scripts did you award full marks to?* — and compared the answers with this register.** **Thirty-three printed full-mark scripts; 22 banked; 11 never read.** Nine 3/3 Explain and two 6/6 Analyse, all May 2023 — including the clearest 6/6 the bank holds (`Irsi Chocolatier`, P1 Q3(d), *"context throughout… interconnected points with logical chains of reasoning"*). **They were invisible for a phrasing reason and a layout reason:** every sweep searched for a *level* phrasing (*"This response **is** a Level 3"*, *"gained a Level 3"*) while May 2023 states it as **`This response scored N marks.`** — **a fourth phrasing no catalogue held** — and in those reports the score line and commentary sit at the **foot of the page BEFORE the script**, so P1 Q3(d) runs across pages 27–28 and P2 Q2(e) across 31–32.
>
> **All eleven are transcribed in full — question, mark scheme, script and examiner comment — in `External_Exemplars/2023-05_Series_Remaining_FullMarks.md`.** **Run the same guard one day later and IT was hiding fourteen** — `audit_er_fullmarks.py`'s score grammar knew two phrasings and the May 2023 Paper 2/2R reports use five, **so the guard built to catch a missed phrasing had one of its own** (four full-mark scripts invisible; all four already banked, so the corrected count is **37 printed / 37 banked**). **The grammar is now enumerated from the corpus and cross-examined by an oracle — see `08_`.** With them the register reads **44 · 25 · 15 · 2 = 86**, and `audit_er_fullmarks.py` is now **check 23**: it fails the run if any printed full-mark script is missing from the register. **The full account is in the 3-mark section below and in `08_`.**

> ### ⚠️ WHAT THIS TABLE COUNTS — AND WHAT IT DOES NOT
> **It counts scripts Pearson printed with FULL marks against them** — 86 of them, across four tiers and every session from June 2019 to June 2026. **Four of the 44 three-mark rows are held as the report's own single-sentence quotation rather than as a full exemplar section** (marked `*` in that section), which is a note about how they are held, not about what they are worth: for a 3-mark Explain the whole answer is one sentence.
>
> **It counts scripts Pearson printed with FULL marks against them.** A script the report itself scores at **11/12** is not a row here, and neither is a **6/12** or a **10/12** — **they are held instead in `03_Calibration_Below_Full_Marks.md` and in the 12-mark section of `02_Verified_Exemplars.md`, which is where their examiner comments teach the most.** The best of them — **Spud Bros, June 2026 P1R Q4(c), 11/12** — is called *"the best 12-mark model in the bank"* in `02_` for the reason that matters: **it is the closest thing to a full-mark 12-mark answer the bank owns, and it is the one Pearson printed with a conclusion.**

---

## 12 MARKS — **2 scripts**

| # | Series | P · Q | Case study | Canonical source |
|---|---|---|---|---|
| 1 | **Jun 2024** | P1 Q4(c) | PPS | `02_Verified_Exemplars.md:938` |
| 2 | **May/Jun 2023** | P1 Q4(c) | Irsi Chocolatier | `External_Exemplars/2023-05_Series_Irsi_AudeRose_IKEA_MM.md:17` |

> ### ⚠️ PERMANENT LIMITATION — BOTH ARE PAPER 1
> **No verified 12/12 exists for Paper 2 or Paper 2R, in any series.** Pearson names the **June 2022** and **June 2024 Paper 1** reports as its 12-mark exemplar sources, and both are harvested. **This is the edge of what is published, not a gap in the search.** **The best held on those two papers is a verified 10/12 on each — IKEA (P2 Q4(c), May 2023) and M&M (P2R Q4(c), May 2023); both were docked for *"limited judgements"*.**

---

## 9 MARKS — **15 scripts**

| # | Series | P · Q | The choice being made | Canonical source |
|---|---|---|---|---|
| 1 | **Jun 2019** | P1 Q3(e) | crowdfunding vs overdraft — *Backyard Shoez* | `02_Verified_Exemplars.md:471` |
| 2 | **Jun 2022** | P1 Q2(f) | retained profit vs bank loan — *TBTS* | `2022-06_P1_TBTS.md:168` |
| 3 | **Jun 2022** | P1 Q3(e) | questionnaires vs focus groups — *TBTS* | `2022-06_P1_TBTS.md:188` |
| 4 | **Jun 2022** | P1R Q2(f) | advertising vs open for breakfast — *Can Culleretes* | `2022-06_P1R_Can_Culleretes.md:57` |
| 5 | **Jun 2022** | P1R Q3(e) | permanent vs temporary contract — *Can Culleretes* | `2022-06_P1R_Can_Culleretes.md:82` |
| 6 | **May/Jun 2023** | P1 Q2(f) | job vs batch production — *Irsi* | `External_Exemplars/2023-05_Series_Irsi_AudeRose_IKEA_MM.md:382` |
| 7 | **May/Jun 2023** | P1 Q3(e) | on-the-job vs off-the-job training — *Irsi* | `External_Exemplars/2023-05_Series_Irsi_AudeRose_IKEA_MM.md:399` |
| 8 | **May/Jun 2023** | P1R Q2(f) | sponsor a flower show vs leaflets — *Aude Rose* | `External_Exemplars/2023-05_Series_Irsi_AudeRose_IKEA_MM.md:409` |
| 9 | **May/Jun 2023** | P1R Q3(e) | questionnaires vs internet — *Aude Rose* | `External_Exemplars/2023-05_Series_Irsi_AudeRose_IKEA_MM.md:417` |
| 10 | **May/Jun 2023** | **P2R Q3(e)** | job rotation vs bonus — *M&M* | `External_Exemplars/2023-05_Series_Irsi_AudeRose_IKEA_MM.md:425` |
| 11 | **Jun 2024** | P1 Q2(f) | — *PPS* | `2024-06_P1_PPS.md:60` |
| 12 | **Jun 2024** | P1 Q3(e) | — *PPS* | `2024-06_P1_PPS.md:79` |
| 13 | **Jun 2024** | P1R Q2(f) | vegan range vs discount — *Café Pinch* | `2024-06_P1R_Cafe_Pinch.md:9` |
| 14 | **Jun 2024** | P1R Q3(e) | communication methods — *Café Pinch* | `2024-06_P1R_Cafe_Pinch.md:24` |
| 15 | **Jun 2025** | **P2R Q2(f)** | weekly meetings vs email — *Rabanne* | `02_Verified_Exemplars.md:840` |

> ### ⭐ TWO OF THE FIFTEEN ARE **PAPER 2R**. AND **NO VERIFIED 9/9 EXISTS FOR PAPER 2, IN ANY SERIES**
> Entries **10** and **15** are the only full-mark Justify scripts the bank holds from an R-paper's second paper. The full split is **P1 ×7 · P1R ×6 · P2R ×2 · P2 ×0** — and **Paper 2's ceiling in the bank is a 7/9**, held at `2023-05_Series_Irsi_AudeRose_IKEA_MM.md:168` and dissected at `:300`.
>
> ✅ **Two independent counts agree, and the second cannot be affected by what the bank chooses to keep.** The register holds **fifteen** 9/9s and not one of them is Paper 2; and the five archived reports print exactly **five** 9/9 mark statements — **2023 P1 ×4** (report pp. 16, 22, 26, 30) and **2023 P2R ×1** (p. 39) — with **none on Paper 2**. Paper 2 prints only **three** 9-mark statements at all: **5/9 · 7/9 · 5/9**. ⚠️ **So the 7/9 (report p. 33) is the highest Paper 2 Justify script the qualifications entire held reporting prints** — which is why `:300` dissects it in full. For Paper 2 it is the *ceiling of official evidence*, not merely a near-miss.
>
> ### ⭐ AND FIVE COME FROM ONE SERIES
> May/June 2023 alone printed **five** 9/9 Justify answers — entries 6–10. The bank previously recorded this as **four**, because the fifth (a Paper 2R script) was filed in a different section of the report.

---

## 6 MARKS — **25 scripts**

| # | Series | P · Q | Topic | Canonical source |
|---|---|---|---|---|
| 1 | **Jun 2019** | P1 Q1(g) | satisfying customer needs | `02_Verified_Exemplars.md:314` |
| 2 | **Jun 2019** | P1 Q4(b) | usefulness of profitability ratios | `02_Verified_Exemplars.md:350` |
| 3 | **Jun 2019** | P1R Q1(g) | customer satisfaction | `2019-06_P1_Official_Exemplar_Booklet.md:513` |
| 4 | **Jun 2022** | P1 Q1(g) | external factors — *TBTS* | `2022-06_P1_TBTS.md:25` |
| 5 | **Jun 2022** | P1 Q3(d) | motivating employees — *TBTS* | `2022-06_P1_TBTS.md:50` |
| 6 | **Jun 2022** | P1R Q1(g) | impact of technology — *Can Culleretes* | `2022-06_P1R_Can_Culleretes.md:114` |
| 7 | **Jun 2022** | P1R Q3(d) | social media reviews — *Can Culleretes* | `2022-06_P1R_Can_Culleretes.md:141` |
| 8 | **Jun 2022** | P2R Q1(g) | two location factors, **43 words** — *Cadbury* | `2022-06_P2R_Cadbury.md:170` |
| 9 | **May/Jun 2023** | P1 Q1(g) | branding — *Irsi* | `External_Exemplars/2023-05_Series_Irsi_AudeRose_IKEA_MM.md:253` |
| 10 | **May/Jun 2023** | P1 Q4(b) | place — *Irsi* | `External_Exemplars/2023-05_Series_Irsi_AudeRose_IKEA_MM.md:262` |
| 11 | **May/Jun 2023** | P1R Q4(b) | measuring success — *Aude Rose* | `External_Exemplars/2023-05_Series_Irsi_AudeRose_IKEA_MM.md:272` |
| 12 | **May/Jun 2023** | P1R Q3(d) | retained profits as finance — *Aude Rose* | `2023-06_P1R_Aude_Rose.md:52` |
| 13 | **May/Jun 2023** | P2 Q3(d) | shortlisting — *IKEA* | `External_Exemplars/2023-05_Series_Irsi_AudeRose_IKEA_MM.md:327` |
| 14 | **Jun 2024** | P1 Q1(g) | — *PPS* | `2024-06_P1_PPS.md:32` |
| 15 | **Jun 2024** | P1 Q3(d) | — *PPS* | `2024-06_P1_PPS.md:47` |
| 16 | **Jun 2024** | P1R Q3(d) | — *Café Pinch* | `2024-06_P1R_Cafe_Pinch.md:65` |
| 17 | **Jun 2025** | P1 Q1(g) | **wide span of control — ONE point, 140 words** — *Four Fitness* | `02_Verified_Exemplars.md:879` |
| 18 | **Jun 2025** | P1R Q1(g) | app concerns — *CCT* | `02_Verified_Exemplars.md:441` |
| 19 | **Jun 2025** | P2 Q1(g) | batch production, two paragraphs ≈100 words as scanned — *Starbucks* *(question number corrected 9 Nov 2026: the paper prints batch production at **1(g)**, and 2(c) is the 3-mark JIT question)* | `02_Verified_Exemplars.md:426` |
| 20 | **May/Jun 2023** | **P2R Q3(d)** | comparing itself with other manufacturers — *M&M* | `External_Exemplars/2023-05_Series_Irsi_AudeRose_IKEA_MM.md:528` |
| 21 | **May/Jun 2023** | **P2R Q4(b)** | continuing to plant trees — *M&M* | `External_Exemplars/2023-05_Series_Irsi_AudeRose_IKEA_MM.md:541` |
| 22 | **Jun 2026** | P1R Q1(g) | sponsorship disadvantages — *Spud Bros* | `External_Exemplars/2026-06_P1R_SpudBros.md:319` |
| 23 | **Jun 2026** | P1R Q3(d) | viral advertising — *Spud Bros* | `External_Exemplars/2026-06_P1R_SpudBros.md:332` |
| 24 | **Jun 2023** | P1 Q3(d) | limitations of break-even charts — *Irsi Chocolatier* *(banked 14 Oct 2026 — `audit_er_fullmarks.py`)* | `External_Exemplars/2023-05_Series_Remaining_FullMarks.md:89` |
| 25 | **Jun 2023** | P1R Q1(g) | motivating employees — *Aude Rose* *(banked 14 Oct 2026 — `audit_er_fullmarks.py`)* | `External_Exemplars/2023-05_Series_Remaining_FullMarks.md:138` |

> ### ✅ THE ONE OPEN AMBIGUITY — CLOSED, 14 Oct 2026
> The June 2019 booklets' own coverage table claimed **"6/6 × 4"** across both booklets while only **three** were enumerated above. **A fourth appeared to be missing, and the count was therefore carried as "19 confirmed, possibly 20".**
>
> **There is no fourth.** The booklets' headings give exactly **6/6 ×3** — Backyard Shoez Q1(g), Backyard Shoez Q4(b) and Lavender Q1(g) — and **the same table was wrong in three other places too** (it claimed `9/9 ×2` for June 2019 where there is **one**, `9` Explain exemplars where there are **8**, and `6/6 ×4` where there are **three**).
>
> ✅ **So: 19, confirmed. Not "possibly 20".** *(The register has since grown to **23** — two May 2023 Paper 2R scripts (rows 20–21, found by the Level-phrasing sweep) and two June 2026 Paper 1R scripts (rows 22–23, whose scripts had been recorded as verdicts but never rendered). Both growths are recorded in `08_Completion_Map.md`.)* Verify with `python3 audit_exemplar_marks.py --all-2019`, which derives the distribution from the booklet headings themselves — **or read the correction block in `2019-06_P1_Official_Exemplar_Booklet.md`.** **The generalisable lesson: when a total disagrees with its own list, count the list. The total was typed by hand.**

---

## 3 MARKS — **47 scripts** *(Jun 2019 ×3 · Jun 2022 ×10 · Jun 2023 ×16 · Jun 2024 ×8 · Jun 2025 ×6 · Jun 2026 ×4)*

| # | Series | P · Q | Topic | Canonical source |
|---|---|---|---|---|
| 1 | **Jun 2019** | P1 Q1(f) | increase gross profit margin — *Backyard Shoez* | `02_Verified_Exemplars.md:178` |
| 2 | **Jun 2019** | P1 Q2(d) | above-the-line promotion (television) | `02_Verified_Exemplars.md:204` |
| 3 | **Jun 2019** | P2 Q1(f) | impact of technology on production | `External_Exemplars/2019-06_P2_Official_Exemplar_Booklet.md:70` |
| 4 | **Jun 2022** | P1 Q2(c) | benefit of a flat structure — *TBTS* | `External_Exemplars/2022-06_P1_TBTS.md:78` |
| 5 | **Jun 2022** | P1 Q2(d) | a method to increase profit — *TBTS* | `External_Exemplars/2022-06_P1_TBTS.md:98` |
| 6 | **Jun 2022** | P1R Q2(c) | a method to encourage repeat purchase — *Can Culleretes* | `External_Exemplars/2022-06_P1R_Can_Culleretes.md:163` |
| 7 | **Jun 2022** | P1R Q2(e) | a benefit of motivating employees — *Can Culleretes* | `External_Exemplars/2022-06_P1R_Can_Culleretes.md:172` |
| 8 | **Jun 2022** | P2R Q1(f) | a fall in banks' interest rates | `02_Verified_Exemplars.md:227` |
| 9 | **Jun 2022** | P2R Q2(c) | non-financial methods of motivation | `02_Verified_Exemplars.md:244` |
| 10 | **Jun 2022** | P2R Q2(d) | fully trained employees — mistakes and quality | `02_Verified_Exemplars.md:251` |
| 11 | **Jun 2022** | P2R Q2(d) | fully trained employees — safety risks | `02_Verified_Exemplars.md:253` |
| 12 | **Jun 2022** | P2R Q2(e) | Kaizen — employee loyalty | `02_Verified_Exemplars.md:259` |
| 13 | **Jun 2022** | P2R Q2(e) | Kaizen — improve the product | `02_Verified_Exemplars.md:261` |
| 14 | **Jun 2023** | P2 Q1(f) | using resources effectively — *IKEA* | `External_Exemplars/2023-06_P2_IKEA.md:110` |
| 15 | **Jun 2023** | P2 Q2(c) | cash flow forecasting — *IKEA* (first) | `External_Exemplars/2023-06_P2_IKEA.md:134` |
| 16 | **Jun 2023** | P2 Q2(c) | cash flow forecasting — *IKEA* (second) | `External_Exemplars/2023-06_P2_IKEA.md:137` |
| 17 | **Jun 2023** | P2 Q2(d) | diseconomies of scale — *IKEA* | `External_Exemplars/2023-06_P2_IKEA.md:157` |
| 18 | **Jun 2024** | P1 Q2(c) | ineffective communication — *PPS* | `External_Exemplars/2024-06_P1_PPS.md:9` |
| 19 | **Jun 2024** | P1 Q2(d) | adapting to local tastes — *PPS* | `External_Exemplars/2024-06_P1_PPS.md:23` |
| 20 | **Jun 2024** | P2 Q2(d) | short layers in the hierarchy — *TUI* | `External_Exemplars/2024-06_P2_TUI.md:9` |
| 21 | **Jun 2024** | P2 Q2(e) | hours required, in a job advert — *TUI* | `External_Exemplars/2024-06_P2_TUI.md:33` |
| 22 | **Jun 2024** | P2 Q2(e) | salary information, in a job advert — *TUI* | `External_Exemplars/2024-06_P2_TUI.md:39` |
| 23 | **Jun 2025** | P1R Q1(f) | limited liability — *CCT* | `External_Exemplars/2025-06_Second_Pass_Addendum.md:128` |
| 24 | **Jun 2025** | P1R Q2(d) | a reason for tariffs on imports * | `External_Exemplars/2025-06_Second_Pass_Addendum.md:144` |
| 25 | **Jun 2025** | P1R Q2(e) | why quality control is important * | `External_Exemplars/2025-06_Second_Pass_Addendum.md:145` |
| 26 | **Jun 2025** | P2 Q1(f) | a disadvantage of training employees | `02_Verified_Exemplars.md:280` |
| 27 | **Jun 2025** | P2 Q2(d) | a problem of poor communication * | `External_Exemplars/2025-06_Second_Pass_Addendum.md:147` |
| 28 | **Jun 2025** | P2R Q2(e) | how the statement of comprehensive income helps * | `External_Exemplars/2025-06_Second_Pass_Addendum.md:148` |
| 29 | **Jun 2026** | P1R Q1(f) | flat organisational structure — *Spud Bros* | `External_Exemplars/2026-06_P1R_SpudBros.md:369` |
| 30 | **Jun 2026** | P1R Q2(c) | why break-even output is calculated — *Spud Bros* | `External_Exemplars/2026-06_P1R_SpudBros.md:381` |
| 31 | **Jun 2026** | P1R Q2(d) | segmenting the market by income — *Spud Bros* | `External_Exemplars/2026-06_P1R_SpudBros.md:393` |
| 32 | **Jun 2026** | P1R Q2(e) | benefit of productivity improvements — *Spud Bros* | `External_Exemplars/2026-06_P1R_SpudBros.md:405` |
| 33 | **Jun 2023** | P1 Q1(f) | benefit of test marketing *(added 14 Oct 2026 — third sweep)* | `External_Exemplars/2023-05_Series_3mark_Sweep.md:13` |
| 34 | **Jun 2023** | P1R Q1(f) | why a business might fail *(added 14 Oct 2026 — third sweep)* | `External_Exemplars/2023-05_Series_3mark_Sweep.md:37` |
| 35 | **Jun 2023** | P1R Q2(c) | an impact of ineffective communication *(added 14 Oct 2026 — third sweep)* | `External_Exemplars/2023-05_Series_3mark_Sweep.md:65` |
| 36 | **Jun 2023** | P1 Q2(c) | a way a business could use e-newsletters *(banked 14 Oct 2026 — `audit_er_fullmarks.py`)* | `External_Exemplars/2023-05_Series_Remaining_FullMarks.md:15` |
| 37 | **Jun 2023** | P1 Q2(d) | a way a business could use market research information *(banked 14 Oct 2026 — `audit_er_fullmarks.py`)* | `External_Exemplars/2023-05_Series_Remaining_FullMarks.md:37` |
| 38 | **Jun 2023** | P1 Q2(e) | a benefit of a decentralised structure *(banked 14 Oct 2026 — `audit_er_fullmarks.py`)* | `External_Exemplars/2023-05_Series_Remaining_FullMarks.md:63` |
| 39 | **Jun 2023** | P1R Q2(d) | an advantage of a partnership *(banked 14 Oct 2026 — `audit_er_fullmarks.py`)* | `External_Exemplars/2023-05_Series_Remaining_FullMarks.md:173` |
| 40 | **Jun 2023** | P1R Q2(e) | a disadvantage of product orientation *(banked 14 Oct 2026 — `audit_er_fullmarks.py`)* | `External_Exemplars/2023-05_Series_Remaining_FullMarks.md:203` |
| 41 | **Jun 2023** | P2 Q2(e) | why businesses continually design new products *(banked 14 Oct 2026 — `audit_er_fullmarks.py`)* | `External_Exemplars/2023-05_Series_Remaining_FullMarks.md:231` |
| 42 | **Jun 2023** | P2R Q1(f) | an advantage of becoming a multinational *(banked 14 Oct 2026 — `audit_er_fullmarks.py`)* | `External_Exemplars/2023-05_Series_Remaining_FullMarks.md:262` |
| 43 | **Jun 2023** | P2R Q2(c) | why branding is important *(banked 14 Oct 2026 — `audit_er_fullmarks.py`)* | `External_Exemplars/2023-05_Series_Remaining_FullMarks.md:296` |
| 44 | **Jun 2023** | P2R Q2(e) | why businesses maintain product quality *(banked 14 Oct 2026 — `audit_er_fullmarks.py`)* | `External_Exemplars/2023-05_Series_Remaining_FullMarks.md:325` |
| 45 | **Jun 2024** | P2R Q2(c) | one advantage to a country of being in a trading bloc — *Jimmy Choo* **(1/3 and 3/3)** *(banked 16 Oct 2026 — the report found by reading the bank's own harvest queue)* | `External_Exemplars/2024-06_P2R_Jimmy_Choo.md:148` |
| 46 | **Jun 2024** | P2R Q2(d) | one way businesses support employees with disabilities — *Jimmy Choo* **(2/3 and 3/3)** *(banked 16 Oct 2026)* | `External_Exemplars/2024-06_P2R_Jimmy_Choo.md:161` |
| 47 | **Jun 2024** | P2R Q2(e) | one impact of an increase in interest rates — *Jimmy Choo* **(2/3 and 3/3)** *(banked 16 Oct 2026)* | `External_Exemplars/2024-06_P2R_Jimmy_Choo.md:177` |

**`*` = held as the report's own one-sentence quotation inside a summary table**, rather than transcribed in a dedicated exemplar section. The mark is stated by the report and the response is complete as printed — **for a 3-mark Explain, the whole answer is one sentence** — but the register marks the difference so a reader can audit the hold. **28 of the 32 are full exemplar sections; 4 are single-sentence holds.**

> ### 🚨 31 OF THESE 35 ROWS DID NOT EXIST UNTIL 14 OCT 2026 — the register held FOUR
> **The section was created for the June 2026 batch and the earlier harvests' 3/3s were never carried over.** **Twenty-eight were recovered from the existing transcripts, and three more from a sweep of the May 2023 reports (rows 33–35).** They were in the bank all along, fully transcribed, with examiner comments:
>
> * **`2022-06_P1_TBTS.md` states in its own summary table: *"Verified 3/3 exemplars — 2 (Q2(c), Q2(d))"*; `2022-06_P1R_Can_Culleretes.md` the same for its two; `2023-06_P2_IKEA.md` says *"4 (Q1(f), Q2(c) ×2, Q2(d))"*.** Three files said how many they held and nothing compared it with the register.
> * **`02_Verified_Exemplars.md` holds six more from June 2022 P2R under its "2/3 vs 3/3 pairs" heading**, and two June 2019 P1 3/3s.
>
> **Why every check passed anyway — the failure was paper-BLIND.** `tally_exemplars.py` matched a heading to a register row on **(tariff, question label)**: `3/3` + `Q2(c)`. The register's June 2026 rows supplied exactly those keys, so **`2022-06_P1_TBTS.md:78` — a June 2022 Paper 1 answer — was "matched" by the June 2026 P1R row for Q2(c), a different paper two years later.** Thirteen uncounted scripts resolved to four registered rows and the check reported *0 unaccounted*.
>
> **This is the paper-blind key failure the bank had already recorded once** (`verify_coverage_claims.py`'s `TIER_LABELS`, where a P1R heading was satisfied by a P1 row) — **and it took the same correction twice, in two different checks.**
>
> **The rule that now prevents it:** a heading that states a full mark must be **CITED BY ITS OWN ROW** — the register row's `file:line` must fall within eight lines of that heading. A (tariff, question) coincidence is no longer enough, because a citation is a location and a label is not. `tally_exemplars.py` fails the run and names every uncited heading.

> ### ⭐ THE JUNE 2026 FOUR, AND THE ONE THING THAT MAKES THEM DIFFERENT
> The four Spud Bros scripts each have **their 0/3 counterpart printed on the facing page**, with the examiner's comment for both — **the only place in the bank where a full-mark 3-marker and a zero on the same question sit side by side.** That is what made them the source of **rule 126** (a 0/3 is a missing mechanism, not a short answer) and of `verify_model_shape.py`'s 3-mark check. **Six other sessions hold 3/3s; none of them prints the zero beside them.**

> ### ⚠️ THE 3-MARK TIER HAS NO PAPER-LEVEL GRID CELL, ON PURPOSE
> `06_`'s coverage grid is per-paper for the 6-, 9- and 12-mark tiers, where a paper-level cell is meaningful. An Explain exemplar is a *technique* example: every one of the 32 is a three-link chain, and the tier is covered as a technique rather than paper by paper. **They are counted here, and cited by every stated 3-mark total in the bank.**

---

## WHAT THIS REGISTER REPLACED

| Location | Claimed | Truth |
|---|---|---|
| `02_Verified_Exemplars.md` | 9/9 = **6**, then **7** | **15** |
| `02_Verified_Exemplars.md:767` | *"May 2023 printed **four** full-mark Justify answers"* | **five** |
| `08_Completion_Map.md:95` | *"**6 × 9/9**"* above **eight** names | **15** |
| `08_Completion_Map.md:94` | *"**9 × 6/6**"* | **19** |
| `02_Verified_Exemplars.md` | *"five verbatim 9/9 Justify scripts"* | **15** |
| — | 12/12 = 2 | **2** ✅ *the only count that was ever right* |

> ## 🚨 WHY THIS HAPPENED — and the rule that stops it
> Totals were **hand-incremented** each time an exemplar was found, while the lists beside them grew by transcription. **The two drifted apart, in five separate places.**
>
> **Rule: never carry a running total by hand.** Where a number appears in prose it must be **re-derivable** from `tally_exemplars.py`, or attributable to a specific line in a register like this one.

---

## THE DUPLICATE-FILE QUESTION — RESOLVED

The bank carried an open task: *"`2023-06_P1R_Aude_Rose.md` and `2023-06_P2_IKEA.md` are duplicates of `2023-05_Series_*.md`."* **That was half right, and the half that was wrong mattered.**

**First, the underlying fact:** *"May 2023"* and *"June 2023"* are **the same exam series** — papers sat in May, reports published in August. So all three files describe **one series**.

| File | Verdict | Action taken |
|---|---|---|
| **`2023-06_P2_IKEA.md`** | ✅ **NOT a duplicate.** Covers Paper 2 **Q1–Q2** (defines, states, explains, the 0/6 and 3/6 Analyse on franchising). The series file covers **Q3(d)–Q4(b)**. **Different questions from the same report.** | **Kept, annotated as complementary.** Deleting it would have destroyed unique content. |
| **`2023-06_P1R_Aude_Rose.md`** | ⚠️ **PARTIAL duplicate.** Its two 9/9s (Q2(f), Q3(e)) are the same scripts as the series file's. But its **6/6 Q3(d), 2/2 Q3(b)**, define and calculation content is **unique**. | **Kept; the two duplicated headings stubbed and marked `not counted`.** `tally_exemplars.py` now skips them. |

> ### 🚨 THE LESSON
> **A "duplicate file" flag is a hypothesis, not a finding.** Had these been deleted on the strength of the note, the bank would have lost four unique entries — including a verified 6/6 (entry 12 above) and a 2/2 Outline. **Check the question numbers before merging or deleting anything.**

---

## HOW TO READ A NUMBER IN THIS BANK

| Kind of number | Trust it? |
|---|---|
| **A row in this register** | ✅ Yes — cites a file and line |
| **Output of `tally_exemplars.py`** | ✅ Yes — re-runnable |
| **A mark quoted verbatim from a Pearson report** | ✅ Yes — but confirm it is a *mark*, not a *level* |
| **A hand-written running total** | ❌ **Assume wrong until re-derived** |
| **A coverage table's "×N" column** | ⚠️ Compare it against its own list before believing it — this is where all five errors were |

---

## 1 MARK SCRIPTS — printed in full, and the only place a 0 is explained

> ### ⭐ THE TABLES NOW CARRY TWO KINDS OF SOURCE — read the row's own note if it matters
> **The June 2023 and June 2026 rows come from reports held on disk in the archive.** **The nine June 2024 P2R rows (§1 ×6 · §2 ×3) were added 16 Oct 2026 from a web-harvested report** — `External_Exemplars/2024-06_P2R_Jimmy_Choo.md`, which transcribes the scripts from the fetcher's own reading of the published PDF. **Both are printings by Pearson; the distinction is only whether the PDF also sits in the archive folder.** The sentence below about *"the archive prints 80"* refers to the on-disk reports alone and is unaffected.

**⚠️ THIS TABLE AND THE 2 MARK TABLE BELOW count SCRIPT PAIRS, not full-mark scripts**: each row is a question the reports printed **twice** — the credited answer beside the rejected one — so a row here is not comparable with a row in the four governed tiers above. **They are rows in this file because they are verified exemplars, not because they are full-mark scripts.**

**The five reports held on disk print 80 marked scripts for the 1- and 2-mark tier — 58 in the four May 2023 reports, 22 in the June 2026 P1R report — and every one of them is now transcribed** *(derived, not typed — `layer_c_1_2mark_coverage.py` reads the five reports and these rows: **BANKED 80 / REMAIN 0**, 14 Oct 2026).* **No model is needed for this tier** — the mark scheme is already the perfect answer — **but a scheme cannot show you what a 0 looks like, and the rejected script is where the marks are actually lost.**

⭐ **The harvest runs across four report sets, one per paper:** `2023-05_Series_One_and_Two_Mark_Pairs.md` (five P2R pairs) · `2023-05_P2R_One_and_Two_Mark_Set.md` (**thirteen scripts**) · `2023-05_P1_and_P1R_One_and_Two_Mark_Set.md` (**twenty** — ten per paper) · `2026-06_P1R_One_Mark_Pairs.md` (five pairs, where the report states the mark outright: `Total: 0 marks` / `Total: 1 mark`).

⭐ **And across all 80 the failures sort into four kinds, none of them ignorance:**

> **1 · the definition that reuses the term, or borrows its neighbour** — P2 Q1(c) ×2 (*"quality"* twice, in two different scripts), P2 Q3(a) (an overdraft defined as *"a loan"*);
> **2 · the business name mistaken for context** — P1 Q1(d), P1 Q2(b), P2 Q1(d), P2 Q2(a) ×2, P2 Q2(b), P1R Q2(b);
> **3 · the answer rounded below the precision the question demanded** — P1R Q3(c), P2 Q1(e) ×2;
> **4 · the procedure, or the example list, where a definition was asked for** — P2 Q1(b) (what a business does with the applications), P1R Q1(c) (*"examples of stakeholders"*), and the failure the P1 Q3(a) commentary names outright.
>
> ⚠️ **Every one of those scripts was written by a candidate who understood the business.** The report's own verdict on its define questions is *"Most candidates understood what the term meant"* — printed beside *"nearly two thirds of the cohort not gaining the mark"*. **The mark is not for understanding; it is for a sentence a stranger could apply.**

| # | Session | Paper · Question | Topic | Source |
|---|---|---|---|---|
| 1 | **Jun 2023** | P2R Q1(c) | define qualitative market research — *M&M* | `External_Exemplars/2023-05_Series_One_and_Two_Mark_Pairs.md:33` |
| 2 | **Jun 2023** | P2R Q2(b) | one reason M&M could dismiss an employee — *M&M* | `External_Exemplars/2023-05_Series_One_and_Two_Mark_Pairs.md:66` |
| 3 | **Jun 2023** | P2R Q3(a) | define autonomy — *M&M* | `External_Exemplars/2023-05_Series_One_and_Two_Mark_Pairs.md:98` |
| 4 | **Jun 2026** | P1R Q1(b) | define secondary sector — *Spud Bros* *(banked 14 Oct 2026)* | `External_Exemplars/2026-06_P1R_One_Mark_Pairs.md:16` |
| 5 | **Jun 2026** | P1R Q1(c) | define e-commerce — *Spud Bros* *(banked 14 Oct 2026)* | `External_Exemplars/2026-06_P1R_One_Mark_Pairs.md:52` |
| 6 | **Jun 2026** | P1R Q2(a) | one current asset — *Spud Bros* *(banked 14 Oct 2026)* | `External_Exemplars/2026-06_P1R_One_Mark_Pairs.md:90` |
| 7 | **Jun 2026** | P1R Q2(b) | a reason employees are motivated — *Spud Bros* *(banked 14 Oct 2026)* | `External_Exemplars/2026-06_P1R_One_Mark_Pairs.md:124` |
| 8 | **Jun 2026** | P1R Q3(a) | define niche marketing — *Spud Bros* *(banked 14 Oct 2026)* | `External_Exemplars/2026-06_P1R_One_Mark_Pairs.md:157` |
| 9 | **Jun 2026** | P1R Q1(d) | one reason brand image is important — *Spud Bros* *(banked 14 Oct 2026)* | `External_Exemplars/2026-06_P1R_Two_Mark_Set.md:16` |
| 10 | **Jun 2023** | P2R Q1(b) | define public corporation — *M&M* *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P2R_One_and_Two_Mark_Set.md:17` |
| 11 | **Jun 2023** | P2R Q1(d) | why M&M should motivate employees — *M&M* *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P2R_One_and_Two_Mark_Set.md:49` |
| 12 | **Jun 2023** | P2R Q2(a) | a non-financial objective — *M&M* *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P2R_One_and_Two_Mark_Set.md:86` |
| 13 | **Jun 2023** | P1R Q1(b) | define economies of scale — *Aude Rose* *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P1_and_P1R_One_and_Two_Mark_Set.md:13` |
| 14 | **Jun 2023** | P1R Q1(c) | define stakeholder — *Aude Rose* *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P1_and_P1R_One_and_Two_Mark_Set.md:39` |
| 15 | **Jun 2023** | P1R Q1(d) | a benefit of JIT production — *Aude Rose* *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P1_and_P1R_One_and_Two_Mark_Set.md:65` |
| 16 | **Jun 2023** | P1R Q2(a) | a fringe benefit — *Aude Rose* *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P1_and_P1R_One_and_Two_Mark_Set.md:142` |
| 17 | **Jun 2023** | P1R Q2(b) | why branding is important — *Aude Rose* **(0/1 — the report prints only the zero-credit script)** *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P1_and_P1R_One_and_Two_Mark_Set.md:168` |
| 18 | **Jun 2023** | P1R Q3(a) | define variable costs — *Aude Rose* *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P1_and_P1R_One_and_Two_Mark_Set.md:211` |
| 19 | **Jun 2023** | P1 Q1(b) | define limited liability — *Irsi* **(0/1)** *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P1_and_P1R_One_and_Two_Mark_Set.md:374` |
| 20 | **Jun 2023** | P1 Q1(c) | define social enterprise — *Irsi* *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P1_and_P1R_One_and_Two_Mark_Set.md:400` |
| 21 | **Jun 2023** | P1 Q1(d) | using the Boston matrix — *Irsi* **(1/1 and 0/1)** *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P1_and_P1R_One_and_Two_Mark_Set.md:426` |
| 22 | **Jun 2023** | P1 Q2(a) | improving competitive position — *Irsi* *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P1_and_P1R_One_and_Two_Mark_Set.md:532` |
| 23 | **Jun 2023** | P1 Q2(b) | extending the life cycle — *Irsi* **(0/1)** *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P1_and_P1R_One_and_Two_Mark_Set.md:560` |
| 24 | **Jun 2023** | P1 Q3(a) | define fringe benefits — *Irsi* *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P1_and_P1R_One_and_Two_Mark_Set.md:601` |
| 25 | **Jun 2023** | P2 Q1(b) | define person specification — *IKEA* **(0/1 and 1/1)** *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P2_One_and_Two_Mark_Set.md:23` |
| 26 | **Jun 2023** | P2 Q1(c) | define quality control — *IKEA* **(0/1 and 0/1)** *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P2_One_and_Two_Mark_Set.md:57` |
| 27 | **Jun 2023** | P2 Q1(d) | why IKEA provides induction training — *IKEA* **(1/1 and 0/1)** *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P2_One_and_Two_Mark_Set.md:101` |
| 28 | **Jun 2023** | P2 Q2(a) | why IKEA would employ temporary staff — *IKEA* **(0/1 and 0/1)** *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P2_One_and_Two_Mark_Set.md:210` |
| 29 | **Jun 2023** | P2 Q2(b) | a financial objective — *IKEA* **(0/1)** *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P2_One_and_Two_Mark_Set.md:250` |
| 30 | **Jun 2023** | P2 Q3(a) | define overdraft — *IKEA* **(0/1)** *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P2_One_and_Two_Mark_Set.md:279` |
| 31 | **Jun 2024** | P2R Q1(b) | define e-newsletter — *Jimmy Choo* **(0/1 and 1/1)** *(banked 16 Oct 2026)* | `External_Exemplars/2024-06_P2R_Jimmy_Choo.md:33` |
| 32 | **Jun 2024** | P2R Q1(c) | define minimum wage — *Jimmy Choo* **(1/1 and 0/1)** *(banked 16 Oct 2026)* | `External_Exemplars/2024-06_P2R_Jimmy_Choo.md:45` |
| 33 | **Jun 2024** | P2R Q1(d) | State — loyal customers — *Jimmy Choo* **(1/1 and 0/1)** *(banked 16 Oct 2026)* | `External_Exemplars/2024-06_P2R_Jimmy_Choo.md:58` |
| 34 | **Jun 2024** | P2R Q2(a) | a non-financial objective — *Jimmy Choo* **(1/1 and 0/1)** *(banked 16 Oct 2026)* | `External_Exemplars/2024-06_P2R_Jimmy_Choo.md:121` |
| 35 | **Jun 2024** | P2R Q2(b) | why Jimmy Choo complies with health and safety laws — *Jimmy Choo* **(1/1 and 0/1)** *(banked 16 Oct 2026)* | `External_Exemplars/2024-06_P2R_Jimmy_Choo.md:134` |
| 36 | **Jun 2024** | P2R Q3(a) | define person specification — *Jimmy Choo* **(1/1 and 0/1)** *(banked 16 Oct 2026)* | `External_Exemplars/2024-06_P2R_Jimmy_Choo.md:224` |


---

## 2 MARK SCRIPTS — the marked calculation scripts, across two series

**Twenty scripts across four papers — fifteen calculations and five `Outline` questions — each printed with its own examiner comment, and between them they isolate both halves of the calculation tier.** **May 2023 isolates the ANSWER** — a value written to the wrong number of decimal places at three separate questions (*22.5* for *22.55*; *31* and *31.4* for *31.38*), a correct value written incompletely, and a complete calculation stopped one step short; **full marks were awarded to a script whose written answer differs from the mark scheme's own figure** *(see the Q4(a) entry — the report prints and credits it)*. ⚠️ **And this series alone settles what the dotted answer line is: a recommendation, not a requirement** — its 2/2 scripts include one that leaves the line blank and one that writes through a struck correction, while **what costs the mark is the precision, at every single question on the paper that demanded it.** **June 2026 isolates the WORKINGS** — three scripts whose final answer is wrong and which were paid anyway, because the scheme's own substitution line is on the page. **Transcribed in full, with the mark schemes, in the four harvest files named in the 1-mark section above.**

| # | Session | Paper · Question | Topic | Source |
|---|---|---|---|---|
| 1 | **Jun 2023** | P2 Q3(c) | calculate a bonus, 2 d.p. — *IKEA* | `External_Exemplars/2023-05_Series_One_and_Two_Mark_Pairs.md:141` |
| 2 | **Jun 2023** | P2 Q4(a) | calculate a percentage decrease, 2 d.p. — *IKEA* | `External_Exemplars/2023-05_Series_One_and_Two_Mark_Pairs.md:191` |
| 3 | **Jun 2026** | P1R Q1(e) | calculate the retained profit left — *Spud Bros* *(banked 14 Oct 2026)* | `External_Exemplars/2026-06_P1R_Two_Mark_Set.md:54` |
| 4 | **Jun 2026** | P1R Q3(b) | why cash is important — *Spud Bros* *(banked 14 Oct 2026)* | `External_Exemplars/2026-06_P1R_Two_Mark_Set.md:100` |
| 5 | **Jun 2026** | P1R Q3(c) | percentage increase in minimum wage — *Spud Bros* *(banked 14 Oct 2026)* | `External_Exemplars/2026-06_P1R_Two_Mark_Set.md:141` |
| 6 | **Jun 2026** | P1R Q4(a) | calculate total costs — *Spud Bros* *(banked 14 Oct 2026)* | `External_Exemplars/2026-06_P1R_Two_Mark_Set.md:201` |
| 7 | **Jun 2023** | P2R Q1(e) | percentage increase in borrowing, 2 d.p. — *M&M* *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P2R_One_and_Two_Mark_Set.md:129` |
| 8 | **Jun 2023** | P2R Q3(c) | the current ratio, 2 d.p. — *M&M* *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P2R_One_and_Two_Mark_Set.md:160` |
| 9 | **Jun 2023** | P2R Q4(a) | price in GBP, 2 d.p. — *M&M* **(1/2 and 1/2 — no full-mark script printed)** *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P2R_One_and_Two_Mark_Set.md:214` |
| 10 | **Jun 2023** | P2R Q3(b) | why locate a factory near a labour force — *M&M* *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P2R_One_and_Two_Mark_Set.md:267` |
| 11 | **Jun 2023** | P1R Q1(e) | break-even output, bunches of flowers — *Aude Rose* *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P1_and_P1R_One_and_Two_Mark_Set.md:97` |
| 12 | **Jun 2023** | P1R Q3(b) | extending the product life cycle — *Aude Rose* *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P1_and_P1R_One_and_Two_Mark_Set.md:246` |
| 13 | **Jun 2023** | P1R Q3(c) | percentage decrease in retained profits, 2 d.p. — *Aude Rose* **(1/2 — answer given to 1 d.p.)** *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P1_and_P1R_One_and_Two_Mark_Set.md:281` |
| 14 | **Jun 2023** | P1R Q4(a) | gross profit margin, 2 d.p. — *Aude Rose* *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P1_and_P1R_One_and_Two_Mark_Set.md:322` |
| 15 | **Jun 2023** | P1 Q1(e) | discount applied to a total, 2 d.p. — *Irsi* **(2/2 and 1/2)** *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P1_and_P1R_One_and_Two_Mark_Set.md:476` |
| 16 | **Jun 2023** | P1 Q3(b) | keeping customer loyalty — *Irsi* *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P1_and_P1R_One_and_Two_Mark_Set.md:629` |
| 17 | **Jun 2023** | P1 Q3(c) | the current ratio, 2 d.p. — *Irsi* *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P1_and_P1R_One_and_Two_Mark_Set.md:667` |
| 18 | **Jun 2023** | P1 Q4(a) | operating profit margin, 2 d.p. — *Irsi* *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P1_and_P1R_One_and_Two_Mark_Set.md:704` |
| 19 | **Jun 2023** | P2 Q1(e) | gross profit margin, 2 d.p. — *IKEA* **(1/2 and 1/2)** *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P2_One_and_Two_Mark_Set.md:145` |
| 20 | **Jun 2023** | P2 Q3(b) | why IKEA reads government reports — *IKEA* **(0/2)** *(banked 14 Oct 2026)* | `External_Exemplars/2023-05_P2_One_and_Two_Mark_Set.md:311` |
| 21 | **Jun 2024** | P2R Q1(e) | predicted value of recycled plastic, 2 d.p. — *Jimmy Choo* **(0/2 ×3 — no full mark printed)** *(banked 16 Oct 2026)* | `External_Exemplars/2024-06_P2R_Jimmy_Choo.md:71` |
| 22 | **Jun 2024** | P2R Q3(b) | why branding is important — *Jimmy Choo* **(0/2 and 2/2)** *(banked 16 Oct 2026)* | `External_Exemplars/2024-06_P2R_Jimmy_Choo.md:232` |
| 23 | **Jun 2024** | P2R Q3(c) | percentage increase on a handbag, 2 d.p. — *Jimmy Choo* **(1/2; the second script's comment is banked, its body is not — see the note at the foot of the harvest file)** *(banked 16 Oct 2026)* | `External_Exemplars/2024-06_P2R_Jimmy_Choo.md:248` |
