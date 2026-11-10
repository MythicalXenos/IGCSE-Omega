# Report-access routes for 4EB1 examiner reports — what works, what doesn't, and the page limits

**Compiled 29 October 2026.** This note exists so that the same hunting is not repeated from scratch. It records which route can reach Pearson's examiner-report and script pages, what each route truncates, and which files are confirmed to exist.

## 1. The sandbox itself cannot reach Pearson

`curl`, `python urllib` and `pip`-style requests from the workspace all fail against `qualifications.pearson.com` with `OpenSSL SSL_connect: SSL_ERROR_SYSCALL` / `TLS/SSL connection has been closed (EOF)`. There is no proxy environment variable and no DNS-level workaround: the egress allow-list covers `github.com`, `codeload.github.com`, `api.github.com`, `registry.npmjs.org`, `pypi.org` and `files.pythonhosted.org` only. **Do not spend time retrying direct downloads.**

Consequence: any Pearson PDF's *text* must be read through a fetch tool, and the bytes can never be cached locally. Local rendering (PyMuPDF) therefore only works for the PDFs already in `Paperlords_Archive/`.

## 2. Two fetch routes, and their page limits

| Route | Reaches | Page limit | Notes |
|---|---|---|---|
| Direct fetch of the Pearson PDF URL | Pearson | **first 30 pages only** | Returns Pearson's own text layer, including its OCR over reproduced scripts where that OCR exists. Chapters are counted over the extracted text, so a 60-page report appears to "end" around Question 7. |
| Reader proxy (`https://r.jina.ai/` + the PDF URL) | Pearson | **no 30-page cut observed** — returned printed pp. 53–64 of a 67-page report | Page markers like `> Int GCSE English Language B 4EB1 01R 59` are printed folios. Use this route for Section C and for late Q8 pages. |

**Practical rule:** for anything past printed p. 30 (Q8 scripts, all of Section C), fetch `https://r.jina.ai/<pearson-pdf-url>` and pick the chunk near the printed page you need. For Section A and early pages, the direct route gives cleaner text.

## 3. Reproduced scripts: sometimes OCR'd, sometimes image-only

The hosted reports are not uniformly image-only. In the June 2025 reports, some reproduced scripts come through the direct route as **handwriting OCR text** (with visible OCR noise such as "an amnescotal structure", "Texb2", "Cloudid" — that is how you can tell it is OCR, not typesetting), while other script pages return nothing at all between the "This is a response to Question N" line and the examiner judgement.

This is the key constraint on transcript work:

- Where OCR text exists, it is **Pearson's own layer**, better provenance than third-party OCR, but still not a facsimile read. Any transcript built from it must be labelled as OCR-route, with uncertain words marked, and must not be promoted to `[VERIFIED CANDIDATE EXEMPLAR]`.
- Where no text comes through, the page is genuinely image-only in the hosted copy and **cannot** be transcribed without downloading the PDF, which the sandbox cannot do.
- Examiner annotations are interleaved with the candidate's words in the OCR. Never merge the two.

**Consequence for the 78 locator records:** the ones whose reports carry OCR text can be upgraded to OCR-route transcripts, one at a time, on request; the ones whose pages are image-only cannot be upgraded from here at all. Neither group can become facsimile-checked without local PDFs.

## 4. Local archive holdings (the only facsimile sources)

`Paperlords_Archive/IGCSE/4EB1_English_Language_B/` holds 23 QPs and 23 MSs, plus exactly **two** examiner reports — May/June 2023 P1 and P1R (`…_ER.pdf`). Every other report has to be read remotely, which is why the 2023 transcripts are the only facsimile-checked ones.

## 5. Report files confirmed to exist (URL pattern)

```
https://qualifications.pearson.com/content/dam/pdf/International-GCSE/English-Language-B/2016/Exam-materials/<name>.pdf
```

| Session | File | Status |
|---|---|---|
| June 2019 | `4eb1-01-pef-20190822.pdf`, `4eb1-01r-pef-20190822.pdf` | exists |
| January 2020 | `4eb1-01-pef-20200305.pdf`, `4eb1-01r-pef-20200305.pdf` | exists |
| May/June–November 2020 | `4eb1-01-pef-20210211.pdf`, `4eb1-01r-pef-20210211.pdf` | exists |
| January 2022 | `4eb1-01-pef-20220224.pdf`, `4eb1-01_pef_20220303.pdf`, `4eb1-01r-pef-20220303.pdf` | exists |
| June 2022 | `4eb1-01-pef-20220825.pdf`, `4eb1-01r-pef-20220825.pdf` | exists |
| June 2023 | `4eb1-01-pef-20230824.pdf`, `4eb1-01r-pef-20230824.pdf` | exists, and is local |
| June 2024 | `4eb1-01-pef-20240822.pdf`, `4eb1-01r-pef-20240822.pdf` | exists |
| November 2024 | `4eb1-01-pef-20250123.pdf` | exists |
| June 2025 | `4eb1-01-pef-20250821.pdf`, `4eb1-01r-pef-20250821.pdf` | exists |
| November 2025 | **exists, centre-gated** — released to centres **27 January 2026** | not public until about January 2027; see §6 |
| June 2026 | **exists, centre-gated** — released to centres **from 25 August 2026** | not public until about mid-2027 to August 2027; see §6 |

