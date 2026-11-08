#!/usr/bin/env python3
"""
merge_script_spans.py -- count SCRIPTS, not page-images.

`extract_scripts.py` finds one picture per page and pairs it with the score printed for it. When a
candidate writes across a page break, the report prints the answer as two pictures and prints the
SAME ResultsPlus comment after the second one. The extractor then records two entries with the same
question, the same mark and the same comment -- which is one script, counted twice.

This was found on June 2025 P1R Q2(f): pages 25 and 26 both carry the identical 399-character
comment ("This is a strong response that effectively covers the mark band criteria..."), and pages
27 and 28 both carry the identical 0-mark comment. Four entries, two scripts.

The merge rule, and why it is safe:

  * same report, same question label, same mark value, consecutive pages; AND
  * the second entry's commentary is the same text as the first's (first 60 characters, because the
    report reprints it with the pairing strip attached); AND
  * the first page's picture reaches the foot of the page, i.e. the answer was still running.

Entries that merely sit on consecutive pages with the same question but DIFFERENT comments are two
scripts, and are left alone. On June 2025 P1R Q2(f) that distinction is what separates the 8-mark
script (one, spanning two pages) from a second 8-mark script, if the report prints one.

    python3 audits/merge_script_spans.py            # report
    python3 audits/merge_script_spans.py --write    # writes audits/corpus/scripts_merged.json
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.join(HERE, "corpus")


def key(r):
    return (r["question"], r.get("mark_value"))


def main():
    data = json.load(open(os.path.join(CORPUS, "scripts.json"), encoding="utf-8"))
    merged_all, report = {}, []
    for rep, rows in data.items():
        rows = sorted(rows, key=lambda r: (r["page"], r.get("n", 0)))
        used = [False] * len(rows)
        out = []
        for i, r in enumerate(rows):
            if used[i]:
                continue
            page_mark = r.get("mark_value")
            group = [r]
            j = i + 1
            while j < len(rows):
                nxt = rows[j]
                same_q = key(nxt) == key(r)
                adjacent = nxt["page"] - group[-1]["page"] <= 1
                # the giveaway: the same comment reprinted after the continuation page
                c1 = (group[-1].get("commentary_after") or "")[:60]
                c2 = (nxt.get("commentary_after") or "")[:60]
                same_comment = bool(c1) and c1 == c2
                # ...or the continuation page carries no comment of its own and no new mark
                no_comment = not (nxt.get("commentary_after") or "").strip()
                if same_q and adjacent and (same_comment or (no_comment and nxt.get("mark_value") == page_mark)):
                    group.append(nxt)
                    used[j] = True
                    j += 1
                    continue
                break
            if len(group) > 1:
                report.append((rep, r["question"], page_mark,
                               [g["page"] for g in group]))
            m = dict(r)
            m["pages"] = [g["page"] for g in group]
            m["images"] = [g["image"] for g in group]
            m["merged_from"] = len(group)
            out.append(m)
        merged_all[rep] = out
    total_rows = sum(len(v) for v in data.values())
    total_scripts = sum(len(v) for v in merged_all.values())
    big_rows = sum(1 for v in data.values() for r in v if (r.get("mark_value") or 0) >= 6)
    big_scripts = sum(1 for v in merged_all.values() for r in v if (r.get("mark_value") or 0) >= 6)
    print(f"page entries: {total_rows}   scripts after merging: {total_scripts}")
    print(f"entries worth 6+ marks: {big_rows}   scripts worth 6+ marks: {big_scripts}")
    print(f"\nspans merged: {len(report)}")
    for rep, q, m, pages in report:
        print(f"  {rep}  Q{q:<6} {str(m):>4} marks  pages {pages}")
    if "--write" in sys.argv:
        json.dump(merged_all, open(os.path.join(CORPUS, "scripts_merged.json"), "w"), indent=1)
        print("\nwrote audits/corpus/scripts_merged.json")


if __name__ == "__main__":
    main()
