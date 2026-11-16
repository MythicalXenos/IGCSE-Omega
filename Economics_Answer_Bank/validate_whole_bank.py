#!/usr/bin/env python3
"""Structural/source regression checks for the generated 4EC1 question manifest.

Run: .venv/bin/python Economics_Answer_Bank/validate_whole_bank.py
Counts are derived from the live source inputs; only the 80-mark-per-paper
qualification invariant and documented, source-specific parser exception are fixed.
This checks correspondence and evidence states, not visual review or answer quality.
"""
from __future__ import annotations
import csv, json, re, sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
ARCHIVE = ROOT / "Paperlords_Archive"
sys.path.insert(0, str(HERE))
import build_paper1_qa_bank as parser

manifest_path = HERE / "Whole_Bank_Question_Manifest.csv"
manifest = list(csv.DictReader(manifest_path.open(encoding="utf-8", newline="")))
errors: list[str] = []
def check(ok: bool, msg: str) -> None:
    print(("PASS " if ok else "FAIL ") + msg)
    if not ok:
        errors.append(msg)
def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()

review = json.loads((HERE / "Whole_Bank_Review_Layer.json").read_text(encoding="utf-8"))
identity = json.loads((HERE / "Whole_Bank_Paper_Identity.json").read_text(encoding="utf-8"))
review_items = review.get("items", {})
paper_identity = identity.get("papers", {})
ids = [r["question_id"] for r in manifest]
check(len(ids) == len(set(ids)), f"question_id unique: {len(ids)} rows")
paper_rows: dict[str, list[dict]] = defaultdict(list)
for r in manifest:
    paper_rows[r["canonical_paper_id"]].append(r)
parts = [(r["canonical_paper_id"], r["q"], r["part"]) for r in manifest]
check(len(parts) == len(set(parts)), "no duplicate question-part within a canonical paper")
for paper_id, rs in sorted(paper_rows.items()):
    total = sum(int(r["marks"]) for r in rs)
    check(total == 80, f"{paper_id}: {len(rs)} distinct parts / {total} marks")
    qps = {r["qp_local_path"] for r in rs if r["qp_local_path"]}
    mss = {r["ms_local_path"] for r in rs if r["ms_local_path"]}
    check(len(qps) == 1, f"{paper_id}: one QP source path")
    check(len(mss) <= 1, f"{paper_id}: at most one local MS source path")
    for path in qps | mss:
        check((ROOT / path).is_file(), f"{paper_id}: source exists: {path}")
    check(all(r["ms_local_path"] or r["ms_source_url"] for r in rs),
          f"{paper_id}: MS is locally present or an exact source URL is recorded")

# Every overlay annotation must attach to exactly one source row and survive rebuilds.
by_id = {r["question_id"]: r for r in manifest}
for qid, annotation in review_items.items():
    r = by_id.get(qid)
    check(r is not None, f"review annotation has a source row: {qid}")
    if r:
        for field in ("prompt_text", "stimulus_text", "specification_topic", "subtopic",
                      "reasoning_skill_family", "command_word", "source_check_status",
                      "qp_pdf_page", "ms_pdf_page", "source_evidence",
                      "er_guidance_path", "er_guidance_status", "er_guidance_reference"):
            if field in annotation:
                check(r.get(field) == str(annotation[field]), f"persistent {field} reapplied: {qid}")
        check(bool(r["raw_prompt_text"]), f"raw prompt retained alongside curated text: {qid}")
        if annotation.get("er_guidance_path"):
            check((ROOT / annotation["er_guidance_path"]).is_file(),
                  f"item-linked ER guidance note exists: {qid}")
# Future completed annotations are valid; this is intentionally not an all-pending assertion.
check(any(r["reasoning_skill_family"] != "PENDING_CLASSIFICATION" for r in manifest),
      "at least one source-reviewed family is represented; other items may remain pending")

