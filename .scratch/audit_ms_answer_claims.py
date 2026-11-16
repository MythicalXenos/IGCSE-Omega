import pymupdf, re, glob, pathlib, unicodedata

def norm(s):
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
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

mstext = {}
for ms in glob.glob('Paperlords_Archive/IGCSE/4EB1_English_Language_B/*/*_MS.pdf'):
    folder = pathlib.Path(ms).parent.name
    label = pathlib.Path(ms).stem.split('_')[-2]
    d = pymupdf.open(ms)
    mstext[(folder_map[folder], label)] = norm(" ".join(p.get_text() for p in d))

STOP = set("the a an of and or to in is are be for with that this it as on by from at which their they them his her its not but can may all any one two".split())

results = []
for f in sorted(pathlib.Path('English_Answer_Bank/Answer_Sets').glob('*_Section_A.md')):
    m = re.match(r'(.+?)_(P\dR?)_Section_A', f.stem)
    key = (key_map.get(m.group(1), m.group(1)), m.group(2))
    big = mstext.get(key, '')
    t = f.read_text()
    answers = re.findall(r'One valid answer is:\s*\*\*(.+?)\*\*', t) + re.findall(r'Two distinct valid answers are:\s*(.+?)\n', t)
    checked = 0
    hits = 0
    misses = []
    for a in answers[:6]:
        words = [w for w in norm(a).split() if w not in STOP and len(w) > 2]
        if not words:
            continue
        checked += 1
        present = sum(1 for w in words if w in big)
        ratio = present / len(words)
        if ratio >= 0.7:
            hits += 1
        else:
            misses.append((a[:60], round(ratio, 2)))
    results.append((f.name, checked, hits, misses))

for r in results:
    print(f'{r[0]:38s} checked={r[1]:2d} supported={r[2]:2d} misses={r[3]}')
