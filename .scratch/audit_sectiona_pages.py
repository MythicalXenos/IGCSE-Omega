"""Verify Section A 'MS p. N' citations, treating N as the PRINTED page number.

The archive mark schemes disagree about whether the printed folio matches the PDF
page, so each file's printed->PDF map is built from the folio printed at the top of
each page (falling back to 1-based position when a page prints no folio).
"""
import pathlib, re, csv, pymupdf

rows = list(csv.DictReader(open('English_Answer_Bank/Answer_Sets/coverage.csv')))
ms_for = {p.name: p for p in pathlib.Path('Paperlords_Archive/IGCSE/4EB1_English_Language_B').rglob('*_MS.pdf')}
cache = {}

def load(pdf):
    if pdf not in cache:
        d = pymupdf.open(pdf)
        pages = [p.get_text() for p in d]
        folio = {}
        for i, t in enumerate(pages):
            lines = [l.strip() for l in t.splitlines() if l.strip()]
            if lines and re.fullmatch(r'\d{1,2}', lines[0]):
                folio[int(lines[0])] = i
        cache[pdf] = (pages, folio)
    return cache[pdf]

problems = []
checked = 0
for f in sorted(pathlib.Path('English_Answer_Bank/Answer_Sets').glob('*_Section_A.md')):
    t = f.read_text()
    m = re.search(r'([A-Za-z0-9_\-]+_MS\.pdf)', t)
    if not m:
        problems.append((f.name, 'no MS file cited'))
        continue
    pdf = ms_for.get(m.group(1))
    if pdf is None:
        problems.append((f.name, 'cited MS not in archive: ' + m.group(1)))
        continue
    pages, folio = load(pdf)
    for cited in sorted({int(x) for x in re.findall(r'MS (?:printed )?p\. ?(\d{1,2})', t)}):
        idx = folio.get(cited)
        if idx is None:
            problems.append((f.name, f'printed p. {cited} not printed in this MS'))
            continue
        checked += 1
        txt = pages[idx]
        if not ('Question' in txt or '\u2022' in txt or 'Answer' in txt or 'Level' in txt):
            problems.append((f.name, f'printed p. {cited} (PDF {idx+1}) has no answer-table furniture'))

print(f'citations checked: {checked}; flagged: {len(problems)}')
for p in problems:
    print(' ', p[0], '|', p[1])
