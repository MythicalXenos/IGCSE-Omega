# 10 — THE CHAIN BANK

**Every answer here is labelled, and the label matters.** Three kinds appear:

| Label | What it is | What it is NOT |
|---|---|---|
| `[VERIFIED CANDIDATE EXEMPLAR]` | a real student script an official Pearson report scores at full marks (session, paper, question, page cited) | — |
| `[OFFICIAL MARK-SCHEME WORKED ANSWER]` | **Pearson's own indicative content, quoted verbatim, carrying the scheme's own (1)(1)(1) allocation** | **not a candidate script · not examiner-marked** |
| `[CONSTRUCTED GRADE 9 TARGET]` | engineered by me from the question paper, the mark scheme and the examiner reports | not official, not a student script, not examiner-marked |

**No model here is ever described as "official" unless it is quoted from Pearson, and no model is ever given a candidate's score.** Where a verified script exists it is held in `02_Verified_Exemplars.md` and labelled there.

---

## WHY THIS FILE EXISTS, AND HOW IT COVERS THE WHOLE QUALIFICATION

Across 38 papers the qualification asks **governed** questions — anything needing three marks or more of written reasoning. That looks like hundreds of essays. It is not, and writing hundreds of essays would be the wrong response to it.

**The number of distinct framings is small and stable:**

| Tariff | Distinct framings | What actually varies |
|---|---|---|
| **3-mark Explain** | **8** | the **topic** |
| **6-mark Analyse** | **~6** | the **topic** and the framing |
| **9-mark Justify** | **1** — *"justify which one of these two options…"* | the **option pair** |
| **12-mark Evaluate** | **~5** | the **topic** |

**So there are only about twenty distinct framings in the whole qualification.** Every governed question is a **framing** wrapped around a **topic**.

**How many instances of each framing there actually are:**

| Tariff | Instances | Where the number comes from |
|---|---|---|
| **3-mark Explain** | **151** | ✅ **derived from the 38 mark schemes — exactly 4 per paper** |
| **6-mark Analyse** | *not yet derived* | ⚠️ the CSV's 86 is unreliable |
| **9-mark Justify** | *not yet derived* | ⚠️ the CSV's 48 is **proven too low** |
| **12-mark Evaluate** | *not yet derived* | ⚠️ the CSV's 17 is unverified |

> 🚨 **The old headline figure of "262 governed items" is withdrawn.** It was built on `4BS1_Question_Instances.csv`, and that file is measurably wrong. **The full scope correction is the next section — read it before trusting any count in this bank, including any count in another file.**

This file supplies both halves:

- **`01_Mark_Tariff_Playbook.md`** already holds the framings — the structure and mark allocation for each tariff.
- **This file holds the topics** — the actual causal chains that earn the marks, one entry per topic.

**A topic done once here covers every paper it has ever appeared on, and every paper it will appear on next.**

---

## HOW TO USE IT

Every entry gives you:

1. **The question as it was actually asked** — with the session and paper, so you can check it.
2. **A model answer** in the exact shape the marks are awarded for.
3. **The chain, broken out** — so you can rebuild it under pressure rather than memorise prose.
4. **A second acceptable chain**, because the mark scheme accepts *"any other appropriate response"*.

> ### ⭐ THE ONE RULE FOR EVERY 3-MARK ANSWER
> **Point + two development steps. Nothing more can score.**
> Pearson's own words: *"from the mark scheme they can **only gain 2 further marks** for explaining the reason. **Do not waste time in the examination with longer responses than necessary.**"*
> **Three sentences. That is the whole answer.**
> ⚠️ **And the third mark is lost by repeating, not by running out of ideas:** *"their second strand of development often involved **merely restating the initial point**."* Each step must be a **new** link.

> ### ⭐ AND THE COMMAND-WORD NOTE THAT APPLIES TO EVERY ENTRY BELOW
> **Explain assesses AO1 — Knowledge. Context is NOT required.**
> June 2025 P1 states it twice: *"No context/reference to the business in the exam paper is required in Explain questions."*
> ⚠️ **But it is not penalised either.** If a topic phrase from the case study comes naturally, use it — it costs nothing.

---

## Batch status

| Batch | Content | Status |
|---|---|---|
| **1** | Newest 3-mark topics — June 2026 + Nov 2025 | ✅ 16 entries |
| **2** | **3.1 Business activity + 3.2 structure/HR cluster** | ✅ **33 entries** |
| **3** | **3.3 Marketing** | ✅ **23 entries (50–72)** |
| **4** | 3.4 Operations + 3.5 Finance + measuring business success | ⬜ next |
| **5–6** | 6-mark Analyse chains | ⬜ |
| **7–8** | 9-mark Justify option pairs | ⬜ |
| **9** | 12-mark Evaluate topics | ⬜ |

### 🚨 SCOPE CORRECTION — **151** three-mark blocks, not 111

**This file previously counted the 3-mark population from `4BS1_Question_Instances.csv` and reported 111. That number is wrong, and the fault was in the measuring instrument rather than in the counting.**

The CSV was built from **question-paper text extraction**, which is column-scrambled and silently loses whole question parts. The **mark schemes** state every part cleanly, and read that way **each of the 38 papers carries exactly four 3-mark Explain questions — 1(f), 2(c), 2(d) and 2(e):**

```
3-mark Explain blocks, read from the mark schemes : 151   (4 x 38 papers)
from 4BS1_Question_Instances.csv                  : 111   (under-count of 40)
```

How much is lost varies by paper — **May/June 2024 P1 shows 3 in the CSV but has 4; Nov 2024 P1 shows 2 and May/June 2025 P2 shows 1, and both have 4.** The shortfall is therefore **not a constant that can be added back on.**

**So `4BS1_Question_Instances.csv` is no longer the scope authority for Layer C — the mark schemes are.** The tool that re-derives this, and which also harvests each block's official worked answer, is **`../build_layer_c_3mark.py`** → **`../layer_c_3mark_master.csv`**. Both are tracked, and the tool re-reads the archive on every run, **so a sandbox re-seed cannot lose the finding again.**

### ⭐ PROGRESS — 3-mark Explain, derived and not estimated

```
3-mark blocks total     :  151
canonical topics        :   97
covered by entries 1-72 :   69 topics  ·  112 blocks
REMAINING               :   28 topics  ·   39 blocks
```

> **How this is counted.** `build_layer_c_3mark.py` reads all 38 mark schemes, harvests every 3-mark block, and normalises each to a canonical topic — *"identification of a benefit to a business of using e-newsletters"*, *"a way a business could use e-newsletters"* and *"a benefit to a business of using e-newsletters"* all resolve to **E-NEWSLETTERS**. **0 blocks are unmapped.** The figure above is **97 distinct canonical topics, of which 69 are carried by an entry in this file.**
> ⚠️ **Rule 118 is now enforced by machine.** Every hand-written total in this file has drifted at least once. **This one cannot**: re-run the tool and it prints the number.

### ⚠️ THE 6-, 9- AND 12-MARK TOTALS ARE STILL UNSAFE — DO NOT QUOTE THEM

The `86 · 48 · 17` figures come from the **same unreliable CSV**, and the mark schemes already contradict one of them: **the P1-family papers carry TWO 9-mark Justify questions, not one.** Verified by hand on **Nov 2024 P1**, which has a Justify at **2(f)** (*crowdfunding vs loan capital*) **and a second at 3(e)** (*price skimming vs cost plus pricing*). **So 48 is an undercount.**

Re-deriving the three larger tariffs needs a proper **block** parser, not a header regex — AO allocations are printed more than once per question, so a regex double-counts. **That re-derivation is the integrity task that follows Batch 4. Until it is done, no 6-, 9- or 12-mark total is asserted anywhere.**

---

# BATCH 1 — the newest series (June 2026 and Nov 2025), all 14 three-mark topics

---

## 1. Long chain of command — disadvantage

**Asked:** *"Explain one disadvantage for a business of having a **long chain of command**."* — June 2026 P1

> **Model answer — 3 marks**
> A long chain of command means instructions pass through many layers of management before reaching the people who do the work. **This slows communication down**, because each layer must relay the message on, so decisions take longer to reach the shop floor. **This means the business reacts more slowly than its competitors** to changes in customer demand, so it can lose sales it would otherwise have made.

| Step | The move |
|---|---|
| **1. Point** | A long chain = many layers between top and bottom |
| **2. Mechanism** | Each layer relays → **messages slow and can be distorted** |
| **3. Consequence** | Slower reaction to the market → **lost sales** |

**Second acceptable chain:** long chain → more managers to pay → **higher wage costs** → less profit at the same revenue.

> ⚠️ **Do not write "communication is bad".** The mark is for **why** many layers slow it down, then what that costs the business.

---

## 2. Why business aims and objectives may change over time

**Asked:** *"Explain one reason why business **aims and objectives may change over time**."* — June 2026 P1

> **Model answer — 3 marks**
> A business's aims may change as the market it operates in changes. **If a competitor launches a much cheaper product, a business aiming to be the market leader may switch to aiming simply to survive**, because it can no longer compete on price. **This changes where the business spends its money** — less on expansion and more on cutting costs — which keeps it trading instead of failing.

**Second acceptable chain:** the business grows → the owner's original aim of *survival* is **achieved**, so the objective moves to **growth or profit**, changing how profits are used.

> ⭐ **The chain pattern is: something changes → the old aim stops fitting → the business redirects its effort.**

---

## 3. Economies of scale — reason a business benefits

**Asked:** *"Explain one reason why a business may **benefit from economies of scale**."* — June 2026 P1

> **Model answer — 3 marks**
> Economies of scale happen when a business grows and its **average cost per unit falls**. A larger business can buy raw materials in bulk, and suppliers charge **less per unit for large orders**, so each item costs less to produce. **This raises the profit margin on every sale**, meaning the business keeps more from the same selling price — and it can undercut rivals while still profiting.

**Second acceptable chain:** growth → **specialist machinery or staff** become affordable → output per worker rises → **unit cost falls**.

> ⚠️ **Name the *source* of the saving** (bulk buying, specialisation, technology). "It gets cheaper because it's bigger" is the answer that scores 1.

---

## 4. Poor cash flow causing business failure

**Asked:** *"Explain one reason why **business failure may be caused by poor cash flow**."* — June 2026 P1

> **Model answer — 3 marks**
> Cash flow is the money moving in and out of a business day to day, and it is different from profit. **A business can be profitable and still fail if its money is tied up in stock and unpaid customer invoices**, so it has no cash in the bank on the day a supplier or wage bill is due. **Suppliers then refuse to deliver or the business cannot pay staff**, and trading stops even though the accounts show a profit.

**Second acceptable chain:** poor cash flow → **cannot pay debts when they fall due** → creditors take legal action or the bank withdraws the overdraft → **the business is forced to close**.

> ### ⭐ THE SINGLE MOST IMPORTANT DISTINCTION IN 3.5
> **Profit is not cash.** Profit is revenue minus costs over a period; cash is what is actually in the bank today. **This distinction is the whole mark.**
> ⚠️ **Note which paper this appeared on: P1.** Cash flow is not a P2-only topic.

---

## 5. Calculating break-even level of output — reason

**Asked:** *"Explain one reason why a business **calculates the break-even level of output**."* — June 2026 P1R

