#!/usr/bin/env python3
"""
repair_stems.py -- put the real question back on every By_Paper item.

The "**Question:**" line in Perfect_Answers/By_Paper/ came from the mark scheme's narrow
question column. Three things go wrong there:

  1. the column is cut to its width, so the sentence stops mid-clause
     ("Which one of the following is a task carried out by the");
  2. on some items the column holds the scheme's own header instead of a question
     ("Indicative content", "Answer Additional guidance");
  3. on some items it holds the PREVIOUS part's question, so the stem is attributed to the
     wrong part number.

All three are repaired from Pearson's question paper, which prints the stem in full. The
guard is the tariff: the paper prints the marks after every stem, and a stem is only accepted
when that number equals the marks the By_Paper heading claims. A mismatched tariff means the
extractor has picked up the wrong part, and the item is left alone and logged.

    python3 audits/repair_stems.py --dry-run
    python3 audits/repair_stems.py --write
"""
import difflib
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qp_stems import stems_for  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BY_PAPER = os.path.join(ROOT, "Perfect_Answers", "By_Paper")

JUNK = {"indicative content", "answer additional guidance", "answer mark", "answer",
        "question mark", "additional guidance", "indicative content mark", ""}
ITEM = re.compile(r"^### `([0-9]\([a-z]\)(?:\([ivx]+\))?)` — (\d+) marks?", re.M)
QLINE = re.compile(r"\*\*Question:\*\* (.+)")


def norm(s):
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u2013", "-")
    return re.sub(r"\s+", " ", s).strip().rstrip(".:;,").lower()


def main():
    write = "--write" in sys.argv
    stats = {"replaced": 0, "tariff-kept": 0, "junk-fixed": 0, "truncation-completed": 0,
             "stem-corrected": 0, "kept-same": 0}
    log = []
    for path in sorted(glob.glob(os.path.join(BY_PAPER, "*.md"))):
        name = os.path.basename(path)[:-3]
        stems = stems_for(name)
        text = open(path, encoding="utf-8").read()
        if not stems:
            log.append(f"{name}: NO QUESTION PAPER TEXT -- untouched")
            continue
        out, pos, file_changes = [], 0, 0
        marks = list(ITEM.finditer(text))
        for idx, m in enumerate(marks):
            key, claimed = m.group(1), int(m.group(2))
            block_end = text.find("\n### `", m.end())
            block_end = len(text) if block_end == -1 else block_end
            block = text[m.start():block_end]
            qm = QLINE.search(block)
            rec = stems.get(key)
            if not rec:
                out.append(text[pos:block_end]); pos = block_end
                continue
            if not qm:
                # no question line at all (the scheme prints none for this item): insert one
                if rec["marks"] is not None and rec["marks"] != claimed:
                    stats["tariff-kept"] += 1
                    out.append(text[pos:block_end]); pos = block_end
                    continue
                head_end = text.find("\n", m.end())
                head_end = len(text) if head_end == -1 else head_end
                rep = f"\n\n**Question:** {rec['stem'].strip()}"
                if rec.get("options"):
                    rep += "  \n**Options:** " + " · ".join(rec["options"])
                new_block = text[m.start():head_end] + rep + block[head_end - m.start():]
                out.append(text[pos:m.start()]); out.append(new_block)
                pos = block_end
                stats["inserted"] = stats.get("inserted", 0) + 1
                stats["replaced"] += 1
                file_changes += 1
                log.append(f"{name} {key}: INSERTED (item had no question line)\n"
                           f"    now: {rec['stem'][:120]}")
                continue
            old, new = qm.group(1).strip(), rec["stem"].strip()
            if rec["marks"] is not None and rec["marks"] != claimed:
                stats["tariff-kept"] += 1
                log.append(f"{name} {key}: TARIFF MISMATCH (paper {rec['marks']}, file {claimed}) -- kept\n"
                           f"    old: {old[:100]}\n    new: {new[:100]}")
                out.append(text[pos:block_end]); pos = block_end
                continue
            if norm(new) == norm(old):
                stats["kept-same"] += 1
                out.append(text[pos:block_end]); pos = block_end
                continue
            o, n = norm(old), norm(new)
            if o in JUNK:
                kind = "junk-fixed"
            elif n.startswith(o[:50]) and len(o) > len(n) * 0.6:
                kind = "truncation-completed"
            else:
                kind = "stem-corrected"
            stats[kind] += 1
            stats["replaced"] += 1
            rep = f"**Question:** {new}"
            if rec.get("options"):
                rep += "  \n**Options:** " + " · ".join(rec["options"])
            replaced = block.replace(qm.group(0), rep)
            out.append(text[pos:m.start()]); out.append(replaced)
            pos = block_end
            file_changes += 1
            log.append(f"{name} {key}: {kind.upper()}\n    was: {old[:120]}\n    now: {new[:120]}")
        out.append(text[pos:])
        if write and file_changes:
            open(path, "w", encoding="utf-8").write("".join(out))
    for k, v in stats.items():
        print(f"  {k:<22} {v}")
    with open(os.path.join(ROOT, "audits", "corpus", "stem_repairs.log"), "w", encoding="utf-8") as f:
        f.write("\n".join(log) + "\n")
    print("log: audits/corpus/stem_repairs.log")
    if not write:
        print("\n(dry run -- nothing written; pass --write)")


if __name__ == "__main__":
    main()
