# Bank reconciliation — verified state, 29 October 2026

Every number below was recomputed from the files in this repository on 29 October 2026, not carried forward from prose. Where a claim cannot be verified from the bank itself, it is marked **unverified** and the reason is given.

## 1. Coverage — the headline figures

| Measure | Value | How it was checked |
|---|---|---|
| Papers in the archive and inventory | **23** | 23 QP/MS pairs in `Paperlords_Archive/IGCSE/4EB1_English_Language_B/` |
| Question-option entries per paper | **11** (Q1–Q8 plus Q9, Q10, Q11) | QP page 21 reads “Answer ONE question from this section”; all three Section C options are covered |
| Total question-option entries | **253** (23 × 11) | `4EB1_Question_Type_Inventory.xlsx`, sheet `All QP questions`, 253 data rows |
| Entries with a complete answer set | **253** | `Answer_Sets/coverage.csv`, 253 rows, all `COMPLETE` |
| Duplicate coverage keys | **0** | checked on session + paper + question |
| Papers complete at 11/11 | **23 of 23** | one row per question per paper, no gaps |
| Coverage percentage | **100%** | 253 ÷ 253 |

Breakdown by section: **161 Section A** (23 papers × Q1–Q7), **23 Section B** (Q8), **69 Section C** (Q9, Q10, Q11).

## 2. Answer-set files on disk

| Measure | Value |
|---|---|
| Markdown answer-set files | **115** (+ `README.md`) |
| Section A files | 23 (each holds Q1–Q7) |
| Section B files | 23 |
| Section C files | 69 |
| Missing files referenced by `coverage.csv` | **0** |
| Answer-set files not referenced by `coverage.csv` | **0** |
| Total words in answer-set markdown | **254,759** across 13,797 lines |
| Explicitly word-counted constructed models | **59 files, 26,670 words** of body text |

The 59 count excludes the eight June 2023 Section B/C files, which carry authentic transcripts rather than constructed prose and therefore no word-count stamp.

## 3. The authentic record — 92, kept separate from coverage

| Measure | Value | Source |
|---|---|---|
| Indexed official candidate-response records | **92** | `4EB1_Question_Type_Inventory.xlsx`, sheet `Official script records`, 92 rows |
| — facsimile-checked transcripts / excerpts | **14** | 9 labelled “facsimile-checked”, 3 “full transcription”, 1 “complete facsimile”, 1 “transcription” |
| — locator-only records (score + page, no wording) | **78** | 78 rows labelled `[OFFICIAL CANDIDATE SCRIPT LOCATOR]` |
| Entries whose answer text is authentic | **14** (June 2023 Q3/Q6/Q7/Q8/Q9/Q10/Q11 on both papers) | `Verified_Candidate_Responses/June_2023_Section_A.md` |
| Entries whose answer text is constructed | **239** | 253 − 14 |

**Coverage is not authenticity.** All 253 entries are *answered*; only 14 of them reproduce a real candidate script. Every constructed set is labelled as such and claims no score, so no constructed model can be mistaken for a marked response.

## 4. Deliverables rebuilt at the same time as the last batch

| File | Size | Contents |
|---|---|---|
| `4EB1_Question_Type_Inventory.xlsx` | 125,888 bytes | 253 question entries, 92 script records, 89 sources |
| `4EB1_Exemplar_and_Model_Answer_Guide.docx` | 58,419 bytes | rebuilt from the guide markdown |
| `Answer_Sets/coverage.csv` | 253 rows | LF only, no duplicate keys |
| Repository folder size | 2.9 MB | `English_Answer_Bank/` |

## 5. Internal consistency checks run this date

- Every tracker file’s live counter reads **253/253 (100%)** with **none outstanding** — 253 appears in 15 places, and no stale “N/253” remains except in dated historical progress sentences, all of which use the phrase “bringing coverage at that stage to …” (75 occurrences) or “at that point” (6).
- The authentic count reads **92** wherever stated (41 occurrences), with **78 locator-only** and **14 transcripts** consistent with the workbook.
- The May/June 2019 P1 “last buildable paper” sentence was corrected in `2203fce` after January 2022 was reopened.
- The January 2022 papers' former “excluded by standing instruction” label was corrected in `880891b`; no user instruction to omit them is recorded anywhere in the bank.
- Worktree is clean; every English-bank change is committed and pushed on `arena/031beb1c-igcse-omega`.

## 6. What is still soft — stated plainly

The four documented gaps, with their evidence and the exact next action for each, are consolidated in [`OPEN_GAPS.md`](OPEN_GAPS.md).

1. **78 locators remain untranscribed.** Those responses have published scores and pinned judgement pages but no wording, because the report reproduces them as page images with no text layer. Converting them needs facsimiles that are not in the archive.
2. **Four papers have no usable examiner report.** None is publicly locatable for November 2025 P1 or for either June 2026 paper; May/June 2021 P1 has no report at all. Those sets cite other papers' guidance and say so.
3. **One mark scheme has a broken text layer — corrected 29 October 2026.** `4EB1_01_2411_MS` (November 2024) is not defective: its printed pages are complete, but body glyphs on printed pp. 4–20 are stored as 2×2-pixel images, so text extraction returns almost nothing. The earlier “every grid emptied / band wording borrowed” entry was an artefact of the text route. Printed pp. 14–20 are now transcribed verbatim in `Source_Notes/November_2024_P1_MS_facsimile_transcription.md`, and all five November 2024 answer sets cite this paper's own content and grids.
4. **One level-label conflict is explained, and both printings are preserved.** June 2023 P1 Q8's report prints “Mark 8, Level 5” for AO5 while the matching grid (printed p. 16) puts 7–8 at Level 4 and has no Level 5 at all. The conflict is real in the published documents and stays quoted as printed wherever it is recorded; what has changed is that it is no longer *unexplained*. Three checks show the report's label is a slip: (i) this AO tops out at 8 across four levels, so a Level 5 cannot exist for it; (ii) the report's own AO5 sentence — “does manipulate complex ideas with a range of features and an extensive vocabulary” — paraphrases the **Level 4** descriptor (“Manipulates complex ideas… Uses extensive vocabulary strategically”); (iii) the same report labels other Section B AO5 marks correctly on the four-level scale (printed p. 42 “Mark = 4, Level 2”; printed p. 48 “Mark = 6, Level 3”), so p. 40 is an isolated slip, most plausibly carried down from the AO4 line immediately above it (11–12 = Level 5). The awarded 8/8 stands untouched.
5. **Report “findings” are not all unique.** The “long-winded and convoluted … too much direct speech” passage appears in three reports (June 2019 P1R, January 2020 P1R, January 2022 P1R) and is now treated as stock wording.
6. **No constructed model has been independently marked.** None of the 239 constructed entries claims a score; the band targets are design intentions argued from the descriptor wording, and are labelled that way in every file.
