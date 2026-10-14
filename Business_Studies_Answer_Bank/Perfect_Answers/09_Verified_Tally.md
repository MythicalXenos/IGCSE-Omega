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
> 1. **Every register row must resolve** — the file exists and the line it names carries the mark, in figures (`6/6`) or in words (*"Level 3 – 6 marks — FULL MARKS"*). ✅ **All 36 rows resolve.**
> 2. **It then scans the whole bank for script-bearing headings** — a heading that names a question label (`Q2(f)`) or one of the register's case studies — and checks each one against the register. ✅ **34 matched, 0 unaccounted.**
> 3. **Everything else is filtered out as narrative.** That is the restatement filter: a rule section called *"THE 9/9 JUSTIFY — six required features"* **is not a script**, and a cross-reference to a transcript held in another file **is not a second script**.
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
| **6-mark Analyse** | **19** |
| **1- and 2-mark items** | n/a — *the mark scheme IS the perfect answer; Pearson publishes no scripts* |

> ### ⚠️ WHAT THIS TABLE COUNTS — AND WHAT IT DOES NOT
> **It counts scripts Pearson printed with FULL marks against them.** A script the report itself scores at **11/12** is not a row here, and neither is a **6/12** or a **10/12** — **they are held instead in `03_Calibration_Below_Full_Marks.md` and in the 12-mark section of `02_Verified_Exemplars.md`, which is where their examiner comments teach the most.** The best of them — **Spud Bros, June 2026 P1R Q4(c), 11/12** — is called *"the best 12-mark model in the bank"* in `02_` for the reason that matters: **it is the closest thing to a full-mark 12-mark answer the bank owns, and it is the one Pearson printed with a conclusion.**

---

## 12 MARKS — **2 scripts**

| # | Series | P · Q | Case study | Canonical source |
|---|---|---|---|---|
| 1 | **Jun 2024** | P1 Q4(c) | PPS | `02_Verified_Exemplars.md:928` |
| 2 | **May/Jun 2023** | P1 Q4(c) | Irsi Chocolatier | `External_Exemplars/2023-05_Series_Irsi_AudeRose_IKEA_MM.md:17` |

> ### ⚠️ PERMANENT LIMITATION — BOTH ARE PAPER 1
> **No verified 12/12 exists for Paper 2 or Paper 2R, in any series.** Pearson names the **June 2022** and **June 2024 Paper 1** reports as its 12-mark exemplar sources, and both are harvested. **This is the edge of what is published, not a gap in the search.** **The best held on those two papers is a verified 10/12 on each — IKEA (P2 Q4(c), May 2023) and M&M (P2R Q4(c), May 2023); both were docked for *"limited judgements"*.**

---

## 9 MARKS — **15 scripts**

| # | Series | P · Q | The choice being made | Canonical source |
|---|---|---|---|---|
| 1 | **Jun 2019** | P1 Q3(e) | crowdfunding vs overdraft — *Backyard Shoez* | `02_Verified_Exemplars.md:461` |
| 2 | **Jun 2022** | P1 Q2(f) | retained profit vs bank loan — *TBTS* | `2022-06_P1_TBTS.md:168` |
| 3 | **Jun 2022** | P1 Q3(e) | questionnaires vs focus groups — *TBTS* | `2022-06_P1_TBTS.md:188` |
| 4 | **Jun 2022** | P1R Q2(f) | advertising vs open for breakfast — *Can Culleretes* | `2022-06_P1R_Can_Culleretes.md:51` |
| 5 | **Jun 2022** | P1R Q3(e) | permanent vs temporary contract — *Can Culleretes* | `2022-06_P1R_Can_Culleretes.md:76` |
| 6 | **May/Jun 2023** | P1 Q2(f) | job vs batch production — *Irsi* | `External_Exemplars/2023-05_Series_Irsi_AudeRose_IKEA_MM.md:382` |
| 7 | **May/Jun 2023** | P1 Q3(e) | on-the-job vs off-the-job training — *Irsi* | `External_Exemplars/2023-05_Series_Irsi_AudeRose_IKEA_MM.md:399` |
| 8 | **May/Jun 2023** | P1R Q2(f) | sponsor a flower show vs leaflets — *Aude Rose* | `External_Exemplars/2023-05_Series_Irsi_AudeRose_IKEA_MM.md:409` |
| 9 | **May/Jun 2023** | P1R Q3(e) | questionnaires vs internet — *Aude Rose* | `External_Exemplars/2023-05_Series_Irsi_AudeRose_IKEA_MM.md:417` |
| 10 | **May/Jun 2023** | **P2R Q3(e)** | job rotation vs bonus — *M&M* | `External_Exemplars/2023-05_Series_Irsi_AudeRose_IKEA_MM.md:425` |
| 11 | **Jun 2024** | P1 Q2(f) | — *PPS* | `2024-06_P1_PPS.md:60` |
| 12 | **Jun 2024** | P1 Q3(e) | — *PPS* | `2024-06_P1_PPS.md:79` |
| 13 | **Jun 2024** | P1R Q2(f) | vegan range vs discount — *Café Pinch* | `2024-06_P1R_Cafe_Pinch.md:9` |
| 14 | **Jun 2024** | P1R Q3(e) | communication methods — *Café Pinch* | `2024-06_P1R_Cafe_Pinch.md:24` |
| 15 | **Jun 2025** | **P2R Q2(f)** | weekly meetings vs email — *Rabanne* | `02_Verified_Exemplars.md:832` |

