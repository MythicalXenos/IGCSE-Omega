#!/usr/bin/env python3
"""Shared parser: every mark scheme into question -> AO split + AO bullets."""
import os, re, zipfile, collections

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ZIP = os.path.join(ROOT, "Paperlords_Archive", "Paperlords_Searchable_Text_Index.zip")

QHEAD = re.compile(r"(?m)^[ \t]*(\d)[ \t]*\(([a-g])\)(?![a-z])")
AO = re.compile(r"A\s?[O0]\s?([1-4])\s*[-–=:]\s*(\d+)\s*marks?", re.I)
BULLET = re.compile(r"^\s*[\u2022\u00b7\u25cf\*]\s*(.+)$")


def sessions():
    z = zipfile.ZipFile(ZIP)
    out = []
    for n in z.namelist():
        m = re.search(r"4BS1_Business_Studies_(.+?)_(P\dR?)_MS\.txt$", n)
        if m:
            out.append((m.group(1), m.group(2), n))
    return sorted(out), z


def parse_ms(text):
    """question -> dict(ao={1:n,...}, bullets=[(ao, text)])"""
    lines = text.split("\n")
    marks = [(i, m.group(1) + "(" + m.group(2) + ")") for i, l in enumerate(lines)
             for m in [QHEAD.match(l)] if m]
    out = {}
    for k, (i, q) in enumerate(marks):
        end = marks[k + 1][0] if k + 1 < len(marks) else len(lines)
        block = lines[i:end]
        ao = {int(a): int(b) for a, b in AO.findall("\n".join(block))}
        bullets = []
        cur = None
        for l in block:
            m = AO.search(l)
            if m and len(l.strip()) < 90:
                cur = int(m.group(1))
                continue
            b = BULLET.match(l)
            if b and len(b.group(1).split()) > 3:
                bullets.append((cur, b.group(1).strip()))
        out.setdefault(q, {"ao": ao, "bullets": bullets})
    return out


def load_all():
    ss, z = sessions()
    data = {}
    for s, p, n in ss:
        data[(s, p)] = parse_ms(z.read(n).decode("utf-8", "ignore"))
    return data


if __name__ == "__main__":
    d = load_all()
    tot = 0
    noao = 0
    for (s, p), qs in sorted(d.items()):
        for q, v in qs.items():
            tot += 1
            if not v["ao"] and q[0] in "1234" and int(q[0]) * 0 == 0:
                pass
        miss = [q for q, v in qs.items() if not v["ao"] and int(q[0]) >= 2]
        if miss:
            print(f"{s} {p}: no AO split parsed for {miss}")
    print(f"\npapers {len(d)}  questions {tot}")
    print("AO splits found:", sum(1 for qs in d.values() for v in qs.values() if v["ao"]))
