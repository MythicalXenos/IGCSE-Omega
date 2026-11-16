#!/usr/bin/env python3
"""Rebuild the source manifest and reapply keyed human review annotations.

Run from any working directory with dependencies installed from requirements.txt:
  python Economics_Answer_Bank/build_whole_bank_manifest.py

The generated manifest is reproducible from repository inputs. Never edit the CSV
as the source of truth: put durable corrections/classifications in
Whole_Bank_Review_Layer.json and paper identity evidence in
Whole_Bank_Paper_Identity.json. Raw PDF/parser text is retained separately from
curated question/stimulus fields.
"""
from __future__ import annotations
import csv, json, re, sys, urllib.parse
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
ARCHIVE = ROOT / "Paperlords_Archive"
sys.path.insert(0, str(HERE))
import build_paper1_qa_bank as parser

PAIRINGS = ARCHIVE / "Paperlords_QP_MS_ER_Pairings.csv"
P1_BANK = HERE / "Paper1_QA_Bank.json"
SUPPLEMENTS = HERE / "Paper1_QA_Supplements.json"
REVIEW_LAYER = HERE / "Whole_Bank_Review_Layer.json"
IDENTITY_LAYER = HERE / "Whole_Bank_Paper_Identity.json"
OUT = HERE / "Whole_Bank_Question_Manifest.csv"


def clean_session(label: str) -> str:
    s = re.sub(r"\s+", " ", label.strip())
    for old, new in (("MayJune", "May-June"), ("Jan ", "January "), ("Nov ", "November ")):
        s = s.replace(old, new)
    return s


def rel(path: Path | str) -> str:
    p = Path(path)
    if not p.is_absolute():
        p = ROOT / p
    try:
        return p.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return p.as_posix()


def pdf_log(path: Path) -> str:
    if not path.is_file():
        return ""
    import pymupdf
    page = pymupdf.open(path)[0].get_text()
    m = re.search(r"\b(P\d{5}[A-Z]{1,2})\b", page)
    return m.group(1) if m else ""


def safe_url(value: str) -> str:
    return urllib.parse.quote(value, safe=":/?&=%#") if value else ""


with PAIRINGS.open(encoding="utf-8-sig", newline="") as f:
    pairing_rows = [r for r in csv.DictReader(f) if r.get("Subject") == "Economics"]
by_qp_path = {}
for r in pairing_rows:
    qp_path = rel(ARCHIVE / r["QP PDF path"])
    by_qp_path[qp_path] = r

review = json.loads(REVIEW_LAYER.read_text(encoding="utf-8"))
review_items = review.get("items", {})
identity = json.loads(IDENTITY_LAYER.read_text(encoding="utf-8"))
paper_identity = identity.get("papers", {})
supplements = json.loads(SUPPLEMENTS.read_text(encoding="utf-8"))
supp_by_key = {(p["session"], p["paper"]): p for p in supplements.get("papers", [])}

rows: list[dict] = []

