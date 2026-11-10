import pymupdf, re, glob, pathlib

def norm(s):
    return s.replace("\u2013", "-").replace("\u2014", "-")

folder_map = {'January_2020': 'Jan 2020', 'January_2022': 'Jan 2022', 'June_2026': 'June 2026',
              'May-June-November_2020': 'MayJuneNov 2020', 'May-June_2019': 'MayJune 2019',
              'May-June_2021': 'MayJune 2021', 'May-June_2022': 'MayJune 2022', 'May-June_2023': 'MayJune 2023',
              'May-June_2024': 'MayJune 2024', 'May_2025': 'May 2025', 'November_2021': 'Nov 2021',
              'November_2023': 'Nov 2023', 'November_2024': 'Nov 2024', 'November_2025': 'Nov 2025'}
key_map = {'June_2019': 'MayJune 2019', 'January_2020': 'Jan 2020', 'January_2022': 'Jan 2022',
           'June_2022': 'MayJune 2022', 'June_2023': 'MayJune 2023', 'June_2024': 'MayJune 2024',
           'MayJuneNov_2020': 'MayJuneNov 2020', 'May_2025': 'May 2025', 'November_2021': 'Nov 2021',
           'November_2023': 'Nov 2023', 'November_2024': 'Nov 2024', 'November_2025': 'Nov 2025',
           'MayJune_2021': 'MayJune 2021', 'June_2026': 'June 2026', 'MayJune_2022': 'MayJune 2022',
           'MayJune_2024': 'MayJune 2024', 'MayJune_2023': 'MayJune 2023', 'MayJune_2019': 'MayJune 2019'}

# measure Section A span in printed terms
span = {}
for ms in sorted(glob.glob('Paperlords_Archive/IGCSE/4EB1_English_Language_B/*/*_MS.pdf')):
    folder = pathlib.Path(ms).parent.name
    label = pathlib.Path(ms).stem.split('_')[-2]
    d = pymupdf.open(ms)
    pages = [norm(p.get_text()) for p in d]
    printed = []
    for i, t in enumerate(pages):
        lines = [l.strip() for l in t.splitlines() if l.strip()]
        printed.append(int(lines[0]) if lines and re.fullmatch(r'\d{1,2}', lines[0]) else None)
    def printed_of(i):
        return printed[i] if printed[i] is not None else i + 1
    # Section A start: first page mentioning 'Question 1' (or SECTION A)
    a_start = next((i for i, t in enumerate(pages) if 'Question 1' in t), None)
    b_start = next((i for i, t in enumerate(pages) if 'Question 8' in t), None)
    if a_start is None or b_start is None:
        span[(folder_map[folder], label)] = None
        continue
    span[(folder_map[folder], label)] = (printed_of(a_start), printed_of(b_start - 1), a_start + 1, b_start)

for f in sorted(pathlib.Path('English_Answer_Bank/Answer_Sets').glob('*_Section_A.md')):
    m = re.match(r'(.+?)_(P\dR?)_Section_A', f.stem)
    key = (key_map.get(m.group(1), m.group(1)), m.group(2)) if m else None
    t = f.read_text()
    line = next((l for l in t.splitlines() if 'mark scheme' in l.lower()), '')
    rng = re.search(r'pp?\.\s*(\d{1,2})\s*[-\u2013]\s*(\d{1,2})', line)
    print(f'{f.name:38s} claim={rng.groups() if rng else None} measured={span.get(key)}')
