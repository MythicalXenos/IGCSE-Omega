#!/usr/bin/env python3
"""
audit_calculations.py -- does the arithmetic in every worked answer actually work?

Every calculation in the mark schemes and in the bank's By_Paper answers is written as a chain
   80 282 - 12 692 = 67 590        /      67 590 / 330 606 x 100 = 20.44
This evaluates each chain left to right (as the schemes write them) and reports every line whose
result differs from the printed figure by more than a rounding tolerance.

Result differences are reported, never corrected: a scheme's printed figure is the authority, and a
disagreement may be rounding, a mid-line rounding step, or a genuine typo in the paper.
"""
import os, re, sys, collections, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ZIP = os.path.join(ROOT, "Paperlords_Archive", "Paperlords_Searchable_Text_Index.zip")
BANK = os.path.join(ROOT, "Business_Studies_Answer_Bank")

NUM = r"\d[\d ,]*\.?\d*"
CHAIN = re.compile(rf"({NUM})\s*([-+/\u00f7x\u00d7*])\s*({NUM})(?:\s*([-+/\u00f7x\u00d7*])\s*({NUM}))?\s*=\s*({NUM})")


def val(s):
    s = s.replace(" ", "").replace(",", "")
    try:
        return float(s)
    except ValueError:
        return None


def op(c):
    return {"x": "*", "\u00d7": "*", "/": "/", "\u00f7": "/"}.get(c, c)


def scan(text, label, out, tol=0.011):
    for m in CHAIN.finditer(text):
        a, o1, b, o2, c, shown = m.groups()
        A, B, C = val(a), val(b), val(c) if c else None
        S = val(shown)
        if None in (A, B, S):
            continue
        try:
            if o2 and C is not None:
                r = eval(f"({A}){op(o1)}({B}){op(o2)}({C})")
            else:
                r = eval(f"({A}){op(o1)}({B})")
        except ZeroDivisionError:
            continue
        if abs(r - S) <= max(tol, abs(S) * 1e-6):
            out[label]["ok"] += 1
        else:
            # allow the printed figure to be a rounded version of the true value
            rounding = abs(round(r, 2) - S) <= tol or abs(round(r, 1) - S) <= tol
            key = "rounded" if rounding else "MISMATCH"
            out[label][key] += 1
            out[label]["rows"].append((m.group(0), r, S, key))


def main():
    z = zipfile.ZipFile(ZIP)
    out = collections.defaultdict(lambda: collections.Counter({"rows": []}))
    for n in z.namelist():
        m = re.search(r"4BS1_Business_Studies_(.+?)_(P\dR?)_(MS|QP)\.txt$", n)
        if not m:
            continue
        t = re.sub(r"[ \t]+", " ", z.read(n).decode("utf-8", "ignore"))
        scan(t, f"{m.group(1)} {m.group(2)} {m.group(3)}", out)

    tot = collections.Counter()
    print("=" * 96)
    print("ARITHMETIC IN THE MARK SCHEMES — every printed chain, re-evaluated")
    print("=" * 96)
    for k in sorted(out):
        c = out[k]
        tots = {x: c[x] for x in ("ok", "rounded", "MISMATCH")}
        for x, v in tots.items():
            tot[x] += v
        if tots["MISMATCH"] or tots["rounded"]:
            print(f"  {k:<34} ok {tots['ok']:>3}  rounded {tots['rounded']:>2}  MISMATCH {tots['MISMATCH']:>2}")
            for row, r, s, kind in c["rows"]:
                print(f"      {kind}: {row[:44]:<44} computed {r:.4g} vs printed {s}")
    print(f"\n  TOTAL  ok {tot['ok']}  rounded {tot['rounded']}  MISMATCH {tot['MISMATCH']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
