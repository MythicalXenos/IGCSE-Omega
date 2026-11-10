"""INTEGRITY CHECK (Layer D): does each MS's 4(c) stem agree with the QP labelled
as the same paper?

Why this exists: the June 2026 P1 mark scheme asks about 'Violet Cakes' while the
question paper labelled June 2026 P1 asks about 'Crumb'. One of the two files is
mislabelled. If MS files are swapped between P1 and P1R anywhere, every case
attribution derived from them is wrong - and case attribution is the AO2 of the
whole bank.

Method: pull the 4(c) stem out of each MS (via the block text) and out of each QP
(text layer, tolerating the 'E valuate' / 'Ev aluate' fragmentation), then score
similarity and hunt for the stem of THIS paper inside the OTHER paper's files.
"""
import difflib
import pathlib
import re
import pypdf

BASE = pathlib.Path('/home/user/IGCSE-Omega/Paperlords_Archive/IGCSE/4BS1_Business_Studies')
FOLDERS = {
    'June 2026': 'June_2026', 'May-June 2019': 'May-June_2019',
    'May-June 2020': 'May-June_2020', 'May-June 2021': 'May-June_2021',
    'May-June 2022': 'May-June_2022', 'May 2023': 'May_2023',
    'May-June 2024': 'May-June_2024', 'May-June 2025': 'May-June_2025',
    'November 2021': 'November_2021', 'November 2023': 'November_2023',
    'November 2024': 'November_2024', 'November 2025': 'November_2025',
}
PAPERS = ['P1', 'P1R', 'P2', 'P2R']


def ms_units():
    """session/paper -> stem as printed in the mark scheme."""
    txt = (BASE.parent.parent.parent / 'Business_Studies_Answer_Bank'
           / 'layer_c_12mark_blocks.txt').read_text(encoding='utf-8')
    lines = txt.split('\n')
    heads = [i for i, l in enumerate(lines) if re.match(r'^=== .+ \| .+ \| .+$', l)]
    out = {}
    for n, i in enumerate(heads):
        end = heads[n + 1] if n + 1 < len(heads) else len(lines)
        ses, paper, _ = [x.strip() for x in lines[i][4:].split('|')]
        body = '\n'.join(lines[i + 1:end])
        m = re.search(r'Question Number\s*(.*?)(?:\n|Indicative)', body, re.S)
        stem = ' '.join(m.group(1).split()) if m else ''
        out[(ses, paper)] = stem
    return out


def qp_stem(folder, tag):
    p = BASE / folder / f'4BS1_Business_Studies_{tag}_QP.pdf'
    if not p.exists():
        return '(no QP file)'
    r = pypdf.PdfReader(str(p))
    best = ''
    for pg in r.pages:
        t = ' '.join((pg.extract_text() or '').split())
        t = re.sub(r'\bE\s?valuate\b', 'Evaluate', t)
        t = re.sub(r'\bEv\s?aluate\b', 'Evaluate', t)
        m = re.search(r'Evaluate.{0,230}?You should use', t)
        if m:
            cand = ' '.join(m.group(0).split())
            if len(cand) > len(best):
                best = cand
    return best


def norm(s):
    # THE FAILURE MODE THIS TOOL HAD FOR TWO MONTHS: it compared the mark scheme's
    # stem (which runs to "...own knowledge of business.") with a question-paper stem
    # that the extractor had already cut at "You should use". Four of the five
    # "MISMATCHES" it reported were that, not a swap. Compare like with like.
    s = re.split(r"You should use", s)[0]
    return re.sub(r"[^a-z ]", "", s.lower()).strip()


# The two differences that are REAL, each verified by reading both documents.
KNOWN_DIFFERENT = {
    ("June 2026", "P1"):
        "the paper is an amended edition: it prints Crumb (owner Alex), the scheme prints "
        "Violet Cakes (owner Claire). Same business, two names. Confirmed against both "
        "documents; the bank prints the paper's names.",
    ("May-June 2022", "P1R"):
        "the scheme says 'the opening of Can Culleretes'; the paper says 'the opening of "
        "Can CAFE' - a second, smaller premises the restaurant is opening. Verified by "
        "reading p. 18 of the QP. The scheme is loose, not swapped; the bank quotes the "
        "paper where it quotes the question.",
}


def main():
    ms = ms_units()
    qps = {}
    for ses, folder in FOLDERS.items():
        for paper in PAPERS:
            qps[(ses, paper)] = qp_stem(folder, f'{folder}_{paper}')

    print(f'{"session":14s} {"pap":4s} {"sim":>5s}  MS business / QP business')
    print('-' * 108)
    flags = []
    for (ses, paper), mstem in sorted(ms.items()):
        qstem = qps.get((ses, paper), '(missing)')
        if not mstem:
            mstem = '(MS prints no stem)'
        a, b = norm(mstem), norm(qstem)
        if a.startswith('ms prints') or b.startswith('no qp') or not b:
            sim = -1
        else:
            sim = difflib.SequenceMatcher(None, a, b).ratio()
        # try the MS stem against every OTHER paper of the same session
        alt = []
        for (s2, p2), q2 in qps.items():
            if s2 != ses or p2 == paper or not q2 or q2.startswith('(no'):
                continue
            r = difflib.SequenceMatcher(None, a, norm(q2)).ratio()
            if r > sim and r > 0.7:
                alt.append((round(r, 2), p2))
        flag = ''
        if sim >= 0 and sim < 0.75 and (ses, paper) not in KNOWN_DIFFERENT:
            flag = '  <<< MISMATCH'
            if alt:
                flag += ' - MS stem matches ' + ', '.join(f'{p} ({r})' for r, p in alt)
            flags.append((ses, paper))
        elif sim >= 0 and sim < 0.90 and (ses, paper) in KNOWN_DIFFERENT:
            flag = '  known difference (read, not inferred)'
        elif sim >= 0 and sim < 0.90:
            flag = '  <<< LOW - read the diff'
            flags.append((ses, paper))
        shown = '  -' if sim < 0 else f'{sim:.2f}'
        print(f'{ses:14s} {paper:4s} {shown:>5}  {mstem[:40]:40s} | {qstem[:40]}{flag}')
    print()
    print(f"MISMATCHES: {len(flags)}")
    print(f"known, verified differences set aside: {len(KNOWN_DIFFERENT)}")
    for k, why in KNOWN_DIFFERENT.items():
        print(f"   {k[0]} {k[1]}: {why}")
    for f in flags:
        print('   ', f)


if __name__ == '__main__':
    main()
