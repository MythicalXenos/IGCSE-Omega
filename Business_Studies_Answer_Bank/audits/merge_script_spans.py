#!/usr/bin/env python3
"""
merge_script_spans.py -- count SCRIPTS, not page-images.

`extract_scripts.py` finds one picture per page-image. A candidate who writes across a page break
gets two pictures, so the manifest holds two entries but the report prints one comment and one
score. Counting entries therefore over-counts scripts -- and it over-counted exactly where the bank
cares most: "73 scripts worth 6+ marks" was 52.

The extractor now walks the report as a stream -- pictures, then the comment that closes them --
and records the span on the first entry of each script (`"span": [[page, n], ...]`) with
`"continuation": true` on the rest. This tool simply reads that: it is the manifest's own account
of which pictures were one answer.

Where no span was recorded, the older evidence still applies and is kept as a fallback: two
consecutive entries with the same question and the same reprinted comment are one script.

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
        out = []
        for r in rows:
            if r.get("continuation"):
                continue                      # part of the script above it
            m = dict(r)
            pages = r.get("span") or [[r["page"], r.get("n", 1)]]
            m["pages"] = [p for p, _ in pages]
            m["images"] = [r["image"]]
            m["merged_from"] = len(pages)
            out.append(m)
            if len(pages) > 1:
                report.append((rep, r["question"], r.get("mark_value"), m["pages"]))
        # fallback for anything the walk could not span: the same comment reprinted
        i = 0
        while i < len(out) - 1:
            a, b = out[i], out[i + 1]
            c1 = (a.get("commentary_after") or "")[:60]
            c2 = (b.get("commentary_after") or "")[:60]
            if (c1 and c1 == c2 and a["question"] == b["question"]
                    and a.get("mark_value") == b.get("mark_value")
                    and b["page"] - a["pages"][-1] <= 1):
                a["pages"] += b["pages"]
                a["merged_from"] += b["merged_from"]
                a["images"] += b["images"]
                report.append((rep, a["question"], a.get("mark_value"), a["pages"]))
                out.pop(i + 1)
                continue
            i += 1
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
