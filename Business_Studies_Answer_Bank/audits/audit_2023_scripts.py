#!/usr/bin/env python3
"""
audit_2023_scripts.py -- check every 2023 script the bank quotes against the report page it claims.

WHY
    The May/June 2023 examiner reports were read by rendering script pages and transcribing them
    by eye. A transcription by eye can drift: a word added, a struck-through word silently
    repaired, a sentence tidied. This compares each quoted block to the OCR of the report and
    reports the overlap. It is a screen, not a proof: OCR of handwriting is imperfect, so a low
    score means LOOK AT IT, and a high score means the page really does carry those words.

METHOD
    For each .md file whose name contains 2023, take every blockquote block (the script) and every
    quoted examiner comment, strip markdown emphasis and strikethrough, tokenise to lowercase
    words of 4+ letters, and compute the best token-overlap against every page of every 2023
    report. Report the best page and the overlap.
"""
import os, re, json, glob, sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OCR = os.path.join(ROOT, "audits", "corpus", "ocr")

def toks(s):
    s = s.replace("~~", "").replace("**", "").replace("*", "").replace("_", "")
    s = s.replace("’", "'").replace("“", '"').replace("”", '"')
    return [w for w in re.findall(r"[a-z]{4,}", s.lower())]

def ocr_pages():
    pages = []
    for f in sorted(glob.glob(os.path.join(OCR, "*.json"))):
        name = os.path.basename(f)[:-5]
        for pg, lines in json.load(open(f)).items():
            pages.append((name, int(pg), Counter(toks(" ".join(lines)))))
    return pages

def blocks(path):
    """Yield (first_line_number, text) for blockquote blocks and inline quoted comments."""
    out, cur, start = [], [], None
    for i, line in enumerate(open(path, encoding="utf-8", errors="ignore"), 1):
        if line.startswith(">"):
            if not cur:
                start = i
            cur.append(line.lstrip("> ").rstrip())
        else:
            if cur:
                out.append((start, " ".join(cur)))
                cur = []
    if cur:
        out.append((start, " ".join(cur)))
    return out

def main():
    pages = ocr_pages()
    files = [p for p in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True) if "2023" in os.path.basename(p)]
    rows = []
    for f in files:
        for ln, text in blocks(f):
            t = Counter(toks(text))
            if sum(t.values()) < 25:
                continue
            best = (0.0, "", 0)
            for name, pg, c in pages:
                common = sum((t & c).values())
                if not common:
                    continue
                score = common / sum(t.values())
                if score > best[0]:
                    best = (score, name, pg)
            rows.append((os.path.relpath(f, ROOT), ln, sum(t.values()), *best))
    rows.sort(key=lambda r: r[3])
    print("=" * 92)
    print("2023 SCRIPT VERIFICATION — quoted words vs the OCR of the report page")
    print("=" * 92)
    print(f"  blocks checked: {len(rows)}\n")
    for f, ln, n, score, name, pg in rows:
        flag = "OK  " if score >= 0.60 else ("MID " if score >= 0.35 else "LOW ")
        print(f"  {flag} {score:0.2f}  {n:>4}w  {f}:{ln}  ->  {name} p{pg}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