> **Model answer — 3 marks**
> Break-even output is the number of units a business must sell to cover its total costs, where revenue exactly equals costs. **Calculating it tells the owner how many sales are needed before the business stops making a loss**, so they know whether their sales forecast is realistic. **This lets them set a target and decide whether to go ahead with the product** — or negotiate a lower rent or cheaper supplier before committing money.

**Second acceptable chain:** break-even output → **compare against expected demand** → if expected demand is lower than break-even, **the launch is not viable** and the money is saved.

> ⚠️ **Rule 07 note:** you do **not** have to draw or read a break-even *chart* for this — the examiner has said diagrams are not required for the calculation questions. **The formula is break-even output = fixed costs ÷ contribution**, and contribution = price − variable cost.

---

## 6. Segmenting the market by income

**Asked:** *"Explain one reason why a business would **segment the market by income**."* — June 2026 P1R

> **Model answer — 3 marks**
> Dividing customers by income lets a business aim a product at the group that can actually afford it. **A business selling luxury goods targets high earners and avoids wasting money advertising to people who will never buy**, because its price point excludes them. **This makes its marketing budget go further**, so the same spend produces more sales than advertising to everyone.

**Second acceptable chain:** income segmentation → **two product versions** (premium and budget) → the business serves both ends of the market and **gains customers it would otherwise lose** to competitors.

> ### ⚠️ THE WORDS TO GET RIGHT
> *Segmentation* is **dividing the market into groups**; *targeting* is choosing which group to serve. **The question says "segment" — answer with the dividing, then the benefit of having divided.**
> ⭐ And note the examiner's warning, recorded as rule 74: **"demographic segmentation" was confused twice in 2023.** Income is one *way* of segmenting; it is not a type of research.

---

## 7. Productivity improvements — benefit to a business

**Asked:** *"Explain one benefit to a business from **productivity improvements**."* — June 2026 P1R

> **Model answer — 3 marks**
> Productivity is output per worker, so an improvement means **the same number of staff produce more**. The business therefore spreads its fixed costs — rent, machinery, salaried managers — across more units. **This lowers the average cost of each unit, so the business makes a bigger profit margin on every sale**, or can cut its price to win customers while still covering costs.

**Second acceptable chain:** higher productivity → **more output without more wages** → unit labour cost falls → **more competitive pricing** → higher market share.

> ⚠️ **Do not confuse productivity with production.** *Production* is how much is made; *productivity* is how much is made **per worker or per hour**. A factory can raise production by hiring, and raise productivity not at all.

---

## 8. Quality control — advantage

**Asked:** *"Explain one advantage for a business of using **quality control**."* — June 2026 P2

> **Model answer — 3 marks**
> Quality control means **inspecting the finished product and removing the ones that fail the standard**. This stops faulty goods reaching customers, so the business does not have to replace them or refund them. **This reduces the cost of returns and replacements, and it protects the business's reputation**, so customers keep buying and the brand can charge a higher price.

**Second acceptable chain:** quality control → **faulty items caught before despatch** → fewer customer complaints → **less damage to reputation and fewer refunds**.

> ### 🚨 THREE TRAPS, ALL DOCUMENTED
> **1.** *"Quality control will increase the competition"* — a real candidate answer, **0 marks**. Quality control does not create competitors.
> **2.** The examiner's standing complaint: *"it was **rare** to see candidates refer to quality control, **quality assurance** or other forms of TQM."* **Learn all three terms and the difference:**
> | Term | When quality is checked | Who is responsible |
> |---|---|---|
> | **Quality control** | at the **end** — inspection and removal | an inspector |
> | **Quality assurance** | **during** — built into every stage | everyone in production |
> | **TQM** | **throughout the whole business**, including suppliers | the whole organisation |
> **3.** ⚠️ **A wrong opening premise poisons the consequences.** A June 2025 answer wrote *"Total quality management gives a business a better name... This will increase profit"* and scored **0**, because *"there is **no understanding of TQM demonstrated** in the response therefore the reference to 'increased customer satisfaction' is **not awarded**."* **Get the definition right before developing it.**

---

## 9. Limited liability — advantage for a shareholder

**Asked:** *"Explain one advantage for a **shareholder** of having **limited liability**."* — June 2026 P2R

> **Model answer — 3 marks**
> Limited liability means a shareholder can only lose the money they invested in the company's shares; they are not personally responsible for its debts. **If the company fails, a shareholder's personal possessions are safe** — their house, car and savings cannot be claimed by the company's creditors. **This makes investing far less risky**, so shareholders are willing to put money in, and the business can raise more capital than an unlimited owner could.

**Second acceptable chain:** limited liability → **risk limited to the investment** → more people willing to buy shares → **business raises more finance for growth**.

> ⚠️ **Read who the question asks about.** This one asks about **the shareholder**, not the business. *"The business can raise finance"* is a business benefit and would be a different answer. Rule 102 — relevance by party — is the fault documented **five times** in the examiner reports.

---

## 10. Temporary employees — advantage for a business

**Asked:** *"Explain one advantage for a business of using **temporary employees**."* — June 2026 P2R

> **Model answer — 3 marks**
> Temporary employees are on short fixed-term contracts rather than permanent ones. **This lets the business take on staff only for a busy period, such as the weeks before Christmas**, so it is not paying wages in the quiet months when there is no work for them. **This makes the wage bill flexible and lowers costs**, and the business does not owe redundancy pay when the busy period ends.

**Second acceptable chain:** temporary staff → **fresh skills brought in for a specific project** → permanent staff learn from them → **capability improves without a long-term salary commitment**.

> ⚠️ **The mark earner is the *flexibility of cost*, not "it is cheaper".** Anyone can be paid less; the point of a temporary contract is that you stop paying when you stop needing.

---

## 11. On-the-job training — advantage for a business

**Asked:** *"Explain one advantage **of on-the-job training for a business**."* — June 2026 P2R

> **Model answer — 3 marks**
> On-the-job training means the employee learns while doing the actual job, usually supervised by an experienced colleague. **The business pays no external trainer or course fees**, and the employee is producing output while they learn. **This means the business gains a more capable worker at almost no direct cost**, and what they learn is exactly what this business's equipment and processes require.

**Second acceptable chain:** on-the-job training → **training matches this firm's own methods** → the employee becomes useful faster → **productivity rises sooner than after an off-the-job course**.

> ### ⚠️ ANSWER THE QUESTION ASKED, NOT THE NEAREST ONE
> **The question says "for a business."** A June 2022 candidate answered about the **employee** (*"less stressful… flexibility"*) and was marked down for it. **Benefits to the trainee score nothing here.**
> ⭐ **And the mirror-image trap**, from a June 2026 P1R answer on off-the-job training: candidates *"described in depth what off-the-job training **was**"* — a description of the method is knowledge the question did not ask for.

---

## 12. High market share — advantage

**Asked:** *"Explain one advantage to a business of having **high market share**."* — Nov 2025 P1

> **Model answer — 3 marks**
> Market share is the proportion of total sales in a market that one business holds. **A business with high market share is the one customers think of first**, so it gets more repeat custom without having to advertise for every sale. **This means its selling costs per unit are lower than its rivals'**, and it can often negotiate better terms from suppliers because it buys in the largest volumes.

**Second acceptable chain:** high market share → **dominant shelf space and distribution** → competitors find it harder to reach customers → **the business can protect its prices rather than discount**.

> ⚠️ **Don't say "it means more customers".** That restates market share. The mark is for **what high share lets the business *do*** — spend less to get each sale, and buy on better terms.

---

## 13. E-commerce — advantage of selling through it

**Asked:** *"Explain one advantage to a business of using **e-commerce to sell its products**."* — Nov 2025 P1

> **Model answer — 3 marks**
> E-commerce means selling through a website or app rather than only from a physical shop. **The business is not limited to customers who can travel to its premises**, so it can sell to anyone with an internet connection, including overseas buyers. **This widens the market without the cost of opening more shops**, so sales can grow while rent and staffing stay roughly the same.

**Second acceptable chain:** e-commerce → **open 24 hours with no staff on the tills at night** → sales happen when the shop would be shut → **more revenue from the same stock**.

> ⚠️ **The mark is not "more customers".** It is the **shop-less reach** — cheaper distribution than physical expansion. That is the causal step.

---

## 14. Mass marketing — advantage

**Asked:** *"Explain one advantage to a business of **mass marketing**."* — Nov 2025 P2

> **Model answer — 3 marks**
> Mass marketing means aiming one product at the whole market rather than at a segment. **Because the business makes one version for everyone, it produces at much larger volumes**, and large volumes bring economies of scale in production and in buying materials. **This lowers the unit cost, so the business can charge a low price and still profit**, which in turn wins it even more customers.

**Second acceptable chain:** mass marketing → **one national advertising campaign instead of many targeted ones** → **marketing cost per customer falls** → the brand is recognised almost everywhere.

> ⚠️ **The mirror image.** If the question had said *niche* marketing, the chain runs the opposite way: higher price, better fit, less competition. **Know both directions for the same topic** — this is exactly how the examiner creates a "State" trap.

---

## 15. Social objective — advantage for a business

**Asked:** *"Explain one advantage to a business of having a **social objective**."* — Nov 2025 P2

> **Model answer — 3 marks**
> A social objective means the business aims to benefit society as well as make money — for example reducing its packaging or paying staff a living wage. **Customers who care about these issues will choose it over a rival that does not**, and are often willing to pay slightly more. **This gives the business a way to compete that does not rely on being the cheapest**, and it attracts employees who want to work somewhere they believe in.

**Second acceptable chain:** a social objective → **better public relations and free positive press** → **cheaper marketing** and a stronger brand image → higher sales at the same price.

> ### ⚠️ THE DEFINITION TRAP — rule 07
> **A social objective is NOT a charity and the business is not government-owned.** A **social enterprise** is *independent* and *not government-owned*; the examiner has twice seen candidates lose marks on exactly this.
> ⭐ **And do not confuse a social objective with a *survival* objective** — a survival aim is about staying in business, not about helping society.

---

## 16. Break-even chart — limitation

**Asked:** *"Explain one **limitation** of a **break-even chart**."* — Nov 2025 P2

> **Model answer — 3 marks**
> A break-even chart plots costs and revenue on straight lines, which assumes **every unit costs the same to make and every unit sells at the same price**. In reality, a business often discounts to shift unsold stock, and bulk buying lowers material costs as output rises, so the lines are not straight. **This means the chart's break-even point is only an estimate**, and an owner who relies on it precisely may set the wrong output or price.

**Second acceptable chain:** a break-even chart shows costs and revenue but **not cash timing** → it cannot show that a profitable business still runs out of money before a debt falls due → **it gives a misleading picture of viability**.

> ### ⚠️ READ THE COMMAND WORD — "limitation", not "disadvantage"
> A **limitation** is about the **tool's accuracy or scope**. A **disadvantage** would be *"it takes management time to prepare"*. **Answering a limitation question with a cost/time disadvantage scores nothing.**
> ⭐ And note: **this came up in a series where the examiner also said break-even diagrams are not required elsewhere** — *"a limitation of a chart"* is a knowledge question, not a drawing question.

---

# WHAT BATCH 1 ESTABLISHES

Read the sixteen answers above side by side and the pattern is visible. **Every one is three sentences doing three jobs**, and they never vary:

| Sentence | Its job |
|---|---|
| **1** | **Define or identify the thing** — often built into the point itself |
| **2** | **The mechanism** — *this means / because / therefore* + a cause |
| **3** | **The business consequence** — profit, cost, sales, cash, reputation |

