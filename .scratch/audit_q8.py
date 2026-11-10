import pymupdf, re, glob, pathlib, unicodedata

LQ, RQ = "\u2018", "\u2019"


def norm(s):
    s = s.replace(RQ, "'").replace(LQ, "'").replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2013", "-").replace("\u2014", "-")
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = s.lower()
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


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

q8 = {}
for qp in glob.glob('Paperlords_Archive/IGCSE/4EB1_English_Language_B/*/*_QP.pdf'):
    folder = pathlib.Path(qp).parent.name
    label = pathlib.Path(qp).stem.split('_')[-2]
    d = pymupdf.open(qp)
    txt = None
    for p in d:
        t = p.get_text()
        if 'SECTION B' in t and re.search(r'^\s*8\s+\S', t, re.M):
            txt = t
            break
    if not txt:
        continue
    m = re.search(r'^\s*8\s+(.+?)(?:\n\s*You should include|\n\s*Think carefully|\n\s*\(30\)|$)', txt, re.S | re.M)
    q8[(folder_map[folder], label)] = norm(re.sub(r'\s+', ' ', m.group(1))) if m else ''

rows = []
for f in sorted(pathlib.Path('English_Answer_Bank/Answer_Sets').glob('*Q*8_Section_B.md')):
    m = re.match(r'(.+?)_(P\dR?)_Q8_Section_B', f.stem)
    if not m:
        rows.append((f.name, 'PARSE FAIL', ''))
        continue
    sess, label = m.group(1), m.group(2)
    prompt = q8.get((key_map.get(sess, sess), label), '')
    if not prompt:
        rows.append((f.name, 'NO QP TEXT', ''))
        continue
    tn = norm(f.read_text())
    toks = prompt.split()
    n = 6
    grams = [' '.join(toks[i:i + n]) for i in range(max(1, len(toks) - n + 1))]
    hit = sum(1 for g in grams if g in tn)
    cov = hit / len(grams)
    rows.append((f.name, f'{cov:.2f}', prompt[:80]))

print('total', len(rows))
for r in sorted(rows, key=lambda x: x[1])[:12]:
    print(r)
