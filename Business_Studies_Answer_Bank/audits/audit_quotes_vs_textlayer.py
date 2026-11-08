#!/usr/bin/env python3
"""
audit_quotes_vs_textlayer.py -- which of the bank's long quotes could NOT have come from the
PDF's text layer?

The Starbucks case (June 2025 P2 1(g)) showed the failure mode: the report prints the script as
an image, the text layer carries only the commentary, and a quote built from the text layer is
therefore *partial* without anyone noticing.

This tool takes every quoted block in the exemplar files and asks a single question: **do these
words appear anywhere in the text of the report they cite?** If they do not, the quote came from
the picture - so it is only as good as the eye that read it, and it belongs on the list to be
checked against the image.

It does not judge the quote. It sorts the bank into "verifiable from text" and "read from a scan".

Usage: python3 audits/audit_quotes_vs_textlayer.py [--min-words 25]
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS = os.path.join(ROOT, "audits", "corpus")
PA = os.path.join(ROOT, "Perfect_Answers")

REPORT_OF = {   # (session, paper) -> corpus key
    ("Jun 2022", "P1"): "4BS1_01_2206", ("Jun 2022", "P1R"): "4BS1_01R_2206",
    ("Jun 2022", "P2R"): "4BS1_02R_2206",
    ("May/Jun 2023", "P1"): "4BS1_01_2306", ("May/Jun 2023", "P1R"): "4BS1_01R_2306",
    ("May/Jun 2023", "P2"): "4BS1_02_2306", ("May/Jun 2023", "P2R"): "4BS1_02R_2306",
    ("Jun 2024", "P1"): "4BS1_01_2406", ("Jun 2024", "P1R"): "4BS1_01R_2406",
    ("Jun 2024", "P2"): "4BS1_02_2406",
    ("Jun 2025", "P1R"): "4BS1_01R_2506", ("Jun 2025", "P2"): "4BS1_02_2506",
    ("Jun 2025", "P2R"): "4BS1_02R_2506", ("Jun 2026", "P1R"): "4BS1_01R_2606",
}

# A script quote is a block-quote line that OPENS with a quotation mark -- that is the
# convention every exemplar file uses ("*\"...\"*"). Commentary lines start with ** or ⭐
# and are not quotes; counting them turned this tool into a machine for false alarms.
QUOTE = re.compile(r"^>\s*(?:\*\*\[READ FROM SCAN\]\*\*\s*)?\*[\"“](.{40,})", re.M)


def norm(t):
    t = re.sub(r"[*_`>#\[\]()\-–—]", " ", t)
    t = t.replace("’", "'").replace("“", '"').replace("”", '"')
    t = re.sub(r"[^A-Za-z0-9' ]", " ", t)
    return re.sub(r"\s+", " ", t).strip().lower()


def shingles(s, n=6):
    w = s.split()
    return {" ".join(w[i:i + n]) for i in range(max(0, len(w) - n + 1))}


def main():
    min_words = 25
    if "--min-words" in sys.argv:
        min_words = int(sys.argv[sys.argv.index("--min-words") + 1])

    texts = {}
    for key in REPORT_OF.values():
        p = os.path.join(CORPUS, key + "_ER.txt")
        if os.path.exists(p):
            texts[key] = norm(open(p, encoding="utf-8", errors="ignore").read())
    # the two reports read live but not stored
    for extra in ("4BS1_01_2506_ER_excerpt", "4BS1_02R_2406_ER"):
        p = os.path.join(CORPUS, extra + ".txt")
        if os.path.exists(p):
            texts[extra] = norm(open(p, encoding="utf-8", errors="ignore").read())

    results = []
    skipped = []
    for path in sorted(glob.glob(os.path.join(PA, "**", "*.md"), recursive=True)):
        body_all = open(path, encoding="utf-8", errors="ignore").read()
        # only exemplar sections: a heading that states a score (3/3, 6/6, 9/9 ...) is a script
        secs = re.split(r"^#{1,3} ", body_all, flags=re.M)
        body = "\n".join(x for x in secs if re.match(r".*?\b\d+/\d+", x.split("\n", 1)[0]))
        if not body:
            continue
        # the session and paper this file is about, from its own heading or filename
        # which report? the filename is the reliable place: 2022-06_P1R_..., 2023-05_P2_...
        stem = os.path.basename(path)
        fm = re.match(r"(20\d\d)-(\d\d)_(P\d\s?R?)(?![A-Za-z])", stem)
        key, session, paper = None, None, None
        if fm:
            yr, mo, pp = fm.group(1), fm.group(2), fm.group(3).replace(" ", "")
            session = {"06": f"Jun {yr}", "05": f"May/Jun {yr}"}.get(mo)
            paper = pp
            key = REPORT_OF.get((session, paper))
        if key is None:
            # This tool is only valid for a file that is about ONE paper. The consolidated files
            # (02_Verified_Exemplars.md and friends) quote a dozen reports each, so a quote cannot
            # be attributed to a report by the file it sits in -- skip them rather than guess.
            skipped.append(os.path.relpath(path, ROOT))
            continue
        for q in QUOTE.finditer(body):
            raw = q.group(1)
            words = norm(raw).split()
            if len(words) < min_words:
                continue
            if not key or key not in texts:
                results.append((os.path.relpath(path, ROOT), session, paper, len(words), "no report held", raw))
                continue
            sh = shingles(" ".join(words))
            hay = texts[key]
            hit = sum(1 for s in sh if s in hay)
            ratio = hit / len(sh) if sh else 0
            if ratio < 0.5:
                results.append((os.path.relpath(path, ROOT), session, paper, len(words),
                                f"only {ratio:.0%} of its 6-word runs appear in the report text",
                                raw))

    if skipped:
        print(f"skipped {len(skipped)} consolidated files (more than one report each):")
        for s_ in skipped:
            print("   " + s_)
        print()
    print(f"{len(results)} long quotes are not supported by the report's TEXT layer "
          f"(>= {min_words} words)\n")
    by_file = {}
    for r in results:
        by_file.setdefault(r[0], []).append(r)
    for f, rs in by_file.items():
        print(f"{f}  ({len(rs)})")
        for _, s, p, n, why, raw in rs:
            print(f"   {s} {p}  {n} words  -- {why}")
            print(f"      {raw.strip()[:110]}")
    json.dump([{"file": r[0], "session": r[1], "paper": r[2], "words": r[3], "why": r[4], "quote": r[5]}
               for r in results], open(os.path.join(CORPUS, "quotes_not_in_textlayer.json"), "w"), indent=1)
    print(f"\nwrote audits/corpus/quotes_not_in_textlayer.json")


if __name__ == "__main__":
    main()
