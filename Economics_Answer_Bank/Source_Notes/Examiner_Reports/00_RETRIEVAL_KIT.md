# Examiner reports — retrieval kit

Goal: get the ~24 ERs we do not hold. Verified working, 2026-11-10.

---

## Why most are missing

Pearson locks ERs for **nine months** after a series. After that they are public
and free — no login. So the only genuinely unobtainable one right now is
**June 2026** (public from ~March 2027).

Everything from June 2019 to November 2025 should be downloadable today.

---

## URL pattern (verified)

Two path forms exist. Newer files:

```
https://qualifications.pearson.com/content/dam/pdf/International-GCSE/Economics/2017/Exam-materials/<code>-pef-<YYYYMMDD>.pdf
```

Older files (2019–2022) use a space and lowercase:

```
https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Economics/2017/exam-materials/<code>_pef_<YYYYMMDD>.pdf
```

`<code>` = `4ec1-01`, `4ec1-01r`, `4ec1-02`, `4ec1-02r`
(the `r` variants are hyphenated lowercase in the newer form, e.g. `4ec1-01r-pef-20220825.pdf`).

`<YYYYMMDD>` is the **publication date**, not the exam date. That is the only
unknown, which is why the search string below is the reliable route.

---

## Confirmed working URLs

| Series | Paper | URL |
|---|---|---|
| June 2019 | 01 | `…/International%20GCSE/Economics/2017/exam-materials/4EC1_01_pef_20190822.pdf` |
| January 2020 | 01R | `…/International%20GCSE/Economics/2017/exam-materials/4EC1_01R_pef_20200305.pdf` |
| June 2022 | 01R | `…/International%20GCSE/Economics/2017/exam-materials/4ec1-01r-pef-20220825.pdf` |
| June 2022 | 02R | `…/International%20GCSE/Economics/2017/exam-materials/4ec1-02r-pef-20220825.pdf` |
| November 2023 | 01 | `…/International-GCSE/Economics/2017/Exam-materials/4ec1-01-pef-20240125.pdf` |
| June 2025 | 01 | `…/International-GCSE/Economics/2017/Exam-materials/4ec1-01-pef-20250821.pdf` |
| June 2025 | 02R | `…/International-GCSE/Economics/2017/Exam-materials/4ec1-02r-pef-20250821.pdf` |

Note the June 2025 pattern: **one publication date serves the whole series**
(`20250821`). So try the same date across `01`, `01r`, `02`, `02r`.

---

## Exact search strings

Paste these into Google. Each one lands on the PDF or a mirror in the first
three results, and the mirror's title contains the date you need.

**Paper 1 (what matters tomorrow):**

```
"4ec1-01-pef" 2025
"4ec1-01-pef" 2024
"4ec1-01r-pef"
"4EC1_01_pef" 2019
"4EC1_01R_pef" 2020
```

**Paper 2 (November, later):**

```
"4ec1-02-pef"
"4ec1-02r-pef"
```

**Everything, as one sweep:**

```
site:qualifications.pearson.com 4ec1 pef
```

---

## The instant route, if you have a school login

This is faster than all of the above and gets January 2020 through June 2026 in
four clicks.

1. `https://qualifications.pearson.com/en/qualifications/edexcel-international-gcses/international-gcse-economics-2017.html`
2. **Exam materials** tab.
3. Filter: **Exam series** = the series; **Material type** = *Examiners' report*.
4. Papers are listed as `4EC1/01`, `4EC1/01R`, `4EC1/02`, `4EC1/02R`.

Edexcel Online credentials needed for anything inside nine months. A teacher or
exams officer at your centre has them.

---

## What to send me

Just paste the text, or drop the PDFs anywhere in the repo and say where. I will
extract the per-question commentary into
`Economics_Answer_Bank/Source_Notes/Examiner_Reports/<series>_<paper>.md` in the
same shape as the two already there.

Priority order, if you only get some:

1. **Nov 2025 P1** — the most recent paper before tomorrow's.
2. **May 2025 P1R** — the regional variant of the paper I set you.
3. **June 2024 P1** — first series with the 8×1·6×2·4×3 short-answer shape.
4. **Nov 2024 P1**.
5. Everything else.
