# IGCSE-Omega — whole-repository audit

> ## ⏳ THIS IS A DATED SNAPSHOT — 9 November 2026, commit `93d535f`
> **Its counts are historical and some are now wrong by design of the work done since** (Business has
> grown from 153 to **274 files**; the verified register from 148 to **150 rows**; the check suite has
> grown to **28**). **For current figures use `README.md` and
> `Business_Studies_Answer_Bank/Perfect_Answers/09_Verified_Tally.md`.** The *analysis* below — what is
> strong, what is missing, and why Economics is a starter kit — still stands and is not superseded.
**Date:** 9 November 2026 · **Branch:** `arena/031beb1c-igcse-omega` @ `93d535f`
**Scope:** every tracked file on this branch and on `main`, every folder, every script, every source.

---

## 1. The shape of it

| Measure | Value |
|---|---|
| Tracked files (this branch) | **663** |
| Tracked bytes | **332 MB** |
| — of which two bundle files | **126.5 MB** |
| Markdown | 287 files |
| PDF | 225 files |
| Python | 53 files |
| PNG | 53 files |
| Text | 14 · CSV 13 · JPEG 5 · XLSX 4 · DOCX 3 · ZIP 1 · SH 1 |

**Three subjects, three banks, one archive, one exam season.**

- **4BS1 Business** — 153 files · 20 MB · **484,099 words**
- **4EB1 English Language B** — 198 files · 6.2 MB · **437,433 words**
- **4EC1 Economics** — 7 files · 184 KB · **3,563 words**
- **Paperlords_Archive** — 229 files · 154 MB (216 PDFs + metadata + text index)

The imbalance is the headline. Business is the most developed bank in the repository;
Economics is a **starter kit**, and it is the paper you sit second.

---

## 2. Root level

| File | What it is | Verdict |
|---|---|---|
| `README.md` | 14 lines, English-only, last meaningfully updated in October | **Stale and now wrong.** It says no fresh English script has been submitted; you have since had a Q3 at 5/10 and a Q7 at 9/15 marked. It mentions no Business or Economics work at all. |
| `README_Workspace.md` | Full folder map, accurate, English-focused | Good. The only reliable "start here" document. |
| `Transfer_Prompt_New_Agent_Mode.md` | Handoff brief: goals, learner profile, subject-specific corrections, evidence rules | **The single most useful file in the repo.** It is the only place your corrections are recorded as rules. |
| `WORKSPACE_BUNDLE_README.txt` | Explains the bundle: "Created 2026-10-12… covers 50 source files" | Accurate. |
| `WORKSPACE_SHA256SUMS.txt` | 50 checksums | Verifies the 50 pre-bundle files. |
| `bundle_part_aa` + `bundle_part_ab` | 65 MB + 61.5 MB binary halves of one 126.5 MB zip | **Redundant.** `.gitignore` states the archive is fully extracted into `Paperlords_Archive/`. Every byte is duplicated in the archive tree. |
| `tools/recover_workspace.sh` | Recovery script: fetch the branch, hard-reset, reinstall `pypdf`/`pymupdf`, print counts | **Keep. Use it first every session.** It exists because the sandbox re-seeds `/home/user` from an old snapshot and silently replaces the checkout with `04b80df Initial commit`. It happened again at the start of this audit. |
| `.gitignore` | Python caches, the oversized source zip, `/tmp`, `*.part` | Correct, and the comment block explains the 100 MB GitHub limit honestly. |

---

## 3. `Paperlords_Archive/` — the archive

**216 PDFs, all individually present, all paired.**

| Subject | QP | MS | ER | Sessions |
|---|---:|---:|---:|---|
| 4BS1 Business | **38** | **38** | **5** | 12 (May/June 2019, 2020, 2021, 2022, 2024, 2025; May 2023; Nov 2021, 2023, 2024, 2025; June 2026) |
| 4EC1 Economics | **42** | **42** | **3** | 13 (adds January 2020, May 2025) |
| 4EB1 English | **23** | **23** | **2** | 14 (adds January 2020, January 2022) |

Every QP has a matching MS. That is the important fact: **you never lack a mark scheme.**

**Metadata and tooling**

