# 4BS1 — PERFECT ANSWERS BANK

**Pearson Edexcel International GCSE Business (4BS1)**
Built 2026-10-13 from the Paperlords archive (38 QPs + mark schemes) and official Pearson exemplar/examiner-report materials.

---

## What this bank is

A benchmark library of **what a top-band answer actually looks like** for every 4BS1 question type, so you can compare your own work against real, examiner-confirmed grade-9-level scripts instead of guessing.

It follows the collection method: gather verified top-tier answers from real exam series for each distinct question type and mark pattern; where genuine candidate scripts are unavailable, construct clearly labelled targets from the official mark scheme and examiner guidance.

## Two specifications — do not mix them

Pearson publishes similar materials for **IGCSE Business 4BS1** (your qualification) and **GCSE Business 1BS0** (a different one). They are not interchangeable. Where a source is GCSE 1BS0 it is labelled as such; its *technique* may transfer but its *scripts* must never be presented as 4BS1 exemplars. See `06_External_Source_Library.md`.

## Labelling contract — read this first

Every answer in this bank carries exactly one label:

| Label | Meaning | What guarantees it |
|---|---|---|
| **`[VERIFIED CANDIDATE EXEMPLAR]`** | A real student's script, reproduced by Pearson, with the mark Pearson awarded stated in the official document. | Session, paper, question, score and report page are all named, and `tally_exemplars.py` proves every register row resolves to a real `file:line` and a real mark token. |
| **`[OFFICIAL MARK-SCHEME WORKED ANSWER]`** | **Pearson's own indicative content, quoted verbatim, carrying the scheme's own `(1)(1)(1)` allocation** — the answer the mark scheme itself prints as acceptable for full marks. | Official words, official allocation. **Not a candidate script and not examiner-marked** — no student wrote it. |
| **`[CONSTRUCTED GRADE 9 TARGET]`** | A model engineered from the QP, mark scheme and examiner-report guidance. | **Not** an official script. **Not** examiner-marked. It is a target, not evidence. **No score is ever claimed for it.** |

Three labels, because there are three kinds of source. Constructed answers are never described in this bank as "official", "a real student script", or "examiner-marked" — and `verify_chain_bank_anchors.py` **fails if any model answer is unlabelled**, which it did on 14 October 2026 for 49 entries that had been covered only by a batch heading.

## Coverage at a glance

**The whole qualification, derived from its 38 mark schemes:** 988 parts worth 3,040 marks, and **every one of the 38 papers sums to exactly 80**.

| Marks | Parts | Where it sits | Verified full-mark exemplars held |
|---|---|---|---|
| **1** | **456** | MCQ · define · state · identify | ✅ **8 × 1/1**, archived and transcribed — ⚠️ *but no model is needed: the MS is the perfect answer* |
| **2** | **152** | calculate one figure · outline one | ✅ **2 × 2/2**, archived and transcribed — ⚠️ *same* |
| **3** | **152** | 1(f) · 2(c) · 2(d) · 2(e) | ✅ **47 × 3/3**, Jun 2019 → Jun 2026 |
| **6** | **114** | 1(g) · 3(d) · 4(b) | ✅ **27 × 6/6** |
| **9** | **76** | 2(f) · 3(e) | ✅ **16 × 9/9** |
| **12** | **38** | 4(c) | ✅ **5 × 12/12** |
| **TOTAL** | **988** | 26 parts / 80 marks per paper | **95 governed full-mark scripts**, plus **the 1- and 2-mark tier — all 80 scripts the five reports print, each transcribed with its examiner comment.** ✅ **`BANKED 80 / REMAIN 0`** *(`layer_c_1_2mark_coverage.py`, check 24; `08_` item 6 closed 14 Oct 2026)* |

**The 380 governed parts (3 marks and above) are all modelled** — 252 entries in `10_Chain_Bank.md`, one per topic rather than one per question, because the framings repeat and only the topic changes. **For the 608 one- and two-mark parts the mark scheme answer *is* the perfect answer** and is already in `By_Paper/`.

> ### ⚠️ THIS TABLE PREVIOUSLY CARRIED WITHDRAWN NUMBERS
> It used to show **696 items** with **111 / 86 / 48 / 17** in the governed tiers and a register of *"3/3 twice · 6/6 three times · 9/9 · 12/12"*. **Both sets came from a question-paper extraction that under-detects, and the exemplar column had drifted as scripts were harvested.** The counts above are the ones `build_layer_c_tariffs.py` prints from the mark schemes, and the exemplar column is the register `tally_exemplars.py` verifies. **`verify_coverage_claims.py` fails if any stated total in this bank disagrees with the register.**

## Files

