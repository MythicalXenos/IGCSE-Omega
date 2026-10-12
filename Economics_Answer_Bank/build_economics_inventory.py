#!/usr/bin/env python3
"""Build a compact, filterable 4EC1 inventory from the existing Paperlords text index.

No QP/MS/ER PDFs are copied. The workbook points to the matching PDFs in the
full archive; the matching text file has the same relative path with .txt instead
of .pdf in Paperlords_Searchable_Text_Index.zip.
"""
from __future__ import annotations
import re
import csv
import zipfile
from collections import Counter
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.worksheet.table import Table, TableStyleInfo

ROOT=Path('/home/user')
BANK=ROOT/'Economics_Answer_Bank'
INDEX_ZIP=ROOT/'Paperlords_Archive'/'Paperlords_Searchable_Text_Index.zip'
PAIRINGS=ROOT/'Paperlords_Archive'/'Paperlords_QP_MS_ER_Pairings.csv'
OUT=BANK/'4EC1_Question_Type_Inventory.xlsx'
MARK_LINE=re.compile(r'^\s*\((1|2|3|6|9|12)\)\s*$')

TYPE_ROWS=[
 ['1','Select one / multiple choice','Choose the correct economic term, relationship, outcome or diagram/data option.','One correct option; use the information in the question. No explanation unless asked.','Demand, supply, market structure, macro objectives, data interpretation.'],
 ['1','State / identify','Give the requested single fact or item.','Answer only what is asked; do not spend time developing it.','Examples include a factor of production or a role of the central bank.'],
 ['2','Define / “What is meant by…”','Define a term, normally requiring two precise parts.','Give the two elements in the mark scheme. Examples are not a substitute for a definition.','Demand; interest rate; current-account surplus; devaluation.'],
 ['2','Calculate','Calculate a price, ratio, elasticity, balance, rate, percentage or per-capita figure.','Show the working, use the requested precision and include correct units/signs. Exact MS rules vary.','Average cost; PED/PES; exchange rates; GDP per capita; fiscal/current-account figures.'],
 ['2','Describe one impact / advantage / reason','Give one point and describe its effect/development.','Point + what happens next; use a relevant context link when the question requires it.','Impact of lower interest rates; advantage of competition; reason for a cost.'],
 ['3','Explain one reason / advantage / impact / way','Develop one economic point, often with a reason, effect or consequence and context.','Explain the causal link. Where the exact MS awards context, apply it; do not just insert a data figure.','Price-inelastic concert demand; currency depreciation; current-account effects.'],
 ['3','Draw and label a diagram','Show a specified change in a market, factor market, PPF or other model.','Make the correct curve/line change and label the new curve and requested equilibrium values. Shift only the curve named by the cause.','Hurricane destroys farmland; quota; subsidy; minimum wage; exchange-rate changes.'],
 ['6','Analyse','Develop an economic mechanism or impact using relevant theory/data/context.','One-sided analysis; build connected cause-and-effect. Quality of analysis matters more than number of points. Evaluation is not required.','Reasons for acquisition; unemployment; inflation; policy effects.'],
 ['9','Assess','Evaluate the issue through arguments on both sides, using economic theory and the evidence/context.','Balanced, applied two-sided reasoning. A separate conclusion is not required and receives no standalone mark.','Trade-bloc membership; inflation; productivity policies; externalities.'],
 ['12','Evaluate','Evaluate a policy, market effect or economic decision and reach a supported judgement.','Develop both sides, weigh the alternatives/conditions, then give a clear supported conclusion. Avoid listing alternatives without evaluating the question set.','Progressive taxation; subsidies; oligopoly; growth and the environment.'],
]

