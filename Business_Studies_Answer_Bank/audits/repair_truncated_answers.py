#!/usr/bin/env python3
"""
repair_truncated_answers.py -- finish answer sentences the mark-scheme column cut in half.

The By_Paper files were built from a text index of the mark schemes, and that index drops the tail
of a sentence whenever it crosses the column edge. The result reads:

    plus 1 further mark for linking it to the context of the

The PDF has the rest ("...question."). This finds the cut by its last six words in the real
mark-scheme PDF and appends what follows, up to the end of that sentence.

Guarded: the cut phrase must occur exactly once in the paper's mark scheme, and the replaced line
must be the LAST line of the item's answer. Anything ambiguous is reported and left alone.

    python3 audits/repair_truncated_answers.py           # report
    python3 audits/repair_truncated_answers.py --write
"""
import os
import re
import sys

import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BY_PAPER = os.path.join(ROOT, "Perfect_Answers", "By_Paper")
ARCHIVE = os.path.join(os.path.dirname(ROOT), "Paperlords_Archive", "IGCSE", "4BS1_Business_Studies")
HEAD = re.compile(r"^### `")
CUT_END = re.compile(r"\b(the|of|to|and|a|an|in|for|with|that|which|is|are|on|as|by|or|at|from|its|their)\s*$", re.I)
# sentences that simply stop at a number -- "...will get a maximum of 1" (mark)
CUT_NUM = re.compile(r"(maximum of \d|\b\d)\s*$")


def ms_text(pid):
    m = re.match(r"4BS1_(.+?)_(P\d\s?R?)$", pid)
    if not m:
        return None
    for pat in (f"4BS1_Business_Studies_{m.group(1)}_{m.group(2)}_MS.pdf",):
        p = os.path.join(ARCHIVE, m.group(1), pat)
        if os.path.exists(p):
            doc = pymupdf.open(p)
            t = "\n".join(pg.get_text() for pg in doc)
            return re.sub(r"[ \t]+", " ", t)
    return None


def append(line, text):
    """append `text` to `line`, keeping markdown emphasis and the space between words"""
    star = line.rstrip().endswith("*")
    core = line.rstrip()[:-1].rstrip() if star else line.rstrip()
    out = core + " " + text.strip()
    return out + ("*" if star else "")


def extend(full, tail):
    """the words after `tail` up to the end of its sentence"""
    hay = re.sub(r"\s+", " ", full)
    needle = re.sub(r"\s+", " ", tail).strip()
    hits = [m.start() for m in re.finditer(re.escape(needle), hay)]
    if len(hits) != 1:
        return None
    rest = hay[hits[0] + len(needle):]
    if re.match(r"\s*\(1\)|\s*Question Number", rest):
        return ""          # the column ended here; nothing was lost but whitespace
    # the scheme's own row marker: "(1) Question Number ..." ends the cell, full stop or not
    cut = len(rest)
    for pat in (r"\(\d\)\s*(?=Question Number|$)", r"Question Number"):
        m2 = re.search(pat, rest)
        if m2:
            cut = min(cut, m2.start())
    rest = rest[:cut]
    stop = re.search(r"[.!?](?=\s|$)", rest)
    if stop:
        return rest[: stop.start() + 1].strip()
    frag = rest.strip().rstrip("(0123456789) ").strip()
    return frag if len(frag.split()) >= 2 else None


def main():
    write = "--write" in sys.argv
    cache, fixed, skipped = {}, 0, []
    for name in sorted(os.listdir(BY_PAPER)):
        if not name.endswith(".md"):
            continue
        pid = name[:-3]
        path = os.path.join(BY_PAPER, name)
        lines = open(path, encoding="utf-8").read().split("\n")
        changed = False
        for i, line in enumerate(lines):
            s = line.strip()
            if not s or s.startswith(("**", ">", "#", "|", "AO", "+", "-", "·", "`")):
                continue
            nxt = next((l for l in lines[i + 1:] if l.strip()), "")
            if nxt.startswith(("###", "**")):
                body = s.strip("*").rstrip()
            else:
                continue
            if not (CUT_END.search(body) or CUT_NUM.search(body)):
                continue
            if len(body.split()) < 4:
                continue
            if re.search(r"(maximum of|will get|get a maximum of)\s+\d$", body):
                # the column cut the word "mark" -- the only thing missing is that word
                lines[i] = append(line, "mark")
                changed = True
                fixed += 1
                print(f"  {pid}: ...{body[-30:]!r} +' mark'")
                continue
            if pid not in cache:
                cache[pid] = ms_text(pid)
            if not cache[pid]:
                skipped.append((pid, body[-50:], "no mark scheme PDF"))
                continue
            tail = " ".join(body.split()[-6:])
            more = extend(cache[pid], tail)
            if more == "":
                continue
            if not more or len(more) > 220:
                skipped.append((pid, tail, "phrase not unique / no end"))
                continue
            lines[i] = append(line, more)
            changed = True
            fixed += 1
            print(f"  {pid}: ...{tail} +{more[:60]!r}")
        if changed and write:
            open(path, "w", encoding="utf-8").write("\n".join(lines))
    print(f"\n{fixed} truncated answer(s) completed" + ("" if write else " (dry run)"))
    for pid, tail, why in skipped[:15]:
        print(f"  left alone {pid}: {tail!r} -- {why}")


if __name__ == "__main__":
    main()
