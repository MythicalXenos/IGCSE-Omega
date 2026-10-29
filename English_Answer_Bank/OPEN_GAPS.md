# Open gaps — what is still missing from the 4EB1 bank, and exactly why

**Status date: 29 October 2026.** The bank is complete in the sense that all 23 indexed papers have 11 of 11 question-option entries (253/253). What follows is the residue: four items the earlier reconciliation called "honest gaps". Two are now closed, one is explained, one is a source-access block that cannot be cleared from this environment.

| # | Gap | Status on 29 Oct 2026 |
|---|---|---|
| a | 78 authentic responses exist only as page images inside Pearson reports | **Blocked** — the PDFs cannot be obtained here; worklist below |
| b | November 2025 P1, June 2026 P1, June 2026 P2, May/June 2021 P1 have no usable examiner report | **3 of 4 now explained: the reports exist but are centre-gated for 12 months** (public from ≈Jan 2027 and ≈Aug 2027, or obtainable today via school ResultsPlus access); May/June 2021 has no report at all |
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

**New route found 29 October 2026 (partial).** Pearson's own text layer over the reproduced scripts is OCR of the handwriting, and it survives on some pages only. In the June 2025 reports it exists for the Section A scripts on printed pp. 18–30 and is absent for the Q8 and Section C script pages, and the workspace cannot download the PDFs, so most locators remain out of reach. What is reachable is collected in [`Source_Notes/June_2025_OCR_route_extracts.md`](Source_Notes/June_2025_OCR_route_extracts.md) — four June 2025 Section A scripts, labelled as OCR-route raw material and **deliberately not counted** in the authentic index. Promote them only if a facsimile arrives. The route itself, with its page limits, is documented in [`Source_Notes/Report_Access_Routes.md`](Source_Notes/Report_Access_Routes.md).

---

## 2. Gap (b) — the four papers without a usable *public* examiner report

| Paper | Position | Evidence |
|---|---|---|
| **May/June 2021 P1** | **No report exists** — this was the optional/unseen assessment series | Report index for the series has no file for it; treated as structural, not an access gap |
| **November 2025 P1** | **Exists — centre-gated until about January 2027** | Pearson released International GCSE November-series examiner reports on **27 January 2026** into its secure download area, and on ResultsPlus from results day (22 January 2026): four December-2025 subject updates (Economics, Business, Geography, Computer Science) carry that date, and the Computer Science update labels the route "secure download". Not publicly downloadable yet because examiner reports for the most recent 12 months are centre-only. Full evidence in `Source_Notes/Report_Access_Routes.md` §6 |
| **June 2026 P1 (4EB1/01R)** | **Exists — centre-gated until about August 2027** | Same rule: released to centres in the August 2026 results window, public roughly twelve months later. The newest publicly downloadable 4EB1 reports are the June 2025 pair, which is exactly the 12-month boundary |
| **June 2026 P2 (4EB1/01)** | **Exists — centre-gated until about August 2027** | Same; note that Pearson has historically published a single report per paper, so the June 2026 pair should yield two files (`4EB1_01_…_ER` and `4EB1_01R_…_ER`) |

**Correction of record (29 October 2026).** These three rows previously read "Not located", with filename probing and search absence offered as the evidence. That framing was wrong: the reports are not missing, they are behind a login, and the 12-month rule explains the boundary exactly (newest public file = June 2025; everything newer is gated). The earlier "publication may be delayed" note is withdrawn.

**How to close these three gaps without waiting.** Anyone with Edexcel Online or ResultsPlus access — the user's school will have it — can download the November 2025 and June 2026 reports today, since they were on ResultsPlus from results day. Dropping those PDFs into `Paperlords_Archive/IGCSE/4EB1_English_Language_B/November_2025/` and `…/June_2026/` would let this bank transcribe any reproduced scripts and complete its commentary layer.

**What this costs and what it does not.** Each of these papers still has a complete mark scheme in the local archive, so every answer set is mark-scheme-anchored. What is missing is the examiner commentary layer (what candidates actually did, what examiners warned about) and any possibility of an authentic script from those series. Coverage is unaffected: all 253 entries are complete and no answer claims a score it has not got.

**What would change the position.** Nothing in the bank has to wait: if a copy of the November 2025 or June 2026 report is supplied (school access), the commentary and any reproduced scripts can be worked immediately. Otherwise the public copies should appear from about January 2027 and August 2027 respectively — worth a re-check then rather than now. May/June 2021 P1 stays structural: that series did not run normally, so no report exists to find.