| File | Use |
|---|---|
| **`00_Pearson_Official_Rulebook.md`** | ⭐ **START HERE.** Pearson's own published marking guidance for 4BS1, by command word. The awarding body stating how its papers are marked. Where anything else disagrees with this, **this wins**. |
| **`External_Exemplars/2019-06_P2_Official_Exemplar_Booklet.md`** | ⭐ **17 real candidate responses with the official mark scheme, awarded mark and examiner commentary** — June 2019 Paper 2/2R. The highest-quality source in the bank. |
| **`07_Official_Exam_Scope.md`** | ⭐ **What you do NOT need to learn.** The Getting Started Guide's own limits on every topic, the exact formulae and definitions in scope, and the precise wording of each required distinction. |
| **`By_Paper/`** | **Every question in every paper.** 38 files, one per question paper, containing all **988 items** with the official mark scheme answer for each. **Every file is checked against the mark schemes by `verify_by_paper.py` — 26 items and 80 marks each, in the identical 12/4/4/3/2/1 tariff shape.** Start here when working a specific paper. |
| `01_Mark_Tariff_Playbook.md` | The rules. AO splits, level bands and the structural recipe for every tariff — with literal opening sentences. **Read before writing anything.** |
| `02_Verified_Exemplars.md` | The verified full-mark scripts, transcribed in full, with examiner commentary. This is the benchmark. |
| `03_Calibration_Below_Full_Marks.md` | Near-miss scripts with the examiner's reason for every mark lost. Arguably more instructive than the full-mark ones. |
| `04_Type_Coverage_and_Gaps.md` | The complete item taxonomy, and an honest statement of what this bank does not contain. |
| `05_Constructed_12mark_Models.md` | `[CONSTRUCTED GRADE 9 TARGET]` models for 12-mark evaluations (batch 1: the six most recent sessions). |
| `06_External_Source_Library.md` | Web-harvested Pearson examiner reports: further `[VERIFIED CANDIDATE EXEMPLAR]` scripts, the full source catalogue, and collected examiner rules. |
| **`10_Chain_Bank.md`** | ⭐⭐ **THE MODELS.** 252 entries — a full-mark-shaped answer for every governed topic in the qualification, plus the scaffolds (entry 228 = the universal 12-mark shape, 175 = the universal 9-mark shape). **This is where you look up a question you have been set.** |
| **`08_Completion_Map.md`** | ⭐ **What "complete" means here, what is finished, and the five things that are not** — each one a fact about what Pearson publishes. Also the full list of the bank's checks. |
| **`09_Verified_Tally.md`** | The per-script register: one row per verified full-mark script, citing file and line. Counts are a property of the register, never hand-typed. |
| **`12_Grade_9_Marks_Budget.md`** | ⭐ **What a 9 costs, in arithmetic.** 160 marks, 133 for a 9, **27 you may lose**; the identical 12/4/4/3/2/1 tariff of every paper; the fixed AO split of the six long questions (**AO4 is only 9 marks a paper**); and the measured cost of each documented fault. Checked by `../verify_grade_budget.py`. |
| **`13_Paper_Craft_and_Timing.md`** | ⭐ **The 90 minutes, measured.** Pearson's cover page says *"use [the marks] as a guide as to how much time to spend"* — this is that arithmetic: **1.125 min per mark**, a 22½-minute budget per question, and where five spare minutes buy the most. Checked by `../verify_paper_craft.py` against all 38 QPs. |
| `16_Five_Verified_Twelve_Markers.md` | ⭐ **The five 12/12s, side by side.** Three different AO4 routes — a named condition, a condition plus an alternative, a time horizon — and one invariant: **two sides and a last word that decides.** Two of the four carry no definition at all and one never says "it depends". |
| `15_Tariff_Fingerprint.md` | ⭐ **What each mark value is MADE OF.** The AO composition of every tariff from all 38 mark schemes: 3-mark is AO1 only, 6-mark has **no AO1 and no AO4**, 9-mark has **no AO1**, 12-mark is the only one that pays for knowledge. Plus the command word each tariff always uses. Checked by `../verify_tariff_fingerprint.py`. |
| `14_Third_Party_Claims_Tested.md` | **Advice you will meet elsewhere, checked against Pearson** — six common claims (both sides, conclusions, "five strands", the "it depends" formula, 1BS0 advice leaking into 4BS1), each marked supported / contradicted / half-true. **Not evidence: no third-party source is relied on anywhere else in the bank.** |
| **`11_Self_Marking_Protocol.md`** | ⭐ **The candidate-facing sheet — five passes over your own answer, one card per tariff, every rule cited by number.** Distilled from rules already in `01_`/`06_`; it introduces no new evidence and scores nothing. |
| `Exemplar_Scans/` | The genuine candidate scripts as page images — see the real handwriting and structure. |
| `../build_perfect_answers.py` | Rebuilds the `By_Paper/` bank from the mark scheme text index. |

