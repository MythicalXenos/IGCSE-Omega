# Open gaps — what is still missing from the 4EB1 bank, and exactly why

**Status date: 29 October 2026.** The bank is complete in the sense that all 23 indexed papers have 11 of 11 question-option entries (253/253). What follows is the residue: four items the earlier reconciliation called "honest gaps". Two are now closed, one is explained, one is a source-access block that cannot be cleared from this environment.

| # | Gap | Status on 29 Oct 2026 |
|---|---|---|
| a | 78 authentic responses exist only as page images inside Pearson reports | **Blocked** — the PDFs cannot be obtained here; worklist below |
| b | November 2025 P1, June 2026 P1, June 2026 P2, May/June 2021 P1 have no usable examiner report | **Blocked for 3 of 4; May/June 2021 has no report at all** |
| c | November 2024 P1 mark scheme "published defective" | **Closed — the verdict was wrong**; see §3 |
| d | June 2023 P1 Q8 AO5 level label conflicts with the grid | **Explained — a printing slip, both readings preserved**; see §4 |

---

## 1. Gap (a) — the 78 locators

**How the 78 break down.** 42 Section A locators (fourteen each for Q3, Q6 and Q7), fourteen Section B Q8 locators, and 22 Section C locators across Q9–Q11 — the counts recorded in `Completion_Map.md`. They come from the June 2019 P1 report and the June 2022, June 2024 and June 2025 P1/P1R reports.

**What a locator is.** A report entry that names the question, the candidate's marks and level for each AO, and the printed pages on which the script is reproduced, but whose script text cannot be read. The bank records these as `[OFFICIAL CANDIDATE SCRIPT LOCATOR]` — 78 of them alongside 14 full transcripts.

**Why they are not yet transcripts.** In the June 2022–June 2025 Pearson reports the reproduced scripts are **page images**, not text. A text extraction of the report returns the surrounding commentary perfectly and then prints only a bare page number where the script should be — for example, in `4eb1-01-pef-20240822.pdf` (June 2024 P1) the text of printed p. 39 ends with "39 Int GCSE English Language B 4EB1 01" and printed pp. 40–42 contribute nothing but their numbers. This is the same class of artefact that produced the false November 2024 "defective mark scheme" verdict, so it is worth being precise: **the content is there in the PDF, as raster images; it cannot be recovered by any text route.**

**What is needed.** The PDF bytes, so that each script page can be rendered to an image and read by eye, exactly as the November 2024 mark scheme pages were read this week. Reports that publish scripts this way, with URLs:

| Paper | Report file | URL |
|---|---|---|
| June 2019 P1 | `4EB1_01_pef_20190822.pdf` | `…/International%20GCSE/English%20Language%20B/2016/exam-materials/4EB1_01_pef_20190822.pdf` |
| June 2022 P1 | `4eb1-01-pef-20220825.pdf` | `…/International%20GCSE/English%20Language%20B/2016/exam-materials/4eb1-01-pef-20220825.pdf` |
| June 2022 P1R | `4eb1-01r-pef-20220825.pdf` | `…/International%20GCSE/English%20Language%20B/2016/exam-materials/4eb1-01r-pef-20220825.pdf` |
| June 2024 P1 | `4eb1-01-pef-20240822.pdf` | `…/International-GCSE/English-Language-B/2016/Exam-materials/4eb1-01-pef-20240822.pdf` |
| June 2024 P1R | `4eb1-01r-pef-20240822.pdf` | `…/International-GCSE/English-Language-B/2016/Exam-materials/4eb1-01r-pef-20240822.pdf` |
| June 2025 P1 | `4eb1-01-pef-20250821.pdf` | `…/International-GCSE/English-Language-B/2016/Exam-materials/4eb1-01-pef-20250821.pdf` |
| June 2025 P1R | `4eb1-01r-pef-20250821.pdf` | `…/International-GCSE/English-Language-B/2016/Exam-materials/4eb1-01r-pef-20250821.pdf` |

(All under `https://qualifications.pearson.com/content/dam/pdf/`. Per-question page numbers for all 78 locators are in `Source_Notes/Official_Pearson_Exemplar_Index.md` §"Section A Q3/Q6/Q7", §"Section B Q8", §"Section C Q9" and §"Section C Q10–Q11".)

**Why it cannot be done from here.** Every route to `qualifications.pearson.com` from this sandbox fails at the TLS handshake:

```
curl: (35) OpenSSL SSL_connect: SSL_ERROR_SYSCALL in connection to qualifications.pearson.com:443
urllib: <urlopen error TLS/SSL connection has been closed (EOF)>
```

Outbound network access from the sandbox is restricted to npm, PyPI and GitHub. The page-fetch tool does reach Pearson, but it returns **extracted text only**, which is precisely the route that loses the scripts. GitHub was searched for mirrored copies of these filenames and does not hold them; the one peer index that lists Pearson filenames stops at the 2023 series.

