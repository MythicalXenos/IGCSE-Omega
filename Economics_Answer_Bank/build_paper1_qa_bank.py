#!/usr/bin/env python3
"""Build a searchable Paper 1 (4EC1/01) question + mark-scheme answer bank.

Sources: Paperlords_Archive/IGCSE/4EC1_Economics/*/ (QP + MS pairs), plus
`Paper1_QA_Supplements.json` for documented official Pearson sources outside the
archive. Supplement QPs must be locally available; their answer keys and source
URLs are maintained in the supplement file.

Output:
  Economics_Answer_Bank/Paper1_QA_Bank.md    human/searchable view
  Economics_Answer_Bank/Paper1_QA_Bank.json  machine index

Evidence policy (see README.md): every answer below is transcribed from the
official Pearson mark scheme. Nothing here is constructed. Where a mark-scheme
block could not be matched to its item, the entry is marked [MS NOT MATCHED]
rather than filled in.
"""
import json
import re
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
        body = re.split(r"\(Total for Question|TOTAL FOR PAPER|Question\s*\n\s*number", body)[0]
        body = clean(body)
        key = f"{m.group(1)}{m.group(2)}"
        if len(body) > len(out.get(key, "")):
            out[key] = body
    return out


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
            raise ValueError(f"Expected one paper for answer override: {override['session']} {override['paper']}")
        item = next((i for i in matches[0]["items"] if i["q"] == override["q"] and i["part"] == override["part"]), None)
        if item is None:
            raise ValueError(f"Answer override item not found: {override}")
        item["answer"] = override["answer"]

    n_items = sum(len(p["items"]) for p in papers)
    n_ans = sum(1 for p in papers for i in p["items"] if i["answer"])
    n_marks = sum(p["total"] for p in papers)

    lines = [
        "# 4EC1/01 Paper 1 — Question + Mark Scheme Answer Bank",
        "",
        "Built by `build_paper1_qa_bank.py` from the Paperlords archive and documented official-Pearson supplements.",
        f"**{len(papers)} papers · {n_items} items · {n_marks} marks · {n_ans} items with an MS answer.**",
        "",
        "Every item below is an official Pearson question. Answers are transcribed from the",
        "matching Pearson mark scheme; any concise paraphrases or summarized descriptor tables",
        "are identified in that paper’s source note. Items without a matched answer are marked",
        "`[MS NOT MATCHED]` — they are never filled in by hand.",
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
            lines.append("")
            lines.append(f"- **MS:** {ans}")
            lines.append("")
        lines.append("")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    OUT_JSON.write_text(json.dumps(papers, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"papers={len(papers)} items={n_items} marks={n_marks} answers={n_ans} "
          f"coverage={n_ans / n_items:.1%}")
    print(f"wrote {OUT_MD.relative_to(ROOT)} ({OUT_MD.stat().st_size / 1024:.0f} KB)")
    print(f"wrote {OUT_JSON.relative_to(ROOT)} ({OUT_JSON.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
