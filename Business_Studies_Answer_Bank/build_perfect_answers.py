#!/usr/bin/env python3
"""Parse all 38 4BS1 mark schemes into structured per-question records."""
import re, json
from collections import Counter
from pathlib import Path

IDX = Path("/tmp/textindex/IGCSE/4BS1_Business_Studies")

MARKER = re.compile(r"^\s*([1-4])\s*\(([a-z])\)\s*\(?\s*([ivx]+)\s*\)?\s*(?=\S)", re.MULTILINE)
MARKER_ALT = re.compile(r"^\s*([1-4])\s*\(([a-z])\)\s*(?=\S)", re.MULTILINE)
AOANY = re.compile(r"A\s*[O0]\s*([1-4])\s*(?:-|\u2013|\u2014|=)\s*(\d+)\s*marks?", re.IGNORECASE)
QHEAD = re.compile(r"^\s*Question\s{2,}(.+?)\s{2,}Mark\s*$", re.MULTILINE)
PAGE = re.compile(r"=====\s*PAGE\s+(\d+)\s*/\s*(\d+)\s*=====")

def page_of(text, pos):
    page = "?"
    for m in PAGE.finditer(text):
        if m.start() > pos: break
        page = m.group(1)
    return page

def all_markers(text):
    found = list(MARKER.finditer(text))
    covered = {(m.group(1), m.group(2)) for m in found}
    out = list(found)
    for m in MARKER_ALT.finditer(text):
        if (m.group(1), m.group(2)) not in covered:
            out.append(m)
    out.sort(key=lambda m: m.start())
    seen, uniq = set(), []
    for m in out:
        if m.start() not in seen:
            seen.add(m.start()); uniq.append(m)
    return uniq

def clean_qtext(s):
    if not s: return ""
    s = s.replace("\u2019","'").replace("\u2018","'").replace("\u00a0"," ")
    return re.sub(r"\s+"," ",s).strip().strip(".:").strip()

def parse_ms(path):
    text = path.read_text(encoding="utf-8", errors="replace").replace("\u00a0"," ")
    headers = []
    for m in QHEAD.finditer(text):
        t = clean_qtext(m.group(1))
        if t and t.lower() not in ("number","mark","answer"):
            headers.append((m.start(), t))
    marks = all_markers(text)
    records = []
    for i, m in enumerate(marks):
        start = m.end()
        end = marks[i+1].start() if i+1 < len(marks) else len(text)
        if end <= start: continue
        block = text[start:end]
        aos = AOANY.findall(block)
        if not aos: continue
        total = sum(int(v) for _, v in aos)
        qtext = ""
        for hpos, htxt in headers:
            if hpos < m.start(): qtext = htxt
            else: break
        records.append({"paper": path.stem, "qnum": m.group(1), "part": m.group(2),
                        "roman": (m.group(3) if (m.re.groups >= 3 and m.group(3)) else ""), "marks": total,
                        "aos": [f"AO{a}:{v}" for a, v in aos], "question": qtext,
                        "answer_raw": block, "page": page_of(text, m.start())})
    return records

def tidy_answer(body):
    out = []
    for ln in body.splitlines():
        if not ln.strip(): continue
        s = re.sub(r"[ \t]{3,}", " \u2503 ", ln.rstrip())
        s = re.sub(r"\s+", " ", s).strip()
        if s: out.append(s)
    return out

def main():
    recs, stats = [], {}
    for f in sorted(IDX.rglob("*_MS.txt")):
        r = parse_ms(f)
        for x in r:
            x["answer_lines"] = tidy_answer(x.pop("answer_raw"))
        recs.extend(r); stats[f.stem] = len(r)
    Path("/home/user/.scratch/ms_parsed.json").write_text(json.dumps(recs, indent=1), encoding="utf-8")
    print(f"papers parsed : {len(stats)}")
    print(f"total items   : {len(recs)}")
    print()
    bad = {k: v for k, v in stats.items() if v < 7}
    print(f"papers with <7 items: {len(bad)}")
    for k, v in sorted(bad.items(), key=lambda x: x[1]): print(f"  {v:>3}  {k}")
    print()
    print("mark distribution:", dict(sorted(Counter(r["marks"] for r in recs).items())))
    print("items with no question text:", sum(1 for r in recs if not r["question"]))
    print()
    print("=== SAMPLE: May 2023 P1 ===")
    for r in recs:
        if "May_2023_P1_MS" in r["paper"]:
            print(f"  {r['qnum']}({r['part']}){r['roman']:<4} {r['marks']:>2}m {str(r['aos']):<24} {r['question'][:52]}")

if __name__ == "__main__":
    main()
