import pymupdf, re, glob, pathlib, json

def norm(s):
    return s.replace("\u2013", "-").replace("\u2014", "-")


folder_map = {'January_2020': 'Jan 2020', 'January_2022': 'Jan 2022', 'June_2026': 'June 2026',
              'May-June-November_2020': 'MayJuneNov 2020', 'May-June_2019': 'MayJune 2019',
              'May-June_2021': 'MayJune 2021', 'May-June_2022': 'MayJune 2022', 'May-June_2023': 'MayJune 2023',
              'May-June_2024': 'MayJune 2024', 'May_2025': 'May 2025', 'November_2021': 'Nov 2021',
              'November_2023': 'Nov 2023', 'November_2024': 'Nov 2024', 'November_2025': 'Nov 2025'}

rows = []
for ms in sorted(glob.glob('Paperlords_Archive/IGCSE/4EB1_English_Language_B/*/*_MS.pdf')):
    folder = pathlib.Path(ms).parent.name
    label = pathlib.Path(ms).stem.split('_')[-2]
    d = pymupdf.open(ms)
    pages = []
    offs = []
    for i, p in enumerate(d):
        t = norm(p.get_text())
        lines = [l.strip() for l in t.splitlines() if l.strip()]
        num = int(lines[0]) if lines and re.fullmatch(r'\d{1,2}', lines[0]) else None
        pages.append(t)
        offs.append(num - (i + 1) if num is not None else None)
    measured = {}
    for key, pat in [('C_content', 'SECTION C'), ('C_AO4', 'AO4'), ('C_AO5', 'AO5')]:
        hit = None
        if key == 'C_content':
            for i, t in enumerate(pages):
                if 'SECTION C' in t:
                    hit = i
                    break
        else:
            start = next((i for i, t in enumerate(pages) if 'SECTION C' in t), 0)
            for i in range(start, len(pages)):
                if key[-3:] in pages[i]:
                    hit = i
                    break
        measured[key] = (hit + 1) if hit is not None else None
    off = offs[measured['C_content'] - 1] if measured['C_content'] else None
    rows.append({'paper': f'{folder_map[folder]} {label}', 'file': pathlib.Path(ms).name,
                 'pages': measured, 'printed_of_content': off,
                 'offset': off})

for r in rows:
    print(f"{r['paper']:18s} content={r['pages']['C_content']} AO4={r['pages']['C_AO4']} AO5={r['pages']['C_AO5']} "
          f"offset(printed-page)={r['offset']}")
