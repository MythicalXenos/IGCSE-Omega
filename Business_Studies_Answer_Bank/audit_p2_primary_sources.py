#!/usr/bin/env python3
"""Inventory the repository-held 4BS1 P2/P2R primary PDFs.

This checks that paired files open, records page counts and the identifiers
printed/extracted from their covers, and records whether the pairing register
points to a locally held examiner report. It does NOT prove QP/MS content
correspondence or that a report was read.

Run: python Business_Studies_Answer_Bank/audit_p2_primary_sources.py
Dependency: PyMuPDF (see requirements_p2_audit.txt).
"""
from __future__ import annotations
import csv, re
from pathlib import Path
import pymupdf

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
ARCHIVE = ROOT / "Paperlords_Archive"
PAIRINGS = ARCHIVE / "Paperlords_QP_MS_ER_Pairings.csv"
OUT = HERE / "Source_Notes" / "P2_Primary_Source_Inventory.csv"

# Keep documented cover/session anomalies visible; do not canonicalise them away.
NOTES = {
    ("MayJune 2019", "P2"): "QP cover P59930RA; MS cover identifies Summer 2019 4BS1 Paper 2 but has no QP log code in text layer. Item/case sequence pairing is registered; cover-code crosswalk not printed.",
    ("MayJune 2019", "P2R"): "QP cover P59932A; MS cover identifies Summer 2019 4BS1 Paper 02R but has no QP log code in text layer. Item/case sequence pairing is registered; cover-code crosswalk not printed.",
    ("MayJune 2020", "P2"): "QP prints 2 June 2020 and P62427A; paired MS cover says November 2020 / 4BS1_02_2011_MS. Sampled Q1(a)(i), Q1(a)(ii), Q1(a)(iii) content aligns. Preserve the session/publication-label discrepancy; administration/cancellation status not established here.",
    ("MayJune 2020", "P2R"): "QP prints 2 June 2020 and P62429A; paired MS cover says November 2020 / 4BS1_02R_2011_MS. Session/publication-label discrepancy preserved; administration/cancellation status not established here.",
    ("MayJune 2022", "P2R"): "QP log P70350A; MS cover text extracts P70350 (suffix A omitted) and uses Paper 02/R cover wording. Session/case sequence registered; keep the printed-code anomaly visible.",
    ("Nov 2021", "P2"): "QP and MS identify November 2021 4BS1/02; sampled Q1 question/answer content aligns. This is a sample check, not a full-paper pairing audit.",
    ("June 2026", "P2"):  "QP and MS printed log P79460A and 4BS1/02, Summer 2026.",
    ("June 2026", "P2R"): "QP and MS printed log P79461A and 4BS1/02R, Summer 2026.",
}

# Report files that are actually present locally, separate from blank pair-register cells.
LOCAL_ERS = {
    ("May 2023", "P2"): ARCHIVE / "IGCSE/4BS1_Business_Studies/May_2023/4BS1_Business_Studies_May_2023_P2_ER.pdf",
    ("May 2023", "P2R"): ARCHIVE / "IGCSE/4BS1_Business_Studies/May_2023/4BS1_Business_Studies_May_2023_P2R_ER.pdf",
    ("MayJune 2022", "P2R"): HERE / "Sources/Official_Pearson/Full_Examiner_Reports/4BS1_02R_2206_ER_full.pdf",
    ("MayJune 2024", "P2"): HERE / "Sources/Official_Pearson/Full_Examiner_Reports/4BS1_02_2406_ER_full.pdf",
    ("MayJune 2025", "P2"): HERE / "Sources/Official_Pearson/Full_Examiner_Reports/4BS1_02_2506_ER_full.pdf",
    ("MayJune 2025", "P2R"): HERE / "Sources/Official_Pearson/Full_Examiner_Reports/4BS1_02R_2506_ER_full.pdf",
}
SAMPLED_CONTENT = {
    ("MayJune 2020", "P2"): "SAMPLED Q1(a)(i-iii) QP/MS content aligns; session identity unresolved",
    ("Nov 2021", "P2"): "SAMPLED Q1 content aligns; cover identity/session read",
    ("May 2023", "P2"): "Q4(c) QP/MS/ER prompt, mark and script cross-checked; ER pp.56-58",
    ("June 2026", "P2"): "QP/MS covers and codes match; no full item content audit",
    ("June 2026", "P2R"): "QP/MS covers and codes match; no full item content audit",
}

def pdf_info(path: Path) -> tuple[str, int, str, bool]:
    try:
        doc = pymupdf.open(path)
        if doc.page_count < 1:
            return "", 0, "", False
        first = "\n".join(doc[i].get_text() for i in range(min(3, doc.page_count)))
        log = re.search(r"\bP\d{5}[A-Z]{0,2}\b", first)
        cover = re.sub(r"\s+", " ", first[:650]).strip()
        return log.group(0) if log else "", doc.page_count, cover, True
    except Exception as e:
        return "", 0, f"OPEN_ERROR: {type(e).__name__}: {e}", False