> ### ⭐ AND THE CONSEQUENCE IS ALWAYS ONE OF SIX THINGS
> **Lower costs · more sales · higher profit · more cash · better reputation · reduced risk.**
> If your third sentence does not land on one of those six, it is not a consequence yet. **Land it.**

---

## Batch 1 status and what comes next

| Batch | Content | Status |
|---|---|---|
| **1** | Newest 3-mark topics — June 2026 (11) + Nov 2025 (5) | ✅ **This file** |
| **2** | Historical 3-mark topics, by spec section 3.1–3.2 | ⬜ next |
| **3** | Historical 3-mark topics, 3.3–3.5 | ⬜ |
| **4** | 6-mark Analyse chains | ⬜ |
| **5–6** | 9-mark Justify option pairs | ⬜ |
| **7** | 12-mark Evaluate topics | ⬜ |

**Remaining: 246 of 262 governed items.**

---

# BATCH 2 — Spec 3.1 (Business activity) and the 3.2 structure cluster

**33 entries.** The clusters are merged into one entry each — partnership appears four times in the papers, the HR function three — **because the chain that earns the marks is identical and only the wording moves.** That deduplication is what makes the bank tractable.

---

# 3.1 — BUSINESS ACTIVITY AND THE EXTERNAL ENVIRONMENT

## 17. Partnership — one **advantage**

**Asked:** *"Explain one advantage of **a partnership**"* — May 2023 P1R · *"…of being **in a partnership**"* — Nov 2021 P1 · *"…of being in a partnership"* — June 2024 P1R

> **Model answer — 3 marks**
> A partnership is owned by **two or more people** who share the capital, the work and the profits. Because each partner puts money in, **the business has more capital than a sole trader could raise alone**, so it can afford better equipment or a second premises much sooner. **This lets it grow faster than a one-owner business**, and each partner also risks less than if they had funded it alone.

**Second chain:** partners bring **different skills** → one may handle finance while another handles customers → **decisions are better and fewer mistakes are made**.

> ### 🚨 THE ERROR TO AVOID
> **A partnership does NOT have limited liability.** Partners are personally responsible for the business's debts — this is an **unlimited liability** business form. **Writing "partners have limited liability" is factually wrong and will not score.** The advantages are **more capital · shared workload · combined skills**. Nothing else.

---

## 18. Partnership — one **disadvantage**

**Asked:** *"Explain one disadvantage of being **in a partnership**"* — June 2020 P1

> **Model answer — 3 marks**
> In a partnership the owners have **unlimited liability**, which means they are personally responsible for the business's debts. **If the business fails, each partner may have to sell personal assets — even their own home — to pay what is owed.** **This makes a partnership far riskier than a limited company**, so some people will not join one and others take on less risk than they otherwise would.

**Second chain:** profits are **shared between the partners** → each partner keeps less than a sole trader would → **less personal reward** for the same effort.

**Third chain:** decisions must be **agreed between partners** → disagreements slow decisions down → **the business reacts slowly to customers**.

> ⚠️ **2019 P1R recorded this exactly:** *"One third of candidates gained a mark for identifying a disadvantage of being in a partnership but then they would **not develop their answers**."* **Identify → explain why it matters → say what it costs.**

---

## 19. Sole trader — one **advantage**

**Asked:** *"Explain one advantage of being a **sole trader**."* — June 2022 P1

> **Model answer — 3 marks**
> A sole trader is **one person who owns and runs the whole business**. Because there are no other owners, **the owner keeps all of the profit** rather than sharing it. **This makes them more motivated to work hard and to keep costs low**, which raises the amount the business earns, and it also means they can make decisions instantly without asking anyone.

**Second chain:** the sole trader **makes every decision alone** → changes can be made immediately → **the business responds to customers faster than a larger firm**.

> ⚠️ **The mirror trap.** If the question asks about **disadvantages** of a sole trader, the answers run the other way: unlimited liability, harder to raise finance, the workload rests on one person, no one to cover illness. **Learn both sides of every business form** — the examiner flips the question word deliberately.

---

## 20. Franchisee — one **advantage**

**Asked:** *"Explain one advantage of being a **franchisee**."* — Summer 2019 P1R

> **Model answer — 3 marks**
> A franchisee pays the franchisor for the right to trade under **an established brand** and sell its proven products. **Customers already recognise the name and know what to expect**, so they buy from it from the day it opens, instead of the business having to build a reputation from nothing. **This means sales build far faster than for an independent start-up**, and the franchisor provides training and national advertising that a new owner could not afford alone.

**Second chain:** the franchisor supplies **proven products, equipment and staff training** → the franchisee avoids the mistakes of a brand-new business → **a much lower risk of failing than starting up independently**.

> ### 🚨 THE EXACT TRAP THE EXAMINER RECORDED
> Summer 2019 P1R: *"Some candidates **explained what a franchisee was but did not provide any advantage** of being a franchisee therefore **not gaining any marks**."*
> **A definition is not a benefit.** Open with the advantage, use the definition only as the mechanism. Only **one third** of candidates gained full marks here.

---

## 21. Multinational — one **benefit**

**Asked:** *"Explain one benefit of being a **multinational business**"* — Nov 2021 P2 · *"…one advantage of **becoming** a multinational business"* — May 2023 P2R

> **Model answer — 3 marks**
> A multinational is a business that **operates in more than one country**. **Producing in a country where wages and land are cheaper lowers the cost of each unit**, so the business can cut its price or keep a larger margin. **And because it sells in several markets at once, a fall in demand in one country is absorbed by the others**, so its revenue is more stable than a business trading in only one place.

**Second chain:** operating inside another country **avoids the import tariffs and quotas** that a foreign exporter would pay → **goods reach customers more cheaply** than a competitor shipping them in.

> ⚠️ **Measure the third sentence.** *"It makes more profit"* is not enough — say **why** profit is more secure: **spread demand across countries**, or **lower costs from cheaper inputs**. ⭐ And note Nov 2021 P2 Q2(d): *"A number of candidates mentioned that the business is world-wide **but then did not develop the comment**."*

---

## 22. Globalisation — one **benefit to a small business**

**Asked:** *"Explain one benefit of **globalisation to a small business**."* — Nov 2023 P1

> **Model answer — 3 marks**
> Globalisation means **countries trade more freely with each other** and customers can buy from abroad more easily. **A small business can now sell through its website to customers in other countries** without opening premises overseas, so its market is not limited to the town it sits in. **This means its sales can grow far beyond what local demand would allow**, while its costs stay those of a small operation.

**Second chain:** globalisation gives a small business access to **cheaper overseas suppliers** → its material costs fall → **it can compete on price with larger rivals**.

> ### ⚠️ RELEVANCE BY PARTY — read the noun
> The question says **a small business**. A **large** business is a different answer (Nov 2023's examiner noted candidates who wrote about **large** firms' concerns). Recorded as **rule 102**, the fault appears **five times** in the reports. **Circle the party before you plan.**

---

## 23. Trading bloc — one **advantage for a country**

**Asked:** *"Explain one advantage for **a country** of being **in a trading bloc**."* — Nov 2024 P2

> **Model answer — 3 marks**
> A trading bloc is **a group of countries that agree to trade with each other without barriers such as tariffs**. **Businesses in a member country can export to the other members without paying import taxes**, so their goods cost less abroad and they win customers they otherwise could not reach. **This raises the country's exports, which creates jobs and brings money into the economy.**

**Second chain:** being inside a bloc makes it **cheaper to move materials between members** → manufacturers locate there to serve the whole bloc → **the country attracts foreign investment**.

> ### 🚨 RELEVANCE BY PARTY AND THE 2024 ERROR
> **This question asks about the COUNTRY, not a business.** Writing *"the business can sell more"* is the wrong party.
> ⚠️ **And the examiner recorded the exact misconception:** *"others **confused the term and wrote about protectionism** rather than **liberalising trade**."* **A trading bloc removes barriers between members — it is the opposite of protectionism.** Do not write about tariffs being *put up*.

---

## 24. Business failure — one **reason**

**Asked:** *"Explain one reason why **businesses fail**"* — June 2021 P2 · *"…why a business **might fail**"* — May 2023 P1R

> **Model answer — 3 marks**
> Many new businesses **start without enough capital** to survive the first months, when they have costs but few customers yet. **They cannot afford to advertise properly or to hold enough stock**, so customers never find them or leave disappointed when items are unavailable. **Sales stay below what is needed to cover the rent and wages, and the business runs out of money and closes.**

**Second chain:** the business **misjudged demand** — it produced what the owner liked rather than what customers wanted → stock remains unsold → **no cash comes in and the business cannot pay its bills**.

**Third chain (from Batch 1, entry 4):** **poor cash flow** — profitable on paper but no money in the bank when a debt falls due.

> ⭐ **Three separate routes score here. Learn all three** — undercapitalisation, misjudged demand, and cash flow — because the same question appears in more than one series and only one is needed. ⚠️ **Never simply write "because it runs out of money"** — that restates failure instead of explaining it.

---

## 25. Not achieving predicted growth — one **disadvantage**

**Asked:** *"Explain one disadvantage for a business that **does not achieve its predicted growth**."* — June 2021 P2

> **Model answer — 3 marks**
> A business that plans to grow **buys machinery, hires staff and takes on a bigger building in advance**, expecting the extra sales to pay for them. **If the growth does not happen, it is carrying costs sized for a business much larger than it actually is**, so each sale has to absorb more fixed cost. **This squeezes profit, and the business may have to make staff redundant or sell equipment it no longer needs** — losing money on assets it bought at full price.

**Second chain:** growth targets are often set to **satisfy investors or a bank** → missing them **damages confidence** → the bank may refuse further lending exactly when the business needs it most.

> ⚠️ **This is the mirror image of the "economies of scale" entry (Batch 1, entry 3).** Expansion helps only if sales follow. **If they do not, fixed costs rise while revenue does not — diseconomies of scale.** Learn the pair together.

---

## 26. Interest rates — an **increase**

**Asked:** *"Explain one impact of an **increase in interest rates** on a business."* — June 2020 P1

> **Model answer — 3 marks**
> An increase in interest rates raises the cost of borrowing. **A business with an overdraft or a loan must pay more interest each month for the same amount of debt**, and that extra payment is a cost that produces nothing. **This reduces profit without any change in sales**, and it may also stop the business investing, because new machinery now costs more to finance.

**Second chain:** higher rates mean customers pay more on their own mortgages and loans → **they have less spare income** → demand for non-essential goods falls → **the business sells less**.

> ⭐ **Two independent routes score 3 marks each — the business's own borrowing, or its customers' spending.** Either is a complete answer. ⚠️ Note the mirror for a **fall** in rates: cheaper borrowing, more investment, customers spend more.

---

## 27. Interest rates — banks **reduce** them

**Asked:** *"Explain one advantage for **businesses** if **banks reduce their interest rates**."* — June 2022 P2R

> **Model answer — 3 marks**
> Cheaper interest means the cost of servicing existing debt falls. **A business paying a variable rate on its loan or overdraft hands over less each month for the same borrowing**, so more of its revenue is kept as profit. **That extra retained money can be spent on new equipment or extra staff to grow the business**, rather than being handed to the bank.

**Second chain:** lower rates make **customers' borrowing cheaper too** → they have more disposable income and are more willing to buy on credit → **demand for the business's products rises**.

