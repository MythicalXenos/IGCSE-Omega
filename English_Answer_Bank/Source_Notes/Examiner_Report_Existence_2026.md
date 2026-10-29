# Do the 2026 examiner reports exist, and why can't we reach them?

**Written 29 October 2026.** This note answers two questions that were being conflated: *why* the
November 2025 and June 2026 4EB1 reports cannot be downloaded, and *whether they exist at all*.
It also records which paper a centre in Bangladesh actually sits, because that decides which reports
are relevant. Companion files: `Report_Access_Routes.md` (the search routes), `../OPEN_GAPS.md`
(the gap list).

---

## Verdict in one paragraph

Two reports are relevant to a Bangladeshi centre: **November 2025 4EB1/01** and **June 2026
4EB1/01**. **Both exist and were released to centres on published dates.** Neither is publicly
downloadable, because Pearson keeps the most recent twelve months of exam materials behind a centre
login. The June 2026 **4EB1/01R** report also exists, but 01R is not a paper a centre in Bangladesh
can sit — it is a time-zone-R variant used in 24 named countries, and Bangladesh is not one of them.

---

## 1. Why they are inaccessible

Three separate locks, and all of them are keyed to a *centre*, not to a candidate or a document.

**(a) The twelve-month rule.** Pearson's past-papers page states it directly:

> "Question papers, mark schemes and examiner reports for the most recent exam sessions (within the
> last 12 months) can be accessed only by registered centres."

That is why the newest publicly downloadable 4EB1 report is the **June 2025** pair
(`4eb1-01-pef-20250821.pdf`, `4eb1-01r-pef-20250821.pdf`) and why nothing newer appears on Pearson's
public file path.

**(b) The recent materials live in a secure area.** For the current series the report is published to
Edexcel Online / Secure Download, and to **ResultsPlus** from results day
(ResultsPlus → ResultsPlus Analysis → Whole cohort results → Cohort paper analysis → series and
subject → **Exam docs** → Examiner Report). A candidate login cannot reach that; a centre login can.

**(c) Mirrors cannot carry what the public path never serves.** The aggregator sites that supply
IGCSE papers scrape the *public* `content/dam/.../Exam-materials/` path. Gated files are not in it.
This is the clean explanation for the shape of this archive: **23 question papers, 23 mark schemes,
and only two examiner reports** (the 2023 pair). It is not that the reports were missed; it is that
the source of the papers does not publish them.

**Ruled out this turn — the report is not hidden inside the mark scheme.** The file suffix `rms`
("report and mark scheme"?) invited that hope, so all 23 local mark-scheme PDFs were text-searched
for "Examiners' Report", "Principal Examiner" and "feedback": **zero occurrences across all 23
files**, which run 19–25 pages. The examiner report is always a separate document, published as
*Examiners' Report — Principal Examiner Feedback*.

---

## 2. Bangladesh: which paper is actually yours

This matters because it cuts the shopping list from three documents to two — and because it decides
whether the June 2026 paper in the archive that you should treat as "yours" is the one labelled P1
or the one labelled P2.

Pearson's *May/June exam start times for International GCSE* document names the R-paper countries
exhaustively:

> "The R-paper versions are used in the following countries: *Australia, Azerbaijan, Brunei,
> Cambodia, China, Hong Kong, India, Indonesia, Japan, Korea, Laos, Macau, Malaysia, Mongolia,
> Myanmar, New Zealand, Oman, Pakistan, Philippines, Singapore, Taiwan, Thailand, United Arab
> Emirates* and *Vietnam*."

**Bangladesh is not on that list.** A centre in Bangladesh enters the **main (M) paper, 4EB1/01**.
(The separate list of *subjects* with no R-paper — Arabic, Art & Design, Bangla, Bangladesh Studies,
Computer Science and others — does not include English Language B; the exclusion here is by country,
not by subject.)

The same document settles the November series:

> "For the November exams, only one version of the International GCSE exams is available (no R-paper
> version will be available in November)."

| Series | Codes that exist | Code a Bangladesh centre sits | Archive files |
|---|---|---|---|
| November 2025 | 4EB1/01 only | **4EB1/01** | `November_2025_P1_*` |
| June 2026 | 4EB1/01 and 4EB1/01R | **4EB1/01** | `June_2026_P2_*` (smartphones / social media texts) |

So in the June 2026 pair, the paper a Bangladeshi candidate sat is the one this archive happens to
label **P2**, and the one labelled **P1** is the 01R time-zone variant (handwriting and letters
texts). Both remain useful practice — they are the same qualification, format and standard — but only
the 4EB1/01 report describes what actually happened to candidates in Bangladesh.

*Caveat, stated because it is easy to over-read the table:* the entry code is set by the country the
centre is in, not chosen by the centre or the candidate. Private candidates entered through the
British Council sit under the same country rule.

---

## 3. Do the reports exist? Evidence, graded

| Report | Exists? | Basis | Confidence |
|---|---|---|---|
| **November 2025 — 4EB1/01** | **Yes** | Pearson subject updates for the November series: "27 January — IAL (October series) and International GCSE (November series) examiners' reports uploaded". Results day for the series was 21–22 January 2026, with the reports following on 27 January | High |
| **June 2026 — 4EB1/01** | **Yes** | Pearson "Getting Ready for Results 2026": question papers 23 June 2026, mark schemes 21 July 2026, **examiner reports from 25 August 2026**; the June 2026 History subject update repeats the same 25 August date for GCSE/International GCSE | High |
| **June 2026 — 4EB1/01R** | **Yes** (inferred, not directly evidenced) | Same publication schedule, and every June series for which we hold a public report published a *separate* 01R document: 2019, 2022, 2023, 2024, 2025 | Medium-high |

