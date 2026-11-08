# Reading a script that will not extract — the layered method, and what it found

**12 November 2026.** This file answers one narrow question: *when the examiner report prints a
candidate's answer as a picture, how do we find out what it actually said?* It records the method,
the four layers that were tried, the one that works, and the two bank defects the working method
exposed.

> ⚠️ **Nothing in this file is a quotation of a candidate.** Where a script has been read off a
> scan, the text is marked **[READ FROM SCAN]** and is *my transcription of handwriting*, not a
> transcript supplied by Pearson. Any claim resting on it is a claim about what the image shows.

---

## 1. Why the text will not come out

Each of the 13 examiner reports holds **52–100 embedded images**, about 2,000 in total. Most are the
scanned script facsimiles. `pymupdf` extracts the *commentary* cleanly — the examiner's words, the
mark, the cohort statistics — and returns **nothing at all** for the handwriting, because there is
no text layer under it.

The four things that were tried, in the order the brief asked for them:

| Layer | What it does | Verdict |
|---|---|---|
| **L1 — whole page** | dump every page of a report to text | works for commentary, **blank where the script is** |
| **L2 — section** | cut the page text at `Question N(x)` headings until the next one | isolates the right commentary, still no script |
| **L3 — sentence** | split that section on full stops | clean, and confirms the mark line (*"3 marks."*) — still no script |
| **L4 — word** | tokenise, bracket every token outside the subject vocabulary | turns *"Grasp"* into `[grasp]`, which is useful for OCR noise — **no help for handwriting** |
| **L5 — gloss** | `difflib` against a 38-scheme vocabulary to guess the intended word | guesses print, not cursive |

**The ladder works downward through the commentary and cannot reach the script**, because the script
is not under the text at all — it is pixels. Layers L1–L5 are implemented in
`audits/reconstruct_scripts.py`; they are worth keeping for the commentary, and they are not the
answer to the question that was asked.

**What is the answer:** render the embedded image to a PNG at 2× and read it. That is
`audits/script_images.py`. It writes the facsimile out and prints the commentary beside it, so each
picture is tied to its mark.

```bash
python3 audits/script_images.py 4BS1_01R_2506 2d     # one question
python3 audits/script_images.py 4BS1_01R_2506        # every question in the report
```

OCR was tried first and does not work on this material. `rapidocr` reads the **printed** question
line perfectly and turns the handwriting beside it into `"AauTasuiffsoulid sekut ena hahctooc on
importhismeans Ceausnasuoudnead bospend Mere.... onimportoragood sasagiesultprojitmargins"`. The
engine is print-trained; the candidates wrote in cursive. Upscaling to 3× and greyscaling gained
words, not meaning. **Do not spend time tuning OCR on these scans — render and read.**

---

## 2. What the images actually say — three worked cases

### Case A. June 2025 P1R Q2(d) — the pair that separates 3 marks from 0

*"Explain one way that the introduction of tariffs might affect a business importing goods."* (3)

**The script credited 3 marks [READ FROM SCAN]:**

> *"[struck] Tariffs would result on a higher tax on imports, this means the business would need to
> spend more on importing goods, as a result, profit margins would decrease."*

**The script credited 0 [READ FROM SCAN]:**

> *"With tariffs, importing goods may be cheaper, allowing this business to import more at a lower
> cost. This could lead to more raw materials or products being sold to customers or other
> businesses. Therefore, ~~[struck]~~ potentially increasing revenue."*

**What this settles.** The zero script is *longer*, *better spelled*, has a *clear chain*, and ends
on a business outcome — and still scores nothing, because it has the **direction of the tariff
backwards**. A tariff is a tax on imports; it makes importing dearer, not cheaper. The 3-mark script
is one causal step (*tax → dearer imports → lower margin*) and one development (*margins fall*). The
examiner's comment on the pair is *"This is a clear way that tariffs can affect a business that is
developed well with interconnected points. 3 marks."* and *"This answer incorrectly addresses the
question. 0 marks."*

**So the rule is not "develop more"** — on this question development was present in the zero script.
**The rule is "get the mechanism's direction right first".** That is worth more than any structure
advice in the bank.

### Case B. June 2025 P2 Q1(g) — the paragraph the text layer drops

