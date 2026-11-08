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


# ---------------------------------------------------------------------------------------------
# ATTRIBUTING A QUOTE TO A REPORT
#
# The first version of this tool refused to touch a file that quotes more than one report, and
# that excluded 02_Verified_Exemplars.md and 10_Chain_Bank.md -- the TWO files that hold most of
# the bank's long quotes. "0 unsupported" from a tool that skipped both was vacuous, and was
# recorded as such.
#
# A quote does not need the file's identity; it needs the identity of the script ABOVE it. Every
# exemplar file states the session and paper in a source line or a heading before each script,
# so the tool now walks the file top to bottom carrying the last session and paper it saw.
# ---------------------------------------------------------------------------------------------
SESSION_RE = re.compile(r"\b(Jan|Jun|June|Nov|May/June|May/Jun|May)\s+(20\d\d)\b", re.I)
PAPER_RE = re.compile(r"\b(?:Paper\s*|4BS1[ _]0?|P)([12])\s*(R)?(?![0-9A-Za-z])", re.I)
TABLE_RE = re.compile(r"\*\*(May/Jun|Jun|Nov|May)\s+(20\d{2})\*\*\s*\|\s*(P[12])(R)?", re.I)
CODE_RE = re.compile(r"4BS1[ _](0[12]R?)[ _](\d{2})(\d{2})", re.I)


def _norm_session(word, year):
    w = word.lower().replace(".", "")
    if w in ("may/jun", "may", "jun", "june"):
        return ("May/Jun" if w.startswith("may") else "Jun") + " " + year
    if w.startswith("nov"):
        return "Nov " + year
    return "Jan " + year


CITATION_LIKE = re.compile(
    r"4BS1|Examiners' Report|Examiner's Report|Publications Code|^\s*#|"
    r"\*\*(?:May/Jun|Jun|Nov|May)\s+20\d{2}\*\*\s*\||"
    r"^\s*(?:\*\*)?(?:June|Jun|May/June|November|Nov|May)\s+20\d{2}\b",
    re.I)


def attribute(line, session, paper):
    """return (session, paper) after reading one line; carry the old value when the line is silent

    Only a line that actually CITES something is allowed to change the attribution. Matching on
    any prose mention of a month pulled quotes from 06_External_Source_Library into a Pearson
    report they never came from, and produced false alarms - the failure mode this whole bank
    keeps having to correct.
    """
    if not CITATION_LIKE.search(line):
        return session, paper
    m = CODE_RE.search(line)
    if m:
        code = m.group(1).upper()          # "01", "02R"
        yy, mm = m.group(2), m.group(3)
        sess = ("May/Jun " if mm == "05" else "Jun ") + "20" + yy
        return sess, "P" + code[1] + ("R" if code.endswith("R") else "")
    m = TABLE_RE.search(line)
    if m:
        return _norm_session(m.group(1), m.group(2)), "P" + m.group(3)[1] + (m.group(4) or "")
    sess = SESSION_RE.search(line)
    pap = PAPER_RE.search(line)
    if sess and pap:
        return _norm_session(sess.group(1), sess.group(2)), "P" + pap.group(1) + ("R" if pap.group(2) else "")
    if sess and not pap:
        # "Examiners' Report June 2025" under a heading that already named the paper, or a
        # file heading that names the session for every script below it
        return _norm_session(sess.group(1), sess.group(2)), paper
    if pap and not sess and session:
        return session, "P" + pap.group(1) + ("R" if pap.group(2) else "")
    return session, paper


# The report's own prose is quoted too -- "Candidates were able to give some valid reasons but
# again did not relate them..." A commentary quote is not a script, so failing to attribute it is
# not a gap in the script audit. Classifying them keeps the count honest in both directions.
COMMENTARY = re.compile(r"\b(candidates?|centres?|examiners?|cohort|level [123]\b|this response|"
                        r"marks? (?:were |was )?awarded|responses? (?:were|was|showed|gave))\b", re.I)


