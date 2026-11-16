# 4BS1 — verification pass, 9 November 2026

**Question this answers:** is the Business bank actually right, or does it only look right?

**Method:** nothing below is taken from the bank's own prose. Every claim is re-derived from the
38 question papers, the 38 mark schemes, the five stored examiner reports, and — where a document
is not stored — from Pearson's live pages, re-fetched and compared word for word.

---

## 1. What already existed, and what it can prove

The bank ships 19 verification scripts. I ran every one that does not need network access.

| Script | What it proves | Result |
|---|---|---|
| `verify_by_paper.py` | 38 files × 26 items = 80 marks; tariff histogram 12/4/4/3/2/1 | **PASS** — 988 items, 3,040 marks |
| `verify_block_tiers.py` | each 6/9/12 block prints its own mark and label | **PASS** — 114/114, 76/76, 38/38 |
| `verify_chain_bank_anchors.py` | 225 model answers each carry a label; no mapping contradicts its official block | **PASS** |
| `verify_paper_coverage.py` | every governed part of every held paper is answered | **PASS** |
| `verify_ms_point_coverage.py` | every mark-scheme point is at least named in its entry | **PASS** — 0 absent |
| `verify_coverage_claims.py` | 18 retired figures each sit next to their correction | **PASS** |
| `tally_exemplars.py` | 148 register rows resolve to a real file:line and a real mark token | **PASS** — 148/148, 0 uncited |
| `verify_boundaries.py` | boundary tables agree with Pearson; additivity rule supported | **PASS** (4 component-sum anomalies explained) |
| `check_ms_qp_agreement.py` | 12-mark stems in QP and MS agree | **5 mismatches flagged** → investigated, see §3 |

**Conclusion so far:** the bank's internal consistency is real, not asserted. That is unusual and it
should be said plainly. But internal consistency is exactly what a mis-paired archive defeats — every
one of those checks passed on a broken paper.

---

## 2. The checks that were missing — and what they found

### 2.1 Does each mark scheme belong to its question paper?

Nothing in the bank tested this. It is now `audits/audit_archive_pairing.py`, and it tests two
independent things: whether the QP's 12-mark stem appears in the MS at all, and whether the two
documents share the case-study business names.

**Result: 28 pairs match by stem, 9 have no stems in the MS and were verified by case name, 1 fails.**

**The failure is June 2026 P1.** The QP is about **Crumb**; the MS is about **Violet Cakes**; the
QP's 12-mark stem appears nowhere in the MS; the two share no case name; the log numbers differ
(P79457R vs P79457A). Full evidence in `../KNOWN_DEFECTS.md` §D1. The By_Paper file now carries a
warning. **This is the single most important thing this pass found: a candidate could have revised
from answers to a paper that does not exist.**

### 2.2 Is the By_Paper content actually verbatim?

