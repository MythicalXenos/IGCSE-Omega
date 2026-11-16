#!/usr/bin/env python3
"""
audit_register_against_er.py -- test each row of the register against the report it cites.

For every row in Perfect_Answers/09_Verified_Tally.md this asks three questions:
  1. is the report the row cites one we actually hold?
  2. does that report print a script for the question named?
  3. is the mark printed for that question the mark the row's section claims?

A row passes only if all three are yes. Anything else is printed with the reason.
"""
import os, re, sys, json, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TALLY = os.path.join(ROOT, "Perfect_Answers", "09_Verified_Tally.md")
INV = json.load(open(os.path.join(ROOT, "audits", "corpus", "inventory.json")))
_extra = json.load(open(os.path.join(ROOT, "audits", "corpus", "inventory_extra.json")))
for _k, _v in _extra.items():
    INV[_k] = _v["marks"]

# June 2019: no examiner report is held, but Pearson's own exemplar booklets are, and they print
# each response with its score. They count as a held source for the questions they cover.
BOOKLETS = {"Jun 2019": [("P1", "4BS1_P1_Exemplar_Booklet_2019"),
                         ("P1R", "4BS1_P1_Exemplar_Booklet_2019"),
                         ("P2", "4BS1_P2_Exemplar_Booklet_2019")]}

BOOKLET_MARK = re.compile(r"This response (?:was given|gained|scored)\s+(?:Level\s*\d+\s*[\u2013-]\s*)?(\d+)\s*marks?")
BOOKLET_HEAD = re.compile(r"Question (\d)\(([a-g])\)(?: \(Paper (\dR)\))?")

REPORT_SESSIONS = {
    "4BS1_01_2206":  ("Jun 2022", "P1"),
    "4BS1_01R_2206": ("Jun 2022", "P1R"),
    "4BS1_02R_2206": ("Jun 2022", "P2R"),
    "4BS1_01_2306":  ("May/Jun 2023", "P1"),
    "4BS1_01R_2306": ("May/Jun 2023", "P1R"),
    "4BS1_02_2306":  ("May/Jun 2023", "P2"),
    "4BS1_02R_2306": ("May/Jun 2023", "P2R"),
    "4BS1_01_2406":  ("Jun 2024", "P1"),
    "4BS1_01R_2406": ("Jun 2024", "P1R"),
    "4BS1_02_2406":  ("Jun 2024", "P2"),
    "4BS1_01R_2506": ("Jun 2025", "P1R"),
    "4BS1_02_2506": ("Jun 2025", "P2"),
    "4BS1_02R_2506": ("Jun 2025", "P2R"),
    "4BS1_01R_2606": ("Jun 2026", "P1R"),
}
_er = json.load(open(os.path.join(ROOT, "audits", "corpus", "inventory_er.json")))
HELD = {}
for _key, (_s, _p) in REPORT_SESSIONS.items():
    if _key in _er:
        HELD[(_s, _p)] = _key
        # inventory_er.json is the fresh read of the stored PDFs and supersedes the older
        # inventory.json, which was built before the singular-"1 mark" and word-number
        # phrasings were handled and therefore under-reports some grades.
        INV[_key] = _er[_key]

# reports read from Pearson's live PDF but not stored as a file -- counted, and labelled
READ_LIVE = {("Jun 2024", "P2R"): "4BS1_02R_2406",
             ("Jun 2025", "P1"): "4BS1_01_2506"}
LIVE = set()
for (_s, _p), _key in READ_LIVE.items():
    if _key in _extra:
        HELD[(_s, _p)] = _key
        INV.setdefault(_key, _extra[_key]["marks"])
        LIVE.add((_s, _p))

TIER = re.compile(r"^## (\d+) MARKS?\b")
ROW = re.compile(r"^\|\s*(\d+)\s*\|")