def add_item(session_label: str, paper: str, item: dict, qp_value: str, ms_value: str,
             source_type: str, source_note: str = "") -> None:
    qp_path = Path(qp_value) if qp_value else Path()
    if qp_value and not qp_path.is_absolute():
        qp_path = ROOT / qp_path
    qp_rel = rel(qp_path) if qp_value else ""
    pair = by_qp_path.get(qp_rel)
    if pair:
        # Use pairing-register paths/URLs, but retain QP source identity separately.
        ms_path = ARCHIVE / pair["MS PDF path"]
        qp_url = pair["Paperlords QP URL"]
        ms_url = pair["Paperlords MS URL"]
        er_pdf_values = [x.strip() for x in pair.get("ER PDF path(s)", "").split(";") if x.strip()]
        er_url_values = [x.strip() for x in pair.get("ER source URL(s)", "").split(";") if x.strip()]
        er_paths = [rel(ARCHIVE / x) for x in er_pdf_values]
        er_status = "REGISTERED_IN_PAIRING" if er_paths or er_url_values else "NOT_LISTED_IN_PAIRING_AVAILABILITY_NOT_CHECKED"
        provenance = "Paperlords archive pairing register"
        alias = pair.get("Session", "")
    else:
        ms_path = Path(ms_value) if ms_value and not ms_value.startswith("http") else None
        if ms_path and not ms_path.is_absolute():
            ms_path = ROOT / ms_path
        qp_url = ms_url = ""
        er_paths, er_url_values = [], []
        er_status = "NOT_LISTED_IN_PAIRING_AVAILABILITY_NOT_CHECKED"
        provenance = source_note or "Incoming or supplemental source; see source note"
        alias = session_label
        supplement = supp_by_key.get((session_label, paper), {})
        # January 2023 P1R has official QP/MS URLs outside the archive pair register.
        if supplement:
            ms_url = supplement.get("ms", "") if str(supplement.get("ms", "")).startswith("http") else ""
            qp_url = "https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Economics/2017/exam-materials/4ec1-01r-que-20230114.pdf" if session_label == "January 2023" else ""
            provenance = supplement.get("source_note", provenance)

    log = pdf_log(qp_path) if qp_value else ""
    paper_id = f"4EC1|{log or clean_session(session_label)}|{paper}"
    ident = paper_identity.get(paper_id, {})
    session = ident.get("canonical_session", clean_session(session_label))
    archive_alias = ident.get("archive_session_alias", "")
    identity_status = ident.get("identity_status", "PENDING_SOURCE_IDENTITY_REVIEW")
    qp_cover_date = ident.get("qp_cover_printed_date", "")
    ms_cover_session = ident.get("ms_cover_session", "")
    ms_printed_code = ident.get("ms_printed_publication_code", "")
    if ident.get("er_local_path"):
        er_paths = [ident["er_local_path"]]
        er_url_values = [ident.get("er_source_url", "")] if ident.get("er_source_url") else er_url_values
        er_status = ident.get("er_status", "LOCAL_ER_SOURCE_IDENTIFIED; ITEM_GUIDANCE_NOT_CROSSWALKED")
    elif ident.get("er_source_url"):
        er_url_values = [ident["er_source_url"]]
        er_status = ident.get("er_status", "REMOTE_ER_SOURCE_IDENTIFIED; ITEM_GUIDANCE_NOT_CROSSWALKED")
    admin_status = ident.get("administration_status", "NOT_VERIFIED_OR_NOT_APPLICABLE")
    if paper_id == "4EC1|P65896A|P1":
        admin_status = "CANCELLED_SERIES_SURVIVING_PAPER_NOT_LIVE_ADMINISTRATION"

    question_id = f"{paper_id}|Q{item['q']}({item['part']})"
    annotation = review_items.get(question_id, {})
    raw_text = item.get("text", "")
    item_locator = item.get("source_locator", {})
    answer = item.get("answer", "")
    qpage = annotation.get("qp_pdf_page", item_locator.get("qp_pdf_page", ""))
    mpage = annotation.get("ms_pdf_page", item_locator.get("ms_pdf_page", ""))

    if source_type == "P2" and ms_path and ms_path.is_file():
        ms_items = parser.parse_ms(ms_path)
        key = f"{item['q']}{item['part']}"
        answer = ms_items.get(key, "")
    if not ms_path and ms_url and answer:
        ms_location_status = "OFFICIAL_REMOTE_MS_CONTENT_ALREADY_IN_SUPPLEMENT; PDF_NOT_LOCAL"
    elif ms_path and ms_path.is_file():
        ms_location_status = "LOCAL_MS_PRESENT; ITEM_SEMANTIC_CHECK_STATUS_IS_SEPARATE"
    else:
        ms_location_status = "MS_SOURCE_NOT_LOCALLY_RESOLVED"

    raw_note = ("Existing P1/P1R bank text; its previous source-layer/raw-text status varies by item. "
                "Do not treat it as an untouched extraction.") if source_type == "P1" else \
               "Raw PDF parser text retained exactly as extracted; may include neighbouring stimulus/layout spillover."
    row = {
        "question_id": question_id,
        "canonical_paper_id": paper_id,
        "paper_group": "Paper 1/P1R" if paper in ("P1", "P1R") else "Paper 2/P2R",
        "session": session,
        "archive_session_alias": archive_alias or (clean_session(alias) if clean_session(alias) != session else ""),
        "paper": paper,
        "variant": "regional R" if paper.endswith("R") else "standard",
        "reference": f"4EC1 {paper} {session} Q{item['q']}({item['part']})",
        "qp_log": log,
        "qp_cover_printed_date": qp_cover_date,
        "ms_cover_session": ms_cover_session,
        "ms_printed_publication_code": ms_printed_code,
        "paper_identity_status": identity_status,
        "administration_status": admin_status,
        "q": item["q"], "part": item["part"], "marks": item["marks"],
        "raw_prompt_text": raw_text,
        "raw_prompt_provenance_note": raw_note,
        "prompt_text": annotation.get("prompt_text", raw_text),
        "stimulus_text": annotation.get("stimulus_text", ""),
        "specification_topic": annotation.get("specification_topic", "PENDING_CLASSIFICATION"),
        "subtopic": annotation.get("subtopic", "PENDING_CLASSIFICATION"),
        "reasoning_skill_family": annotation.get("reasoning_skill_family", "PENDING_CLASSIFICATION"),
        "command_word": annotation.get("command_word", "PENDING_CLASSIFICATION_AND_STEM_CHECK"),
        "qp_pdf_page": qpage, "ms_pdf_page": mpage,
        "source_check_status": annotation.get("source_check_status", "PENDING_WHOLE_BANK_SOURCE_CHECK"),
        "qp_ms_item_correspondence_status": annotation.get("qp_ms_item_correspondence_status", "KEY_MATCH_ONLY_SEMANTIC_CORRESPONDENCE_NOT_CHECKED"),
        "answer_review_status": annotation.get("answer_review_status", "NOT_AUDITED_AS_LEARNER_RESPONSE"),
        "student_mastery_status": "NOT_ASSESSED",
        "source_identity_status": annotation.get("identity_status", identity_status),
        "source_evidence": annotation.get("source_evidence", ""),
        "er_guidance_path": annotation.get("er_guidance_path", ""),
        "er_guidance_status": annotation.get("er_guidance_status", "NOT_ITEM_CROSSWALKED"),
        "er_guidance_reference": annotation.get("er_guidance_reference", ""),
        "reviewer_note": annotation.get("reviewer_note", ""),
        "qp_local_path": qp_rel,
        "ms_local_path": rel(ms_path) if ms_path else "",
        "ms_location_status": ms_location_status,
        "er_local_path": ";".join(er_paths),
        "er_source_url": ";".join(safe_url(x) for x in er_url_values),
        "er_status": er_status,
        "qp_source_url": safe_url(qp_url), "ms_source_url": safe_url(ms_url),
        "source_provenance": provenance,
        "answer_or_ms_extract": answer,
        "extraction_note": ("Whole-bank source-layer status applies; earlier item-specific audits do not automatically transfer. "
                            "Use exact QP/MS evidence and source_evidence; this row is not scored or guaranteed."),
    }
    rows.append(row)

