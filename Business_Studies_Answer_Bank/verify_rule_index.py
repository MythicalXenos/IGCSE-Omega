#!/usr/bin/env python3
"""Check the rule index: every rule defined once, and every citation resolves.

WHY THIS EXISTS
---------------
The bank cites rules by number in nearly every file -- "rule 74", "rule 91",
"rule 118" -- and the rule number is the only handle a reader has on a long piece
of examiner evidence. A number that is cited but never defined, defined twice, or
reused for something else sends the reader to the wrong rule with no sign that
anything is wrong.

Two things make that a live risk here:

  * the rules are split across TWO files by design -- `01_Mark_Tariff_Playbook.md`
    carries the tariff rules and `06_External_Source_Library.md` the rest -- so
    "the rules are all in 06_" is false and a reader looking for rule 50 in 06_
    has been told the wrong thing;
  * `10_Chain_Bank.md` numbers its 252 entries with the SAME `## N. Title`
    heading format as the rules. The two numbering domains look identical in a
    grep, which is exactly how a duplicate rule number would hide.

RUN FROM `Business_Studies_Answer_Bank/`. Prints one RESULT.

  python3 verify_rule_index.py
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
PA = HERE / "Perfect_Answers"
RULE_FILES = ("01_Mark_Tariff_Playbook.md", "06_External_Source_Library.md")

# The split this bank documents: tariff rules in 01_, the rest in 06_.
EXPECTED_01 = {41, 42} | set(range(49, 64))          # 41,42,49-63  = 17
TOP_RULE = 125

HEADING = re.compile(r"^#{2,4}\s+(\d{1,3})\.\s+\S")
CITE = re.compile(r"\b[Rr]ule[s]?\s+(\d{1,3})\b")


def main() -> int:
    problems = []
    defined: dict[int, list[str]] = {}

    for name in RULE_FILES:
        path = PA / name
        if not path.exists():
            print(f"!! missing rule file {name}")
            return 1
        for i, line in enumerate(path.read_text(encoding="utf-8").split("\n"), 1):
            m = HEADING.match(line)
            if m:
                defined.setdefault(int(m.group(1)), []).append(f"{name}:{i}")

    print("=" * 74)
    print("RULE DEFINITIONS")
    print("=" * 74)
    print(f"  rule headings in {RULE_FILES[0]} + {RULE_FILES[1]}: "
          f"{sum(len(v) for v in defined.values())}")
    print(f"  distinct rule numbers: {len(defined)}")

    dupes = {n: v for n, v in defined.items() if len(v) > 1}
    for n, v in sorted(dupes.items()):
        problems.append(f"rule {n} is defined {len(v)} times: {v}")
        print(f"  FAIL rule {n} defined {len(v)}x  {v}")

    missing = [n for n in range(1, TOP_RULE + 1) if n not in defined]
    if missing:
        problems.append(f"rule numbers with no definition: {missing}")
        print(f"  FAIL no definition for: {missing}")

    beyond = sorted(n for n in defined if n > TOP_RULE)
    if beyond:
        problems.append(f"rule numbers above the documented maximum {TOP_RULE}: {beyond}")
        print(f"  NOTE rule numbers above {TOP_RULE}: {beyond} — the index needs a new entry")

    got_01 = {n for n, v in defined.items() if all(s.startswith(RULE_FILES[0]) for s in v)}
    if got_01 != EXPECTED_01:
        problems.append(f"the 01_/06_ split moved: 01_ now defines {sorted(got_01)}, "
                        f"the bank documents {sorted(EXPECTED_01)}")
        print(f"  FAIL 01_ defines {sorted(got_01)}")
    print(f"  {RULE_FILES[0]} defines: {len(got_01)} rules  {sorted(got_01)[:4]} … {sorted(got_01)[-3:]}")
    print(f"  {RULE_FILES[1]} defines the other {len(defined) - len(got_01)}")
    if not dupes and not missing:
        print(f"  every rule number 1–{TOP_RULE} is defined exactly once.")

    # ---- citations, across every markdown file in the bank -------------------
    print()
    print("=" * 74)
    print("CITATIONS — does every 'rule N' a file quotes actually exist?")
    print("=" * 74)
    cited: dict[int, set[str]] = {}
    files = sorted(PA.rglob("*.md"))
    for f in files:
        for m in CITE.finditer(f.read_text(encoding="utf-8", errors="replace")):
            cited.setdefault(int(m.group(1)), set()).add(f.name)
    dangling = sorted(n for n in cited if n not in defined and n > TOP_RULE)
    print(f"  files scanned: {len(files)}")
    print(f"  distinct rule numbers cited: {len(cited)}")
    if dangling:
        for n in dangling:
            problems.append(f"rule {n} is cited in {sorted(cited[n])} but never defined")
            print(f"  FAIL rule {n} cited in {sorted(cited[n])} — no such rule")
    if not cited:
        print("  NONE PARSED — check the parser, not the bank.")
        problems.append("no rule citation parsed")
    if cited and not dangling:
        print("  every citation resolves to a rule that exists.")

    print()
    print("=" * 74)
    for pr in problems:
        print(f"  !! {pr}")
    print("RESULT:", "OK — the rule index is complete, unambiguous, and every "
                     f"citation in the bank resolves." if not problems
          else f"FAIL — {len(problems)} problem(s).")
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
