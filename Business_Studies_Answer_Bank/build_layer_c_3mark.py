#!/usr/bin/env python3
"""Layer C — the authoritative 3-mark Explain inventory, built from the MARK SCHEMES.

WHY THIS EXISTS
---------------
`4BS1_Question_Instances.csv` was built from question-paper TEXT EXTRACTION, and
that extraction is column-scrambled. It therefore UNDER-COUNTS the 3-mark Explain
questions badly:

    CSV:      111 three-mark instances
    ACTUAL:   152 three-mark blocks, 4 per paper x 38 papers  (1(f), 2(c), 2(d), 2(e))

The 152 figure is DERIVED, not asserted: build_layer_c_tariffs.py reads the same
38 mark schemes, reconstructs every question part, and confirms all 38 papers sum
to exactly 80 marks -- the paper's stated total. The labels are invariant: every
paper carries 1(f), 2(c), 2(d) and 2(e) at 3 marks, and all 38 agree.

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
# Some mark schemes print no bullet glyph at all (May-June 2019 P2 and P2R: the
# answer is plain prose after "for a maximum of 3 marks."). Without this branch
# those eight blocks harvested an EMPTY worked answer.
PLAIN = re.compile(
    r"for a maximum of 3 marks\.?\s*(.+?)"
    r"(?=\s*(?:Answers? that list|Accept any|NB |Note:|\(\d+\s*\)?\s*Question|Question Number)|$)",
    re.S)
# A worked answer must stop before the next question's stem, or the canonical-topic
# fallback reads the NEXT question and mislabels this one. That is exactly how
# May-June 2021 P2 2(c) -- "explain one reason why businesses fail" -- was filed
# as BATCH PRODUCTION: its segment ran on into 2(d)'s stem.
STOP = re.compile(
    r"\s*(?:NB |Note:|Answers? that list|Accept any other appropriate response"
    r"|\(\d+\s*\)\s*(?:Question|Total)|Question Number).*$", re.S)

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
    (r"business failure|business might fail|some businesses fail|poor cash flow|why businesses fail|businesses fail", "BUSINESS FAILURE"),
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


def repair(text: str) -> str:
    """Undo the character fragmentation in the May-June 2021 PDFs.

    Those files print "A0 1 - 3 mark s" for "AO1 - 3 marks", which defeats the
    BLOCK pattern and silently dropped one whole block -- May-June 2021 P1 1(f),
    the difference between the 151 this script used to report and the true 152.

    A targeted repair is used rather than de-spacing the whole document, because
    de-spacing destroys the readable spacing of the harvested workanswer.
    """
    text = re.sub(r"\bA\s?[O0]\s?([1-4])\b", r"AO\1", text)
    text = re.sub(r"\bm\s?a\s?r\s?k\s?s\b", "marks", text)
    return text


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
        raw = repair(re.sub(r"\s+", " ", "".join(
            (p.extract_text() or "") for p in pypdf.PdfReader(str(pdf)).pages)))
        session = pdf.parent.name.replace("_", " ")
        paper = re.search(r"(P\dR?)_MS", pdf.name).group(1)
        hits = list(BLOCK.finditer(raw))
        for i, m in enumerate(hits):
            if re.match(r"\s*A[O0]2", raw[m.end():m.end() + 40]):
                continue  # the 6/9/12-mark headers also print "AO1 = 3 marks"
            # bound the segment at the next block, not at a fixed character count
            end = hits[i + 1].start() if i + 1 < len(hits) else min(len(raw), m.end() + 1200)
            seg = raw[m.end():end]
            a = AWARD.search(seg)
            topic = " ".join(a.group(1).split()).rstrip(",") if a else ""
            w = WORKED.search(seg) or PLAIN.search(seg)
            worked = STOP.sub("", " ".join(w.group(1).split())).strip() if w else ""
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
