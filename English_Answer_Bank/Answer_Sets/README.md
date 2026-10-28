# 4EB1 answer-set coverage and method

The canonical whole-bank completion map (23 QP/MS pairs, 253 question-option entries, current paper-by-paper totals and research stages) is [`../Completion_Map.md`](../Completion_Map.md).

## Completion standard

A batch is marked **complete** only when, for each question in its stated scope, it records:

1. the exact QP prompt, paper/session and printed page;
2. the relevant QP source-text location where needed;
3. the corresponding official MS answer/indicative content and page;
4. a usable answer or answer key, including accepted alternatives for retrieval questions;
5. a clear evidence label and a note that an original worked answer has not been Pearson-scored.

A complete answer-set entry does **not** mean a candidate received full marks. Authentic candidate scripts are separate evidence: use `[VERIFIED CANDIDATE EXEMPLAR]` only for wording checked against the facsimile, and `[OFFICIAL CANDIDATE SCRIPT LOCATOR]` for a Pearson-reproduced response with a published score/page but no checked transcript. The question inventory’s 253 entries are not counted as answers unless a question-specific answer is recorded here or linked to an explicitly complete answer set. `coverage.csv` is the row-level manifest consumed by the workbook builder: `COMPLETE` means that exact QP/MS question is covered by a complete answer-set file; the default `NO COMPLETE ANSWER SET RECORDED` does not deny that a selected model or exemplar locator may exist elsewhere.

## Completed batches

| Paper | Scope | Status | Answer-set file |
|---|---|---|---|
| May/June 2022 P1 (4EB1/01) | Section A Q1–Q7 | **Complete: 7 question entries** | [`June_2022_P1_Section_A.md`](June_2022_P1_Section_A.md) |
| June 2023 P1 (4EB1/01) | Section A Q1–Q7 | **Complete: 7 question entries** | [`June_2023_P1_Section_A.md`](June_2023_P1_Section_A.md) |
| June 2023 P1R (4EB1/01R) | Section A Q1–Q7 | **Complete: 7 question entries** | [`June_2023_P1R_Section_A.md`](June_2023_P1R_Section_A.md) |
| November 2023 P1 (4EB1/01) | Section A Q1–Q7 | **Complete: 7 question entries** | [`November_2023_P1_Section_A.md`](November_2023_P1_Section_A.md) |
| May/June 2024 P1 (4EB1/01) | Section A Q1–Q7 | **Complete: 7 question entries** | [`June_2024_P1_Section_A.md`](June_2024_P1_Section_A.md) |
| May/June 2024 P1R (4EB1/01R) | Section A Q1–Q7 | **Complete: 7 question entries** | [`June_2024_P1R_Section_A.md`](June_2024_P1R_Section_A.md) |
| November 2024 P1 (4EB1/01) | Section A Q1–Q7 | **Complete: 7 question entries** | [`November_2024_P1_Section_A.md`](November_2024_P1_Section_A.md) |
| May 2025 P1 (4EB1/01) | Section A Q1–Q7 | **Complete: 7 question entries** | [`May_2025_P1_Section_A.md`](May_2025_P1_Section_A.md) |
| May 2025 P1R (4EB1/01R) | Section A Q1–Q7 | **Complete: 7 question entries** | [`May_2025_P1R_Section_A.md`](May_2025_P1R_Section_A.md) |
| November 2025 P1 (4EB1/01) | Section A Q1–Q7 | **Complete: 7 question entries** | [`November_2025_P1_Section_A.md`](November_2025_P1_Section_A.md) |
| June 2026 P1 (archive label; 4EB1/01R) | Section A Q1–Q7 | **Complete: 7 question entries** | [`June_2026_P1_Section_A.md`](June_2026_P1_Section_A.md) |
| June 2026 P2 (archive label; 4EB1/01) | Section A Q1–Q7 | **Complete: 7 question entries** | [`June_2026_P2_Section_A.md`](June_2026_P2_Section_A.md) |