**One-pass method for whenever a facsimile route opens** (so this is a transcription job, not a research job):

1. `pymupdf.open(report); page.get_pixmap(dpi=200).save(...)` for each script page named in the index.
2. Transcribe legibly only; mark illegible words `[illegible]`, doubtful readings `[wording uncertain: …]`, and never repair candidate spelling silently.
3. Record the printed page range, the report's AO marks/levels verbatim, and the script wording as a separate transcript file under `Verified_Candidate_Responses/`.
4. Move the locator's row to transcript status; increment the authentic index by one per script.

**Do not** attempt to reconstruct these scripts from commentary. No wording has been invented for any locator and none should be.

---

## 2. Gap (b) — the four papers without a usable examiner report

| Paper | Position | Evidence |
|---|---|---|
| **May/June 2021 P1** | **No report exists** — this was the optional/unseen assessment series | Report index for the series has no file for it; treated as structural, not an access gap |
| **November 2025 P1** | Not located | Filename patterns tried (`4eb1-01-pef-2026…` variants), Pearson course-materials listing unavailable, GitHub and peer indexes carry nothing beyond 2023 |
| **June 2026 P1 (4EB1/01R)** | Not located | Same; series too recent for the report to be in any third-party index |
| **June 2026 P2 (4EB1/01)** | Not located | Same; no report, no scripts, no exemplars found for P2 in any series |

**What this costs and what it does not.** Each of these papers still has a complete mark scheme in the local archive, so every answer set is mark-scheme-anchored. What is missing is the examiner commentary layer (what candidates actually did, what examiners warned about) and any possibility of an authentic script. Those sets say so in their provenance blocks rather than borrowing commentary from another paper.

**What would change the position.** A report appearing at any of the Pearson exam-materials URLs; the release of the June 2026 reports (historically published in the January following the series, i.e. from January 2027 for a June 2026 series); or a facsimile route that also carries the report PDFs. Until then, re-running the same searches is wasted work — this section exists so it is not repeated.

---

## 3. Gap (c) — November 2024 P1 mark scheme: closed

The mark scheme `4EB1_01_2411_MS` is **not defective**. Its text layer is: body glyphs on printed pp. 4–20 are stored as 2×2-pixel image objects, so extraction returns question numbers, AO labels, level labels and bullet glyphs while the printed page is perfect. Rendering the pages recovers everything. The earlier "every grid emptied / band wording borrowed" claim is retracted in every file that carried it.

The evidence, the transcription and the correction-of-record are in [`Source_Notes/November_2024_P1_MS_facsimile_transcription.md`](Source_Notes/November_2024_P1_MS_facsimile_transcription.md). Printed pp. 14–20 — Q8 indicative content and its three grids, and Section C Q9/Q10/Q11 content with the AO4 and AO5 grids — are transcribed verbatim there, and all five November 2024 answer sets now cite this paper's own wording.

**Residue:** printed pp. 1–3 (general guidance) and pp. 4–13 (Section A answers and the AO2/AO3 grids) have not been transcribed. No answer set currently cites Section A wording from this paper, so nothing is blocked; transcribe them if that changes.

---

## 4. Gap (d) — June 2023 P1 Q8 AO5 label: explained

The report prints "**Mark 8, Level 5**" for AO5; the matching grid (printed p. 16) puts 7–8 at **Level 4** and has no Level 5. Both readings are preserved as printed wherever the response is recorded. The label is a slip in the report:

1. Section B AO5 tops out at 8 marks across **four** levels — there is no fifth level for this AO to be at.
2. The report's AO5 sentence ("does manipulate complex ideas with a range of features and an extensive vocabulary") is a paraphrase of the grid's **Level 4** bullet ("Manipulates complex ideas… Uses extensive vocabulary strategically").
3. The same report applies the four-level scale correctly to other Section B AO5 marks: printed p. 42 "Mark = 4, Level 2", printed p. 48 "Mark = 6, Level 3". p. 40 is the only outlier, and the AO4 line directly above it awards 11–12 = Level 5.

The awarded **8/8** is full marks and is untouched. Full reasoning: `Answer_Sets/June_2023_P1_Q8_Section_B.md` and `Verified_Candidate_Responses/June_2023_Section_A.md`.

---

## 5. What is *not* a gap, so nobody reopens it

- **Coverage.** 253/253 question-option entries across 23 papers; Section B Q8 and Section C complete for every paper.
- **Counts.** Authentic index 92 (14 transcripts + 78 locators); 239 constructed entries; 59 constructed models. None of the constructed entries claims a score.
- **Form differentiation** across Section C is deliberate and paper-specific: Q9 the discursive statement, Q10 a supplied-entitlement story (late title reveal only where the report or mark scheme permits it), Q11 a description.
- **Duplicate archive bundle.** Removed in `45a1ef7` after hash verification; do not re-raise.
