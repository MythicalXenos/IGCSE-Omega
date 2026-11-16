# The script census — what the reports actually print, and what the register can prove

**Second pass, 9 November 2026.** This one does not check the bank against itself. It counts
scripts in the five examiner reports held on disk, question by question, and then walks every one
of the 148 register rows to the page that is supposed to carry it.

Tools written for this pass:

- `audits/audit_tier_inventory.py` — per-question script counts, each mark line printed for eyeballing.
- `audits/audit_register_against_er.py` — every register row → the report (or Pearson exemplar
  booklet) it cites; pass only if a printed mark line matches.
- `audits/audit_er_script_inventory.py` — first, cruder version; kept because it produced the
  error described in §1.

---

## 1. A finding I published and then had to withdraw

Earlier in this pass I recorded that the 3-mark section of `09_Verified_Tally.md` claimed **47**
scripts while its table held **106** rows — an unreconciled header.

**That was my bug, not the bank's.** My section splitter treated `## 1 MARK SCRIPTS` and
`## 2 MARK SCRIPTS` as continuations of the 3-mark section, so 47 + 36 + 23 = 106 rows were
counted as "3-mark rows". The header breakdown (Jun 2019 ×3 · Jun 2022 ×10 · Jun 2023 ×16 ·
Jun 2024 ×8 · Jun 2025 ×6 · Jun 2026 ×4 = 47) reconciles **exactly** with the 47 rows that are
actually there.

The check that settles it: 2 + 15 + 25 + 47 + 36 + 23 = **148**, the headline figure. The file
was internally consistent the whole time. Withdrawn, and stated here so the mistake is on the
record rather than quietly deleted.

**What this cost:** one turn spent attacking a defect that did not exist. **What it bought:** a
section splitter that is now used by both new tools, and a rule — *read the table through its own
header, never through a regex that guesses where sections end.*

---

## 2. The census — scripts printed in the five held reports

Every mark line was matched with the four phrasings the reports actually use, and each capture
was printed for eyeballing before it was counted:

> `This response scored N marks.` · `Total: N marks` · `This response was Level 3 – N marks.` ·
> `This is a Level 3 response – N marks.` · `This response gained a Level 2 – N marks.`

"Full" below includes 1- and 2-mark parts, where the printed script is often the full mark.

| Report | Scripts printed | Full-mark scripts | Full by tier | Top script |
|---|---|---|---|---|
| May/Jun 2023 P1 (4BS1_01) | 22 | 18 | 4×1, 4×2, 4×3, 3×6, 2×9, 1×12 | **12/12** at Q4(c) |
| May/Jun 2023 P1R (4BS1_01R) | 20 | 17 | 5×1, 3×2, 4×3, 3×6, 2×9, 0×12 | 9/9 at Q2(f), Q3(e); Q4(c) tops out at **4/12** |
| May/Jun 2023 P2 (4BS1_02) | 33 | 9 | 2×1, 2×2, 4×3, 1×6, 0×9 | 10/12 at Q4(c); Q2(f) tops out at **7/9** |
| May/Jun 2023 P2R (4BS1_02R) | 37 | 15 | 6×1, 3×2, 3×3, 2×6, 1×9 | 10/12 at Q4(c); Q2(f) tops out at **8/9** |
| Jun 2026 P1R (4BS1_01R) | 39 | 16 | 6×1, 4×2, 4×3, 2×6, 0×9 | 11/12 at Q4(c); Q2(f) tops out at **8/9** |
| **total** | **151** | **75** | 3+ tiers: 3/3×19, 6/6×11, 9/9×5, 12/12×1 | — |

Two consequences worth stating plainly:

- **A paper can print no full-mark script at its hardest question.** P1R 2023 prints a 4/12 at
  Q4(c) and a 1/2 at Q3(c). That is Pearson's own evidence that the top band is not a formality —
  and it is also why the bank's "perfection" tier leans on so few P1R scripts.
- **The "no full mark printed" cases are real, not gaps in the search.** P2 2023 has no 9/9; P2
  and P2R 2023 and P1R 2026 have no 12/12.

### The 1- and 2-mark tier: 80 is correct

Independent count: **47** scripts on 1-mark parts + **33** on 2-mark parts = **80**, which is
exactly what `layer_c_1_2mark_coverage.py` reports. Of those, the four May 2023 reports print
**58**; the other 22 are in the June 2026 P1R report. The tally sentence *"the archive prints 80"*
means all five reports; if it ever meant the four 2023 papers it should read 58. Not edited —
flagged as a wording risk, not a factual error.

### Full-mark coverage in the four May 2023 reports

| Tier | Full marks printed | Register rows for that series | Verdict |
|---|---|---|---|
| 3/3 | 16 | 16 | complete |
| 6/6 | 9 | 9 (7 labelled May/Jun 2023 + 2 labelled Jun 2023) | complete |
| 9/9 | 5 | 5 | complete |
| 12/12 | 1 | 1 | complete |
| June 2026 P1R: 3/3 ×4, 6/6 ×2 | 6 | 6 | complete |

No printed full mark in the held reports is missing from the register, and no register row claims
a full mark the report did not print.