- `Paperlords_Searchable_Text_Index.zip` — 219 text files, one per record plus README. Searchable without opening a PDF.
- `Paperlords_Full_Catalog.csv` / `.xlsx` — source links, paths, extraction status.
- `Paperlords_QP_MS_ER_Pairings.csv` — 103 QP→MS→ER links.
- `manifest.csv`, `Workspace_Cleanup_Log.csv`, `recovery_notes.csv`.
- `search_paperlords.py` — stdlib keyword search over the index. Working.

**Known defects, all documented rather than hidden**

1. **Economics May/June 2022 P2R QP** has zero readable pages. Two independently downloaded copies of the same paper exist as replacements under `RECOVERED_ALTERNATIVES/` and `Recovered_Alternatives/`. Verified 20 pages, cover 4EC1/02R.
2. **English June 2026 P1/P2 mark schemes are filename-swapped** — `..._P1_MS.pdf` is internally Paper 01, `..._P2_MS.pdf` is Paper 01R. The pairing CSV maps by the internal cover code, not the filename. Documented in the archive README.
3. **Two directories for one recovery** (`RECOVERED_ALTERNATIVES` and `Recovered_Alternatives`) — case-sensitivity hygiene, harmless.
4. `Selected_Test/4BS1_May2023_P1_QP.pdf` is a deliberate convenience copy of an archived paper.

**Examiner reports are the weak spot: 10 total, none from 2024–2026 except two Business files.** For English, 2024 and 2025 ERs were used in the research but were never stored locally.

---

## 4. `Business_Studies_Answer_Bank/` — 153 files, 20 MB

The most serious object in the repository. Built 12–14 October, then extended into a
`Perfect_Answers/` layer that is really a small research database.

### Core

| File | Words | What it does |
|---|---:|---|
| `4BS1_Exemplar_and_Model_Answer_Guide.md` / `.docx` | — | Mark-format map, first-sentence starters, exemplars, constructed targets |
| `4BS1_Question_Type_Inventory.xlsx` | — | 5 sheets; **696 standalone mark items** across **38 QPs** |
| `4BS1_Question_Instances.csv` | — | Portable item index with QP/MS paths |

### `Perfect_Answers/` — 97 files

| File | Words | What it does |
|---|---:|---|
| `00_Pearson_Official_Rulebook.md` | 6,519 | **Pearson's own guidance**, quoted, organised by command word. Declared the highest authority in the bank. Derived from all 38 mark schemes: 988 parts / 3,040 marks / 38×80. |
| `01_Mark_Tariff_Playbook.md` | 5,733 | What earns 1, 2, 3, 6, 9, 12 |
| `02_Verified_Exemplars.md` | 13,169 | Full-mark scripts with session, paper, question, page |
| `03_Calibration_Below_Full_Marks.md` | 3,936 | Scripts that missed, and why |
| `04_Type_Coverage_and_Gaps.md` | 2,395 | What exists and what does not |
| `05_Constructed_12mark_Models.md` | 3,620 | Labelled 12-mark targets |
| `06_External_Source_Library.md` | 24,434 | Sourced external guidance, GCSE 1BS0 clearly separated from IGCSE 4BS1 |
| `07_Official_Exam_Scope.md` | 3,261 | What is actually examinable |
| `08_Completion_Map.md` | 17,881 | Paper-by-paper state |
| `09_Verified_Tally.md` | 6,785 | **148-row register**, `tally_exemplars.py` verifies every row |
| `10_Chain_Bank.md` | **108,440** | Every governed question (3+ marks) across 38 papers, by framing, with a labelled answer each |
| `11_Self_Marking_Protocol.md` | 2,829 | How to mark your own script |
| `By_Paper/` | 38 files | **Every paper, 26 items, 80 marks each** |
| `External_Exemplars/` | 35 files | Real series scripts: IKEA, Cadbury, LEGO, TUI, Jimmy Choo, Starbucks, Rabanne, SpudBros… |
| `Exemplar_Scans/` | 11 PNGs | Facsimile pages of 11/12, 6/12, 9/9, 6/6, 3/3 scripts |

**The discipline here is the best in the repo.** Every answer carries one of three labels — `[VERIFIED CANDIDATE EXEMPLAR]`, `[OFFICIAL MARK-SCHEME WORKED ANSWER]`, `[CONSTRUCTED GRADE 9 TARGET]` — and there are scripts that **fail the build** if a model is unlabelled or a tally row does not resolve. That is not decoration; it caught 49 unlabelled entries and a wrong register on 14 October.

**This is, functionally, the revision system you should be using tomorrow.**

---

