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

**What can be verified, was.** On 9 November 2026 the June 2022 4BS1/02R report was retrieved
again from Pearson and compared to this bank's transcription of the Cadbury 1-mark pair. It
matches **word for word**, including the examiner tip *"Try and avoid using the name of the
scenario but include something that is related to the business… perhaps including chocolate cake
designers"*. One load-bearing citation checked, one exact match. That is evidence for the method;
it is not evidence for all 148 rows.

**What would close it.** Store the 15 published 4BS1 examiner reports alongside the archive
(roughly 8–12 MB). The URLs are already recorded in `06_External_Source_Library.md`.

---

## D5 — The archive holds 5 of the ~15 published 4BS1 examiner reports

**Severity: medium. Status: documented.**

Local: May 2023 P1, P1R, P2, P2R and June 2026 P1R. Everything else in the bank's exemplar
register was read from a report that is not stored. Reports for November 2024 onwards are
centre-gated for twelve months; the older ones are freely available and could be stored.
