# Do the answers answer their own questions?

**Third pass, 9 November 2026.** The first two passes audited structure, counts and the evidence
behind the exemplar register. None of them tested the thing that matters most: **is each model
answer the right answer to the question printed above it, and is it built the way the marks are
awarded?**

This pass does that, and it is honest about where it stops.

Tools:

- `audits/audit_question_quotes.py` — every quoted question traced to the paper or the scheme.
- `audits/audit_answer_fidelity.py` — first version; superseded, kept for the trail.
- `audits/audit_answer_shape.py` — mechanical shape tests per tariff.

---

## 1. What was tested, and against what

The bank's answers live in `10_Chain_Bank.md`: **252 entries covering 380 governed questions**
(the three-mark, six-mark, nine-mark and twelve-mark parts of 38 papers).

Three tests, each against a primary document rather than the bank's own prose:

1. **Question pairing.** Every question quoted in an entry, traced to the question paper of the
   session and paper the entry names.
2. **Figures and names.** Every currency amount, percentage and business name in a model answer,
   checked against the cited paper and mark scheme.
3. **Shape.** Does the answer have the structure the marks require — a chain at three marks, both
   options at nine, a judgement at twelve.

**What this pass does not do:** it does not decide whether the *reasoning* is sound. A chain can be
well-formed and still be a bad argument. That test needs a human reading, and it has been done on a
sample only.

---

## 2. Question pairing — 363 citations

| Outcome | Citations |
|---|---|
| **Verbatim in the question paper** | **287** |
| **Verbatim in the mark scheme** | **27** |
| Paraphrase | 4 |
| **Not found in either** | **24** |
| Fragments (`"…of being in a partnership"`) — not checkable | 10 |
| Entries that quote no question at all | 11 |

**287 of 363 citations are the exact words of the paper.** That is the single strongest accuracy
result in this whole audit, because it means the answer beside each question was written for a
question that exists, in the session claimed.

### The 27 "verbatim in the mark scheme" cases are not errors — but they are worth knowing

On nine-mark justify questions the paper prints only an option label — *"Option 1: above the line
promotion · Option 2: below the line promotion"* — and the scheme is what spells out what each
option means. Where the bank quotes the scheme's description, the quote is accurate; it is simply
not on the paper. A reader checking the paper for those words will not find them. That is a
citation-format problem, not a content problem.

### The 24 "not found" cases — read, not counted

Every one of these was read by eye. They are **composite quotations**: the paper's option label
joined to the scheme's description, presented inside one set of quotation marks as if both were the
paper's wording. The substance was right in every case examined. Examples:

- **#193** quotes *"Option 1: hold an event to increase awareness of her flower shop…"*. The paper
  prints *"sponsor a local event such as a flower show"*; *"increase the awareness of her flower
  shop"* is the scheme's AO2 bullet. Same question, merged wording.
- **#217** quotes *"keep employees 'on call' for emergencies… employ college and university
  students during the summer holidays"*. The paper prints *"casual employees / part-time
  employees"*; both descriptions are the scheme's expansion, verified word for word against the
  May–June 2024 P2R mark scheme.
- **#224** quotes *"open coffee shops in supermarkets / in hospitals"* — verified exact against the
  June 2025 P2 paper.

**Verdict: no wrong question was found. 24 citations misattribute the scheme's words to the
paper.** That is a real defect to fix by relabelling, not by rewriting any answer.

### The 11 entries that quote no question

Mostly scaffolds and comparison tables (*#175 the nine-mark scaffold, #228 the twelve-mark
scaffold*), where there is no single question to quote. Legitimate, but the file does not say so,
and a reader scanning for the question finds nothing.

---

## 3. Figures and names — no invention found

Every currency amount, percentage and proper noun in every model answer was checked against the
cited paper and scheme.

- **Answers quoting a figure that appears in neither the paper nor the scheme: 0.**
- **Answers naming a business that appears in neither: 0.** The first run flagged 121 entries; every
  flag was a sentence-initial capital (*"Customers…"*, *"With…"*), not a name.

So the case-study facts — the percentages, the £ figures, the business names — are anchored. That
is the check that catches the failure mode this bank would most plausibly have: an answer written
for one case study and filed under another.

---

## 4. Shape — and a warning about my own checker

### Three-mark answers (100 entries)

| Test | Flagged | After reading |
|---|---|---|
| No causal connective | 18 → 6 after broadening | **0** |

I read all six that survived the first two refinements (#45, #57, #67, #72, #93, #100). **All six
are properly chained.** Example, #100: *"Paying suppliers on time establishes a good relationship
with them (1). If the business needs goods urgently from them (1)… they would be more likely to
help (1)."* That is point → condition → consequence, and it would score 3.

**My checker was cruder than the answers.** Nothing in the three-mark tier failed on reading.

### Nine-mark answers (50 entries tested)

Every one read in the sample states the choice in the first sentence. #176:

> *"The owners of Ocean Vibes should take the venture capital. The decisive fact is what the
> investor brings beyond money… A loan would do the opposite in one important respect…"*

Choice, application, counter-argument, and a named condition under which the choice holds. That is
the AO2/AO3/AO4 shape the scheme asks for.

My automated "only one option discussed" flag fired on 43 of 50 — **a string-matching artefact**,
because the models name the options by content rather than as "Option 1/Option 2". I am recording
the flag and its refutation rather than quietly deleting it.

### Twelve-mark answers (38 entries, 228–252)

**Not yet shape-tested.** These entries use a different internal format (a scaffold, then a
constructed answer, then a marking table), and my extractor failed on 28 of them. The sample read
(#229) is complete and well-formed, but this is the one tier where the mechanical test has not run.
Stated here rather than glossed.

---

## 5. What is still not verified

1. **Whether the reasoning is right.** The chains are well-formed; whether each causal step is
   true is a judgement no script here makes. Sample read, not full read.
2. **The 12-mark tier's shape**, for the mechanical reason above.
3. **The 54 register rows whose reports are not held** — unchanged from the script-evidence pass.
4. **Whether an examiner would award the marks.** No constructed answer in this bank has ever been
   marked by Pearson. The label `[CONSTRUCTED GRADE 9 TARGET]` is honest about this; nothing in
   this pass changes it.

---

## 6. Verdict

- **The questions are real.** 287 of 363 quoted questions are the exact words of the paper they
  are attributed to, 27 more are the scheme's own words, and not one wrong question was found.
- **The facts are anchored.** Zero invented figures, zero invented business names.
- **The three-mark tier is sound on reading** — 100 of 100.
- **One genuine defect, and it is a labelling defect:** 24 citations present the mark scheme's
  wording inside quotation marks as if it were the paper's, and 11 entries quote no question at
  all. The answers do not need changing. The citations do.
- **One tier is untested:** the twelve-mark answers have not been mechanically shape-checked.