# P1/P1R: use existing indexed answers and exact local/incoming QP paths.
for paper_record in json.loads(P1_BANK.read_text(encoding="utf-8")):
    for item in paper_record["items"]:
        add_item(paper_record["session"], paper_record["paper"], item,
                 paper_record.get("qp", ""), paper_record.get("ms", ""), "P1",
                 paper_record.get("source_note", ""))

# P2/P2R: parse actual paired PDFs; the malformed June 2022 P2R uses the recovered copy.
for pairing in pairing_rows:
    paper = pairing.get("Paper", "")
    if paper not in ("P2", "P2R"):
        continue
    qp = ARCHIVE / pairing["QP PDF path"]
    if pairing.get("Session") == "MayJune 2022" and paper == "P2R":
        qp = ARCHIVE / "RECOVERED_ALTERNATIVES/4EC1_Economics_June_2022_P2R_QP_alternative.pdf"
    for item in parser.parse_qp(qp):
        add_item(pairing["Session"], paper, item, str(qp),
                 str(ARCHIVE / pairing["MS PDF path"]), "P2")

# Deterministic ordering; no deduplication across genuine paper appearances.
rows.sort(key=lambda x: (x["paper_group"], x["session"], x["paper"], x["q"], x["part"]))
ids = [x["question_id"] for x in rows]
if len(ids) != len(set(ids)):
    dupes = sorted({x for x in ids if ids.count(x) > 1})
    raise SystemExit(f"Duplicate question_id(s); resolve identity/duplicate sources: {dupes[:20]}")

with OUT.open("w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
    writer.writeheader()
    for row in rows:
        cleaned = {k: "\n".join(str(v).splitlines()) if isinstance(v, str) else v for k, v in row.items()}
        writer.writerow(cleaned)

from collections import Counter
print(f"Wrote {OUT.relative_to(ROOT)}: {len(rows)} question parts, {sum(int(r['marks']) for r in rows)} marks")
print(Counter((r["paper_group"], r["paper"]) for r in rows))