> ⚠️ **Answer to "advantage for businesses" — both routes are about the business.** Do not drift into describing the effect on the wider economy; the question names **businesses** as the party.

---

## 28. Tariffs — one **effect on a business importing goods**

**Asked:** *"Explain one way that the **introduction of tariffs** might affect a business **importing goods**."* — June 2025 P1R

> **Model answer — 3 marks**
> A tariff is **a tax charged on goods coming into the country**. A business that imports its raw materials must now pay that tax on every delivery, so **the landed cost of each unit rises even though nothing about the product has changed**. **This forces the business either to raise its prices — and risk losing customers to cheaper domestic rivals — or to accept a lower profit margin on every sale.**

**Second chain:** imported components become dearer → the business **looks for domestic suppliers instead** → it may lose the quality or specification it relied on, or pay more while it changes supply.

> ### 🚨 A REAL 0-MARK ANSWER, QUOTED IN THE REPORT
> *"With tariffs, importing goods may be **cheaper**, allowing this business to import more at a lower cost… Therefore, potentially increasing revenue."*
> **Examiner: "This answer incorrectly addresses the question. 0 marks."**
> **A tariff RAISES the cost of imports.** Getting this direction backwards scores nothing, however well written the rest is. **Check the direction of every economic effect before you build on it.**

---

## 29. Complying with health and safety legislation — one **reason**

**Asked:** *"Explain one reason why a business **complies with health and safety legislation**."* — June 2022 P2

> **Model answer — 3 marks**
> Health and safety law sets **the minimum standards an employer must meet** to keep workers safe. **A business that ignores it faces fines, prosecution and possibly being ordered to stop operating**, which can destroy a small firm. **Complying therefore protects the business's licence to trade and its reputation**, and it reduces the cost of accidents — lost working days, compensation and higher insurance premiums.

**Second chain:** a safe workplace **reduces accidents and sick leave** → output is not disrupted → **the business avoids the cost of replacing and retraining injured staff**.

> ### ⚠️ REPEALING THE "BECAUSE IT'S THE LAW" TRAP
> *"Because it is the law"* states the requirement, not the **reason**. The mark is for **what complying protects the business from** — fines, closure, compensation, reputational damage. **Always convert the legal duty into a business consequence.**

---

# 3.2 — PEOPLE IN BUSINESS: structure and the HR function

## 30. The human resource function — purpose and responsibilities

**Asked:** *"Explain one reason why **many businesses have a human resource functional area**"* — Summer 2019 P1 · *"…one **responsibility** of the human resources function"* — June 2020 P1R · *"…one reason why many businesses have a **human resource function**"* — June 2024 P1

> **Model answer — 3 marks**
> The human resource function is **the department responsible for the people a business employs** — recruiting them, writing their contracts, training them and handling discipline. **Because one department looks after every employee in the same way, recruitment and pay are handled consistently and fairly**, so the business is less likely to break employment law and face a tribunal. **This means managers in other departments can concentrate on production and sales instead of staffing problems.**

**Second chain:** HR **forecasts how many staff with which skills the business will need** → it can recruit and train ahead of demand → **the business is not short of the right people when it expands**.

> ### 🚨 THE KNOWLEDGE GAP THE EXAMINER NAMED TWICE
> Summer 2019 P1 **Q02b** was a **State** question on a function of the finance area — *"**less than one fifth** of candidates were able to correctly identify"* it.
> November 2023 P1 Q2(b) — a task of an HR employee — ***"only one tenth of candidates"*** identified one.
> **These are 1-mark questions being missed by 80–90% of candidates.** ⭐ **Know concrete tasks for each function**, not vague labels:
> | Function | Concrete tasks to have ready |
> |---|---|
> | **Human resources** | recruiting · writing job descriptions and contracts · arranging training · handling discipline and grievances · staff welfare |
> | **Finance** | keeping accounts · preparing the cash flow forecast · paying wages · arranging loans · calculating costs and profit |
> | **Marketing** | market research · designing the marketing mix · advertising campaigns · branding and packaging |
> | **Operations** | production scheduling · stock control · quality · machinery maintenance |

---

## 31. Short **span** of control — one reason

**Asked:** *"Explain one reason why a business would have a **short span of control**."* — Summer 2019 P1R

> **Model answer — 3 marks**
> A span of control is **the number of employees one manager directly supervises**. With a short span the manager oversees only a few, so **each worker gets close attention, and problems are spotted and corrected before they become costly**. **This suits complex, skilled or dangerous work**, where a mistake is expensive or unsafe, and it also means staff can be trained and supported individually — which raises quality and reduces accidents.

**Second chain:** a short span means **more managers are needed** to cover the same staff → **each employee is answerable to someone clearly** → instructions and responsibility are unambiguous.

> ### 🚨 SPAN OF CONTROL IS NOT CHAIN OF COMMAND
> | Term | What it counts |
> |---|---|
> | **Span of control** | how many staff **one manager** supervises directly |
> | **Chain of command** | how many **layers** of management sit between the top and the bottom |
> ⚠️ **The examiner recorded the confusion:** November 2023 P1 — ***"some candidates confused this [span of control] with hierarchical levels within an organisation structure."***
> ⭐ **And check the direction.** This entry is *why a business would **choose** a short span* — a deliberate design decision for close supervision. The mirror (a business has a short span because it is **small**) is a different answer and less good.

---

## 32. Short **chain** of command — one benefit

**Asked:** *"Explain one benefit to a business of having a **short chain of command**"* — Summer 2019 P2 · *"…having a short chain of command"* — June 2024 P2

> **Model answer — 3 marks**
> A short chain of command means there are **few layers of management between the owner and the people doing the work**. **Instructions reach the staff who act on them without being passed down through several managers**, so messages are neither delayed nor altered on the way. **This lets the business respond to a customer request or a problem on the shop floor almost immediately**, which a taller structure cannot do.

**Second chain:** fewer layers means **fewer managers' salaries** → **overheads are lower** → the business keeps more of each sale as profit.

> ⭐ **This is the mirror of Batch 1 entry 1** (*the disadvantage of a **long** chain of command*). Learn the pair — the examiner asks both directions across series, and the chain simply reverses.

---

## 33. Flat organisational structure — one benefit

**Asked:** *"Explain one benefit to a business of having a **flat organisational structure**."* — June 2022 P1

> **Model answer — 3 marks**
> A flat structure has **very few levels of management and wide spans of control**, so most staff report to one or two managers. **Because there are fewer managers to pay, the business's wage bill is lower** and more of its revenue is left as profit. **It also means employees are given more responsibility for their own work**, which raises motivation and lets decisions be made quickly by the people closest to the customer.

**Second chain:** staff in a flat structure **can speak directly to senior managers** → good ideas reach decision-makers → **the business improves faster than one where ideas must climb a hierarchy**.

> ⚠️ **Do not confuse "flat" with "small".** A large business can deliberately choose a flat structure to cut overheads — **the question asks about the structure, not the size**.

---

## 34. Decentralised organisation — one advantage

**Asked:** *"Explain one benefit to a business that has a **decentralised organisational structure**"* — May 2023 P1 · *"…one advantage to a business of having a **decentralised organisation**"* — June 2024 P1

> **Model answer — 3 marks**
> Decentralisation means **authority to make decisions is passed down to managers in each region, branch or department** rather than kept at head office. **Local managers know their own customers, staff and competitors**, so the decisions they take fit the local market far better than one rule applied everywhere. **This improves customer service and speeds up decisions**, because a local manager does not have to wait for approval from head office.

**Second chain:** responsibility is pushed down → **local managers feel trusted and are more motivated** → staff stay longer and perform better.

> ⭐ **The mirror is centralisation** — consistency across branches, one clear brand, easier control, bulk buying. **Know both.** ⚠️ The examiner's recurring complaint about this topic: candidates describe **what** decentralisation is and never reach **what it gives the business**.

---

## 35. Improving communication with employees — one benefit

**Asked:** *"Explain one benefit to a business of **improving communication with its employees**."* — June 2022 P1R

> **Model answer — 3 marks**
> When a business communicates well, **every employee knows what is expected of them and why it matters**. **This reduces misunderstanding and mistakes** — work is done right the first time instead of being repeated, saving materials and time. **It also makes staff feel informed and valued, so they are more motivated**, and motivated staff work more productively and are less likely to leave.

**Second chain:** better communication lets **staff raise problems early** → faults are fixed before they reach the customer → **fewer complaints and returns**.

> ⚠️ **This is a benefit question, so every sentence must be a *gain*.** If you write *"poor communication causes mistakes"*, you are answering the **impact of ineffective communication** — the next entry — not this one.

---

## 36. Ineffective communication — one **impact**

**Asked:** *"Explain one impact of **ineffective communication** on a business."* — May 2023 P1R · *"…one impact on a business of ineffective communication"* — June 2024 P1

> **Model answer — 3 marks**
> Ineffective communication means **a message is misunderstood, delayed or never delivered**. **Employees then carry out work that does not match what was asked for** — the wrong quantity, the wrong specification or the wrong deadline — and the work has to be done again. **This wastes materials, labour and time, raising the cost of every unit**, and if the error reaches the customer it causes complaints and lost future sales.

**Second chain:** messages are delayed → **decisions cannot be made when they are needed** → the business misses opportunities such as a supplier's deadline or a seasonal selling window.

> ⭐ **The verified June 2025 answer that scored 3/3 used exactly this shape:** *"Messages being delayed or sent to the wrong receiver might cause decision making to slow down. This can cause the business to **miss out on opportunities such as securing a deal with a new supplier**."* **Generic → specific consequence.**

---

## 37. Using a **letter** to communicate with an employee — one reason

**Asked:** *"Explain one reason why an **employer might use a letter** to communicate with an employee."* — June 2025 P2R

> **Model answer — 3 marks**
> A letter is a **formal, written message that can be kept on file**. **Some matters must be recorded in writing** — a change to someone's contract, a warning, a promotion or a redundancy — because the employee and the business may later need proof of what was said. **This gives the business a dated record it can rely on in a tribunal or dispute**, which a verbal message cannot.

**Second chain:** a letter is **delivered to a named person and read privately** → a sensitive message is not overheard by others → **confidentiality is preserved**, which protects the employee's dignity and the business's professionalism.

> ⚠️ **The mark is the *formal record* — not "letters are old-fashioned" or "letters are clear".** The examiner is asking you to match **the channel to the message**: formal and confidential subjects need a written, private channel.

---

## 38. Health and safety training **as part of induction** — one reason

**Asked:** *"Explain one reason why employees should undertake **health and safety training as part of their induction programme**."* — June 2020 P2

> **Model answer — 3 marks**
> An induction programme is **the training a new employee receives in their first days**, before they work unsupervised. **If safety training happens then, the employee never has a chance to learn unsafe habits**, because they are taught the correct procedure from the very first time they use the equipment. **This reduces accidents to new staff — who are the most likely to have them — cutting lost working days, compensation claims and higher insurance premiums.**

**Second chain:** induction safety training is a **recorded, legal duty** → the business can prove it trained the employee → **it is protected from prosecution if an accident does occur**.

> ⭐ **The reason to put it in *induction* specifically is that new starters are the highest-risk group.** A generic answer about safety training misses the word the examiner put in the question.

---

## 39. Equal opportunities — one way businesses ensure them

