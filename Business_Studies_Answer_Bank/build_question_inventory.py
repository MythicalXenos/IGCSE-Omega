#!/usr/bin/env python3
"""Build a filterable 4BS1 item index from the searchable text-index ZIP.

The output is an inventory aid, not a replacement for visually checking each PDF.
"""
from __future__ import annotations
import csv
import re
import zipfile
from collections import Counter
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo

ROOT = Path('/home/user')
BANK = ROOT / 'Business_Studies_Answer_Bank'
INDEX_ZIP = ROOT / 'Paperlords_Archive' / 'Paperlords_Searchable_Text_Index.zip'
PAIRINGS_CSV = ROOT / 'Paperlords_Archive' / 'Paperlords_QP_MS_ER_Pairings.csv'
ITEMS_CSV = BANK / '4BS1_Question_Instances.csv'
TYPE_BOOK = BANK / '4BS1_Question_Type_Inventory.xlsx'

MARK_LINE = re.compile(r'^\s*\((1|2|3|6|9|12)\)\s*$')
PAGE_HEAD = re.compile(r'^===== PAGE (\d+) / (\d+) =====$')

TYPE_ROWS = [
    ['1', 'Select / multiple choice', 'Select one answer; some items are short calculations or numerical interpretation.', 'Choose one correct option; do not add an essay.', 'The correct response is the mark-scheme answer.'],
    ['1', 'Define', 'Define a business term.', 'Give a precise meaning; avoid using the term in its own definition.', 'Stakeholder; quantitative data.'],
    ['1', 'State / identify', 'State one valid point, normally linked to the named business if requested.', 'One clear item only; include the context where required.', 'On-the-job training method; financial objective.'],
    ['2', 'Calculate', 'Short numeric calculation (often percentage, markup, cost or cash-flow figure).', 'Write formula/substitution and final answer with units/rounding. Working can earn a mark.', 'Markup; gross profit margin; exchange-rate conversion.'],
    ['2', 'Outline one', 'Give one reason, benefit, method, impact or feature, then briefly develop or contextualise it.', 'Point + one relevant detail/application; do not list unrelated points.', 'Why IKEA reads government reports; why a firm uses robotics.'],
    ['3', 'Explain one', 'Explain one reason, way, benefit, disadvantage or impact.', 'Direct point + how/why it happens + a consequence. One developed point is better than a list.', 'Increase gross profit margin; impact of technology.'],
    ['6', 'Analyse / assess / how', 'Level-based analysis: importance, benefits, usefulness, effects, reasons, or how information/strategy is used.', 'Use the business context and develop logical cause-and-effect chains. Usually two developed strands; no generic definition needed.', 'Importance of customer needs; usefulness of ratios; benefits of franchising.'],
    ['9', 'Justify one of two options', 'Choose between two methods, options, strategies, or sources.', 'State your choice early; apply and develop reasons; consider a limitation/alternative; finish with a justified, contextual judgement. Equal coverage of both options is not compulsory.', 'Finance, motivation, pricing, research, operations, growth.'],
    ['12', 'Evaluate', 'Importance, benefits, impact/effects, factors, whether/extent, why/how, or likely success.', 'Build applied arguments, balance with a limitation/counterargument, and make a supported judgement. The exact paper mark scheme determines AO weighting.', 'Demographic segmentation, location, marketing, legal structure, quality, market changes.'],
]