PATTERNS=[
 ['1','Select one answer / multiple choice','One-step recall, diagram reading or data/relationship selection.','Choose the single correct option.','2019 P1 and P2 Q1(a) items; all sessions indexed.'],
 ['1','State / identify one item','Name a role, factor, objective or other fact.','One precise point; no explanation needed unless the prompt says so.','2023 P2 Q2(c), role of a central bank (examiner report).'],
 ['2','Define a term','“What is meant by…”; the scheme usually requires two defining features.','Two precise components. Do not give an example instead of a component.','2019 P1 Q1(c) demand; P2 Q1(c) interest rate.'],
 ['2','Calculate','Numeric business/economic calculation; sometimes a currency, percentage, balance or rate.','Show figures and working; use units, sign and decimal places exactly as requested.','2019 P1 average cost/PED; P2 exchange rate; 2023 fiscal deficit and unemployment rate.'],
 ['2','Describe one impact / advantage / reason','A single point followed by a described effect or development.','Impact + development; keep the answer focused on the specified person/group/economy.','2019 P2 Q1(d), lower interest rates and consumers.'],
 ['3','Explain one reason / effect / advantage / method','Explain one developed economic point; the prompt may require application to the case.','Point → economic mechanism → consequence/context. No definition-only opening.','2019 P1 Q1(h), ticket demand elasticity; P2 Q2(e), depreciating currency.'],
 ['3','Draw and label a diagram','A graphical response with marks for a curve/line shift and labelled consequences.','Shift the correct curve once; label the new curve and equilibrium price/quantity or the requested points.','2019 P1 Q1(g), hurricane/supply; P2 Q1(f), quota.'],
 ['6','Analyse why / how / impact / benefits','One-sided analysis of a policy or economic mechanism.','Develop connected chains; apply data/theory. Do not add evaluation just to sound balanced.','2023 P2 Q1(h), benefits of quotas; Q4(b) P2R, inflation and exports.'],
 ['9','Assess whether / extent / benefits / effectiveness / impact','A levels-based evaluation with more than one viewpoint.','Develop a balanced argument using the extract; no separate conclusion is required.','2019 P2 Q2(g), Thailand and a trade bloc; 2023 P2 Q2(g), infrastructure spending.'],
 ['12','Evaluate whether / how effective / most effective / impact','A higher-tariff evaluation requiring a supported judgement.','Balance, compare conditions/alternatives and conclude. Evaluate the asked policy before suggesting other policies.','2019 P2 Q4(c), progressive taxes; 2023 P2 Q4(c), subsidies and the environment.'],
]