**A regularity worth knowing.** In some series the 01R commentary is folded into the 01 document
rather than published separately — the November 2020 report says in its opening pages that
"4EB1/01R was very small. Where it is appropriate, comments are made for the 4EB1/01R paper",
i.e. one document covering both. Since November has no R paper at all, this ambiguity can only ever
affect the June rows.

**What is *not* evidence of absence** (all four have been misread as such at some point in this
project):

- a 404 on a guessed filename — gated files are not served on the public path at all, so a correct
  guess and a wrong guess look identical;
- absence from aggregator sites (savemyexams, kingsbridge, paperlords all stop at June 2025);
- absence from search-engine indexes;
- absence from the local archive.

---

## 4. Exactly what to ask for

Publication codes follow the format confirmed inside the published June 2025 report,
`4EB1_01_2506_ER` (session digits `YYMM`). Filenames follow the pattern
`4eb1-0X-pef-YYYYMMDD.pdf`, where **the date is the mark-scheme publication date for that series** —
verified against four sessions:

| Session | Mark scheme file | Examiner report file | Same date? |
|---|---|---|---|
| June 2019 | — | `4EB1_01R_pef_20190822.pdf` | — |
| November 2023 | `4eb1-01-rms-20240125.pdf` | `4eb1-01-pef-20240125.pdf` | Yes |
| June 2024 | `4eb1-01-rms-20240822.pdf` | `4eb1-01-pef-20240822.pdf` | Yes |
| November 2024 | `4eb1-01-rms-20250123.pdf` | `4eb1-01-pef-20250123.pdf` | Yes |
| June 2025 | `4eb1-01-rms-20250821.pdf` | `4eb1-01-pef-20250821.pdf` | Yes |

Applying that pattern to the two missing series:

| Series | Publication code | Likely filename | First public (approx.) | Priority for this bank |
|---|---|---|---|---|
| **November 2025, 4EB1/01** | `4EB1_01_2511_ER` | `4eb1-01-pef-20260127.pdf` | ~January 2027 | **High** — the paper a Bangladeshi centre sat |
| **June 2026, 4EB1/01** | `4EB1_01_2606_ER` | `4eb1-01-pef-20260825.pdf` | ~August 2027 | **High** — the paper a Bangladeshi centre sat |
| June 2026, 4EB1/01R | `4EB1_01R_2606_ER` | `4eb1-01r-pef-20260825.pdf` | ~August 2027 | Optional — extra practice, not a paper Bangladesh can sit |

The filenames are **inferences** from the pattern above, not seen. The publication codes are more
reliable than the filenames — quote a code inside a centre if a search box is involved, since that is
the identifier printed on the document itself. Do not treat a 404 on any of these as new information.

Where they live: **Edexcel Online** → Exam materials / secure download for the series, or
**ResultsPlus** → Exam docs → Examiner Report. Both are centre logins; the school exams officer or
Head of English will have one.

---

## 5. What happens when they arrive

Drop the PDFs into the archive:

- `Paperlords_Archive/IGCSE/4EB1_English_Language_B/November_2025/`
- `Paperlords_Archive/IGCSE/4EB1_English_Language_B/June_2026/`

and say so. They can be used even if the text layer is poor, because the script pages are
**image-only**: with the PDF in hand the pages can be rendered and read, which is exactly what the
OCR route in `June_2025_OCR_route_extracts.md` does. On arrival the work is:

1. extract the question-by-question examiner commentary and add it to the five affected answer sets
   (`November_2025_P1_Q8`–`Q11`, `June_2026_P2_Q8`–`Q11`, plus the 01R sets if that file comes too);
2. locate any reproduced candidate response, record page, score and level, and either transcribe it
   to `[VERIFIED CANDIDATE EXEMPLAR]` or add a `[OFFICIAL CANDIDATE SCRIPT LOCATOR]` row;
3. update the authentic index, `coverage.csv`, `OPEN_GAPS.md` and the cross-source audit in the same
   commit, then re-run the docx/xlsx builders and the link scan.

---

## 6. Dead ends re-tested 29–30 October 2026

Recorded so they are not retried, with the exact behaviour observed.

| Route | Result |
|---|---|
| `examoo.s3.eu-west-2.amazonaws.com/.../25-jun/rep.pdf` | `AccessDenied` (S3 XML error) |
| `examoo.../26-jun/rep.pdf` | `AccessDenied` |
| `.../Teaching and learning materials/4eb1-er-summary-24-06.pdf` | 404 |
| `.../4eb1-er-summary-25-06.pdf` | 404 |
| `.../4eb1-er-summary-25-11.pdf` | 404 |
| `.../english-language-b-2016.coursematerials.html` | 404 (materials pages are dynamic, no static listing) |
| `.../Exam-materials/4eb1-01-pef-20260127.pdf` | 404 |
| `.../Exam-materials/4eb1-01-rms-20260127.pdf` | 404 |
| `.../Exam-materials/4eb1-01r-pef-20260825.pdf` | 404 |
| all 23 local mark-scheme PDFs searched for report text | no report content in any of them |

The 404s are consistent with gating, not with absence — see §3. The only public examiner-report
*summary* document found is `4eb1-er-summary-22-06.pdf` (June 2022), a one-off; no later series
summary exists at that pattern.
