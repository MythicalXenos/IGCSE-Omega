# KNOWN DEFECTS — 4BS1 bank, archive and sources

**Started 9 November 2026.** Every entry below was found by checking a document against another
document, not by reading the bank's own prose. Each entry states the evidence, the consequence,
and what was done about it. Nothing is fixed by assertion.

---

## D1 — June 2026 P1: the question paper and the mark scheme are not the same paper

**Severity: high — it corrupts a whole By_Paper file. Status: contained, not fixable from here.**

**Evidence.**

| | Question paper | Mark scheme |
|---|---|---|
| File | `…_June_2026_P1_QP.pdf` | `…_June_2026_P1_MS.pdf` |
| Cover code | 4BS1/01 | 4BS1/01 |
| Log number | **P79457R** | **P79457A** |
| Publication code | — | **4BS1_01_2606_MS** |
| The business throughout | **Crumb** (20 mentions) | **Violet Cakes** (31 mentions) |
| Final 12-mark stem | "Evaluate the extent to which quality will give **Crumb** a competitive advantage" | "…will give **Violet Cakes** a competitive advantage" |

Both are genuine Pearson documents. They are not a pair. A normalised containment test puts the
QP's 12-mark stem in the MS at **zero**; the two documents share **no** case name.

**Consequence before the fix.** `Perfect_Answers/By_Paper/4BS1_June_2026_P1.md` reproduced the
Violet Cakes mark scheme under the heading "June 2026 — Paper 1", so a candidate revising from it
was reading answers to a paper they would never sit. Every internal check passed, because
`verify_by_paper.py` verifies structure (26 items, 80 marks) and structure cannot see content.

**What was done.** A warning banner now heads that file, and
`audits/audit_archive_pairing.py` now tests every one of the 38 pairs by content. It is the first
check in the bank that can fail on a mis-paired paper.

**What is still unknown.** Which document is the misfiled one. The MS carries the standard
publication code for the standard paper, which suggests the *paper* is the odd one — but the
paper's own cover says 4BS1/01. Resolving this needs Pearson's 2026 examiner report, which is
centre-gated until approximately August 2027. Until then the pair is treated as **unusable for
question-specific revision**, and the MS content is retained only as general indicative content.

---

## D2 — Nine mark schemes print no question stems

**Severity: low. Status: verified by case name instead.**

May/June 2019 (all four papers), May/June 2020 (all four) and November 2021 P1 print answer
content without restating the question. This is why `verify_by_paper.py` shows those files with
no `**Question:**` lines — and it is correct behaviour, not a gap: **no question text was invented
to fill the hole.** The pairing for all nine was confirmed by case name instead
(Backyard Shoez, Lavender, Yellow, Tata, Loaf, TADS, HRMW, Emirates, Artify Studio).

---

## D3 — The May/June 2020 mark schemes are titled "November 2020"

**Severity: cosmetic. Status: recorded.**

Each May/June 2020 MS cover reads "November 2020" while the matching QP cover reads
"Tuesday 2 June 2020". The content pairs correctly (HRMW appears 21 times in the QP and 24 times
in the MS). Pearson appears to have published the 2020 series mark schemes under a November
heading; the archive filename is not at fault. Do not "correct" the files.

---

## D4 — 148 verified exemplars rest on documents that are not in this repository

**Severity: medium, and it is the bank's largest structural weakness. Status: partially verified.**

`09_Verified_Tally.md` registers 148 full-mark scripts. Most are quoted from Pearson examiner
reports that were read online and never stored, so **the register cannot be re-verified from the
repository alone** — only its internal consistency can be (`tally_exemplars.py`, 148/148 rows
resolve).

**Re-measured 9 November 2026, row by row (`audits/audit_register_against_er.py`): of the 148
rows, 82 trace to a printed score line in a document that is in this repository, 54 cite a report
that is not held, 11 are the rejected half of a 1- or 2-mark pair and are correct as such, and 1
names a June 2019 question the exemplar booklet does not cover. Zero rows were contradicted by
the report they cite.**