**Asked:** *"Explain one way businesses ensure that **all employees have equal opportunities**."* — May 2023 P2R

> **Model answer — 3 marks**
> One way is to **use the same job description, person specification and selection criteria for every applicant**, and to record why each candidate was rejected against those criteria. **This means a decision can be shown to be based on the applicant's ability rather than their sex, race, age or religion**, and anyone who is passed over can be given a reason. **The business therefore avoids employment tribunal claims and the fines and bad publicity that follow, and it recruits from the whole pool of available talent rather than half of it.**

**Second chain:** advertise vacancies **where all sections of the community will see them** → a wider range of people applies → **the business can choose the best person rather than the nearest one**.

> ⚠️ **"One way" means a method, not a benefit.** Describe **what the business does** (uses the same criteria · advertises widely · trains managers on bias · monitors promotion rates) and then **why it matters**. Answering with a benefit where a method was asked is a command-word failure.

---

## 40. Supporting employees with disabilities — one way

**Asked:** *"Explain one way businesses **support employees with disabilities**."* — June 2024 P2R

> **Model answer — 3 marks**
> One way is to **adapt the workplace and the work itself** — fitting a ramp, providing a modified keyboard or screen reader, or allowing a different shift pattern so someone can travel outside peak hours. **This lets the person do the job they were hired for without the disability becoming the obstacle**, so the business keeps an experienced employee instead of losing them. **It also widens the group of people the business can recruit from**, and it is often required by law, so acting early avoids tribunal claims.

**Second chain:** train managers and colleagues **so nobody treats the employee differently** → the person feels part of the team → **they stay longer and work more productively**.

> ⚠️ **As with entry 39, the command word is "one way" — a method.** And note the equality angle: **the business gains** (keeps skills, broader recruitment, legal protection). **Charity is not the answer; advantage is.**

---

## 41. Full-time employees — one benefit

**Asked:** *"Explain one benefit for a business of having **full-time employees**."* — June 2020 P2

> **Model answer — 3 marks**
> A full-time employee works **all the business's normal hours every week**, rather than for a fixed short period. **Because they are always there, they build up detailed knowledge of the products, the customers and the procedures**, so they handle unusual situations without being supervised and make fewer mistakes. **This gives customers consistency and the business reliable cover**, and the employer repays the commitment with loyalty — so fewer staff leave and recruitment and training costs fall.

**Second chain:** full-time staff can be **given responsibility and promotion** → the business develops future supervisors from within → **it saves the cost of recruiting experienced managers externally**.

> ⚠️ **Contrast with entry 42 (seasonal staff) and Batch 1 entry 10 (temporary employees).** All three are employment-type questions and the examiner flips between them. **The variable is the trade-off: permanence for reliability, versus flexibility for cost.**

---

## 42. Seasonal staff — one reason

**Asked:** *"Explain one reason for a business **using seasonal staff**."* — June 2020 P2

> **Model answer — 3 marks**
> Seasonal staff are taken on **only for the part of the year when demand peaks**, such as a shop at Christmas or a hotel in summer. **The business can serve far more customers in its busiest weeks** without turning them away, so it captures sales it would otherwise lose. **And when the season ends the contracts finish**, so the business is not paying wages through the quiet months or making redundancies it cannot afford.

**Second chain:** seasonal workers are often **experienced in that season's work** → they can be useful with very little training → **the business avoids the cost of a long induction**.

> ⭐ **Two halves, and the second is the one candidates forget: gain the peak sales, then lose the cost in the trough.** A one-sided answer about "more staff to help" is worth 1 mark.

---

## 43. Retaining employees — one benefit

**Asked:** *"Explain one benefit to a business of **retaining its employees**."* — Summer 2019 P2R

> **Model answer — 3 marks**
> Retention means **keeping existing staff rather than losing them and hiring replacements**. **Every leaver has to be recruited, inducted and trained again, and for a period they produce less than an experienced worker**, so holding on to someone avoids all of that spending. **The business keeps the skills and customer relationships that person built up**, which a replacement must start from scratch.

**Second chain:** long-serving staff **know regular customers by name and understand what they want** → customers receive better service → **they return and spend more**.

> ⚠️ **The temptation is to write "it saves money".** Say **what** the money would have been spent on — **advertising the vacancy, management time interviewing, induction and training, and the drop in output while the new person learns**.

---

## 44. Fully trained employees — one reason

**Asked:** *"Explain one reason why a business has **fully trained employees**."* — June 2022 P2R

> **Model answer — 3 marks**
> A fully trained employee has **been taught the correct way to do every part of their job, including the equipment and the safety rules**. **Because they do not have to guess, they make fewer mistakes and produce less waste**, so less material is thrown away and less work has to be repeated. **This lowers the cost of each unit and raises the quality the customer receives**, which protects the business's reputation.

**Second chain:** trained staff **can cover for each other and take on more tasks** → the business needs fewer people to run the same operation → **labour costs per unit fall**.

> ⚠️ **Do not answer with "so they can do their job"** — that is the definition of trained, not a reason. The mark is for **the business consequence of the training**: less waste, higher quality, lower cost, fewer accidents.

---

## 45. Employees keeping their **CV up to date** — one reason

**Asked:** *"Explain one reason why **employees keep their curriculum vitae (CV) up to date**."* — June 2021 P2

> **Model answer — 3 marks**
> A CV is **a written summary of a person's qualifications, skills and work history**. **If an employee loses their job at short notice they may need to apply for a new one within days**, and a CV that has not been updated for years will leave out the experience and training they have gained most recently. **Keeping it current means they can apply immediately and present their strongest case**, which matters most when they are competing against many other applicants.

**Second chain:** updating a CV encourages an employee to **notice the skills they have gained** → they can see their own progress and use it to **ask for a promotion or a pay rise** inside the business.

> ### 🚨 READ WHO THE QUESTION IS ABOUT
> **This asks why the EMPLOYEE keeps it up to date — not why the business benefits.** A single CV helps one person; a business does not benefit from an employee having a tidy CV. **Relevance by party — rule 102 — is the single most costly error in the qualification, documented five times.**

---

## 46. Motivating employees — one benefit

**Asked:** *"Explain one benefit for a business of **motivating its employees**"* — June 2022 P1R · *"…one method a business could use to **motivate** its employees"* — June 2022 P2R

> **Model answer — 3 marks**
> A motivated employee **wants to do the job well rather than merely avoid being told off**. **They work faster and take more care**, so the same number of staff produces more output of better quality — raising productivity and reducing waste at the same time. **This lowers the cost of each unit**, so the business earns a bigger profit on every sale, and motivated staff are far less likely to leave.

**Second chain:** motivated staff deal with customers **more helpfully and patiently** → customers return and recommend the business → **sales rise without extra advertising**.

### ⭐ AND THE "METHOD" VARIANT
The June 2022 P2R question asked for a **method**, not a benefit — so the answer must be an action:
> **Model — 3 marks.** One method is **job rotation, where employees swap between different tasks on a rota**. **Doing the same job repeatedly becomes boring, and rotating gives variety and lets staff learn new skills**, which makes the work more interesting. **The business gains a more flexible workforce** that can cover for absences or move to whichever task is busiest, so it copes with change without hiring.

> ### 🚨 BENEFIT vs METHOD — the command-word trap
> **"Benefit of motivating" wants a consequence. "Method to motivate" wants an action taken.** ⚠️ And on the **Justify** questions about motivation the examiner states: ***"there are no knowledge marks"*** — listing Maslow or Herzberg adds nothing.

---

## 47. Herzberg's motivational theory — one factor

**Asked:** *"Explain one of the **factors in Herzberg's motivational theory**."* — June 2020 P2

> **Model answer — 3 marks**
> Herzberg divided what affects workers into **hygiene factors** — pay, working conditions, job security — and **motivators** — achievement, recognition, responsibility and advancement. Take **recognition**: **praising an employee for work that was done well tells them their effort was noticed**, which is a reward it costs the business nothing to give. **The employee takes more pride in the work and repeats the standard**, whereas ignoring good work leaves them feeling taken for granted and they do only enough to get by.

**Second chain — hygiene, e.g. job security:** an employee who fears redundancy **cannot concentrate on the work** → they look for another job → **the business loses them and pays to recruit a replacement**.

> ### ⭐ THE ONE THING TO KNOW ABOUT HERZBERG FOR 4BS1
> **Hygiene factors stop dissatisfaction; only motivators create motivation.** High pay on its own will not make someone work harder — it only prevents them resenting the job. **That single distinction is what the question is testing.**
> ⚠️ **Do not write "Hertzberg" or "Maslow" and stop.** The examiner wants **one named factor, explained through to what the business gains**.
> ⭐ **CONTENT GAP, NAMED BY THE EXAMINER:** Herzberg appears on the list of topics examiners say candidates do not know. **Learn three motivators and three hygiene factors by name.**

---

## 48. Fringe benefits — one reason

**Asked:** *"Explain one reason why a business uses **fringe benefits**."* — Summer 2019 P2

> **Model answer — 3 marks**
> Fringe benefits are **rewards given on top of wages** — a company car, free or subsidised meals, private health cover, gym membership. **They allow the business to offer a better overall package than rivals who pay the same wage**, so it can attract stronger applicants without permanently raising every salary it pays. **Staff who value the benefits stay longer**, which saves the cost of recruiting and training replacements.

**Second chain:** fringe benefits such as free meals or health cover **improve employees' wellbeing and attendance** → fewer days lost to sickness → **output is not disrupted and productivity rises**.

> ### 🚨 A REAL 0-MARK ANSWER FROM JUNE 2026
> *"One impact of using fringe benefits to their employees is that **it reduces their salaries** which can demotivate the employees resulting in a loss for business…"*
> **Examiner: "0 marks awarded as the candidate has attempted an impact on the employee rather than the business."**
> **Two failures at once: a wrong premise (fringe benefits do not reduce salaries) and the wrong party (this was a "benefit to the business" question).**

---

## 49. Paying above the minimum wage — one reason

**Asked:** *"Explain one reason why a business **would pay its employees above the minimum wage**."* — June 2022 P2

> **Model answer — 3 marks**
> The minimum wage is **the legal floor an employer must pay**, so paying above it is a deliberate choice. **Offering more attracts a larger and better pool of applicants**, letting the business pick the most capable rather than whoever will accept the lowest pay. **It also makes existing staff less likely to leave for a rival**, saving the recruitment and training costs of replacing them, and better-paid staff tend to take more care in their work.

**Second chain:** pay above the minimum **signals that the business values its staff** → they work harder and co-operate more → **productivity rises** and the extra wage cost is covered by the extra output.

> ### 🚨 THE STATE TRAP ON THIS EXACT TOPIC — A 10% QUESTION
> ⚠️ **Do not confuse this 3-mark Explain with the 1-mark State version.** On **Examine** you explain; on **State** you must be **in context** — *"a reason why **Huawei** would pay above the minimum wage"* requires a Huawei-specific reason or phrase.
> **Ideal answer (from the Nov 2024 report):** *"Many candidates stated it was a quick, easy or an **unbiased** method which is **not correct**"* — that is the focus-group trap, but the pattern is the same: **a plausible-sounding phrase that is simply untrue scores nothing.** **Only use a reason you can develop.**

---

---

# BATCH 3 — Spec 3.3 (Marketing)

**23 entries.** Marketing is the largest remaining cluster: 33 of the 151 three-mark blocks sit in 3.3, in 23 distinct topics.