PROMPT_PATTERNS = [
    ['1', 'Select one answer / multiple choice', 'Select the correct term, objective, function, source, consequence or numerical option.', 'Choose one response only. Context may determine which option is correct.', 'May/June 2019 P1 Q1(a)(i)–(iv); May/June 2019 P1 Q1(a)(v)–(vi).'],
    ['1', 'Define a term', 'Define a named business term (for example, stakeholder).', 'Give a precise meaning without repeating the term.', 'May/June 2019 P1 Q1(b).'],
    ['1', 'State / identify / name one item', 'Give one fact, method, objective, role, function or context-specific point.', 'One clear answer; check whether the item must be linked to the named business.', 'May/June 2019 P1 Q1(d); May 2023 P1 Q1(c).'],
    ['2', 'Calculate', 'Calculate a percentage, ratio, cost, cash-flow figure, exchange-rate amount or other business number.', 'Show formula/substitution and answer; include the required units/rounding.', 'Markup; gross profit margin; exchange-rate conversion; ratios in later sessions.'],
    ['2', 'Outline one reason / benefit / method / impact', 'Give one relevant point and briefly develop or contextualise it.', 'Point + a relevant detail or business link; do not list unrelated points.', 'May 2023 P2, IKEA reading government reports.'],

    ['2', 'State / identify (where specified)', 'Name the requested feature or item; the prompt may ask for more than one short point.', 'Answer the exact number of points requested and use the case where required.', 'Items are indexed individually in “All QP items”.'],
    ['3', 'Explain one reason / benefit / advantage / disadvantage / limitation / impact', 'Explain why one condition, feature or consequence matters to a business.', 'Point → how/why → consequence. Develop one point rather than giving a list.', '2019 P1 Q1(f); 2020–2026 examples indexed by session.'],

    ['3', 'Explain one way / method / strategy / measure', 'Explain one action or approach a business can use to achieve an aim or respond to a situation.', 'Name one suitable approach, then explain its effect in the specific business context.', 'May/June 2019 P1 Q1(f); May/June 2020 P1R; June 2026 P1.'],

    ['3', 'Explain one purpose / importance / factor / responsibility / use', 'Explain one purpose, factor, responsibility or use of a business concept/process.', 'Explain its relevance and develop a consequence; avoid an unnecessary definition.', 'May/June 2019 P2 Q2(d), job production; May 2023 P2, effective resource use.'],

    ['6', 'Analyse why / how / reasons', 'Explain why a business takes an action or how a factor/process affects it.', 'Apply the case and develop cause-and-effect; more than an assertion is needed.', 'May 2023 P2, IKEA shortlisting factory candidates; June 2026 P1, Crumb requesting CVs.'],

    ['6', 'Analyse benefits / advantages / disadvantages / impacts / effects', 'Analyse one or more consequences of an action, resource, strategy or business condition.', 'Link the effect to outcomes for the named business; follow the exact question’s scope.', 'May 2023 P2, IKEA franchises; June 2026 P1, Crumb using focus groups.'],

    ['6', 'Analyse importance / usefulness / purpose', 'Assess how valuable a concept, information source, objective or process is to the business.', 'Explain what it enables the business to do and why the result matters.', 'May 2019 P1 Q1(g), Q4(b).'],
    ['6', 'Analyse two methods / benefits (when explicitly asked)', 'Compare or develop two stated methods/benefits, if the wording asks for two.', 'Cover the number requested; make each point contextual and analytically developed.', 'Nov 2024 P1 Q2(d): two primary-research methods.'],
    ['9', 'Justify which of two options', 'Choose between two methods, strategies, sources, approaches or business options.', 'State choice → applied/developed reasons → limitation/alternative → supported final decision. Equal space for both options is not compulsory.', 'Repeated through 2019–June 2026; motivation, pricing, finance, research, HR and operations.'],
    ['12', 'Evaluate importance / benefits / usefulness', 'Judge the value of a strategy, concept, activity or process to the named business.', 'Develop benefits and limits, then prioritise with a supported judgement.', 'May 2023 P2 Q4(c); June 2024 P1 Q4(c).'],
    ['12', 'Evaluate factors / decision criteria', 'Judge which factors matter when making a business decision such as choosing a location.', 'Compare relative importance and costs/trade-offs; conclude which factor(s) should dominate and when.', 'May/June 2019 P2 Q4(c), factory location; May/June 2021 P1 Q4(c), success measures.'],

    ['12', 'Evaluate whether / extent / likely success', 'Judge whether a proposed action/status/strategy is worthwhile or how far it will work.', 'Arguments for and against; make a conditional, context-specific decision.', 'May/June 2020 P1 Q4(c), TADS becoming a private limited company.'],
    ['12', 'Evaluate impact / effects / how / why', 'Judge consequences of a change, strategy or business decision.', 'Develop positive and negative consequences, weigh their significance and finish with a reasoned conclusion.', 'May/June 2020 P2 Q4(c), consumer spending/competition; May/June 2022 P1R Q4(c), venture capital.'],

]