## 5. `Economics_Answer_Bank/` — 7 files, 184 KB, 3,563 words

| File | What it does |
|---|---|
| `4EC1_Exemplar_and_Model_Answer_Guide.md` / `.docx` | 8 sections: pattern map, first-sentence starters, 2/3/6/9/12-mark examples, examiner warnings |
| `4EC1_Question_Type_Inventory.xlsx` | **42 QP/MS pairs, 671 detected mark items** |
| `Source_Notes/Official_Pearson_Exemplar_Index.md` | Score-verified scripts, page map |
| `README.md`, two build scripts | Storage/evidence policy, rebuilds |

**What is missing, and it matters for the 11th:**

- No `Perfect_Answers` equivalent. **No By_Paper. No Chain Bank. No verified tally. No rulebook.**
- No examiner reports from 2024–2026 (only three May 2023 ERs, in the archive).
- No 12/12 candidate script — the 12-mark model is constructed and labelled as such.
- The guide is 3,563 words against Business's 484,099. Same qualification family, same command words, **1/136th of the material.**

The gap is structural, not fatal: `01_Mark_Tariff_Playbook.md` and `10_Chain_Bank.md` are the same command-word logic in a different subject, so the *method* transfers and only the *content* has to be looked up. But the Economics bank will not carry you through the 11th unaided.

---

## 6. `English_Answer_Bank/` — 198 files, 6.2 MB, 437,433 words

The most **complete** bank: 253/253 question-option entries across 23 papers, every row `COMPLETE` in `coverage.csv`.

| Layer | Files | Content |
|---|---:|---|
| `Answer_Sets/` | **116** | Section A (23 papers × Q1–Q7 = 161), Section B (23), Section C (69) |
| `Lesson/` | 15 | The teaching layer: five forms, plain skeletons, multiple examples per slot, Q9 engine, whole-paper plans, and the four Section A documents written on 3 November |
| `Practice/` | 21 | Nov 2024 practice set with both texts verbatim, June 2025 texts, learner attempts, Q9 drafts 2–4, situation audit |
| `Source_Notes/` | 19 | ER inventory, mark ladder, form frequency, OCR routes, official Pearson writing guidance + PDF |
| `Verified_Candidate_Responses/` | 7 | 14 authentic transcripts, friend's 66/100 calibration, 29/30 and 24/30 Q9s, friend's 17/30 |

**Evidence honesty, verified:** 14 authentic transcripts, 78 locator-only records, 239 constructed entries — and the bank says so in every file. Two known blocks are recorded rather than papered over: 78 scripts exist only as page images in Pearson reports that cannot be fetched from this sandbox, and the November 2025 / June 2026 reports are centre-gated for 12 months.

**Learner record, which the root README does not know about**

| Date | What | Mark |
|---|---|---|
| 1 Nov | Section A full script | assessed, re-marked against MS |
| 3 Nov | Nov 2024 Q3 | **5/10**, unfinished at 27 min |
| 3 Nov | Nov 2024 Q7 | **9/15** |
| 2 Nov | Q9 draft 4 (typed) | **21/30** (14 + 7) |
| — | Friend's full paper | **66/100** — A 25 · B 24 · C 17 |

---

## 7. The rest

| Path | Contents | Verdict |
|---|---|---|
| `Study_Notes/Economics_2026_P2/Text_Extractions/` | June 2026 Economics P2 QP + MS, clean and original text | Four files, correctly named. Only study note in the repo. |
| `uploads/` | `Saad mock 1 p2.pdf`; `CamScanner…pdf.txt` (11 MB); one screenshot; five WhatsApp images | **Unprocessed.** The mock is unmarked; nothing in the repo references it. |
| `.scratch/` | 13 audit scripts + 8 PNGs of the June 2026 P2R script | Working evidence for the English audit. Keep, but it is not documentation. |
| `git` history | 1 commit on `main`; ~90 on this branch | See §8. |

---

## 8. `main` versus this branch

| | `main` (`387f734`) | This branch (`93d535f`) |
|---|---|---|
| Commits | **1** — "Add full master bundle split parts" | ~90 |
| Bundle | seven `.txt` parts, 132.7 MB | two binary parts, 126.5 MB |
| `.gitignore`, `tools/`, `.scratch/` | absent | present |
| Banks | Business + Economics + early English | full English layer |

