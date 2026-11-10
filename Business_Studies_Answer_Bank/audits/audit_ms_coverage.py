#!/usr/bin/env python3
"""
audit_ms_coverage.py -- does each model answer cover the mark scheme's own AO points?

For every governed question (3, 6, 9, 12 marks) the mark scheme lists indicative content under
AO1/AO2/AO3/AO4. A constructed answer that ignores a whole AO cannot reach the top band, however
well written. This measures, per bullet, how much of the scheme's own wording the answer touches,
and prints every bullet it does not touch so the gap can be read.

Overlap is token-based on distinctive words (numbers, business terms), not on phrasing, because a
good answer paraphrases deliberately. A LOW score therefore means "the answer says nothing on this
point", not "the answer used different words" -- but it is still evidence to read, not a verdict.

Usage: python3 audits/audit_ms_coverage.py [--min N] [--show-all]
"""
import os, re, sys, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ms_parse

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CHAIN = os.path.join(ROOT, "Business_Studies_Answer_Bank", "Perfect_Answers", "10_Chain_Bank.md")

STOP = set("""a an the and or but of for to in on at by with from as is are was were be been
this that these those it its their his her they them we you i one two three which who whom whose
when where why how not no can could may might must should would will shall do does did done
business businesses customers customer also more most than then there here about into over under
between if so because what very much many some any other such same own only just both each either
neither per up down out off again further once e g ie etc""".split())


def words(s):
    for a, b in (("\u2019", "'"), ("\u2018", "'"), ("\u2013", "-"), ("\u2014", "-")):
        s = s.replace(a, b)
    return [w for w in re.findall(r"[a-z0-9']+", s.lower()) if w not in STOP and len(w) > 2]


QSTEM = re.compile(r"\(([a-g])\)")


def qp_stems():
    import zipfile
    z = zipfile.ZipFile(ms_parse.ZIP)
    out = {}
    for n in z.namelist():
        m = re.search(r"4BS1_Business_Studies_(.+?)_(P\dR?)_QP\.txt$", n)
        if not m:
            continue
        t = re.sub(r"[ \t]+", " ", z.read(n).decode("utf-8", "ignore"))
        hits = list(QSTEM.finditer(t))
        d = {}
        qn, prev = 0, "a"
        for i, mm in enumerate(hits):
            letter = mm.group(1)
            if letter == "a" or letter <= prev:
                qn += 1
            prev = letter
            end = hits[i + 1].start() if i + 1 < len(hits) else len(t)
            body = t[mm.end():end]
            body = re.split(r"\.{4,}|\n\n\n|===== PAGE", body)[0]
            body = re.sub(r"\s+", " ", body).strip()
            if len(body.split()) < 4:
                continue
            d.setdefault(f"{qn}({letter})", body[:400])
        out[(m.group(1), m.group(2))] = d
    return out


def run_len(hay, needle):
    h = " " + " ".join(hay) + " "
    best = 0
    n = len(needle)
    for st in range(n):
        for L in range(min(n - st, 40), best, -1):
            if " " + " ".join(needle[st:st + L]) + " " in h:
                best = L
                break
    return best


def entries():
    text = open(CHAIN, encoding="utf-8").read()
    out = []
    for m in re.finditer(r"^## (\d+)\.\s*(.+)$", text, re.M):
        start = m.end()
        nxt = re.search(r"^## \d+\.", text[start:], re.M)
        out.append((int(m.group(1)), m.group(2).strip(),
                    text[m.start():start + (nxt.start() if nxt else len(text))]))
    return out


def model_answer(body):
    m = re.search(r"Model answer[^\n]*\n((?:>.*\n?)+)", body)
    if not m:
        return ""
    return re.sub(r"^>\s?", "", m.group(1), flags=re.M).strip()


CITE = re.compile(r'\*?"([^"\n]{8,320})"\*?\s*[\u2014\u2013-]\s*\*{0,2}'
                  r'([A-Za-z][A-Za-z\u2013\u2014\-/ ]{2,26}?\d{4})\*{0,2}\s*[,·]?'
                  r'\s*\*{0,2}\s*(P\dR?)?')


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


def main():
    show_all = "--show-all" in sys.argv
    data = ms_parse.load_all()
    stems = qp_stems()
    res = collections.Counter()
    gaps = []
    for num, title, body in entries():
        ans = model_answer(body)
        if not ans:
            continue
        aw = set(words(ans))
        head = body.split("\n\n>")[0]
        cites = [(stem_txt, (resolve(s), p)) for stem_txt, s, p in CITE.findall(head) if p]
        matched = None
        for stem_txt, key in cites:
            if key not in data or key not in stems:
                continue
            needle = words(stem_txt)
            best_q, best = None, 0
            for q, qs_txt in stems[key].items():
                r = run_len(words(qs_txt), needle)
                if r > best:
                    best_q, best = q, r
            if best_q and best >= 4:
                matched = (key, best_q)
                break
        if not matched:
            res["entry could not be tied to a question"] += 1
            continue
        key, q = matched
        v = data[key].get(q)
        if not v or not v["bullets"]:
            res["question has no AO bullets"] += 1
            continue
        res["entries tested"] += 1
        # the scheme offers ALTERNATIVE points, so an untaken bullet is not a defect.
        # What matters is whether the answer works in every AO the question awards marks for.
        by_ao = collections.defaultdict(list)
        for ao, b in v["bullets"]:
            by_ao[ao].append((overlap(b, aw), b))
        for ao in sorted(v["ao"]):
            pts = by_ao.get(ao, [])
            if not pts:
                res[f"AO{ao}: scheme gives no bullet"] += 1
                continue
            best_o, best_b = max(pts)
            if best_o >= 0.30:
                res[f"AO{ao}: covered"] += 1
            elif best_o >= 0.15:
                res[f"AO{ao}: partly covered"] += 1
                gaps.append((num, title, key, q, ao, round(best_o, 2), best_b))
            else:
                res[f"AO{ao}: NOT covered"] += 1
                gaps.append((num, title, key, q, ao, round(best_o, 2), best_b))

    print("=" * 100)
    print("MARK-SCHEME POINT COVERAGE — each model answer against its own scheme's AO bullets")
    print("=" * 100)
    for k, v in res.most_common():
        print(f"  {k:<32} {v}")
    print("\n" + "=" * 100)
    print("WHOLE-AO GAPS — the answer may reword a point, but it cannot ignore an AO")
    print("=" * 100)
    shown = collections.Counter()
    for num, title, key, q, ao, o, b in gaps:
        if not show_all and shown[num] >= 2:
            continue
        shown[num] += 1
        print(f"  #{num:<4} {key[0]} {key[1]} {q:<5} AO{ao}  {o:<5} {b[:96]}")
    print(f"\n  total gap rows: {len(gaps)} across {len(shown)} entries")
    return 0


def overlap(bullet, aw):
    bw = words(bullet)
    if len(bw) < 3:
        return 1.0
    hit = sum(1 for w in set(bw) if w in aw)
    return hit / len(set(bw))


if __name__ == "__main__":
    sys.exit(main())
