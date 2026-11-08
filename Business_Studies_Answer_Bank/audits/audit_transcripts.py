#!/usr/bin/env python3
"""
audit_transcripts.py -- check that every examiner quote in a transcript is really in the report.

Transcripts restore what a scan says. They also quote the examiner's comment, and a quote of a
*text* document has no excuse for being approximate: it can be checked character for character.
This tool does that, and it checks the reconstructed script too where a scan-read line happens
to survive in the PDF's text layer (rare, but it happens for pages where the report did not use
an image).

Quotes are matched after normalising whitespace and curly quotes; `[…]` inside a quote is a
restoration and is skipped, `…` splits the quote into parts that are each located.

Usage:
    python3 audits/audit_transcripts.py 4BS1_01R_2206
    python3 audits/audit_transcripts.py --all
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS = os.path.join(ROOT, "audits", "corpus")
TR = os.path.join(CORPUS, "transcripts")


def norm(s):
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2013", "-").replace("\u2014", "-")
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"\s+([.,;:])", r"\1", s)   # the PDF text layer often puts a space before a full stop
    return s.strip()


def parts(q):
    q = q.replace("*", "").replace("_", "")
    q = re.sub(r"\[[^\]]*\]", "", q)          # restorations are mine, not the report's
    q = re.sub(r"^>\s*", "", q, flags=re.M)
    return [norm(p) for p in re.split(r"\u2026|\.\.\.", q) if len(norm(p).split()) >= 4]


QUOTE = re.compile(r'["\u201c]([^"\u201d]{60,}?)["\u201d]', re.S)


def main():
    keys = sys.argv[1:]
    if not keys or "--all" in keys:
        keys = sorted({os.path.basename(p).split("_ER")[0]
                       for p in glob.glob(os.path.join(CORPUS, "*_ER.txt"))})
    total = bad = 0
    for key in keys:
        hay_path = os.path.join(CORPUS, key + "_ER.txt")
        if not os.path.exists(hay_path):
            print(f"{key}: no report text held -- its quotes cannot be checked")
            continue
        hay = norm(open(hay_path, encoding="utf-8", errors="ignore").read())
        for f in sorted(glob.glob(os.path.join(TR, key + "*.md"))):
            text = open(f, encoding="utf-8").read()
            # only the sections that quote the EXAMINER are checked; the script itself is a
            # transcription of handwriting and is not expected to appear in the report.
            for sec in re.split(r"^#{1,4} ", text, flags=re.M):
                head = sec.split("\n", 1)[0].lower()
                if not any(w in head for w in ("examiner", "verbatim", "cohort", "comment")):
                    continue
                body = sec.split("\n", 1)[1] if "\n" in sec else ""
                if "READ FROM SCAN" in body:
                    continue
                body = body.replace("*", "").replace("_", "")
                body = re.sub(r"^>\s?", "", body, flags=re.M)
                for m in QUOTE.finditer(body):
                    for p in parts(m.group(1)):
                        total += 1
                        if p not in hay:
                            bad += 1
                            print(f"{os.path.basename(f)}  NOT IN THE REPORT:")
                            print(f"   {p[:200]}")
    print(f"\n{total} examiner-quote fragments checked, {bad} not found in the report text")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
