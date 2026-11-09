# IGCSE-Omega

Three Pearson Edexcel International GCSE subjects, one archive, one evidence system.

| Subject | Bank | Size | State |
|---|---|---|---|
| **4BS1 Business** | `Business_Studies_Answer_Bank/` | 274 files · 69 MB · 867k words | **Most developed.** Rulebook, tariff playbook and fingerprint, 38 By_Paper files, **150-row** verified register, 113k-word chain bank, **29 checks** |
| **4EB1 English Language B** | `English_Answer_Bank/` | 198 files · 6.0 MB · 488k words | **Complete.** 253/253 question entries across 23 papers; 14 authentic transcripts, 78 locators, 239 labelled constructed models |
| **4EC1 Economics** | `Economics_Answer_Bank/` | 7 files · 0.2 MB · 6.2k words | **Starter kit.** Inventory of 42 papers / 671 items; no perfect-answers layer yet |

`Paperlords_Archive/` holds the source material: **216 PDFs** — 103 question papers, 103 mark schemes, 10 examiner reports — every QP paired to its MS, plus a page-by-page searchable text index and a keyword search script.

## Start here

1. `README_Workspace.md` — the folder map.
2. `Transfer_Prompt_New_Agent_Mode.md` — goals, learner profile, subject-specific corrections, evidence rules.
3. `REPO_AUDIT_2026-11-09.md` — whole-repository audit: what exists, what is strong, what is missing.
4. If the checkout has reverted to `04b80df Initial commit` and most folders are untracked: **`bash tools/recover_workspace.sh`**.

## Evidence contract

Nothing in these banks is presented as more than it is. Every answer carries a label:

- **`[VERIFIED CANDIDATE EXEMPLAR]`** — a real script, reproduced by Pearson, with the published score.
- **`[OFFICIAL MARK-SCHEME WORKED ANSWER]`** — Pearson's own indicative content, quoted.
- **`[CONSTRUCTED GRADE 9 TARGET]`** — written from the QP/MS/ER; not official, not examiner-marked, no score claimed.

Verification: **28 scripts** in `Business_Studies_Answer_Bank/` fail the run when a label, a tally row, a boundary figure, a score pairing or an arithmetic claim does not resolve — listed in `Perfect_Answers/08_Completion_Map.md`.

## Learner record

- English 4EB1: mock **55/100**; Section A the weak point. Marked since: Q3 **5/10**, Q7 **9/15**, Q9 draft 4 **21/30**. Friend's full paper **66/100** (A 25 · B 24 · C 17).
- Business 4BS1: full May 2023 Paper 1 handwritten script marked — **55/80**. Four questions of May 2023 Paper 2 — **15/30**. Records in `Business_Studies_Answer_Bank/Mock_Records/`.
- Economics 4EC1: no baseline yet.
