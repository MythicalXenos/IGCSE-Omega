# ARCHIVE LABEL AUDIT — 14 October 2026

Three file-level defects in `Paperlords_Archive/IGCSE/4BS1_Business_Studies/` were
found while opening the 12-mark tier, and two of them had already propagated into
the bank. This note records what was wrong, how it was proved, and what changed.
Run `python3 check_archive_file_labels.py` to re-verify at any time.

---

## 1. 🚨 May/June 2024 — the two mark-scheme PDFs were filed under each other's names

**Proved by the files' own front matter.** Each mark scheme prints its paper code
on page 1; each question paper prints `4BS1/0N` in its footer:

| file | printed inside | content |
|---|---|---|
| `..._May-June_2024_P1_MS.pdf` | **"Paper 01R"** | Café Pinch |
| `..._May-June_2024_P1R_MS.pdf` | **"Paper 01"** | PPS |
| `..._May-June_2024_P1_QP.pdf` | `4BS1/01` | **PPS** |
| `..._May-June_2024_P1R_QP.pdf` | `4BS1/01R` | **Café Pinch** |

**The question papers are correctly named; the mark schemes were swapped.**
Independent confirmation: the examiner reports and every hand-written ER file in
the bank already say *June 2024 P1 = PPS* and *June 2024 P1R = Café Pinch*
(`06_External_Source_Library.md`, `09_Verified_Tally.md`, `External_Exemplars/2024-06_*`).

**Fixed:** the two MS files were renamed to match their printed codes, so
**June 2024 Paper 1 = PPS** and **Paper 1R = Café Pinch**.

**What that corrected downstream** — the block files carry the paper label from
the file name, so before the rename, every May/June 2024 block was attributed to
the wrong paper:

- `layer_c_{3,6,9,12}mark_blocks.txt` regenerated (block **order and index are
  unchanged** — verified by diffing the `===` header lines, 0 differences — so
  every coverage map keyed by block number still points at the same slot).
- `layer_c_3mark_master.csv` — the 8 May/June 2024 rows now read correctly
  (P1: HR function · ineffective communication · decentralised structure ·
  seasonal staff. P1R: venture capital · HR responsibility · partnership ·
  hierarchical structure disadvantage).
- 16 paper citations corrected in `10_Chain_Bank.md` and one heading in
  `05_Constructed_12mark_Models.md` — e.g. *gross profit margin to PPS* is now
  **P1 1(g)**, *Kumaran of Café Pinch* is now **P1R 1(g)**.
- The `COVERED` maps in `layer_c_6mark_coverage.py` and
  `layer_c_9mark_coverage.py` were re-paired to the corrected content (both were
  content-based, so blocks 55–60 and 37–40 needed re-pairing, not renumbering).
- `layer_c_9mark_inventory.csv` and `layer_c_9mark_topics.csv` regenerated.

**Trap recorded:** a swap of this kind is invisible in the reading. Only the
file's own printed code catches it — the case names look entirely plausible on
either paper.

---

## 2. ⚠️ June 2026 Paper 1 — the mark scheme names a different business from the question paper

| | owner | business | chocolate from | wedding cakes for |
|---|---|---|---|---|
| `..._June_2026_P1_QP.pdf` | **Alex** | **Crumb** | France, Belgium | "many celebrities" |
| `..._June_2026_P1_MS.pdf` | **Claire** | **Violet Cakes** | France | **Harry and Meghan** |