def is_commentary(text):
    return len(COMMENTARY.findall(text)) >= 2


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
    global LABELLED
    LABELLED = 0
    commentary = 0
    unattributed = 0
    NOT_SCRIPTS = {"00_Pearson_Official_Rulebook.md", "01_Mark_Tariff_Playbook.md",
                   "04_Type_Coverage_and_Gaps.md", "05_Constructed_12mark_Models.md",
                   "06_External_Source_Library.md", "07_Official_Exam_Scope.md",
                   "08_Completion_Map.md", "09_Verified_Tally.md", "11_Self_Marking_Protocol.md",
                   "README.md"}
    for path in sorted(glob.glob(os.path.join(PA, "**", "*.md"), recursive=True)):
        if os.path.basename(path) in NOT_SCRIPTS:
            continue
        body_all = open(path, encoding="utf-8", errors="ignore").read()
        stem = os.path.basename(path)
        fm = re.match(r"(20\d\d)-(\d\d)_(P\d\s?R?)(?![A-Za-z])", stem)
        f_session = f_paper = None
        if fm:
            yr, mo, pp = fm.group(1), fm.group(2), fm.group(3).replace(" ", "")
            f_session = {"06": f"Jun {yr}", "05": f"May/Jun {yr}", "11": f"Nov {yr}"}.get(mo)
            f_paper = pp
        session, paper = f_session, f_paper
        # walk the file once, keeping the session and paper that the LAST source line named
        raw_lines = body_all.split("\n")
        labelled_here = 0
        for lineno, line in enumerate(raw_lines, 1):
            m = QUOTE.match(line)
            if m:
                raw = m.group(1)
                words = norm(raw).split()
                if len(words) < min_words:
                    continue
                if "read from the printed script image" in " ".join(raw_lines[max(0, lineno - 3):lineno - 1]):
                    labelled_here += 1
                    LABELLED += 1
                    continue
                if not session or not paper:
                    if is_commentary(raw):
                        commentary += 1
                    else:
                        unattributed += 1
                    continue
                # the archive calls the June sitting "May/Jun" in some years and "Jun" in others;
                # Pearson's report is the same report either way.
                key = REPORT_OF.get((session, paper))
                if key is None and session.startswith("Jun "):
                    key = REPORT_OF.get(("May/" + session, paper))
                    if key is None and session.startswith("May/Jun "):
                        key = None
                rel = os.path.relpath(path, ROOT)
                if not key or key not in texts:
                    results.append((rel, session, paper, len(words), "no report held for this session/paper", raw))
                    continue
                sh = shingles(" ".join(words))
                hay = texts[key]
                hit = sum(1 for s_ in sh if s_ in hay)
                ratio = hit / len(sh) if sh else 0
                if ratio < 0.5:
                    results.append((rel, session, paper, len(words),
                                    f"only {ratio:.0%} of its 6-word runs appear in the report text",
                                    raw))
                continue
            session, paper = attribute(line, session, paper)

    if commentary:
        print(f"{commentary} long quote(s) of examiner commentary sit above any citation - "
              f"not script checks, so not counted as gaps\n")
    if unattributed:
        print(f"{unattributed} long quote(s) sit above any line naming a session and paper "
              f"- not checked\n")
    if LABELLED:
        print(f"{LABELLED} long quote(s) are already labelled as read from the script image - not reported\n")
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
    # --label: a quote that is NOT in the report's text layer was read from the printed script
    # image. Pearson prints every marked script as a picture, so this is normal -- but the bank's
    # own rule is that a scan-read transcript must SAY it is scan-read, and only two quotes in the
    # whole bank said so. This writes the label, in place, once per quote.
    if "--unlabel" in sys.argv:
        # A label is a claim too, and a wrong one is as bad as a missing one: this removes any
        # label whose quote the report's text layer DOES support. It caught the Cafe Pinch
        # examiner comment, which Pearson prints in text and which had been marked unverifiable.
        removed = 0
        for path in sorted(glob.glob(os.path.join(PA, "**", "*.md"), recursive=True)):
            if os.path.basename(path) in NOT_SCRIPTS:
                continue
            raw = open(path, encoding="utf-8").read().split("\n")
            session = paper = None
            out = []
            for i, line in enumerate(raw):
                if line.startswith("> **[") and ("read from the printed script image" in line
                                                 or "not in any text layer held" in line):
                    nxt = raw[i + 1] if i + 1 < len(raw) else ""
                    qm = QUOTE.match(nxt)
                    key = REPORT_OF.get((session, paper)) if (session and paper) else None
                    if qm and key in texts and len(norm(qm.group(1)).split()) >= min_words:
                        sh = shingles(norm(qm.group(1)))
                        hit = sum(1 for x in sh if x in texts[key])
                        if sh and hit / len(sh) >= 0.5:
                            removed += 1
                            print(f"  unlabelled {os.path.relpath(path, ROOT)}:{i + 1}")
                            continue
                    out.append(line)
                    continue
                if not QUOTE.match(line):
                    session, paper = attribute(line, session, paper)
                out.append(line)
            if "--write" in sys.argv:
                open(path, "w", encoding="utf-8").write("\n".join(out))
        print(f"\n{removed} label(s) removed" + ("" if "--write" in sys.argv else " (dry run)"))

    if "--label-unverified" in sys.argv:
        # The other half of the problem: a quote can be perfectly genuine and STILL be
        # unverifiable here, because the report it came from is not held in text form (the
        # June 2019 booklet, the November series). Saying nothing implies it was checked.
        WORD = ("> **[⚠️ not in any text layer held in this repo — a transcription, not a copy; "
                "re-check against the printed page before relying on it]**")
        todo = [r for r in results if not r[4].startswith("only")]
        print(f"\n--label-unverified: {len(todo)} quote(s) from reports not held in text form")
        if "--write" in sys.argv:
            by = {}
            for r in todo:
                by.setdefault(r[0], set()).add(" ".join(norm(r[5]).split()[:8]))
            for rel, heads in sorted(by.items()):
                path = os.path.join(ROOT, rel)
                lines = open(path, encoding="utf-8", errors="ignore").read().split("\n")
                out, added = [], 0
                for i, line in enumerate(lines):
                    m = QUOTE.match(line)
                    if m and len(norm(m.group(1)).split()) >= min_words:
                        head = " ".join(norm(m.group(1)).split()[:8])
                        prev = " ".join(lines[max(0, i - 2):i])
                        if head in heads and "not in any text layer held" not in line and "not in any text layer held" not in prev:
                            out.append(WORD)
                            added += 1
                    out.append(line)
                if added:
                    open(path, "w", encoding="utf-8").write("\n".join(out))
                print(f"  {rel}: {added}")

    if "--label" in sys.argv:
        LABEL = ("> **[read from the printed script image — these words are not in the PDF's "
                 "text layer, so they are a transcription, not a copy]**")
        if "--write" not in sys.argv:
            print("\n--label without --write: nothing changed")
        else:
            todo = {}
            for r in results:
                if r[4].startswith("only"):
                    todo.setdefault(r[0], set())
            print("\nlabelled quotes by file:")
            for rel in sorted({r[0] for r in results if r[4].startswith("only")}):
                path = os.path.join(ROOT, rel)
                lines = open(path, encoding="utf-8", errors="ignore").read().split("\n")
                out, added = [], 0
                for i, line in enumerate(lines):
                    m = QUOTE.match(line)
                    if m and len(norm(m.group(1)).split()) >= min_words \
                            and ("read from the printed script image" in line
                                 or (i and "read from the printed script image" in lines[i - 1])
                                 or (i > 1 and "read from the printed script image" in lines[i - 2])):
                        out.append(line)
                        continue
                    if m and len(norm(m.group(1)).split()) >= min_words:
                        # is this the quote the audit flagged? match on the first 8 words
                        head = " ".join(norm(m.group(1)).split()[:8])
                        if any(" ".join(norm(r[5]).split()[:8]) == head
                               for r in results if r[0] == rel and r[4].startswith("only")):
                            out.append(LABEL)
                            added += 1
                    out.append(line)
                if added:
                    open(path, "w", encoding="utf-8").write("\n".join(out))
                print(f"  {rel}: {added}")
    json.dump([{"file": r[0], "session": r[1], "paper": r[2], "words": r[3], "why": r[4], "quote": r[5]}
               for r in results], open(os.path.join(CORPUS, "quotes_not_in_textlayer.json"), "w"), indent=1)
    print(f"\nwrote audits/corpus/quotes_not_in_textlayer.json")


if __name__ == "__main__":
    main()