EXEMPLARS = [
    ['3', 'Explain one way to increase gross profit margin', 'May/June 2019 P1 Q1(f)', 'Official candidate A: 3/3; candidate B: 1/3', 'PDF pp. 5–6', 'The full-mark script develops one method; the lower response lists several ways without explaining one.', 'Local: Sources/Official_Pearson/4BS1_Paper1_Exemplar_Commentaries_June2019.pdf', 'https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Business%20Studies/2017/teaching-learning-materials/IG_Business_Paper_1_exemplar_with_commentaries.pdf'],
    ['6', 'Analyse importance of satisfying customer needs', 'May/June 2019 P1 Q1(g)', 'Official candidate A: 6/6; candidate B: 2/6', 'PDF pp. 7–9', 'Full-mark answer applies the shoe-retail context and develops loyalty/word-of-mouth into sales and profit.', 'Local: Sources/Official_Pearson/4BS1_Paper1_Exemplar_Commentaries_June2019.pdf', 'https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Business%20Studies/2017/teaching-learning-materials/IG_Business_Paper_1_exemplar_with_commentaries.pdf'],
    ['3', 'Explain one above-the-line promotion method', 'May/June 2019 P1 Q2(d)', 'Official candidate A: 3/3; candidate B: 1/3', 'PDF pp. 10–12', 'The examiner notes the candidate could skip the opening definition and go straight to television advertising and its effect.', 'Local: Sources/Official_Pearson/4BS1_Paper1_Exemplar_Commentaries_June2019.pdf', 'https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Business%20Studies/2017/teaching-learning-materials/IG_Business_Paper_1_exemplar_with_commentaries.pdf'],
    ['9', 'Justify a motivation option', 'May/June 2019 P1 Q2(f)', 'Official candidate A: 7/9; candidate B: 4/9', 'PDF pp. 13–16', 'High-level but not full marks; shows application and chains, but needed a stronger final evaluation.', 'Local: Sources/Official_Pearson/4BS1_Paper1_Exemplar_Commentaries_June2019.pdf', 'https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Business%20Studies/2017/teaching-learning-materials/IG_Business_Paper_1_exemplar_with_commentaries.pdf'],
    ['6', 'Analyse usefulness of break-even analysis', 'May/June 2019 P1 Q3(d)', 'Official candidate A: 4/6; candidate B: 2/6', 'PDF pp. 17–19', 'Examiner feedback: develop how the tool helps the specific business, rather than merely defining it.', 'Local: Sources/Official_Pearson/4BS1_Paper1_Exemplar_Commentaries_June2019.pdf', 'https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Business%20Studies/2017/teaching-learning-materials/IG_Business_Paper_1_exemplar_with_commentaries.pdf'],
    ['9', 'Justify a source of finance', 'May/June 2019 P1 Q3(e)', 'Official candidate A: 9/9; candidate B: 3/9', 'PDF pp. 20–25 (A’s marker comments at PDF p. 23)', 'Full-mark real student script; detailed context, chains for both options, and a justified choice.', 'Local: Sources/Official_Pearson/4BS1_Paper1_Exemplar_Commentaries_June2019.pdf', 'https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Business%20Studies/2017/teaching-learning-materials/IG_Business_Paper_1_exemplar_with_commentaries.pdf'],
    ['6', 'Analyse usefulness of profitability ratios', 'May/June 2019 P1 Q4(b)', 'Official candidate A: 6/6; candidate B: 2/6', 'PDF pp. 26–29', 'Full-mark script links the ratios to decisions the retailer can make.', 'Local: Sources/Official_Pearson/4BS1_Paper1_Exemplar_Commentaries_June2019.pdf', 'https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Business%20Studies/2017/teaching-learning-materials/IG_Business_Paper_1_exemplar_with_commentaries.pdf'],
    ['12', 'Evaluate importance of primary market research', 'May/June 2019 P1 Q4(c)', 'Official candidate A: 10/12; candidate B: 4/12', 'PDF pp. 30–35', 'Near-full rather than perfect; the examiner says the judgement needed more thorough evaluation.', 'Local: Sources/Official_Pearson/4BS1_Paper1_Exemplar_Commentaries_June2019.pdf', 'https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Business%20Studies/2017/teaching-learning-materials/IG_Business_Paper_1_exemplar_with_commentaries.pdf'],
    ['12', 'Evaluate importance of marketing to maintain market share', 'June 2024 P1 Q4(c)', 'Official candidate: 12/12', 'Examiner report pp. 37–39; excerpt saved locally', 'Full-mark candidate answer; examiner highlights balance, context throughout, linked reasoning, and a supported “it depends” conclusion.', 'Local: Sources/Official_Pearson/June2024_P1_Examiners_Report_Excerpts_12mark_Evaluate.pdf', 'https://qualifications.pearson.com/content/dam/pdf/International-GCSE/Business/2017/Exam-materials/4bs1-01-pef-20240822.pdf'],
    ['9', 'Justify which motivation option IKEA should use', 'May 2023 P2 Q3(e)', 'Official examiner-report example: 5/9', 'Examiner report pp. 48–50; excerpt saved locally', 'Exact-paper comparator: both options described, but the script was underdeveloped with limited evaluation. No separate knowledge marks.', 'Local: Sources/Official_Pearson/May2023_P2_Examiners_Report_Excerpts_Q3e_Q4c.pdf', 'https://qualifications.pearson.com/content/dam/pdf/International-GCSE/Business/2017/Exam-materials/4bs1-02-pef-20230824.pdf'],
    ['12', 'Evaluate demographic segmentation at IKEA', 'May 2023 P2 Q4(c)', 'Official examiner-report example: 10/12', 'Examiner report pp. 56–58; excerpt saved locally', 'Exact-paper near-full answer: developed knowledge, application and analysis; examiner says judgement was limited. Useful comparison with the constructed model in the guide.', 'Local: Sources/Official_Pearson/May2023_P2_Examiners_Report_Excerpts_Q3e_Q4c.pdf', 'https://qualifications.pearson.com/content/dam/pdf/International-GCSE/Business/2017/Exam-materials/4bs1-02-pef-20230824.pdf'],
    ['Various', 'Paper 2 example responses across 3-, 6-, 9- and 12-mark questions', 'June 2019 P2/P2R', 'Real candidate answers at several levels; e.g. 3/3 Explain, 7/9 Justify, 8/12 Evaluate', 'Original PDF pp. 5–14, 18–20, 24–31 (selected)', 'Selected official P2/2R scripts and examiner comments; 3/3 Q1(f), 5/6 Q1(g), 7/9 Q2(f), 6/9 Q3(e), 8/12 Q4(c), 5/6 P2R Q1(g), plus comparison scripts.', 'Local selected excerpt: Sources/Official_Pearson/June2019_P2_Exemplar_Responses_Selected_Pages.pdf', 'https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Business%20Studies/2017/teaching-learning-materials/IG_Business_Paper_2_exemplar_responses.pdf'],

]

