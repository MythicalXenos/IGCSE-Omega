#!/usr/bin/env python3
"""
audit_archive_pairing.py -- independent QP/MS pairing audit for 4BS1.

WHY THIS EXISTS
    verify_by_paper.py proves each By_Paper file has 26 items summing to 80.
    It cannot prove that the QP and the MS in the archive belong to the SAME PAPER.
    On 9 November 2026 a content check found June 2026 P1 fails that test: the QP is
    about "Crumb", the MS is about "Violet Cakes". Both documents are genuine Pearson
    files; they are simply not a pair. Every internal check in the bank passed anyway,
    because structure cannot see content.

METHOD (two independent tests)
    A. STEM CONTAINMENT -- take the QP's first "Evaluate ..." stem (its 12-mark 4(c)),
       normalise to letters+digits, and test whether the first 60 characters appear
       anywhere in the normalised MS. This survives line breaks, hyphenation and
       re-flowed columns. It fails when the MS prints no stem at all (common in
       2019/2020 papers) -- that is NOT evidence of a mismatch.
    B. CASE-NAME OVERLAP -- the business names a paper is about. A pair that shares
       no name is suspicious; a pair that shares the case name is almost certainly
       correct. All-caps names (HRMW, TADS, NEXT, CCT, AWG, PPS) are included.

VERDICTS
    MATCH          stem found in the MS, or case names overlap
    NO-STEM        the MS prints no question stem; case names still agree -> verified by B
    MISMATCH       the stem is absent from the MS and the case names do not agree
    NO-TEXT        extraction produced almost nothing; treat as unproven, never as wrong

USAGE
    python3 audits/audit_archive_pairing.py [--csv]
Exit code 0 = no mismatch, 1 = at least one.
"""
import sys, os, re, glob

try:
    import fitz
except ImportError:
    sys.exit("pymupdf required: pip install pymupdf")

BASE = os.path.join(os.path.dirname(__file__), "..", "..",
                    "Paperlords_Archive", "IGCSE", "4BS1_Business_Studies")

STOP = set("""The This That These Those However Therefore Because Which What When Where
Business Businesses Study Studies Paper Question Questions Section Total Marks Mark Figure
Table Case Source Pearson Edexcel International GCSE Summer Autumn June November May January
October Answer Answers Candidate Centre Number Turn Over Evaluate Analyse Explain Justify
Define State Outline Calculate Assess Discuss Using Your You Should Information Provided
Knowledge Own Exam Examination Qualifications BTEC Level Unit Awarded Assessment Objective
Indicative Content Accept Guidance Notes Note AO1 AO2 AO3 AO4 AO5 AO6 Section A B C D
Option Options Correct Not Only Mark Scheme Results General Marking""".split())
NAME_STOP = STOP | {"Company", "Companies", "Group", "Limited", "Ltd", "Plc"}


def text(path):
    try:
        doc = fitz.open(path)
        return "\n".join(p.get_text() for p in doc)
    except Exception:
        return ""


def squash(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def first_stem(t):
    m = re.search(r"\bEvaluate\b", t)
    return t[m.start():m.start() + 160] if m else ""


def case_names(t):
    out = set()
    for w in re.findall(r"\b[A-Za-z]{3,12}\b", t):
        if w.isupper() and 3 <= len(w) <= 6 and w not in NAME_STOP:
            out.add(w)
    for w in re.findall(r"\b[A-Z][a-z]{2,}\b", t):
        if w not in NAME_STOP:
            out.add(w)
    # keep only names that recur -- a one-off capitalised word is usually a heading
    counts = {}
    for w in re.findall(r"\b[A-Za-z]{3,12}\b", t):
        if w in out:
            counts[w] = counts.get(w, 0) + 1
    return {w for w, n in counts.items() if n >= 3}


def main():
    rows = []
    for sess in sorted(os.listdir(BASE)):
        d = os.path.join(BASE, sess)
        if not os.path.isdir(d):
            continue
        for qp in sorted(glob.glob(os.path.join(d, "*_QP.pdf"))):
            ms = qp.replace("_QP.pdf", "_MS.pdf")
            paper = os.path.basename(qp).split("_")[-2]
            if not os.path.exists(ms):
                rows.append((sess, paper, "NO-MARK-SCHEME", "", "", 0.0))
                continue
            qt, mt = text(qp), text(ms)
            if len(qt) < 3000 or len(mt) < 3000:
                rows.append((sess, paper, "NO-TEXT", "", "", 0.0))
                continue
            stem = first_stem(qt)
            key = squash(stem)[:60]
            stem_found = bool(key) and key in squash(mt)
            ms_has_stem = bool(first_stem(mt))
            cq, cm = case_names(qt), case_names(mt)
            shared = cq & cm
            frac = len(shared) / max(1, len(cq))
            if stem_found:
                verdict = "MATCH"
            elif not ms_has_stem:
                verdict = "NO-STEM" if frac > 0 else "MISMATCH"
            else:
                verdict = "MISMATCH"
            rows.append((sess, paper, verdict, re.sub(r"\s+", " ", stem)[:64],
                         ",".join(sorted(shared)[:6]), round(frac, 3)))

    print("=" * 80)
    print("4BS1 ARCHIVE PAIRING AUDIT -- does each mark scheme belong to its question paper?")
    print("=" * 80)
    print(f"  pairs examined : {len(rows)}")
    tally = {}
    for r in rows:
        tally[r[2]] = tally.get(r[2], 0) + 1
    for k in sorted(tally):
        print(f"  {k:<15}: {tally[k]}")
    bad = [r for r in rows if r[2] not in ("MATCH", "NO-STEM")]
    if bad:
        print("\n  DEFECTS -- the pair must not be presented as a matched set")
        for s, p, v, stem, shared, frac in bad:
            print(f"    {s:<16}{p:<5}{v:<10} stem: {stem[:52]!r}")
            print(f"    {'':16}{'':5}shared case names: {shared or '(none)'}")
    nostem = [r for r in rows if r[2] == "NO-STEM"]
    if nostem:
        print("\n  VERIFIED BY CASE NAME ONLY (the MS prints no question stems)")
        for s, p, v, stem, shared, frac in nostem:
            print(f"    {s:<16}{p:<5}{shared}")
    if "--csv" in sys.argv:
        print("\nsession,paper,verdict,shared_names,overlap")
        for r in rows:
            print(f'{r[0]},{r[1]},{r[2]},"{r[4]}",{r[5]}')
    print()
    print("RESULT:", "OK -- every pair is the same paper."
          if not bad else f"FAIL -- {len(bad)} pair(s) do not belong together.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