with PAIRINGS.open(encoding="utf-8-sig", newline="") as f:
    all_rows = list(csv.DictReader(f))
rows = [r for r in all_rows if r.get("Subject") == "Business Studies" and r.get("Paper") in {"P2", "P2R"}]
records = []
for r in sorted(rows, key=lambda x: (x["Session"], x["Paper"])):
    qp = ARCHIVE / r["QP PDF path"]
    ms = ARCHIVE / r["MS PDF path"]
    qcode, qpages, qcover, qok = pdf_info(qp)
    mcode, mpages, mcover, mok = pdf_info(ms)
    er_paths = [x.strip() for x in (r.get("ER PDF path(s)") or "").split(";") if x.strip()]
    er_states = []
    for er in er_paths:
        path = ARCHIVE / er
        if not path.is_file():
            er_states.append(f"REGISTERED_NOT_HELD:{er}")
        else:
            _, n, _, ok = pdf_info(path)
            er_states.append(f"HELD_READABLE_{n}pp:{er}" if ok else f"HELD_UNREADABLE:{er}")
    local_er = LOCAL_ERS.get((r["Session"], r["Paper"]))
    if local_er and local_er.is_file():
        _, er_pages, _, er_ok = pdf_info(local_er)
        er_local_status = f"HELD_READABLE_{er_pages}pp; report-page review: May 2023 P2/P2R sampled, otherwise NOT_REVIEWED"
        er_local_path = str(local_er.relative_to(ROOT))
    else:
        er_local_status = "NO_P2_ER_FILE_MAPPED_IN_LOCAL_INVENTORY; this is not proof of non-publication"
        er_local_path = ""
    qcode_mcode_status = (
        "SESSION_LABEL_CONFLICT_CONFIRMED; unresolved"
        if r["Session"] == "MayJune 2020"
        else "CODE_SUFFIX_VARIANCE; visual check required"
        if (r["Session"], r["Paper"]) == ("MayJune 2022", "P2R")
        else "PRINTED_LOG_MATCH_ONLY; question-by-question pairing not verified"
        if qcode and mcode and qcode == mcode
        else "MS_LOG_ABSENT_FROM_TEXT_LAYER; inspect printed cover and content"
    )
    records.append({
        "session_as_pairing_register": r["Session"], "paper": r["Paper"],
        "qp_path": (Path("Paperlords_Archive") / r["QP PDF path"]).as_posix(),
        "qp_held_readable": str(qok).upper(), "qp_pages": qpages, "qp_log_from_cover_text": qcode,
        "ms_path": (Path("Paperlords_Archive") / r["MS PDF path"]).as_posix(),
        "ms_held_readable": str(mok).upper(), "ms_pages": mpages, "ms_cover_code_or_publication_code": mcode,
        "register_ER_paths": "; ".join(er_paths), "ER_pair_register_status": "; ".join(er_states) or "NO_ER_PATH_IN_PAIRING_REGISTER",
        "ER_local_source_path": er_local_path, "ER_local_read_review_status": er_local_status,
        "qp_read_review_status": "HELD_READABLE; cover/page-count opened; full paper not reviewed",
        "ms_read_review_status": "HELD_READABLE; cover/page-count opened; full mark scheme not reviewed",
        "qp_ms_identity_status": qcode_mcode_status,
        "qp_ms_content_sample_status": SAMPLED_CONTENT.get((r["Session"], r["Paper"]), "NO_ITEM_LEVEL_CONTENT_COMPARISON_RECORDED"),
        "SAM_status": "OFFICIAL_PEARSON_PAPER_SAM_REVIEWED_ONLINE_2026-11-10; not retained locally; see Source_Notes/2026-11-10_Substantive_Sample_Review.md",
        "Pearson_exemplar_status": "Exemplar inventory exists; no per-session completeness or source mapping claimed here",
        "identity_or_session_note": NOTES.get((r["Session"], r["Paper"]), "Cover/session text extracted; use the original printed pages and item-level sources before teaching. This inventory is not a content audit."),
        "source_material_status": "Business case/data are included in the QP PDF; no separate P2/P2R source-material PDF is listed by the pairing register.",
        "cover_text_review_status": "TEXT_LAYER_READ; not a visual page review",
    })

fields = list(records[0]) if records else []
with OUT.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader(); w.writerows(records)
print(f"P2/P2R pairs: {len(records)}; QPs readable: {sum(x['qp_held_readable']=='TRUE' for x in records)}; MSs readable: {sum(x['ms_held_readable']=='TRUE' for x in records)}")
print(f"Wrote {OUT.relative_to(ROOT)}")
print("Coverage and identity checks are inventory-level; no content-verification claim is made by this script.")
