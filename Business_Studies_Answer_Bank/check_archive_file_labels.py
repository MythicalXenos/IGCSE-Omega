"""LAYER D: verify that every archive MS/QP file's NAME matches the paper code
PRINTED INSIDE it.

Why: the May/June 2024 pair is filed the wrong way round - the file called
`..._P1_MS.pdf` prints "Paper 01R" and vice versa. Every block extracted from a
mislabelled file inherits the wrong session/paper attribution, and paper
attribution is what ties a block to a case study and to a tariff.

Pearson prints the paper code in the MS front matter ("Paper 01R: ...") and in
the QP footer ("4BS1/01R"). Read both, compare to the file name.
"""
import pathlib
import re
import pypdf

BASE = pathlib.Path('/home/user/IGCSE-Omega/Paperlords_Archive/IGCSE/4BS1_Business_Studies')


def first_page_text(p, pages=2):
    r = pypdf.PdfReader(str(p))
    return ' '.join(' '.join((pg.extract_text() or '').split()) for pg in r.pages[:pages])


def ms_claim(p):
    t = first_page_text(p)
    m = re.search(r'Paper\s*0?([12]R?)\b', t)
    return ('P' + m.group(1)) if m else '(no code printed)'


def qp_claim(p):
    r = pypdf.PdfReader(str(p))
    for pg in r.pages[:6]:
        t = ' '.join((pg.extract_text() or '').split())
        m = re.search(r'4BS1\s*/\s*0([12]R?)', t)
        if m:
            return 'P' + m.group(1)
    return '(no code printed)'


def main():
    bad = []
    for folder in sorted(p for p in BASE.iterdir() if p.is_dir()):
        files = sorted(folder.glob('*.pdf'))
        by = {}
        for f in files:
            m = re.match(r'4BS1_Business_Studies_(.+?)_(P\d R?|P\dR?)_(MS|QP)\.pdf$', f.name)
            if not m:
                continue
            by.setdefault(m.group(2).replace(' ', ''), {})[m.group(3)] = f
        print(f'--- {folder.name}')
        for paper in sorted(by):
            pair = by[paper]
            for kind, fn in (('MS', ms_claim), ('QP', qp_claim)):
                if kind not in pair:
                    print(f'    {paper:4s} {kind}: FILE MISSING')
                    continue
                claim = fn(pair[kind])
                ok = 'ok ' if claim == paper else 'BAD'
                if claim != paper:
                    bad.append((folder.name, paper, kind, pair[kind].name, claim))
                print(f'    {paper:4s} {kind}: prints {claim:5s} {ok}  {pair[kind].name}')
    print()
    print('=' * 78)
    print(f'MISLABELLED FILES: {len(bad)}')
    for sess, paper, kind, name, claim in bad:
        print(f'   {sess:14s} file says {paper:4s} but prints {claim:5s} :: {name}')


if __name__ == '__main__':
    main()
