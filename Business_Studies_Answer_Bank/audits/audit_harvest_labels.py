#!/usr/bin/env python3
"""
audit_harvest_labels.py -- do the harvest files' own headings tell the truth?

Every exemplar in Perfect_Answers/ opens with a heading that states the score, e.g.

    ## [VERIFIED CANDIDATE EXEMPLAR] -- **1/2** . Q3(c) ...

Directly under it the file quotes the examiner's comment, which prints the score in
Pearson's own words ("This response scored 1 mark."). Where the two disagree, the
heading is the thing a reader trusts -- so a heading that overstates the score is a
real defect, not a typo. This tool finds those disagreements.

It does NOT judge whether the script is any good; it only compares the label the bank
attached with the score the bank itself quoted from the report.

Usage: python3 audits/audit_harvest_labels.py [--fix-suggestions]
"""
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PA = os.path.join(ROOT, "Perfect_Answers")

BOUND = re.compile(r"^#{2,4} ", re.M)
LABEL = re.compile(r"([0-9]+)\s*/\s*([0-9]+)")
QLINE = re.compile(r"Q(?:uestion)?\s*(\d)\s*\(([a-g])\)")
# the score as printed inside the quoted examiner comment
SCORED = re.compile(
    r"(?:This response scored|scored)\s+(?:Level\s*\d+\s*[\u2013-]\s*)?(\d+)\s*marks?"
    r"|(\d+)\s*marks?\s+awarded"
    r"|Level\s*\d+\s*[\u2013-]\s*(\d+)\s*marks?", re.I)


def sections(path):
    text = open(path, encoding="utf-8", errors="ignore").read()
    heads = list(BOUND.finditer(text))
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        head = text[m.start():text.find("\n", m.start()) if text.find("\n", m.start()) > 0 else len(text)]
        lab = LABEL.search(head)
        if not lab:
            continue
        if "exemplar" not in head.lower():
            continue
        window = text[m.start():m.start() + 400]
        qm = QLINE.search(window)
        qn, ql = (qm.group(1), qm.group(2)) if qm else ("?", "?")
        yield head, int(lab.group(1)), int(lab.group(2)), qn, ql, text[m.end():end]


def main():
    bad = 0
    total = 0
    for path in sorted(glob.glob(os.path.join(PA, "**", "*.md"), recursive=True)):
        for head, num, den, qn, ql, body in sections(path):
            # only look at the comment quoted immediately under the heading
            chunk = body[:2500]
            found = []
            for m in SCORED.finditer(chunk):
                v = next((g for g in m.groups() if g), None)
                if v is not None:
                    found.append(int(v))
            if not found:
                continue
            total += 1
            # the first score quoted under the heading belongs to this script
            if found[0] != num:
                bad += 1
                rel = os.path.relpath(path, ROOT)
                print(f"{rel}\n   heading says {num}/{den}  Q{qn}({ql})  but the quoted comment says {found[0]}")
                print(f"   {head.strip()[:150]}")
    print(f"\n{total} labelled exemplar headings carry a quoted score; {bad} disagree with their own quote")


if __name__ == "__main__":
    main()
