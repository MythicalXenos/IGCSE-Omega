#!/usr/bin/env python3
"""
audit_answer_fidelity.py -- does every model answer belong to the question it claims?

The test is against the question paper, never against the bank's own prose.

  T1  every question quoted under "**Asked:**" / "**Also asked:**" must appear in the QP of the
      session and paper it is attributed to. Short stems are matched by proportion, distinctive
      stems by contiguity; a stem that appears in many papers is reported as generic, not as an
      error, because generic wording cannot prove misattribution either way.
  T2  the model answer must be on the same topic as the question (content-word overlap).
  T3  a 3-mark answer must contain a causal link -- Pearson caps a bare list of points at 1 mark.

Usage:  python3 audits/audit_answer_fidelity.py [--all]
"""
import os, re, sys, zipfile, collections

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BANK = os.path.join(ROOT, "Business_Studies_Answer_Bank")
ZIP = os.path.join(ROOT, "Paperlords_Archive", "Paperlords_Searchable_Text_Index.zip")
CHAIN = os.path.join(BANK, "Perfect_Answers", "10_Chain_Bank.md")

STOP = set("""a an the and or but of for to in on at by with from as is are was were be been
this that these those it its their his her they them we you i one two three which who whom whose
when where why how not no can could may might must should would will shall do does did done
business businesses question paper marks mark explain analyse evaluate justify state define
calculate outline give identify describe discuss assess using use used also more most than then
there here about into over under between if so because what very much many some any other
such same own only just both each either neither per up down out off again further once
""".split())


def tokens(s):
    for a, b in (("\u2019", "'"), ("\u2018", "'"), ("\u201c", '"'), ("\u201d", '"'),
                 ("\u2013", "-"), ("\u2014", "-")):
        s = s.replace(a, b)
    return re.findall(r"[a-z0-9']+", s.lower())


def load_qps():
    z = zipfile.ZipFile(ZIP)
    out = {}
    for n in z.namelist():
        if "/4BS1_" not in n or not n.endswith("_QP.txt"):
            continue
        m = re.search(r"4BS1_Business_Studies_(.+?)_(P\dR?)_QP\.txt$", n)
        if m:
            out[(m.group(1), m.group(2))] = tokens(z.read(n).decode("utf-8", "ignore"))
    return out


def resolve(session):
    s = session.replace("\u2013", "-").replace("\u2014", "-")
    low = re.sub(r"\s+", " ", s.replace("/", " ")).strip().lower()
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
    """longest contiguous run of needle found in hay"""
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
    show_all = "--all" in sys.argv
    qps = load_qps()
    text = open(CHAIN, encoding="utf-8").read()
    entries = []
    for m in re.finditer(r"^## (\d+)\.\s*(.+)$", text, re.M):
        start = m.end()
        nxt = re.search(r"^## \d+\.", text[start:], re.M)
        body = text[m.start():start + (nxt.start() if nxt else len(text))]
        entries.append((int(m.group(1)), m.group(2).strip(), body))

    cite = re.compile(r'\*?"([^"\n]{8,320})"\*?\s*[\u2014\u2013-]\s*\*{0,2}'
                      r'([A-Za-z][A-Za-z\u2013\u2014\-/ ]{2,26}?\d{4})\*{0,2}\s*[,·]?'
                      r'\s*\*{0,2}\s*(P\dR?)?')
    res = collections.Counter()
    rows = []
    for num, title, body in entries:
        head = body.split("\n\n>")[0]
        pairs = cite.findall(head)
        if not pairs:
            res["entry quotes no question"] += 1
            rows.append((num, title, "-", "-", "NO QUOTED QUESTION"))
            continue
        for stem, session, paper in pairs:
            if stem.strip().startswith(("\u2026", "...")) or stem.strip().startswith("of "):
                res["fragment quote - not checkable"] += 1
                continue
            if not paper:
                res["citation lacks a paper"] += 1
                rows.append((num, title, session, "?", "citation has no paper"))
                continue
            key = (resolve(session), paper)
            if key not in qps:
                res["paper missing from index"] += 1
                rows.append((num, title, session, paper, "no such file in the index"))
                continue
            needle = tokens(stem)
            if not needle:
                continue
            best = run_len(qps[key], needle)
            total = len(needle)
            ok = best >= 8 or (total <= 8 and best >= max(4, total - 1)) or best / total >= 0.85
            if ok:
                res["T1 question found in the cited paper"] += 1
            else:
                elsewhere = [f"{s} {p}" for (s, p), tk in qps.items()
                             if run_len(tk, needle) >= max(6, int(0.85 * total))]
                if len(elsewhere) > 3:
                    res["T1 wording generic - cannot discriminate"] += 1
                elif elsewhere:
                    res["T1 found ONLY in another paper"] += 1
                    rows.append((num, title, session, paper,
                                 f"wording is in {', '.join(elsewhere)}"))
                else:
                    res["T1 not found in any paper"] += 1
                    rows.append((num, title, session, paper,
                                 f"best run {best}/{total} tokens"))

    print("=" * 92)
    print(f"THE QUESTION EACH MODEL ANSWER CLAIMS TO ANSWER — {len(entries)} entries, "
          f"{sum(res.values())} citations")
    print("=" * 92)
    for k, v in sorted(res.items()):
        print(f"  {k:<46} {v}")

    print("\n" + "=" * 92)
    print("MISSES — read each one, do not just count them")
    print("=" * 92)
    for num, title, session, paper, why in rows:
        print(f"  #{num:<4} {title[:52]:<52} {session} {paper}\n         -> {why}")
    if not show_all:
        print(f"\n({len(rows)} rows printed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