# Regressions for the two known question/stimulus boundary leaks.
regressions = {
    "4EC1|P73498A|P1|Q4(b)": {
        "prompt_has": "analyse why price elasticity of demand (PED) may be relatively inelastic",
        "stimulus_has": "same brand of coffee can be bought for €0.80 a cup",
        "qp_page": 19, "ms_page": 19,
        "qp_terms": ("Marina Café is popular with tourists and locals", "price elasticity of demand (PED) may be relatively inelastic at Marina Café"),
        "ms_terms": ("few substitutes", "€1.20 more at Marina Café"),
    },
    "4EC1|P75954A|P1|Q1(h)": {
        "prompt_has": "usually becomes more price elastic over time",
        "stimulus_has": "changed from –1.5 to –2.0",
        "qp_page": 5, "ms_page": 6,
        "qp_terms": ("Six months after the price for a soft drink increased", "more price elastic over time"),
        "ms_terms": ("consumers may not be able to break their habit", "more substitutes are available"),
    },
    "4EC1|P60749A|P1|Q1(h)": {
        "prompt_has": "demand for these tickets might be price inelastic",
        "stimulus_has": "most popular music artists can sell for very high prices",
        "qp_page": 4, "ms_page": 6,
        "qp_terms": ("Concert tickets to see the most popular music artists", "price inelastic"),
        "ms_terms": ("no substitutes", "want to see the artist performing live"),
    },
    "4EC1|P58384A|P2|Q1(g)": {
        "wrong_neighbor": "Australia has referred India",
        "prompt_has": "current account deficit for Mexico",
        "stimulus_has": "Mexico’s current account deficit increased to $5.082bn",
        "qp_page": 5, "ms_page": 6,
        "qp_terms": ("Mexico’s current account deficit", "quality of domestic goods"),
        "ms_terms": ("Imports are likely to increase", "$5.082bn"),
    },
    "4EC1|P62031A|P2|Q3(d)": {
        "wrong_neighbor": "China’s central bank",
        "prompt_has": "recession in a country such as Italy",
        "stimulus_has": "manufacturing sector decreased for the third month",
        "qp_page": 15, "ms_page": 13,
        "qp_terms": ("Italy entered a recession", "Analyse the impact on unemployment"),
        "ms_terms": ("Manufacturers may cut back on recruitment", "unemployment rate rises"),
    },
}
import pymupdf
for qid, spec in regressions.items():
    r = by_id.get(qid)
    check(r is not None, f"known regression row exists: {qid}")
    if not r:
        continue
    if spec.get("wrong_neighbor"):
        check(spec["wrong_neighbor"] in r["raw_prompt_text"], f"raw leakage retained for diagnosis: {qid}")
        check(spec["wrong_neighbor"] not in r["prompt_text"], f"neighbouring stimulus removed from curated stem: {qid}")
    check(spec["prompt_has"] in r["prompt_text"], f"curated stem content retained: {qid}")
    check(spec["stimulus_has"] in r["stimulus_text"], f"relevant stimulus separated: {qid}")
    check(int(r["qp_pdf_page"]) == spec["qp_page"] and int(r["ms_pdf_page"]) == spec["ms_page"],
          f"source pages retained: {qid}")
    qp = pymupdf.open(ROOT / r["qp_local_path"])
    ms = pymupdf.open(ROOT / r["ms_local_path"])
    qp_text = qp[spec["qp_page"] - 1].get_text()
    ms_text = ms[spec["ms_page"] - 1].get_text()
    check(all(normalize(t) in normalize(qp_text) for t in spec["qp_terms"]), f"QP source page regression: {qid}")
    check(all(normalize(t) in normalize(ms_text) for t in spec["ms_terms"]), f"MS content regression: {qid}")
    check(("QP_AND_MS_ITEM_TEXT_MATCH_CHECKED" in r["source_check_status"] or
           "QP_AND_MS_ITEM_TEXT_CHECKED" in r["source_check_status"]),
          f"item-level QP/MS text status explicit: {qid}")
    if qid.endswith("Q3(d)"):
        check("IDENTITY_CONFLICT_PENDING" in r["source_check_status"],
              f"QP/MS sitting conflict remains explicit: {qid}")