EXEMPLARS=[
 ['2','Define demand','June 2019 P1 Q1(c)','Official candidates: 2/2; 1/2','Original PDF pp. 4–5','Two separate parts are required: willingness/ability and a given price; examples do not earn definition marks.','Official Pearson Paper 1 2019 exemplar PDF','https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Economics/2017/teaching-learning-materials/ig-economics-paper-1-exemplar-responses-with-commentaries.pdf'],
 ['2','Calculate average cost','June 2019 P1 Q1(f)','Official candidates: 2/2; 1/2','Original PDF p. 7','Show the calculation and give the final monetary unit.','Official Pearson Paper 1 2019 exemplar PDF','https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Economics/2017/teaching-learning-materials/ig-economics-paper-1-exemplar-responses-with-commentaries.pdf'],
 ['3','Draw supply/market diagram after hurricane','June 2019 P1 Q1(g)','Official candidates: 3/3; 2/3','Original PDF pp. 9–10','The 3/3 answer labels the leftward supply shift, higher equilibrium price and lower quantity.','Official Pearson Paper 1 2019 exemplar PDF','https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Economics/2017/teaching-learning-materials/ig-economics-paper-1-exemplar-responses-with-commentaries.pdf'],
 ['3','Explain why concert-ticket demand may be price inelastic','June 2019 P1 Q1(h)','Official candidates: 3/3; 2/3','Original PDF p. 12','One developed reason plus context earns full marks; an undeveloped reason misses the explanation mark.','Official Pearson Paper 1 2019 exemplar PDF','https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Economics/2017/teaching-learning-materials/ig-economics-paper-1-exemplar-responses-with-commentaries.pdf'],
 ['6','Analyse Coca-Cola buying shares in Inca Kola','June 2019 P1 Q1(i)','Official candidates: 5/6; 4/6','Original PDF pp. 15–16','Both are below full marks; the higher answer has clear knowledge/application and connected analysis but not all level criteria.','Official Pearson Paper 1 2019 exemplar PDF','https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Economics/2017/teaching-learning-materials/ig-economics-paper-1-exemplar-responses-with-commentaries.pdf'],
 ['2','Calculate PED','June 2019 P1 Q2(c)','Official candidates: 2/2; 0/2','Original PDF p. 18','A correct answer including the negative sign is required by this MS; a formula alone earns no marks.','Official Pearson Paper 1 2019 exemplar PDF','https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Economics/2017/teaching-learning-materials/ig-economics-paper-1-exemplar-responses-with-commentaries.pdf'],
 ['2','Describe a passenger advantage from competition','June 2019 P1 Q2(f)','Official candidates: 2/2; 1/2','Original PDF p. 20','A relevant advantage must be developed, not repeated.','Official Pearson Paper 1 2019 exemplar PDF','https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Economics/2017/teaching-learning-materials/ig-economics-paper-1-exemplar-responses-with-commentaries.pdf'],
 ['3','Explain higher auto-rickshaw fares outside Dhaka centre','June 2019 P1 Q2(g)','Official candidates: 3/3; 2/3','Original PDF p. 22','The 3/3 response explains weaker competition and links it to the number of people outside the city centre.','Official Pearson Paper 1 2019 exemplar PDF','https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Economics/2017/teaching-learning-materials/ig-economics-paper-1-exemplar-responses-with-commentaries.pdf'],
 ['9','Assess training/education as the best way to raise productivity','June 2019 P1 Q3(e)','Official candidates: 6/9; 5/9','Original PDF pp. 27–28','Neither response is full marks; the 6/9 answer has two viewpoints but lacks thorough analysis/evaluation.','Official Pearson Paper 1 2019 exemplar PDF','https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Economics/2017/teaching-learning-materials/ig-economics-paper-1-exemplar-responses-with-commentaries.pdf'],
 ['12','Evaluate how firms may be influenced by oligopoly','June 2019 P1 Q4(c)','Official candidates: 9/12; 7/12','Original PDF pp. 34 and 36 (examiner comments)','Near-full, not perfect. The 9/12 script meets the lower-level criteria but has limited chains; the 7/12 script has relevant but less-developed reasoning.','Official Pearson Paper 1 2019 exemplar PDF','https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Economics/2017/teaching-learning-materials/ig-economics-paper-1-exemplar-responses-with-commentaries.pdf'],
 ['2','Define interest rate','June 2019 P2 Q1(c)','Official candidates: 2/2; 1/2','Original PDF pp. 5–6','Two parts: cost of borrowing and reward for lending/saving. A central-bank example does not replace the definition.','Official Pearson Paper 2 2019 exemplar PDF','https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Economics/2017/teaching-learning-materials/ig-economics-paper-2-exemplar-responses.pdf'],
 ['2','Describe an impact of lower interest rates on consumers','June 2019 P2 Q1(d)','Official candidates: 2/2; 1/2','Original PDF pp. 7–8','Identify an impact and describe its development, such as cheaper borrowing leading to more loans/purchases.','Official Pearson Paper 2 2019 exemplar PDF','https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Economics/2017/teaching-learning-materials/ig-economics-paper-2-exemplar-responses.pdf'],
 ['2','Calculate a sterling price from an exchange rate','June 2019 P2 Q1(e)','Official candidates: 2/2; 1/2','Original PDF p. 10','The mark scheme requires a correct calculation and a final answer with currency units/precision.','Official Pearson Paper 2 2019 exemplar PDF','https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Economics/2017/teaching-learning-materials/ig-economics-paper-2-exemplar-responses.pdf'],
 ['3','Draw and label a quota diagram','June 2019 P2 Q1(f)','Official candidates: 3/3; 2/3','Original PDF pp. 12–13','All three labels are needed; the 2/3 response did not label the new curve.','Official Pearson Paper 2 2019 exemplar PDF','https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Economics/2017/teaching-learning-materials/ig-economics-paper-2-exemplar-responses.pdf'],
 ['3','Explain an advantage of a depreciating currency','June 2019 P2 Q2(e)','Official candidates: 3/3; 2/3','Original PDF p. 15','Full marks came from an advantage, development and country context; the lower script lacked context.','Official Pearson Paper 2 2019 exemplar PDF','https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Economics/2017/teaching-learning-materials/ig-economics-paper-2-exemplar-responses.pdf'],
 ['9','Assess benefits of Thailand joining a trade bloc','June 2019 P2 Q2(g)','Official candidates: 8/9; 5/9','Original PDF pp. 19 and 21','The 8/9 answer is not full marks; data use, balance and developed evaluation are praised. A separate conclusion is not required.','Official Pearson Paper 2 2019 exemplar PDF','https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Economics/2017/teaching-learning-materials/ig-economics-paper-2-exemplar-responses.pdf'],
 ['6','Analyse the impact of unemployment','June 2019 P2 Q3(d)','Official candidates: 5/6; 3/6','Original PDF pp. 23–24','The full reasoning chain is more important than a list; the lower script was mostly undeveloped statements.','Official Pearson Paper 2 2019 exemplar PDF','https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Economics/2017/teaching-learning-materials/ig-economics-paper-2-exemplar-responses.pdf'],
 ['9','Assess inflation’s impact on Turkey','June 2019 P2 Q3(e)','Official candidates: 6/9; 4/9','Original PDF pp. 28 and 31','Both are below full marks. The 6/9 response is balanced but remains Level 2; the 4/9 answer is less developed.','Official Pearson Paper 2 2019 exemplar PDF','https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Economics/2017/teaching-learning-materials/ig-economics-paper-2-exemplar-responses.pdf'],
 ['12','Evaluate progressive tax as a way to reduce poverty/inequality','June 2019 P2 Q4(c)','Official candidates: 9/12; 7/12','Original PDF pp. 36–37','The 9/12 answer is a strong but not full-mark example; its judgement/evaluation can be compared with the mark scheme.','Official Pearson Paper 2 2019 exemplar PDF','https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Economics/2017/teaching-learning-materials/ig-economics-paper-2-exemplar-responses.pdf'],
 ['6','Analyse quota benefits to domestic farmers','June 2023 P2 Q1(h)','Official examiner-report script: 6/6','Printed report p. 14; source PDF path in archive','The report praises developed analysis linking quotas to protection, growth and preventing dumping; this is a verified full-mark script.','IGCSE/4EC1_Economics/May_2023/4EC1_Economics_May_2023_P2_ER.pdf','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/Economics/2017/Exam-materials/4ec1-02-pef-20230824.pdf'],
 ['9','Assess infrastructure spending and productive potential','June 2023 P2 Q2(g)','Official examiner-report script: 9/9','Printed report p. 21; source PDF path in archive','Verified full marks: applied, balanced discussion of costs/time lags and alternatives. The examiner explicitly says a separate conclusion is not required.','IGCSE/4EC1_Economics/May_2023/4EC1_Economics_May_2023_P2_ER.pdf','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/Economics/2017/Exam-materials/4ec1-02-pef-20230824.pdf'],
 ['12','Evaluate subsidies to protect the environment','June 2023 P2 Q4(c)','Official examiner-report script: 10/12','Printed report p. 37; source PDF path in archive','Not full marks. The answer is balanced and contextual, but the examiner calls for a supported, non-repetitive judgement.','IGCSE/4EC1_Economics/May_2023/4EC1_Economics_May_2023_P2_ER.pdf','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/Economics/2017/Exam-materials/4ec1-02-pef-20230824.pdf'],
 ['9','Assess fiscal-surplus benefits for a country','June 2023 P2R Q2(g)','Official examiner-report script: 9/9','Printed report p. 23; source PDF path in archive','Verified full marks: two benefits are balanced against the high taxes that created the surplus and possible living-standard effects.','IGCSE/4EC1_Economics/May_2023/4EC1_Economics_May_2023_P2R_ER.pdf','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/Economics/2017/Exam-materials/4ec1-02r-pef-20230824.pdf'],
 ['6','Analyse inflation’s effect on export demand','June 2023 P2R Q4(b)','Official examiner-report script: 6/6','Printed report p. 38; source PDF path in archive','Verified full marks: develops comparison with other countries’ inflation and connects it to exports/current account.','IGCSE/4EC1_Economics/May_2023/4EC1_Economics_May_2023_P2R_ER.pdf','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/Economics/2017/Exam-materials/4ec1-02r-pef-20230824.pdf'],
 ['12','Evaluate pollution permits to protect the environment','June 2023 P2R Q4(c)','Official examiner-report script: 11/12','Printed report p. 42; source PDF path in archive','Near-full, not perfect: balanced argument and judgement, but one criterion was not fully met.','IGCSE/4EC1_Economics/May_2023/4EC1_Economics_May_2023_P2R_ER.pdf','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/Economics/2017/Exam-materials/4ec1-02r-pef-20230824.pdf'],
 ['9','Assess public parks/open spaces','June 2023 P1R Q2(h)','Official examiner-report script: 7/9','Printed report p. 25; source PDF path in archive','A Level 3 response with evidence and more than one viewpoint, but not fully balanced.','IGCSE/4EC1_Economics/May_2023/4EC1_Economics_May_2023_P1R_ER.pdf','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/Economics/2017/Exam-materials/4ec1-01r-pef-20230824.pdf'],
 ['9','Assess a merger and economies of scale','June 2023 P1R Q3(e)','Official examiner-report script: 7/9','Printed report p. 31; source PDF path in archive','Two-sided and applied; the examiner says no separate judgement/conclusion is required for Assess.','IGCSE/4EC1_Economics/May_2023/4EC1_Economics_May_2023_P1R_ER.pdf','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/Economics/2017/Exam-materials/4ec1-01r-pef-20230824.pdf'],
 ['12','Evaluate the extent to which derived demand affects demand for labour','June 2023 P1R Q4(c)','Official examiner-report script: 11/12','Printed report p. 38; source PDF path in archive','Not full marks. Balanced argument and supported conclusion; examiner notes organisation/application were not excellent.','IGCSE/4EC1_Economics/May_2023/4EC1_Economics_May_2023_P1R_ER.pdf','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/Economics/2017/Exam-materials/4ec1-01r-pef-20230824.pdf'],
]

