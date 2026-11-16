import pymupdf, re, glob, pathlib, json

LQ, RQ, LD, RD = "\u2018", "\u2019", "\u201c", "\u201d"


def norm(s):
    return s.replace("\u2013", "-").replace("\u2014", "-").replace("\u2212", "-")


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

mspages = {}
for ms in glob.glob('Paperlords_Archive/IGCSE/4EB1_English_Language_B/*/*_MS.pdf'):
    folder = pathlib.Path(ms).parent.name
    label = pathlib.Path(ms).stem.split('_')[-2]
    d = pymupdf.open(ms)
    mapping = {}
    texts = {}
    for i, p in enumerate(d):
        t = norm(p.get_text())
        texts[i + 1] = t
        lines = [l.strip() for l in t.splitlines() if l.strip()]
        if lines and re.fullmatch(r'\d{1,2}', lines[0]):
            mapping[int(lines[0])] = i + 1
    mspages[(folder_map[folder], label)] = (mapping, texts)

CLAIM_RE = {
    'C_AO4': re.compile(r'AO4[^.\n]{0,40}?p\.?\s*(\d{1,2})', re.I),
    'C_AO5': re.compile(r'AO5[^.\n]{0,40}?p\.?\s*(\d{1,2})', re.I),
}

issues = []
for f in sorted(pathlib.Path('English_Answer_Bank/Answer_Sets').glob('*_Section_C.md')):
    m = re.match(r'(.+?)_(P\dR?)_Q(\d{1,2})_Section_C', f.stem)
    if not m:
        continue
    sess, label = m.group(1), m.group(2)
    key = (key_map.get(sess, sess), label)
    if key not in mspages:
        issues.append((f.name, 'no MS map', key))
        continue
    mapping, texts = mspages[key]
    t = norm(f.read_text())
    head = t[:4000]
    for what, rx in CLAIM_RE.items():
        mm = rx.search(head)
        if not mm:
            continue
        claimed = int(mm.group(1))
        pdf = mapping.get(claimed)
        if pdf is None:
            issues.append((f.name, what, f'printed p.{claimed} not present in MS map'))
            continue
        page = texts[pdf]
        token = 'AO4' if what == 'C_AO4' else 'AO5'
        if token not in page:
            issues.append((f.name, what, f'printed p.{claimed} (pdf {pdf}) lacks {token}'))

print('Section C page-claim issues:', len(issues))
for i in issues:
    print(' ', i)
