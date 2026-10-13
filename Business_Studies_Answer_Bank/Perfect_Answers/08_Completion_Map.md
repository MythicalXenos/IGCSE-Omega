# 08 — COMPLETION MAP

*What "completing Business" means, exactly, and what is still missing. Updated 2026-10-13.*

---

## THE DEFINITION OF "COMPLETE"

"Complete" cannot mean *a verified full-mark script for every question ever asked* — Pearson only publishes a handful of exemplars per report, and for many questions no full-mark script has ever been published. Those gaps can never be filled with real scripts.

So complete means **four things, all achievable**:

| # | Layer | Definition of done |
|---|---|---|
| **A** | **Evidence** | Every 4BS1 examiners' report that Pearson has published **and that is retrievable** is held and read in full — text layer *and* script pages. |
| **B** | **Exemplars** | Every question type × tariff × paper has the best available **verified** exemplar captured verbatim, with session, paper, question, exact mark and page. |
| **C** | **Models** | Every remaining governed item has a clearly labelled `[CONSTRUCTED GRADE 9 TARGET]` answer built from QP + MS + ER. |
| **D** | **Integrity** | Files 00–08 contain **no stale or unverified claims**, no duplicates, and every rule traces to a cited source. |

**Layers A and B are finite and closeable. Layer C is the long one. Layer D is housekeeping that must accompany both.**

---

## LAYER A — EVIDENCE COVERAGE

> ### 🚨 THREE STRUCTURAL FACTS — established this session, and they bound "complete"
> 1. **November-series reports contain NO candidate scripts.** They are *"Principal Examiner Feedback"* — commentary only. **Every verified script in the bank comes from a Summer series.**
> 2. **The November series runs only Papers 01 and 02.** Pearson's availability table: *Papers 1R & 2R — Nov 2025: **No**; Jun 2026: **Yes***. **"Nov P1R"/"Nov P2R" reports do not exist to be found.**
> 3. **June 2021 has no report** — that series used teacher-assessed grades. **Nothing is missing; it was never produced.**

### Coverage after the Phase 1 sweep

| Series | P1 | P1R | P2 | P2R | Status |
|---|---|---|---|---|---|
| **Jun 2019** | ✅ | ✅ **new** | ✅ | ✅ | **COMPLETE** |
| **Nov 2020** | ✅ | — | ✅ | — | **COMPLETE** (2 papers only) |
| **Nov 2021** | ✅ | — | ✅ **new** | — | **COMPLETE** |
| **Jun 2022** | ✅ | ✅ | ✅ | ✅ | **COMPLETE** |
| **May/Jun 2023** | ✅ | ✅ | ✅ | ✅ | **COMPLETE** |
| **Nov 2023** | ✅ **new** | — | ✅ | — | **COMPLETE** |
| **Jun 2024** | ✅ | ✅ | ✅ | ⛔ | **COMPLETE** — P2R report confirmed non-existent |
| **Nov 2024** | ✅ | — | ✅ **new** | — | **COMPLETE** |
| **Jun 2025** | ✅ | ✅ | ✅ | ✅ | **COMPLETE** |
| **Nov 2025** | ❓ | — | ❓ | — | **OUTSTANDING** — not found at any date tried |
| **Jun 2026** | ❓ | ✅ | ❓ | ❓ | **P1R COMPLETE** · others behind Edexcel Online |

**Ten of eleven report-bearing series are complete.** The whole **Summer 2019 → Summer 2025** run is now closed.

### Outstanding, precisely

| Item | State | Why |
|---|---|---|
| **Nov 2025 P1 · P2** | ❓ | Publication ~Jan 2026. **Every date tried returned 404** (`20260121`, `20260122`, `20260123`). Not on any mirror either. **May not be publicly posted yet, or the filename differs.** |
| **Jun 2026 P1 · P2 · P2R** | ⛔ | Pearson states Summer 2026 examiner reports released **"From 25 August 2026"** via **secure download** (Edexcel Online login). The **P1R** report circulates and is held; the other three do not. **Likely unreachable until the public release.** |
| **Jun 2020** | ❓ | **Verify whether a report was produced** — that series was cancelled. The archive holds QP/MS but no ER. |
| **Nov 2022** | ❓ | **Verify whether a series ran** — no QP, MS or ER in the archive, and none held. |

### Held locally, needing no fetch

`May_2023/` **P1 · P1R · P2 · P2R** (187pp) · `June_2026/P1R` (48pp) — **5 files, complete, with scripts.**

### Chunks still unread in reports already fetched

**June 2025 ×4** — ✅ **NOW COMPLETE.** A second pass over all four reports recovered two further verified full-mark exemplars and nine rule-groups (**rules 110–117**). See `External_Exemplars/2025-06_Second_Pass_Addendum.md`.

**What the second pass added to the verified set:**
| Item | Detail |
|---|---|
| **A 10th verified 6/6 Analyse** | June 2025 P1 Q1(g) — *Four Fitness*, wide span of control. **"1 point with developed strands"** — one idea, six links, ~140 words. |
| **A 7th verified 9/9 Justify** | June 2025 P2R Q2(f) — *Rabanne*, weekly meetings vs email. The named condition in full. |
| **The State minimum, quantified** | *"**Just one reference to the context of the business is enough for a 'state' question.**"* |
| **The 3-mark anatomy, proved** | 1 point + **2** developed steps = 3 · 1 point + **1** step = 2. Same question, same cohort. |
| **Premature rounding** | New calculation trap — *"rounded their figures up or down prematurely."* |
| **A priced 5/9 one-sided Justify** | Everything except balance → capped at 5. |
| **Word-collision cluster 19 → 22** | *trade bloc · job production · share capital.* |

