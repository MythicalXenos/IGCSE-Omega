#!/usr/bin/env python3
"""PAPER-LEVEL COVERAGE — can the bank answer a whole paper, part by part?

WHY THIS EXISTS
---------------
The four tier checks (`layer_c_coverage.py`, `layer_c_6mark_coverage.py`,
`layer_c_9mark_coverage.py`, `layer_c_12mark_coverage.py`) each prove their own
tier is covered: every derived block maps to an entry in `10_Chain_Bank.md`.
That is coverage by TIER.

Nobody had asked the question the user actually asks when sitting a paper:
**"I have June 2026 Paper 1R in front of me - is every question on it answered
somewhere in this bank?"** That is coverage by PAPER, and it is a different
assertion. A tier can be 100% covered while a single paper is missing a part,
if one paper's block was folded into another's row of a hand-kept map.

WHAT IT DOES
------------
For all 38 papers, it resolves each GOVERNED part - the 4 x 3-mark, 3 x 6-mark,
2 x 9-mark and 1 x 12-mark, ten per paper, 380 in total - down to the entry
number in `10_Chain_Bank.md` that answers it, and then checks that the entry
exists. It uses the SAME maps the tier checks use (imported, never re-typed),
so this script cannot disagree with them about a block's entry; it only asks a
different question of the same data.

It also checks the things only a per-paper view can see:
  * every paper carries exactly 4 / 3 / 2 / 1 governed parts;
  * no paper repeats a question label (a duplicated row keyed to the wrong paper
    would otherwise resolve happily);
  * the four tier inventories agree on the 38 session/paper keys - a paper
    present in one tier's CSV and absent from another's would leave parts
    unresolved on one side and invisible on the other.

A part that resolves to no entry is reported as UNANSWERED and fails the run.
That is the one outcome this script exists to make impossible to miss.

Run from Business_Studies_Answer_Bank/ (NOT from Perfect_Answers/).
"""
from __future__ import annotations
import collections
import csv
import importlib.util
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
CHAIN = HERE / "Perfect_Answers" / "10_Chain_Bank.md"


def load_map(module_name: str):
    """Import a tier's coverage script for its COVERED map - never re-typed here."""
    spec = importlib.util.spec_from_file_location(module_name, HERE / f"{module_name}.py")
    assert spec and spec.loader, module_name
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.COVERED


def rows(path: pathlib.Path, **cols: str):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return [{k: (r[v] or "").strip() for k, v in cols.items()} for r in csv.DictReader(fh)]


