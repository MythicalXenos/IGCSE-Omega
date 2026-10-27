# 4EB1 answer-set coverage and method

## Completion standard

A batch is marked **complete** only when, for each question in its stated scope, it records:

1. the exact QP prompt, paper/session and printed page;
2. the relevant QP source-text location where needed;
3. the corresponding official MS answer/indicative content and page;
4. a usable answer or answer key, including accepted alternatives for retrieval questions;
5. a clear evidence label and a note that an original worked answer has not been Pearson-scored.

A complete answer-set entry does **not** mean a candidate received full marks. Authentic candidate scripts are separate evidence and are called verified only when Pearson confirms the exact script and score. The question inventory’s 253 entries are not counted as answers unless a question-specific answer is recorded here or linked to an explicitly complete answer set. `coverage.csv` is the row-level manifest consumed by the workbook builder: `COMPLETE` means that exact QP/MS question is covered by a complete answer-set file; the default `NO COMPLETE ANSWER SET RECORDED` does not deny that a selected model or exemplar locator may exist elsewhere.

## Completed batches

| Paper | Scope | Status | Answer-set file |
|---|---|---|---|
| June 2023 P1 (4EB1/01) | Section A Q1–Q7 | **Complete: 7 question entries** | [`June_2023_P1_Section_A.md`](June_2023_P1_Section_A.md) |
| June 2023 P1R (4EB1/01R) | Section A Q1–Q7 | **Complete: 7 question entries** | [`June_2023_P1R_Section_A.md`](June_2023_P1R_Section_A.md) |

Both batches were checked against the local QP/Source Booklet and matching MS. Retrieval answer keys include the MS’s accepted alternatives; Q3/Q6/Q7 have original worked responses built from the MS. Their separate candidate-script scores are cited only as calibration. **Total complete: 14/253 question-option entries.**

## Work already elsewhere, not counted as complete answer sets

`../4EB1_Exemplar_and_Model_Answer_Guide.md` contains selected constructed models, including June 2023 P1 Q3/Q6/Q7/Q8 and Section C Q9/Q10/Q11. Those examples remain useful but do not substitute for a checked answer set for every question variation. In particular, the Section C “mini-models” and official script score/page locators are not automatically complete responses to every archived prompt.

## Remaining queue

1. November 2023 P1 Section A Q1–Q7.
2. Section A Q1–Q7 for each remaining QP/MS pair, one paper at a time, prioritizing analysis/comparison while including the retrieval keys.
3. Q8 QP/MS-specific sets, with the four Issue 4 forms from November 2025 onward tracked separately; older forms retained as historical practice only.
4. Section C Q9, Q10 and Q11 alternatives for every paired paper, each separately identified and answered.

Track each finished batch here and in `../Project_Status.md`. Do not claim all-archive answer coverage until all 253 indexed question-option entries have either a complete answer-set reference or a deliberate, sourced exclusion.
