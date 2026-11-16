import pymupdf, re, glob, pathlib

def norm(s):
    return (s.replace("\u2013", "-").replace("\u2014", "-").replace("\u2212", "-"))

for ms in sorted(glob.glob('Paperlords_Archive/IGCSE/4EB1_English_Language_B/*/*_MS.pdf')):
    d = pymupdf.open(ms)
    pages = [norm(p.get_text()) for p in d]
    blob = "\n".join(pages)
    name = pathlib.Path(ms).name.replace('4EB1_English_Language_B_', '')
    secB_ao4 = bool(re.search(r'11-12', blob))
    secB_ao5 = bool(re.search(r'\b7-8\b', blob))
    secC_ao4 = bool(re.search(r'17-20', blob))
    secC_ao5 = bool(re.search(r'\b9-10\b', blob))
    # locate pages
    def page_with(pat):
        for i, t in enumerate(pages):
            if re.search(pat, t):
                return i + 1
        return None
    p_b4 = page_with(r'11-12')
    p_b5 = page_with(r'\b7-8\b')
    p_c4 = page_with(r'17-20')
    p_c5 = page_with(r'\b9-10\b')
    print(f"{name:55s} B(11-12)={secB_ao4} B(7-8)={secB_ao5} C(17-20)={secC_ao4} C(9-10)={secC_ao5} pages: B4={p_b4} B5={p_b5} C4={p_c4} C5={p_c5}")