> ### ⚠️ ONE DELIBERATE NON-ADDITION
> The June 2025 P2R **Q3(e)** Justify script (product trials vs advertising) is a strong answer, **but no mark is printed against it in the retrievable text.** It is filed as **script-without-mark** and is **not** counted as a verified exemplar. **This is what the labelling contract requires.**

### Chunks still unread — none outstanding

### 🚨 INTEGRITY CORRECTION — the running totals were wrong

`09_Verified_Tally.md` is new. It **derives** the exemplar counts from the bank's own headings via `tally_exemplars.py` instead of carrying hand-written totals.

| Claimed | Truth |
|---|---|
| 9/9 = 6, then 7 | **14** |
| 6/6 = 9 (then 10) | **18** |
| 12/12 = 2 | **2** ✅ *the only count that was right* |

**Cause:** totals were hand-incremented while the lists beside them grew by transcription. The two drifted.
**Rule going forward: never carry a running total by hand.** Quote the script's output.

**Two duplicate files remain the reason the naive scan over-counts by 2** — `2023-06_P1R_Aude_Rose.md` and `2023-06_P2_IKEA.md` against `2023-05_Series_*.md`. **This fold is now overdue.**

**None.** All four June 2025 reports have now been read end to end — see the second-pass entry above.

---

## LAYER B — EXEMPLAR COVERAGE

Currently held (verbatim, with award):

| Type | Tariff | Best verified |
|---|---|---|
| **Analyse** | 6 | **18 × 6/6** — derived, see `09_Verified_Tally.md` |
| **Justify** | 9 | **14 × 9/9** — derived, see `09_Verified_Tally.md` |
| **Evaluate** | 12 | **2 × 12/12** (Jun 2024 P1 PPS · May 2023 P1 Irsi) · 11/12 (Spud Bros) |
| **Explain** | 3 | multiple 3/3 |
| **Calculate** | 2 | 2/2 with the d.p. rule |
| **State / Define** | 1 | 1/1 vs 0/1 pairs |
| **Outline** | 2 | 2/2 |

### ⚠️ The one structural gap that cannot be closed by more searching
> **No verified 12/12 exists for Paper 2 or Paper 2R.** The bank holds two 12/12s, both on Paper 1. Pearson's own support page states the 12-mark exemplars are in the **June 2022 and June 2024 Paper 1** reports — precisely the two papers already harvested. **Best verified for Paper 2 is 10/12 (IKEA, M&M).**
>
> **Consequence:** every Paper 2 12-mark model must remain `[CONSTRUCTED GRADE 9 TARGET]` **unless** the June 2026 P2/P2R reports prove otherwise. **That is the whole reason Layer A still matters.**

---

## LAYER C — CONSTRUCTED MODELS

**6 written of ~382 governed items.**

Priority order:
1. **Any type × paper with no verified exemplar at all.**
2. **Tariffs 9 and 12** (36 of the 80 marks).
3. **Tariffs 3 and 6** (the volume).
4. Tariffs 1 and 2 (cheapest; last).

---

## LAYER D — INTEGRITY WORK (outstanding)

| Item | Status |
|---|---|
| ✅ **Stale claim in `06_`** — "no full-mark Analyse/Justify held for 2026" | **CORRECTED.** June 2026 P1R supplied verified 6/6 and 8/9 scripts; the claim is rewritten. |
| Duplicate 2023 files — `2023-06_P1R_Aude_Rose.md`, `2023-06_P2_IKEA.md` vs `2023-05_Series_*` | **Consolidate.** |
| Taxonomy table + rules 48–63 → `01_` | Not yet moved. |
| E1–E12 folding into `06_` | Not yet folded. |
| `May-June_2019_P2R` 79-marks puzzle | Unresolved. |
| **Word-collision cluster** | ✅ now **19 entries**; run a collision check over every QP in the archive to find the remaining pairs. |
| **253 MiB redundant tracked duplicate bundle parts** | **Awaiting your approval to delete.** |
| June 2026 grade boundaries (Grade 9 = 133/160 overall) | Sourced but **needs verification against the grade-boundary PDF** before entering `00_`. |

---

## ORDER OF WORK

**Phase 1 — Evidence.**
1. ✅ **DONE — the Summer 2019 → Summer 2025 run is complete.** Nov 2023 P1, Nov 2024 P2, Nov 2021 P2 and Summer 2019 P1R were all recovered in this sweep, along with nine new rule-groups (rules 100–109).
2. **Outstanding:** Nov 2025 P1/P2 (filename unknown) · Jun 2026 P1/P2/P2R (secure download) · verify Jun 2020 and Nov 2022.
3. **Render the unread script pages of the June 2025 reports** — chunks 2–3 of all four hold the remaining 12-mark exemplars.

**Phase 2 — Exemplars.** Capture the best script for every type × paper from the newly acquired reports.

**Phase 3 — Models.** Fill Layer C in batches, prioritised as above.

**Phase 4 — Integrity.** Purge stale claims, consolidate duplicates, move the taxonomy, fold E-rules, verify boundaries.

---

## WHAT WILL REMAIN OPEN AT THE END

Stated plainly so the final report is honest:

1. **No verified 12/12 on Paper 2 or 2R** — unless June 2026 supplies one.
2. **A handful of report-papers that were never published or are not retrievable** (e.g. Jun 2024 P2R — confirmed non-existent).
3. **The single marked script per question in each report** — Pearson publishes one or two examples per question, so many valid routes to full marks are simply never shown.