**Both files print `4BS1/01 Summer 2026`, and the MS cites "Question Paper Log
Number P79457A" — the same paper as the QP's barcode `P79457RA`.** The MS also
names two competitors (*Gail's Bakery*, *Flour Cafe*) that the QP never mentions.
The rest is a perfect match: the £240 wedding cakes, the 60 application forms and
the 5% shortlist, the cookbook-versus-vegan-products 9-mark options.

**Not fixed — it cannot be fixed from here.** Two Pearson documents for the same
paper disagree on the case name. **Both names must therefore be given wherever
this paper's content is used**, and a student sitting a paper must use the name
printed on their own question paper. **The bank now carries both.** This is the
only one of the 38 papers with such a disagreement — `check_ms_qp_case_names.py`
checks all 38 and flags this pair alone.

---

## 3. ⚠️ May/June 2022 P2R mark scheme prints "Paper 02" in its front matter

Contents are correct (Cadbury — the P2R case); the front-matter line is Pearson's
own slip. **No action: do not "fix" this file.**

---

## 4. ⭐ Found while regenerating: the block files were stale

`extract_ms_blocks.py` has been improved since the committed block files were
written — it now backs up to the nearest real stem heading, so **each block
carries its own question stem** (3-mark `1(f)` etc. previously began mid-answer).
Regenerating was therefore not cosmetic. Two consequences:

- blocks are longer and begin with the stem; anything parsing them must
  **re-anchor on the block's own `Question Number` / `Q. No.` heading**, because
  the first `Level Mark Descriptor` and the first `(AO2)` marker in the text may
  belong to the *previous* question. `build_layer_c_9mark_inventory.py` was
  patched to re-anchor, to accept the letter-fragmented heading
  (`Quest ion Number`), and it now reads **76/76 option pairs and 42 MS stems**
  (was 76 / 30).
- stems recovered from the MS rose from 30 to 42 of 76 in the 9-mark tier.

**Verification rule used throughout:** the 3-mark, 6-mark and 9-mark coverage
scripts all still report **0 remaining** after every regeneration.

---

## 5. Also corrected this pass

`04_Type_Coverage_and_Gaps.md` still carried the **withdrawn** population figures
(`111 / 86 / 48 / 17`, "262 of the 696 items", "6-mark ~24 marks per paper"). It
now carries the mark-scheme-derived **152 / 114 / 76 / 38** and the per-paper
skeleton that all 38 papers satisfy:

**1(f) 3 · 1(g) 6 · 2(c)(d)(e) 3 · 2(f) 9 · 3(d) 6 · 3(e) 9 · 4(b) 6 · 4(c) 12 = 60
marks, plus 20 marks of 1- and 2-mark items = 80.**

---

# 6. THE MAY/JUNE 2024 SWAP, RESOLVED — the second-order damage

**Fixed in `9b44650`, and re-opened on 14 Oct 2026 because the fix was only half of it.**
The two mark schemes were misnamed, so `P1` held Café Pinch (which is Paper 01R) and
`P1R` held PPS (which is Paper 01). The files were renamed, the `10_Chain_Bank.md`
citations were corrected, and the six-mark coverage map's six May/June 2024 entries
were swapped to match. **That last step was the mistake** — not in intent, in
evidence: it was done by reading the *paper labels* in the inventory, and those
labels were themselves the stale, pre-rename ones.

## What had actually happened, in order

1. **The block dump was made before the rename.** `layer_c_6mark_blocks.txt` headed
   the PPS blocks `P1R` and the Café Pinch blocks `P1` — because the headings were
   taken from the filenames, and the filenames were the swapped thing.
2. **`layer_c_6mark_inventory.csv` was built from that dump — and it had no builder.**
   The file named `build_layer_c_6mark_inventory.py` was a copy of the *9-mark*
   builder: it read `layer_c_9mark_blocks.txt`, filtered `Mark value == "9"`, and
   wrote `layer_c_9mark_inventory.csv`. **A committed artifact with no reproducible
   builder is an artifact nobody can re-derive, and this is what that costs.**
3. **The block dump was then regenerated** (after the rename), which flipped the
   order of the six May/June 2024 blocks — `P1R` sorts before `P1` — **so the dump
   and the inventory silently disagreed about which block was which.**
4. **The chain-bank citations were corrected correctly** (entry 118 gained
   *"the gross profit margin to PPS"*, entry 139 gained *"Kumaran, the owner of
   Café Pinch"*), **and the coverage map was then swapped to match the labels** —
   which put each block against the entry for the *other* paper's question.

## How it surfaced

`verify_chain_bank_anchors.py` (new, this pass) scores every block→entry mapping
against **the block's own mark-scheme content** rather than against its label. It
flagged six May/June 2024 mappings in the six-mark tier at 17–29% overlap, and the
printed pairings made the swap obvious at a glance:

| block | the block's actual question | the map said | the entry that actually quotes it |
|---|---|---|---|
| 55 | PPS — *gross profit margin* | 139 motivating employees | **118 profitability ratios** |
| 56 | PPS — *reliable market research* | 144 measuring success | **143 market research** |
| 57 | PPS — *importance of cash* | 145 market segmentation | **123 cash** |
| 58 | Café Pinch — *motivated employees* | 118 profitability ratios | **139 motivating employees** |
| 59 | Café Pinch — *measuring success* | 143 market research | **144 measuring success** |
| 60 | Café Pinch — *market segmentation* | 123 cash | **145 market segmentation** |

## The repair, and why it is now permanent

- **`build_layer_c_6mark_inventory.py` was rewritten as a real 6-mark builder**
  (6-mark block dump in, 6-mark CSV out, `Mark value == "6"`), with the stem trim
  that stops a May-June 2021 stem running on into `Indica t ive content Mark 1 (g)`.
- **The inventory was regenerated**, moving 6 rows and cleaning 1 stem. It now
  reproduces from the dump: `--check` prints the 7 differing rows and nothing else.
- **The coverage map was re-keyed to the regenerated numbering** and every
  May/June 2024 pair is annotated in the map itself with its block, case and entry.
- **`verify_chain_bank_anchors.py` now passes with no contradiction**: 114 + 76 + 38
  = **228 mappings, 0 below the floor**, and **146 of them proven outright** because
  the entry quotes the question verbatim (108 of 114 in the 6-mark tier, 38 of 38 in
  the 12-mark tier).
- **The one genuine content gap it found was filled:** block 99 is **AWG, Nov 2023
  P1 4(b) — *"Analyse how this could affect its business"*, Kaizen run in the
  business's own clothing workshop** — and **entry 119 did not carry the case**. The
  entry now cites it and prints the scheme's AWG anchors, with the distinction that
  matters: **Yellow is told what its suppliers should do; AWG is told what its own
  workshop will do. Same mechanism, different actor — and the actor is what the
  scheme marks.**

## Reproducibility audit of the other two inventories

Both were regenerated and diffed against the committed files: **9-mark 0 rows
changed, 12-mark 0 rows changed.** They reproduce exactly. **The six-mark inventory
was the only one whose builder did not exist.**

---

# 7. The same-day stale-claim sweep

Three more claims that were true when written and were not true when read — the
class of error Phase 4 exists to find:

| Where | Said | Truth |
|---|---|---|
| `06_External_Source_Library.md` § *Highest-value unharvested targets* | **five** tariff-and-paper combinations with **no** full-mark exemplar held, listing 2025 and 2023 P2R targets | **All four named targets have since been harvested.** Replaced with a tariff × paper grid derived from the register: **exactly three open cells** — Paper 2 Justify 9/9, Paper 1R Evaluate 12/12 (best held 11/12), and **Paper 2/2R Evaluate 12/12, which is permanent.** |
| `External_Exemplars/2019-06_P1_Official_Exemplar_Booklet.md` | *"Verified 9/9 on Paper 2 or Paper 2R Justify — **not held**"* | **Paper 2R is now held twice** (May 2023 M&M, June 2025 Rabanne). Only **Paper 2** is still missing. The row was typed when the bank held two 9/9s and was never revisited as the count rose to fifteen. |
| `04_Type_Coverage_and_Gaps.md` | the question-paper CSV is *"still useful for the 1- and 2-mark items"* | **It is not.** Derived: **456 one-mark and 152 two-mark parts** against the CSV's **328 and 106** — the same non-constant under-detection, in the tiers where it had been assumed harmless. |

**Every figure above is now derived rather than typed**, and the two scripts that
derive them — `build_layer_c_tariffs.py` (full distribution + the 80-mark check on
all 38 papers) and `verify_chain_bank_anchors.py` (mappings) — are tracked.
