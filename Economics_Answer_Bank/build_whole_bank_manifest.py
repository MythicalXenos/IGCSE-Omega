import sys,csv,json,re,urllib.parse
from pathlib import Path
sys.path.insert(0,'Economics_Answer_Bank');import build_paper1_qa_bank as parser
ROOT=Path('.'); archive=ROOT/'Paperlords_Archive'; bank=ROOT/'Economics_Answer_Bank'
rows=list(csv.DictReader(open(archive/'Paperlords_QP_MS_ER_Pairings.csv',encoding='utf-8-sig')))
rows=[r for r in rows if r['Subject']=='Economics']
def norm(s):return re.sub(r'[^a-z0-9]','',s.lower())
def sessnorm(s):
 s=s.lower().replace('mayjune','may-june').replace('jan ','january ').replace('nov ','november ').replace('june ','june ').replace('may ','may ')
 s=re.sub(r'\s+',' ',s.strip())
 return norm(s)
def findpair(sess,paper):
 for r in rows:
  if r['Paper']==paper and sessnorm(r['Session'])==sessnorm(sess):return r
 return None
out=[]
def add(sess,paper,item,source,source_type):
 r=findpair(sess,paper)
 localqp=source.get('qp','');localms=source.get('ms','')
 if r:
  qpurl=r['Paperlords QP URL'];msurl=r['Paperlords MS URL']; erurl=r['ER source URL(s)']
  qp_local=str(archive/r['QP PDF path']); ms_local=str(archive/r['MS PDF path']); er_local='; '.join(str(archive/x) for x in r['ER PDF path(s)'].split(';') if x)
  if r['Recovered QP PDF path']:
   qp_local=str(archive/r['Recovered QP PDF path']); qpurl=r['Recovered QP URL'] or qpurl
  provenance='Archive QP/MS pairing register'
 else:
  qp_local=str(ROOT/localqp) if localqp else ''
  ms_local=str(ROOT/localms) if localms and not localms.startswith('http') else ''
  qpurl='';msurl=localms if localms.startswith('http') else '';erurl=''
  er_local=''
  provenance=source.get('source_note','Outside archive pairing register')
 # links are exact source URLs as supplied; spaces are encoded for readability
 safe=lambda x: urllib.parse.quote(x,safe=':/?&=%#') if x else ''
 qloc=item.get('source_locator',{})
 ans=item.get('answer','')
 out.append({
 'paper_group':'Paper 1/P1R' if paper in ('P1','P1R') else 'Paper 2/P2R',
 'session':sess,'paper':paper,'variant':'R' if paper.endswith('R') else 'standard',
 'reference':f"4EC1 {paper} {sess} Q{item['q']}({item['part']})",
 'q':item['q'],'part':item['part'],'marks':item['marks'],'prompt_text':item['text'],
 'specification_topic':'PENDING_CLASSIFICATION','subtopic':'PENDING_CLASSIFICATION',
 'reasoning_skill_family':'PENDING_CLASSIFICATION','command_word':'PENDING_CLASSIFICATION_AND_STEM_CHECK',
 'source_check_status':'PENDING_WHOLE_BANK_VISUAL_SOURCE_CHECK',
 'qp_pdf_page':qloc.get('qp_pdf_page',''),'ms_pdf_page':qloc.get('ms_pdf_page',''),
 'qp_local_path':qp_local,'ms_local_path':ms_local,'er_local_path':er_local,
 'qp_source_url':safe(qpurl),'ms_source_url':safe(msurl),'er_source_url':safe(erurl),
 'source_provenance':provenance,'answer_or_ms_extract':ans,
 'extraction_note':'P1/P1R from existing JSON bank; P2/P2R PDF text extraction. Text/layout and diagram-only items need visual source check; page locators are navigation aids, not identity proof.' if source_type=='P2' else 'Existing P1/P1R bank item. Preserve that bank’s own source notes and locator caveats; visually audit before using as definitive classification.'
 })
for p in json.load(open(bank/'Paper1_QA_Bank.json',encoding='utf-8')):
  for i in p['items']: add(p['session'],p['paper'],i,p,'P1')
for r in rows:
 if r['Paper'] not in ('P2','P2R'):continue
 qp=archive/r['QP PDF path']
 if r['Session']=='MayJune 2022' and r['Paper']=='P2R':qp=archive/'RECOVERED_ALTERNATIVES/4EC1_Economics_June_2022_P2R_QP_alternative.pdf'
 ms=archive/r['MS PDF path']; mskeys=parser.parse_ms(ms)
 for i in parser.parse_qp(qp):
  i['answer']=mskeys.get(f"{i['q']}{i['part']}",'')
  add(r['Session'],r['Paper'],i,{'qp':str(qp),'ms':str(ms)},'P2')
# deterministic order
out.sort(key=lambda x:(x['paper_group'],x['session'],x['paper'],x['q'],x['part']))
path=bank/'Whole_Bank_Question_Manifest.csv'
with open(path,'w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=out[0].keys(),lineterminator='\n');w.writeheader()
 for row in out:
  cleaned={k:'\n'.join(line.rstrip() for line in str(v).splitlines()) for k,v in row.items()}
  w.writerow(cleaned)
print(path,len(out),'records',sum(x['marks'] for x in out),'marks')
from collections import Counter
print(Counter(x['paper_group'] for x in out))