**What can be verified, was.** On 9 November 2026 the June 2022 4BS1/02R report was retrieved
again from Pearson and compared to this bank's transcription of the Cadbury 1-mark pair. It
matches **word for word**, including the examiner tip *"Try and avoid using the name of the
scenario but include something that is related to the business… perhaps including chocolate cake
designers"*. One load-bearing citation checked, one exact match. That is evidence for the method;
it is not evidence for all 148 rows.

**What would close it.** Store the published 4BS1 examiner reports for 2022, 2024 and 2025
alongside the archive. **Retrieval from this environment is not possible** — see D5.

---

## D5 — The archive holds 5 of the ~15 published 4BS1 examiner reports

**Severity: medium. Status: documented.**

Local: May 2023 P1, P1R, P2, P2R and June 2026 P1R. Everything else in the bank's exemplar
register was read from a report that is not stored. Pearson withholds examiner reports behind
Edexcel Online for the first nine months after a series; the older ones are public.

**Attempted and failed, 9 November 2026:** `curl`/`wget` to qualifications.pearson.com return
HTTP 000; the qualification and exam-materials landing pages return 404 through the fetch tool;
guessed direct-PDF names (`4bs1-02r-pef-20240822.pdf` and a 2025 equivalent) both 404; the
pdfcoffee mirror returns 503; Scribd serves a stub only. The only files that resolve are the
un-gated teaching materials, and those were retrieved.

---

## D6 — The stored June 2019 Paper 1 exemplar PDF has no text layer for its scripts

**Severity: low for the reader, high for any automated quote check. Status: documented, workaround known.**

`Sources/Official_Pearson/4BS1_Paper1_Exemplar_Commentaries_June2019.pdf` extracts the examiner
comments as text but leaves **the candidate responses and the mark-scheme tables as images**. The
same document served live by Pearson has both as text.

Consequence: `audits/audit_quotes.py` will report every quoted candidate sentence from
`2019-06_P1_Official_Exemplar_Booklet.md` as "not found", and it is wrong to read those misses as
fabrication. The same applies to the Paper 2 booklet's stored copy, which is "selected pages"
only.


---

## D7 — 77 citations do not use the question paper's own words (57 of them are the mark scheme's)

**Severity: low to medium. Status: located, not yet fixed.**

