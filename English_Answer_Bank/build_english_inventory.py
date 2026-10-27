#!/usr/bin/env python3
"""Build the 4EB1 question-pattern workbook from the local searchable index."""
import csv
import re
import zipfile
from collections import Counter
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.worksheet.table import Table, TableStyleInfo

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / 'Paperlords_Archive'
INDEX_ZIP = ARCHIVE / 'Paperlords_Searchable_Text_Index.zip'
PAIRINGS = ARCHIVE / 'Paperlords_QP_MS_ER_Pairings.csv'
BANK = ROOT / 'English_Answer_Bank'
OUT = BANK / '4EB1_Question_Type_Inventory.xlsx'
ANSWER_COVERAGE = BANK / 'Answer_Sets' / 'coverage.csv'

PATTERNS = [
    ['1','Short retrieval','Use the stated line range; state/identify one relevant fact.','Read the line reference first. Give one direct, specific answer and stop. Do not analyse language or add several alternatives.','Q1, Q2 or Q4 across the archive; Q1/Q2/Q4 are usually 1 mark each.'],
    ['2','Short retrieval','Find two points/details from the stated lines (usually Q5).','Write two separate, precise details from the correct lines. Check that each detail answers the exact question.','Q5 across the archive; 2 marks.'],
    ['3','Language and structure analysis','Explain how the writer presents an idea, impression or experience.','Make a point about a writer’s choice; use a short quotation; zoom in on a word/structural choice; explain its effect and link it to the question. Select a few rich examples instead of listing devices.','10 marks; e.g. June 2023 P1 Q3 (outside) or Q6 (walk).'],
    ['4','Short retrieval','Identify one difficulty, reason, piece of advice or fact from the stated lines.','Give one point within the specified range. Do not use information from elsewhere in the text.','Q4 across the archive; 1 mark.'],
    ['5','Two-detail retrieval','Name/state two experiences, effects or details from a specified passage.','Give two distinct details, normally one per line/bullet. Do not repeat the same idea in different words.','Q5 across the archive; 2 marks.'],
    ['6','Language and structure analysis','Explain how a writer presents ideas or experiences in Text Two.','Use the same analytical chain as Q3: point → brief reference → precise method/word → effect/meaning. Cover the passage rather than retelling it.','10 marks; e.g. June 2023 P1 Q6 (a walk).'],
    ['7','Comparison of ideas and perspectives','Compare how both writers present their ideas/perspectives.','Compare throughout, not as two separate summaries. Pair a point from each text, support both with brief references, and explain what the contrast/similarity reveals about viewpoint, purpose or tone.','15 marks; both texts and balanced references are essential.'],
    ['8','Reading-to-writing / audience task','Use ideas from both texts for a named audience/purpose. From November 2025 onward, Issue 4 forms are article for a school/college magazine or website, speech/talk to peers, website contribution, or letter.','Plan all required bullets; adapt ideas from both texts; sustain the specified form, tone and register; use clear paragraphs and accurate sentences. Check the series before applying the post-November-2025 form restriction to older papers.','30 marks: AO1 10, AO4 12, AO5 8.'],
    ['9','Discursive / argumentative writing','Respond to a statement with a discussion, argument or considered viewpoint.','Take a clear position; develop reasons and examples; acknowledge a credible counterpoint; end with a reasoned view. Keep paragraphs purposeful and avoid repeating the claim.','30 marks: AO4 20, AO5 10.'],
    ['10','Narrative writing','Write a true or imaginary story to a given title.','Build around one central decision/problem/change. Plan a clear opening, turning point and ending; control time and viewpoint; use dialogue/details only when they move the story.','30 marks: AO4 20, AO5 10.'],
    ['11','Descriptive writing','Describe a person, place, object, experience or view.','Keep the focus descriptive rather than turning it into a plot. Organise details by viewpoint or senses; use precise nouns/verbs and varied sentence lengths; choose imagery that fits the mood.','30 marks: AO4 20, AO5 10.'],
]

