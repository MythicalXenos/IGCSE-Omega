# Economics 4EC1 Answer Bank

Built 2026-10-12 from the Paperlords archive and official Pearson exemplar/report material.

## Deliverables

- **`4EC1_Paper_Fingerprint.md` — ⭐ start here.** The measured structure of the qualification: 42
  papers, **998 items, 3,360 marks**; every paper is 4 questions × 20 marks with **exactly 3 six-mark,
  2 nine-mark and 1 twelve-mark** item, Q4 always `2 · 6 · 12`; and what each tariff is made of —
  3-mark **AO2 only**, 6-mark **AO2 3 + AO3 3**, 9-mark **AO2 3 + AO3 3 + AO4 3**, 12-mark
  **AO2 4 + AO3 4 + AO4 4**, with **no AO1 above 2 marks**. Checked by
  `verify_economics_fingerprint.py`.
- **`4EC1_Command_Words_Verified.md`** — the three long-answer command words in Pearson's own words,
  quoted from the June 2023 examiner reports and verified character-for-character against the PDFs:
  *Analyse* = one side, no evaluation, no definition; *Assess* = two sides, **no conclusion
  required**; *Evaluate* = two sides **and** a supported judgement. All 17 quotations are re-checked
  on every run of the verifier, and so is the copy of each quote in the doc that uses it.
- **`4EC1_What_Stops_You_At_11.md`** — the nearest thing to a 12/12 in the archive is **11/12**, and the
  examiner says why it stopped there: *"does not present an excellent organisation of information and
  application is only reasonable"*. The three commented 12-mark scripts (11, 11, 10) with the exact
  reason for each lost mark, the three rules the report states for the 12-marker, and the timing
  budget. The final table — what a 12/12 must contain — is **labelled as construction**.
- `verify_economics_fingerprint.py` — 85 checks; exit 0 = every claim above still holds.
- `4EC1_Exemplar_and_Model_Answer_Guide.docx` — main guide with answer patterns, official-score evidence and constructed targets.
- `4EC1_Exemplar_and_Model_Answer_Guide.md` — searchable source version.
- `4EC1_Question_Type_Inventory.xlsx` — filterable workbook: question-family map, prompt-pattern map, 671 item-level entries with matching QP/MS PDF paths, official exemplar scores/pages and source register.
- `Paper1_QA_Bank.md` / `.json` — searchable Paper 1 QP and mark-scheme bank; now 22 records, including a documented January 2023 P1R supplement.
- `Paper1_QA_Supplements.json` — source-backed non-archive additions and item overrides. January 2023 P1R has a locally held QP and an official Pearson MS URL; the MS PDF is not stored locally. Its content is summarized/paraphrased and the publication-code discrepancy is documented.
- `build_paper1_qa_bank.py` — rebuilds the Q&A bank from the Paperlords archive plus the supplement input.
- `build_economics_inventory.py` — rebuilds the workbook from the searchable index and QP/MS pairing file.
- `make_docx.py` — rebuilds the DOCX from the Markdown guide.
- `Source_Notes/Official_Pearson_Exemplar_Index.md` — score-verified scripts and source-page map.

## Storage policy

To protect workspace space, no extra QP, MS, examiner-report or exemplar PDFs were copied here. The 42 archived 4EC1 QPs, their matching mark schemes and the three 2023 examiner reports remain in `Paperlords_Archive/`. Use the PDF paths in the workbook or the official Pearson links. For searchable text, take the same relative path and replace `.pdf` with `.txt` inside `Paperlords_Searchable_Text_Index.zip`. The unreadable May/June 2022 P2R QP is represented by the verified recovered alternative, paired with the original matching mark scheme.

## Correction log

- **9 Nov 2026 — item counts.** The guide and the workbook counted **671 items** (262/173/98/60/42/36).
  The true figure is **998** (337/220/189/126/84/42). The old number cannot be right on its own terms:
  it totals 2,072 marks over 42 papers, i.e. 49 marks a paper on papers that print 80. The cause is a
  regex that only accepts a mark value alone on its line. **The `.xlsx` still carries the low counts;
  use `4EC1_Paper_Fingerprint.md` for structure and do not use the workbook to count items.**
- **9 Nov 2026 — hard-coded paths.** `make_docx.py` and `build_economics_inventory.py` read
  `/home/user/Economics_Answer_Bank`, which only works if the repo is cloned at `/home/user`. Both now
  resolve paths from the script's own location.
- **9 Nov 2026 — the damaged QP.** `4EC1_Economics_May-June_2022_P2R_QP.pdf` has a broken object table
  (*Object 87 0 not defined*) and opens as 0 pages in pymupdf and pypdf. Two recovered copies exist and
  both parse to 23 items / 80 marks. **This is the file, not the paper.**

## Evidence policy

- “OFFICIAL — full marks” means a published real candidate script with a verified score of all marks.
- “OFFICIAL — not full marks” states the actual score and is calibration only.
- “CONSTRUCTED full-credit target” is an original response built from the exact QP/MS and examiner guidance. It is not a past-candidate script and is not guaranteed a precise mark.
- The checked June 2019 exemplar booklets and June 2023 examiner reports contained verified full-mark examples for 2-, 3-, 6- and 9-mark items. No 12/12 script was located in those sources; the guide labels its 12-mark model as constructed.
