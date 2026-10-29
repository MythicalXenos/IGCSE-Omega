# Cross-source audit — 29 October 2026

A whole-bank reconciliation pass, run mechanically rather than by reading. Every question paper and mark scheme in the local archive was re-extracted with PyMuPDF and compared against what the 115 answer-set files actually say. This file records the method, the results, the corrections that came out of it, and the page-number conventions that caused most of the confusion.

---

## 1. Method

- **Extraction.** Every `*_QP.pdf` and `*_MS.pdf` in `Paperlords_Archive/IGCSE/4EB1_English_Language_B/` was opened with PyMuPDF 1.x; text taken from every page, then normalised: curly quotes and dashes flattened, Unicode folded to ASCII, punctuation stripped, whitespace collapsed, lowercased.
- **Matching.** Each claim in the bank was reduced to overlapping 5- or 6-word windows and tested for presence in the normalised source text. A window hit-rate of 1.00 means the bank's wording is a substring of the source, character for character, after normalisation.
- **Question extraction.** Section A questions were pulled from the QP by the printed `N⇥` markers; Q8 from the Section B page; Q9–Q11 from the page containing "Answer ONE question from this section". The extraction was checked by eye against the rendered QP pages for several papers before being trusted.
- **Page numbers.** Each mark-scheme page's own printed number (where printed) was read from the first line of its extracted text, giving a per-file offset rather than assuming one.

Scripts kept in `.scratch/`: `audit_sectiona.py`, `audit_sectionc.py`, `audit_q8.py`, `audit_ms_grids.py`, `measure_ms_pages.py`, `ms_page_truth.py`, `check_c_claims.py`, `check_b_claims.py`.

---

## 2. What matched, exactly

| Check | Result |
|---|---|
| Section A questions quoted in the Section A files | **161 of 161** (Q1–Q7 on 23 papers), hit-rate 1.00 |
| Section B Q8 prompts | **23 of 23**, hit-rate 1.00 |
| Section C Q9 statements | **23 of 23**, hit-rate 1.00 |
| Section C Q10 titles | **23 of 23** titles identical to the QP's `entitled '…'` |
| Section C Q11 tasks | **23 of 23**, hit-rate 1.00, all opening with "Describe" |
| Question-option coverage | 253 rows, 11 per paper on all 23 papers, all `COMPLETE` |
| Answer-set files referenced by `coverage.csv` | **0 missing**, **0 orphans** |
| Internal markdown links | **0 broken** (after two fixes, §4) |
| Mark-scheme page maps for the latest three series | Rendered page maps agree with every Section C citation: May 2025 P1R prints 20/21/22 (content/AO4/AO5, printed = PDF), May 2025 P1 prints 21/22/23, November 2025 P1 prints 17/18/19 at PDF 20/21/22, June 2026 Paper 01R prints 20/21/22, and June 2026 Paper 01 restarts so printed 8/9/10 sit at PDF 20/21/22 |
| Mark-scheme grid structure | 22 of 23 mark schemes extract as text and show Section B AO4 top band **11–12**, AO5 top **7–8**, Section C AO4 **17–20**, AO5 **9–10**. The 23rd (November 2024) is confirmed by facsimile, pp. 15–20 |
| Section A mark-scheme page citations | 116 "MS p. N" citations across the 23 Section A files resolve to pages that actually carry answer tables in the matched mark scheme (checked with printed-folio mapping, since offsets differ by paper) — 0 errors |
| Report-access routes | Documented in `Source_Notes/Report_Access_Routes.md`: the workspace has no egress to Pearson, the direct fetch route truncates at 30 pages, the reader-proxy route reaches the late pages, and hosted script pages carry a partial OCR text layer — so no further locator can be promoted to a facsimile transcript from this machine |
| Section C mark-scheme page citations | 184 "printed p. N" citations resolve to Section C content or an AO4/AO5 grid — 0 errors after the June 2026 fixes; the remaining script flags are QP page numbers and examiner-report pages, not MS citations |
| Mark-scheme answers cited in Section A files | 20 of 23 papers: every sampled "One valid answer is…" claim is supported by the paper's own mark scheme text. November 2024 was checked by rendering printed p. 8 (Q4's first accepted bullet is "a new hobby"; Q5 accepts "smoking" and "social media"). The June 2026 pair and May/June 2025 P1R cite mark-scheme bullets **paraphrased**, which those three files now state explicitly |

**Form differentiation is now a measured fact, not a convention.** All 23 Q10s read "Write a story (true or imaginary) entitled ‘…’"; all 23 Q11s read "Describe …"; 22 of 23 Q9s quote a statement for discussion. The single exception is **January 2022 P1 Q9, "Discuss whether travel broadens the mind."** — a discursive task with no quoted statement. Any summary of the pattern should say "Q9 is a discursive task, usually a quoted statement", not "always a quoted statement".

---

## 3. Page references: the offset table