In `10_Chain_Bank.md`, 24 of 363 quoted questions put the mark scheme's expansion of an option
inside the quotation marks attributed to the paper. On 9-mark justify questions the paper prints
only a label (*"Option 1: casual employees"*); the scheme explains what that means (*"some
employees like the option of being 'on call'"*). The bank quotes both as one sentence.

**Verified against primary sources:** #193 (May 2023 P1R), #217 (May–June 2024 P2R), #224
(June 2025 P2) — the substance is right in each case, the attribution is not.

**Fix — done 9 Nov 2026.** The full list is written out in
`Perfect_Answers/10a_Citation_Corrections.md`, item by item, with the paper's own wording beside
each. The strict re-count found **77** citations that are not the paper's exact words: **57**
option-label cases, **14** condensed stems and **6** read by hand. The earlier figure of 24 came
from a looser test and is superseded by the 77. A note at the head of `10_Chain_Bank.md` now says
so. **No answer needed rewriting, and no wrong question was found.**

**Measured by** `audits/build_citation_corrections.py` and `audits/audit_question_quotes.py`.

---

## D8 — Pearson's own mark scheme contains an arithmetic error, and the bank copied it

**Severity: low for the exam, high for learning. Status: FIXED 9 November 2026.**

May–June 2020, Paper 2R, 1(a)(iii): a football costs 1,060 rupees, sells for 1,600. The correct
answer, D = 50.94%, is right: (1,600 − 1,060) ÷ 1,060 × 100 = 50.94%.

The distractor explanations are wrong:

- *"1 600 / 1 060 = 15.09"* — the true value is 1.509, i.e. **150.94%**.
- *"1 600 – 1 060 = 0.52 / 1 600"* — the true subtraction is **540**, giving 540 ÷ 1,600 × 100 =
  **33.75%**, which is the figure the scheme prints.

Verified against the printed PDF text, not the searchable index, so this is Pearson's error and not
a scanning artefact. The bank had reproduced both lines verbatim.

**Fix applied:** a correction note now sits under the two lines in
`Perfect_Answers/By_Paper/4BS1_May-June_2020_P2R.md`.

**Why it matters beyond this question:** it is the one place in 38 papers where "quoted verbatim
from Pearson" and "arithmetically correct" pull in opposite directions. Every other calculation in
the archive recomputes cleanly.

---

## D9 — `7 239 / 85 038` is a denominator typo in Pearson's own June 2022 Paper 2R scheme

**Severity: low for the exam. Status: OPEN — logged, not corrected, because the graded answer is unaffected.**

June 2022, Paper 2R, Q1(e): the scheme's working prints `7 239 / 85 038`, while the base figure in the
same question is **85 083**. The graded outcome does not change, so this is a transcription slip in
Pearson's own working, not a marking error. It is logged rather than "fixed" in the bank because the
bank quotes the scheme verbatim; the note sits beside the quote.

---

## D10 — June 2022 Paper 1R Q3(d): the bank quoted half the answer and drew the wrong lesson

**Severity: high for technique. Status: FIXED 12 November 2026.**

The entry quoted the first paragraph of a 6/6 Analyse and described it as *"the negative chain… this
reaches 6/6 on its own"*. **The scan shows two paragraphs — negative, then positive — and the examiner
praises the candidate for having both:** *"the candidate has thought about the positives of customers
using social media to review Can Culleretes and the negative effects as well."*

A student following the old note would write a one-sided answer and lose half of what the examiner
paid for. The second paragraph is now quoted, the claim is corrected in place, and the whole script is
transcribed at `audits/corpus/transcripts/4BS1_01R_2206_3d.md`.

**Why it was missed:** the answer is a scanned image. The PDF's text layer carries the examiner's
comment and nothing else, so quoting "the script" meant quoting whatever had been read by eye, once.

**Measured by** `audits/audit_quotes_vs_textlayer.py` — which now lists **52** further long quotes that
are not in any report's text layer, i.e. read from scans, and which therefore need the same check.

---

## D11 — June 2022 Paper 1R Q1(g): the quote dropped a chain and called legible words illegible

**Severity: medium. Status: FIXED 12 November 2026.**

The bank's quote omitted the candidate's middle chain (*"higher production capability… produce more
meals"*) and marked three words as unreadable (`[productivity]`, `[didn't]`, `[reduce]`) that read
cleanly at 2× on the scan. Replaced with the full transcription, `[Although]` alone still supplied
because the crop cuts it at the left margin.

---

## D12 — the extraction tool paired 42 script images with no score

**Severity: tooling only. Status: FIXED 12 November 2026.**

`audits/extract_scripts.py` finds each script image, renders it and attaches the score printed for it.
Its first version paired **415 of 457**; the other 42 opened an answer booklet with no score line of
their own, or had the score printed *above* the picture, or on the following page. Both cases are now
handled (look above the picture; walk forward to the next page, stopping at the next question
heading). The 42 that remain unpaired are booklets, not failures.

**The rule this repeats:** a tool that reports a gap where there is none is worse than no tool.

---

## D13 — every script quote in the bank was presented as if it came from the report's text

**Severity: high — this is the bank's own labelling rule, broken 352 times. Status: FIXED 12 November 2026.**

Pearson prints each marked script as an **image**. The report's text layer carries the examiner's
commentary and, usually, the question — **not the candidate's answer**. So a quote from a script is
almost always a **transcription**, and the bank's rule (in `00_Pearson_Official_Rulebook.md`) says a
transcription must say so. **Two quotes in the entire bank said so.**

`audits/audit_quotes_vs_textlayer.py` was rewritten to attribute each quote to the report it belongs
to by walking the file for the last citation line, rather than skipping any file that quotes more
than one report. Before the rewrite it **skipped 20 of the 20 consolidated files**, including
`02_Verified_Exemplars.md` and `10_Chain_Bank.md` — the two files holding most of the bank's long
quotes. Its "0 unsupported" result was therefore vacuous.

**What the fixed tool found, at 25+ words:**

| Where the quote's words actually are | Quotes |
|---|---|
| in the held report's text layer (checked, ~100% of 6-word runs found) | the majority |
| **not** in the text layer, report held → script image | **157, now labelled** |
| **not** in the text layer, report **not held** in text form at all | **241, now labelled** |
| quote sits above any line naming a session and paper | 17, **not checked** |
| files that are not script banks (library, rulebook, tally) | excluded |

Two labels are used, and they say different things:

* `[read from the printed script image — these words are not in the PDF's text layer, so they are a transcription, not a copy]`
* `[⚠️ not in any text layer held in this repo — a transcription, not a copy; re-check against the printed page before relying on it]`

**The second label is not a clean bill of health.** It says the bank cannot prove the quote in this
repo. The sessions affected are **June 2019, June 2020, November 2020, June 2022 Paper 2, November
2021, November 2023, November 2024 and June 2024 Paper 2R** — all cited in the bank, none held as
text. Verification of those needs the printed page, not a grep.

**Verified by eye while fixing this:** the Cadbury 0-mark quote (`2022-06_P2R_Cadbury.md`, Q1(d),
p. 8 of `4BS1_02R_2206_ER_full.pdf`) matches the handwriting word for word, including
*"reputation"*, which reads ambiguously in the scan. The transcription was sound; the **label** was
what was missing. That distinction matters — the defect was provenance, not accuracy.

**One false alarm found and removed while doing this:** attributing quotes by any prose mention of a
month pulled 23 quotes from `06_External_Source_Library.md` (news articles, not scripts) into a
Pearson report and reported them as unsupported. Attribution now accepts only citation-shaped lines,
and the non-script files are excluded.

**Follow-up, same day.** Two more attribution bugs were found and fixed while sweeping the files the
first pass could not read: a heading that names only the session (`# May/June 2023 · the four
papers`) was discarded instead of carried, and `P1_ER.pdf`-style filenames were not recognised as a
paper. Fixing them moved 24 quotes from "unchecked" into "checked", which is why the totals above
read **157** and **17** rather than 133 and 45.

**Register damage, and the fix.** Every inserted label shifted the citations below it: 96 rows
first, then 119 once the second batch landed. Three repair heuristics were tried and each made it
worse -- the last one moved rows onto a *different script with the same question number* in a
neighbouring section, and the register started failing on paper as well as line. The working tool is
`audits/resync_register.py`, and it does no searching: it takes the register as it stood before the
labels (`git show 1f38eb2`) and adds the count of label lines above each cited line. Arithmetic on a
known diff. `tally_exemplars.py` then verifies it independently against the files.

---

## D14 — 174 multiple-choice items credited an answer without printing the options

**Severity: high for revision use, zero for doctinal accuracy. Status: FIXED 12 November 2026.**

A 4BS1 paper has eight one-mark multiple-choice questions per paper (some sittings six). The mark
scheme prints:

> *"AO1 - 1 mark. The only correct answer is C. A is not correct because personal savings are an
> internal source of finance…"*

and nothing else — the options live on the question paper. The bank copied the scheme, so the item
read **"the answer is C"** to a reader who had never been shown A, B or D. **174 items across 38
papers** were like this.

`audits/qp_stems.py` now reads the four options from the QP (`A\t Personal savings`), and
`audits/repair_mcq_options.py` writes them under the question, plus the credited option in words:

```
**Options:** A · Personal savings · B · Retained profit · C · Bank loan · D · Selling assets

**Credited option:** **C · Bank loan**
```

**Guard:** only 1-mark items; only where the paper prints exactly four options; only where the
scheme names a letter; and the letter must appear among the paper's options — **0 cases** where it
did not. Where the scheme is silent, nothing is inserted.

The words next to the letter are the paper's, not the scheme's. That is a deliberate mix: **the
letter is Pearson's, the wording is Pearson's, but the pairing is done here**, so the line is
labelled as a *credited option* rather than as a quotation.