SOURCES = [
    ['Archive corpus', '38 Business 4BS1 QPs with matching MS; 5 examiner reports in the searchable archive, plus catalog/pairing maps.', 'Paperlords_Archive/Paperlords_Searchable_Text_Index.zip; Paperlords_Archive/Paperlords_QP_MS_ER_Pairings.csv', 'Local archive; use search_paperlords.py or the workbook.'],
    ['2019 Paper 1/1R exemplar booklet', 'Official Pearson real candidate responses with mark schemes and examiner comments across 3-, 6-, 9- and 12-mark questions.', 'Sources/Official_Pearson/4BS1_Paper1_Exemplar_Commentaries_June2019.pdf', 'https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Business%20Studies/2017/teaching-learning-materials/IG_Business_Paper_1_exemplar_with_commentaries.pdf'],
    ['2019 Paper 2/2R exemplar booklet', 'Official Pearson real Paper 2 candidate responses and examiner comments; selected pages are saved locally, while the full source remains at Pearson.', 'Sources/Official_Pearson/June2019_P2_Exemplar_Responses_Selected_Pages.pdf', 'https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Business%20Studies/2017/teaching-learning-materials/IG_Business_Paper_2_exemplar_responses.pdf'],

    ['May 2023 P2 examiner report', 'Exact-paper examples for IKEA Q3(e) and Q4(c), with level/score and examiner commentary.', 'Sources/Official_Pearson/May2023_P2_Examiners_Report_Excerpts_Q3e_Q4c.pdf; source PDF in archive ZIP.', 'https://qualifications.pearson.com/content/dam/pdf/International-GCSE/Business/2017/Exam-materials/4bs1-02-pef-20230824.pdf'],
    ['June 2024 P1 examiner report', 'Includes a 12/12 real-candidate evaluation response for marketing importance to PPS.', 'Sources/Official_Pearson/June2024_P1_Examiners_Report_Excerpts_12mark_Evaluate.pdf', 'https://qualifications.pearson.com/content/dam/pdf/International-GCSE/Business/2017/Exam-materials/4bs1-01-pef-20240822.pdf'],
]