SOURCES=[
 ['Archive corpus','42 4EC1 QPs with matching MS; 3 examiner reports in the searchable archive. The May/June 2022 P2R QP is represented by a verified recovered alternative because the original is unreadable.','Paperlords_Archive/Paperlords_Searchable_Text_Index.zip; Paperlords_Archive/Paperlords_QP_MS_ER_Pairings.csv','All PDF paths point into Paperlords_All_IGCSE_Archive_4EC1_4BS1_4EB1.zip.'], 
 ['June 2019 Paper 1 exemplars','Pearson booklet with actual candidate scripts, mark schemes and examiner commentary for 10 selected questions.','External official PDF; no local copy to conserve space.','https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Economics/2017/teaching-learning-materials/ig-economics-paper-1-exemplar-responses-with-commentaries.pdf'],
 ['June 2019 Paper 2 exemplars','Pearson booklet with actual candidate scripts, mark schemes and examiner commentary for 9 selected questions.','External official PDF; no local copy to conserve space.','https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Economics/2017/teaching-learning-materials/ig-economics-paper-2-exemplar-responses.pdf'],
 ['June 2023 examiner reports','Exact-session script commentary/marks and advice for P1R, P2 and P2R.','Use the three full report PDFs inside the Paperlords archive at the paths in the exemplar sheet.','Official Pearson report URLs are listed beside each example in the workbook.'],
]

