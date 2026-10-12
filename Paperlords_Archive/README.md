# Paperlords IGCSE archive + searchable teaching reference

Downloaded and indexed on 2026-10-04.

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
- The full archive ZIP has been losslessly repacked using ZIP-LZMA compression to fit the workspace budget. All 220 archive entries, sizes, and CRC checks were verified unchanged. Some built-in unzip tools may not support ZIP-LZMA; if extraction fails, use 7-Zip, WinRAR, or another LZMA-capable ZIP utility.
- `Selected_Test/4BS1_May2023_P1_QP.pdf` is a convenience copy of the Business Paper 1 used for the recent timed baseline; the original is still in the full archive.

## Business answer bank
`../Business_Studies_Answer_Bank/` contains a searchable 4BS1 question-type inventory built from all 38 Business QPs in this archive, a model-answer guide, and selected official Pearson candidate-response sources. `../Economics_Answer_Bank/` contains a compact 4EC1 inventory and model-answer guide built from 42 QPs, including the recovered May/June 2022 P2R paper. `../English_Answer_Bank/` contains a 4EB1 inventory built from 23 QP/MS pairs and official June 2023 candidate-script examples. All banks distinguish official scored scripts from constructed models; see each folder’s README.

## Known document issue
The Paperlords-stored Economics MayJune 2022 P2R QP has zero readable pages in PDF parsers. The original file remains in the PDF archive; a verified 20-page copy of the same 4EC1/02R paper is included under `RECOVERED_ALTERNATIVES/`. The recovery source URL and validation are in `recovery_notes.csv`.

Text extraction is a searchable aid, not a visual replacement for PDFs; inspect the original for diagrams, charts, layout or handwriting. Paperlords may not host every Pearson exam session ever issued.
