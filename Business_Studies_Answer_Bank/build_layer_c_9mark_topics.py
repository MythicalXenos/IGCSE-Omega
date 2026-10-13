#!/usr/bin/env python3
"""Assign each 9-mark Justify block to a canonical OPTION-PAIR topic.

WHY THE OPTION PAIR IS THE UNIT
-------------------------------
All 76 nine-mark questions in this qualification use ONE framing:

    "Justify which one of these two options X should choose."

The framing never varies, so it carries no information and needs no entry. **What
varies is the pair of options** -- and the mark scheme's AO4 section gives the
judgement for each. Two blocks share a topic when they are asking the candidate to
choose BETWEEN THE SAME TWO KINDS OF THING (a bank loan against personal savings),
even when the business, the amounts and the wording differ.

RULES ARE FIRST-MATCH-WINS, so order matters: the more specific pair must be
tested before the more general one. A block that matches no rule is printed as
UNMAPPED and must be added deliberately -- an unmapped block is never silently
folded into a neighbouring topic.

Writes layer_c_9mark_topics.csv.
"""
import collections
import csv
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
INV = HERE / "layer_c_9mark_inventory.csv"
OUT = HERE / "layer_c_9mark_topics.csv"

# (regex over "option1 || option2", canonical topic)
RULES = [
    # ---- finance: source of finance (specific pair FIRST) ---------------
    (r"venture capitalist.*franchisee|franchisee will pay",
     "GROWTH — venture capital vs franchising"),
    (r"venture capital.*crowdfunding|crowdfunding.*venture capitalist|persuaded to invest in Jacob",
     "FINANCE — venture capital vs crowdfunding"),
    (r"venture capitalist|venture capital|appeal to an individual who wishes to invest",
     "FINANCE — venture capital vs a bank loan"),
    (r"crowdfund.*overdraft|overdraft",
     "FINANCE — crowdfunding vs an overdraft"),
    (r"appeal to the public for funding|Saha may appeal to the public",
     "FINANCE — crowdfunding vs a bank loan"),
    (r"crowdfund.*retained|retained profits which have been earned",
     "FINANCE — crowdfunding vs retained profit"),
    (r"crowdfund", "FINANCE — startups: crowdfunding vs another source"),
    (r"personal saving", "FINANCE — personal savings vs a bank loan"),
    (r"selling off|sell off assets|selling any bicycle equipment",
     "FINANCE — retained profit vs selling unused assets"),
    (r"retained profit|retained profits", "FINANCE — retained profit vs a bank loan"),
    # ---- pricing ---------------------------------------------------------
    (r"price skimming|sold at a high price when it is released",
     "PRICING — cost plus vs price skimming"),
    (r"competition pricing", "PRICING — competition pricing vs cost plus"),
    (r"match the price|matching the price .*discount|discount on the price of a 3",
     "PRICING — price matching vs a discount"),
    (r"introductory price|low price for its meals",
     "PRICING — penetration/introductory pricing vs another tactic"),
    (r"cost plus", "PRICING — cost plus vs promotional pricing"),
    (r"cheaper price|cheaper price encourages|selling at a cheaper price",
     "PRICING — lowering the price vs another tactic"),
    (r"discount|coupon", "PROMOTION — coupons/discounts vs another method"),
    (r"half- ?priced|half- ?priced drink", "PRICING — price cut vs a linked giveaway"),
    # ---- research and success measures -----------------------------------
    (r"questionnaire.*focus group|focus group.*questionnaire",
     "RESEARCH — questionnaires vs focus groups"),
    (r"questionnaire", "RESEARCH — questionnaires vs secondary research"),
    (r"primary market research", "RESEARCH — primary vs secondary research"),
    (r"secondary research|secondary market research",
     "RESEARCH — primary vs secondary research"),
    (r"internet to view|view a large selection of webs|websites|customers can take their time completing the form",
     "RESEARCH — primary vs secondary research"),
    (r"customer satisfaction will indicate|high level of profit will show",
     "MEASURING SUCCESS — customer satisfaction vs profit"),
    # ---- promotion -------------------------------------------------------
    (r"TV advert|free headphones", "PROMOTION — mass advertising vs a free giveaway"),
    (r"social media to advertise", "PROMOTION — social media vs coupons"),
    (r"special offers", "PROMOTION — special offers vs another method"),
    (r"sponsoring a local charity|sponsoring a local",
     "PROMOTION — sponsoring a charity vs special offers"),
    (r"sponsor", "PROMOTION — sponsorship vs another method"),
    (r"e-?newsletter", "PROMOTION — targeted online advertising vs e-newsletters"),
    (r"targeted online advertising",
     "PROMOTION — targeted online advertising vs e-newsletters"),
    (r"celebrity|free game applications",
     "PROMOTION — paid celebrity endorsement vs a free giveaway"),
    (r"pop-?up|cookery courses", "PROMOTION — events vs widening the courses offered"),
    (r"leaflets can be handed|event will increase the awareness",
     "PROMOTION — events vs leaflets"),
    (r"food to passing trade|charity shops that Loaf works with could display",
     "PROMOTION — attracting passing trade vs free promotional space"),
    (r"increase the awareness of Artify|become known to a wider market",
     "PROMOTION — local awareness vs a wider market"),
    (r"noticeboard", "COMMUNICATION — noticeboard vs a staff meeting"),
    # ---- marketing / product --------------------------------------------
    (r"increase in advertising can reach|opening for breakfast",
     "MARKETING — promotion vs extending the offer"),
    (r"increasing promotion more people will know|new features to the cars",
     "MARKETING — promotion vs product improvement"),
    (r"bought the last book|respond to changing food trends",
     "PRODUCT — extending the range for existing customers vs new trends"),
    (r"teaching other musical instruments|online lessons",
     "PRODUCT — widening the range vs widening the delivery"),
    (r"vegan range", "PRODUCT — new product range vs a price discount"),
    (r"variety of aftershaves|advertising of a new perfume",
     "PRODUCT — widening the range vs promoting the range"),
    (r"add an extra element to its website|create a USP|USP",
     "MARKETING — creating a USP vs improving the website"),
    (r"online purchases|to view the smartwatch", "PLACE — physical stores vs online"),
    (r"coffee shops in supermarkets|coffee shops in hospitals",
     "PLACE — which new location to open in"),
    # ---- motivation, job design, contracts ------------------------------
    (r"job enrichment.*job rotation|job rotation.*job enrichment",
     "JOB DESIGN — job enrichment vs job rotation"),
    (r"adding additional tasks", "JOB DESIGN — adding tasks vs job rotation"),
    (r"job enrichment", "JOB DESIGN — a bonus vs job enrichment"),
    (r"bonus payment if car manufacturing targets|move to different jobs on or off the production line",
     "JOB DESIGN — job rotation vs a bonus"),
    (r"financial methods to its employees|non-financial benefit|extra five days.holiday|commission|hourly rate",
     "MOTIVATION — financial reward vs non-financial methods"),
    (r"extra .*holiday|holiday away from the restaurant",
     "MOTIVATION — extra holiday vs a bonus"),
    (r"e-?mail is a method", "COMMUNICATION — email vs face-to-face"),
    (r"full-?time", "CONTRACTS — full-time vs part-time staff"),
    (r"job share", "CONTRACTS — part-time vs job share"),
    (r"part-?time", "CONTRACTS — part-time vs job share"),
    (r"permanent contract|temporary contract",
     "CONTRACTS — permanent vs temporary contract"),
    (r"on call", "CONTRACTS — on-call staff vs students"),
    # ---- training and recruitment ---------------------------------------
    (r"induction training", "TRAINING — induction vs off-site training"),
    (r"on-the-job training|remain on the", "TRAINING — on-the-job vs off-the-job"),
    (r"off-?the-?job|off site|trained by experts", "TRAINING — on-the-job vs off-the-job"),
    (r"internally|internal employee", "RECRUITMENT — internal vs external"),
    (r"external|agency", "RECRUITMENT — internal vs external"),
    # ---- operations ------------------------------------------------------
    (r"JIT.*Kaizen|Kaizen.*JIT", "OPERATIONS — Kaizen vs JIT"),
    (r"just-?in-?time|JIT", "OPERATIONS — Kaizen/employee involvement vs JIT"),
    (r"employees are involved in the process of improving",
     "OPERATIONS — Kaizen/employee involvement vs JIT"),
    (r"flow production", "PRODUCTION — flow vs batch production"),
    (r"batch production", "PRODUCTION — batch vs job production"),
    (r"job production", "PRODUCTION — batch vs job production"),
    # ---- structure and costs --------------------------------------------
    (r"limited liability as will his new",
     "STRUCTURE — partnership vs private limited company"),
    (r"reduce the wages|reducing commission",
     "COSTS — reducing wages vs reducing commission"),
]


def main() -> int:
    rows = list(csv.DictReader(INV.open(encoding="utf-8")))
    for r in rows:
        text = f"{r['option_1']} || {r['option_2']}"
        topic = "***UNMAPPED***"
        for pat, canon in RULES:
            if re.search(pat, text, re.I):
                topic = canon
                break
        r["topic"] = topic

    with OUT.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    tally = collections.Counter(r["topic"] for r in rows)
    print(f"blocks            : {len(rows)}")
    print(f"distinct topics   : {len(tally)}")
    unmapped = [r for r in rows if r["topic"].startswith("***")]
    print(f"UNMAPPED          : {len(unmapped)}")
    for r in unmapped:
        print(f"   [{r['n']}] {r['session']} {r['paper']} {r['question']}: "
              f"{r['option_1'][:60]} | {r['option_2'][:60]}")
    print()
    for t, c in tally.most_common():
        print(f"  {c:>2}  {t}")
    print(f"\nwrote {OUT.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
