#!/usr/bin/env python3
"""Build a searchable Paper 1 (4EC1/01) question + mark-scheme answer bank.

Sources: Paperlords_Archive/IGCSE/4EC1_Economics/*/ (QP + MS pairs), plus
`Paper1_QA_Supplements.json` for documented official Pearson sources outside the
archive. Supplement QPs must be locally available; their answer keys and source
URLs are maintained in the supplement file.

Output:
  Economics_Answer_Bank/Paper1_QA_Bank.md    human/searchable view
  Economics_Answer_Bank/Paper1_QA_Bank.json  machine index

Evidence policy (see README.md): answer text is extracted from the local official
Pearson mark schemes, except documented supplements/paraphrases. Nothing here is
constructed. This is still a provisional extraction: question stems may contain
cross-question/source-passage leakage and item-to-MS joins have not yet received
the required visual/source audit. Page locators are navigation aids, not proof.
"""
import json
import re
import unicodedata
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "Paperlords_Archive" / "IGCSE" / "4EC1_Economics"
OUT_MD = Path(__file__).resolve().parent / "Paper1_QA_Bank.md"
OUT_JSON = Path(__file__).resolve().parent / "Paper1_QA_Bank.json"
SUPPLEMENTS = Path(__file__).resolve().parent / "Paper1_QA_Supplements.json"

ITEM_RE = re.compile(r"\n\s*(?:(\d{1,2})\s*)?\(([a-i])\)\s*\t?\s*")
MS_KEY_RE = re.compile(r"(?m)^[ \t]*(\d{1,2})[ \t]*\(([a-i])\)[ \t]*$")
MARKS_RE = re.compile(r"\((\d{1,2})\)")


FURNITURE = re.compile(
    r"(?m)^[ \t]*(?:Turn over|DO NOT WRITE IN THIS AREA|\d{1,3}|[A-D](?:[ \t]+[A-D]){0,3})[ \t]*$"
)


def clean(t):
    t = re.sub(r"\*?P\d{5}[A-Z]\d+\*?", "", t)
    t = re.sub(r"DO NOT WRITE IN THIS AREA", "", t)
    t = re.sub(r"\.{20,}", "", t)
    t = FURNITURE.sub("", t)
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t.strip()


def parse_qp(path):
    text = "\n".join(pg.get_text() for pg in pymupdf.open(path))
    # Question boundaries are fixed by the "Total for Question N = 20 marks" footers.
    stops = [(m.start(), int(m.group(1))) for m in re.finditer(r"Total for Question\s*(\d{1,2})", text)]
    chunks = []
    start = 0
    for pos, num in stops:
        chunks.append((num, start, pos))
        start = pos
    if stops:
        chunks.append((stops[-1][1], start, len(text)))
    items = []
    for qnum, s, e in chunks:
        chunk = text[s:e]
        hits = list(ITEM_RE.finditer(chunk))
        for i, m in enumerate(hits):
            end = hits[i + 1].start() if i + 1 < len(hits) else len(chunk)
            seg = chunk[m.end():end]
            seg = re.split(r"Total for Question", seg)[0]
            marks = [int(x) for x in MARKS_RE.findall(seg)]
            if not marks:
                continue
            stem = MARKS_RE.sub("", seg)
            stem = clean(stem)
            stem = re.sub(r"\[\s*lines?\s*\]", "", stem)
            if len(stem) < 12:
                continue
            items.append({"q": qnum, "part": m.group(2), "marks": marks[-1], "text": stem})
    return items


def parse_ms(path):
    text = "\n".join(pg.get_text() for pg in pymupdf.open(path))
    hits = list(MS_KEY_RE.finditer(text))
    out = {}
    for i, m in enumerate(hits):
        end = hits[i + 1].start() if i + 1 < len(hits) else len(text)
        body = text[m.end():end]
        # Pearson mark schemes can place the next question's prompt between the
        # current response block and its next numbered answer key. Stop at the
        # case-insensitive "Question Number" table header so that prompt text
        # is not misfiled as part of the preceding mark-scheme answer.
        body = re.split(
            r"\(Total for Question|TOTAL FOR PAPER|Question\s+Number",
            body,
            flags=re.I,
        )[0]
        body = clean(body)
        key = f"{m.group(1)}{m.group(2)}"
        if len(body) > len(out.get(key, "")):
            out[key] = body
    return out


def _search_normalize(text):
    text = unicodedata.normalize("NFKD", text).casefold()
    text = "".join(ch if ch.isalnum() or ch.isspace() else " " for ch in text)
    return " ".join(text.split())


def _local_pdf_path(value):
    if not value or str(value).startswith("http"):
        return None
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def _paper_page_text(path):
    return [page.get_text() for page in pymupdf.open(path)] if path and path.is_file() else []