def classify(mark: int, text: str) -> str:
    t = text.lower()
    if mark == 1:
        if re.search(r'\bdefine\b', t): return 'Define (1)' 
        if re.search(r'\bstate\b|\bidentify\b|\bname\b', t): return 'State/identify (1)'
        if re.search(r'select one answer|which one of the following|select one', t): return 'MCQ/selection (1)'
        if re.search(r'\bcalculate\b|how much|percentage increase|what is the percentage', t): return 'Numerical/MCQ calculation (1)'
        return 'Other one-mark item (check prompt)'
    if mark == 2:
        if re.search(r'\bcalculate\b|how much|percentage increase|markup|mark-up', t): return 'Calculate (2)'
        if re.search(r'\boutline\b', t): return 'Outline one (2)'
        if re.search(r'\bstate\b|\bidentify\b', t): return 'State/identify (2)'
        return 'Other two-mark item (check prompt)'
    if mark == 3:
        return 'Explain one (3)' if re.search(r'\bexplain\b', t) else 'Three-mark explain-family (3)'
    if mark == 6:
        return 'Analyse/assess (6)'
    if mark == 9:
        return 'Justify a choice (9)'
    if mark == 12:
        return 'Evaluate (12)'
    return f'{mark}-mark item'


def find_excerpt(lines: list[str], start: int, end: int, mark: int) -> str:
    """Return the text between adjacent standalone mark lines, not a broad page window.

    On the source QPs the mark is normally printed after its prompt. Splitting at
    the previous mark prevents adjacent MCQs from being merged together. The excerpt
    itself stops before the mark line; the caller separately checks a few following
    lines for instructions such as “Select one answer.”
    """
    segment = lines[start + 1:end]
    text = re.sub(r'\s+', ' ', ' '.join(segment)).strip()
    # Prefer the command expected for this mark value. A question can follow an
    # inline-mark item on the same page, so generic "State/Explain" matches may
    # otherwise select the preceding item instead of the current one.
    preferred = {
        1: r'\b(?:Define|State|Identify|Which one|Which|What|How much|How|Calculate|Give|Name)\b',
        2: r'\b(?:Calculate|Outline|State|Identify|Explain|Describe)\b',
        3: r'\b(?:Explain|Describe)\b',
        6: r'\b(?:Analyse|Analyze|Assess)\b',
        9: r'\bJustify\b',
        12: r'\bEvaluate\b',
    }
    matches = list(re.finditer(preferred.get(mark, r'\b\w+\b'), text, re.I))
    if matches:
        text = text[matches[0].start():]
    else:
        generic = r'\b(?:Define|State|Identify|Which one|Which|What|How much|How|Calculate|Outline|Explain|Analyse|Analyze|Assess|Justify|Evaluate|Give|Name|Describe|Suggest|Recommend|To what extent)\b'
        matches = list(re.finditer(generic, text, re.I))
        if matches:
            text = text[matches[0].start():]
    text = re.sub(r'\bDO NOT WRITE.*$', '', text, flags=re.I)
    text = re.sub(r'\bTOTAL FOR PAPER.*$', '', text, flags=re.I)
    return text[:600].strip()


def build_items():
    items=[]
    pairings={}
    with PAIRINGS_CSV.open('r',encoding='utf-8-sig',newline='') as f:
        for row in csv.DictReader(f):
            if row.get('Subject')=='Business Studies' and row.get('Course code')=='4BS1':
                pairings[row.get('QP PDF path','')]={
                    'MS PDF path inside full ZIP':row.get('MS PDF path',''),
                }
    with zipfile.ZipFile(INDEX_ZIP) as z:
        names=[n for n in z.namelist() if '/4BS1_Business_Studies/' in n and n.endswith('_QP.txt')]
        for name in names:
            raw=z.read(name).decode('utf-8','replace')
            header={}
            for key in ['SESSION','PAPER','PDF PATH IN COMPLETE ZIP']:
                m=re.search(rf'^{re.escape(key)}:\s*(.+)$',raw,re.M)
                header[key]=m.group(1).strip() if m else ''
            pages=re.split(r'(?m)^===== PAGE (\d+) / (\d+) =====\s*$',raw)
            # split format returns preamble, pageNo, pageTotal, pageText, ...
            for k in range(1,len(pages)-2,3):
                page_no=pages[k]; page_text=pages[k+2]
                lines=page_text.splitlines()
                previous_mark=-1
                for i,line in enumerate(lines):
                    mm=MARK_LINE.fullmatch(line)
                    if not mm: continue
                    mark=int(mm.group(1))
                    excerpt=find_excerpt(lines,previous_mark,i,mark)
                    classification_text=' '.join([excerpt] + lines[i+1:min(len(lines),i+4)])
                    qtype=classify(mark,classification_text)
                    qp_pdf=header.get('PDF PATH IN COMPLETE ZIP','')
                    matching_ms=pairings.get(qp_pdf,{})
                    items.append({
                        'Session':header.get('SESSION',''),
                        'Paper':header.get('PAPER',''),
                        'Mark value':mark,
                        'Detected type':qtype,
                        'Page in QP':page_no,
                        'Prompt/context excerpt (text extraction)':excerpt,
                        'QP PDF path inside full ZIP':qp_pdf,
                        'Matching MS PDF path inside full ZIP':matching_ms.get('MS PDF path inside full ZIP',''),
                    })
                    previous_mark=i
    return items


