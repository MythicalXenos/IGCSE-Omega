# January 2023 — 4EC1/01R — source audit

Checked 2026-11-10 against Pearson source documents.

| Material | Verified source / identifier | Local state |
|---|---|---|
| Question paper | `https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Economics/2017/exam-materials/4ec1-01r-que-20230114.pdf` — cover identifies 4EC1/01R, 80 marks; question-paper log `P71556A`. | User-supplied copy: `uploads/Incoming_Economics_2026-11/4ec1-01r-que-20230114.pdf`. |
| Mark scheme | `https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Economics/2017/exam-materials/4ec1-01r-rms-20230302.pdf` — cover identifies January 2023, Paper 01R; content matches the QP topics and question sequence. | Retrieved/read from Pearson; a PDF copy is not currently in the workspace. |
| Examiner report | `https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Economics/2017/exam-materials/4ec1-01r-pef-20230302.pdf` — publication code `4EC1_01R_ER_2301`. | User-supplied copy: `uploads/Incoming_Economics_2026-11/4ec1-01r-pef-20230302.pdf`. |

## Publication-code discrepancy

The mark-scheme PDF’s cover names **Paper 01R**, and its URL uses `01r`, but its
printed Publications Code is `4EC1_01_MS_2301` (without the `R`). Do not silently
correct the source code or classify the paper as standard 01: the title, QP log
`P71556A`, matching QP, and question content identify this as the 01R mark
scheme. Preserve the literal code and discrepancy in any future index entry.

## Answer-bank status

The January 2023 P1R record has now been added to `Paper1_QA_Bank.json` and
`Paper1_QA_Bank.md` as an official-source supplement: 24 items / 80 marks, using
the local incoming QP and the linked Pearson MS. The MS PDF itself is still not
stored locally. Its official URL, the source-code discrepancy, and concise
paraphrases/summaries of its indicative content are preserved in the supplement
input; the builder does not download or independently re-verify the PDF. The
record does not present those summaries as verbatim transcription. It does
not add this paper to the Paperlords archive or pairing CSV.
