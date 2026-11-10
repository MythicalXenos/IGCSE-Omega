"""Check Section C 'MS printed p. N' claims against the archive mark schemes.

Each cited printed page must exist in the matched mark scheme and carry Section C
material (indicative content or an AO4/AO5 grid). Citations beyond the MS page count
are examiner-report pages and are skipped.
"""
import pathlib, re, pymupdf

ms_files = {p.name: p for p in pathlib.Path('Paperlords_Archive/IGCSE/4EB1_English_Language_B').rglob('*_MS.pdf')}
cache = {}
MARKERS = ('SECTION C', 'Indicative content', 'Points of comparison', 'Question 9', 'Question 10',
           'Question 11', 'Questions 9, 10 and 11', 'AO4', 'AO5')

def load(pdf):
    if pdf not in cache:
        pages = [p.get_text() for p in pymupdf.open(pdf)]
        folio = {}
        for i, t in enumerate(pages):
            lines = [l.strip() for l in t.splitlines() if l.strip()]
            if lines and re.fullmatch(r'\d{1,2}', lines[0]):
                folio.setdefault(int(lines[0]), []).append(i)
        cache[pdf] = (pages, folio)
    return cache[pdf]

problems, checked, skipped = [], 0, 0
for f in sorted(pathlib.Path('English_Answer_Bank/Answer_Sets').glob('*_Section_C.md')):
    t = f.read_text()
    m = re.search(r'([A-Za-z0-9_\-]*_MS\.pdf)', t)
    if not m:
        problems.append((f.name, 'no MS file cited')); continue
    stem = m.group(1)
    pdf = ms_files.get(stem)
    if pdf is None:  # citations abbreviate the front of the filename: score by session token
        sessns = ('January_2020', 'January_2022', 'May-June-November_2020', 'May-June_2019', 'May-June_2021',
                  'May-June_2022', 'May-June_2023', 'May-June_2024', 'May_2025', 'November_2021',
                  'November_2023', 'November_2024', 'November_2025', 'June_2026')
        hits = [s for s in sessns if s in t]
        cands = [(1 if any(s in n for s in hits) else 0, n) for n in ms_files if n.endswith(stem)]
        pdf = ms_files[max(cands)[1]] if cands else None
    if pdf is None:
        problems.append((f.name, 'cited MS not in archive: ' + m.group(1))); continue
    pages, folio = load(pdf)
    for cited in sorted({int(x) for x in re.findall(r'printed p\. ?(\d{1,2})', t)}):
        candidates = folio.get(cited, [])
        if not candidates and 0 < cited <= len(pages):
            candidates = [cited - 1]
        if not candidates:
            if cited > len(pages):
                skipped += 1
                continue
            problems.append((f.name, f'printed p. {cited} cannot be located')); continue
        checked += 1
        if not any(any(mk in pages[i] for mk in MARKERS) for i in candidates):
            pgs = ', '.join(str(i + 1) for i in candidates)
            problems.append((f.name, f'printed p. {cited} (PDF {pgs}) is not Section C content'))

print(f'citations checked: {checked}; report-page citations skipped: {skipped}; flagged: {len(problems)}')
for p in problems:
    print(' ', p[0], '|', p[1])
