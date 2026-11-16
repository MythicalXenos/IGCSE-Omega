"""LAYER D: for every session/paper, do the mark scheme and the question paper
name the SAME business?

The June 2026 P1 pair does not: the QP is about 'Crumb' and the MS is about
'Violet Cakes' (same story - cake business, French chocolate, celebrity wedding
cakes - different name). A renamed case would silently corrupt every AO2 claim
in the bank, because AO2 is 'apply to the business'.

Method: collect capitalised non-sentence-initial tokens appearing >=5 times in
each document, subtract the shared vocabulary, and report the names that appear
in only one of the two.
"""
import pathlib
import re
import collections
import pypdf

BASE = pathlib.Path('/home/user/IGCSE-Omega/Paperlords_Archive/IGCSE/4BS1_Business_Studies')
STOP = set("""The This That These Those There Their They Then When What Which While With
Within Without Some Such Sales Revenue Profit Business Market Customer Customers
Paper Question Number Mark Scheme Award Credit Accept Allow Ignore Reject Total
Pearson Edexcel International GCSE Business Studies Summer June November October
Candidates Candidate Answer Answers Level Levels Descriptor Demonstrates Apply
Knowledge Understanding Analysis Evaluation Application Marks Marking Guidance
Effective Limited Sound Good Clear Detailed Mostly Accurate Elements Relevant
However Therefore Because Also Although Wording Questions Fig Figure Table Source
Sources Unit Price Cost Costs Cash Flow Forecast Budget Break Even Margin Ratio
Facebook Instagram Twitter YouTube Online Website App Apps CEO HR CCTV UK USA
For Example One Two Three Four Five Six Seven Eight Nine Ten First Second Third
January February March April May July August September December Week Weeks Day
Days Year Years Month Months Monday Tuesday Wednesday Thursday Friday Saturday
Sunday High Low New Old More Most Less Least Best Worst Small Large Big Long
Short Term Terms Time Times Employee Employees Staff Worker Workers Manager
Managers Owner Owners Team Group Chief Executive Managing Director Directors
Company Companies Ltd Partnership Sole Trader Franchise Franchisee Franchisor
Income Statement Balance Sheet Assets Liabilities Capital Equity Dividend
Dividends Interest Rate Rates Loan Loans Bank Banks Overdraft Mortgage
Potential Existing Current Future Local National Global Worldwide International
Increase Decrease Rise Fall Growth Decline Demand Supply Stock Stocks Product
Products Service Services Quality Price Prices Value Money Payment Payments
During Before After Around Between Off Out Over Under Same Other Others Each
Every Both Either Neither Many Much Most Only Own Part Whole All Any Few""".split())


def doc_text(p):
    return ' '.join(' '.join((pg.extract_text() or '').split())
                    for pg in pypdf.PdfReader(str(p)).pages)


def name_set(t, thresh=5):
    # a "name" token: Capitalised, not ALL-CAPS, not sentence-initial-looking
    toks = re.findall(r"(?<![.!?]\s)(?<!^)\b([A-Z][a-z]{2,})\b", t)
    c = collections.Counter(toks)
    return {w for w, n in c.items() if n >= thresh and w not in STOP}


def main():
    print(f'{"session":14s} {"pap":4s}  MS-only names            | QP-only names')
    print('-' * 100)
    issues = []
    for folder in sorted(p for p in BASE.iterdir() if p.is_dir()):
        for paper in ['P1', 'P1R', 'P2', 'P2R']:
            ms = folder / f'4BS1_Business_Studies_{folder.name}_{paper}_MS.pdf'
            qp = folder / f'4BS1_Business_Studies_{folder.name}_{paper}_QP.pdf'
            if not (ms.exists() and qp.exists()):
                continue
            try:
                m, q = name_set(doc_text(ms)), name_set(doc_text(qp))
            except Exception as e:
                print(f'{folder.name:14s} {paper:4s}  ERROR {e}')
                continue
            ms_only = sorted(m - q)
            qp_only = sorted(q - m)
            flag = '  <<< CASE MISMATCH' if ms_only and qp_only else ''
            if flag:
                issues.append((folder.name, paper, ms_only, qp_only))
            print(f'{folder.name:14s} {paper:4s}  {", ".join(ms_only)[:40]:40s}| {", ".join(qp_only)[:40]}{flag}')
    print('\nFLAGGED:', len(issues))
    for s, p, a, b in issues:
        print(f'   {s} {p}: MS-only {a}  ||  QP-only {b}')


if __name__ == '__main__':
    main()