EXEMPLARS = [
    ['10','Language analysis: writer’s ideas about spending time outdoors','June 2023 P1 Q3','9/10, Level 5 (not full marks)','Examiner report, printed p. 10; candidate response shown pp. 7–9','Discriminating references and perceptive understanding, but not enough analysis for 10/10. Useful near-full calibration.','IGCSE/4EB1_English_Language_B/May-June_2023/4EB1_English_Language_B_May-June_2023_P1_ER.pdf','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/English-Language-B/2016/Exam-materials/4eb1-01-pef-20230824.pdf'],
    ['10','Language analysis: writer’s experiences of a walk','June 2023 P1 Q6','10/10, Level 5 (full marks)','Examiner report, printed p. 20; script shown pp. 17–19','Explores language and structure throughout; short references are embedded to clarify analysis.','IGCSE/4EB1_English_Language_B/May-June_2023/4EB1_English_Language_B_May-June_2023_P1_ER.pdf','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/English-Language-B/2016/Exam-materials/4eb1-01-pef-20230824.pdf'],
    ['15','Compare both writers’ ideas and perspectives about being outdoors','June 2023 P1 Q7','15/15, Level 5 (full marks)','Examiner report, printed p. 30; script shown pp. 25–29','Comprehensive comparisons, balanced references and analysis of the writers’ perspectives; compares throughout.','IGCSE/4EB1_English_Language_B/May-June_2023/4EB1_English_Language_B_May-June_2023_P1_ER.pdf','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/English-Language-B/2016/Exam-materials/4eb1-01-pef-20230824.pdf'],
    ['10','Language analysis: writer’s ideas about Ben Francis and Gymshark','June 2023 P1R Q3','8/10, Level 4 (not full marks)','Examiner report, printed p. 10; script shown pp. 7–9','Thorough understanding/exploration; good range including positive language, statistics and dialogue, with detailed references.','IGCSE/4EB1_English_Language_B/May-June_2023/4EB1_English_Language_B_May-June_2023_P1R_ER.pdf','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/English-Language-B/2016/Exam-materials/4eb1-01r-pef-20230824.pdf'],
    ['30','Talk to peers about walking/getting outside; three required bullet points','June 2023 P1 Q8','AO1 10/10 + AO4 12/12 + AO5 8/8 = 30/30 (full marks)','Examiner report, printed p. 40; script shown pp. 36–39','All bullets are covered in detail; the response keeps a sharp focus on purpose and audience.','IGCSE/4EB1_English_Language_B/May-June_2023/4EB1_English_Language_B_May-June_2023_P1_ER.pdf','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/English-Language-B/2016/Exam-materials/4eb1-01-pef-20230824.pdf'],
    ['30','Discuss “Fresh air and exercise are the keys to happiness.”','June 2023 P1 Q9','AO4 11/20 + AO5 6/10 = 17/30 (not full marks)','Examiner report, printed p. 48; script shown pp. 45–47','Useful mid-level calibration for a discursive answer; the report points to development and more persuasive control as improvement routes.','IGCSE/4EB1_English_Language_B/May-June_2023/4EB1_English_Language_B_May-June_2023_P1_ER.pdf','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/English-Language-B/2016/Exam-materials/4eb1-01-pef-20230824.pdf'],
    ['30','Story entitled “A Difficult Decision”','June 2023 P1 Q10','AO4 20/20 + AO5 10/10 = 30/30 (full marks)','Examiner report, printed p. 55; script shown pp. 51–54','The story is tightly controlled and engaging; the report highlights its opening, narrative control and varied sentence structures.','IGCSE/4EB1_English_Language_B/May-June_2023/4EB1_English_Language_B_May-June_2023_P1_ER.pdf','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/English-Language-B/2016/Exam-materials/4eb1-01-pef-20230824.pdf'],
    ['30','Describe your favourite walk','June 2023 P1 Q11','AO4 16/20 + AO5 7/10 = 23/30 (not full marks)','Examiner report, printed p. 62; script shown pp. 58–61','A strong descriptive calibration example; the report notes clear focus, vocabulary and structure, with accuracy/control still improvable.','IGCSE/4EB1_English_Language_B/May-June_2023/4EB1_English_Language_B_May-June_2023_P1_ER.pdf','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/English-Language-B/2016/Exam-materials/4eb1-01-pef-20230824.pdf'],
    ['10','Language analysis: writer’s ideas about women in technology/work','June 2023 P1R Q6','10/10, Level 5 (full marks)','Examiner report, printed p. 19; script shown pp. 17–18','Perceptive analysis with embedded references. The published report explicitly calls this a full-mark response.','IGCSE/4EB1_English_Language_B/May-June_2023/4EB1_English_Language_B_May-June_2023_P1R_ER.pdf','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/English-Language-B/2016/Exam-materials/4eb1-01r-pef-20230824.pdf'],
    ['15','Compare both writers’ ideas and perspectives','June 2023 P1R Q7','8/15, Level 3 (lower-scoring)','Examiner report, printed p. 24; script shown pp. 22–23','Relevant comparisons and references; a wider range and further development were needed. Pearson’s reproduced script excerpt ends mid-sentence.','IGCSE/4EB1_English_Language_B/May-June_2023/4EB1_English_Language_B_May-June_2023_P1R_ER.pdf','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/English-Language-B/2016/Exam-materials/4eb1-01r-pef-20230824.pdf'],
    ['30','Talk to peers about how successful people can be an inspiration; three required bullet points','June 2023 P1R Q8','AO1 9/10 + AO4 10/12 + AO5 7/8 = 26/30 (not full marks)','Examiner report, printed p. 34; script shown pp. 30–33','Published mark is 26/30; Pearson’s reproduced script cuts off after “The” at the start of its final sentence, so do not infer how the original answer ended.','IGCSE/4EB1_English_Language_B/May-June_2023/4EB1_English_Language_B_May-June_2023_P1R_ER.pdf','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/English-Language-B/2016/Exam-materials/4eb1-01r-pef-20230824.pdf'],
    ['30','Discuss “You do not need to earn a lot of money to be successful.”','June 2023 P1R Q9','AO4 11/20 + AO5 6/10 = 17/30 (not full marks)','Examiner report, printed p. 44; script shown pp. 40–43','Mid-level calibration; the report says more development and proofreading would help.','IGCSE/4EB1_English_Language_B/May-June_2023/4EB1_English_Language_B_May-June_2023_P1R_ER.pdf','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/English-Language-B/2016/Exam-materials/4eb1-01r-pef-20230824.pdf'],
    ['30','Story entitled “The Day Everything Changed”','June 2023 P1R Q10','AO4 20/20 + AO5 10/10 = 30/30 (full marks)','Examiner report, printed p. 50; script shown pp. 47–49 (printed p. 46 is commentary)','The examiner praises the controlled structure, credible young-child viewpoint, clear title/time-frame links and varied sentences.','IGCSE/4EB1_English_Language_B/May-June_2023/4EB1_English_Language_B_May-June_2023_P1R_ER.pdf','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/English-Language-B/2016/Exam-materials/4eb1-01r-pef-20230824.pdf'],
    ['30','Describe your role model','June 2023 P1R Q11','AO4 17/20 + AO5 9/10 = 26/30 (not full marks)','Examiner report, printed p. 56; script shown pp. 53–55','A descriptive response with a clear focus and perceptive detail; remaining errors do not impede meaning.','IGCSE/4EB1_English_Language_B/May-June_2023/4EB1_English_Language_B_May-June_2023_P1R_ER.pdf','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/English-Language-B/2016/Exam-materials/4eb1-01r-pef-20230824.pdf'],
    ['10','Language analysis: writer’s relationship with Hassan','June 2025 P1R Q3','10/10, Level 5 (full marks)','Examiner report, printed p. 9; candidate response reproduced before judgement','Methodical and perceptive analysis with a wide range of judicious references; exact script not transcribed because scan OCR is unreliable.','Not present in current checkout; consult official report.','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/English-Language-B/2016/Exam-materials/4eb1-01r-pef-20250821.pdf'],
    ['10','Language analysis: writer’s friendship with Claudia','June 2025 P1R Q6','10/10, Level 5 (full marks)','Examiner report, printed p. 19; response reproduced in report','Detailed language/structure analysis and a strong focus on tone; exact script not transcribed because scan OCR is unreliable.','Not present in current checkout; consult official report.','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/English-Language-B/2016/Exam-materials/4eb1-01r-pef-20250821.pdf'],
    ['15','Compare writers’ ideas and perspectives about friendship','June 2025 P1R Q7','14/15, Level 5 (near-full, not full marks)','Examiner report, printed p. 30; response reproduced in report','Balanced references and comparisons throughout; exact script not transcribed because scan OCR is unreliable.','Not present in current checkout; consult official report.','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/English-Language-B/2016/Exam-materials/4eb1-01r-pef-20250821.pdf'],
    ['15','Compare writers’ ideas and perspectives about friendship (low-score calibration)','June 2025 P1R Q7','5/15, Level 2','Examiner report, printed p. 34; response reproduced in report','Pearson notes virtually no quotations/detailed references and undeveloped comparisons; exact script not transcribed.','Not present in current checkout; consult official report.','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/English-Language-B/2016/Exam-materials/4eb1-01r-pef-20250821.pdf'],
]

