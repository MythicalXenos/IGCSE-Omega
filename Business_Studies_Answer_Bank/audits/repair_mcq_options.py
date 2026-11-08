#!/usr/bin/env python3
"""
repair_mcq_options.py -- put the four options back into every multiple-choice item.

The mark scheme prints "The only correct answer is C" and nothing else. The By_Paper files copied
that sentence, so 180 one-mark items said "C" to a reader who had never been shown A, B or D. The
question paper prints them; `qp_stems.py` now reads them.

This inserts one line under `**Question:**`:

    **Options:** A · Personal savings · B · Retained profit · C · Bank loan · D · Selling assets

and states the credited option in words next to the letter, because the letter alone is what the
scheme gives and the words are what the reader needs.

Guarded by the tariff: only 1-mark items are touched, and only if the paper's stem for that key
carries exactly four options. Nothing is inserted where the file already has an options line.

    python3 audits/repair_mcq_options.py            # report
    python3 audits/repair_mcq_options.py --write
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import qp_stems  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BY_PAPER = os.path.join(ROOT, "Perfect_Answers", "By_Paper")

HEAD = re.compile(r"^### `([^`]+)` — (\d+) marks?")
ANSWER = re.compile(r"The only correct answer is\s*([A-D])")


def main():
    write = "--write" in sys.argv
    total = added = mismatched = 0
    for name in sorted(os.listdir(BY_PAPER)):
        if not name.endswith(".md"):
            continue
        pid = name[:-3]
        stems = qp_stems.stems_for(pid) or {}
        path = os.path.join(BY_PAPER, name)
        lines = open(path, encoding="utf-8").read().split("\n")
        out, i, changed = [], 0, 0
        while i < len(lines):
            line = lines[i]
            out.append(line)
            hm = HEAD.match(line)
            if not hm or hm.group(2) != "1":
                i += 1
                continue
            key = hm.group(1)
            # the block runs to the next heading
            j = i + 1
            while j < len(lines) and not lines[j].startswith("### "):
                j += 1
            block = "\n".join(lines[i + 1:j])
            total += 1
            i += 1
            if "**Options:**" in block or "Option 1" in block:
                continue
            opts = stems.get(key, {}).get("options") or []
            if len(opts) != 4:
                continue
            am = ANSWER.search(block)
            if not am:
                continue
            letter = am.group(1)
            text = next((o.split(" · ", 1)[1] for o in opts if o.startswith(letter + " ")), None)
            if text is None:
                mismatched += 1
                print(f"  !! {pid} {key}: scheme says {letter}, the paper has no such option")
                continue
            # insert directly under the Question line, or after the heading when there is none
            qline = next((k for k in range(i, j) if lines[k].startswith("**Question:**")), None)
            at = (qline + 1) if qline is not None else i
            assert at > 0
            new = (f"**Options:** " + " · ".join(opts) +
                   f"\n\n**Credited option:** **{letter} · {text}**")
            lines.insert(at, new)
            j += 1
            changed += 1
            added += 1
            i = at + 1
        if changed:
            print(f"  {name}: {changed}")
            if write:
                open(path, "w", encoding="utf-8").write("\n".join(lines))
    print(f"\n{total} one-mark items; {added} given their options"
          + ("" if write else " (dry run)"))
    if mismatched:
        print(f"{mismatched} scheme letters do not appear among the paper's options")


if __name__ == "__main__":
    main()
