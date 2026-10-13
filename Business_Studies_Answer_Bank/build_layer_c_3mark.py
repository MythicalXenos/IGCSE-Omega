#!/usr/bin/env python3
"""Layer C — the authoritative 3-mark Explain inventory, built from the MARK SCHEMES.

WHY THIS EXISTS
---------------
`4BS1_Question_Instances.csv` was built from question-paper TEXT EXTRACTION, and
that extraction is column-scrambled. It therefore UNDER-COUNTS the 3-mark Explain
questions badly:

    CSV:      111 three-mark instances
    ACTUAL:   151 three-mark blocks, 4 per paper x 38 papers  (1(f), 2(c), 2(d), 2(e))

Examples of the shortfall: May-June 2024 P1 shows 3 in the CSV but has 4;
Nov 2024 P1 shows 2 but has 4; May-June 2024 P2 / May-June 2025 P2 show 1 each but have 4.

This script does not use the CSV at all. It reads the official MARK SCHEMES, which
state every question part and its AO allocation cleanly, and it also harvests the
official worked answer for each block -- because a 3-mark mark-scheme entry IS a
3/3 answer ("Award 1 mark for X (1) ... (1) ... (1)").

RUN FROM Business_Studies_Answer_Bank/.  Writes layer_c_3mark_master.csv.
"""
import csv
import json
import pathlib
import re
import sys

ARCHIVE = pathlib.Path(__file__).resolve().parent.parent / "Paperlords_Archive" / "IGCSE" / "4BS1_Business_Studies"
OUT = pathlib.Path(__file__).resolve().parent / "layer_c_3mark_master.csv"

BLOCK = re.compile(r"(\d+) \(([a-z]+)\)(?:\(([ivx]+)\))?\s*(A[O0]1)\s*[-=]\s*3\s*marks?", re.I)
# ⚠️ Do NOT loosen the third alternative to `for a+`: "for an entrepreneur" makes it
# match early and silently TRUNCATES the topic. It must be the full phrase.
AWARD = re.compile(r"Award 1 mark\s+(?:for\s+)?(.*?)(?:,?\s*plus\s+2\s+further|\.\s|,?\s*for\s+a+\s+maximum)", re.S | re.I)
WORKED = re.compile(r"•\s*(.*?(?:\(\d\).*?){1,4})", re.S)

