#!/usr/bin/env python3
"""LAYER C, 12-MARK TIER — inventory of the 38 governed Evaluate blocks.

Source of truth: layer_c_12mark_blocks.txt (regenerate: python3 extract_ms_blocks.py 12).

Reports, per block:
  session, paper, stem (from the MS, else the instances CSV - content only),
  the four AO bullet sets verbatim, and a derived TOPIC.

The stem trap is the one already documented for the 6- and 9-mark tiers:
2019 / 2020 / Nov-2021-P1 mark schemes print NO Q1-Q3 stem, so 4(c) can come
out blank. The CSV fills the CONTENT gap; it is never a counting authority.
"""
import csv
import re
import pathlib
import collections

BLOCKS = pathlib.Path('layer_c_12mark_blocks.txt')
OUT = pathlib.Path('layer_c_12mark_inventory.csv')


def parse_blocks():
    lines = BLOCKS.read_text(encoding='utf-8').split('\n')
    heads = [i for i, l in enumerate(lines)
             if re.match(r'^=== .+ \| .+ \| .+$', l)]
    out = []
    for n, i in enumerate(heads):
        end = heads[n + 1] if n + 1 < len(heads) else len(lines)
        ses, paper, part = [x.strip() for x in lines[i][4:].split('|')]
        body = re.sub(r'={70,}', '', '\n'.join(lines[i + 1:end]))
        body = re.sub(r'Level Mark Descriptor.*', '', body, flags=re.S)
        body = body.replace('Indicative content Mark', '\nSTOP')
        body = body.replace('Indicative Content Mark', '\nSTOP')
        out.append({'session': ses, 'paper': paper, 'part': part, 'body': body})
    return out


def stem_of(body):
    """The block now OPEN includes the tail of the previous question, so read the
    stem from the LAST 'Question Number' / 'Q. No.' heading whose following text
    carries a full run of AO sections - i.e. this block's own header."""
    best = ''
    for m in re.finditer(r'(?i)(?:q\s*u\s*e\s*s\s*t\s*i\s*o\s*n\s*n\s*u\s*m\s*b\s*e\s*r'
                         r'|q\.\s*no\.)', body):
        seg = body[m.end():]
        cut = seg.find('Level Mark Descriptor')
        if cut > 0:
            seg = seg[:cut]
        if len(re.findall(r'\bA[O0]\s*[1234]\s*=', seg)) < 4:
            continue
        sm = re.search(r'\s*(.*?)\s*(?:Indicative content Mark|Indicative Content Mark|STOP)',
                       body[m.start():], re.S)
        cand = ' '.join(sm.group(1).split()) if sm else ''
        cand = re.sub(r'^Question Number|^Q\.\s*No\.', '', cand).strip()
        if cand and not re.fullmatch(r'4\s*\(c\)', cand):
            best = cand
    return best


def ao_bullets(body):
    res = {}
    for ao in (1, 2, 3, 4):
        m = re.search(r'AO%d\s*=' % ao, body)
        if not m:
            res[ao] = []
            continue
        tail = body[m.end():]
        nxt = re.search(r'AO\d\s*=', tail)
        chunk = tail[:nxt.start()] if nxt else tail
        chunk = chunk.replace('3 marks', ' ')
        chunk = re.sub(r'\(12\)\s*$', '', chunk)
        chunk = re.sub(r'4BS1[\d/]*\s*(Summer|November)[^\n]*', '', chunk)
        bullets = [' '.join(b.split()) for b in re.split(r'•', chunk) if len(' '.join(b.split())) > 8]
        res[ao] = bullets
    return res


# ---- topic rules: FIRST MATCH WINS -------------------------------------
# order matters: a stem naming two concepts goes to the EARLIER rule
RULES = [
    ('LOCATION', r'\blocat(e|ing|ion)\w*|where .{0,30}(factory|shop|studio|business)'),
    ('BUSINESS STRUCTURE / OWNERSHIP', r'private limited company|public limited|ltd status|ownership|sole trader|partnership'),
    ('ORGANISATION STRUCTURE', r'centralis|decentralis|organisational? structure|span of control|hierarch'),
    ('FRANCHISE', r'franchis'),
    ('INTEREST RATES', r'interest rate'),
    ('CASH FLOW FORECASTING', r'cash[- ]flow'),
    ('FINANCIAL DOCUMENTS', r'financial document|statement of comprehensive income|balance sheet|final accounts'),
    ('VENTURE CAPITAL', r'venture capital'),
    ('QUALITY', r'\bquality\b|TQM|total quality'),
    ('CUSTOMER NEEDS / MARKET CHANGE', r'changes? in (the )?(customer|market|consumer)|respond(ing)? to the changes|changes? in customer needs|consumer spending'),
    ('MARKET ORIENTATION', r'market orientation'),
    ('DEMOGRAPHIC SEGMENTATION', r'demographic|segment'),
    ('PRODUCT TRIALS', r'product trial|test(ing)? (it|the product) on the market|test market'),
    ('MARKET RESEARCH', r'market research'),
    ('PUBLIC RELATIONS', r'public relations'),
    ('PROMOTION / ADVERTISING', r'advertis|promot|social media|e-newsletter'),
    ('MARKETING', r'\bmarketing\b'),
    ('COMPETITIVE ADVANTAGE', r'competitive advantage|remain competitive|maintain(ed)? .{0,25}(market share|advantage)'),
    ('MEASURING SUCCESS', r'measur\w* .{0,24}(success|business)|make a business.{0,25}success|only consider profit'),
    ('SOCIAL OBJECTIVES / ETHICS', r'social objective|ethic|charit|donat|sustainab|environment'),
    ('MOTIVATION', r'motivat'),
    ('COMMUNICATION', r'communicat'),
]


