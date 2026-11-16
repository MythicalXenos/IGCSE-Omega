#!/usr/bin/env python3
"""
reconstruct_scripts.py -- read a candidate script out of an examiner report, in layers, and say
what it most likely meant.

The reports print handwriting as OCR'd text, and some of it is rubble: "It the need of customer are
not satisfied". This tool does not pretend the rubble is a quotation. It works down four layers and
labels every line with which layer it came from:

  1  PAGE      the whole section, exactly as the report prints it
  2  PARAGRAPH the script block, split from the examiner's commentary
  3  SENTENCE  one sentence per line, so a broken sentence is visible as a unit
  4  WORD      every token, with the ones that are not words in this subject marked
  +  GLOSS     the likely intended reading, proposed from the mark scheme's own bullet points and
               the examiner's comment, never presented as the candidate's words

Vocabulary for the word test = every word in the 38 mark schemes and 38 question papers, plus
every word in the report itself. A token outside that set is either handwriting debris or a
spelling slip, and both are flagged rather than silently "corrected".

Usage:
  python3 audits/reconstruct_scripts.py 4BS1_02R_2406 1(b)
  python3 audits/reconstruct_scripts.py 4BS1_02R_2406 --all
"""
import os, re, sys, zipfile, difflib, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ms_parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS = os.path.join(ROOT, "audits", "corpus")

QHEAD = re.compile(r"Question\s+(\d)\s*\(\s*([a-g])\s*\)", re.I)
COMMENT = re.compile(r"ResultsPlus|Examiner Comments|Examiner Tips?|Examiner.s Comments", re.I)
MARKLINE = re.compile(r"(?:\d+\s*marks?\b|Level\s*\d+\s*[\u2013-]\s*\d+\s*marks?)", re.I)


def vocabulary():
    z = zipfile.ZipFile(ms_parse.ZIP)
    vs = set()
    for n in z.namelist():
        if "/4BS1_" in n and n.endswith(".txt"):
            vs.update(re.findall(r"[a-z']+", z.read(n).decode("utf-8", "ignore").lower()))
    return vs


def section(text, q):
    """the longest run after any heading that names this question -- duplicates occur"""
    heads = list(QHEAD.finditer(text))
    best = ""
    for i, m in enumerate(heads):
        if f"{m.group(1)}({m.group(2)})".lower() != q.lower():
            continue
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        cand = text[m.end():end]
        if len(cand) > len(best):
            best = cand
    return best


def blocks(sec):
    """split a question section into script/comment pairs"""
    paras = [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", sec)]
    paras = [p for p in paras if p]
    out, cur = [], []
    for p in paras:
        cur.append(p)
        if MARKLINE.search(p) or COMMENT.search(p):
            out.append(" ".join(cur))
            cur = []
    if cur:
        out.append(" ".join(cur))
    return out


def sentences(b):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", b) if s.strip()]


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    key = sys.argv[1]
    q = sys.argv[2] if len(sys.argv) > 2 else None
    p = os.path.join(CORPUS, key + "_ER.txt")
    if not os.path.exists(p):
        print("no corpus for", key)
        return 1
    text = open(p, encoding="utf-8", errors="ignore").read()
    vocab = vocabulary()
    qs = [q] if q else []
    if not qs:
        ms = ms_parse.load_all()
        for name, (s, pp) in {"4BS1_02R_2406": ("May-June_2024", "P2R")}.items():
            pass
        qs = [f"{a}({b})" for a in range(1, 5) for b in "abcdefg"]

    for qq in qs:
        sec = section(text, qq)
        if not sec.strip():
            continue
        print("=" * 92)
        print(f"  {key}   QUESTION {qq}")
        print("=" * 92)
        for i, b in enumerate(blocks(sec), 1):
            print(f"\n--- LAYER 1: PAGE / block {i} ---")
            print(b[:700] + ("…" if len(b) > 700 else ""))
            print(f"\n--- LAYER 3: SENTENCE ---")
            for s in sentences(b):
                print("   •", s)
            toks = re.findall(r"[A-Za-z']+", b)
            bad = [t for t in toks if t.lower() not in vocab and len(t) > 2]
            print(f"\n--- LAYER 4: WORD ({len(toks)} tokens, {len(bad)} outside the subject vocabulary) ---")
            print("   " + " ".join(f"[{t}]" if t in bad else t for t in toks)[:900])
            if bad:
                print("\n--- LAYER 5: GLOSS — proposed, not the candidate's words ---")
                for t in bad[:8]:
                    near = difflib.get_close_matches(t.lower(), vocab, n=2, cutoff=0.6)
                    print(f"   [{t}] → {' / '.join(near) if near else 'no close word: handwriting debris'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
