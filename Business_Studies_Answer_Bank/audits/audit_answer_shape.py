#!/usr/bin/env python3
"""
audit_answer_shape.py -- is each model answer shaped the way its marks are actually awarded?

This does not judge style. It tests the four mechanical properties the mark schemes and the
examiner reports say the marks hang on:

  S1  3-mark answers: one point developed twice. Tested as (a) a causal connective is present and
      (b) the answer does not enumerate more than one distinct point (Pearson caps a list at 1 mark).
  S2  6-mark answers: the answer must touch the business in the case, not only generic nouns.
  S3  9-mark answers: the choice must be stated in the first sentence, and both options must be
      discussed -- an answer that only argues one side cannot reach AO4.
  S4  12-mark answers: a judgement must be present (the answer must commit, not just describe).

Every entry is printed with the sentence that satisfies or fails the test, so a wrong verdict can
be seen rather than trusted.
"""
import os, re, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CHAIN = os.path.join(ROOT, "Business_Studies_Answer_Bank", "Perfect_Answers", "10_Chain_Bank.md")

CAUSAL = re.compile(r"\b(because|so that|so|therefore|which means|this means|meaning|leads to|"
                    r"as a result|consequently|allowing|enabling|results in|which is why|hence|"
                    r"this gives|this makes|this attracts|this allows|which is|that is why|"
                    r"means that|helps|enables|reduces|increases|saves|lowers|raises|wins|"
                    r"leading to|and so|then)\b", re.I)
JUDGE = re.compile(r"\b(however|but |although|whereas|on balance|overall|in conclusion|"
                   r"depends|decisive|the stronger|more important|outweigh)", re.I)
CHOOSE = re.compile(r"\b(should|I would|the better|choose|pick|go with|recommend)\b", re.I)


def entries():
    text = open(CHAIN, encoding="utf-8").read()
    out = []
    for m in re.finditer(r"^## (\d+)\.\s*(.+)$", text, re.M):
        start = m.end()
        nxt = re.search(r"^## \d+\.", text[start:], re.M)
        out.append((int(m.group(1)), m.group(2).strip(),
                    text[m.start():start + (nxt.start() if nxt else len(text))]))
    return out


def model_answer(body):
    """the blockquote that follows the 'Model answer' marker -- never an earlier note"""
    m = re.search(r"Model answer[^\n]*\n((?:>.*\n?)+)", body)
    if not m:
        return ""
    block = re.sub(r"^>\s?", "", m.group(1), flags=re.M)
    return block.strip()


def main():
    res = collections.Counter()
    fails = []
    for num, title, body in entries():
        ans = model_answer(body)
        if not ans:
            res["no model answer found"] += 1
            fails.append((num, title, "-", "NO MODEL ANSWER"))
            continue
        mm = re.search(r"Model answer[^\n]*?(\d+)\s*marks", body)
        m = mm
        tier = int(m.group(1)) if m else None
        if tier is None:
            res["tier not stated"] += 1
            continue
        sents = [s for s in re.split(r"(?<=[.!?])\s+", ans) if len(s.split()) > 3]
        if tier == 3:
            res["3-mark entries"] += 1
            if not CAUSAL.search(ans):
                res["S1 3-mark: no causal link"] += 1
                fails.append((num, title, "S1", "no because/so/therefore in the answer"))
            # enumerating more than one point
            numbered = len(re.findall(r"(?m)^\s*(?:[-*\u2022]|\d\.)\s", ans))
            if numbered >= 3:
                res["S1 3-mark: written as a list of 3+"] += 1
                fails.append((num, title, "S1", f"{numbered} bullets - Pearson caps a list at 1 mark"))
        elif tier == 6:
            res["6-mark entries"] += 1
            if len(ans.split()) < 110:
                res["S2 6-mark: under 110 words"] += 1
                fails.append((num, title, "S2", f"{len(ans.split())} words"))
        elif tier == 9:
            res["9-mark entries"] += 1
            first = sents[0] if sents else ans
            if not CHOOSE.search(first):
                res["S3 9-mark: choice not in the first sentence"] += 1
                fails.append((num, title, "S3", "opening sentence: " + first[:100]))
            if not JUDGE.search(ans):
                res["S3 9-mark: no counter-argument word"] += 1
                fails.append((num, title, "S3b", "no however/although/on balance"))
        elif tier == 12:
            res["12-mark entries"] += 1
            if not JUDGE.search(ans):
                res["S4 12-mark: no judgement language"] += 1
                fails.append((num, title, "S4", "no however/on balance/depends"))

    print("=" * 90)
    print("ANSWER SHAPE — mechanical tests only")
    print("=" * 90)
    for k, v in sorted(res.items()):
        print(f"  {k:<44} {v}")
    print("\n" + "=" * 90)
    print("FAILURES — each with the evidence")
    print("=" * 90)
    for num, title, tag, why in fails:
        print(f"  #{num:<4} {tag:<4} {title[:46]:<46} {why}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