def locate_item_pages(qp_pages, ms_pages, q_ends, item):
    """Add navigation hints only; this does not validate text or QP/MS pairing.

    The question span comes from each QP's printed "Total for Question N"
    footer. An exact page is added only when a prompt prefix uniquely matches
    page-level text; short/diagram-only items retain the question span.
    """
    qp_page, qp_method = None, "unlocated"
    normalized_pages = [_search_normalize(page) for page in qp_pages]
    tokens = _search_normalize(item.get("text", "")).split()
    for n in (12, 8, 5, 3):
        if len(tokens) < n:
            continue
        phrase = " ".join(tokens[:n])
        matches = [idx + 1 for idx, text in enumerate(normalized_pages) if phrase in text]
        if len(matches) == 1:
            qp_page, qp_method = matches[0], f"prompt-prefix-{n}-words"
            break
    if qp_page is None:
        label = re.compile(rf"\(\s*{re.escape(item['part'])}\s*\)", re.I)
        candidates = [idx + 1 for idx, text in enumerate(qp_pages) if label.search(text)]
        if len(candidates) == 1:
            qp_page, qp_method = candidates[0], "unique-part-label-only"

    qnum = int(item["q"])
    prior_end = 1 if qnum == 1 else q_ends.get(qnum - 1)
    this_end = q_ends.get(qnum)
    q_span = [prior_end + 1, this_end] if prior_end is not None and this_end is not None else None

    ms_page = None
    key = re.compile(
        rf"(?m)^\s*{re.escape(str(item['q']))}\s*\(\s*{re.escape(item['part'])}\s*\)\s*$",
        re.I,
    )
    matches = [idx + 1 for idx, page in enumerate(ms_pages) if key.search(page)]
    if len(matches) == 1:
        ms_page = matches[0]
    item["source_locator"] = {
        "qp_pdf_page": qp_page,
        "qp_question_page_span": q_span,
        "qp_locator_method": qp_method,
        "ms_pdf_page": ms_page,
        "locator_caveat": "Navigation hint only; not a visual transcription or QP/MS identity check.",
    }