SOURCES = [
    ['Archive QPs and matching MSs','The searchable index includes 23 4EB1 QP and 23 matching MS text records; 23 local QP PDFs, 23 local MS PDFs and two June 2023 ER PDFs are present. The single full PDF collection ZIP is absent.','Paperlords_Archive/IGCSE/4EB1_English_Language_B/ plus Paperlords_Searchable_Text_Index.zip and Paperlords_QP_MS_ER_Pairings.csv.','Use local PDFs for page-image verification; June 2024–2025 ER PDFs are official online Pearson sources.'],
    ['June 2023 Source Booklet text','Separate Source Booklet PDFs are not present; the text is appended to the local QPs: P1 PDF pp. 30–34 (printed pp. 2–6) and P1R PDF pp. 30–33 (printed pp. 2–5). Candidate-script references are not treated as source-verified quotations unless a specific cross-check is recorded.','The local June 2023 P1 and P1R QP PDFs.',''],
    ['June 2023 P1 examiner report','Official candidate-response examples and examiner comments for Q3–Q11, with published scores and printed page numbers.','Paperlords_Archive/IGCSE/4EB1_English_Language_B/May-June_2023/4EB1_English_Language_B_May-June_2023_P1_ER.pdf','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/English-Language-B/2016/Exam-materials/4eb1-01-pef-20230824.pdf'],
    ['June 2023 P1R examiner report','Official candidate-response examples and examiner comments for the R variant.','Paperlords_Archive/IGCSE/4EB1_English_Language_B/May-June_2023/4EB1_English_Language_B_May-June_2023_P1R_ER.pdf','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/English-Language-B/2016/Exam-materials/4eb1-01r-pef-20230824.pdf'],
    ['Pearson June 2022 examiner report','Additional official script examples; includes a published full-mark Q6 script and assessed writing examples.','Not duplicated locally.','https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/English%20Language%20B/2016/exam-materials/4eb1-01-pef-20220825.pdf'],
    ['Pearson June 2024 P1 examiner report','Section A guidance and candidate-response examples; warns against feature-spotting, generic effects, retelling and leaving Q7 blank.','Not duplicated locally.','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/English-Language-B/2016/Exam-materials/4eb1-01-pef-20240822.pdf'],
    ['Pearson June 2024 P1R examiner report','Recent official examiner feedback and sample responses for the R variant.','Not duplicated locally.','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/English-Language-B/2016/Exam-materials/4eb1-01r-pef-20240822.pdf'],
    ['Pearson November 2024 P1 examiner report','Section A examiner feedback for Q1–Q7.','Not duplicated locally.','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/English-Language-B/2016/Exam-materials/4eb1-01-pef-20250123.pdf'],
    ['Pearson June 2025 P1 examiner report','Section A feedback; direct PDF and Jina text route consulted for this batch.','Not duplicated locally; Jina reports 63 pages.','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/English-Language-B/2016/Exam-materials/4eb1-01-pef-20250821.pdf'],
    ['Pearson June 2025 P1R examiner report','Verified 10/10 Q3 and Q6 and 14/15 Q7 candidate-response score locators; scanned wording is OCR-corrupted.','Not duplicated locally; Jina reports 67 pages.','https://qualifications.pearson.com/content/dam/pdf/International-GCSE/English-Language-B/2016/Exam-materials/4eb1-01r-pef-20250821.pdf'],
    ['Pearson 4 August 2025 specification update and Q8 writing guidance','From November 2025 onward, Q8 uses only the four Issue 4 text types: article, peer speech/talk, website contribution and letter.','See Section_A_Examiner_Research_2024-2025.md for detail.','https://qualifications.pearson.com/en/news-policy/qualifications/international-gcses/english/specification-update-international-gcse-english-language-b-4eb1-for-first-teaching-september-2025.html'],
    ['June 2026 report access check','Pearson announced release from 25 August 2026; recent materials are restricted to registered centres. No direct official 4EB1 report PDF has been verified.','See Section_A_Examiner_Research_2024-2025.md; do not infer filenames or use third-party report copies as official.','https://qualifications.pearson.com/en/news-policy/subject-updates/history/getting-ready-for-results-day-summer-2026.html'],
]


