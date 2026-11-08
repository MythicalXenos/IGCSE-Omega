#!/usr/bin/env python3
"""
repair_citations.py -- keep the register's line citations pointing at the exemplar.

Every row of Perfect_Answers/09_Verified_Tally.md ends with `path:line`. The line is a real
citation and it drifts every time a file above it is edited -- which is exactly what happened
when the June 2022 Paper 1R entries were rewritten from the scans: six rows began pointing at
the wrong line, and one pointed at a "# PAPER 1" heading, making the paper look wrong when it
was not.

This re-points each row at the heading that carries its question number in the cited file.
It never changes WHICH file is cited, only the line, and it reports every move.

    python3 audits/repair_citations.py            # report only
    python3 audits/repair_citations.py --write
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TALLY = os.path.join(ROOT, "Perfect_Answers", "09_Verified_Tally.md")
PA = os.path.join(ROOT, "Perfect_Answers")

ROW = re.compile(r"^\|\s*(\d+)\s*\|(.*)\|\s*`([^`]+\.md):(\d+)`\s*\|\s*$")
PQ = re.compile(r"(P\dR?)\s*Q(\d)\(([a-g])\)")


def resolve(f):
    for base in ("", "External_Exemplars"):
        p = os.path.join(PA, base, f)
        if os.path.exists(p):
            return p, (f if base == "" else f"{base}/{f}")
    return None, f


def heading_line(lines, qn, ql):
    """the line of the exemplar heading for that question"""
    pat = re.compile(rf"^#+.*\bQ\s*{qn}\s*\(\s*{ql}\s*\)", re.I)
    hits = [i + 1 for i, ln in enumerate(lines) if pat.match(ln)]
    if not hits:
        pat2 = re.compile(rf"^#+.*Q\s*{qn}\({ql}\)", re.I)
        hits = [i + 1 for i, ln in enumerate(lines) if pat2.search(ln)]
    return hits


def main():
    write = "--write" in sys.argv
    text = open(TALLY, encoding="utf-8").read()
    out, changed, unresolved = [], 0, []
    for line in text.split("\n"):
        m = ROW.match(line)
        if not m:
            out.append(line)
            continue
        qm = PQ.search(m.group(2))
        if not qm:
            out.append(line)
            continue
        paper, qn, ql = qm.group(1), qm.group(2), qm.group(3)
        path, shown = resolve(m.group(3))
        if not path:
            out.append(line)
            continue
        lines = open(path, encoding="utf-8", errors="replace").read().split("\n")
        old = int(m.group(4))
        # Only touch a citation that has actually drifted. If the cited line already sits
        # inside the section for this question, it is a legitimate pointer to the middle of
        # the analysis, and moving it would lose information.
        heads = [(i + 1, ln) for i, ln in enumerate(lines) if ln.startswith("#")]
        pat = re.compile(rf"\bQ\s*{qn}\s*\(\s*{ql}\s*\)", re.I)
        cur_head = max([h for h, _ in heads if h <= old], default=0)
        if cur_head and pat.search(lines[cur_head - 1]):
            out.append(line)
            continue
        hits = heading_line(lines, qn, ql)
        if not hits:
            unresolved.append(f"{shown} Q{qn}({ql})")
            out.append(line)
            continue
        new = min(hits, key=lambda h: abs(h - old))
        if new != old:
            line = line.replace(f"{m.group(3)}:{old}", f"{shown}:{new}")
            changed += 1
            print(f"  {shown} Q{qn}({ql}): line {old} -> {new}")
        elif shown != m.group(3):
            line = line.replace(f"{m.group(3)}:{old}", f"{shown}:{new}")
        out.append(line)
    if write:
        open(TALLY, "w", encoding="utf-8").write("\n".join(out))
    print(f"\n{changed} citation line(s) re-pointed" + ("" if write else " (dry run)"))
    for u in unresolved:
        print("  no heading found for", u)


if __name__ == "__main__":
    main()
