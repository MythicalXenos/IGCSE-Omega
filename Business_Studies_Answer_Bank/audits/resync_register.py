#!/usr/bin/env python3
"""
resync_register.py -- move the register's line citations past the scan-read labels.

`audit_quotes_vs_textlayer.py --label/--label-unverified` inserts a one-line label above each
transcribed quote. Every label shifts every citation below it in the same file. The first label
pass moved 96 register rows off their scripts.

THE METHOD, and why it is this one.

Counting the inserted lines is exact ONLY if the register is otherwise unchanged -- and saying so
plainly is the point. Three earlier versions tried to *repair* a citation by searching for a nearby
line that looked right; each one could latch onto a different script with the same question number
in a neighbouring section, and the register went from wrong lines to wrong lines plus wrong papers.

So this tool does not search. It takes the register as it stood before the labels (`--from`, a git
ref, default `1f38eb2`), and for every row adds the number of label lines that now sit above the
old line number. That is arithmetic on a known diff, not a guess about content.

    python3 audits/resync_register.py --check      # show the drift, change nothing
    python3 audits/resync_register.py --write

Run `tally_exemplars.py` afterwards. It must exit 0, and it checks the register against the files
independently -- so a bad resync shows up there, not in a summary line here.
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PA = os.path.join(ROOT, "Perfect_Answers")
TALLY = os.path.join(PA, "09_Verified_Tally.md")
REL = "Business_Studies_Answer_Bank/Perfect_Answers/09_Verified_Tally.md"
ROW = re.compile(r"^\|\s*\d+\s*\|.*\|\s*`([^`]+\.md):(\d+)`\s*\|\s*$")
LABELS = ("read from the printed script image", "not in any text layer held")
DEFAULT_REF = "1f38eb2"


def git_show(ref, path):
    return subprocess.run(["git", "-C", ROOT, "show", f"{ref}:{path}"],
                          capture_output=True, text=True, check=True).stdout


def main():
    ref = DEFAULT_REF
    if "--from" in sys.argv:
        ref = sys.argv[sys.argv.index("--from") + 1]
    base = git_show(ref, REL).split("\n")
    write = "--write" in sys.argv
    out, moved, missing = [], 0, []
    cache = {}
    for line in base:
        m = ROW.match(line)
        if not m:
            out.append(line)
            continue
        f, old = m.group(1), int(m.group(2))
        path = next((c for c in (os.path.join(PA, f), os.path.join(PA, "External_Exemplars", f))
                     if os.path.exists(c)), None)
        if not path:
            missing.append((f, old))
            out.append(line)
            continue
        if path not in cache:
            cache[path] = [i for i, l in enumerate(open(path, encoding="utf-8").read().split("\n"), 1)
                           if any(x in l for x in LABELS)]
        added = sum(1 for i in cache[path] if i <= old)
        if added:
            line = line.replace(f":{old}`", f":{old + added}`")
            moved += 1
        out.append(line)
    if write:
        open(TALLY, "w", encoding="utf-8").write("\n".join(out))
    print(f"{moved} citation(s) moved past {sum(len(v) for v in cache.values())} label line(s)"
          + ("" if write else " (dry run)"))
    for f, o in missing:
        print(f"  !! {f}:{o} file not found")


if __name__ == "__main__":
    main()