> ### ⭐ TWO OF THE FIFTEEN ARE **PAPER 2R** AND NONE ARE PAPER 2
> Entries **10** and **15** are the only full-mark Justify scripts the bank holds from an R-paper's second paper. **Paper 2 has none** — its best is a 7/9 (IKEA, June 2023).
>
> ### ⭐ AND FIVE COME FROM ONE SERIES
> May/June 2023 alone printed **five** 9/9 Justify answers — entries 6–10. The bank previously recorded this as **four**, because the fifth (a Paper 2R script) was filed in a different section of the report.

---

## 6 MARKS — **23 scripts**

| # | Series | P · Q | Topic | Canonical source |
|---|---|---|---|---|
| 1 | **Jun 2019** | P1 Q1(g) | satisfying customer needs | `02_Verified_Exemplars.md:314` |
| 2 | **Jun 2019** | P1 Q4(b) | usefulness of profitability ratios | `02_Verified_Exemplars.md:350` |
| 3 | **Jun 2019** | P1R Q1(g) | customer satisfaction | `2019-06_P1_Official_Exemplar_Booklet.md:513` |
| 4 | **Jun 2022** | P1 Q1(g) | external factors — *TBTS* | `2022-06_P1_TBTS.md:25` |
| 5 | **Jun 2022** | P1 Q3(d) | motivating employees — *TBTS* | `2022-06_P1_TBTS.md:50` |
| 6 | **Jun 2022** | P1R Q1(g) | impact of technology — *Can Culleretes* | `2022-06_P1R_Can_Culleretes.md:108` |
| 7 | **Jun 2022** | P1R Q3(d) | social media reviews — *Can Culleretes* | `2022-06_P1R_Can_Culleretes.md:133` |
| 8 | **Jun 2022** | P2R Q1(g) | two location factors, **43 words** — *Cadbury* | `2022-06_P2R_Cadbury.md:170` |
| 9 | **May/Jun 2023** | P1 Q1(g) | branding — *Irsi* | `External_Exemplars/2023-05_Series_Irsi_AudeRose_IKEA_MM.md:253` |
| 10 | **May/Jun 2023** | P1 Q4(b) | place — *Irsi* | `External_Exemplars/2023-05_Series_Irsi_AudeRose_IKEA_MM.md:262` |
| 11 | **May/Jun 2023** | P1R Q4(b) | measuring success — *Aude Rose* | `External_Exemplars/2023-05_Series_Irsi_AudeRose_IKEA_MM.md:272` |
| 12 | **May/Jun 2023** | P1R Q3(d) | retained profits as finance — *Aude Rose* | `2023-06_P1R_Aude_Rose.md:52` |
| 13 | **May/Jun 2023** | P2 Q3(d) | shortlisting — *IKEA* | `External_Exemplars/2023-05_Series_Irsi_AudeRose_IKEA_MM.md:327` |
| 14 | **Jun 2024** | P1 Q1(g) | — *PPS* | `2024-06_P1_PPS.md:32` |
| 15 | **Jun 2024** | P1 Q3(d) | — *PPS* | `2024-06_P1_PPS.md:47` |
| 16 | **Jun 2024** | P1R Q3(d) | — *Café Pinch* | `2024-06_P1R_Cafe_Pinch.md:65` |
| 17 | **Jun 2025** | P1 Q1(g) | **wide span of control — ONE point, 140 words** — *Four Fitness* | `02_Verified_Exemplars.md:871` |
| 18 | **Jun 2025** | P1R Q1(g) | app concerns — *CCT* | `02_Verified_Exemplars.md:423` |
| 19 | **Jun 2025** | P2 Q2(c) | batch production, 46 words — *Starbucks* | `02_Verified_Exemplars.md:423` |
| 20 | **May/Jun 2023** | **P2R Q3(d)** | comparing itself with other manufacturers — *M&M* | `External_Exemplars/2023-05_Series_Irsi_AudeRose_IKEA_MM.md:528` |
| 21 | **May/Jun 2023** | **P2R Q4(b)** | continuing to plant trees — *M&M* | `External_Exemplars/2023-05_Series_Irsi_AudeRose_IKEA_MM.md:541` |
| 22 | **Jun 2026** | P1R Q1(g) | sponsorship disadvantages — *Spud Bros* | `External_Exemplars/2026-06_P1R_SpudBros.md:319` |
| 23 | **Jun 2026** | P1R Q3(d) | viral advertising — *Spud Bros* | `External_Exemplars/2026-06_P1R_SpudBros.md:332` |