This is the single largest source of apparent contradictions in the bank, and it is a formatting problem, not a factual one. In these files the printed page number is whatever appears printed on the page — which is **not** always the PDF page number.

| Mark scheme | Offset (printed − PDF page) | Consequence |
|---|---|---|
| June 2019 P1 / P1R | 0 | printed p. 13 = PDF page 13 |
| January 2020 P1 | −1 | printed p. 15 = PDF page 16 |
| January 2020 P1R | **no printed numbers** | bank cites PDF pages and says so |
| May/June–November 2020 P1 / P1R | −1 | printed p. 15 = PDF page 16 |
| May/June 2021 P1 | 0 | — |
| January 2022 P1 / P1R | −1 | printed p. 16 = PDF page 17 |
| May/June 2022 P1 / P1R | 0 | — |
| May/June 2023 P1 / P1R | **no printed numbers** | bank cites PDF pages and says so |
| May/June 2024 P1 / P1R | −1 | printed p. 17 = PDF page 18 |
| May/June 2025 P1 | −1 | printed p. 17 = PDF page 18 |
| May/June 2025 P1R | 0 | — |
| November 2021 P1 | 0 | — |
| November 2023 P1 | **no printed numbers** | bank cites PDF pages and says so |
| November 2024 P1 | 0 | printed p. 18 = PDF page 18 |
| November 2025 P1 | −3 | printed p. 17 = PDF page 20 |
| June 2026, Paper 01 | **−12** (pagination restarts) | printed p. 8 = PDF page 20 |
| June 2026, Paper 01R | 0 | — |

**Two notations are in use and both are correct:**

1. **"printed p. N"** — the number printed on the page. This is the majority convention and the one to prefer.
2. **"PDF index N" / bare "p. N"** — the 0-based page index in the file. Used in the June 2026 sets (whose printed pagination restarts) and in a handful of provenance lines that say so explicitly in the same sentence.

Every Section C and Q8 page claim was checked against the measured page under the convention that file declared, and **all of them are correct**. The only wording defects found were two misleading labels, fixed in §4.

---

## 4. Corrections made in this pass

| # | What was wrong | Where | Fix |
|---|---|---|---|
| 1 | Two links pointed at `MayJune_2022_P1R_Section_A.md` / `MayJune_2022_P1_Section_A.md`, which do not exist (the files are `June_2022_…`) | `Answer_Sets/MayJune_2022_P1R_Q8_Section_B.md`, `…_P1_Q8_…` | repointed to `June_2022_P1R_Section_A.md` / `June_2022_P1_Section_A.md` |
| 2 | Two files broke the naming pattern used by every other 2025 file (`May_2025_…`) | `MayJune_2025_P1_Q8_Section_B.md`, `MayJune_2025_P1R_Q8_Section_B.md` | renamed to `May_2025_P1_Q8_Section_B.md` and `May_2025_P1R_Q8_Section_B.md`; 5 references updated in `coverage.csv`, `Answer_Sets/README.md`, `Project_Status.md`, `4EB1_Exemplar_and_Model_Answer_Guide.md` |
| 3 | "Q8 indicative content **PDF p. 17**" gave the printed page under a PDF label | `May_2025_P1_Q8_Section_B.md` | now "printed p. 17 (PDF index 17)", with the offset stated |
| 4 | Bank totals were stale (they predated ten papers) | `BANK_RECONCILIATION.md` §2 | recomputed: 115 files, 255,803 words, 13,700 lines, 84 word-counted models at 42,753 words |
| 5 | November 2024 Q9 said "three support / four qualify", which forced the loosest supporting point into the qualifying column | `Answer_Sets/November_2024_P1_Q09_Section_C.md` | corrected to four support / three qualify on the plain reading, with the ambiguity named |
| 6 | Section A accepted-point lists in three files were presented as if quoted, but are paraphrases of the mark-scheme bullets | `June_2026_P1_Section_A.md`, `June_2026_P2_Section_A.md`, `May_2025_P1R_Section_A.md` | each file now carries a "Wording of the accepted points" note with the MS's own phrasing set beside the paraphrase |
| 7 | The exemplar guide's opening paragraph was a stale 28 October build log, left with an unclosed `**`, and still carried the retracted November 2024 "no indicative content" warning | `4EB1_Exemplar_and_Model_Answer_Guide.md` | replaced with a current status block; the retraction is now stated there too |
| 8 | The guide said the June 2023 AO5 conflict was left "unresolved" | same file | now explains the slip while preserving both printings |
| 9 | All six June 2026 Section C sets were one page out on their mark-scheme references: the paired `…_P1_MS.pdf` restarts its printed pagination, so printed p. 8 is **PDF page 20**, and the AO4/AO5 grids are PDF pages 21–22 (printed pp. 9–10), not 20–21 | `Answer_Sets/June_2026_P1_Q9/Q10/Q11_Section_C.md`, `Answer_Sets/June_2026_P2_Q9/Q10/Q11_Section_C.md`, `Answer_Sets/coverage.csv` | every reference now states both the printed number and the PDF page; the 01R pair (whose `…_P2_MS.pdf` does not restart) keeps printed = PDF |
| 10 | The retracted November 2024 "defective mark scheme" verdict was still live in `build_english_inventory.py` (two long workbook rows) and in four `coverage.csv` notes, which also described the grids as borrowed from May/June 2024 | `build_english_inventory.py`, `Answer_Sets/coverage.csv` | all six now state that the file is complete as printed, that only its text layer is broken, and that its own grids are used (AO4 printed p. 19, AO5 printed p. 20) |
| 11 | January 2022 P1/P1R Q8 were described in the workbook as "excluded by standing instruction" | `build_english_inventory.py` | label withdrawn: both sets exist and no such instruction was ever given |
| 12 | November 2024 Section A mark-scheme pages were untranscribed, so the answer set's keys rested on an earlier visual pass | `Source_Notes/November_2024_P1_MS_facsimile_transcription.md` | printed pp. 5–13 now transcribed verbatim from rendered pages; two bullets corrected against the printed wording (Q1 last bullet, Q2 fourth bullet) |
| 13 | The June 2025 P1R Q11 AO5 value was recorded as an unresolved 7-vs-8 conflict | `4EB1_Exemplar_and_Model_Answer_Guide.md`, `Project_Status.md`, `Completion_Map.md`, `Source_Notes/Official_Pearson_Exemplar_Index.md` | closed at **7/10** (judgement prints 13 then 7; total 20/30; no Q11 judgement reading 8 exists in pp. 58–63). The stray “8” is withdrawn as unsourced |