*"Analyse the benefits for Starbucks of using batch production."* (6)

The register quoted this 6/6 answer as **one paragraph, "3 sentences, 46 words"**. The scan shows a
**second paragraph** the text layer does not carry:

> **[READ FROM SCAN]** *"Further, batch production is convenient as it helps implement changes to
> ~~the~~ the food produced fast and easily. ~~This is b~~ For example, if Starbucks wants to change
> the flavour of the cake from strawberry to chocolate, they can easily implement this change by
> affecting only a selected number of batches. It saves time and resources spent on the cakes & so
> on."*

The scan is **cut off at the bottom of the page**, mid-sentence — *"cakes & so on."* is the last
legible line — so more may exist than Pearson reproduced. **Two consequences:**

1. **The quote in the bank was truncated without an ellipsis and the word count was wrong.** Fixed
   in `Perfect_Answers/02_Verified_Exemplars.md`, with the correction dated in place.
2. **The finding it supported got stronger, not weaker.** The 6/6 is *two developed advantages*
   (flexibility / no stock piles; fast changeovers / only some batches affected), not one. The
   earlier reading — "one point can get 6" — was built on half the evidence.

### Case C. June 2023 P1R Q2(b) — the heading said 1/1, the script scored 0/1

The register's heading for this entry read **1/1**. The report prints **one** script for the
question and the examiner awards it **0**. Reading the scan was not needed to catch this — the
commentary says *"no context no marks can be gained"* — but the mismatch only surfaced once the
score check was run against every row. **Corrected to 0/1**, dated, in place.

---

## 3. What the layered check changed, in numbers

| | Before 9 Nov | After 12 Nov |
|---|---|---|
| Register rows traced to a printed score | 82 | **141 of 148** |
| Mark mismatches | 13 | **0** |
| Rows still uncheckable | 54 | **6** (one missing PDF: June 2022 P1R) |
| Rows where the report prints nothing | 1 | 1 (June 2019 P2 1(f) — the booklet is silent) |

The three mismatches that survived the first pass were **my checker's fault, not the bank's**:

- it read a **stale inventory** built before singular *"1 mark"* and word-numbers were handled;
- it read the **section tier** instead of the row, so rows already annotated **(0/1)** were scored
  as if they claimed full marks;
- a loop variable **overwrote the question number** in the booklet branch.

That is the same lesson as the earlier false alarms: **a checker that flags correct material is
broken, and the material has to be read by eye before it is called wrong.**

---

## 4. What is still only in pixels

These are the places where a bank claim rests on a scan and nothing else, so they carry the most
residual risk:

| Where | Why it matters |
|---|---|
| Every 6-, 9- and 12-mark exemplar from 2023–2026 | long handwritten answers, quoted in the bank from the text layer where it exists — the Starbucks case proves the text layer can be **partial** |
| The June 2019 booklet exemplars | scans of a booklet, not a report |
| The June 2024 P2R (Jimmy Choo) scripts | read live, never stored; only the marks are recorded |

**Next step, if the accuracy pass continues:** run `script_images.py` over every 6/9/12-mark
exemplar in the register and compare the image with the quoted text, the way Case B was done. That is
the only remaining class of defect this method has found.

---

## 5. Rules for using anything in this file

1. **Never quote a scan-read line as the candidate's words.** Label it *read from scan*. Cursive `s`
   and `r`, `a` and `o`, and crossed-out words are all guessable and all capable of changing a mark.
2. **The mark line is the anchor.** Read the examiner's comment first; it tells you what the script
   was paid for. Then read the image to see how.
3. **A struck-out word is evidence, not noise.** Twice now (Case B, and the 1/1 fringe-benefit script
   in the 2023 P1R file) a candidate rewrote mid-sentence and the examiner paid the rewrite. Say so
   rather than tidying it out of the quote.
4. **If the scan is cut off, say it is cut off.** Do not close the sentence.

---

*Tools: `audits/script_images.py` (render + read), `audits/reconstruct_scripts.py` (the L1–L5
ladder, for commentary), `audits/ocr_scripts.py` (OCR, kept only to show it does not work here).
Images land in `audits/corpus/scripts_png/`; OCR dumps in `audits/corpus/ocr/`.*