# Compare archive PDF text parses and item keys/marks to the row-level manifest.
# A known P1R MS parser exception is documented as an (c)-only printed heading.
archive_pairs = [r for r in csv.DictReader((ARCHIVE / "Paperlords_QP_MS_ER_Pairings.csv").open(encoding="utf-8-sig", newline=""))
                 if r.get("Subject") == "Economics"]
by_path = defaultdict(list)
for r in manifest:
    by_path[r["qp_local_path"]].append(r)
for pair in archive_pairs:
    qprel = (ARCHIVE / pair["QP PDF path"]).resolve().relative_to(ROOT).as_posix()
    # For recovered June 2022 P2R the manifest points at the verified alternative.
    if pair["Session"] == "MayJune 2022" and pair["Paper"] == "P2R":
        qprel = "Paperlords_Archive/RECOVERED_ALTERNATIVES/4EC1_Economics_June_2022_P2R_QP_alternative.pdf"
    rs = by_path.get(qprel, [])
    if not rs:
        check(False, f"archive source included in manifest: {qprel}")
        continue
    parsed = {(int(x["q"]), x["part"], int(x["marks"])) for x in parser.parse_qp(ROOT / qprel)}
    listed = {(int(x["q"]), x["part"], int(x["marks"])) for x in rs}
    check(parsed == listed, f"QP item keys and marks correspond: {qprel} ({len(listed)} parts)")
    ms_path = ROOT / rs[0]["ms_local_path"]
    ms_keys = set(parser.parse_ms(ms_path)) if ms_path.is_file() else set()
    expected_keys = {f"{x['q']}{x['part']}" for x in rs}
    missing = expected_keys - ms_keys
    allowed = set(paper_identity.get(rs[0]["canonical_paper_id"], {}).get("known_ms_key_exceptions", []))
    check(not (missing - allowed), f"MS keys present or explicitly excepted: {qprel}; missing={sorted(missing)}")

# January 2023 P1R is incoming (not one of the archive pairs) and has an official remote MS.
jan_rows = [r for r in manifest if r["canonical_paper_id"] == "4EC1|P71556A|P1R"]
check(bool(jan_rows), "incoming January 2023 P1R included independently of archive register")
if jan_rows:
    jan_qp_path = ROOT / jan_rows[0]["qp_local_path"]
    jan_parsed = {(x["q"], x["part"], x["marks"]) for x in parser.parse_qp(jan_qp_path)}
    jan_listed = {(int(x["q"]), x["part"], int(x["marks"])) for x in jan_rows}
    check(jan_parsed == jan_listed, f"incoming January 2023 P1R QP keys/marks match ({len(jan_listed)} parts)")
    check(all("qualifications.pearson.com" in r["ms_source_url"] for r in jan_rows),
          "incoming January 2023 P1R has exact official MS URL")
    check(all("4EC1_01_MS_2301" in r["ms_printed_publication_code"] for r in jan_rows),
          "January 2023 P1R MS printed-code anomaly is retained")
    check(all((ROOT / r["er_local_path"]).is_file() for r in jan_rows),
          "January 2023 P1R local examiner report path exists")

# Source state categories are explicit and not conflated.
check(all(r["source_check_status"] for r in manifest), "every row states source-check status")
check(all(r["er_status"] for r in manifest), "every row distinguishes ER register state")
check(all(r["answer_review_status"] == "NOT_AUDITED_AS_LEARNER_RESPONSE" for r in manifest),
      "answer review remains distinct from source extraction and student mastery")
print(f"\nDerived inventory: {len(paper_rows)} paper IDs, {len(manifest)} question parts, "
      f"{sum(int(r['marks']) for r in manifest)} marks")
if errors:
    print(f"\nFAILED: {len(errors)} check(s)")
    sys.exit(1)
print("PASS: all structural and targeted source regression checks")