def classify(mark:int,text:str)->str:
    t=text.lower()
    if mark==1:
        if re.search(r'select one answer|which one|multiple choice|\bwhich\b',t):return 'Select / MCQ (1)'
        if re.search(r'\bstate\b|\bidentify\b|\bname\b',t):return 'State / identify (1)'
        return 'Other one-mark item (check prompt)'
    if mark==2:
        if re.search(r'calculate|how much|percentage|ratio|balance|per capita',t):return 'Calculate (2)'
        if re.search(r'define|what is meant',t):return 'Define (2)'
        if re.search(r'describe|outline|explain',t):return 'Describe / explain one (2)'
        return 'Other two-mark item (check prompt)'
    if mark==3:
        if re.search(r'draw|label|diagram|pie chart|curve',t):return 'Draw and label diagram (3)'
        return 'Explain one (3)'
    if mark==6:return 'Analyse (6)'
    if mark==9:return 'Assess (9)'
    if mark==12:return 'Evaluate (12)'
    return f'{mark}-mark item'

def find_excerpt(lines:list[str],start:int,end:int,mark:int)->str:
    text=re.sub(r'\s+',' ',' '.join(lines[start+1:end])).strip()
    prefer={
      1:r'\b(?:Define|State|Identify|Which one|Which|What|How much|How|Calculate|Give|Name)\b',
      2:r'\b(?:Calculate|Define|What is meant|Describe|Outline|Explain)\b',
      3:r'\b(?:Explain|Describe|draw|Using the diagram|On the blank)\b',
      6:r'\b(?:Analyse|Analyze)\b',9:r'\bAssess\b',12:r'\bEvaluate\b'}
    matches=list(re.finditer(prefer[mark],text,re.I))
    if matches:text=text[matches[0].start():]
    text=re.sub(r'\bDO NOT WRITE.*$','',text,flags=re.I)
    text=re.sub(r'\bTOTAL FOR PAPER.*$','',text,flags=re.I)
    return text[:620].strip()

def style(ws,widths):
    ws.freeze_panes='A2';ws.auto_filter.ref=ws.dimensions
    ws.row_dimensions[1].height=32
    for c in ws[1]:
        c.font=Font(bold=True,color='FFFFFF');c.fill=PatternFill('solid',fgColor='24476B');c.alignment=Alignment(wrap_text=True,vertical='center')
    for row in ws.iter_rows(min_row=2):
        for c in row:c.alignment=Alignment(wrap_text=True,vertical='top')
    for col,width in widths.items():ws.column_dimensions[col].width=width