All twelve batches were checked against the local QP and matching MS, and against source text where available. The May/June 2022 P1, June 2023, May/June 2024, November 2024, May 2025, November 2025 and both June 2026 P1/P2 source texts are appended to their local QPs. Candidate-script wording is not treated as independently verified quotation evidence unless a specific check is recorded. Retrieval keys include accepted alternatives; the longer answers are original MS-based responses and are not Pearson-scored. The May/June 2022 P1, June 2023, June 2024 and May 2025 P1/P1R sets cite separate candidate-script score locators as calibration only; those marks do not transfer to the constructed answers. For May 2025 P1, the official June 2025 report’s Q3 locators are 9/10 Level 5 (printed judgement p. 12) and 5/10 Level 3 (p. 9); Q6 locators are 9/10 Level 5 (p. 20) and 2/10 Level 1 (p. 17); Q7 locators are 13/15 Level 5 (p. 25) and 5/15 Level 2 (p. 28). The 9/10 and 13/15 samples are near-full, not full marks. For May 2025 P1R, Q3 locators are 10/10 Level 5 (printed judgement p. 9) and 3/10 Level 2 (p. 12); Q6 locators are 10/10 Level 5 (p. 19) and 5/10 Level 3 (p. 23); Q7 locators are 14/15 Level 5 (p. 30) and 5/15 Level 2 (p. 34). These remain locator-only: candidate wording and script-page spans are not verified, and lower scores are retained accurately. No locator score is assigned to a worked answer. For May/June 2022 P1, the official June 2022 report records Q3 at 8/10 Level 4 (printed judgement p. 8) and 3/10 Level 2 (p. 11), Q6 at 10/10 Level 5/full marks (p. 16) and 5/10 Level 3 (p. 18), and Q7 at 11/15 Level 4 (p. 23) and 8/15 Level 3 (p. 25). The 28 October full-text recheck exposed no visual candidate-page facsimile; script-page spans remain unpinned, no wording is transcribed, and these six records remain locator-only. The local November 2023 archive has no ER PDF; Pearson’s official online report was reviewed in all five text chunks and no score-bearing script locator was found, so no candidate score is reported for that paper. The official November 2024 P1 report was likewise reviewed in all five returned text chunks; no reproduced candidate wording or score-bearing exemplar was located in that text route. For November 2025 P1, exact Pearson-domain searches and public course-materials/report routes did not surface an accessible report or candidate facsimile; the local pairing table also has no ER entry. This is an access gap, not evidence that no report exists. The QP, appended source pages and matching MS were visually checked, and the original Q3/Q6/Q7 worked answers are clearly separated from authentic-response evidence; no candidate score or wording is claimed. For June 2026 P1, the matching 01R MS is stored under the archive filename `..._P2_MS.pdf`; the cover-code audit and corrected pairing are documented in `Paperlords_Archive/README.md` and the June 2026 answer set. For June 2026 P2, the matching Paper 01 MS is stored under `..._P1_MS.pdf`; exact official-domain searches and the public course-materials route did not surface a report or script facsimile. This is an access gap, not proof of non-existence; the source, QP and matching MS checks are documented in [`June_2026_P2_Section_A.md`](June_2026_P2_Section_A.md). No June 2026 candidate wording or score is claimed. **Total complete: 84/253 question-option entries (33.2%); 169 remain.**

## Work already elsewhere, not counted as complete answer sets

`../4EB1_Exemplar_and_Model_Answer_Guide.md` contains selected constructed models, including June 2023 P1 Q3/Q6/Q7/Q8 and Section C Q9/Q10/Q11. Those examples remain useful but do not substitute for a checked answer set for every question variation. In particular, the Section C “mini-models” and official script score/page locators are not automatically complete responses to every archived prompt.

## Authentic-response phase — active priority

`../Verified_Candidate_Responses/June_2023_Section_A.md` contains facsimile-checked transcriptions/excerpts of fourteen genuine Pearson-reproduced responses: June 2023 P1 Q3 (9/10 L5), Q6 (10/10 L5), Q7 (15/15 L5), Q8 (30/30), Q9 (17/30; AO4/AO5 L3), Q10 (30/30), Q11 (23/30); and P1R Q3 (8/10 L4), Q6 (10/10 L5), Q7 (8/15 L3), Q8 (26/30), Q9 (17/30; AO4/AO5 L3), Q10 (30/30), Q11 (26/30). It flags uncertain/crossed-out wording and the three Pearson reproductions that visibly end incomplete. In addition, the workbook and `../Source_Notes/Official_Pearson_Exemplar_Index.md` record **78 locator-only** Pearson examples: eleven from June 2019 P1 plus 67 from June 2022/2024/2025 P1/P1R. The combined locators comprise 42 Section A Q3/Q6/Q7 records, fourteen Section B Q8 score/AO records and 22 Section C Q9–Q11 score/AO records. Exact June 2019/2022 prompts and matching local MS checks are recorded; exact marks/levels and printed judgement pages are preserved, but no locator-batch candidate wording is transcribed. The resulting **92 authentic-response records** remain separate from the **84/253** answer-set coverage. Continue the all-section real-script search. Before constructing each next paper-specific batch, review its official report and exhaust accessible source routes; keep any unavailable script facsimile as an explicit gap. The November 2024 P1 report yielded narrative feedback but no candidate wording or score-bearing exemplar in the reviewed five-chunk text route. Retain lower-scoring examples with their true marks, and never let a score/page locator become a transcript.

## Constructed answer-set queue — resume after the real-script-first phase

**Next selected paper-specific batch:** May/June 2022 P1R (4EB1/01R), Section A Q1–Q7. Before drafting, review its official Pearson report and pursue visually verifiable facsimiles for the existing Q3/Q6/Q7 locators; then verify the exact P1R QP/source and matching P1R MS independently. Transcribe only legible wording from a visually checked script, keep locator-only records and constructed answers separate, and preserve any remaining access gap. Never infer candidate wording or marks from OCR.

1. Section A Q1–Q7 for each remaining QP/MS pair, continuing with May/June 2022 P1R (4EB1/01R) after its authentic-report/facsimile review; proceed one paper at a time, prioritizing analysis/comparison while including the retrieval keys.
2. Q8 QP/MS-specific sets, with the four Issue 4 forms from November 2025 onward tracked separately; older forms retained as historical practice only.
3. Section C Q9, Q10 and Q11 alternatives for every paired paper, each separately identified and answered.

Track each finished batch here and in `../Project_Status.md`. Do not claim all-archive answer coverage until all 253 indexed question-option entries have either a complete answer-set reference or a deliberate, sourced exclusion.
