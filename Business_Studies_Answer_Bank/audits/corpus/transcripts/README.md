# Transcripts — handwriting read off the examiner reports

Every file here is **a transcription of a scanned script**, not Pearson's text. The convention is in
`audits/QUOTE_TEMPLATE.md`; the method is in `audits/SCRIPT_RECONSTRUCTION.md`.

Three rules, and they are not negotiable:

1. **`[bracketed]` words are supplied**, not written by the candidate. Where a word was supplied from
   context, the file says which layer supplied it and why.
2. **`~~struck~~` words were struck out by the candidate** and are shown, because twice now a struck
   word has been the point of the answer.
3. **`…` means the scan stops here** — page edge, crop, or printed rule across the writing. The file
   says which. A transcript is never completed by guessing past a cut.

## What is transcribed

| File | Report | Question | Score |
|---|---|---|---|
| `4BS1_01R_2206_1g.md` | Jun 2022 P1R (Can Culleretes) | 1(g) | 6/6 |
| `4BS1_01R_2206_2c.md` | Jun 2022 P1R | 2(c) | 3/3 |
| `4BS1_01R_2206_2e.md` | Jun 2022 P1R | 2(e) | 3/3 |
| `4BS1_01R_2206_2f.md` | Jun 2022 P1R | 2(f) | 9/9 |
| `4BS1_01R_2206_3d.md` | Jun 2022 P1R | 3(d) | 6/6 |
| `4BS1_01R_2206_3e.md` | Jun 2022 P1R | 3(e) | 9/9 |
| `4BS1_01R_2206_4b.md` | Jun 2022 P1R | 4(b) | 6/6 |
| `4BS1_01R_2206_4c.md` | Jun 2022 P1R | 4(c) | 12/12 |
| `4BS1_01_2206_4c.md` | Jun 2022 P1 (TBTS) | 4(c) | 12/12 |
| `4BS1_01R_2506_2f_8.md` | Jun 2025 P1R (China Cycle Tours) | 2(f) | 8/9 |
| `4BS1_01R_2506_2f_0.md` | Jun 2025 P1R | 2(f) | **0/9** |
| `4BS1_01R_2506_3d.md` | Jun 2025 P1R (China Cycle Tours) | 3(d) | 6/6 |
| `4BS1_01R_2506_3e.md` | Jun 2025 P1R | 3(e) | 9/9 |
| `4BS1_01R_2506_4c.md` | Jun 2025 P1R | 4(c) | 11/12 |
| `4BS1_01R_2506_4c_10.md` | Jun 2025 P1R | 4(c) | 10/12 |

**Fourteen scripts across three reports.** The first eight are June 2022 P1R, every level-based question
on the paper; `4BS1_01_2206_4c.md` is June 2022 **P1** Q4(c), transcribed 12 Nov 2026 from pages 37–38
of the full report; the last five are June 2025 P1R, where the report prints **two scripts on Q2(f)** — 8 and
**0** — and **two on Q4(c)** — 10 and 11. Each pair is held constant except one variable: on Q2(f) it
is whether the answer treats the option as a *measure*; on Q4(c) it is whether the judgement is
conditional. The remaining quotes that were read from scans
across the other 13 reports are listed in `audits/corpus/quotes_not_in_textlayer.json` and are the
next batch.

## Checking

```
python3 audits/audit_transcripts.py --all
```

It re-reads every examiner quote in every file here and fails if a fragment is not found, character for
character, in the report text. **16/16 pass.**
