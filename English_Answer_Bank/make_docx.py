from __future__ import annotations
import re
from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

BASE=Path(__file__).resolve().parent
MD=BASE/'4EB1_Exemplar_and_Model_Answer_Guide.md'
OUT=BASE/'4EB1_Exemplar_and_Model_Answer_Guide.docx'

def clean_inline(s:str)->str:
    s=re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',r'\1 — \2',s)
    s=s.replace('**','').replace('__','').replace('`','')
    s=s.replace('*','')
    return s.strip()

def shade(cell, fill):
    tcPr=cell._tc.get_or_add_tcPr()
    shd=OxmlElement('w:shd'); shd.set(qn('w:fill'),fill); tcPr.append(shd)

def set_cell_text(cell,text,bold=False,color=None):
    cell.text=''
    p=cell.paragraphs[0]
    p.paragraph_format.space_after=Pt(2)
    run=p.add_run(clean_inline(text))
    run.bold=bold
    if color:run.font.color.rgb=RGBColor(*color)
    run.font.size=Pt(8.5)
    cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.TOP

def is_table_line(line):
    return line.strip().startswith('|') and line.strip().endswith('|')

def parse_table(lines, i, doc):
    raw=[]
    while i<len(lines) and is_table_line(lines[i]):
        raw.append(lines[i].strip())
        i+=1
    rows=[]
    for line in raw:
        cells=[c.strip() for c in line.strip('|').split('|')]
        if all(re.fullmatch(r':?-{3,}:?',c or '-') for c in cells):
            continue
        rows.append(cells)
    if rows:
        cols=max(len(r) for r in rows)
        table=doc.add_table(rows=1,cols=cols)
        table.alignment=WD_TABLE_ALIGNMENT.CENTER
        table.style='Table Grid'
        for j in range(cols):
            txt=rows[0][j] if j<len(rows[0]) else ''
            set_cell_text(table.rows[0].cells[j],txt,bold=True,color=(255,255,255))
            shade(table.rows[0].cells[j],'24476B')
        for r in rows[1:]:
            cells=table.add_row().cells
            for j in range(cols):
                txt=r[j] if j<len(r) else ''
                set_cell_text(cells[j],txt)
        doc.add_paragraph().paragraph_format.space_after=Pt(0)
    return i

def main():
    lines=MD.read_text(encoding='utf-8').splitlines()
    doc=Document()
    section=doc.sections[0]
    section.top_margin=Inches(.65); section.bottom_margin=Inches(.65)
    section.left_margin=Inches(.78); section.right_margin=Inches(.78)
    styles=doc.styles
    styles['Normal'].font.name='Aptos'
    styles['Normal'].font.size=Pt(10)
    styles['Normal'].paragraph_format.space_after=Pt(5)
    for nm,size,col in [('Title',24,'17365D'),('Heading 1',17,'17365D'),('Heading 2',13,'24527A'),('Heading 3',11,'287070')]:
        st=styles[nm]; st.font.name='Aptos Display'; st.font.size=Pt(size); st.font.bold=True; st.font.color.rgb=RGBColor.from_string(col)
        st.paragraph_format.space_before=Pt(10); st.paragraph_format.space_after=Pt(4)
    # header/footer
    hp=section.header.paragraphs[0]
    hp.text='4EB1 English Language B • Official exemplars and model answers'
    hp.style='Caption'; hp.alignment=WD_ALIGN_PARAGRAPH.RIGHT
    fp=section.footer.paragraphs[0]
    fp.alignment=WD_ALIGN_PARAGRAPH.CENTER
    fp.add_run('Study reference • 4EB1 • ')
    fld=OxmlElement('w:fldSimple'); fld.set(qn('w:instr'),'PAGE'); fp._p.append(fld)

    i=0
    while i<len(lines):
        line=lines[i].strip()
        if not line:
            i+=1; continue
        if is_table_line(lines[i]):
            i=parse_table(lines,i,doc);continue
        if line.startswith('# '):
            p=doc.add_paragraph(style='Title');p.add_run(clean_inline(line[2:]));i+=1;continue
        if line.startswith('## '):
            doc.add_heading(clean_inline(line[3:]),level=1);i+=1;continue
        if line.startswith('### '):
            doc.add_heading(clean_inline(line[4:]),level=2);i+=1;continue
        if line.startswith('#### '):
            doc.add_heading(clean_inline(line[5:]),level=3);i+=1;continue
        if line.startswith('> '):
            p=doc.add_paragraph(style='Quote');p.paragraph_format.left_indent=Inches(.2)
            r=p.add_run(clean_inline(line[2:]));r.italic=True;r.font.color.rgb=RGBColor(55,75,95)
            i+=1;continue
        if line.startswith('- '):
            p=doc.add_paragraph(style='List Bullet');p.add_run(clean_inline(line[2:]));i+=1;continue
        if re.match(r'^\d+\.\s+',line):
            p=doc.add_paragraph(style='List Number');p.add_run(clean_inline(re.sub(r'^\d+\.\s+','',line)));i+=1;continue
        # Join wrapped Markdown paragraph lines until a structural break.
        parts=[line];i+=1
        while i<len(lines):
            nxt=lines[i].strip()
            if (not nxt or nxt.startswith('#') or nxt.startswith('> ') or nxt.startswith('- ') or re.match(r'^\d+\.\s+',nxt) or is_table_line(lines[i])):break
            parts.append(nxt);i+=1
        txt=clean_inline(' '.join(parts))
        p=doc.add_paragraph()
        p.add_run(txt)
        # Make source labels easy to spot.
        if txt.startswith('[VERIFIED CANDIDATE EXEMPLAR]') or txt.startswith('[OFFICIAL MARK-SCHEME WORKED ANSWER]') or txt.startswith('[CONSTRUCTED GRADE 9 TARGET]') or txt.startswith('OFFICIAL') or txt.startswith('CONSTRUCTED') or txt.startswith('Question type:'):
            p.paragraph_format.keep_with_next=True
    doc.core_properties.title='4EB1 Official Exemplar and Model Answer Guide'
    doc.core_properties.subject='Pearson Edexcel International GCSE English Language B question types and answer exemplars'
    doc.core_properties.author='Arena.ai Agent Mode'
    doc.save(OUT)
    print('saved',OUT,'bytes',OUT.stat().st_size)

if __name__=='__main__':main()
