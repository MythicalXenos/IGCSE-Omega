#!/usr/bin/env python3
"""
audit_tier_inventory.py -- how many scripts each report prints per question, and how many the
register holds for that question.

The mark line is read with the three phrasings the reports use, plus the "only gained N mark"
variant. Every capture is printed so the count can be eyeballed -- no silent regex trust.
"""
import os, re, sys, json, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS = os.path.join(ROOT, "audits", "corpus")
TALLY = os.path.join(ROOT, "Perfect_Answers", "09_Verified_Tally.md")

REPORTS = [("May/Jun 2023", "P1", "4BS1_01_2306"),
           ("May/Jun 2023", "P1R", "4BS1_01R_2306"),
           ("May/Jun 2023", "P2", "4BS1_02_2306"),
           ("May/Jun 2023", "P2R", "4BS1_02R_2306"),
           ("Jun 2026", "P1R", "4BS1_01R_2606")]

TARIFF = {"1(a)":1,"1(b)":1,"1(c)":1,"1(d)":1,"1(e)":2,"1(f)":3,"1(g)":6,
          "2(a)":1,"2(b)":1,"2(c)":3,"2(d)":3,"2(e)":3,"2(f)":9,
          "3(a)":1,"3(b)":2,"3(c)":2,"3(d)":6,"3(e)":9,
          "4(a)":2,"4(b)":6,"4(c)":12}

# Every marking line the five reports use. Each variant was observed and eyeballed:
#   This response scored N marks / This response only gained N marks / Total: N marks
#   This response was Level 3 - 7 marks / This response gained a Level 2 - 4 marks
#   This response is a Level 3 - 10 marks / This is a Level 3 response - 6 marks
MARK = re.compile(
    r"Total:\s*(?P<a>\d+)\s*marks?\b"
    r"|(?:This|this)\s+(?:response|candidate)[^.\n]{0,110}?\b(?P<b>\d+)\s*marks?\b"
    r"|This is a Level\s*\d+ response\s*[\u2013-]\s*(?P<c>\d+)\s*marks?\b")
NOTE = re.compile(r"of a Level\s*\d+ mark")
VALUE = re.compile(r"(\d+)\s*marks?\b")
HEAD = re.compile(r"Question\s+(\d)\s*\(([a-g])\)")


def printed(path):
    t = open(path, encoding="utf-8", errors="ignore").read()
    heads = [(m.start(), f"{m.group(1)}({m.group(2)})") for m in HEAD.finditer(t)]
    per = collections.defaultdict(list)
    caps = []
    for m in MARK.finditer(t):
        q = None
        for pos, h in heads:
            if pos < m.start():
                q = h
        if NOTE.search(m.group(0)):
            continue
        v = next((g for g in m.groups() if g), None)
        if q is None or v is None:
            continue
        per[q].append(int(v))
        caps.append((q, int(v), m.group(0)))
    return per, caps


def register_rows():
    lines = open(TALLY, encoding="utf-8").read().split("\n")
    tier, hdr, out = None, None, []
    for l in lines:
        m = re.match(r"^## (\d+) MARKS?\b", l)
        if m:
            tier = int(m.group(1)); hdr = None; continue
        if l.startswith("## "):
            tier = None; continue
        if l.startswith("|"):
            cells = [c.strip() for c in l.strip("|").split("|")]
            if cells and cells[0] == "#":
                hdr = cells; continue
            if tier and hdr and re.match(r"^\d+$", cells[0]):
                rec = dict(zip(hdr, cells))
                s = (rec.get("Series") or rec.get("Session") or "").replace("**", "").strip()
                s = {"Jun 2023": "May/Jun 2023"}.get(s, s)
                pq = re.sub(r"[*`]", "", rec.get("P · Q") or rec.get("Paper · Question") or "")
                mm = re.search(r"(P\dR?)\s*Q(\d)\(([a-g])\)", pq)
                if mm:
                    out.append((s, mm.group(1), f"{mm.group(2)}({mm.group(3)})", tier))
    return out


def main():
    reg = register_rows()
    regc = collections.Counter((s, p, q) for s, p, q, _ in reg)
    regtier = {(s, p, q): t for s, p, q, t in reg}
    print("=" * 96)
    print("PER-QUESTION INVENTORY — printed scripts vs register rows")
    print("=" * 96)
    printed_by_q = {}
    for series, paper, key in REPORTS:
        p = os.path.join(CORPUS, key + "_ER_full.txt")
        if not os.path.exists(p):
            print(f"{key}: corpus missing"); continue
        per, caps = printed(p)
        for q, vals in per.items():
            printed_by_q[(series, paper, q)] = sorted(vals, reverse=True)
        print(f"\n{series} {paper}  ({key})   scripts printed: {sum(len(v) for v in per.values())}")
        for q in sorted(per, key=lambda x: (int(x[0]), x[2])):
            vals = sorted(per[q], reverse=True)
            flag = "  ⚠ exceeds tariff" if any(v > TARIFF[q] for v in vals) else ""
            rows = regc.get((series, paper, q), 0)
            tier = regtier.get((series, paper, q), "-")
            mark = "" if rows == len(vals) else "   ← register holds %s" % rows
            print(f"   {q:<5} tariff {TARIFF[q]:>2}  printed {len(vals)} {str(vals):<22} "
                  f"register {rows} row(s) at {tier} marks{mark}{flag}")

    print("\n" + "=" * 96)
    print("TIER TOTALS across the five held reports")
    print("=" * 96)
    for tier in (1, 2, 3, 6, 9, 12):
        pr = sum(len(v) for (s, p, q), v in printed_by_q.items() if TARIFF[q] == tier)
        rr = sum(1 for s, p, q, t in reg if t == tier and TARIFF[q] == tier)
        print(f"  {tier:>2}-mark questions: printed {pr:>3}   register rows {rr:>3}")

    # every printed script the register does not name, and vice versa
    print("\nRegister rows naming a question whose printed scripts do not include that mark:")
    bad = 0
    for s, p, q, t in reg:
        vals = printed_by_q.get((s, p, q))
        if vals is None:
            continue
        if t not in vals:
            bad += 1
            print(f"   {s} {p} {q}: row at {t} marks; printed {vals}")
    print(f"   total: {bad} (all of these are the 0-mark half of a pair, or a question printed only once)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
