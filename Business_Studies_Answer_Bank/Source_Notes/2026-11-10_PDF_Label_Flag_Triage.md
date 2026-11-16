# PDF filename/printed-label audit flags — evidence-based triage

**Date:** 10 November 2026. The eight outputs of `check_archive_file_labels.py` are audit flags, not eight findings of mislabelled files. The script’s text-layer lookup can fail to recover a code from front matter. None of the PDFs was renamed or relabelled in this triage.

| Filename flagged | Evidence checked | Triage outcome |
|---|---|---|
| June 2026 P1 MS | PDF identifies Summer 2026 and 4BS1/01; internal case content names Violet Cakes and the MS follows that paper’s case, despite a known amendment that changed the QP business name to Crumb. | **No file-mislabel finding.** Explainable text/code and amended-case discrepancy; retain as a source caution, not a filename correction. The QP/MS change is documented in `check_ms_qp_agreement.py` output and the handoff. |
| June 2026 P1R MS | Front matter identifies Summer 2026 and Paper 01R; its case material is consistent with the paired P1R QP. | **Unconfirmed flag; no mismatch found in this bounded text/case check.** Not a visual certification. |
| June 2026 P2 MS | Front matter identifies Summer 2026 and 4BS1/02, publication/log P79460A; paired QP printed log is P79460A and its Nando’s case appears in the MS. | **No mismatch found** for this flag; script’s missing-code output was not evidence of a wrong file. |
| June 2026 P2R MS | Front matter identifies Summer 2026 and 4BS1/02R, publication/log P79461A; paired QP printed log is P79461A and Apple case content appears in the MS. | **No mismatch found** for this flag; script’s missing-code output was not evidence of a wrong file. |
| May–June 2021 P1 MS | Front matter identifies Summer 2021, 4BS1/01; the paired P1 question/case material is represented in the MS. The front-matter extraction does not yield the log code. | **Unconfirmed flag; no filename correction.** The paper/session and content are supporting clues, not full item-by-item verification. |
| May–June 2022 P2R MS | MS front matter identifies Summer 2022 and Paper 02; its sampled and internal case content is Cadbury, matching the paired P2R QP (P2 is LEGO). The P2R QP has a different log/suffix identity. | **A printed-code/suffix discrepancy is supported; a wrong-content or swapped-file finding is not.** Cadbury-vs-LEGO case evidence argues against treating this as the P2 MS swapped into the P2R filename. Keep the pair’s identity caution and verify the full printed pages/official source before correcting a label. |
| November 2025 P1 MS | Front matter identifies November 2025, 4BS1/01 and log P78969A; MS case content includes Ocean Vibes, matching paired P1 QP. | **No mismatch found** in the filename-vs-content comparison; the missing extraction flag does not establish mislabelling. |
| November 2025 P2 MS | Front matter identifies November 2025, 4BS1/02 and log P78971A; MS case content includes Samsung, matching paired P2 QP. | **No mismatch found** in the filename-vs-content comparison; the missing extraction flag does not establish mislabelling. |

## Limits and action

This is a targeted text-layer and case-content triage, not a visual cover audit or full QP/MS item-by-item comparison for all eight papers. The stronger code/case agreements reduce the likelihood of a wrong file for several flags but do not certify complete pairing. The May–June 2022 P2R suffix discrepancy remains open as a publication-code identity caveat. Preserve all eight as historical audit outputs; do not describe them as eight confirmed mislabels. Continue source-page verification before changing filenames or inventories.