def style_sheet(ws, widths=None):
    ws.freeze_panes='A2'
    ws.auto_filter.ref=ws.dimensions
    for cell in ws[1]:
        cell.font=Font(bold=True,color='FFFFFF')
        cell.fill=PatternFill('solid',fgColor='24476B')
        cell.alignment=Alignment(wrap_text=True,vertical='center')
    ws.row_dimensions[1].height=32
    for row in ws.iter_rows(min_row=2):
        for cell in row:
            cell.alignment=Alignment(wrap_text=True,vertical='top')
    if widths:
        for col,width in widths.items(): ws.column_dimensions[col].width=width


def main():
    BANK.mkdir(parents=True,exist_ok=True)
    items=build_items()
    with ITEMS_CSV.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(items[0].keys()))
        w.writeheader();w.writerows(items)
    wb=Workbook()
    ws=wb.active;ws.title='Question families'
    headers=['Marks','Command/family','What the question looks like','High-yield answer shape','Archive examples']
    ws.append(headers)
    for row in TYPE_ROWS: ws.append(row)
    style_sheet(ws,{'A':10,'B':27,'C':56,'D':67,'E':56})
    # More detailed command-stem patterns within the broad mark families.
    ws_patterns=wb.create_sheet('Prompt pattern map')
    pattern_headers=['Marks','Prompt pattern','What is asked','High-yield response','Archive examples']
    ws_patterns.append(pattern_headers)
    for row in PROMPT_PATTERNS: ws_patterns.append(row)
    style_sheet(ws_patterns,{'A':10,'B':48,'C':68,'D':78,'E':62})
    # Item-level inventory
    ws2=wb.create_sheet('All QP items')
    cols=list(items[0].keys());ws2.append(cols)
    for item in items: ws2.append([item[k] for k in cols])
    style_sheet(ws2,{'A':20,'B':12,'C':12,'D':33,'E':13,'F':88,'G':76,'H':76})
    # Official candidate/examiner examples
    ws3=wb.create_sheet('Official exemplars')
    ex_headers=['Marks','Question type','Series / prompt','Published score','Source section/pages','Examiner takeaway','Local source','Official source URL']
    ws3.append(ex_headers)
    for row in EXEMPLARS:ws3.append(row)
    style_sheet(ws3,{'A':12,'B':42,'C':38,'D':34,'E':30,'F':72,'G':80,'H':90})
    # Sources
    ws4=wb.create_sheet('Sources & scope')
    ws4.append(['Source','What it contains','Local location','URL / access note'])
    for row in SOURCES:ws4.append(row)
    style_sheet(ws4,{'A':30,'B':78,'C':95,'D':100})
    # add tables for filter controls on populated sheets
    for sheet,tabname in [(ws,'FamiliesTable'),(ws_patterns,'PromptPatternsTable'),(ws2,'ItemsTable'),(ws3,'ExemplarsTable'),(ws4,'SourcesTable')]:
        ref=sheet.dimensions
        tab=Table(displayName=tabname,ref=ref)
        tab.tableStyleInfo=TableStyleInfo(name='TableStyleMedium2',showFirstColumn=False,showLastColumn=False,showRowStripes=True,showColumnStripes=False)
        sheet.add_table(tab)
    wb.save(TYPE_BOOK)
    print(f'Built {len(items)} items from {len({i["QP PDF path inside full ZIP"] for i in items})} QPs')
    print('Mark counts:',dict(sorted(Counter(i['Mark value'] for i in items).items())))
    print('Type book:',TYPE_BOOK,'bytes',TYPE_BOOK.stat().st_size)
    print('Items CSV:',ITEMS_CSV,'bytes',ITEMS_CSV.stat().st_size)

if __name__=='__main__': main()