## The authority order

When guidance conflicts, trust in this order:

1. **`00_Pearson_Official_Rulebook.md`** — Pearson's published marking guidance. The rule.
2. **`By_Paper/`** — the official mark schemes. Authoritative for accepted content.
3. **`02_Verified_Exemplars.md`** / `External_Exemplars/` — real scripts with confirmed marks. Evidence of the rule in action.
4. **`01_Mark_Tariff_Playbook.md`** — this bank's synthesis. Useful, but derived.

## The two layers

**Layer 1 — official content (complete).** `By_Paper/` holds the mark scheme answer for every one of the **988 items** across all 38 papers. For the **608 one- and two-mark items (456 + 152)** the mark scheme answer **is** the perfect answer — there is nothing to add. For the **380 level-based items** it is the official accepted content that a full-mark response must assemble into developed chains.

> ### ⚠️ THESE THREE NUMBERS WERE WRONG UNTIL 14 OCT 2026 — and they looked right
> This paragraph used to say **977 items · 595 one- and two-mark (443 + 152) · 382 level-based**. Every figure was typed by hand, and the file it described **agreed with all of them** — so nothing in `By_Paper/` looked broken. **Three defects were hiding behind that agreement, in three different files:**
>
> 1. **May-June 2024 P2 and P2R** each collapsed the six one-mark MCQs into a single heading read as **"6 marks"** — the scheme prints the roman numeral on its own line, so the parser saw six `AO1 - 1 mark` runs as one item. **And it carried the content of only the FIRST of the six.** Measured on the file as committed: **one "only correct answer is" and three distractors, where the mark scheme prints six and eighteen.** ⚠️ **So five MCQs' official answers were simply absent from the file — while the "6 marks" heading still counted their marks.** The paper still summed to 80, which is why nothing noticed.
> 2. **May-June 2019 P2R was missing `1(a)(iii)`** — a **withdrawn item** that carries a mark but **no AO label**, which the generator used as its start-of-item signal. That is the paper that sums to **79**.
>
> ✅ **All three are repaired (`repair_by_paper_mcq_blocks.py`), and the check that found them is now tracked: `python3 verify_by_paper.py` compares every file against the tariff table derived from the mark schemes — item count, mark total, tariff histogram and governed-part labels. It passes 38/38, and the counts above are now what it prints.**
>
> **The lesson is sharper than "counts drift", and it has two halves.** **First: a check that only sums marks cannot see a six-for-one substitution** — the old reality check, *does this paper total 80?*, was satisfied by a file that had lost five questions **and** was satisfied on both 2024 papers. **Second: a file can be internally consistent and still be wrong.** `By_Paper/`'s headers agreed with its own headings, in all 38 files; agreement between a document and itself is not evidence. **What broke the deadlock was an INDEPENDENT count** — the tariff table derived from the mark schemes by `build_layer_c_tariffs.py`, which says how many parts of each tariff a paper must have.

**Layer 2 — constructed models (complete).** The official content assembled into full-mark-shaped responses: **252 entries covering all 380 governed parts**, held in `10_Chain_Bank.md` and checked by `verify_model_shape.py` against the shape each tariff requires — a mechanism step on 3-mark, developed strands on 6-mark, a **named condition** on 9-mark, and a woven judgement on 12-mark.

**Everything in this bank is verified by 29 checks** that run in about half a minute; `08_Completion_Map.md` lists them and says what each one would catch. **Each prints how many items it read, so a check that parses nothing is visible rather than silent** — the failure this bank has hit three times.

## Sources

- `../Sources/Official_Pearson/4BS1_Paper1_Exemplar_Commentaries_June2019.pdf` — 39 pp. Official June 2019 Paper 1/1R booklet: question, mark scheme, real responses, examiner comments.
- `../Sources/Official_Pearson/June2019_P2_Exemplar_Responses_Selected_Pages.pdf` — 21 pp. Selected original pages 5–14, 18–20, 24–31 of Pearson's Paper 2/2R booklet.
- `../Sources/Official_Pearson/May2023_P2_Examiners_Report_Excerpts_Q3e_Q4c.pdf` — 6 pp.
- `../Sources/Official_Pearson/June2024_P1_Examiners_Report_Excerpts_12mark_Evaluate.pdf` — 3 pp. One of **four** verified 12/12s; this excerpt holds the June 2024 P1 (PPS) one. The other three are the June 2022 P1 and P1R, and May/June 2023 P1 — see `16_Five_Verified_Twelve_Markers.md`.
- `../../Paperlords_Archive/` — 38 QPs, 38 MSs, 5 ERs for 4BS1, plus the searchable text index.

The Paperlords PDFs remain authoritative for visuals, tables and diagrams. The text index is a search aid.