# regex on the normalised mark-scheme topic phrase -> canonical Layer C topic
MAP = [
    (r"franchisee", "FRANCHISEE advantage"),
    (r"partners may disagree|partners may fall out", "PARTNERSHIP"),
    (r"paying its suppliers on time|pay their suppliers on time|pay suppliers on time", "PAYING SUPPLIERS ON TIME"),
    (r"negotiate deals with suppliers|cheaper rate", "INCREASE GROSS PROFIT MARGIN"),
    (r"television|above.?the.?line", "ABOVE-THE-LINE promotion method"),
    (r"below.?the.?line", "BELOW-THE-LINE promotion method"),
    (r"product life cycle", "PRODUCT LIFE CYCLE extension"),
    (r"penetration pricing", "PENETRATION PRICING"),
    (r"targeted advertising online", "TARGETED ADVERTISING ONLINE"),
    (r"e-newsletters", "E-NEWSLETTERS"),
    (r"sponsor", "SPONSORSHIP"),
    (r"public relations", "PUBLIC RELATIONS"),
    (r"purpose of market research", "MARKET RESEARCH purpose"),
    (r"secondary market research|secondary research|internet for secondary", "SECONDARY MARKET RESEARCH"),
    (r"questionnaire", "QUESTIONNAIRES disadvantage"),
    (r"market research information", "USING MARKET RESEARCH INFORMATION"),
    (r"loyal customers", "LOYAL CUSTOMERS advantage"),
    (r"social media", "SOCIAL MEDIA use"),
    (r"focus groups", "FOCUS GROUPS advantage"),
    (r"strong brand|why branding is important", "BRANDING importance"),
    (r"product orientation", "PRODUCT ORIENTATION disadvantage"),
    (r"product trials", "PRODUCT TRIALS"),
    (r"test marketing", "TEST MARKETING"),
    (r"repeat purchase", "REPEAT PURCHASE method"),
    (r"boston matrix", "BOSTON MATRIX"),
    (r"segment the market by income|market segmentation", "MARKET SEGMENTATION"),
    (r"limited liability", "LIMITED LIABILITY advantage"),
    (r"introducing new products|design new products", "NEW PRODUCTS benefit"),
    (r"packaging", "PACKAGING importance"),
    (r"venture capital|venture capitalist", "VENTURE CAPITAL"),
    (r"crowdfunding", "CROWDFUNDING"),
    (r"personal savings", "PERSONAL SAVINGS disadvantage"),
    (r"retained profit", "RETAINED PROFIT disadvantage"),
    (r"borrowing money from a bank", "BANK LOAN disadvantage"),
    (r"cash flow forecast", "CASH FLOW FORECAST"),
    (r"statement of financial position", "STATEMENT OF FINANCIAL POSITION purpose"),
    (r"statements of comprehensive income", "STATEMENT OF COMPREHENSIVE INCOME"),
    (r"financial documents of a business", "FINANCIAL DOCUMENTS (shareholders)"),
    (r"break-even level of output", "BREAK-EVEN OUTPUT calculation reason"),
    (r"break-even chart", "BREAK-EVEN CHART limitation"),
    (r"increase its profit|increasing profit", "INCREASE PROFIT method"),
    (r"interest rates are decreased|banks reduce their interest rates", "INTEREST RATES decrease"),
    (r"increase in interest rates", "INTEREST RATES increase"),
    (r"tariffs", "TARIFFS effect"),
    (r"trading bloc", "TRADING BLOC"),
    (r"multinational", "MULTINATIONAL"),
    (r"globalisation", "GLOBALISATION"),
    (r"sole trader", "SOLE TRADER"),
    (r"partnership", "PARTNERSHIP"),
    (r"private limited company", "PRIVATE LIMITED COMPANY (LTD)"),
    (r"business failure|business might fail|some businesses fail|poor cash flow", "BUSINESS FAILURE"),
    (r"predicted growth", "PREDICTED GROWTH not achieved"),
    (r"economies of scale", "ECONOMIES OF SCALE"),
    (r"diseconomies of scale", "DISECONOMIES OF SCALE"),
    (r"high market share", "HIGH MARKET SHARE"),
    (r"mass marketing", "MASS MARKETING"),
    (r"e-commerce", "E-COMMERCE"),
    (r"social objective", "SOCIAL OBJECTIVE"),
    (r"business aims and objectives may change", "AIMS AND OBJECTIVES change"),
    (r"measure of business success|measure of success", "MEASURING BUSINESS SUCCESS"),
    (r"human resource functional area|human resource function", "HR FUNCTION"),
    (r"responsibility of the human resources function", "HR FUNCTION"),
    (r"short span of control", "SHORT SPAN OF CONTROL"),
    (r"chain of command", "CHAIN OF COMMAND"),
    (r"flat organisational structure", "FLAT STRUCTURE"),
    (r"hierarchical organisational structure", "HIERARCHICAL STRUCTURE disadvantage"),
    (r"decentralised", "DECENTRALISED STRUCTURE"),
    (r"letter to communicate", "LETTER as a channel"),
    (r"ineffective communication", "INEFFECTIVE COMMUNICATION"),
    (r"improves communication with employees", "IMPROVING COMMUNICATION"),
    (r"health and safety training", "INDUCTION HEALTH AND SAFETY TRAINING"),
    (r"health and safety legislation", "HEALTH AND SAFETY LEGISLATION"),
    (r"equal opportunities", "EQUAL OPPORTUNITIES"),
    (r"disabilities", "EMPLOYEES WITH DISABILITIES"),
    (r"full-time employees", "FULL-TIME EMPLOYEES"),
    (r"seasonal", "SEASONAL STAFF"),
    (r"retaining", "RETENTION"),
    (r"fully trained", "FULLY TRAINED EMPLOYEES"),
    (r"curriculum vitae|cv", "CV UP TO DATE"),
    (r"job advertisement", "JOB ADVERTISEMENT information"),
    (r"motivate its employees|motivating employees", "MOTIVATING EMPLOYEES"),
    (r"herzberg", "HERZBERG"),
    (r"fringe benefits", "FRINGE BENEFITS"),
    (r"minimum wage", "ABOVE-MINIMUM PAY"),
    (r"training its employees", "TRAINING disadvantage"),
    (r"on-the-job training", "ON-THE-JOB TRAINING"),
    (r"temporary employees", "TEMPORARY EMPLOYEES"),
    (r"job production", "JOB PRODUCTION"),
    (r"batch production", "BATCH PRODUCTION"),
    (r"flow production", "FLOW PRODUCTION disadvantage"),
    (r"just-in-time|jit", "JIT STOCK CONTROL"),
    (r"kaizen", "KAIZEN"),
    (r"robotics", "ROBOTICS"),
    (r"technology on production", "TECHNOLOGY impact"),
    (r"quality control", "QUALITY CONTROL"),
    (r"total quality management|tqm", "TQM"),
    (r"maintain the quality of their products|quality of goods manufactured", "QUALITY importance"),
    (r"use resources effectively", "RESOURCE USE EFFICIENCY"),
    (r"proximity of material", "LOCATION proximity of materials"),
    (r"productivity improvements", "PRODUCTIVITY"),
]