def style_sheet(ws, widths):
    ws.freeze_panes = 'A2'
    ws.sheet_view.showGridLines = False
    for c in ws[1]:
        c.font = Font(bold=True, color='FFFFFF')
        c.fill = PatternFill('solid', fgColor='17365D')
        c.alignment = Alignment(wrap_text=True, vertical='center')
    ws.row_dimensions[1].height = 34
    for col, width in widths.items():
        ws.column_dimensions[col].width = width
    for row in ws.iter_rows(min_row=2):
        for cell in row:
            cell.alignment = Alignment(wrap_text=True, vertical='top')
    if ws.max_row > 1:
        ref = f'A1:{ws.cell(ws.max_row, ws.max_column).coordinate}'
        tab = Table(displayName=re.sub(r'[^A-Za-z0-9]', '', ws.title)[:20] + 'Table', ref=ref)
        tab.tableStyleInfo = TableStyleInfo(name='TableStyleMedium2', showRowStripes=True, showColumnStripes=False, showFirstColumn=False, showLastColumn=False)
        ws.add_table(tab)


def get_q_start(seg, q):
    # OCR sometimes glues page-layout labels to the question number (DO4, AREA5),
    # or puts an option label before it (EITHER 9 / OR 10). Anchor at line start
    # so a page code such as *P72858A01928* cannot be mistaken for Q8.
    labels = r'(?:(?:AREA|THIS|DO|NOT|WRITE|IN|OR|EITHER)\s*)*'
    pat = re.compile(rf'(?im)^\s*{labels}{q}\s*(?=[A-Z“‘\"\'])')
    matches = list(pat.finditer(seg))
    return matches[0].start() if matches else None