`main` is not a working branch. It is a **single snapshot commit holding a duplicate copy of the archive bundle**, chunked differently. The `.gitignore` records that the two sets were verified byte-identical by sha256 and that the `.txt` set was deleted from this branch to reclaim 126.5 MB.

**Net effect: the same 126 MB zip is stored twice in the repository's history, and 332 MB of tracked files exist to serve 216 PDFs totalling about 154 MB.** The repository works. It is roughly twice the size it needs to be.

---

## 9. What is genuinely strong

1. **Source discipline.** Three- or four-label evidence contracts, applied consistently across all three banks, with the label definitions written down.
2. **Verification that actually runs.** `tally_exemplars.py` (148 rows), `verify_chain_bank_anchors.py`, `verify_boundaries.py`, `check_ms_qp_agreement.py`. These fail loudly. That is rare and it is the reason the numbers can be trusted.
3. **Corrections are recorded as rules, not vibes.** The `Transfer_Prompt` carries your explicit corrections — subsidy "for families", national parks, import versus capacity, never calling a constructed answer official.
4. **The archive is complete and paired.** 103 QPs, 103 MSs, every one matched.
5. **`tools/recover_workspace.sh`.** It diagnoses the exact failure I hit twice today and fixes it in one command.

## 10. What is wrong or weak

| # | Problem | Severity |
|---|---|---|
| 1 | **Economics is 1/136th the size of Business** and is sat on the 11th | **High** |
| 2 | **126.5 MB bundle duplicated**, plus the `.txt` copy in history | Medium (housekeeping) |
| 3 | **Root `README.md` is stale** — English-only, and factually wrong about the learner record | Medium (misleads every new session) |
| 4 | **`uploads/Saad mock 1 p2.pdf` is unmarked and unreferenced** | Medium — unknown evidence sitting idle |
| 5 | **No error log.** Five subjects' worth of mistakes are scattered across attempt files; nothing accumulates them | Medium |
| 6 | **No spaced-repetition record.** Practice exists; scheduling does not | Low–Medium |
| 7 | Examiner reports: 10 total, almost all 2023 | Low (nothing can be done locally) |
| 8 | `RECOVERED_ALTERNATIVES` vs `Recovered_Alternatives` duplication | Cosmetic |

---

## 11. What to use, in what order, for the next 36 hours

**Business — 10th**

1. `Perfect_Answers/00_Pearson_Official_Rulebook.md` — the command words and what each tariff rewards. 20 minutes, then close it.
2. `Perfect_Answers/01_Mark_Tariff_Playbook.md` — the 3/6/9/12 method.
3. `Perfect_Answers/By_Paper/4BS1_November_2025_P1.md` — 26 items, 80 marks, official MS content for every one.
4. `Perfect_Answers/10_Chain_Bank.md` — **do not read start to finish.** Search it by command word and by topic.
5. `Perfect_Answers/09_Verified_Tally.md` + `Exemplar_Scans/` — read one 12/12 and one 6/6 by eye.

**Economics — 11th**

1. `Economics_Answer_Bank/4EC1_Exemplar_and_Model_Answer_Guide.md` — all eight sections, it is only 3,500 words.
2. `4EC1_Question_Type_Inventory.xlsx` — the pattern map sheet gives the question families.
3. Archive: any P1 QP + MS pair, 2019–2026. The mark scheme is the answer key; nothing else is needed.
4. Then **build Economics the Business way** — that is the one structural job worth doing, and it can be done in an evening because the format already exists.

---

## 12. Recommended next builds

1. **`Economics_Answer_Bank/Perfect_Answers/`** — 00 Rulebook (command words), 01 Tariff Playbook, 08 Completion Map, 09 Tally, 10 Chain Bank. Clone the Business structure; change the content.
2. **`ERROR_LOG.md`** — one row per mistake: date, subject, question, what went wrong, what the rule now is. Populated from the existing attempt files. This is the highest-value small file in the repo.
3. **Mark `uploads/Saad mock 1 p2.pdf`** and file it under `Verified_Candidate_Responses` or a new `Mock_Records/`.
4. **Rewrite root `README.md`** to cover three subjects and the real learner record.
5. **Retire the bundle** (or keep it out of the working tree) once the archive is confirmed complete — verify `sha256` against `.gitignore`'s recorded hash first.

---

*Every figure above was measured from the checkout, not carried forward from prose. Where a claim could not be measured — examiner-report availability, unmarked uploads — it is stated as unknown rather than assumed.*