> ## ⭐⭐ A NEW LABEL, AND WHY IT IS NEEDED
> Batches 1 and 2 were `[CONSTRUCTED GRADE 9 TARGET]` throughout. **Batch 3 is different: for almost every entry below, Pearson's own mark scheme prints a worked answer** — the *"Award 1 mark for … (1) … (1) … (1)"* model that the scheme accepts as a full-mark response.
> That is a **third source category**, and the labelling contract has only two labels, so this batch uses a third and defines it:
>
> | Label | What it is | What it is NOT |
> |---|---|---|
> | `[VERIFIED CANDIDATE EXEMPLAR]` | a real student script that an official Pearson report scores at full marks (session, paper, question, page cited) | — |
> | **`[OFFICIAL MARK-SCHEME WORKED ANSWER]`** | **Pearson's own indicative content, quoted verbatim, carrying the scheme's own (1)(1)(1) allocation** | **not a candidate script · not examiner-marked · no candidate wrote it** |
> | `[CONSTRUCTED GRADE 9 TARGET]` | engineered by me from QP + MS + ER | not official, not a student script, not examiner-marked |
>
> **Every entry below states which of its chains come from the scheme and which are mine.** Where a chain is labelled *scheme*, the (1) markers are Pearson's, and the route is one the scheme explicitly accepts. **This still does not make it a marked script** — it is the scheme's own model, which is the strongest thing that exists for a 3-mark question, but it is a different kind of evidence and it is labelled as such.

> ### ⭐⭐ THE 3-MARK MARKETING RULE, AND IT IS NEW
> **`NB No marks are awarded for a definition.`**
> This line appears in the mark schemes for **May/June 2020 P2R, May/June 2022 P2, May 2023 P2R, Nov 2024 P1, Nov 2024 P2 and June 2026 P2** — six series, and it is in none of them by accident.
> **Do not open these answers by defining the term.** *"E-newsletters are electronic newsletters"* scores **0**. *"Above-the-line promotion is promotion through the media"* scores **0**. The first mark is for a **method / reason / benefit**, not for a definition — so start with the thing itself and spend all three sentences on **what it does and what follows**.

---

# 3.3.1 — THE MARKET AND MARKET RESEARCH

## 50. Market research — one **purpose**

**Asked:** *"Explain one purpose of market research for a business."* — May/June 2020 P1

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> A purpose of market research is **to identify your customers' needs** (1) — the business finds out what people actually want before it commits money to a product. **This helps it design products that meet those needs** (1) rather than guessing and building something nobody wants. **That makes the business more successful** (1), because it is spending on products that will actually sell.

**The chain, broken out**
1. **Identify customer needs** — the purpose itself.
2. **Design the product to meet them** — what the business does with the finding.
3. **The business is more successful** — sales/profit consequence.

**A second acceptable route** *(scheme, May/June 2020 P1)*
*Reduce the risk of failure* → a new product is tested on real customers before launch → **the business does not waste money on something unwanted**.

**More purposes you can use, if they chain honestly:** to find out the size of the market · to find out what competitors charge · to see whether a price will be accepted · to identify a gap in the market.

> ⚠️ **The word "purpose" is doing the work here.** A purpose is **why the business does it** — so the answer must be a reason to research, not a description of a research *method*. *"A purpose is to hand out questionnaires"* is a method and answers a different question.

---

## 51. Questionnaires — one **disadvantage**

**Asked:** *"Explain one disadvantage of using questionnaires as a method of market research."* — May/June 2022 P2

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> **If the questionnaire is too long (1)** people may be **reluctant to complete it** (1) — they lose interest and stop part-way through. **They may then not give true answers** (1), so the business makes decisions on information that looks like data but is not accurate.

**The chain, broken out**
1. **The questionnaire is too long** — this is the identification; a questionnaire-specific flaw.
2. **People will not complete it / lose focus** — the behavioural consequence.
3. **The data is wrong or too thin** — the consequence to the *business*.

**A second acceptable route** *(scheme, same question)*
*Too many questions* → **people do not focus properly** (1) → **a low rate of return** (1) → **the business does not get the information it needed** (1).

**More disadvantages that chain properly:** closed questions **limit the answers** → the respondent cannot say what they really think → the business misses the real reason customers behave as they do · posted questionnaires get **a poor response rate** → the sample is too small to be representative → the findings cannot be trusted · people may **lie to appear sensible** → the business acts on false information.

> ⭐ **Notice the shape: the flaw is in the *method*, and the third sentence is about the *information*.** A questionnaire disadvantage that ends on "it costs money" has stopped one link early — costs apply to every method and do not distinguish a questionnaire.

---

## 52. Secondary market research — one **benefit** or **reason**

**Asked:** *"Explain one benefit to a business of using the internet to carry out secondary market research."* — May/June 2020 P2R · *"Explain one benefit to a business of using secondary market research."* — May/June 2021 P1 · *"Explain one reason why secondary research would be used by a business."* — Nov 2021 P2

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> Secondary research **already exists and is available** (1) — the business does not have to go out and gather it. **This saves the business a great deal of time and effort** (1) that would otherwise be spent collecting data itself. **The information can then be used to develop its products or to learn about other businesses** (1), so the saving converts into something useful rather than just being a saving.

**The chain, broken out**
1. **The data already exists** — secondary means second-hand, collected by someone else.
2. **Saves time, effort or money** — the immediate benefit.
3. **The saving is used** — quicker decision, more funds for something else, or the data used to develop a product.

**A second acceptable route** *(scheme, May/June 2021 P1)*
**Businesses save money by not carrying out the research themselves** (1) → **the information is freely accessible on the internet** (1) → **they can access a large amount of information at no cost** (1).

**A third acceptable route** *(scheme, May/June 2020 P2R)*
**Access to a large volume of data** (1) → **they do not have to go out and collect it themselves** (1) → **it is much cheaper and quicker because someone else has already done it** (1).

> ⚠️ **The distinction that must be right:** secondary = **data that already exists** (government statistics, competitor websites, reports, newspaper articles, internal sales records). Primary = **collected first-hand** (surveys, interviews, questionnaires, observation, focus groups). **Calling a questionnaire "secondary research" is the commonest error on this question** and it earns nothing.
> ⚠️ **A weak secondary-research advantage: "it is more accurate."** It usually is not — it was collected for someone else's purpose, so it may be out of date or not quite fit. Use **cheaper · quicker · large volume**, which are the scheme's own points.

---

## 53. Using market research information — one **way**

**Asked:** *"Explain one way a business could use market research information."* — May 2023 P1

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> The business can **find out what customers think of its products** (1) — the research tells it what is working and what is not. **It can then act on the feedback it has collected** (1), changing the product, the price or the way it is promoted. **As a result it better meets the needs of its customers** (1), which is what turns the information into sales.

**The chain, broken out**
1. **Find out what customers think** — the use.
2. **Act on the feedback** — the decision the business takes.
3. **Better meets customer needs** — the outcome.

**A second acceptable route** *(constructed)*
Use the research to **set the price** → the business knows what customers are willing to pay → **it avoids pricing itself out of the market**.

**A third** *(constructed)* — use it to **choose where to locate** → the research shows where the target customers are → **the shop gets more passing trade**.

> ⚠️ **The trap is stopping at "to make decisions".** *"A business can use market research to make better decisions"* is not developed — the examiner cannot see which decision, or what improves as a result. **Name the decision and name the outcome.**

---

## 54. Focus groups — one **advantage**

**Asked:** *"Explain one advantage of using focus groups when carrying out market research."* — Nov 2024 P2

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> Using a focus group means the researchers **talk directly to the people in the group** (1) rather than through a form. **This means they may get a more truthful answer** (1) — people say more in conversation than they write on a questionnaire. **This allows the researchers to gain in-depth insights into consumers' thoughts, feelings and motivations** (1), which is exactly what a business needs when a decision is finely balanced.

**The chain, broken out**
1. **Direct discussion with the group** — the method's distinctive feature.
2. **More honest, fuller answers** — the immediate advantage.
3. **Depth and reasoning, not just numbers** — what the business gets that a survey cannot give it.

**A second acceptable route** *(scheme, same question)*
**A variety of people discuss the research together** (1) → **detailed notes of the discussion can be taken** (1) → **they can be analysed later** (1).

> 🚨 **THE REPORTED ERROR — from the Nov 2024 report, on this exact question:**
> *"Many candidates stated it was a **quick, easy or an unbiased** method which is **not correct**."*
> A focus group is **not** quick (it must be arranged, run and written up), **not** easy (it needs a skilled moderator, and one loud voice can dominate it) and **not** unbiased (the group can be led by whoever runs it, and people may agree with the majority). **Never use any of those three.** Use **depth**, **honesty of response** or **the discussion itself**.

---

## 55. Branding — why it is **important** / one **advantage of a strong brand**

**Asked:** *"Explain one advantage of having a strong brand."* — June 2026 P2 · *"Explain one reason why branding is important to businesses."* — May 2023 P2R

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> With a strong brand the **product or service is easily recognisable** (1) — customers spot it instantly among competitors' goods. **This may lead customers to choose the business over its competitors** (1), even when the price is higher. **This leads to high levels of sales revenue** (1), and it means the business does not have to compete only on price.

**The chain, broken out**
1. **Recognisable / differentiated** — the customer can tell it apart.
2. **Chosen over competitors** — the buying decision changes.
3. **Revenue, loyalty, or the ability to charge more** — the commercial outcome.

**A second acceptable route** *(scheme, May 2023 P2R)*
**Branding differentiates the products from others** (1) → **it helps customers identify the brand they want** (1) → **and it maintains loyalty** (1).

**A third acceptable route** *(scheme, same question)*
**The business develops a strong image for its product** (1) → **this can increase the price customers will pay** (1) → **the brand itself becomes worth a great deal of money** (1).

> ⚠️ **`NB No marks are awarded for a definition.`** *"Branding is giving a product a name and a logo"* scores **0** on both series. **Never open with a definition.**
> ⚠️ **And do not confuse branding with advertising.** Branding is the **identity** — name, logo, design, the associations customers hold. Advertising is **how it is communicated**. An answer about "putting adverts on television" belongs to entry 64, not here. **A strong brand is the asset; advertising is a cost.**

---

## 56. Packaging — why it is **important**

**Asked:** *"Explain one reason why packaging is important to a business."* — June 2026 P2

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> The packaging **protects the goods** (1) — that is its first job, and the scheme's own opening point. **This matters particularly if the goods are fragile or easily broken** (1) in transit or on the shelf. **This should ensure the goods are delivered safely to the customer** (1), so the business does not lose money replacing damaged stock or lose the customer altogether.

**The chain, broken out**
1. **Protects the product** — the physical function.
2. **Because the goods are fragile / must survive handling** — why protection matters here.
3. **They arrive in good condition** — the consequence: no waste, no replacements, no lost sale.

**A second acceptable route** *(scheme, same question)*
**Packaging attracts consumers** (1) → **customers who care about how a product looks** (1) → **it may persuade the consumer to purchase it** (1).

> ⭐ **Packaging has three separate jobs and you should pick the one that chains best:** **protect** the product · **attract** the customer · **inform** them (ingredients, instructions, warnings, and legally required information). **Attract** is the strongest route in a competitive market, because it is the only one that changes a buying decision.
> ⚠️ **`NB No marks are awarded for a definition.`** Do not write *"packaging is the material wrapped around a product."*