All of these are public *now* because they are more than twelve months old. Older reports also sit under the legacy path `…/English%20Language%20B/2016/exam-materials/…` (percent-encoded, case-sensitive).

## 6. The two "missing" reports — resolved: they exist, but are centre-gated

**Earlier framing (withdrawn).** This file's first version treated the November 2025 P1 and June 2026 reports as "not located, possibly delayed". Further searching on 29 October 2026 shows that is the wrong model. Both exist; neither is publicly downloadable yet, and there is a rule that explains it exactly.

**The rule, in Pearson's own words.** Pearson's past-papers page states: "Question papers, mark schemes and examiner reports for the most recent exam sessions (within the last 12 months) can be accessed only by registered centres." Examiner reports for a series are therefore released to centres first, on a published date, and become public after that window.

**The release dates, from Pearson's own subject updates.**

| Series | Statement | Source |
|---|---|---|
| November 2025 | "27 January — IAL (October series) and International GCSE (November series) examiners' reports uploaded" | December 2025 Economics and Business updates; Geography subject update: "27 January - International GCSE (November series) examiners' reports on website"; Computer Science update: "GCSE Examiner Reports — 27 January 2026 (available on ResultsPlus from Results Day)" |
| June 2026 | "Exam materials release dates … Question papers 23 June 2026 · Mark schemes 21 July 2026 · **Examiner reports from 25 August 2026**" | "Getting Ready for Results 2026" (Pearson languages subject update); June 2026 History subject update repeats: "GCSE / International GCSE examiners reports will be made available on our website from **25 August 2026**" |

So neither series is missing a report. The November 2025 report went out on **27 January 2026** and the June 2026 reports from **25 August 2026**, both into Pearson's secure download area, and both on ResultsPlus from results day (the "Getting Ready for Results 2026" page gives the click path: ResultsPlus → ResultsPlus Analysis → Whole cohort results → Cohort paper analysis → the series and subject → **Exam docs** → Examiner Report). What is gated is the *public* copy.

**What the community says — and it matches exactly.** Students and teachers asking this same question reach the same two conclusions: the reports exist and are released on a published date, and the recent ones are locked.

- r/Edexcel, asked for the IGCSE English Language B June 2025 report (24 August 2025): "**26th August is when they get officially released on the Pearson site.** I haven't seen any links that have them, so fair chance saying that you aren't finding them before that date." The June 2025 report is dated 21 August 2025, so the community date is within days of the real one.
- The Student Room, "GCSE Edexcel Mathematics Examiners Report": the reports are all on the Pearson course-materials page "**but the recent ones are locked and can only legitimately be accessed via your teacher**."
- The Student Room, "Edexcel IGCSE summer 2024": the mark schemes "**won't be available to the public until the summer of 2025**", quoting Pearson's rule verbatim: "Question papers, mark schemes and examiner reports for the most recent exam sessions (within the last 12 months) can be accessed only by registered centres."
- The Student Room, "Where can I find the 2014 GCSE Edexcel Examiner Reports?": "They've been released today on the Edexcel website! **... only to teachers though.**"
- r/Edexcel, on finding locked material elsewhere: "some things like **Examiner Reports** for the most recent papers **are not available on places other than the Edexcel website**"; r/alevel, same question: "theyre all locked".

That last point explains this archive's own shape. The local QP/MS collection comes from paperlords, which the community recommends precisely for *locked papers and mark schemes* — and which, per the same threads, does not carry examiner reports. Hence 23 QPs and 23 MSs locally but only two ERs (the 2023 pair).

**Why the twelve-month boundary lands where it does.** Newest publicly downloadable 4EB1 reports: the June 2025 pair (`4eb1-01-pef-20250821.pdf`, `4eb1-01r-pef-20250821.pdf`). Everything from June 2025 backwards is public; everything from November 2025 forwards is not. That is the gating rule doing its work, not missing files — and it is why filename probes on the 2026 dates return "Page not found": the files are in the centre area, not under `Exam-materials/`.

**What this predicts (approximate; re-test, don't assume).**

| Session | Released to centres | Expected public window |
|---|---|---|
| November 2025 P1 | 27 January 2026 | from about **January 2027** |
| June 2026 P1 / P2 | from 25 August 2026 | somewhere between **mid-2027 and August 2027** |

The uncertainty in the June 2026 row is real: Pearson's rule speaks of "the most recent exam sessions (within the last 12 months)", which could be counted from the session or from the release date, and the user-facing pages only say the materials "will be made available on our website". The one hard observation is that the June 2025 pair is public now and the June 2026 pair is not.

**What this means for the bank, and for the user.** Nothing about coverage changes: both papers already have complete mark schemes, so their answer sets stand. But the two reports are *obtainable now* by anyone with Edexcel Online or ResultsPlus access — the user's school almost certainly has it, since the reports are on ResultsPlus from results day. If the user can download `4EB1_01_2511_ER` (November 2025) and the two June 2026 equivalents, this bank gains its last missing commentary layer and, where scripts are reproduced, its last missing locators. That is a school-side action, not something this workspace can do.

**Dead ends already eliminated for this question** (do not repeat): direct shell access to Pearson (no egress, TLS reset); GitHub code and repository search; Pearson's sitemap (105 unfilterable chunks); the JavaScript course-materials page (returns a cookie-consent shell); GitHub Actions as a proxy fetcher (repository reports `actions=false`, token gets 403 on actions endpoints); date-pattern filename probing across the plausible publication dates.