def normalise(topic: str) -> str:
    t = re.sub(r"\s+", " ", topic.lower()).strip().rstrip(",")
    t = re.sub(r"^(the )?(identificat?i?o?n? of|identifica tion of|identificat ion of)\s+", "", t)
    return t.strip().rstrip(",")


def canonical(topic: str, worked: str = "") -> str:
    """Match the mark-scheme topic phrase against the rule table.

    The PDF text layer sprinkles spaces inside words ("p redicted growth",
    "li mitation of a cash flow fore c ast"), so every pattern is also tested
    against a whitespace-stripped copy. Where the topic phrase is generic
    ("identification of an advantage"), the official worked answer is used
    instead -- but ONLY then, because the harvested segment can run on into
    the next question and would otherwise match the wrong topic.
    """
    tight = lambda x: re.sub(r"\s+", "", x)          # strip whitespace noise
    for probe in (normalise(topic), tight(normalise(topic))):
        for pat, canon in MAP:
            if re.search(pat, probe) or re.search(tight(pat), probe):
                return canon
    if worked:
        w = tight(worked[:400].lower())
        for pat, canon in MAP:
            if re.search(tight(pat), w):
                return canon
    return "***UNMAPPED***"


def harvest() -> list[dict]:
    try:
        import pypdf
    except ImportError:
        sys.exit("pip install --break-system-packages pypdf cryptography")
    rows = []
    for pdf in sorted(ARCHIVE.glob("*/4BS1_*_MS.pdf")):
        raw = re.sub(r"\s+", " ", "".join(
            (p.extract_text() or "") for p in pypdf.PdfReader(str(pdf)).pages))
        session = pdf.parent.name.replace("_", " ")
        paper = re.search(r"(P\dR?)_MS", pdf.name).group(1)
        for m in BLOCK.finditer(raw):
            if re.match(r"\s*A[O0]2", raw[m.end():m.end() + 40]):
                continue  # the 6/9/12-mark headers also print "AO1 = 3 marks"
            seg = raw[m.end():m.end() + 800]
            a = AWARD.search(seg)
            topic = " ".join(a.group(1).split()).rstrip(",") if a else ""
            w = WORKED.search(seg)
            worked = " ".join(w.group(1).split()) if w else ""
            rows.append(dict(session=session, paper=paper, question=f"{m.group(1)}({m.group(2)})",
                             ms_topic=topic, canonical_topic=canonical(topic, worked),
                             ms_worked_answer=worked))
    return rows


def main() -> int:
    rows = harvest()
    with OUT.open("w", newline="", encoding="utf-8") as fh:
        wtr = csv.DictWriter(fh, fieldnames=list(rows[0]))
        wtr.writeheader()
        wtr.writerows(rows)
    topics = sorted({r["canonical_topic"] for r in rows})
    unmapped = [r for r in rows if r["canonical_topic"] == "***UNMAPPED***"]
    print(f"3-mark blocks harvested : {len(rows)}   (papers: {len({(r['session'], r['paper']) for r in rows})})")
    print(f"canonical topics        : {len(topics)}")
    print(f"unmapped                : {len(unmapped)}")
    print(f"written                 : {OUT.name}")
    for r in unmapped:
        print("   UNMAPPED:", r["session"], r["paper"], r["question"], "|", r["ms_topic"][:80])
    return 0


if __name__ == "__main__":
    sys.exit(main())
