# Economics whole-bank inventory reconciliation (working baseline)

**Status: inventory reconciled; classification is not yet complete.** This file resolves the scope discrepancy and gives a row-level, source-traceable starting manifest. It is not the requested ranked reasoning-family index: the manifest's topic, subtopic, reasoning-family and command-word columns are deliberately marked pending rather than filled with unreliable keyword guesses.

## Reconciled scope

The currently available, paired 4EC1 Economics question-paper scope is **43 paper/variant documents**: 22 Paper 1/P1R and 21 Paper 2/P2R. The archive pairing CSV has 42 pairs (21 of each paper group), which yield **998 parts and 3,360 marks**; the additional Paper 1R sitting is January 2023 (24 parts, 80 marks), available as incoming Pearson QP/MS material and documented in `Source_Notes/Examiner_Reports/2023-01_P1R_Source_Audit.md` and `2023-01_P1_MS_Source_Audit.md`. Thus 42 is the archive-register pairing count, not the complete local/incoming question-bank count.

| Inventory group | Paper records | Parts | Marks | Scope/source check |
|---|---:|---:|---:|---|
| Paper 1 + P1R | 22 | 539 | 1,760 | Existing parsed bank; 21 archive pairs plus the January 2023 P1R incoming Pearson source |
| Paper 2 + P2R | 21 | 483 | 1,680 | All 21 archive QPs parsed; each has 23 parts and 80 marks |
| **Combined** | **43** | **1,022** | **3,440** | No cross-paper deduplication: each actual sitting/variant/question part is a separate appearance |

Each paper in these sets totals 80 marks. Item counts per paper differ for P1/P1R; P2/P2R has 23 parsed parts per paper. The question reference includes session and variant so repeated question designs across sittings are preserved as distinct occurrences.

## Cross-checks and exceptions

- The 539-item Paper 1/P1R JSON bank contains 22 papers and sums to 1,760 marks. For the 21 archive-paired P1/P1R papers, the extracted `(question, part, marks)` signatures matched the QP parse; all question keys were found in the paired MS. January 2023 P1R is separately sourced from incoming/official Pearson material; its MS cover/code discrepancy and source caveats remain recorded in the cited source-audit note.
- Parsing the 21 Paper 2/P2R question papers yields 483 parts/1,680 marks. All 23 parsed question keys per paper are present in the corresponding mark scheme (483/483 key matches). The Paperlords June 2022 P2R QP copy is malformed for extraction; the manifest uses `Paperlords_Archive/RECOVERED_ALTERNATIVES/4EC1_Economics_June_2022_P2R_QP_alternative.pdf`, not the malformed original. June 2024 PDFs emit MuPDF layer-configuration warnings; they still parsed to the expected 23 parts/80 marks and complete MS-key match. These automated checks are not a substitute for visual validation of layout, diagrams, prompt boundaries or answer linkage.
- The existing workbook's type sheet has **671 rows** (P1 225, P1R 128, P2 202, P2R 116), which is **351 fewer** than the reconciled 1,022 question-part appearances. By group, workbook rows are 353 vs 539 P1/P1R (186 fewer) and 318 vs 483 P2/P2R (165 fewer). It is a partial/type-oriented inventory and cannot be used as the bank denominator.
- Paperlords' pairing CSV lists ERs for May 2023 P1R, P2 and P2R; the two Paper 2 examiner reports locally indexed in the archive are May 2023 P2 and P2R. Other ER guidance must be linked by exact paper identity from the local source-note/incoming report files when classifying; do not infer a report match from a session label alone. A missing ER is not a missing QP/MS question.

## Manifest

`Whole_Bank_Question_Manifest.csv` has one row per parsed question-part appearance (1,022 rows), including the exact session/variant/question reference, extracted prompt, marks, available MS text, local QP/MS/ER paths, archive source URLs when registered, and provenance/extraction caveats. It deliberately keeps every sitting occurrence and does not merge similar wording. Topic, subtopic, reasoning family and command-word fields say `PENDING_CLASSIFICATION`; every row's `source_check_status` says `PENDING_WHOLE_BANK_VISUAL_SOURCE_CHECK`. Rows sourced from the PDF text parser, especially Paper 2, still require visual audit; its text may contain layout spillover or omit diagram-only content. These explicit pending flags apply to this new whole-bank crosswalk even where an underlying question/answer had been checked in an earlier, different workflow. The manifest is a working evidence ledger, not a final classification or answer-quality claim.

`build_whole_bank_manifest.py` regenerates the CSV using the repository parser and PyMuPDF. It expects PyMuPDF to be installed; in the current sandbox the temporary dependency is at `/tmp/omega_pydeps` and can be used with `PYTHONPATH=/tmp/omega_pydeps`.

## Classification and audit still required

Next deliverable work remains: visually verify question wording/layout where needed; assign specification topic/subtopic and reusable reasoning/skill family (including separate recall, calculation, diagram, MCQ and definition skills); verify command word; build separate ranked P1/P1R and P2/P2R family indexes; report distinct papers, parts, marks and command-word/mark breakdowns; explain mechanisms, context changes and limits; link each occurrence to QP, MS and any identity-matched ER guidance; identify ambiguous/unclassified items; and use recurrence only to sequence a whole-bank answer audit, never as a forecast or scope filter. No answer is scored/guaranteed by this inventory.