def main():
    papers = []
    for qp in sorted(BASE.glob("*/*_QP.pdf")):
        if not re.search(r"P1R?_QP\.pdf$", qp.name):
            continue
        ms_path = qp.with_name(qp.name.replace("_QP.pdf", "_MS.pdf"))
        items = parse_qp(qp)
        ms = parse_ms(ms_path) if ms_path.exists() else {}
        session = qp.parent.name.replace("_", " ")
        paper = "P1R" if "P1R_" in qp.name else "P1"
        for it in items:
            it["answer"] = ms.get(f"{it['q']}{it['part']}", "")
        papers.append({
            "session": session,
            "paper": paper,
            "qp": str(qp.relative_to(ROOT)),
            "ms": str(ms_path.relative_to(ROOT)),
            "items": items,
            "total": sum(i["marks"] for i in items),
        })

    # Add documented official-Pearson supplements that are not yet in the
    # Paperlords archive. External source URLs and any MS-code discrepancies
    # remain visible in the generated record.
    supplements = json.loads(SUPPLEMENTS.read_text(encoding="utf-8")) if SUPPLEMENTS.exists() else {"papers": [], "overrides": []}
    for supplement in supplements.get("papers", []):
        qp_path = ROOT / supplement["qp"]
        if not qp_path.is_file():
            raise FileNotFoundError(f"Supplement QP not found: {qp_path}")
        items = parse_qp(qp_path)
        answer_map = supplement["answers"]
        item_keys = {f"{it['q']}{it['part']}" for it in items}
        if item_keys != set(answer_map):
            raise ValueError(
                f"Supplement answer keys do not match QP items for "
                f"{supplement['session']} {supplement['paper']}: "
                f"missing={sorted(item_keys - set(answer_map))}, "
                f"extra={sorted(set(answer_map) - item_keys)}"
            )
        text_overrides = supplement.get("text_overrides", {})
        for it in items:
            key = f"{it['q']}{it['part']}"
            it["answer"] = answer_map[key]
            if key in text_overrides:
                it["text"] = text_overrides[key]
            else:
                it["text"] = re.sub(r"(?m)^\s*(?:[\uf0a2\s]+|\(?\s*)$", "", it["text"])
                it["text"] = re.sub(r"(?m)^\s*Turn over\s*$", "", it["text"], flags=re.I)
                it["text"] = re.sub(r"(?m)^\s*\d{1,2}\s*$", "", it["text"])
                it["text"] = re.sub(r"\n{2,}", "\n", it["text"]).strip()
                it["text"] = "\n".join(line.rstrip() for line in it["text"].splitlines())
        papers.append({
            "session": supplement["session"],
            "paper": supplement["paper"],
            "qp": supplement["qp"],
            "ms": supplement["ms"],
            "source_note": supplement.get("source_note", ""),
            "items": items,
            "total": sum(i["marks"] for i in items),
        })

    for override in supplements.get("overrides", []):
        matches = [p for p in papers if p["session"] == override["session"] and p["paper"] == override["paper"]]
        if len(matches) != 1:
            raise ValueError(f"Expected one paper for item override: {override['session']} {override['paper']}")
        item = next((i for i in matches[0]["items"] if i["q"] == override["q"] and i["part"] == override["part"]), None)
        if item is None:
            raise ValueError(f"Item override target not found: {override}")
        if "answer" in override:
            item["answer"] = override["answer"]
        if "text" in override:
            item["text"] = override["text"]
        if "context_note" in override:
            item["context_note"] = override["context_note"]

    for paper in papers:
        qp_pages = _paper_page_text(_local_pdf_path(paper.get("qp")))
        ms_pages = _paper_page_text(_local_pdf_path(paper.get("ms")))
        q_ends = {}
        for page_number, page_text in enumerate(qp_pages, start=1):
            for qnum in re.findall(r"Total for Question\s*(\d+)", page_text, re.I):
                q_ends[int(qnum)] = page_number
        if qp_pages and set(q_ends) != {1, 2, 3, 4}:
            raise ValueError(f"QP footer locator failure for {paper['session']} {paper['paper']}: {q_ends}")
        for item in paper["items"]:
            locate_item_pages(qp_pages, ms_pages, q_ends, item)

    n_items = sum(len(p["items"]) for p in papers)
    n_ans = sum(1 for p in papers for i in p["items"] if i["answer"])
    n_marks = sum(p["total"] for p in papers)

    lines = [
        "# 4EC1/01 Paper 1 — Question + Mark Scheme Answer Bank",
        "",
        "Built by `build_paper1_qa_bank.py` from the Paperlords archive and documented official-Pearson supplements.",
        f"**{len(papers)} papers · {n_items} items · {n_marks} marks · {n_ans} items with an MS answer.**",
        "",
        "This machine-extracted index is provisional: some question stems leak later source passages",
        "because the parser does not yet fully respect PDF page/layout boundaries. Mark-scheme content",
        "is extracted from local official PDFs except where a source note documents a supplement.",
        "QP/MS page locators aid review but are not visual verification; consult the exact PDFs before use.",
        "Entries without a matched answer are marked `[MS NOT MATCHED]` — never filled in by hand.",
        "",
    ]
    for p in papers:
        lines.append(f"## {p['session']} — {p['paper']}  ({p['total']} marks)")
        lines.append("")
        qp_ref = f"[QP]({p['qp']})" if str(p['qp']).startswith("http") else f"`{p['qp']}`"
        ms_ref = f"[official Pearson MS]({p['ms']})" if str(p['ms']).startswith("http") else f"`{p['ms']}`"
        lines.append(f"QP: {qp_ref} · MS: {ms_ref}")
        if p.get("source_note"):
            lines.append("")
            lines.append(f"> Source note: {p['source_note']}")
        lines.append("")
        for it in p["items"]:
            ans = it["answer"] or "[MS NOT MATCHED]"
            ans = ans.replace("\n", " ").strip()
            ans = re.sub(r"\s{2,}", " ", ans)
            lines.append(f"**{it['q']}({it['part']}) — {it['marks']} marks.** {it['text']}")
            locator = it.get("source_locator", {})
            span = locator.get("qp_question_page_span")
            qref = f"QP Q{it['q']} PDF pages {span[0]}–{span[1]}" if span else "QP page span unlocated"
            if locator.get("qp_pdf_page"):
                qref += f"; prompt match p. {locator['qp_pdf_page']} ({locator['qp_locator_method']})"
            mref = f"; MS PDF p. {locator['ms_pdf_page']}" if locator.get("ms_pdf_page") else ""
            lines.append(f"- **Source locator (navigation only):** {qref}{mref}")
            if it.get("context_note"):
                lines.append(f"- **Context locator:** {it['context_note']}")
            lines.append("")
            lines.append(f"- **MS:** {ans}")
            lines.append("")
        lines.append("")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    OUT_JSON.write_text(json.dumps(papers, ensure_ascii=False, indent=1), encoding="utf-8")
    locators = [item.get("source_locator", {}) for paper in papers for item in paper["items"]]
    qp_spans = sum(loc.get("qp_question_page_span") is not None for loc in locators)
    qp_exact = sum(loc.get("qp_pdf_page") is not None for loc in locators)
    ms_exact = sum(loc.get("ms_pdf_page") is not None for loc in locators)
    print(f"papers={len(papers)} items={n_items} marks={n_marks} answers={n_ans} "
          f"coverage={n_ans / n_items:.1%}; QP question spans={qp_spans}, "
          f"unique QP prompt locators={qp_exact}, local MS item locators={ms_exact}")
    print(f"wrote {OUT_MD.relative_to(ROOT)} ({OUT_MD.stat().st_size / 1024:.0f} KB)")
    print(f"wrote {OUT_JSON.relative_to(ROOT)} ({OUT_JSON.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