All 988 blocks were compared to their own mark scheme. Contiguous-match testing flagged 156; a
word-coverage test showed almost all of those are artefacts of two-column mark schemes being
reflowed (the MS's "Award 1 mark for correctly substituting…" column interleaves with the working),
plus `Café` → `Caf` and `AO2` → `A02` typing variants. **No block was found whose content is not in
its mark scheme.** The "reproduced verbatim" claim survives — with the caveat that "verbatim" means
word-for-word, not layout-for-layout.

### 2.3 Are the stored examiner reports what the bank says they are?

`Sources/Official_Pearson/May2023_P2_Examiners_Report_Excerpts_Q3e_Q4c.pdf` was read in full. It
contains exactly what the filename claims: the report's commentary on Q3(e) and Q4(c), the printed
5/9 script and the printed 10/12 script. Used directly to mark a real candidate this session.

### 2.4 Are the external quotations real? (the load-bearing one)

The bank's highest-authority document is `00_Pearson_Official_Rulebook.md`, built from Pearson's
**International GCSE Business assessment support page**. That page was re-fetched on 9 November 2026
and is still live, still dated **26 August 2026**. Four claims were checked word for word:

- *"Candidates do not have to consider both options in their response. Candidates can achieve the
  full marks only considering the one option."* — **present, exact.**
- *"An 'explain' question does not need to be in context as there are no AO2 marks available."* —
  **present, exact.**
- *"'Explain' questions, for instance, should only require three sentences… Anything more is not
  required and wastes time."* — **present, exact.**
- *"Using the name of the business is not application (AO2) as the name of the business is used in
  the question."* — **present, exact.**

The bank's most important page is not invented. That is now evidence, not trust.

**A correction to this report's own first draft.** When the page was fetched I wrote that two
further rules — the answer-line mechanic ("if the answer is correct on the answer line, the examiner
will automatically give 2 marks… if the final answer is not to 2 decimal places the candidates will
not gain access to the full marks") and the AO4 balance rule ("the points of evaluation should be
**as detailed as the AO3 points**") — were missing from the rulebook. **They were not missing.**
Both were already in `00_Pearson_Official_Rulebook.md`, at §CALCULATE and at the 12-mark Examiner
Tip, quoted exactly. The check confirmed the bank; it did not correct it.

That mis-statement is left visible here on purpose: it is the same failure the bank warns about
elsewhere — asserting a gap before searching for it. The search took one `grep`.

---

## 3. The five `check_ms_qp_agreement.py` mismatches — investigated, not assumed

| Session | Paper | Verdict |
|---|---|---|
| June 2026 | P1 | **Real defect** — see §2.1 |
| May–June 2022 | P1R | False alarm: the script truncated the stem at 40 characters; the full stem matches (0.74 similarity on truncated text) |
| May–June 2024 | P1 | False alarm, same cause |
| May–June 2025 | P1 | False alarm, same cause |
| May–June 2025 | P1R | False alarm, same cause |

The script's own similarity threshold was too strict for stems that wrap across a column. **The
script is right about the one real defect and noisy about four that are not.** It is retained
because on the real one it was the only thing in the repository that raised a hand.

---

## 4. Marking quality — checked against Pearson's printed scripts

Two handwritten scripts from `uploads/` were marked this session against their real mark schemes:

| Script | Scope | Mark | Calibration |
|---|---|---:|---|
| May 2023 P1 (Irsi Chocolatier) | **full paper**, 26 answers | **55/80** | every level anchored to a printed 0/3, 2/3, 3/3, 6/6, 10/12 script |
| May 2023 P2 (IKEA) | 4 questions only | **15/30** | anchored to printed 0/6, 3/6, 5/9, 10/12 |

Records: `../Mock_Records/`.

During the second marking, **one mark was nearly recorded wrong**: 4(a) looked like a 20.48%
answer, but the mark scheme's own figure is 67 590 ÷ 330 606 = 20.44, exactly what the candidate
had written. The lesson is recorded in the file: **the mark scheme outranks the marker's arithmetic.**

---

## 5. What is still not verified, and cannot be from here

| # | Unverified | Why | Consequence |
|---|---|---|---|
| 1 | **132 of 148 exemplar rows** | the reports they come from were read online and never stored | the register proves its own consistency, not its sources |
| 2 | **Which June 2026 P1 document is misfiled** | needs Pearson's 2026 report, centre-gated to ≈Aug 2027 | the pair is quarantined, not repaired |
| 3 | **Nine MS files' question stems** | those mark schemes print no stems | pairing proved by case name only |
| 4 | **2024–2026 examiner reports generally** | centre-gated for 9–12 months | the newest examiner guidance in the bank is May 2023 |

**The fix for #1 is not research, it is storage:** the ~15 published 4BS1 examiner reports are
freely available and would take roughly 10 MB. Every one of them is a primary source this bank is
currently quoting without holding.

---

## 6. Verdict

- **The structure is sound.** 38 papers, 80 marks each, every governed part answered, every model
  labelled, everything internally re-derived by scripts that fail loudly.
- **The doctrine is sound and now externally re-verified** on its four most load-bearing quotations.
- **The archive is not sound in one place**, and the bank had no test that could see it. That is
  fixed: the test exists, it fails on the bad pair, and the bad pair is now quarantined in public.
- **The exemplars are the weak layer**, not because they are wrong but because they are
  unverifiable from the repository. Until the reports are stored, `[VERIFIED CANDIDATE EXEMPLAR]`
  means "verified when it was read", not "verifiable now".
