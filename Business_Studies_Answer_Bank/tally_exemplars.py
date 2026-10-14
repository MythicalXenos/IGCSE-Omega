#!/usr/bin/env python3
"""Verify the verified-exemplar register, and flag anything unregistered.

WHY THIS EXISTS
---------------
The bank carried hand-written counts ("the bank now holds six 9/9s") sitting
directly above a list of fourteen. A hand-written total is an assertion; a
derived total is evidence.

The first version of this script simply counted *headings* that name a mark.
That was worse than useless in a subtle way: it printed **17 / 14 / 4** against a
register of **19 / 15 / 2**, because it also counted

  * rule sections that discuss "THE 9/9" or "THE 12/12" without printing one,
  * cross-references to a script whose transcript lives in another file, and
  * repeated references to the same script.

A count that is wrong in a *new* way every time it is run is not evidence either.

WHAT IT DOES NOW
----------------
1. **Parses the register itself** — `09_Verified_Tally.md` — and treats it as
   the source of truth: one row per distinct full-mark script, each with a
   canonical `file:line`.
2. **Checks every row resolves** — the file exists and the line it names carries
   the mark token. A register row pointing at nothing is a broken claim.
3. **Scans the whole bank for script-bearing headings and matches them to the
   register.** A heading is *script-bearing* if it names a question label
   (`Q2(f)`, `Q4(c)`) or one of the register's case studies. Everything else is
   narrative and is ignored — that is the restatement filter, and it is why this
   script no longer counts a rule heading as a lost script.
4. **Prints any heading that is script-bearing and NOT accounted for by the
   register.** That list is the only thing worth reading. An empty list means
   the register is complete against the bank's own prose.

Exit code is 0 when the register verifies and 1 when it does not, so this can be
run as a check rather than read as a report.

Run from Business_Studies_Answer_Bank/:  python3 tally_exemplars.py
"""
import re, sys, pathlib, collections

ROOT = pathlib.Path(__file__).parent / "Perfect_Answers"
REGISTER = ROOT / "09_Verified_Tally.md"
TOKEN = re.compile(r"(?<![\d/])(3/3|6/6|9/9|12/12)(?![\d/])")
ROW = re.compile(r"^\|\s*\d+\s*\|(.+)\|\s*`([^`]+?):(\d+)`\s*\|\s*$")
QLABEL = re.compile(r"\bQ\s?(\d)\s?\(([a-z])\)")
RULEY = re.compile(r"^\s*(?:\d+\.|#{2,4}\s*\d+\.)|ANATOMY|WHAT THIS|HOW TO|THE TEST|"
                   r"REQUIRED FEATURES|NON-NEGOTIABLE|CHECKLIST", re.I)


def parse_register():
    """Return [(tariff, label_text, file, line)] from the register's tables."""
    rows, tariff = [], None
    for line in REGISTER.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^##\s*(3|6|9|12)\s*MARKS", line)
        if m:
            # 3 joined the register on 14 Oct 2026 (four June 2026 Explain
            # scripts). It was left out of this regex at first, which made this
            # script print TOTAL: 40 while verify_coverage_claims.py printed 44
            # from the same file - two checks disagreeing about the same data is
            # exactly the failure this script exists to prevent.
            tariff = {"3": "3/3", "6": "6/6", "9": "9/9", "12": "12/12"}[m.group(1)]
            continue
        if line.startswith("## "):
            tariff = None
        if tariff and (rm := ROW.match(line)):
            label, f, ln = rm.group(1), rm.group(2).strip(), int(rm.group(3))
            rows.append((tariff, label, f, ln))
    return rows


def resolve(rows):
    """Every register row must point at a real file and a line carrying the mark."""
    bad = []
    for tariff, label, f, ln in rows:
        path = ROOT / f
        if not path.exists():
            # register also cites files by a shortened name (e.g. "2023-05_Series…md")
            hits = list(ROOT.rglob(f.split(":")[0])) if "/" not in f else []
            if not hits:
                bad.append((tariff, label, f, ln, "file not found"))
                continue
            path = hits[0]
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        window = lines[max(0, ln - 4): ln + 4]
        # a row may be sourced to a heading that states the mark in words
        # ("Level 3 – 6 marks — FULL MARKS") rather than as "6/6".
        n = int(tariff.split("/")[0])
        words = re.compile(rf"(?<![\d/]){n}(?![\d/])\s*marks?\b", re.I)
        if not any(TOKEN.search(w) or words.search(w) for w in window):
            bad.append((tariff, label, f, ln, "no mark token near that line"))
    return bad


def register_labels(rows):
    """Question labels and case names the register knows about."""
    labels, names = set(), set()
    for tariff, label, f, ln in rows:
        for q in QLABEL.findall(label):
            labels.add((tariff, f"q{q[0]}{q[1]}"))
        for tok in re.split(r"[^A-Za-z]+", label):
            if len(tok) > 3 and tok[0].isupper():
                names.add(tok.lower())
    return labels, names


def scan(heading_only=True):
    out = []
    for f in sorted(ROOT.rglob("*.md")):
        for i, line in enumerate(f.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if not line.lstrip().startswith("#"):
                continue
            if "not counted" in line:
                continue
            tok = TOKEN.search(line)
            if not tok:
                continue
            out.append((tok.group(1), str(f.relative_to(ROOT)), i, line.strip("# ").strip()))
    return out


def main():
    rows = parse_register()
    bad = resolve(rows)
    labels, names = register_labels(rows)
    counts = collections.Counter(t for t, *_ in rows)

    print("=" * 78)
    print("REGISTER — 09_Verified_Tally.md")
    print("=" * 78)
    for t in ("3/3", "6/6", "9/9", "12/12"):
        print(f"  {t}: {counts[t]} rows")
    print(f"  TOTAL: {sum(counts.values())}")
    print()
    if bad:
        print("!! ROWS THAT DO NOT RESOLVE")
        for t, label, f, ln, why in bad:
            print(f"   {t}  {f}:{ln}  ({why})  {label[:60]}")
    else:
        print("OK  every register row resolves to a real file and a real mark token.")

    print()
    print("=" * 78)
    print("CANDIDATE HEADINGS FOUND IN THE BANK")
    print("=" * 78)
    unaccounted, narrative, matched = [], 0, 0
    for tariff, f, ln, txt in scan():
        qs = QLABEL.findall(txt)
        key = f"q{qs[0][0]}{qs[0][1]}" if qs else None
        if key and (tariff, key) in labels:
            matched += 1
            continue
        named = {t.lower() for t in re.split(r"[^A-Za-z]+", txt) if len(t) > 3}
        if named & names:
            matched += 1
            continue
        if RULEY.search(txt) or not key:
            narrative += 1
            continue
        unaccounted.append((tariff, f, ln, txt))

    print(f"  matched to a register row : {matched}")
    print(f"  narrative / rule headings : {narrative}   (ignored — the restatement filter)")
    print(f"  UNACCOUNTED               : {len(unaccounted)}")
    for tariff, f, ln, txt in unaccounted:
        print(f"    !! {tariff}  {f}:{ln}  {txt[:90]}")
    print()
    print("=" * 78)
    ok = not bad and not unaccounted
    print("RESULT:", "OK — the register is complete against the bank's own prose."
          if ok else "FAIL — see the rows above. Fix the register, not this script.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
