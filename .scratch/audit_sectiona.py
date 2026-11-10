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

qs = {}
for qp in glob.glob('Paperlords_Archive/IGCSE/4EB1_English_Language_B/*/*_QP.pdf'):
    folder = pathlib.Path(qp).parent.name
    label = pathlib.Path(qp).stem.split('_')[-2]
    d = pymupdf.open(qp)
    # gather text up to the Section B page
    texts = []
    for p in d:
        t = p.get_text()
        if 'SECTION B' in t and re.search(r'^\s*8\s+\S', t, re.M):
            break
        texts.append(t)
    blob = "\n".join(texts)
    found = {}
    for m in re.finditer(r"^([1-7])[ \t]*\t\s*(.+?)(?=\n[1-7][ \t]*\t|\n\s*\(Total for Question|$)", blob, re.S | re.M):
        num = m.group(1)
        if num in found:
            continue
        body = re.sub(r"\s+", " ", m.group(2))
        found[num] = norm(body)[:400]
    qs[(folder_map[folder], label)] = found

rows = []
for f in sorted(pathlib.Path('English_Answer_Bank/Answer_Sets').glob('*_Section_A.md')):
    m = re.match(r'(.+?)_(P\dR?)_Section_A', f.stem)
    if not m:
        rows.append((f.name, 'PARSE FAIL', '', 0))
        continue
    sess, label = m.group(1), m.group(2)
    found = qs.get((key_map.get(sess, sess), label), {})
    tn = norm(f.read_text())
    if not found:
        rows.append((f.name, 'NO QP QUESTIONS', '', 0))
        continue
    worst = (1.0, '', '')
    for num, body in found.items():
        toks = body.split()
        n = 5
        if len(toks) < n:
            continue
        grams = [' '.join(toks[i:i + n]) for i in range(len(toks) - n + 1)]
        cov = sum(1 for g in grams if g in tn) / len(grams)
        if cov < worst[0]:
            worst = (cov, num, body[:90])
    rows.append((f.name, f'{worst[0]:.2f}', sorted(found), len(found)))

print('papers checked', len(rows))
for r in rows: print(r[0], r[1], r[2], 'n=', r[3])
print()
for r in sorted(rows, key=lambda x: x[1])[:14]:
    print(r)