**Word counts of the models are sound.** Every one of the 84 explicit "Word count: N words" stamps was tested against the prose beneath it; the mean absolute difference is 47 words, and the differences come from craft annotations inside the model section that the stamp excludes. No stamp is wrong by a margin that would change a question's answer.

---

## 5. The June 2026 label swap — confirmed again, and it is not an error

The archive folder's filenames are crossed relative to the document covers:

| File | Cover / component | Date |
|---|---|---|
| `…_June_2026_P1_QP.pdf` | **4EB1/01R**, P79650A | Thursday 21 May 2026 |
| `…_June_2026_P2_QP.pdf` | **4EB1/01**, P79649A | Thursday 21 May 2026 |
| `…_June_2026_P1_MS.pdf` | headed **Paper 01** (printed pages run 1–10 from PDF page 13) | — |
| `…_June_2026_P2_MS.pdf` | headed **Paper 01R** (printed = PDF page) | — |

The bank's June 2026 answer sets therefore cite **P1_QP with P2_MS** (the 01R pair) and **P2_QP with P1_MS** (the 01 pair). That pairing is right, and each affected file states it. Anyone opening the folder cold will assume the opposite; the label-swap note in `Answer_Sets/README.md` and in each June 2026 provenance block is the guard against that.

---

## 6. Counts, re-derived

| Measure | Value | How measured |
|---|---|---|
| Answer-set markdown files | **115** (+ `README.md`) | directory listing |
| Answer-set words | **255,803** across **13,700** lines | whitespace split |
| Word-counted constructed models | **84** (63 Section C + 21 Section B Q8) | canonical `Word count:` stamps; the six June 2023 Section C files and the two June 2023 Q8 files carry authentic transcripts instead, so no stamp |
| Total words in those models | **42,753** | sum of stamps |
| Section A files | 23 (Q1–Q7 each) | — |
| Section B files | 23 | — |
| Section C files | 69 | — |
| Authentic records | **92** = 14 facsimile-checked transcripts/excerpts + 78 locator-only records | workbook sheet `Official script records`, 92 data rows, labels counted: 78 LOCATOR, 14 transcript |
| Question-option coverage | **253 of 253**, 23 papers × 11 | `coverage.csv` |

Note: the earlier figure "59 models, 26,670 words" was measured when the bank held about nineteen fewer papers. It is retired.

---

## 7. What this pass did *not* verify, stated plainly

- **Candidate-script wording** — 78 locator records still have no transcript; nothing here changes that.
- **Examiner-report commentary** — quoted from earlier reads; not re-fetched this turn (Pearson is unreachable from the sandbox; see `OPEN_GAPS.md`).
- **Marks and levels in locator rows** — carried forward as recorded, not re-derived from the reports.
- **Section A mark-scheme indicative content** — for 20 of 23 papers every sampled claim was matched against the MS text; the exceptions are the June 2026 pair and May/June 2025 P1R (paraphrased, now labelled). November 2024 is now fully transcribed (printed pp. 5–13): p. 4 is general guidance with no answer content, so nothing in that range is left unread.

Those four are the honest residue, and they are all recorded in `OPEN_GAPS.md`.
