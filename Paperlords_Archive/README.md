# Paperlords IGCSE archive + searchable teaching reference

Downloaded and indexed on 2026-10-04.

## Current checkout verification (2026-10-28)

The single `Paperlords_All_IGCSE_Archive_4EC1_4BS1_4EB1.zip` is not present as a standalone file, but all **216 active Paperlords PDFs are present individually** under `IGCSE/` (including 48 English Language B PDFs: 23 QPs, 23 MSs and the two June 2023 ERs). The searchable text index, catalog and pairing metadata are present as well. Use the individual local PDFs for page/visual verification; June 2024–2025 examiner reports used in the English research are linked official Pearson sources and are not among the local 4EB1 ER PDFs. Do not mistake the root-level split workspace bundle for a standalone archive ZIP.

## Subjects
- Economics — 4EC1
- Business Studies — 4BS1
- English Language B — 4EB1

## Files
- `Paperlords_All_IGCSE_Archive_4EC1_4BS1_4EB1.zip` — all 216 active PDF records listed by Paperlords for these subjects (103 QPs, 103 mark schemes, 10 examiner reports), including listed R papers. All 103 QPs pair to a matching MS; 10 have a matching listed ER. The ZIP also includes one valid alternative for a malformed Paperlords PDF.
- `Paperlords_Searchable_Text_Index.zip` — page-by-page text extraction for the 216 listed records plus the recovered alternative, with `index.csv` and a README. This lets the assistant search the full question/mark-scheme/examiner-report text when answering.
- `Paperlords_Full_Catalog.xlsx` — filterable catalog with source links, ZIP paths, text paths and extraction status.
- `Paperlords_Full_Catalog.csv` — same catalog in CSV format.
- `Paperlords_QP_MS_ER_Pairings.csv` and the workbook’s `QP-MS-ER Map` sheet — all 103 QPs paired to their matching MS, with any listed ER attached.
- `search_paperlords.py` — keyword/phrase search over the text index (standard library only). Example: `python search_paperlords.py --subject Economics --session 2022 --type QP "inflation"`.
- `Workspace_Cleanup_Log.csv` — file cleanup crosswalk.

## Storage and selected test
- The source PDFs are stored individually under `IGCSE/` in this repository. The historical full archive ZIP was part of the split full-workspace bundle at the repository root; it is not a standalone file in this folder. The individual PDFs and searchable index are sufficient for the answer banks, so do not reconstruct another duplicate archive unless needed.
- `Selected_Test/4BS1_May2023_P1_QP.pdf` is a convenience copy of the Business Paper 1 used for the recent timed baseline; its original is stored at `IGCSE/4BS1_Business_Studies/May_2023/4BS1_Business_Studies_May_2023_P1_QP.pdf`.

## Business answer bank
`../Business_Studies_Answer_Bank/` contains a searchable 4BS1 question-type inventory built from all 38 Business QPs in this archive, a model-answer guide, and selected official Pearson candidate-response sources. `../Economics_Answer_Bank/` contains a compact 4EC1 inventory and model-answer guide built from 42 QPs, including the recovered May/June 2022 P2R paper. `../English_Answer_Bank/` contains a 4EB1 inventory built from 23 QP/MS pairs and official June 2023 candidate-script examples. All banks distinguish official scored scripts from constructed models; see each folder’s README.

## June 2026 4EB1 mark-scheme filename audit

The two June 2026 English Language B mark-scheme PDFs are named by Paperlords archive label, but their internal Pearson component covers are reversed relative to the same-named QPs: `4EB1_English_Language_B_June_2026_P1_MS.pdf` is Paper 01 (smartphones; matches the P2 QP, cover 4EB1/01), while `..._P2_MS.pdf` is Paper 01R (handwriting; matches the P1 QP, cover 4EB1/01R). The QP/MS/ER pairing CSV now maps each QP to the MS whose internal component and content match. Original PDF names and bytes were left unchanged; verify the cover code before using either file. The paper-specific Section A answer sets document the exact QP/source/MS checks and public report-access findings: [June 2026 P1, cover 4EB1/01R](../English_Answer_Bank/Answer_Sets/June_2026_P1_Section_A.md) and [June 2026 P2, cover 4EB1/01](../English_Answer_Bank/Answer_Sets/June_2026_P2_Section_A.md).

## Known document issue
The Paperlords-stored Economics May-June 2022 P2R QP at `IGCSE/4EC1_Economics/May-June_2022/4EC1_Economics_May-June_2022_P2R_QP.pdf` has zero readable pages in PDF parsers. A verified 20-page copy of the same 4EC1/02R paper is included under `RECOVERED_ALTERNATIVES/`; use it with the matching original MS. The recovery source URL and validation are in `recovery_notes.csv`.

Text extraction is a searchable aid, not a visual replacement for PDFs; inspect the original for diagrams, charts, layout or handwriting. Paperlords may not host every Pearson exam session ever issued.
