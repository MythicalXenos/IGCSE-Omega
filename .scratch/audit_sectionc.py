import pymupdf, re, pathlib, glob, unicodedata

LQ = "\u2018"; RQ = "\u2019"; LDQ = "\u201c"; RDQ = "\u201d"


def norm(s):
    s = s.replace(RQ, "'").replace(LQ, "'").replace(LDQ, '"').replace(RDQ, '"')
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

truth = {}
for qp in glob.glob('Paperlords_Archive/IGCSE/4EB1_English_Language_B/*/*_QP.pdf'):
    folder = pathlib.Path(qp).parent.name
    label = pathlib.Path(qp).stem.split('_')[-2]
    d = pymupdf.open(qp)
    pg = None
    for p in d:
        if 'Answer ONE question from this section' in p.get_text():
            pg = p.get_text()
            break
    if not pg:
        continue
    got = {}
    lines = [l.strip() for l in pg.splitlines()]
    for i, l in enumerate(lines):
        m = re.match(r"^(9|10|11)\s+(.+)$", l)
        if m and m.group(1) not in got:
            txt = m.group(2)
            if i + 1 < len(lines) and lines[i + 1] and not re.match(r"^(9|10|11|OR|EITHER|\(Total)", lines[i + 1]):
                txt += " " + lines[i + 1]
            got[m.group(1)] = txt
    truth[(folder_map[folder], label)] = got

key_map = {'June_2019': 'MayJune 2019', 'January_2020': 'Jan 2020', 'January_2022': 'Jan 2022',
           'June_2022': 'MayJune 2022', 'June_2023': 'MayJune 2023', 'June_2024': 'MayJune 2024',
           'MayJuneNov_2020': 'MayJuneNov 2020', 'May_2025': 'May 2025', 'November_2021': 'Nov 2021',
           'November_2023': 'Nov 2023', 'November_2024': 'Nov 2024', 'November_2025': 'Nov 2025',
           'MayJune_2021': 'MayJune 2021', 'June_2026': 'June 2026', 'MayJune_2022': 'MayJune 2022',
           'MayJune_2024': 'MayJune 2024', 'MayJune_2023': 'MayJune 2023', 'MayJune_2019': 'MayJune 2019'}

TITLE_RE = re.compile("entitled\\s*[" + LQ + "'\"" + "]([^" + RQ + "'\"]+)[" + RQ + "'\"]")
Q11_RE = re.compile(r"describe\s+([^.]{10,120})", re.I)
Q9_RE = re.compile("[" + LQ + "'\"]" + "([^" + RQ + "\"]{10,150})[" + RQ + "'\"]" + "[^" + RQ + "\"]{0,30}?(discuss|to what extent)", re.I)

rows = []
for f in sorted(pathlib.Path('English_Answer_Bank/Answer_Sets').glob('*_Section_C.md')):
    m = re.match(r'(.+?)_(P\dR?)_Q(\d{1,2})_Section_C', f.stem)
    if not m:
        rows.append((f.name, 'PARSE FAIL', ''))
        continue
    sess, label, q = m.group(1), m.group(2), str(int(m.group(3)))
    qp = truth.get((key_map.get(sess, sess), label), {}).get(q)
    if not qp:
        rows.append((f.name, 'NO QP TEXT', q))
        continue
    tn = norm(f.read_text())
    if q == '10':
        mt = TITLE_RE.search(qp)
        frag = norm(mt.group(1)) if mt else ''
        rows.append((f.name, 'TITLE OK' if frag and frag in tn else 'TITLE MISS', frag))
    elif q == '11':
        mt = Q11_RE.search(qp)
        frag = norm(mt.group(1))[:60] if mt else ''
        rows.append((f.name, 'Q11 OK' if frag and frag in tn else 'Q11 MISS', frag))
    else:
        mt = Q9_RE.search(qp)
        frag = norm(mt.group(1))[:60] if mt else norm(qp)[:50]
        rows.append((f.name, 'Q9 OK' if frag and frag in tn else 'Q9 MISS', frag))

print('total', len(rows))
bad = [r for r in rows if ' OK' not in r[1]]
print('flagged', len(bad))
for r in bad:
    print(r)