def clean_prompt(text, q):
    text = re.sub(r'(?m)^===== PAGE .*?=====\s*$', ' ', text)
    text = re.sub(r'(?i)Total for Question\s+\d+\s*=\s*\d+\s*marks?', ' ', text)
    text = re.sub(r'(?i)TOTAL FOR SECTION [ABC]\s*=\s*\d+\s*MARKS?', ' ', text)
    text = re.sub(r'(?m)^\s*\*?[A-Z]?\d{4,}[A-Z0-9]*\*?\s*$', ' ', text)
    text = re.sub(r'\*P\d+[A-Z0-9]*\*', ' ', text)
    text = re.sub(r'\uf0a2+', ' ', text)
    # Remove long answer-space dot leaders and OCR layout labels.
    text = re.sub(r'(?m)^\s*\.{8,}.*$', ' ', text)
    text = re.sub(r'(?m)^\s*\d+\s+\.{5,}.*$', ' ', text)
    text = re.sub(r'(?m)^\s*(?:AREA|THIS|DO|NOT|WRITE|IN)\s*$', ' ', text)
    text = re.sub(r'(?i)(?:AREA|THIS|DO|NOT|WRITE|IN)\s*\.{5,}.*$', ' ', text, flags=re.M)
    text = re.sub(r'(?<![A-Za-z])(?:AREA|THIS|DO|NOT|WRITE|IN)(?=\s{2,}|\d)', ' ', text)
    text = re.sub(r'(?<=\w)(?:AREA|THIS|DO|NOT|WRITE|IN)(?=\s{2,})', ' ', text)
    text = re.sub(r'(?i)\bTurn over\b', ' ', text)
    # The printed mark label is the end of the task; drop the answer-space that follows.
    text = re.split(r'\(\s*\d{1,2}\s*\)', text, maxsplit=1)[0]
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.split(rf'(?i)\bTotal for Question\s+{q}\b', text)[0]
    return text[:850].strip(' .\t\n(')


def page_at(raw, pos):
    pages = list(re.finditer(r'(?m)^===== PAGE (\d+) / \d+ =====', raw[:pos]))
    return pages[-1].group(1) if pages else ''