> ### ✅ THE ONE OPEN AMBIGUITY — CLOSED, 14 Oct 2026
> The June 2019 booklets' own coverage table claimed **"6/6 × 4"** across both booklets while only **three** were enumerated above. **A fourth appeared to be missing, and the count was therefore carried as "19 confirmed, possibly 20".**
>
> **There is no fourth.** The booklets' headings give exactly **6/6 ×3** — Backyard Shoez Q1(g), Backyard Shoez Q4(b) and Lavender Q1(g) — and **the same table was wrong in three other places too** (it claimed `9/9 ×2` for June 2019 where there is **one**, `9` Explain exemplars where there are **8**, and `6/6 ×4` where there are **three**).
>
> ✅ **So: 19, confirmed. Not "possibly 20".** *(The register has since grown to **23** — two May 2023 Paper 2R scripts (rows 20–21, found by the Level-phrasing sweep) and two June 2026 Paper 1R scripts (rows 22–23, whose scripts had been recorded as verdicts but never rendered). Both growths are recorded in `08_Completion_Map.md`.)* Verify with `python3 audit_exemplar_marks.py --all-2019`, which derives the distribution from the booklet headings themselves — **or read the correction block in `2019-06_P1_Official_Exemplar_Booklet.md`.** **The generalisable lesson: when a total disagrees with its own list, count the list. The total was typed by hand.**

---

## 3 MARKS — **4 scripts** *(all June 2026, P1R)*

| # | Series | P · Q | Topic | Canonical source |
|---|---|---|---|---|
| 1 | **Jun 2026** | P1R Q1(f) | flat organisational structure | `External_Exemplars/2026-06_P1R_SpudBros.md:369` |
| 2 | **Jun 2026** | P1R Q2(c) | why break-even output is calculated | `External_Exemplars/2026-06_P1R_SpudBros.md:381` |
| 3 | **Jun 2026** | P1R Q2(d) | segmenting the market by income | `External_Exemplars/2026-06_P1R_SpudBros.md:393` |
| 4 | **Jun 2026** | P1R Q2(e) | benefit of productivity improvements | `External_Exemplars/2026-06_P1R_SpudBros.md:405` |

> ### ⭐ ALL FOUR ARE THE NEWEST SESSION, AND EACH HAS ITS 0/3 PARTNER ON THE FACING PAGE
> Before 14 Oct 2026 the bank held **three** Explain exemplars, all June 2019. **This is the tier that is 152 parts of the qualification** — joint most common written type after the one-mark items. The four are transcribed with their **0/3 counterparts**, the examiner comments for both, and the rule the report states four times: **identify + two logical links.** See `08_Completion_Map.md` for the finding.

> ### ⚠️ REGISTER READS 44 ROWS ACROSS FOUR TIERS NOW — AND TWO CHECKS ONLY MODEL THREE
> `tally_exemplars.py` and `verify_coverage_claims.py` both parse the `## N MARKS` sections generically, so the four rows above are counted and resolved like the rest **but do not appear in the three-tier coverage grid** (`06_`'s grid is per-paper for 6/9/12 only, because those are the tiers where a Paper-level cell is meaningful). **The 3-mark tier has no paper-level grid cell on purpose** — an Explain exemplar is a technique example, and the six-mark ladder it feeds is already gridded.

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