def main():
    lines = open(TALLY, encoding="utf-8").read().split("\n")
    tier, hdr = None, None
    results = collections.Counter()
    per_key = collections.Counter()
    rows = []
    for i, l in enumerate(lines, 1):
        m = TIER.match(l)
        if m:
            tier = int(m.group(1)); hdr = None; continue
        if l.startswith("## "):
            tier = None; continue
        if l.startswith("|") and not ROW.match(l):
            cells = [c.strip() for c in l.strip("|").split("|")]
            if cells and cells[0] == "#":
                hdr = cells
            continue
        if tier and ROW.match(l):
            cells = [c.strip() for c in l.strip("|").split("|")]
            if hdr is None or len(cells) < 3: continue
            rec = dict(zip(hdr, cells))
            rows.append((i, tier, rec))

    print("=" * 92)
    print(f"REGISTER vs REPORT — {len(rows)} rows, {sum(1 for r in rows if r[1])} with a mark tier")
    print("=" * 92)
    uncheckable = []
    for i, t, rec in rows:
        series = (rec.get("Series") or rec.get("Session") or "").replace("**", "").strip()
        series = {"Jun 2023": "May/Jun 2023"}.get(series, series)
        pq = re.sub(r"[*`]", "", rec.get("P · Q") or rec.get("Paper · Question") or "")
        m = re.search(r"(P\dR?)\s*Q(\d)\(([a-g])\)", pq)
        if not m:
            results["NO QUESTION PARSED"] += 1
            print(f"  L{i:<4} {t:>2}mk  {series:<12} {pq:<14}  ⚠ no question in row")
            continue
        paper, qn, ql = m.group(1), m.group(2), m.group(3)
        q = f"{qn}({ql})"
        # The register annotates a row whose printed script(s) did not earn full marks, e.g.
        # "**(0/1 and 1/1)**" or "**(0/2 x3 -- no full mark printed)**". Those annotations ARE
        # the claim; reading the section tier as the claim turned honest rows into mismatches.
        cell = rec.get("Topic") or rec.get("P · Q") or ""
        ann = re.findall(r"\((\d+)/(\d+)", cell)
        claim = {int(a) for a, _ in ann} if ann else {t}
        key = HELD.get((series, paper))
        if key is None and series in BOOKLETS:
            bp = os.path.join(ROOT, "audits", "corpus", BOOKLETS[series][0][1] + ".txt")
            for p2, stem in BOOKLETS[series]:
                if p2 != paper:
                    continue
                bp = os.path.join(ROOT, "audits", "corpus", stem + ".txt")
                if not os.path.exists(bp):
                    continue
                btext = open(bp, encoding="utf-8").read()
                heads = [(m.start(), f"{m.group(1)}({m.group(2)})", m.group(3))
                         for m in BOOKLET_HEAD.finditer(btext)]
                vals = []
                for m in BOOKLET_MARK.finditer(btext):
                    bq, pg = None, None
                    for pos, h, pgp in heads:
                        if pos < m.start():
                            bq, pg = h, pgp
                    vals.append((bq, pg, int(m.group(1))))
                hit = [v for qq, pg, v in vals
                       if qq == q and (pg is None or pg == paper)]
                marks = sorted(hit, reverse=True)
                if not marks:
                    continue
                if claim <= set(marks):
                    results["VERIFIED (Pearson exemplar booklet)"] += 1
                else:
                    results["mark mismatch"] += 1
                    print(f"  L{i:<4} {tier:>2}mk  {series:<12} {paper} {q:<6}  ✗ booklet: printed {marks}")
                break
            else:
                results["booklet silent on this question"] += 1
                print(f"  L{i:<4} {tier:>2}mk  {series:<12} {paper} {q:<6}  · booklet prints nothing here")
            continue
        if key is None:
            results["report not held"] += 1
            uncheckable.append((series, paper, q, t))
            continue
        marks = INV[key].get(q)
        if not marks:
            results["question not printed"] += 1
            print(f"  L{i:<4} {t:>2}mk  {series:<12} {paper} {q:<6}  ✗ {key}: no script printed for this question")
            continue
        if claim <= set(marks):
            per_key[key] = per_key.get(key, 0) + 1
            results["VERIFIED (report stored)" if (series, paper) not in LIVE
                    else "VERIFIED (report read live, not stored)"] += 1
        else:
            results[f"mark mismatch"] += 1
            extra = f" (row annotates {sorted(claim)}/1)" if claim != {t} else ""
            print(f"  L{i:<4} {t:>2}mk  {series:<12} {paper} {q:<6}  ✗ {key}: printed marks {marks}, row claims {sorted(claim)}{extra}")
    if "--by-report" in sys.argv:
        print("\n--- verified rows per source ---")
        for k, n in sorted(per_key.items(), key=lambda kv: (-kv[1], kv[0])):
            print(f"  {k:<24} {n:>3}")
    print("\n--- summary ---")
    for k, v in results.most_common():
        print(f"  {k:<26} {v}")
    print(f"\n  rows whose report we do not hold: {len(uncheckable)}")
    per = collections.Counter((s, p) for s, p, _, _ in uncheckable)
    for (s, p), n in sorted(per.items(), key=lambda x: -x[1]):
        print(f"     {s:<14} {p:<4} {n:>3} rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())
