# The extraction template — one script, one folder, no shortcuts

Every script in this bank is a **transcription of handwriting**, and the safest form of it is the
one that can be checked against the scan line by line. This file is the template for that. Nothing
in `transcripts/` is Pearson's text; it is read off the image, and it is labelled that way.

---

## 1. The ladder, applied to one script

The brief asks for the reading to go down in layers, fixing each gap with context. In practice each
layer answers a different question, so all six are used, in this order:

| Layer | Question it answers | Where it comes from |
|---|---|---|
| **L1 · page** | which page of the report holds this script? | the manifest (`audits/corpus/scripts.json`) — page, the picture's position, its size |
| **L2 · section** | which question does it belong to? | the heading in force at that page (start of section → end, not end of section → next question) |
| **L3 · block** | where does the script start and stop, and which paragraph is which? | the drawing's bounding box, then the ruled-line spacing inside it |
| **L4 · line** | what does each line say? | zoom to 2–4×, read line by line, record struck words as struck |
| **L5 · word** | what is that word, when the image will not settle it? | the bank's vocabulary (all 38 schemes + the 14 question papers), then the sentence's own grammar |
| **L6 · intent** | what was the candidate *trying* to say? | the mark scheme's indicative content, the examiner's comment on **this** script, and business doctrine |

**L6 is the only layer that is allowed to add words**, and every word it adds is in `[brackets]`.
Brackets mean *"not visible / not legible; supplied to make the sentence readable"* — never
*"the candidate wrote this"*. Where even L6 cannot settle it, the line is marked `[illegible]` and the
gap is stated rather than filled.

---

## 2. The record for each script

One file per question per report, at
`audits/corpus/transcripts/<report-key>_<question>.md`:

```
# <report> · Q<n>(<x>) · <tariff> marks · printed score <n>
image: audits/corpus/scripts_png/<key>_p<page>_<n>.png
ladder: L1 p<page> / L2 <question> / L3 <paragraphs> / L4 <lines> / L5 <n> words resolved / L6 <n> glossed
status: COMPLETE | PARTIAL (cut at page edge) | UNCERTAIN (<line numbers>)

## Paragraph 1
> [READ FROM SCAN] "<text, with [supplied words] and ~~struck words~~>"

## What could not be read, and why
...

## L6 — what the candidate was trying to say, in plain English
...one sentence per paragraph, every idea traced to a scheme bullet...

## Scheme bullets this answer hits (and the ones it does not)
| bullet | hit? | where in the script |
```

---

## 3. Transcription conventions

1. **`[word]`** — supplied. The image does not show it clearly enough to quote.
2. **`~~word~~`** — struck out by the candidate. Say so; do not tidy it away. Twice now a struck
   word has been the point.
3. **`word[s]`** — the candidate's spelling kept, a letter added in brackets only where the word
   would otherwise be unreadable.
4. **`…`** — the scan stops here (page edge, crop, or a genuinely blank run of lines). Say which.
5. **Line breaks** follow the ruled lines, not the candidate's sentences. A candidate who writes one
   sentence across four ruled lines gets four lines.
6. **No silent correction of grammar or spelling.** The bank's own note — *"Transcriptions are
   faithful to the candidate's handwriting, including spelling and punctuation errors"* — is the
   standard, and it is only true if the errors are visible.

---

## 4. How the layers were built into the tools

| Tool | Layer | What it does |
|---|---|---|
| `audits/extract_scripts.py` | L1–L3 | walks every page, cuts at headings, finds each script picture, renders it at 2×, and pairs it with the mark printed for it — including the pages where the score sits above the picture, or on the next page |
| `audits/script_images.py` | L3–L4 | renders one question's pictures and prints the commentary beside them, for reading by eye |
| `audits/reconstruct_scripts.py` | L4–L5 | the word layer: flags tokens outside the subject vocabulary and glosses them |
| `audits/ocr_scripts.py` | — | kept only as a record that OCR fails on cursive; do not use it on these scans |

The manifest is the index: 457 script images across 14 reports, each with its page, question,
rendered file, printed mark and the commentary that follows it.