def family(q):
    return {
        1: 'Short retrieval', 2: 'Short retrieval', 3: 'Language analysis',
        4: 'Short retrieval', 5: 'Two-detail retrieval', 6: 'Language analysis',
        7: 'Comparison', 8: 'Reading-to-writing', 9: 'Discursive writing',
        10: 'Narrative writing', 11: 'Descriptive writing'
    }[q]


def build_rows():
    records = []
    with PAIRINGS.open(encoding='utf-8-sig', newline='') as f:
        for r in csv.DictReader(f):
            if r.get('Subject') == 'English Language B' and r.get('Course code') == '4EB1':
                records.append(r)
    items = []
    with zipfile.ZipFile(INDEX_ZIP) as z:
        for rec in records:
            qp_text = rec['QP text path']
            raw = z.read(qp_text).decode('utf-8', 'replace')
            header = {}
            for k in ('SESSION', 'PAPER', 'PDF PATH IN COMPLETE ZIP'):
                m = re.search(rf'^{re.escape(k)}:\s*(.+)$', raw, re.M)
                header[k] = m.group(1).strip() if m else ''
            cover = re.search(r'4EB1\s*/\s*\d{2}R?', raw[:5000])
            cover_code = cover.group(0).replace(' ', '') if cover else ''
            totals = list(re.finditer(r'(?i)Total for Question\s+(\d+)\s*=\s*(\d+)\s*marks?', raw))
            last_end = 0
            for t in totals:
                q, marks = int(t.group(1)), int(t.group(2))
                seg = raw[last_end:t.start()]
                relstart = get_q_start(seg, q)
                if relstart is None:
                    prompt = '[Question stem not extracted automatically; open the linked QP.]'
                    qp_page = ''
                else:
                    absolute_start = last_end + relstart
                    prompt = clean_prompt(raw[absolute_start:t.start()], q)
                    qp_page = page_at(raw, absolute_start)
                items.append({
                    'Session': header['SESSION'],
                    'Archive paper label': header['PAPER'],
                    'Cover component code': cover_code,
                    'Question': q,
                    'Marks': marks,
                    'Section': 'A: Reading' if q <= 7 else ('B: Reading & Writing' if q == 8 else 'C: choose ONE of Q9–Q11'),
                    'Question family': family(q),
                    'Question prompt / context (text-index extract)': prompt,
                    'QP page': qp_page,
                    'QP PDF path inside full archive': rec['QP PDF path'],
                    'Matching MS PDF path inside full archive': rec['MS PDF path'],
                })
                last_end = t.end()
    return items, len(records)


def load_answer_coverage():
    coverage = {}
    with ANSWER_COVERAGE.open(encoding='utf-8-sig', newline='') as f:
        for row in csv.DictReader(f):
            key = (row['Session'].strip(), row['Archive paper label'].strip(),
                   row['Cover component code'].strip(), int(row['Question']))
            if key in coverage:
                raise ValueError(f'Duplicate answer coverage key: {key}')
            if row['Status'].strip() not in {'COMPLETE', 'PARTIAL'}:
                raise ValueError(f"Unsupported answer-set status for {key}: {row['Status']}")
            coverage[key] = row
    return coverage


