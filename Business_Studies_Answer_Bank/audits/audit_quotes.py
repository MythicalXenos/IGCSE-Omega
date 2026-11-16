#!/usr/bin/env python3
"""
audit_quotes.py -- verify every quotation in the 4BS1 bank against primary sources.

WHY
    The bank's authority rests on the sentence "every quotation is verbatim". Nothing tested
    that. This does. It reads every .md file in the bank, extracts every double-quoted span of
    eight words or more, and asks whether those words appear in a primary source held locally:
        38 mark schemes + 38 question papers + 5 full examiner reports.
    Quotations from Pearson web pages are NOT in this corpus; they are listed separately by the
    caller and checked by hand (see AUDIT_REPORT §2.4).

OUTPUT
    matched / near-matched / unmatched, with file:line for each unmatched span, so each one can
    be read and judged rather than trusted.

USAGE
    python3 audits/audit_quotes.py [--all]
Exit 0 always: this is a reading list, not a gate.
"""
import os, re, sys, glob, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS_DIRS = [
    os.path.join(ROOT, "audits", "corpus"),
]

def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("–", "-").replace("—", "-").replace("…", "...")
    s = re.sub(r"[^a-z0-9' ]", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()

def corpus():
    import fitz
    texts = []
    for d in CORPUS_DIRS:
        for f in glob.glob(os.path.join(d, "*.txt")):
            texts.append(open(f, encoding="utf-8", errors="ignore").read())
    arch = os.path.join(ROOT, "..", "Paperlords_Archive", "IGCSE", "4BS1_Business_Studies")
    for f in sorted(glob.glob(os.path.join(arch, "*", "*_MS.pdf"))) + \
             sorted(glob.glob(os.path.join(arch, "*", "*_QP.pdf"))):
        try:
            texts.append("\n".join(p.get_text() for p in fitz.open(f)))
        except Exception:
            pass
    return norm(" \n ".join(texts))

def quotes_from(path):
    out = []
    for i, line in enumerate(open(path, encoding="utf-8", errors="ignore"), 1):
        for m in re.finditer(r'"([^"\n]{40,400})"', line):
            out.append((i, m.group(1)))
    return out

def main():
    C = corpus()
    files = [p for p in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True)
             if "/audits/" not in p]
    total = hit = near = miss = 0
    misses = []
    for f in files:
        for ln, q in quotes_from(f):
            n = norm(q)
            if len(n.split()) < 8:
                continue
            total += 1
            if n in C:
                hit += 1
            else:
                # try a long leading fragment: catches quotes that the bank truncated
                frag = " ".join(n.split()[:8])
                if frag in C:
                    near += 1
                else:
                    miss += 1
                    misses.append((os.path.relpath(f, ROOT), ln, q[:110]))
    print("=" * 78)
    print("4BS1 QUOTATION AUDIT — do the bank's quotations exist in its own sources?")
    print("=" * 78)
    print(f"  quoted spans of 8+ words : {total}")
    print(f"  found verbatim           : {hit}")
    print(f"  first-8-words found      : {near}   (quoted with different tail)")
    print(f"  NOT FOUND                : {miss}")
    print()
    if "--all" in sys.argv:
        for f, ln, q in misses:
            print(f"  {f}:{ln}\n      {q}")
    else:
        from collections import Counter
        c = Counter(f for f, _, _ in misses)
        for f, k in c.most_common():
            print(f"  {k:>3}  {f}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