---

## 57. The product life cycle — one way to **extend** it

**Asked:** *"Explain one way the product life cycle can be extended."* — May/June 2019 P1

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> The business could **change the packaging of its product** (1) — a new look makes an established product feel new again. **This could be done by brightening up the old packaging or adding extras to it** (1), such as a resealable opening or a smaller size. **This could result in more repeat purchase as well as new custom** (1), pushing the sales curve back up before it declines.

**The chain, broken out**
1. **An extension strategy** — one of the recognised ones (packaging, new markets, new uses, updated features, relaunch, new promotion, price cut).
2. **How it is done specifically** — the detail that shows it is a real strategy.
3. **Sales recover** — repeat purchase, new customers, or a later decline.

**A second acceptable route** *(constructed — the most reliable alternative)*
**Sell into a new market** → the product is launched in another country where it is not yet known → **sales rise again from customers who have never seen it**.

**A third** *(constructed)* — **find a new use for the product** → customers who already own it buy it for a second purpose → **existing customers spend more**.

> ⚠️ **The instruction is "extend", not "increase".** *"Cut the price"* or *"advertise more"* on its own describes ordinary promotion, not extension. **Extension strategies are the ones that reset the product's position once it has matured** — new markets, new uses, new packaging, updated features, rebranding.
> ⭐ **The same topic appeared as a 2-mark Outline in May 2023 P1R** — *"Outline one way Aude Rose could extend the product life cycle of one of its products."* The 2-mark version needs **one** link; the 3-mark version needs **two**. **Do not spend 3-mark effort on a 2-mark question.**

---

## 58. Continually introducing **new products** — one benefit

**Asked:** *"Explain one benefit to a business of continually introducing new products."* — May/June 2020 P2R · *"Explain one reason why businesses continually design new products."* — May 2023 P2

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> A business introduces new products **to keep customers interested in the business and in the products it sells** (1) — attention moves to whatever is new. **It can replace an old product with a new one** (1) as the old one reaches the end of its life, so the business always has something current on the shelf. **This keeps it up with trends in the market** (1), so customers do not drift to a competitor who looks more modern.

**The chain, broken out**
1. **Customers stay interested** — the immediate benefit.
2. **Old products are replaced** — the business maintains its range rather than watching it age.
3. **The business keeps up with trends** — consequence: retained customers, protected sales.

**A second acceptable route** *(scheme, May 2023 P2)*
**Designing new products keeps existing customers interested** (1) → **they will visit the store to see and purchase the new goods** (1) → **increasing profit for the business** (1).

**A third acceptable route** *(scheme, May 2023 P2)*
**Fashions constantly change** (1) → **if the business does not introduce new products, demand for its existing ones decreases** (1).

> ⭐ **The strongest version of this answer is the "or else" version** — the scheme's third route is written as a **counterfactual**, and it is the most persuasive shape: *fashions change; if we stand still, demand falls.* Use it when you want the third sentence to land hard.

---

## 59. The **Boston Matrix** — one benefit

**Asked:** *"Explain one benefit to a business of using the Boston Matrix."* — May/June 2022 P1

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> The Boston Matrix helps a business to **balance its product portfolio** (1) — it shows the whole range on one chart rather than looking at products one at a time. **It shows whether the business has too many similar products** (1) all in the same position, which is a risk if that market turns. **And it can lead the business to identify when it needs to introduce a new product** (1), so it is not left with nothing as its current products age.

**The chain, broken out**
1. **See the whole portfolio at once** — the tool's function.
2. **Spot the imbalance** — too many of one kind, or nothing in the growth corner.
3. **Take a portfolio decision** — introduce, invest in, or drop a product.

**A second acceptable route** *(constructed — the classic decision route)*
The Matrix shows which products are **cash cows** → those can fund the ones that need investment → **the business knows where to spend its money instead of guessing**.

**The four quadrants you may name** *(they will not score on their own — they must be turned into a consequence)*
| | High market growth | Low market growth |
|---|---|---|
| **High market share** | **Star** | **Cash cow** |
| **Low market share** | **Question mark** | **Dog** |

> 🚨 **Naming a quadrant scores nothing.** *"A dog is a product with low market share in a low-growth market"* is a definition, and it earns **0**. **The benefit is always about the DECISION the matrix allows** — which products to keep, which to invest in, which to withdraw from, and whether the range as a whole is balanced.

---

## 60. **Product trials** — why they are important

**Asked:** *"Explain one reason why product trials are important to a business."* — May/June 2022 P2

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> A trial **gains customer feedback on a new product** (1) before the business commits to a full launch. **It identifies the strengths and weaknesses of the product** (1) — what people liked and what they complained about. **These can then be addressed before the product goes into the wider market** (1), so the faults are fixed while they are still cheap to fix.

**The chain, broken out**
1. **Feedback is collected** — the purpose of a trial.
2. **Strengths and faults are identified** — what the feedback reveals.
3. **Corrections happen before the full launch** — the financial consequence: money is not wasted producing a flawed product at scale.

**A second acceptable route** *(scheme, same question)*
**A customer is offered a three-month trial of the games** (1) → **they find out whether they like them** (1) → **if they do, they may buy the console** (1) — a trial that leads to a purchase.

> ⚠️ **Trial vs test marketing — keep these apart.** A **product trial** is the customer using the product (a sample, a short free use, a taste). **Test marketing** is the business launching in one restricted area to see how the whole marketing mix performs. Both reduce risk; only test marketing is about *a region*. If the question says **trial**, write about the **customer using the product**.

---

## 61. **Test marketing** — one benefit

**Asked:** *"Explain one benefit for a business that uses test marketing."* — May 2023 P1

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> **The risk of failure is reduced** (1) — the business does not commit to a national launch on a hunch. **This is because the new product is only tested in one area, gaining feedback from customers** (1) there. **This leads to modifications being made before the final launch** (1), so the faults are found while the cost of fixing them is still small.

**The chain, broken out**
1. **Risk is reduced** — the benefit.
2. **Because only one area is used and feedback comes back** — the mechanism.
3. **Changes are made before the full launch** — the consequence.

**A second acceptable route** *(constructed)*
**It tests the whole marketing mix, not just the product** → the business finds out whether the price, the promotion and the packaging work together → **it can change any of them before a national launch**, when it is still cheap.

> ⭐ **Test marketing and product trials are close cousins, and this is the cleanest way to tell them apart:** a **trial** puts the *product* in a customer's hands; **test marketing** puts the *whole mix* into a *small market* and measures how it sells. Use the word "area" for test marketing.

---

## 62. **Product orientation** — one disadvantage

**Asked:** *"Explain one disadvantage to a business of product orientation."* — May 2023 P1R

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> With a product-oriented approach **the product may not suit the needs of the customer** (1) — the business has designed what it thinks is good rather than what customers asked for. **So potential customers may go elsewhere** (1) to a business that does offer what they want. **This results in the business losing sales** (1), and the more it has invested in the product, the more it loses.

**The chain, broken out**
1. **The product does not match customer needs** — the fault in the orientation itself.
2. **Customers go elsewhere** — the behavioural consequence.
3. **Lost sales** — the commercial consequence.

**A second acceptable route** *(constructed)*
**The business may miss a change in the market entirely** → rivals spot a new trend first because they are watching customers → **the product becomes outdated while it is still being improved**.

> ⚠️ **Product orientation vs market orientation — this distinction is the whole question.**
> **Product orientation** = *"we will make the best product we can, and customers will buy it"* — the business leads, the customer follows.
> **Market orientation** = *"we will research what customers want, then make it"* — the customer leads.
> **A product-oriented business is not automatically wrong** — it can produce genuine innovation — **but its disadvantage is always some version of the same thing: it is building for itself, not for the customer.** Name the mismatch in sentence one, and the lost sale in sentence three.

---

# 3.3.2 — PRICE

## 63. **Penetration pricing** — one way it can be used / one benefit

**Asked:** *"Explain one way a business can use penetration pricing."* — May/June 2019 P1R · *"Explain one benefit of using penetration pricing for a new product."* — May/June 2020 P2R

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> A business can **offer a low price for a new product** (1) when it first enters the market. **This will entice customers to try the new product in its introduction stage** (1) — people will take a chance on something cheap even if they have never heard of it. **And it stops them from buying from the competitors** (1), so the business gains its market foothold at the rival's expense.

**The chain, broken out**
1. **Set a low price at launch** — the strategy itself.
2. **Customers try the new product** — because the risk of trying is low.
3. **Competitors lose those customers / the business gets established** — the commercial consequence.

**A second acceptable route** *(scheme, May/June 2020 P2R)*
**The business prices below its competitors** (1) → **in order to get established in the market** (1) → **once customers are buying, the price may be increased** (1).

> 🚨 **DO NOT CONFUSE THE TWO PRICING STRATEGIES — this is a 1-mark multiple-choice favourite.**
> | | **Penetration pricing** | **Price skimming** |
> |---|---|---|
> | Price at launch | **LOW** | **HIGH** |
> | Why | to grab market share quickly, and to undercut rivals | to earn high revenue from early adopters who must have it |
> | Then | price **rises** once established | price **falls** as competitors enter |
> The **1-mark** questions name one and ask for the other's meaning: *"Which one of the following is the name of a pricing strategy where a business sets a **high** price for a new product in the market?"* — answer **price skimming**. **Recheck which one the question is asking before you write.**

---

# 3.3.2 — PROMOTION

## 64. **Above-the-line** promotion — one method

**Asked:** *"Explain one method of above the line promotion a business could use."* — May/June 2019 P1 · *"Explain one method of above the line promotion a business may use to increase its sales revenue."* — Nov 2024 P1

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> A business could use **television advertising** (1) — a classic above-the-line channel that reaches a mass audience at once. **This can be seen by large numbers of people, raising awareness of the product** (1) among customers who had never heard of it. **This results in an increase in sales for the business** (1), because awareness is the first thing that has to exist before anyone can buy.

**The chain, broken out**
1. **Name the medium** — television, radio, newspapers, magazines, cinema, outdoor/billboards.
2. **It reaches a lot of people → awareness rises** — what the medium does.
3. **Awareness converts into sales** — the commercial consequence.

**A second acceptable route** *(scheme, Nov 2024 P1)*
**A business could use billboards** (1) → **they are seen by many people as they drive or walk through busy areas** (1) → **leading to increased brand recognition of the products** (1).

**A third** *(scheme, Nov 2024 P1)*
**Television advertising** (1) → **viewed by a wide audience** (1) → **increased awareness of the product** (1).

**Which media are above the line:** television · radio · newspapers · magazines · cinema · outdoor (billboards, bus sides) · **increasingly, paid digital display**. **The test: the business pays a media owner to broadcast to a general audience.**

> ⚠️ **`NB No marks are awarded for a definition`** (Nov 2024 P1, on this question). *"Above-the-line promotion is advertising in the media"* scores **0**.
> 🚨 **THE ONE-LINK ERROR TO AVOID.** *"A business can use television advertising (1). This is advertising on television (1)."* — that is a **restatement**, not development, and it scores **1**. The second sentence must add something the first did not contain: **who sees it**, and **what changes as a result**.

---

## 65. **Below-the-line** promotion — one method

