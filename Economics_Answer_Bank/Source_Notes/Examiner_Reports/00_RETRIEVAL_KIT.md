# Examiner reports — retrieval and status guide

Status checked 2026-11-10. This is a Paper 1-first research aid, not a claim that
all reports have been found or that a search miss proves nonexistence.

## Access and publication status

Pearson’s Qualification and Assessment Publication Policy and its June 2026
Economics update state that exam materials, including examiner reports, are
restricted to Pearson-centre teachers for 12 months after an exam series and
require Edexcel Online access during that period. Pearson’s updates scheduled
International GCSE reports for November 2025 on 27 January 2026 and June 2026
on 25 August 2026. Those schedule notices do not establish that a specific
4EC1 Paper 1 or Paper 1R report is publicly retrievable. Exact reports for those
recent series remain unlocated in unauthenticated public access as of this check.
A direct URL 404 or search miss is not evidence that a report was never issued.

Pearson’s Summer 2021 announcement and a contemporaneous British Council
notice establish that the International GCSE May/June exams were cancelled and
were not sat globally; Economics’ own March update confirms the subject was
included. The standard P1 QP/MS are extant and paired by QP log `P65896A`, but
the sources checked do not establish whether that exact paper was among the
unseen materials Pearson supplied for Teacher Assessed Grades. Its ER is **not
located**. Pearson’s final R timetable had listed 4EC1/01R for 20 May before
cancellation; its exact QP/MS/ER remain **not located**. See
`2021-06_P1_P1R_Source_Audit.md` for Pearson’s TAG/unseen-materials guidance
and the distinctions among scheduled, cancelled, and extant documents.

## Local Paper 1 report materials

The cover-checked inventory of incoming P1/P1R reports is
`Incoming_P1_Report_Inventory.md`.

- **May 2023 P1R:** in the archive and available for the answer-bank work.
- **November 2023 P1:** source retrieved; notes at `2023-11_P1_ER.md`.
- **November 2024 P1:** official Pearson source retrieved; publication code
  `4EC1_01_2411_ER`. Key points are recorded in the research handoff.
- **June 2025 P1:** official Pearson PDF in
  `uploads/Incoming_Economics_2026-11/4ec1-01-pef-20250821.pdf`; complete
  question-by-question summary at `2025-06_P1_ER.md`.
- **January 2023 P1:** Pearson’s standard 4EC1/01 ER has been directly
  retrieved/read. Its cover publication code is `4EC1_01_ER_2301`; question-by-
  question notes are at `2023-01_P1_ER.md`. The PDF is not yet stored locally:
  a command-line download failed at TLS, so the inventory records this
  separately from the local incoming PDFs. The official P1 mark scheme was also
  retrieved/read at Pearson; its cover identifies Paper 01 and QP log `P71555A`,
  but its printed publication code anomalously reads `4EC1_02_MS_2301`. It is
  not stored locally; details at `2023-01_P1_MS_Source_Audit.md`. Do not confuse
  this with the distinct 01R mark scheme and its separate code/log discrepancy.
- **January 2023 P1R:** official QP, MS and ER are all identified. QP and ER
  are incoming local files; the official MS was retrieved/read at Pearson but
  its PDF is not yet stored locally. A 24-item / 80-mark answer-bank supplement
  is now included, with its content labelled as summaries/paraphrases. Its
  printed MS code omits the R despite the cover identifying 01R; details at
  `2023-01_P1R_Source_Audit.md`. The P1 ER (`4EC1_01_ER_2301`) and P1R ER
  (`4EC1_01R_ER_2301`) are separate reports.
- Other PDFs in `uploads/Incoming_Economics_2026-11/` include P1/P1R reports for
  several earlier series. Verify each PDF’s cover publication code and paper
  content before assigning a session or updating a pairing; do not infer identity
  from filenames alone.

The archive pairing CSV currently indexes **only its own Paperlords files**; an
empty ER cell means none is listed in that archive, not necessarily that no
report exists elsewhere.

## Verified Pearson URL patterns

Current-style files often use:

```
https://qualifications.pearson.com/content/dam/pdf/International-GCSE/Economics/2017/Exam-materials/<code>-pef-<YYYYMMDD>.pdf
```

Older files may use:

```
https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Economics/2017/exam-materials/<code>_pef_<YYYYMMDD>.pdf
```

Codes vary in capitalization and formatting (`4EC1_01`, `4ec1-01`, `4EC1_01R`,
`4ec1-01r`). The date is the publication date, not necessarily the exam date.
These patterns are search aids only: confirm that a retrieved document is a
Pearson PDF and verify its cover code and content.

Confirmed examples:

| Series | Paper | Confirmed URL |
|---|---|---|
| June 2019 | 01 | `https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Economics/2017/exam-materials/4EC1_01_pef_20190822.pdf` |
| January 2020 | 01R | `https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Economics/2017/exam-materials/4EC1_01R_pef_20200305.pdf` |
| June 2022 | 01R | `https://qualifications.pearson.com/content/dam/pdf/International-GCSE/Economics/2017/Exam-materials/4ec1-01r-pef-20220825.pdf` |
| November 2023 | 01 | `https://qualifications.pearson.com/content/dam/pdf/International-GCSE/Economics/2017/Exam-materials/4ec1-01-pef-20240125.pdf` |
| November 2024 | 01 | `https://qualifications.pearson.com/content/dam/pdf/International-GCSE/Economics/2017/Exam-materials/4ec1-01-pef-20250123.pdf` |
| June 2025 | 01 | `https://qualifications.pearson.com/content/dam/pdf/International-GCSE/Economics/2017/Exam-materials/4ec1-01-pef-20250821.pdf` |

## How to continue the audit

1. Search the official Pearson qualification materials page and web-indexed
   Pearson PDFs for the exact series/paper code.
2. If using a guessed URL, record a 404 as a failed retrieval attempt only—not
   proof of nonexistence.
3. Verify the cover publication code, paper number and series against the PDF
   contents before filing it. Preserve filename/title conflicts as documented
   discrepancies rather than silently retagging the file.
4. Record whether the source is official or secondary, what was searched, and
   what remains unverified. Keep “not located” distinct from “not issued.”
5. Summarize question-by-question examiner advice in
   `Source_Notes/Examiner_Reports/<series>_<paper>_ER.md`; avoid reproducing full
   candidate scripts or extensive copyrighted text.

Pearson sources on the access policy and release schedule are listed in
`Source_Notes/Official_Source_Register.md`. The next audit priority is to verify
and index the incoming P1/P1R report PDFs by their covers, then revisit any
unresolved standard P1 sessions in the pairing inventory.