def topic_of(stem):
    s = stem.lower()
    for name, pat in RULES:
        if re.search(pat, s, re.I):
            return name
    return 'UNMAPPED'


# Seven mark schemes print no 4(c) stem AND sit outside the CSV's coverage.
# Stems below were read off the QUESTION PAPER (page cited) - see
# Source_Notes/ARCHIVE_LABEL_AUDIT_2026-10-14.md for the June 2026 name clash.
STEM_OVERRIDES = {
    ('June 2026', 'P2R'): 'Evaluate the importance of Apple responding to changes in the market.',
    ('May-June 2024', 'P2R'): 'Evaluate the factors Jimmy Choo would have to consider when making decisions on the location of a new factory.',
    ('May-June 2024', 'P2'): 'Evaluate the benefits for TUI of providing a quality service.',
    ('May-June 2025', 'P2R'): 'Evaluate the effect for Rabanne of working hard to maintain and improve its public relations.',
    ('May-June 2025', 'P2'): 'Evaluate why Starbucks carries out product trials that might reduce the risks from introducing new products.',
    ('November 2021', 'P1'): 'Evaluate the factors that Artify Studio would have considered when deciding where to locate its second art studio.',
    ('November 2025', 'P2'): 'Evaluate whether a centralised organisation structure will benefit Samsung.',
}


def main():
    blocks = parse_blocks()
    assert len(blocks) == 38, f'expected 38 blocks, got {len(blocks)}'

    csv_stems = {}
    for r in csv.DictReader(open('4BS1_Question_Instances.csv', encoding='utf-8-sig')):
        if r['Mark value'].strip() != '12':
            continue
        csv_stems[(r['Session'], r['Paper'])] = ' '.join(
            r['Prompt/context excerpt (text extraction)'].split())

    rows = []
    for b in blocks:
        stem = stem_of(b['body'])
        src = 'MS'
        if not stem and (b['session'], b['paper']) in STEM_OVERRIDES:
            stem, src = STEM_OVERRIDES[(b['session'], b['paper'])], 'QP'
        if not stem:
            key = (b['session'].replace('-', '').replace(' ', ''), b['paper'])
            cand = None
            for (s, p), v in csv_stems.items():
                if p == b['paper'] and s.replace('-', '').replace(' ', '') == key[0]:
                    cand = v
                    break
            if cand:
                stem, src = cand, 'CSV'
            else:
                stem, src = '(stem not printed and not recovered)', 'NONE'
        aos = ao_bullets(b['body'])
        rows.append({
            'Session': b['session'], 'Paper': b['paper'], 'Part': b['part'],
            'Stem source': src, 'Stem': stem, 'Topic': topic_of(stem),
            'AO1': ' || '.join(aos[1]), 'AO2': ' || '.join(aos[2]),
            'AO3': ' || '.join(aos[3]), 'AO4': ' || '.join(aos[4]),
        })

    with OUT.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    print(f'blocks parsed             : {len(rows)}')
    print(f'stems from MS            : {sum(1 for r in rows if r["Stem source"] == "MS")}')
    print(f'stems from CSV           : {sum(1 for r in rows if r["Stem source"] == "CSV")}')
    print(f'stems still missing      : {sum(1 for r in rows if r["Stem source"] == "NONE")}')
    bad = [r for r in rows if not all(len(r["AO%d" % a].split(" || ")) >= 1 for a in (1, 2, 3, 4))]
    print(f'blocks missing an AO set : {len(bad)}')
    topics = collections.Counter(r['Topic'] for r in rows)
    print(f'distinct topics          : {len(topics)}  (unmapped {topics.get("UNMAPPED", 0)})')
    print()
    for t, c in topics.most_common():
        papers = [f'{r["Session"][:12]}/{r["Paper"]}' for r in rows if r['Topic'] == t]
        print(f'  {c}  {t}\n       {", ".join(papers)}')


if __name__ == '__main__':
    main()