---

## 3. Row-by-row: what 148 rows can actually be proved

Each row was resolved to a paper and question, then matched against the printed mark lines for
that question.

| Outcome | Rows |
|---|---|
| **Verified** — a printed mark line states the row's mark | **82** |
| **Not held** — the row cites a report that is not in the repository | **54** |
| **Zero half of a pair** — row is the rejected script in the 1- or 2-mark tier (section text says so) | **11** |
| **Booklet silent** — June 2019 P1R row for a question the exemplar booklet does not cover | **1** |
| **Contradicted** — row claims a mark the report never printed | **0** |

Two things follow.

**The 82 include every June 2019 row the exemplar booklets cover.** The Paper 1/1R and Paper 2
June 2019 exemplar booklets are Pearson publications held in `Sources/Official_Pearson/`, and they
print each response with its score. All six June 2019 rows traced (Q1(f) 3, Q1(g) 6, Q2(d) 3,
Q3(e) 9, Q4(b) 6, P1R Q1(g) 6). That is a stronger source than an examiner report, because the
booklet is a teaching document Pearson published openly.

**The 54 are not a scandal, but they are the bank's real exposure** — 36% of the register rests
on documents nobody can open from inside this repository.

---

## 4. Where the register's own numbers overstate what is held

`09_Verified_Tally.md` §"1 MARK SCRIPTS" says *"every one of them is now transcribed"* and cites a
coverage check that scans **five** reports. That is true of the five reports. It is not true of
*the archive* in the sense of "everything Pearson published", because nine series of reports are
never scanned. The sentence should not be read as a claim about the qualification.

---

## 5. The exemplar booklets: a second, better source — with a catch

The Pearson exemplar booklets for Paper 1/1R and Paper 2 (June 2019) are un-gated and were
retrieved live during this pass. Their contents are exactly what the register needs: question,
mark scheme, two or three candidate responses, the score each was given, and the examiner's
reasoning.

Paper 2's booklet is the answer to a question the bank had ruled out: does Pearson ever print a
P2 12-mark response? It does — **Q4(c), 8/12 and 7/12**. No 12/12. So the bank's "no verified
12/12 for Paper 2, in any series" survives contact with the source it was least able to check.

**The catch.** The copy of the Paper 1 booklet stored in `Sources/Official_Pearson/`
(`4BS1_Paper1_Exemplar_Commentaries_June2019.pdf`) has a text layer containing the examiner
comments but **not the candidate scripts and not the mark-scheme tables** — those are image-only
in that file. The live Pearson PDF has them as text. Consequence: the bank's transcription of the
script bodies cannot be checked against the stored copy, only against the live one. Any audit that
greps the local corpus for a quoted candidate sentence will therefore report a false miss.

This is also the cleanest explanation for the 2 128 "not found" spans in `audit_quotes.py`: the
corpus is missing the two exemplar booklets' script bodies, the May 2023 and June 2026 scripts are
images, and the Pearson web-page quotes were never in the corpus at all.

---

## 6. Acquisition: what was tried, and what Pearson will give up

| Route | Result |
|---|---|
| `curl` / `wget` to qualifications.pearson.com | blocked — `SSL_ERROR_SYSCALL`, HTTP 000 |
| Pearson qualification / exam-materials landing pages | 404 through the fetch tool; the site's page URLs are not discoverable from here |
| Pearson direct PDF (`/content/dam/.../4bs1-0X[-r]-pef-YYYYMMDD.pdf`) | the exemplar booklets resolve; examiner-report filenames need exact publication dates and the two guessed dates both 404'd |
| Pearson exemplar booklets (Paper 1/1R, Paper 2, June 2019) | **retrieved in full** |
| pdfcoffee mirror of a 2024 examiner report | 503 |
| Scribd mirror | accessible only as a stub; document body not served |
| paperlords.org/igcse | exhaustively mapped last pass — holds only the five reports already stored |

Pearson also states on its own assessment-support page that examiner reports are withheld behind
Edexcel Online for the first nine months after a series. The reports the register needs (2022,
2024, 2025) are outside that window, so they exist publicly — but this environment cannot reach
them, and cannot be given credentials.

**Therefore: the remaining 54 rows cannot be closed from here by retrieval.** They can be closed
by storing the PDFs, which is a download this sandbox cannot perform.

---

## 7. Verdict

- The register's arithmetic is sound: 148 rows, every section total reconciles, no contradiction
  found in any row that could be tested.
- Full-mark coverage of the four May 2023 reports and June 2026 P1R is **complete** at every tier:
  3/3, 6/6, 9/9, 12/12 — nothing printed and unbanked, nothing banked and unprinted.
- **82 of 148 rows are now traceable to a printed score line in a document held in the
  repository.** Before this pass the number was zero.
- **54 rows remain unproven**, and they are unprovable without the 2022, 2024 and 2025 reports.
- Two of the bank's own cautionary claims — "no 12/12 exists for Paper 2" and "the 1/2-mark tier
  is fully transcribed" — were tested against primary sources and held.
- One claim of my own was wrong and is withdrawn in §1.
