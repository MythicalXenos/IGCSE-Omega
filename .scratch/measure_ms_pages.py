import pymupdf, re, glob, pathlib, json

def norm(s):
    return s.replace("\u2013", "-").replace("\u2014", "-").replace("\u2212", "-")

folder_map = {'January_2020': 'Jan 2020', 'January_2022': 'Jan 2022', 'June_2026': 'June 2026',
              'May-June-November_2020': 'MayJuneNov 2020', 'May-June_2019': 'MayJune 2019',
              'May-June_2021': 'MayJune 2021', 'May-June_2022': 'MayJune 2022', 'May-June_2023': 'MayJune 2023',
              'May-June_2024': 'MayJune 2024', 'May_2025': 'May 2025', 'November_2021': 'Nov 2021',
              'November_2023': 'Nov 2023', 'November_2024': 'Nov 2024', 'November_2025': 'Nov 2025'}

out = {}
for ms in sorted(glob.glob('Paperlords_Archive/IGCSE/4EB1_English_Language_B/*/*_MS.pdf')):
    folder = pathlib.Path(ms).parent.name
    label = pathlib.Path(ms).stem.split('_')[-2]
    d = pymupdf.open(ms)
    pages = [norm(p.get_text()) for p in d]
    # Section C start: page containing 'SECTION C' (last occurrence region) or the Q9 content page
    cstart = None
    for i, t in enumerate(pages):
        if 'SECTION C' in t:
            cstart = i
    rec = {}
    if cstart is not None:
        for j in range(cstart, len(pages)):
            t = pages[j]
            if 'AO4' in t and 'AO4' not in rec:
                rec['C_AO4'] = j + 1
            if 'AO5' in t and 'AO5' not in rec:
                rec['C_AO5'] = j + 1
    rec['C_content'] = (cstart + 1) if cstart is not None else None
    # Section B: page with 'Question 8'
    bstart = None
    for i, t in enumerate(pages):
        if re.search(r'Question\s*8', t):
            bstart = i
            break
    if bstart is not None:
        for j in range(bstart, len(pages)):
            t = pages[j]
            if 'AO1' in t and 'B_AO1' not in rec:
                rec['B_AO1'] = j + 1
            if 'AO4' in t and 'B_AO4' not in rec:
                rec['B_AO4'] = j + 1
            if 'AO5' in t and 'B_AO5' not in rec:
                rec['B_AO5'] = j + 1
    out[f"{folder_map[folder]}|{label}"] = rec

for k, v in out.items():
    print(k, v)