def main() -> int:
    parts = []          # (session, paper, tier, question, entry)
    problems = []

    map3 = load_map("layer_c_coverage")
    map6 = load_map("layer_c_6mark_coverage")
    map9 = load_map("layer_c_9mark_coverage")
    map12 = load_map("layer_c_12mark_coverage")

    # ---- 3-mark: 152 parts -> canonical topic -> entry -------------------
    for r in rows(HERE / "layer_c_3mark_master.csv", session="session", paper="paper",
                  q="question", topic="canonical_topic"):
        parts.append((r["session"], r["paper"], 3, r["q"], map3.get(r["topic"]), r["topic"]))

    # ---- 6-mark and 9-mark: one block per part, keyed by `n` -------------
    for r in rows(HERE / "layer_c_6mark_inventory.csv", session="session", paper="paper", q="question", n="n"):
        parts.append((r["session"], r["paper"], 6, r["q"], map6.get(int(r["n"])), f"block {r['n']}"))
    for r in rows(HERE / "layer_c_9mark_inventory.csv", session="session", paper="paper", q="question", n="n"):
        parts.append((r["session"], r["paper"], 9, r["q"], map9.get(int(r["n"])), f"block {r['n']}"))

    # ---- 12-mark: one block per paper, POSITIONAL (row order = block no.) -
    for i, r in enumerate(rows(HERE / "layer_c_12mark_inventory.csv", session="Session",
                               paper="Paper", q="Part"), 1):
        parts.append((r["session"], r["paper"], 12, r["q"], map12.get(i), f"block {i}"))

    print("=" * 74)
    print("PAPER-LEVEL COVERAGE - every governed part of every paper, down to its entry")
    print("=" * 74)
    print(f"  parts resolved: {len(parts)}   "
          f"(3-mark {sum(1 for p in parts if p[2] == 3)} · 6-mark {sum(1 for p in parts if p[2] == 6)} · "
          f"9-mark {sum(1 for p in parts if p[2] == 9)} · 12-mark {sum(1 for p in parts if p[2] == 12)})")
    if len(parts) != 380:
        problems.append(f"expected 380 governed parts, resolved {len(parts)}")
    if not parts:
        print("  NONE PARSED - check the inventory paths, not the bank.")
        return 1

    # ---- every referenced entry must exist in the chain bank -------------
    headings = {int(m.group(1)) for m in
                re.finditer(r"^##\s+(\d+)\.", CHAIN.read_text(encoding="utf-8"), re.M)}
    print(f"  chain bank entries: {len(headings)}")

    unanswered = [p for p in parts if p[4] is None]
    dangling = sorted({p[4] for p in parts if p[4] is not None and p[4] not in headings})

    # ---- per-paper view --------------------------------------------------
    by_paper = collections.defaultdict(list)
    for p in parts:
        by_paper[(p[0], p[1])].append(p)

    shape = collections.Counter()
    for (session, paper), ps in sorted(by_paper.items()):
        counts = collections.Counter(t for _, _, t, _, _, _ in ps)
        shape[(counts[3], counts[6], counts[9], counts[12])] += 1
        labels = [q for _, _, _, q, _, _ in ps]
        dupes = [q for q, n in collections.Counter(labels).items() if n > 1]
        if dupes:
            problems.append(f"{session} {paper}: question label(s) {dupes} appear more than once")

    entry_nums = [p[4] for p in parts if p[4]]
    print(f"  papers: {len(by_paper)}   distinct entries reached: {len(set(entry_nums))}")
    print(f"  papers per tariff shape: {dict(shape)}   (want one shape: 4/3/2/1)")
    if len(shape) != 1 or (4, 3, 2, 1) not in shape:
        problems.append(f"papers do not all carry the 4/3/2/1 governed shape: {dict(shape)}")

    # ---- agreement between the four inventories --------------------------
    seen = {t: {(p[0], p[1]) for p in parts if p[2] == t} for t in (3, 6, 9, 12)}
    if not (seen[3] == seen[6] == seen[9] == seen[12]):
        for t in (6, 9, 12):
            only = seen[3] ^ seen[t]
            if only:
                problems.append(f"3-mark and {t}-mark inventories disagree on {len(only)} paper key(s): {sorted(only)[:4]}")
    else:
        print(f"  all four inventories agree on the same {len(seen[3])} session/paper keys.")

    # ---- the assertion the script exists for -----------------------------
    print()
    if unanswered:
        print("=" * 74)
        print(f"UNANSWERED PARTS — {len(unanswered)}")
        print("=" * 74)
        for session, paper, tier, q, _e, block in unanswered:
            print(f"  {session} {paper} {q} ({tier} marks) — {block} has no entry in the chain bank")
        problems.extend(f"{s} {p} {q} ({t}) unanswered" for s, p, t, q, _e, _b in unanswered)
    for n in dangling:
        print(f"  DANGLING entry {n} — named by a coverage map but not a heading in 10_Chain_Bank.md")
        problems.append(f"entry {n} dangling")
    if not unanswered and not dangling:
        print(f"  every one of the {len(parts)} governed parts resolves to an entry - "
              f"{len(set(entry_nums))} entries answer {len(parts)} parts.")

    # ---- the newest paper, printed in full so the claim is visible -------
    # NEWEST session in the bank, not the alphabetically last paper: `!=` here
    # would sort every non-2026 paper ABOVE June 2026 and print 2019 as the
    # example. (Caught on the first run, which printed May-June 2019 P2R.)
    newest = max(by_paper, key=lambda k: (k[0] == "June 2026", k[1]))
    print()
    print(f"  WORKED EXAMPLE — {newest[0]} {newest[1]}, every governed part and the entry that answers it")
    for _s, _p, tier, q, entry, block in sorted(by_paper[newest], key=lambda x: (x[2], x[3])):
        print(f"    {tier:>2}-mark  {q:<7} -> entry {entry}   [{block}]")

    print()
    print("RESULT:", "OK — the bank answers every governed part of every paper it holds."
          if not problems else f"FAIL — {len(problems)} problem(s).")
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