**Asked:** *"Explain one method of below-the-line promotion a business may use to retain its customers."* — Nov 2023 P1

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> Existing customers may be offered **sales promotions or discounts** (1) — a targeted offer rather than a mass advertisement. **The aim is to entice customers to buy at a lower price** (1), so they have a direct reason to come back now rather than later. **This therefore encourages repeat sales by its customers** (1), which is precisely what "retain" means here.

**The chain, broken out**
1. **Name the below-the-line method** — discount, coupon, loyalty card, sample, point-of-sale display, personal selling, direct mail, exhibition, competition.
2. **What it does to the individual customer** — gives them a targeted reason to act.
3. **Retention / repeat purchase** — the outcome the question asked for.

**A second acceptable route** *(constructed)*
**A loyalty card that rewards every tenth purchase** → the customer has something to lose by shopping elsewhere → **they keep coming back to build up the reward**.

**A third** *(constructed)* — **free samples in store** → the customer tries the product at no risk → **they buy it afterwards**, and the business has only paid for the sample, not for a national advert.

> ⚠️ **The dividing line, and it is the marks:** **above the line** = paid, mass media, no direct contact, hard to measure. **Below the line** = **targeted at particular customers**, direct, and much easier to measure because you know who received it.
> ⭐ **Read the tail of the question.** This one says *"to retain its customers"* — so the chain must **end on retention or repeat purchase**. A discount that ends on "more sales this week" answers a different question and leaves the last mark behind.

---

## 66. **Sponsorship** — one reason / one advantage

**Asked:** *"Explain one reason why a business would sponsor an event."* — May/June 2020 P2R · *"Explain one advantage for a business of using sponsorship."* — Nov 2021 P2 · *"Explain one reason why a business might use sponsorship."* — Nov 2024 P2

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> By sponsoring an event **the business will gain publicity** (1) — its name appears alongside the event rather than inside an advert. **The event could be local, national or global** (1), so the business chooses how wide it wants the exposure to be. **This would mean the business covers a wide spectrum of people** (1), and those people associate the name with the event they already care about.

**The chain, broken out**
1. **Sponsorship buys publicity / brand awareness** — the reason.
2. **The scale depends on the event chosen** — local, national or global; the business can target its reach.
3. **The audience is exposed and may buy** — increased awareness leading to revenue or profit.

**A second acceptable route** *(scheme, Nov 2021 P2 and Nov 2024 P2 — almost identical wording)*
**Brand awareness will be increased** (1) → **this could encourage followers of the event to consider purchasing from the business** (1) → **leading to increased revenue or profits** (1).

**A third** *(scheme, May/June 2020 P2R)*
**Sponsorship is making a financial contribution to an event** (1) → **this makes more people aware of the business's products** (1) → **this could in turn increase sales** (1).

> ⚠️ **`NB No marks are awarded for a definition`** — Nov 2024 P2 says it on this exact question. But note the tension: **May/June 2020 P2R's own worked answer opens with a definition** *("Sponsorship is making a financial contribution to an event (1)")*. **The safe reading: a definition only counts when it is immediately made operational** — when it says what the sponsorship *buys*. **Definition-then-nothing is what the scheme refuses.**
> ⭐ **The strongest sponsorship answers name the audience match** — sponsor the local flower show and you reach the people who buy flowers. **That is the one thing a repeat of "it raises awareness" can never do.**

---

## 67. **Targeted advertising online** — one advantage / one reason

**Asked:** *"Explain one advantage for a business of using targeted advertising online."* — May/June 2019 P2R · *"Explain one reason why a business would use targeted advertising online to promote itself."* — May/June 2025 P2R

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> The business can **send information to customers who have purchased from it before** (1) — the online data tells it who those people are. **Those customers are more likely to purchase again** (1) than a random reader of an advert would be. **This can lead to improved customer loyalty** (1), at a far lower cost per sale than advertising to everyone.

**The chain, broken out**
1. **The business can select its audience** — by previous purchase, by interest, by demographic, by location.
2. **The audience is therefore more likely to want it** — the targeting does the work.
3. **Better conversion — loyalty, awareness or revenue** — the commercial result.

**A second acceptable route** *(scheme, May/June 2019 P2R)*
**The business can target a wider audience** (1) → **because it is worldwide and available 24/7** (1) → **and it is a relatively cheap method compared with traditional advertising** (1).

**A third** *(scheme, May/June 2025 P2R)*
**The business could promote to a specific demographic** (1) → **using different online activities** (1) → **which may lead to increased brand awareness** (1).

> ⭐ **"Targeted" is the word that earns the second mark.** The scheme's own answers never just say "more people see it" — they say **the right people** see it: people who bought before, people in one demographic. **Say who is targeted, and why they are the right people.**
> ⚠️ **And "cheap" needs the comparison.** *"It is cheap"* is weaker than the scheme's *"a relatively cheap method **compared with traditional advertising**"*. The comparison is what makes it an advantage rather than a claim.

---

## 68. **E-newsletters** — one benefit / one way a business could use them

**Asked:** *"Explain one benefit to a business of using e-newsletters."* — May/June 2020 P1R · *"Explain one way a business could use e-newsletters."* — May 2023 P1

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> An e-newsletter **can target the business's existing customers** (1) — it goes only to people who have already given their email address. **This allows the business to introduce new products to them** (1) directly, without paying for an advert that most readers would ignore. **And this can encourage more sales** (1) from customers who already trust the business.

**The chain, broken out**
1. **It reaches a list the business already owns** — existing customers, by email.
2. **What it does with them** — introduces new products, offers discounts, gives news.
3. **A sale, a return visit or loyalty** — the consequence.

**A second acceptable route** *(scheme, May 2023 P1)*
**E-newsletters can be personalised based on a customer's previous transactions** (1) → **it could include special discounts just for them** (1) → **leading to customers being motivated to return** (1).

> ⭐ **The mechanism to remember: an e-newsletter is the only channel in the syllabus aimed at people who have already opted in.** That is the whole argument — **no wasted reach**, because every recipient has already shown interest. Say that, and the second mark is secure.
> ⚠️ **`NB No marks are awarded for a definition.`** *"An e-newsletter is a newsletter sent by email"* scores **0**. Say what it **does**.

---

## 69. **Social media** — one way a business can use it

**Asked:** *"Explain one way social media can be used by a business."* — Nov 2021 P1

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> A business can use social media to **create a targeted advertising campaign** (1) — the platform's own data selects who sees the post. **The business can send a specific advert to a targeted group** (1) by age, location or interest. **Those people are likely to be interested in the product or service** (1), so the money spent reaches people who might actually buy.

**The chain, broken out**
1. **Name the use** — advertising, customer service, market research, building a community, launching a product.
2. **How the platform does it** — targeting, two-way contact, instant reach, free to post.
3. **What the business gains** — more relevant reach, faster answers, feedback, loyalty.

**A second acceptable route** *(constructed — customer service)*
**Responding to complaints publicly** → other customers see the business dealing with the problem → **it builds trust rather than losing the sale**.

**A third** *(constructed — market research)*
**Reading what customers post about the product** → the business learns what people really think without running a survey → **it can change the product quickly**.

> ⚠️ **Do not just say "to advertise".** That would fit almost any channel. **The mark comes from what is distinctive about social media** — it is **two-way** (the business and the customer can both speak), **targeted** by the platform's own data, and often **free to publish, paid only to promote**.

---

## 70. **Public relations** — why good PR is important

**Asked:** *"Explain one reason why having good public relations is important to a business."* — Nov 2021 P2

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> Good public relations means it is **likely to improve the business's brand image** (1) — how the public sees it, rather than what it says about itself. **This could lead to increased sales** (1), because customers prefer to buy from a business they trust. **And therefore to overall profitability** (1).

**The chain, broken out**
1. **The public's view of the business improves** — image or reputation.
2. **Customers respond** — they buy, they stay, they recommend.
3. **Profit or resilience** — and note the second real benefit: **goodwill protects the business when something goes wrong.**

**A second acceptable route** *(constructed — the resilience route, which is stronger)*
**When a product fails or a mistake is made, the business is given the benefit of the doubt** → customers do not immediately leave → **a crisis does not become a collapse**.

> ⭐ **Public relations is not advertising, and the difference is the marks.** Advertising **buys** attention; public relations **earns** it — through press coverage, charitable work, how the business treats customers and staff, and how it behaves when it is criticised. **If your answer could be rewritten as an advert, it is probably the wrong topic.**

---

# 3.3.3 — CUSTOMER LOYALTY AND REPEAT PURCHASE

## 71. Encouraging **repeat purchase** — one method

**Asked:** *"Explain one method a business could use to encourage repeat purchase of its products."* — May/June 2022 P1R

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> The business could **issue loyalty cards** (1) — a card that records what the customer has bought. **This could be used to offer special discounts** (1) once a certain number of purchases is reached. **This leads to customers being motivated to return to the business rather than its competitors** (1), because switching now would mean losing the reward they have built up.

**The chain, broken out**
1. **Name the method** — loyalty card, discount for returning, subscription, free gift, reminder email, high-quality after-sales service.
2. **The specific feature that rewards returning** — the accumulated discount, the member price, the personalised offer.
3. **The customer comes back instead of going elsewhere** — and the switching cost is what does it.

**A second acceptable route** *(constructed — quality and service, not a gimmick)*
**Consistently good quality and customer service** → the customer has no reason to try anyone else → **they return without needing a discount**, so margin is protected.

**A third** *(constructed)* — **an e-newsletter with the customer's own offers** → the business stays in touch between purchases → **the reminder itself brings them back**.

> ⚠️ **Repeat purchase is not the same as loyalty.** A discount buys a **repeat purchase**; a good product earns **loyalty**. If the question says **repeat purchase**, a short-term method is fine and expected. If it says **loyal customers** (entry 72), the answer must be about the relationship, not the discount.
> 🚩 **The trap:** *"A business can advertise"* is not a method of encouraging repeat purchase — advertising wins **new** customers. **Name something that only works if the customer comes back.**

---

## 72. **Loyal customers** — one advantage

**Asked:** *"Explain one advantage for a business of having loyal customers."* — May/June 2019 P2R

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> An advantage will be **repeat custom** (1) — loyal customers come back and buy again. **If customers are loyal they will shop only at that business** (1) rather than comparing prices elsewhere. **This could increase market share or revenue** (1), and it costs the business nothing extra to sell to a customer it already has.

**The chain, broken out**
1. **They return and buy again** — repeat custom.
2. **They do not shop around** — competitors are shut out.
3. **Revenue, market share, or lower cost of selling** — the commercial gain.

**A second acceptable route** *(constructed — the cost argument, which is the strongest)*
**Winning a new customer costs money in advertising, while selling to an existing one does not** → the same revenue is earned at a lower marketing cost → **profit rises without sales having to rise**.

**A third** *(constructed — the referral route)*
**Loyal customers recommend the business to others** → new customers arrive without being advertised to → **the business grows without paying for that growth**.

> ⭐ **This topic has a 1-mark State twin, and it is a different question.** *"State one advantage for PPS of keeping its customers loyal"* (May/June 2024 P1) · *"State one possible reason why TUI would want to keep its customers loyal"* (May/June 2024 P2) · *"State one possible reason why Huawei would want to keep its customers loyal to its brand"* (Nov 2021 P2).
> **On State, one reference to the business is enough and no reasoning is needed. On Explain, you need the two steps.** Do not write three sentences for a one-mark State question.

---

---