def add_table(ws,name):
    t=Table(displayName=name,ref=ws.dimensions)
    t.tableStyleInfo=TableStyleInfo(name='TableStyleMedium2',showRowStripes=True,showColumnStripes=False,showFirstColumn=False,showLastColumn=False)
    ws.add_table(t)

def build_items():
    # Use the recovered readable QP for May/June 2022 P2R in place of the
    # unreadable Paperlords QP; pair it with the original matching MS.
    records={}
    with PAIRINGS.open(encoding='utf-8-sig',newline='') as f:
        for r in csv.DictReader(f):
            if r.get('Subject')=='Economics' and r.get('Course code')=='4EC1':
                text_path=r.get('QP text path','')
                pdf_path=r.get('QP PDF path','')
                if r.get('Recovered QP text path'):
                    text_path=r['Recovered QP text path']
                    pdf_path=r['Recovered QP PDF path']
                records[text_path]={'qp_pdf':pdf_path,'ms_pdf':r.get('MS PDF path','')}
    items=[]
    with zipfile.ZipFile(INDEX_ZIP) as z:
        for name,paths in records.items():
            raw=z.read(name).decode('utf-8','replace');head={}
            for key in ('SESSION','PAPER'):
                m=re.search(rf'^{re.escape(key)}:\s*(.+)$',raw,re.M);head[key]=m.group(1).strip() if m else ''
            split=re.split(r'(?m)^===== PAGE (\d+) / (\d+) =====\s*$',raw)
            for k in range(1,len(split)-2,3):
                page=split[k];lines=split[k+2].splitlines();prev=-1
                for i,line in enumerate(lines):
                    m=MARK_LINE.fullmatch(line)
                    if not m:continue
                    mark=int(m.group(1));excerpt=find_excerpt(lines,prev,i,mark)
                    typ=classify(mark,' '.join([excerpt]+lines[i+1:min(len(lines),i+4)]))
                    items.append({'Session':head.get('SESSION',''),'Paper':head.get('PAPER',''),'Mark value':mark,'Detected type':typ,'Page in QP':page,'Prompt/context excerpt (text extraction)':excerpt,'QP PDF path inside full ZIP':paths['qp_pdf'],'Matching MS PDF path inside full ZIP':paths['ms_pdf']})
                    prev=i
    return items

def main():
    BANK.mkdir(parents=True,exist_ok=True);items=build_items()
    wb=Workbook();ws=wb.active;ws.title='Question families'
    ws.append(['Marks','Command/family','What the question looks like','High-yield answer shape','Archive examples'])
    for r in TYPE_ROWS:ws.append(r)
    style(ws,{'A':10,'B':34,'C':68,'D':78,'E':60});add_table(ws,'FamiliesTable')
    wp=wb.create_sheet('Prompt pattern map');wp.append(['Marks','Prompt pattern','What is asked','High-yield response','Archive examples'])
    for r in PATTERNS:wp.append(r)
    style(wp,{'A':10,'B':50,'C':72,'D':80,'E':62});add_table(wp,'PatternTable')
    wi=wb.create_sheet('All QP items');cols=list(items[0].keys());wi.append(cols)
    for x in items:wi.append([x[c] for c in cols])
    style(wi,{'A':20,'B':12,'C':12,'D':32,'E':13,'F':90,'G':82,'H':82});add_table(wi,'ItemsTable')
    we=wb.create_sheet('Official exemplars');we.append(['Marks','Question / prompt','Series / question','Published score','Source page(s)','Examiner takeaway','Local archive path / source','Official source URL'])
    for r in EXEMPLARS:we.append(r)
    style(we,{'A':10,'B':52,'C':34,'D':35,'E':36,'F':80,'G':86,'H':94});add_table(we,'ExemplarsTable')
    wsrc=wb.create_sheet('Sources & scope');wsrc.append(['Source','What it contains','Local location / storage note','Official URL / access note'])
    for r in SOURCES:wsrc.append(r)
    style(wsrc,{'A':34,'B':84,'C':90,'D':108});add_table(wsrc,'SourcesTable')
    wb.save(OUT)
    print('Built',len(items),'items from',len({x['QP PDF path inside full ZIP'] for x in items}),'QPs; counts',dict(sorted(Counter(x['Mark value'] for x in items).items())),'bytes',OUT.stat().st_size)

if __name__=='__main__':main()
