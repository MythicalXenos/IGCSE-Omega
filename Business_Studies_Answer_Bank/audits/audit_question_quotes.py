#!/usr/bin/env python3
"""
audit_question_quotes.py -- is the question the bank quotes the question that was asked?

Each entry in 10_Chain_Bank.md quotes the question(s) it answers, then names the session and
paper. This walks every quote back to the archive and classifies it:

  VERBATIM IN THE QUESTION PAPER   -- the words are on the paper
  VERBATIM IN THE MARK SCHEME      -- the words are the scheme's own description of the option
                                      (common in 9-mark justify questions, where the paper prints
                                      'Option 1: above the line promotion' and the scheme spells out
                                      what that means). Accurate, but a reader checking the paper
                                      will not find it.
  PARAPHRASE                       -- close, not exact; the task is the same
  NOT FOUND                        -- in neither document: the quote must be read by eye

Exit code is always 0: this produces a reading list, not a gate.
"""
import os, re, sys, zipfile, collections

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BANK = os.path.join(ROOT, "Business_Studies_Answer_Bank")
ZIP = os.path.join(ROOT, "Paperlords_Archive", "Paperlords_Searchable_Text_Index.zip")
CHAIN = os.path.join(BANK, "Perfect_Answers", "10_Chain_Bank.md")


def tokens(s):
    for a, b in (("\u2019", "'"), ("\u2018", "'"), ("\u201c", '"'), ("\u201d", '"'),
                 ("\u2013", "-"), ("\u2014", "-")):
        s = s.replace(a, b)
    return re.findall(r"[a-z0-9']+", s.lower())


def load():
    z = zipfile.ZipFile(ZIP)
    qp, ms, raw = {}, {}, {}
    for n in z.namelist():
        m = re.search(r"4BS1_Business_Studies_(.+?)_(P\dR?)_(QP|MS)\.txt$", n)
        if not m:
            continue
        k = (m.group(1), m.group(2))
        t = z.read(n).decode("utf-8", "ignore")
        raw[(k, m.group(3))] = t
        (qp if m.group(3) == "QP" else ms)[k] = tokens(t)
    return qp, ms, raw


def resolve(session):
    s = session.replace("\u2013", "-").replace("\u2014", "-").replace("/", " ")
    low = re.sub(r"\s+", " ", s).strip().lower()
    y = re.search(r"(19|20)\d\d", low)
    if not y:
        return None
    y = y.group(0)
    if low.startswith("nov"):
        return f"November_{y}"
    if y == "2023" and low.startswith("may"):
        return "May_2023"
    if y == "2026":
        return "June_2026"
    return f"May-June_{y}"


def run_len(hay, needle):
    js = " " + " ".join(hay) + " "
    best = 0
    n = len(needle)
    for start in range(n):
        for L in range(min(n - start, 45), best, -1):
            if " " + " ".join(needle[start:start + L]) + " " in js:
                best = L
                break
    return best


def main():
    qp, ms, raw = load()
    cite = re.compile(r'\*?"([^"\n]{8,320})"\*?\s*[\u2014\u2013-]\s*\*{0,2}'
                      r'([A-Za-z][A-Za-z\u2013\u2014\-/ ]{2,26}?\d{4})\*{0,2}\s*[,·]?'
                      r'\s*\*{0,2}\s*(P\dR?)?')
    text = open(CHAIN, encoding="utf-8").read()
    entries = []
    for m in re.finditer(r"^## (\d+)\.\s*(.+)$", text, re.M):
        start = m.end()
        nxt = re.search(r"^## \d+\.", text[start:], re.M)
        entries.append((int(m.group(1)), m.group(2).strip(),
                        text[m.start():start + (nxt.start() if nxt else len(text))]))

    res = collections.Counter()
    rows = []
    for num, title, body in entries:
        head = body.split("\n\n>")[0]
        pairs = cite.findall(head)
        if not pairs:
            res["no question quoted"] += 1
            continue
        for stem, session, paper in pairs:
            if stem.strip().startswith(("\u2026", "...", "of ")):
                res["fragment - not checkable"] += 1
                continue
            if not paper:
                res["citation names no paper"] += 1
                continue
            key = (resolve(session), paper)
            if key not in qp:
                res["paper not in archive"] += 1
                rows.append((num, title, session, paper, "PAPER NOT IN ARCHIVE", "", ""))
                continue
            needle = tokens(stem)
            total = len(needle)
            bq = run_len(qp[key], needle)
            bm = run_len(ms.get(key, []), needle)
            exact = bq >= 8 or (total <= 8 and bq >= max(4, total - 1)) or (total and bq / total >= .85)
            inexact = bm >= 8 or (total <= 8 and bm >= max(4, total - 1)) or (total and bm / total >= .85)
            if exact:
                res["verbatim in the question paper"] += 1
            elif inexact:
                res["verbatim in the mark scheme"] += 1
            elif total and max(bq, bm) / total >= 0.6:
                res["paraphrase"] += 1
                rows.append((num, title, session, paper, "PARAPHRASE", bq, bm))
            else:
                res["NOT FOUND in either"] += 1
                rows.append((num, title, session, paper, "NOT FOUND", bq, bm))

    print("=" * 96)
    print(f"EVERY QUESTION QUOTED IN THE CHAIN BANK — {len(entries)} entries")
    print("=" * 96)
    for k, v in res.most_common():
        print(f"  {k:<38} {v}")
    print("\n" + "=" * 96)
    print("NEEDS A HUMAN EYE — paraphrase and not-found, with the quoted words")
    print("=" * 96)
    for num, title, session, paper, why, bq, bm in rows:
        print(f"  #{num:<4} {title[:50]:<50} {session} {paper:<4} {why:<11} QP {bq} / MS {bm}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
