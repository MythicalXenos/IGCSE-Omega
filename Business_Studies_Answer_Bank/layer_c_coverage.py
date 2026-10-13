#!/usr/bin/env python3
"""Layer C coverage check for the 3-mark Explain bank.

Reads `layer_c_3mark_master.csv` (produced by `build_layer_c_3mark.py`, which
derives it from the 38 mark schemes) and reports how many canonical topics are
carried by an entry in `Perfect_Answers/10_Chain_Bank.md`.

READ THIS BEFORE QUOTING THE OUTPUT
-----------------------------------
This SUPERSEDES the earlier version of this script, which matched question
stems from `4BS1_Question_Instances.csv` against the wording in the chain bank.
That approach was abandoned because the CSV is built from question-paper text
extraction and under-counts the 3-mark population by 40 (111 reported, 151
actual). Matching job is now done against a derived, verified topic list.

To mark a topic as covered, add it to COVERED with the entry number in the
chain bank that carries it. Nothing is inferred from wording any more.

Run from Business_Studies_Answer_Bank/ (NOT from Perfect_Answers/).
"""
import csv
import sys
from pathlib import Path

BANK = Path(__file__).resolve().parent
MASTER = BANK / "layer_c_3mark_master.csv"

# canonical topic -> the entry number in 10_Chain_Bank.md that carries it
COVERED = {
    # Batch 1 — June 2026 + Nov 2025
    "CHAIN OF COMMAND": 1, "AIMS AND OBJECTIVES change": 2, "ECONOMIES OF SCALE": 3,
    "BUSINESS FAILURE": 4, "BREAK-EVEN OUTPUT calculation reason": 5, "MARKET SEGMENTATION": 6,
    "PRODUCTIVITY": 7, "QUALITY CONTROL": 8, "LIMITED LIABILITY advantage": 9,
    "TEMPORARY EMPLOYEES": 10, "ON-THE-JOB TRAINING": 11, "HIGH MARKET SHARE": 12,
    "E-COMMERCE": 13, "MASS MARKETING": 14, "SOCIAL OBJECTIVE": 15, "BREAK-EVEN CHART limitation": 16,
    # Batch 2 — 3.1 + the 3.2 structure/HR cluster
    "PARTNERSHIP": 17, "SOLE TRADER": 19, "FRANCHISEE advantage": 20, "MULTINATIONAL": 21,
    "GLOBALISATION": 22, "TRADING BLOC": 23, "PREDICTED GROWTH not achieved": 25,
    "INTEREST RATES increase": 26, "INTEREST RATES decrease": 27, "TARIFFS effect": 28,
    "HEALTH AND SAFETY LEGISLATION": 29, "HR FUNCTION": 30, "SHORT SPAN OF CONTROL": 31,
    "FLAT STRUCTURE": 33, "DECENTRALISED STRUCTURE": 34, "IMPROVING COMMUNICATION": 35,
    "INEFFECTIVE COMMUNICATION": 36, "LETTER as a channel": 37,
    "INDUCTION HEALTH AND SAFETY TRAINING": 38, "EQUAL OPPORTUNITIES": 39,
    "EMPLOYEES WITH DISABILITIES": 40, "FULL-TIME EMPLOYEES": 41, "SEASONAL STAFF": 42,
    "RETENTION": 43, "FULLY TRAINED EMPLOYEES": 44, "CV UP TO DATE": 45,
    "MOTIVATING EMPLOYEES": 46, "HERZBERG": 47, "FRINGE BENEFITS": 48, "ABOVE-MINIMUM PAY": 49,
    # Batch 3 — 3.3 Marketing
    "MARKET RESEARCH purpose": 50, "QUESTIONNAIRES disadvantage": 51,
    "SECONDARY MARKET RESEARCH": 52, "USING MARKET RESEARCH INFORMATION": 53,
    "FOCUS GROUPS advantage": 54, "BRANDING importance": 55, "PACKAGING importance": 56,
    "PRODUCT LIFE CYCLE extension": 57, "NEW PRODUCTS benefit": 58, "BOSTON MATRIX": 59,
    "PRODUCT TRIALS": 60, "TEST MARKETING": 61, "PRODUCT ORIENTATION disadvantage": 62,
    "PENETRATION PRICING": 63, "ABOVE-THE-LINE promotion method": 64,
    "BELOW-THE-LINE promotion method": 65, "SPONSORSHIP": 66,
    "TARGETED ADVERTISING ONLINE": 67, "E-NEWSLETTERS": 68, "SOCIAL MEDIA use": 69,
    "PUBLIC RELATIONS": 70, "REPEAT PURCHASE method": 71, "LOYAL CUSTOMERS advantage": 72,
    # Batch 4 — 3.4 Operations, 3.5 Finance, and the last stragglers
    "MEASURING BUSINESS SUCCESS": 73, "PRIVATE LIMITED COMPANY (LTD)": 74,
    "HIERARCHICAL STRUCTURE disadvantage": 75, "JOB PRODUCTION": 76, "BATCH PRODUCTION": 77,
    "FLOW PRODUCTION disadvantage": 78, "TECHNOLOGY impact": 79, "ROBOTICS": 80,
    "JIT STOCK CONTROL": 81, "KAIZEN": 82, "TQM": 83, "QUALITY importance": 84,
    "RESOURCE USE EFFICIENCY": 85, "LOCATION proximity of materials": 86,
    "JOB ADVERTISEMENT information": 87, "TRAINING disadvantage": 88, "CASH FLOW FORECAST": 89,
    "INCREASE PROFIT method": 90, "INCREASE GROSS PROFIT MARGIN": 91, "CROWDFUNDING": 92,
    "VENTURE CAPITAL": 93, "BANK LOAN disadvantage": 94, "PERSONAL SAVINGS disadvantage": 95,
    "RETAINED PROFIT disadvantage": 96, "STATEMENT OF COMPREHENSIVE INCOME": 97,
    "STATEMENT OF FINANCIAL POSITION purpose": 98, "FINANCIAL DOCUMENTS (shareholders)": 99,
    "PAYING SUPPLIERS ON TIME": 100,
}


def main() -> int:
    if not MASTER.exists():
        sys.exit(f"{MASTER.name} missing -- run build_layer_c_3mark.py first")
    rows = list(csv.DictReader(MASTER.open(encoding="utf-8")))
    counts: dict[str, int] = {}
    for r in rows:
        counts[r["canonical_topic"]] = counts.get(r["canonical_topic"], 0) + 1

    unknown = sorted(set(COVERED) - set(counts))
    covered = {k: v for k, v in counts.items() if k in COVERED}
    remaining = {k: v for k, v in counts.items() if k not in COVERED}

    print(f"3-mark blocks            : {len(rows)}")
    print(f"canonical topics         : {len(counts)}")
    print(f"covered by entries 1-100  : {len(covered)} topics  ·  {sum(covered.values())} blocks")
    print(f"REMAINING                : {len(remaining)} topics  ·  {sum(remaining.values())} blocks")
    if unknown:
        print(f"\nWARNING: {len(unknown)} names in COVERED are not in the master CSV:")
        for u in unknown:
            print("   ", u)
    print("\nREMAINING TOPICS")
    print("-" * 60)
    for k, v in sorted(remaining.items()):
        print(f"  {v}  {k}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