def main():
    BANK.mkdir(parents=True, exist_ok=True)
    items, paper_count = build_rows()
    coverage = load_answer_coverage()
    inventory_keys = set()
    for item in items:
        key = (item['Session'], item['Archive paper label'],
               item['Cover component code'], item['Question'])
        inventory_keys.add(key)
        row = coverage.get(key)
        if row:
            item['Answer-set status'] = row['Status'].strip()
            item['Answer-set reference'] = row['Answer set file'].strip()
            item['Answer-set notes'] = row['Notes'].strip()
        else:
            item['Answer-set status'] = 'NO COMPLETE ANSWER SET RECORDED'
            item['Answer-set reference'] = ''
            item['Answer-set notes'] = ('Selected models or candidate score locators may exist elsewhere; '
                                        'complete QP/MS-specific answer-set coverage is not recorded.')
    stale_coverage = sorted(set(coverage) - inventory_keys)
    if stale_coverage:
        raise ValueError(f'Coverage entries do not match the current question inventory: {stale_coverage}')
    wb = Workbook()
    ws = wb.active
    ws.title = 'Question patterns'
    ws.append(['Q number','Pattern','Common wording / task','High-yield response shape','Marks / archive examples'])
    for row in PATTERNS:
        ws.append(row)
    style_sheet(ws, {'A':12,'B':30,'C':76,'D':88,'E':74})

    wp = wb.create_sheet('Prompt map')
    wp.append(['Q number','Section','Marks','Question family','Response method'])
    for r in PATTERNS:
        q = int(r[0]); marks = {1:1,2:1,3:10,4:1,5:2,6:10,7:15,8:30,9:30,10:30,11:30}[q]
        sec = 'A: Reading' if q <= 7 else ('B: Reading & Writing' if q == 8 else 'C: choose ONE of Q9–Q11')
        wp.append([q, sec, marks, r[1], r[3]])
    wp.append(['','Paper structure','100 marks answered','Section A = 40; Section B = 30; Section C = choose one of Q9, Q10 or Q11 (30).','The inventory includes all three Section C options for practice; candidates answer only one.'])
    style_sheet(wp, {'A':12,'B':34,'C':26,'D':36,'E':100})

    wi = wb.create_sheet('All QP questions')
    wi.append(list(items[0].keys()))
    for item in items:
        wi.append(list(item.values()))
    style_sheet(wi, {'A':20,'B':18,'C':20,'D':12,'E':10,'F':36,'G':30,'H':100,'I':12,'J':88,'K':88,'L':34,'M':54,'N':100})

    we = wb.create_sheet('Official student scripts')
    we.append(['Marks available','Question type / task','Series / paper / question','Published score','Official report page(s)','Examiner commentary / lesson','Local archive path','Pearson source URL','Evidence label / transcript status'])
    transcript_status = {
        'June 2023 P1 Q3': '[VERIFIED CANDIDATE EXEMPLAR] — facsimile-checked transcription in Verified_Candidate_Responses/June_2023_Section_A.md; uncertain/crossed-out wording is flagged.',
        'June 2023 P1 Q6': '[VERIFIED CANDIDATE EXEMPLAR] — facsimile-checked transcription in Verified_Candidate_Responses/June_2023_Section_A.md; uncertain/crossed-out wording is flagged.',
        'June 2023 P1 Q7': '[VERIFIED CANDIDATE EXEMPLAR] — facsimile-checked transcription in Verified_Candidate_Responses/June_2023_Section_A.md; uncertain/crossed-out wording is flagged.',
        'June 2023 P1 Q8': '[VERIFIED CANDIDATE EXEMPLAR] — facsimile-checked full transcription in Verified_Candidate_Responses/June_2023_Section_A.md; Pearson awarded 30/30.',
        'June 2023 P1 Q9': '[VERIFIED CANDIDATE EXEMPLAR] — facsimile-checked full transcription in Verified_Candidate_Responses/June_2023_Section_A.md; lower score (17/30; AO4 and AO5 Level 3) retained.',
        'June 2023 P1 Q10': '[VERIFIED CANDIDATE EXEMPLAR] — full transcription line-by-line checked against the facsimile in Verified_Candidate_Responses/June_2023_Section_A.md; Pearson awarded 30/30 (AO4 and AO5 Level 5); crossed-out wording and uncertain revisions are flagged.',
        'June 2023 P1R Q10': '[VERIFIED CANDIDATE EXEMPLAR] — full transcription line-by-line checked against the facsimile in Verified_Candidate_Responses/June_2023_Section_A.md; Pearson awarded 30/30 (AO4 and AO5 Level 5); script begins on printed p. 47, not p. 46, and revisions/uncertainty are flagged.',
        'June 2023 P1 Q11': '[VERIFIED CANDIDATE EXEMPLAR] — facsimile-checked transcription in Verified_Candidate_Responses/June_2023_Section_A.md; lower score (23/30; AO4 Level 4 and AO5 Level 4) retained; uncertain/crossed-out wording flagged.',
        'June 2023 P1R Q11': '[VERIFIED CANDIDATE EXEMPLAR] — facsimile-checked transcription in Verified_Candidate_Responses/June_2023_Section_A.md; lower than full marks (26/30; AO4 and AO5 Level 5) retained; revisions/uncertain wording flagged.',
        'June 2023 P1R Q3': '[VERIFIED CANDIDATE EXEMPLAR] — facsimile-checked transcription in Verified_Candidate_Responses/June_2023_Section_A.md; lower score retained and uncertain wording flagged.',
        'June 2023 P1R Q6': '[VERIFIED CANDIDATE EXEMPLAR] — facsimile-checked excerpt transcription in Verified_Candidate_Responses/June_2023_Section_A.md; Pearson’s reproduction stops at an incomplete phrase.',
        'June 2023 P1R Q7': '[VERIFIED CANDIDATE EXEMPLAR] — facsimile-checked excerpt transcription in Verified_Candidate_Responses/June_2023_Section_A.md; 8/15 retained and Pearson’s reproduction ends mid-sentence.',
        'June 2023 P1R Q8': '[VERIFIED CANDIDATE EXEMPLAR] — facsimile-checked excerpt transcription in Verified_Candidate_Responses/June_2023_Section_A.md; 26/30 retained and Pearson’s reproduction ends mid-sentence at “The”.',
        'June 2023 P1R Q9': '[VERIFIED CANDIDATE EXEMPLAR] — facsimile-checked full transcription in Verified_Candidate_Responses/June_2023_Section_A.md; lower score (17/30; AO4 and AO5 Level 3) retained and uncertain handwriting flagged.',
    }
    for row in EXEMPLARS:
        status = transcript_status.get(row[2], '[VERIFIED CANDIDATE EXEMPLAR] — Pearson score/page locator; exact script wording is not transcribed here.')
        we.append(row + [status])
    style_sheet(we, {'A':16,'B':62,'C':30,'D':38,'E':56,'F':100,'G':92,'H':110,'I':100})

    wsrc = wb.create_sheet('Sources & scope')
    wsrc.append(['Source','What it contains','Workspace location / note','Public source'])
    for row in SOURCES:
        wsrc.append(row)
    wsrc.append(['June 2026 archive labels','The archive labels the two June 2026 QPs as P1 and P2. Their cover codes are 4EB1/01R and 4EB1/01 respectively; P2 is a filename/archive label, not a separate qualification component.','Check the “Cover component code” column alongside archive label.',''])
    wsrc.append(['Evidence standard','[VERIFIED CANDIDATE EXEMPLAR] requires Pearson-confirmed exact response, score, session, paper, question and report page. [OFFICIAL MARK-SCHEME WORKED ANSWER] uses indicative content, not a scored script. [CONSTRUCTED GRADE 9 TARGET] is original, not official/scored, and claims no mark. Full marks means every mark available; distinguish near-full. Do not reconstruct scanned wording from corrupt OCR.','See README.md and Project_Status.md.',''])
    wsrc.append(['Current PDF availability','23 QPs, 23 matching MSs and two June 2023 ER PDFs are present individually under Paperlords_Archive/IGCSE/4EB1_English_Language_B/; the full-collection ZIP is absent.','June 2024–2025 ER PDFs remain official online Pearson sources, not local files.',''])
    wsrc.append(['Coverage count',f'{paper_count} QPs; {len(items)} question-option entries. Q9–Q11 are mutually exclusive options; the workbook indexes all three.','All question prompts are matched to their archive QP and MS paths.',''])
    complete_answer_sets = sum(1 for item in items if item['Answer-set status'] == 'COMPLETE')
    wsrc.append(['Answer-set coverage',f'{complete_answer_sets} of {len(items)} indexed question-option entries currently have a complete answer-set record. Inventory rows without COMPLETE are not claims that no model or exemplar exists; they are not yet in a complete QP/MS-specific answer set.','See Answer_Sets/README.md and Answer_Sets/coverage.csv; per-question fields are on the All QP questions sheet.',''])
    style_sheet(wsrc, {'A':34,'B':92,'C':100,'D':110})

    wb.save(OUT)
    print('Built', len(items), 'question entries from', paper_count, 'QP/MS pairs; pattern counts', dict(sorted(Counter(i['Question family'] for i in items).items())), 'bytes', OUT.stat().st_size)
    missing = [i for i in items if i['Question prompt / context (text-index extract)'].startswith('[Question stem')]
    if missing:
        print('Question prompts needing manual PDF lookup:', [(i['Session'],i['Archive paper label'],i['Question']) for i in missing])

if __name__ == '__main__':
    main()
