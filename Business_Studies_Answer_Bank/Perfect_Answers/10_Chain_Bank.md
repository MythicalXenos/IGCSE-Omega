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
| **3-mark Explain** | **152** | ✅ **derived — 1(f) · 2(c) · 2(d) · 2(e), 4 per paper** |
| **6-mark Analyse** | **114** | ✅ **derived — 1(g) · 3(d) · 4(b), 3 per paper** |
| **9-mark Justify** | **76** | ✅ **derived — 2(f) · 3(e), 2 per paper** |
| **12-mark Evaluate** | **38** | ✅ **derived — 4(c), 1 per paper** |
| **TOTAL GOVERNED** | **380** | ✅ 152 + 114 + 76 + 38 |

> 🧮 **Coverage is now DERIVED, not carried by hand.** Run `python3 layer_c_6mark_coverage.py` from the folder above: it reads the derived inventory, checks every block against a `COVERED` map, and **also checks the other way — any entry number that does not exist in this file is printed as a dangling reference.** It was written because **Batch 5b recorded twelve blocks covered when it had covered eight**, leaving four 2019 blocks missing until the block file was re-read by hand. **That is the failure mode this bank is built to prevent, and one hand-counted total was enough.**

**Progress against those 380 blocks:**

| Tier | Blocks | Written | Remaining |
|---|---|---|---|
| 3-mark Explain | 152 | ✅ **152** | 0 |
| **6-mark Analyse** | **114** | **66** | **48** |
| 9-mark Justify | 76 | 0 | 76 |
| 12-mark Evaluate | 38 | 0 | 38 |

> **How those four numbers were obtained, and why they can be trusted.** `build_layer_c_tariffs.py` reads the same 38 mark schemes, reconstructs every question part from its printed AO allocation, and then **checks its own work: a 4BS1 paper is worth 80 marks, and all 38 papers now sum to exactly 80.** The question labels are *invariant* — all 38 papers carry 1(f), 2(c), 2(d) and 2(e) at 3 marks, 1(g), 3(d) and 4(b) at 6 marks, 2(f) and 3(e) at 9 marks, and 4(c) at 12. Run `python3 build_layer_c_tariffs.py` to reproduce; it writes `layer_c_6_9_12_master.csv`.
>
> **These supersede the CSV's 86 / 48 / 17**, which came from question-paper text extraction. They also settle an earlier open question: the 9-mark count is not merely ≥2 on P1-family papers — **every one of the 38 papers has exactly two 9-mark Justify questions.**

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
| **4** | **3.4 Operations + 3.5 Finance + the last stragglers** | ✅ **28 entries (73–100)** |
| **5a** | **6-mark Analyse — June 2026, all four papers** | ✅ **12 entries (101–112)** |
| **5b** | **6-mark Analyse — May–June 2019, all four papers** | ✅ **7 entries (113–119)** |
| **5c** | **6-mark Analyse — May–June 2020, all four papers** | ✅ **8 entries (120–127)** |
| **5d** | **+ the four 2019 blocks Batch 5b missed** | ✅ **4 entries (128–131)** |
| **5e** | **6-mark Analyse — June 2021 + June 2022** | ✅ **11 entries (132–142)** |
| **5f** | **6-mark Analyse — May–June 2024, all four papers** | ✅ **6 entries (143–148)** |
| **5g–6** | 6-mark Analyse — the remaining **48 blocks** | ⬜ next |
| **7–8** | 9-mark Justify option pairs — 76 blocks | ⬜ |
| **9** | 12-mark Evaluate topics — 38 blocks | ⬜ |

> ✅ **THE 3-MARK TIER IS CLOSED.** All **97 canonical topics** and all **152 blocks across the 38 papers** are covered by entries 1–100.
>
> 🔄 **THE 6-MARK TIER IS NOW OPEN — entries 101 onward.** It is a bigger job than the 3-mark tier was, and for a reason worth understanding: **the 3-mark tier repeats its topics constantly** (152 blocks collapsed into 97 topics), but **the 6-mark tier mostly does not** — June 2026's twelve 6-mark questions are twelve different topics. The tier holds **114 blocks**; where a topic does repeat it is called out and one entry answers every instance of it — entry **108 (multinational)** already covers four papers, and entry **111 (induction)** covers three.

### 🚨 SCOPE CORRECTION — **152** three-mark blocks, not 111

**This file previously counted the 3-mark population from `4BS1_Question_Instances.csv` and reported 111. That number is wrong, and the fault was in the measuring instrument rather than in the counting.**

The CSV was built from **question-paper text extraction**, which is column-scrambled and silently loses whole question parts. The **mark schemes** state every part cleanly, and read that way **each of the 38 papers carries exactly four 3-mark Explain questions — 1(f), 2(c), 2(d) and 2(e):**

```
3-mark Explain blocks, read from the mark schemes : 152   (4 x 38 papers)
from 4BS1_Question_Instances.csv                  : 111   (under-count of 40)
```

How much is lost varies by paper — **May/June 2024 P1 shows 3 in the CSV but has 4; Nov 2024 P1 shows 2 and May/June 2025 P2 shows 1, and both have 4.** The shortfall is therefore **not a constant that can be added back on.**

**So `4BS1_Question_Instances.csv` is no longer the scope authority for Layer C — the mark schemes are.** The tool that re-derives this, and which also harvests each block's official worked answer, is **`../build_layer_c_3mark.py`** → **`../layer_c_3mark_master.csv`**. Both are tracked, and the tool re-reads the archive on every run, **so a sandbox re-seed cannot lose the finding again.**

### ⭐ PROGRESS — 3-mark Explain, derived and not estimated

```
3-mark blocks total      :  152
canonical topics         :   97
covered by entries 1-100 :   97 topics  ·  152 blocks
REMAINING                :    0 topics  ·    0 blocks
```

> **How this is counted.** `build_layer_c_3mark.py` reads all 38 mark schemes, harvests every 3-mark block, and normalises each to a canonical topic — *"identification of a benefit to a business of using e-newsletters"*, *"a way a business could use e-newsletters"* and *"a benefit to a business of using e-newsletters"* all resolve to **E-NEWSLETTERS**. **0 blocks are unmapped.** The figure above is **97 distinct canonical topics, all of which are now carried by an entry in this file.**
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

**23 entries.** Marketing is the largest remaining cluster: 33 of the 152 three-mark blocks sit in 3.3, in 23 distinct topics.

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

---

# BATCH 4 — Spec 3.4 (Operations), 3.5 (Finance), and the last stragglers

**28 entries — and this closes the 3-mark bank.** After this batch, every one of the **97 canonical 3-mark topics**, across all **152 blocks in all 38 papers**, is carried by an entry in this file.

---

## 73. Measuring business **success** — one measure

**Asked:** *"Explain one measure a business can use to judge its success."* — Nov 2021 P1 · *"Explain one way to measure the success of a business."* — May/June 2020 P1

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> **Market share can be used to measure the success of a business** (1) — what proportion of the whole market it sells to. **Changes in market share show how well or how badly the business is doing against its rivals** (1), which profit alone cannot tell you: profit can rise while market share quietly falls. **This helps the business make decisions** (1) — whether to invest, hold, or change what it is doing.

**The chain, broken out**
1. **Name a measure** — market share · profit · customer satisfaction · sales revenue · number of customers · staff turnover · growth.
2. **What it reveals** — whether performance is improving or slipping.
3. **What the business does with it** — a decision.

**A second acceptable route** *(scheme, May/June 2020 P1)*
**Customer satisfaction** (1) → **happy customers revisit the business** (1) → **they recommend it to friends and family** (1).

**Measures worth knowing, each with the comparison that makes it a measure:**
| Measure | The comparison it needs |
|---|---|
| Market share | against the whole market, or against last year |
| Profit | against last year, or against the target set |
| Customer satisfaction | against a previous survey, or a rival |
| Staff turnover | against the industry, or the previous year |

> ⚠️ **A measure needs something to measure *against*.** *"Profit measures success"* is a definition. *"**A rise in** profit compared with last year shows the business is doing better"* is a measure. **The comparison earns the second mark.**

---

## 74. **Private limited company (Ltd)** — one benefit to the owner

**Asked:** *"Explain one benefit to an owner of a private limited company."* — May/June 2025 P1R

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> A private limited company has **limited liability** (1) — the owner's responsibility for the company's debts is capped. **This reduces the risk of ownership** (1) compared with a sole trader or a partnership, where the owner can be pursued personally. **Their personal possessions are protected if the business has to pay back outstanding debts** (1), so the worst case is losing what they put in, not their home.

**The chain, broken out**
1. **Limited liability exists** — the legal feature.
2. **The risk to the owner is capped** — what that means for them.
3. **Personal assets are protected** — the concrete consequence.

**A second acceptable route** *(constructed)*
**The company can sell shares privately** → it raises far more capital than a sole trader could → **it can grow faster** without the owner taking on more personal risk.

> 🚨 **READ THE QUESTION: it asks about the OWNER, not the business.** This is one of the **relevance-by-party** traps — five separate instances are recorded in this bank. *"The business has limited liability"* is an answer about the **business**; **the mark is for what it does for the owner.** Write *"the owner's personal possessions are protected"*.
> ⚠️ **Do not claim an Ltd can sell shares to the public.** That is a **public** limited company (plc). An Ltd sells shares **privately, by invitation** — which is exactly what keeps control with the existing owners, and is a legitimate separate benefit if you want a different route.

---

## 75. **Hierarchical** organisational structure — one disadvantage

**Asked:** *"Explain one disadvantage of having a hierarchical organisational structure."* — May/June 2024 P1

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> **Communication through many layers can be difficult** (1) — a message has to pass through every level to reach the bottom. **There is a long chain of command** (1), so each layer can delay it or change it on the way. **This possibly leads to slow decision-making** (1), and the business reacts to customers more slowly than a flatter rival does.

**The chain, broken out**
1. **Many layers** — the structural fact.
2. **A long chain of command** — the mechanism that causes the problem.
3. **Slow decisions** — or messages arriving distorted.

**A second acceptable route** *(constructed)*
**A wide span of control at the top** → managers have too many staff to supervise closely → **problems are not spotted until they have grown**.

> ⚠️ **The scheme links two syllabus terms in one breath — "many layers" and "long chain of command" — and it is worth copying that link.** It shows you know how they connect: **layers are the structure; the chain of command is the path instructions travel through them.**
> ⚠️ **Do not write "it costs more".** More layers do cost more in salaries, but that answers a *cost* question. **This question is about organisational structure, so the answer must be about communication, decisions or control.**

---

# 3.4 — OPERATIONS MANAGEMENT

## 76. **Job production** — one reason to use it

**Asked:** *"Explain one reason why a business would use job production."* — May/June 2019 P2

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> Job production is used **to produce a unique piece of work** (1) — one item at a time, made to order. **It is made to meet the exact needs of the customer** (1), which the business could not do with standardised output. **This requires the time and the skills of the employees** (1), which is why job production suits businesses selling high-value, bespoke products.

**The chain, broken out**
1. **Unique, made-to-order output** — the defining feature.
2. **Exact customer requirements are met** — why a customer will pay for it.
3. **It needs skilled labour, and allows a high price** — the consequence for the business.

**A second acceptable route** *(constructed — the pricing route)*
**Each item is unique** → the customer cannot compare it with a rival's price → **the business can charge a premium**, which covers the high labour cost.

> ⚠️ **`NB No marks are awarded for a definition`** — printed on this exact question in 2019 P2. *"Job production makes one item at a time"* scores **0**.
> 🚨 **JOB PRODUCTION HAS NOTHING TO DO WITH JOBS OR EMPLOYMENT.** This is a named word-collision in this bank. A candidate who writes *"job production means the business creates jobs for people"* has answered a **completely different question and scores zero.** Job production = **one bespoke item at a time** — a wedding cake, a tailored suit, a made-to-measure bridge.

---

## 77. **Batch production** — one reason to use it

**Asked:** *"Explain one reason why a business would use batch production."* — May/June 2021 P2

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> A business with **a wide range of products may need to produce them in smaller numbers** (1) — neither one at a time nor in one endless run. **It can then change the product easily — the colour or the size, for example** (1) — between one batch and the next. **And it does so without incurring too much cost** (1), because the same machinery and layout are reused for every batch.

**The chain, broken out**
1. **Variety is needed, in moderate volumes** — the business's situation.
2. **The line can be switched between batches** — the flexibility this gives.
3. **Costs stay controlled** — or: it is cheaper than job production at this volume.

**A second acceptable route** *(constructed — the stock route)*
**Producing in batches builds stock ahead of demand** → customers are served immediately → **the business does not lose sales while it waits for a new batch**.

> ⭐ **Batch production sits between the other two, and the exam expects you to place it.**
> | | **Job** | **Batch** | **Flow** |
> |---|---|---|---|
> | Output | one unique item | groups of identical items | continuous, high volume |
> | Labour | highly skilled | semi-skilled | low-skilled, often automated |
> | Example | wedding cake | a bakery's batch of loaves | bottling a drink |
> **Use volume and flexibility as the reason — never "it makes more products", which is the answer for flow production, not batch.**

---

## 78. **Flow production** — one disadvantage

**Asked:** *"Explain one disadvantage for a business of using flow production to produce its goods."* — Nov 2024 P1

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> **The employees may get bored on the production line** (1) — the work is repetitive and each person does one task all day. **Their job roles are likely to be monotonous** (1), with no variety and little skill involved. **This leads to poorly motivated employees and high labour turnover** (1), so the business is constantly recruiting and training replacements.

**The chain, broken out**
1. **Repetitive, specialised work** — the nature of a flow line.
2. **Monotony and low motivation** — the effect on the worker.
3. **High labour turnover, poor quality, or industrial action** — the cost to the business.

**A second acceptable route** *(scheme, same question)*
**The production facility may be inflexible** (1) → **the goods produced are standardised and similar** (1) → **which may prevent the business from tailoring its products to individual customer tastes** (1).

> ⭐ **The inflexibility route is often the stronger of the two**, because it is a **strategic** disadvantage rather than a human one — a rival offering variety can take customers a flow line cannot serve at all. **Both routes are the scheme's, so choose whichever chains more naturally to the case.**
> ⚠️ **Note the scheme's own example wording "high labour turnover"** — the exam expects the technical term, not just "staff leave".

---

## 79. **Technology** — one impact on production

**Asked:** *"Explain one impact of technology on the manufacture of vehicles."* — May/June 2019 P2

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> **Fewer people are required in the factories to do repetitive jobs** (1), because machines can perform them instead. **People get bored doing these jobs and make mistakes** (1), so removing them also removes a source of error. **Fewer employees brings the cost of goods down** (1), through lower wage costs or fewer faulty items.

**The chain, broken out**
1. **Technology replaces labour** — the impact itself.
2. **The effect on the work or the product** — fewer errors, faster output, more consistent quality.
3. **A cost consequence** — unit costs fall.

**A second acceptable route** *(scheme, same question)*
**More robots are manufacturing the vehicles than previously** (1) → **the vehicles can be manufactured in any country** (1) → **so the business could move to a cheaper country** (1).

> ⚠️ **"Impact" is not the same word as "benefit".** An impact can be negative, and the scheme's own answer hedges — it notes that people **make mistakes** on dull jobs, so the technology is not simply good. **If the question says impact, a balanced answer is safe. If it says benefit, write only the upside.**

---

## 80. **Robotics** — one reason a business would use it

**Asked:** *"Explain one reason why a business would use robotics in its production."* — Nov 2024 P2

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> Using robots **reduces production errors** (1) — a machine does not tire or lose concentration. **Robots can be programmed to do the same thing time after time** (1), with no variation between items. **Products can therefore be made with greater consistency and higher quality** (1), which is what the customer actually experiences.

**The chain, broken out**
1. **Robots reduce error, or raise output** — the reason.
2. **Because they repeat a programmed action exactly** — the mechanism.
3. **Consistency, quality, or lower unit cost** — the consequence.

**A second acceptable route** *(scheme, same question)*
**Robotics increases the number of goods produced** (1) → **reducing the cost of production** (1) → **leading to the possibility of greater profits** (1).

> ⚠️ **Robotics, technology and automation overlap almost completely in a 3-mark answer — so use the scheme's own vocabulary.** Robots are **programmed**; they remove **errors**; they give **consistency**. An answer that says only *"it is faster"*, without naming consistency or error-reduction, stops one link short.

---

## 81. **Just in time (JIT)** stock control — one reason or benefit

**Asked:** *"Explain one way in which the JIT method of stock control might benefit a business."* — May/June 2020 P1R · *"Explain one reason why many manufacturing businesses use just-in-time (JIT)."* — May/June 2025 P2

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> JIT **reduces the amount of inventory held by the business** (1) — materials arrive as they are needed rather than being stockpiled. **This reduces the costs associated with over-ordering** (1) and, because far less space is needed for storage, **overall costs for the business may be reduced** (1).

**The chain, broken out**
1. **Less stock is held** — the defining feature of JIT.
2. **Storage and holding costs fall** — the immediate benefit.
3. **Overall costs fall, or space is freed for something else** — the consequence.

**A second acceptable route** *(scheme, May/June 2025 P2)*
**JIT reduces out-of-date or damaged stock** (1) → **less storage space is required** (1) → **the space can be used for other business activities** (1).

**A third** *(scheme, May/June 2020 P1R)*
**Less space needed for buffer stock** (1) → **a reduction in storage costs** (1) → **stock arrives as and when it is needed** (1).

> ⚠️ **`No marks are awarded for a definition`** — printed on both of these. Do not write *"JIT means stock arrives just in time"* and stop there.
> 🚩 **JIT has a matching DISADVANTAGE, and you should be able to produce it too:** there is **no buffer stock**, so if a supplier is late **production stops entirely** — orders cannot be fulfilled and sales are lost. **On a "benefit" or "reason" question keep to the upside; on an evaluate or analyse question the stoppage risk is the strongest counter-argument you have.**

---

## 82. **Kaizen** — one reason manufacturers use it

**Asked:** *"Explain one reason why many manufacturing businesses use Kaizen in their factories."* — May/June 2022 P2R

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> **Kaizen means employees are involved in the process of improvement** (1) — the people doing the work are the ones who suggest the changes. **They suggest ways to improve the manufacturing process** (1), which is precisely what a manager sitting in an office cannot see. **This can lead to improved product quality** (1).

**The chain, broken out**
1. **Everyone is involved in improvement** — the defining feature of Kaizen (continuous improvement).
2. **Suggestions come from the people doing the job** — why those suggestions are worth having.
3. **Quality improves, waste falls, costs fall** — the consequence.

**A second acceptable route** *(scheme, same question)*
**Kaizen helps reduce waste** (1) → **because employees understand how to operate the machinery more effectively** (1) → **resulting in lower overall costs for the business** (1).

> ⚠️ **`No marks are awarded for a definition.`** *"Kaizen is continuous improvement"* scores **0** — and that is the exact trap here, because the definition is the memorable part. **Say what it does:** it puts the people who run the machines in charge of improving them, and that produces suggestions no manager can generate from a desk.
> ⭐ **Kaizen is on the examiners' list of named content gaps** — historically candidates have simply not known it. **Two points are enough: employees suggest improvements, and waste falls so costs fall.**

---

## 83. Total quality management (**TQM**) — one advantage or benefit

**Asked:** *"Explain one benefit for a business from the introduction of total quality management (TQM)."* — Nov 2021 P1 · *"Explain one advantage to a business of using total quality management."* — May/June 2025 P1

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> TQM produces **improved product quality** (1) — fewer faults reach the customer. **This is because everyone is working as a team** (1) and quality is everybody's responsibility, not one inspector's. **So fewer mistakes are likely to be made** (1).

**The chain, broken out**
1. **Quality improves** — the benefit.
2. **Because responsibility is shared by all employees** — the mechanism, and the thing that separates TQM from quality control.
3. **Fewer mistakes, less waste, higher customer satisfaction** — the consequence.

**A second acceptable route** *(scheme, May/June 2025 P1)*
**Increased customer satisfaction** (1) → **because managing quality is the responsibility of every employee** (1) → **so they are fully trained and complete their role effectively and consistently** (1).

> 🚨 **TQM AND QUALITY CONTROL ARE NOT THE SAME, AND THIS IS THE TRAP.**
> | | **Quality control** | **TQM** |
> |---|---|---|
> | Who is responsible | **one inspector, or one department** | **every employee** |
> | When | **at the end** — faults found after production | **throughout** — faults prevented |
> | Effect on waste | the faulty items are already made | the faulty items are never made |
> **This has already cost marks in a real paper:** a candidate who answered TQM with *"increased customer satisfaction"* as a standalone claim had it **not awarded**, because the premise underneath it was wrong. **A TQM answer must contain the words "all employees" or "everyone".** That is the phrase the mark rests on.

---

## 84. **Quality** of goods — why it is important

**Asked:** *"Explain one reason why the quality of goods manufactured by a business is important to its success."* — Nov 2023 P2 · *"Explain one reason why businesses maintain the quality of their products."* — May 2023 P2R

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> **Manufacturing quality goods leads to a good reputation for the business** (1) — customers talk about it, and the name comes to stand for something. **This encourages more people to purchase the goods** (1), including people who would not previously have considered the business. **Which increases the sales for the business** (1).

**The chain, broken out**
1. **Quality builds reputation** — or: it prevents complaints and returns.
2. **Customers choose it, and come back to it** — the behavioural effect.
3. **Sales, profit, or the ability to charge more** — the commercial result.

**A second acceptable route** *(scheme, May 2023 P2R)*
**Consumers expect quality products** (1) → **and expect them to perform the function for which they were bought** (1) → **failure to do this could lose customers to competitors** (1).

> ⚠️ **"Quality" does not mean "expensive", and it does not mean "luxury".** Quality means **fit for purpose** — the product does what the customer bought it to do. A cheap product can be high quality. **Use "fit for purpose" or "performs the function it was bought for" and you cannot be wrong.**
> ⭐ **The strongest third sentence is the counterfactual** — *"if it does not, customers go to a competitor."* The scheme reaches for it in its own answer, and it lands the point without needing a number.

---

## 85. **Using resources effectively** — one reason

**Asked:** *"Explain one reason why businesses want to use resources effectively in manufacturing."* — May 2023 P2

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> **Being effective in the use of resources reduces waste** (1) — fewer materials thrown away, fewer items scrapped. **This could decrease the amount of inventory held** (1), because the business no longer has to over-order to cover for spoilage. **Thus lowering the expenses of the business** (1).

**The chain, broken out**
1. **Waste is reduced** — the immediate effect.
2. **Less material and less stock is needed** — the mechanism.
3. **Costs fall, or output rises for the same input** — the consequence.

**A second acceptable route** *(scheme, same question)*
**Using fewer machines to manufacture goods** (1) → **makes the business more efficient** (1) → **allowing for greater productivity** (1).

> ⚠️ **Efficiency and effectiveness are different words — use the one the question gives you.** **Efficiency** = producing with the least input (cost per unit). **Effectiveness** = achieving the intended result (the right output). The scheme treats them together so either is safe — **but the chain must end on waste, cost or productivity.** "It is good for the environment" is not a scheme point here.

---

## 86. **Location** — why the proximity of materials matters

**Asked:** *"Explain one reason why proximity of material is important to a business when locating to a new factory."* — Nov 2024 P1

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> **Locating close to materials may reduce delivery costs** (1) — the raw materials have far less distance to travel. **Because the material only has to travel a short distance to the new factory** (1), the transport element of the cost is much smaller. **This reduces total cost and increases the profitability of the business** (1).

**The chain, broken out**
1. **Delivery and transport costs fall** — the immediate benefit.
2. **Because the distance is short** — the mechanism.
3. **Total costs fall, or production is not delayed** — the consequence.

**A second acceptable route** *(scheme, same question)*
**Access to materials close to the new factory saves time** (1) → **if the business runs out of inventory it can be delivered quickly** (1) → **which prevents delays in production** (1).

> ⭐ **Two routes, and the second is the better one to memorise** — *"prevents delays in production"* is a stronger business consequence than a cost saving, and **a business close to its materials can run a leaner stock policy**, which links straight back to JIT (entry 81).
> **Other location factors, in case the question is broader:** proximity to **the market** (the customers) · **labour** (skilled workers available) · **competitors** (clustering brings customers to the area) · **the cost of the site** · **government grants or incentives**.

---

## 87. **Job advertisement** — one important piece of information

**Asked:** *"Explain one important piece of information that should be included in a job advertisement in a newspaper."* — May/June 2024 P2

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> The advertisement should include **an address, telephone number or website** (1) for making contact. **This range gives the applicant a greater choice** (1) about how they apply. **Which means more of the right people apply** (1), rather than giving up at the first obstacle.

**The chain, broken out**
1. **Name the piece of information** — contact details · salary · job title and description · person specification · location · hours · closing date.
2. **What it does for the applicant** — they can judge whether it is worth applying, and how to do it.
3. **What that does for the business** — better applicants, fewer wasted applications, less time sifting.

**A second acceptable route** *(scheme, same question)*
**Including the salary** (1) → **people apply if the amount offered interests them** (1) → **saving applicants time and effort, so they apply for the job they actually want** (1).

> ⭐ **The best answers to this question catch both sides in one sentence** — what the *applicant* gains, and what the *business* gains as a result. *"The salary is included so people know whether it is worth applying, which means the business does not waste time on applications from people who would refuse the pay."*
> ⚠️ **`No marks are awarded for a definition.`** Do not write *"a job advertisement is an advert for a job."*

---

## 88. Training employees — one **disadvantage**

**Asked:** *"Explain one disadvantage for a business of training its employees."* — May/June 2025 P2

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> **Training employees takes a great deal of time** (1) — the training has to be delivered, and someone has to deliver it. **It needs existing employees to carry it out** (1), so experienced staff are taken off the work they are paid to do. **This can reduce the productivity of the business** (1) in the short term, even though the training should raise it later.

**The chain, broken out**
1. **Training costs time and money** — the disadvantage.
2. **Existing staff are diverted to deliver it** — the specific mechanism.
3. **Productivity falls, or output is missed** — the consequence.

**A second acceptable route** *(scheme, same question)*
**Existing employees have to be taught how to train others** (1) → **which incurs additional expense** (1) → **and there is no guarantee they are trained efficiently** (1).

> ⭐ **Read this beside entry 11 (on-the-job training — advantage).** An advantage question and a disadvantage question on the same topic need **different chains**, not one chain reversed. Here the chain is **time → staff diverted → productivity falls.**
> 🚩 **The strongest third sentence available — mine, not the scheme's — is the poaching risk:** training employees makes them **more employable elsewhere**, so a competitor can hire them away and the business has paid to train its rival's workforce. **That is a real disadvantage, and it cannot be answered by "but they work better afterwards".**

---

# 3.5 — FINANCE

## 89. **Cash flow forecast** — why it is important / one limitation

**Asked:** *"Explain one reason why cash flow forecasts are important for a business."* — May/June 2019 P2R · *"Explain one reason why cash flow forecasting is important to a business."* — May 2023 P2 · *"Explain one limitation of a cash flow forecast when making business decisions."* — May/June 2021 P1

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> **It allows the business to predict its future inflows and outflows** (1) — money coming in and money going out, month by month. **It knows whether it can survive** (1) through a lean period or a large payment. **And whether it has sufficient funds to keep trading** (1), so it can arrange finance before the problem arrives rather than after.

**The chain, broken out**
1. **Inflows and outflows are predicted** — what the forecast does.
2. **Shortfalls are visible in advance** — the point of looking.
3. **The business acts before the crisis** — arrange a loan or overdraft, delay a payment, chase debtors.

**A second acceptable route** *(scheme, May 2023 P2)*
**Businesses can plan for the future** (1) → **by estimating the revenue coming in and the money going out** (1) → **and can identify periods of insufficient funds so they can plan for that situation and make adjustments to enable survival** (1).

**⭐ THE LIMITATION — and it is a different question, so it needs a different chain** *(scheme, May/June 2021 P1)*
> **A limitation is that it is a forecast, not an actual figure** (1) — it is an estimate, and estimates can be wrong. **The forecast does not show what happens if goods are not sold** (1) — the sales figures in it are assumptions, not guarantees. **Nor does it provide a contingency plan if that occurs** (1).
> **Other limitations that chain honestly:** it is only as good as the figures put into it · it cannot predict an unexpected event such as a machine breakdown or a lost customer · it shows cash, not profit, so a business can look healthy on one and be in trouble on the other.

> 🚨 **CASH FLOW IS NOT PROFIT — this confusion is the single most expensive one in 3.5.**
> | | **Cash flow** | **Profit** |
> |---|---|---|
> | What it measures | money **actually moving** in and out | revenue **earned** minus costs **incurred** |
> | A sale on 60-day credit | no cash yet — **already revenue** | revenue now, cash later |
> | A loan received | **cash in — not revenue at all** | not profit |
> | A machine bought for cash | cash out immediately | **depreciated over years**, not a one-off cost |
> **A business can be profitable and still fail**, because the cash arrives too late to pay the wages. That sentence is worth memorising; it is the standard content of a 6- or 12-mark answer on cash.

---

## 90. One method of **increasing profit**

**Asked:** *"Explain one method a small business might use to increase its profit."* — May/June 2020 P1R and May/June 2022 P1 · *"Explain one way a business could increase its profit."* — May/June 2025 P1R

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> **Profits could be increased by cutting costs** (1). **A small business could cut the number of workers it has, or reduce their hours** (1), which are usually its largest single expense. **So if the revenue stays the same, this will increase the profit** (1).

**The chain, broken out**
1. **Cut costs, or raise the price** — the two levers, and there are only two.
2. **Name the specific cost** — wages · rent · materials · energy · stock.
3. **Profit rises because revenue is unchanged** — the mechanism, and the scheme always states it.

**A second acceptable route** *(scheme, May/June 2022 P1)*
**Cutting costs** (1) → **such as reducing the number of employees** (1) → **which could increase profit if revenue stays the same** (1).

**A third acceptable route — the other lever** *(scheme, May/June 2025 P1R)*
**Increase the price of the product** (1) → **if customers feel the quality is high they may be willing to pay the new price** (1) → **and if costs stay the same, profit will increase** (1).

> ⭐ **The scheme's phrasing is the thing to steal: "if revenue stays the same" and "if costs stay the same".** Profit is **revenue minus costs**, so a change to one side only counts if you say what happens to the other. **Say both halves and the third mark takes care of itself.**
> ⚠️ **`Answers that list three methods with no explanation will get 1 mark only.`** Do not write three levers with no chain — **one lever, fully developed, outscores three named and abandoned.**

---

## 91. Increasing the **gross profit margin**

**Asked:** *"Explain one way a business could increase its gross profit margin."* — May/June 2019 P1

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> A business could **negotiate deals with its suppliers at a cheaper rate** (1) — buying the same materials for less. **This keeps costs as low as possible** (1), and the gross profit margin is revenue minus the cost of sales, so a lower cost of sales raises the margin directly. **This means the business can look to reduce the prices of its products or services to encourage more sales** (1), or simply keep the extra as profit.

**The chain, broken out**
1. **Reduce the cost of sales, or raise the selling price** — the two levers on this ratio, and again there are only two.
2. **Name the specific action** — negotiate with suppliers · buy in bulk · find a cheaper supplier · reduce waste · raise the price if demand allows.
3. **The margin rises, and here is what the business does with it** — keep it, or cut the price to win volume.

**A second acceptable route** *(constructed — the price lever)*
**Raise the selling price without raising the cost of sales** (1) → **the gap between the two widens** (1) → **so the gross profit margin rises even if the number of sales stays the same.**

> 🚨 **GET THE FORMULA RIGHT — and write it, because the exam recognises it:**
> **Gross profit margin = (gross profit ÷ revenue) × 100**, where **gross profit = revenue − cost of sales.**
> ⚠️ **Do not confuse gross profit with profit.** **Gross profit** counts only the **cost of sales** — what it cost to buy or make the goods. **Profit (net)** also deducts **expenses** — rent, wages, advertising, interest. **A higher gross margin does not guarantee a higher net profit** if expenses have risen alongside it, and saying so is a strong closing sentence.
> ⭐ **This topic is on the examiners' named gap list** — *"gross profit margin"* and *"profitability ratios"* both appear. **The six ratios are on the formulae sheet; the formula for gross profit margin is not one you have to carry in your head, but you must know which two figures go into it.**

---

## 92. **Crowdfunding** — one benefit or reason for using it

**Asked:** *"Explain one benefit to a business of using crowdfunding as a source of finance."* — May/June 2021 P1 · *"Explain one reason why some businesses use crowdfunding as a source of finance."* — Nov 2023 P2

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> **Crowdfunding can be a fast way to raise finance** (1) — the pitch goes online and the money can come in quickly. **It comes from many small investors** (1) rather than one lender or bank. **At a point when no other lender may be available** (1) — which is the reason a business with no trading history reaches for it at all.

**The chain, broken out**
1. **It raises money fast, or from many people** — the benefit.
2. **Because it is online, and open to anyone** — the mechanism.
3. **When banks or investors would say no** — the consequence, and the strongest one.

**A second acceptable route** *(scheme, Nov 2023 P2)*
**Crowdfunding is organised online** (1) → **and can come from anywhere in the world** (1) → **giving access to a wide number of investors** (1).

> ⚠️ **`No marks are awarded for a definition`** — printed on the Nov 2023 question. *"Crowdfunding is raising money from lots of people online"* scores **0** on its own.
> 🚩 **The matching DISADVANTAGE, in case the question flips:** crowdfunding is **public**, so **competitors and customers see the idea** before it launches · the campaign **may fail and raise nothing at all** · the business may owe **rewards or equity** to its backers · and it takes **marketing effort** to succeed. **Use these on any evaluate or analyse question about finance.**

---

## 93. **Venture capital** — one advantage or one disadvantage

**Asked:** *"Explain one advantage of using a venture capitalist."* — May/June 2024 P1 · *"Explain one disadvantage for an entrepreneur of using venture capital to start their business."* — June 2026 P2R

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]` — **advantage**
> **Venture capitalists can be specialists** (1) — they bring more than money. **They may bring skills and new ideas to the business** (1), from having backed similar businesses before. **Giving it a greater chance of success** (1), particularly where the owner is strong on the product and weak on the business side.

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]` — **disadvantage**
> **The entrepreneur may lose some control of the business** (1) — the venture capitalist becomes a part-owner. **Because they give a share of the business away** (1) in exchange for the investment. **So they will have to consult others before making decisions** (1), and they can no longer simply do as they wish.

**The chain, broken out**
1. **Money — and usually expertise — comes in** / **or: ownership and control go out.**
2. **The specific mechanism** — skills and ideas, or a share of the business handed over.
3. **Greater chance of success** / **or: shared profits and slower decisions.**

**A second acceptable route — the profit route** *(scheme, June 2026 P2R)*
**The entrepreneur will have to share future profits with the venture capitalist** (1) → **which means the entrepreneur keeps a smaller proportion of profits** (1) → **so they receive less personal income** (1).

> 🚨 **VENTURE CAPITAL vs BANK LOAN vs CROWDFUNDING — the exam tests the difference.**
> | | **Bank loan** | **Venture capital** | **Crowdfunding** |
> |---|---|---|---|
> | What the business gives up | **interest** | **a share of ownership and control** | rewards, or equity |
> | Repayments | fixed, monthly, regardless of profit | **dividends only if profitable** | depends on the model |
> | Expertise | none | **often, yes** | none |
> **The single most useful sentence in this topic:** a bank loan must be repaid **whether or not the business succeeds**, while venture capital is repaid **only if the business makes a profit.** That is the trade-off, stated once, and it is the spine of any 9-mark Justify on the two.

---

## 94. Borrowing from a **bank** — one disadvantage

**Asked:** *"Explain one disadvantage to a small business of borrowing money from a bank."* — May/June 2025 P1

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> **Borrowing from a bank means the business has to pay back the loan with interest** (1). **This will increase its costs** (1), and for a small business the repayment is a fixed outgoing every month regardless of how trade goes. **Leading to a reduction in profit** (1) — and if the payments cannot be met, the business risks insolvency.

**The chain, broken out**
1. **The loan must be repaid, with interest** — the disadvantage.
2. **This adds a fixed cost that does not move with sales** — the specific mechanism.
3. **Profit falls, or cash flow comes under pressure** — the consequence.

**A second acceptable route** *(constructed)*
**The business must provide security, or a guarantee, to get the loan** → the owner may have to risk personal assets → **which raises the personal risk of running the business**.

> ⭐ **The interest point should be written as a *fixed* cost, not just a cost.** A repayment is due **whether or not the business sells anything this month** — which is why a bank loan is dangerous for a business with unpredictable income, and is exactly the trade-off against venture capital (entry 93, and the table there).
> ⚠️ **Read the party.** This question says **"to a small business"**. A large business can borrow on better terms than a small one, so **"the interest rate is likely to be higher for a small business, because it is seen as riskier"** is a strong and specifically small-business point.

---

## 95. **Personal savings** — one disadvantage as a source of finance

**Asked:** *"Explain one disadvantage of using personal savings as a source of finance for a business."* — May/June 2022 P1R

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> **Money to deal with an emergency may not be available** (1) — the savings that would have covered it have gone into the business. **So there is no back-up if things go wrong** (1), and the owner has no reserve to fall back on. **Meaning that it may be necessary to find another source of finance** (1), possibly at short notice and on poor terms.

**The chain, broken out**
1. **The savings are gone** — the disadvantage.
2. **There is no reserve left for an emergency** — the specific mechanism.
3. **The owner must borrow, or the business cannot respond** — the consequence.

**A second acceptable route** *(constructed)*
**The amount available is limited to what the owner has saved** → it may be too little for the expansion planned → **so the business grows more slowly than a rival that borrowed properly**.

**A third** *(constructed — the personal-risk route)*
**The owner's own money is at risk** → there is no limited liability protecting it in a sole trader or partnership → **and losing it affects the owner's household, not just the business.**

> ⭐ **Every source of finance has the same four-point skeleton, and it is worth knowing it off by heart:** **cost** (interest, or profit shared) · **availability** (how much, how fast) · **control** (what the owner gives up) · **risk** (what happens if it goes wrong). **Run those four against any source and you will never be short of a chain.**

---

## 96. **Retained profit** — one disadvantage as a source of finance

**Asked:** *"Explain one disadvantage to a business of using retained profit to purchase goods and services."* — Nov 2023 P2

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> **Using retained profit reduces the amount of funds available for the business to use** (1) — the reserve is spent. **If there is an emergency where funds are needed — a machine breaking down, for example** (1) — **the business may not have the funds to get it repaired** (1).

**The chain, broken out**
1. **The reserve is spent** — the disadvantage.
2. **Nothing is left for the unexpected** — the specific mechanism.
3. **The business cannot respond, or must borrow** — the consequence.

**A second acceptable route** *(scheme, same question)*
**By using its retained profit to buy new machinery** (1) → **the business may not have the funds** (1) → **to pay the rent or the wages of its employees** (1).

> ⭐ **The scheme's own vocabulary is the key: retained profit IS the financial cushion.** So the disadvantage is always, in one form or another, **"the cushion is gone"** — and the scheme's two examples (machine repair, rent and wages) are the ones to reuse.
> ⚠️ **Do not say retained profit "has no cost".** It has **no interest and no ownership is given up** — that is its advantage — but it has a **very real opportunity cost**, because the money can only be spent once. **Say which one the question is asking about.**

---

## 97. The **statement of comprehensive income** — one reason it is used

**Asked:** *"Explain one reason why businesses use statements of comprehensive income when making decisions."* — May/June 2025 P2R

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> **A business can see how the business is performing** (1) over the period — whether it is heading in the right direction. **It can calculate the profit margin** (1), because the statement holds revenue, cost of sales and expenses together. **Along with other calculations, if the performance has deteriorated** (1) — which is what turns the statement into a decision.

**The chain, broken out**
1. **It shows performance over a period** — the statement's function.
2. **It allows ratios to be calculated** — profit margin, and what has changed.
3. **A decision is taken** — cut costs, raise prices, change the product mix.

**A second acceptable route** *(scheme, same question)*
**Businesses can use it to compare themselves with similar businesses** (1) → **which lets them judge their performance against competitors** (1) → **giving an indication of how well the business is doing** (1).

> 🚨 **KNOW WHAT IS ON IT — this is a named content gap.** The **statement of comprehensive income** shows, for a **period**: **revenue** − **cost of sales** = **gross profit**; then minus **expenses** = **profit (net)**. It is the answer to *"how did the business do?"*
> ⚠️ **`No marks are awarded for a definition`** — printed here. Write what the statement is **for**, not what it is.
> ⭐ **The contrast to hold in your head:** the statement of comprehensive income is the **video** (a period, what happened); the statement of financial position is the **photograph** (one moment, what the business owns and owes). That one sentence has carried many candidates through this pair.

---

## 98. The **statement of financial position** — one purpose

**Asked:** *"Explain one purpose for a business of the statement of financial position."* — Nov 2023 P2

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> **By reviewing its financial position, a business can see how the business is performing** (1) — what it owns set against what it owes. **It may decide to expand further if it has the funds** (1), because the statement shows whether the money is there. **By introducing new products to sell** (1) — the decision the statement makes possible.

**The chain, broken out**
1. **It shows the position at one moment** — assets, liabilities and capital.
2. **Something becomes visible** — whether the business can afford to expand; whether it is carrying too much debt.
3. **A decision follows** — invest, borrow, cut stock, reduce liabilities.

**A second acceptable route** *(scheme, same question)*
**If a business has liabilities** (1) → **it may want to find ways to reduce its expenditure** (1) → **by decreasing the amount of stock it holds** (1).

> 🚨 **KNOW WHAT IS ON IT.** The **statement of financial position** records, **on one date**: **non-current assets** (buildings, machinery), **current assets** (stock, debtors, cash), **current liabilities** (creditors, overdraft), **non-current liabilities** (bank loans), and **capital / equity**. **Assets = liabilities + capital.**
> ⚠️ **`No marks are awarded for a definition`** — printed here too. Say what it is **for**.
> ⭐ **The one-sentence distinction, again:** the statement of comprehensive income is **for a period**; the statement of financial position is **on a date**. **Getting that backwards is the commonest error on this pair.**

---

## 99. **Financial documents** — why shareholders are interested

**Asked:** *"Explain one reason why shareholders would be interested in the financial documents of a business."* — Nov 2025 P1

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> **Shareholders may review the financial documents to assess whether the business is making a profit** (1). **The shareholder is interested in gaining a return on their investment** (1) — dividends, and a share price that rises. **Which helps them decide whether to sell their shares or buy more** (1).

**The chain, broken out**
1. **Shareholders look at the documents** — the act.
2. **They are looking for a return, or for trouble** — dividends, share price, debt levels, growth.
3. **They act on it** — buy more shares, sell, or vote at the AGM.

**A second acceptable route** *(scheme, same question)*
**To compare the financial performance of the business** (1) → **in order to identify cost savings** (1) → **which can help to improve the profitability of the business** (1).

> ⚠️ **Note which party the scheme is thinking from, and read the question the same way.** *"Shareholders are interested because the business wants to know its profit"* mixes the parties up — **the shareholder is a separate person from the business**, and their interest is in **what THEY get**, which is the return on their investment. **Check who the question asks about; five instances in this bank turn on exactly that.**
> ⭐ **Shareholders versus other stakeholders, in one line each:** **shareholders** want **dividends and a rising share price** · **banks** want to know **whether the loan will be repaid** · **the government** wants **the correct tax** · **managers** want **data for decisions** · **employees** want **job security and the ability to pay wages**.

---

## 100. **Paying suppliers on time** — why it is important

**Asked:** *"Explain one reason why it is important that businesses pay their suppliers on time."* — May/June 2025 P2

> **Model answer — 3 marks** `[OFFICIAL MARK-SCHEME WORKED ANSWER]`
> **Paying suppliers on time establishes a good relationship with them** (1). **If the business needs goods urgently from them** (1) at some point, **they would be more likely to help, knowing they would be paid on time** (1).

**The chain, broken out**
1. **The relationship is maintained** — the immediate benefit.
2. **Because the supplier trusts the business** — the mechanism.
3. **Better terms, priority treatment, or continued supply** — the consequence.

**A second acceptable route** *(scheme, same question)*
**Paying on time gives the business better negotiating power with the supplier** (1) → **so if the supplier trusts them, they may negotiate better prices** (1) → **thus keeping the business's costs down** (1).

> ⭐ **Note what the scheme does NOT say: there is no legal or moral argument here.** The mark is purely commercial — **a supplier who trusts you helps you in a crisis, and gives you better terms.** That is why payment terms are a **cash-flow decision, not just an accounting one**: the business is trading a short-term cash advantage (holding on to the money longer) against a long-term relationship (entry 89 on cash flow).
> 🚩 **The mirror question — a known trap — is the opposite one:** *"Which one of the following would be a benefit to a business of **delaying** paying its suppliers?"* (May/June 2024 P2, 1 mark). **Delaying payment keeps cash in the business longer** — that is a genuine short-term cash-flow benefit, and the exam has asked for it. **Know both sides; the syllabus expects you to see the trade-off.**

---

# ✅ THE 3-MARK BANK IS CLOSED

| Batch | Content | Entries |
|---|---|---|
| **1** | Newest 3-mark topics — June 2026 + Nov 2025 | 16 |
| **2** | 3.1 Business activity + 3.2 structure/HR cluster | 33 |
| **3** | 3.3 Marketing | 23 |
| **4** | **3.4 Operations + 3.5 Finance + the last three stragglers** | **28** |
| **TOTAL** | | **100 entries** |

```
3-mark blocks total           :  152
canonical topics              :   97
carried by entries 1-100      :   97 topics  ·  152 blocks
REMAINING                     :    0 topics  ·    0 blocks
```

**Every 3-mark Explain question in the qualification — all 152 blocks across all 38 papers — is now covered by a named entry above.** Reverify at any time with `python3 layer_c_coverage.py` from the folder above.

> ⚠️ **What this does NOT mean.** It does not mean there is a verified full-mark script for every one of these questions — Pearson has published scripts for only a fraction of them, and those are held in `02_Verified_Exemplars.md` and `External_Exemplars/`. **For almost every entry above, the model is the mark scheme's own worked answer** — official, but not a candidate's script. **The labelling rules at the top of this file apply to all of it.**
> ✅ **The 152nd block.** The count was 151 until this was traced to a single dropped mark-scheme block: **May–June 2021 P1 1(f)**, *"identification of a strategy of extending a product life cycle"*, whose PDF prints its header character-fragmented as `A0 1 - 3 mark s` and so defeated the extractor. It is now recovered and its topic — **PRODUCT LIFE CYCLE extension** — was **already carried** by entry 57. **So the topic count is unchanged at 97 and no new entry was needed; only the block count corrected.**
> ✅ **The 6-, 9- and 12-mark totals are now derived** (see the table at the top of this file): **114 · 76 · 38**, validated by all 38 papers summing to exactly 80 marks. **The scope of Batches 5–9 is therefore 228 blocks**, and no figure in this file is carried over from the CSV (rule 120).

---

# BATCH 5 — 6-MARK ANALYSE, PART 1

**12 entries — every 6-mark Analyse question in June 2026, across all four papers.** June 2026 is the most recent series and the one the bank had least on, and its twelve questions are twelve *different* topics, so this batch adds twelve topics rather than deepening existing ones.

> ### ⭐ THE ONE RULE FOR EVERY 6-MARK ANSWER
> **One point, developed in strands. The examiners said it themselves on the only 6/6 in the archive whose comment is printed:**
>
> *"The candidate has provided **1 point with developed strands**, analysing the effectiveness of the wide span of control. There is **application throughout their response**. Candidates are reminded that **there are no marks for knowledge in this question**."* (June 2025 P1, Q1(g), Four Fitness — 6/6)
>
> **Depth beats breadth.** Two separate reasons each developed once scored **5/6** on Rabanne 2(d) in the same session. **Take one point and keep asking "and then what?" until you reach something measurable.**
>
> ### WHAT THE MARK SCHEME GIVES YOU
> Every block below carries the scheme's own **AO2** bullets (application — facts you must take from the case) and **AO3** bullets (the chains). **The AO2 line is where candidates lose the most marks**: the scheme's second AO2 bullet is almost always the case-specific detail — *"as the partners had dropped out of college and had to work from a garage, it is likely they had few funds"* — and a generic answer cannot access it.
>
> **Labels:** the model answers in this batch are `[CONSTRUCTED GRADE 9 TARGET]` — **not** examiner-marked. The **AO2 anchors and the chains they use are quoted from the official mark scheme**, which is why each entry prints them.

---

## 101. SPONSORSHIP — the disadvantages

**Asked:** *"Analyse the disadvantages for Spud Bros of using sponsorship."* — **June 2026 P1R, 1(g)**

**The AO2 anchors the scheme wants:** Spud Bros sponsor an **English Football League club** — so customers will associate the brand with that club; and the sponsorship fee will be **expensive** for a small family business.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Spud Bros would pay to sponsor an English Football League club, and **the fee is fixed for the season whatever happens on the pitch**. Because customers link the brand to the club, **bad results or a player's poor behaviour attach themselves to Spud Bros' image too** — the association is the whole point of sponsoring, but it works in both directions. Supporters of rival clubs may then avoid the brand for that reason alone. **And because the fee must be paid up front, a small family business has to recover it**, which pressures the brothers towards a higher price for a portion of potatoes — and **a higher price means fewer customers are willing to buy**, which is the opposite of what the sponsorship was meant to achieve.

| Step | The move |
|---|---|
| **1. Point** | Sponsorship **ties the brand to the club** — and it is expensive |
| **2. Strand A** | Poor results / a player's bad behaviour → the damage **transfers to Spud Bros' image** |
| **3. Strand B** | The fee is **fixed and paid up front** → it must be recovered through price |
| **4. Measurable end** | A higher price → **fewer customers buying** |

**Second acceptable chain:** the cost of the sponsorship → **less cash left for the vans, staff or new products** → slower growth than the brothers planned → goals missed.

> ⚠️ **Do not write "sponsorship costs money",** which is knowledge and earns nothing (AO2/AO3 only — there is no AO1 mark here). Write **why the cost bites for a small family business**, and **what the association does to a brand when the team loses**.

---

## 102. VIRAL ADVERTISING — the advantages

**Asked:** *"Analyse the advantages for Spud Bros of using viral advertising."* — **June 2026 P1R, 3(d)**

**The AO2 anchors:** Spud Bros is a **small family-owned business**, so it can reach a **wide audience**; and Jacob and Harley can **minimise the cost of marketing** because posting on sites such as **Instagram is free**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Viral advertising costs Spud Bros almost nothing to place, because **Jacob and Harley can post on Instagram for free rather than paying for airtime or billboard space** — which matters to a small family-owned business with limited funds. **The same post can then be seen by people the brothers could never have reached locally**, because a share carries the brand beyond their own followers. **That reach widens brand awareness far faster than paid advertising would**, and because the audience is not limited to their city, it opens up new locations. **The measurable end is speed of growth:** the brothers can expand to meet their own business goals sooner, because **demand can arrive from outside the area** before they have paid for a single poster.

| Step | The move |
|---|---|
| **1. Point** | Viral advertising is **free to place** — the platform carries the cost |
| **2. Strand A** | A share carries it **beyond local followers** → wider brand awareness |
| **3. Strand B** | The audience is not limited to their city → **new markets open up** |
| **4. Measurable end** | **Faster expansion**, because demand arrives before paid marketing is needed |

**Second acceptable chain:** free reach → **marketing budget preserved** → those funds go into **more vans or better equipment** → capacity to serve the new demand.

> ⭐ **The strongest version of this answer always returns to "small family-owned business".** Free reach matters *because* the budget is thin. Drop that and you have lost the AO2.

---

## 103. GROWTH — the benefits for the owners

**Asked:** *"Analyse the benefits of growth for the owners of Spud Bros."* — **June 2026 P1R, 4(b)**

**The AO2 anchors:** more potato vans located in the **UK** selling more potatoes; **expanding into the US and Canada** will increase brand awareness.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> As Spud Bros puts more vans on the road and expands into the US and Canada, **the volume of potatoes it buys and sells rises**. **Higher volume lets the brothers buy their potatoes in bulk at a lower price per sack**, so each portion costs less to make while still selling at the same price. **That is the economies-of-scale benefit of growth, and it is what raises the profit on every van, not just the total.** **The measurable end is what it does for the owners personally:** more profit per portion means the business can fund further expansion from its own earnings, and the brothers **meet the growth goals they set for the business** — which is the point of expanding into two new countries in the first place.

| Step | The move |
|---|---|
| **1. Point** | More vans + two new countries → **higher volume** |
| **2. Strand A** | Higher volume → **bulk buying → lower cost per portion** |
| **3. Strand B** | Lower unit cost → **more profit on every sale, not just more sales** |
| **4. Measurable end** | Owner's goals met → **self-funded further expansion / financial stability** |

**Second acceptable chain:** brand awareness rises in the US and Canada → **new customers try the product** → revenue rises **without** the brothers having to be physically present, because the brand travels ahead of them.

> ⚠️ **"Growth is good for owners" scores nothing.** The mark is for the **mechanism** — volume → unit cost → margin — and then for linking it to **the owners' own goals**.

---

## 104. CURRICULUM VITAE — why a business asks for one

**Asked:** *"Analyse why Violet Cakes may request a curriculum vitae (CV) from job applicants."* — **June 2026 P1, 1(g)**

**The AO2 anchors:** Violet Cakes can assess whether recruits have **worked in the food industry before**; and a CV can be used to **shortlist** candidates with **experience of baking cakes**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> A CV sets out an applicant's history in writing, so **Violet Cakes can see at a glance whether someone has worked in the food industry before**. **That matters in a cafe, where the work is hands-on and a mistake is expensive** — you cannot teach someone to handle a commercial kitchen in an interview. **Because the CV shows experience of baking cakes, Claire can shortlist only the candidates who are likely to cope with a real cafe environment and with customers.** **The measurable end is what it saves:** by filtering at the CV stage, Violet Cakes avoids **paying staff time to interview people who turn out not to have the required skills**, and that time and money goes back into running the cafe.

| Step | The move |
|---|---|
| **1. Point** | A CV shows **written evidence of food-industry experience** |
| **2. Strand A** | Food-industry history → **shortlist candidates who can cope in a cafe** |
| **3. Strand B** | Fitting the environment → **less risk of a bad hire in a hands-on job** |
| **4. Measurable end** | **Time and money saved** on interviewing unsuitable candidates |

**Second acceptable chain:** the CV reveals experience of **dealing with customers** → the candidate needs **less training** → Violet Cakes gets productive staff **sooner** during a busy period.

> ⭐ **The generic route — "a CV tells you about the candidate" — is the trap.** The scheme's two AO2 bullets both point at **the food industry and cake baking**, and those are the details that earn the application marks.

---

## 105. FOCUS GROUPS — the advantages when making decisions

**Asked:** *"Analyse the advantages to Violet Cakes of using focus groups when making decisions."* — **June 2026 P1, 3(d)**

**The AO2 anchors:** Violet Cakes can **gather opinions about the customer service in the cafe** from the people selected; and it could **give the group different flavours of cookies and ask for their feedback**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> A focus group puts a small number of selected customers in a room together, so **Violet Cakes can gather opinions about its customer service directly from the people who have experienced it**. **Because they can also hand out different flavours of cookies and ask the group for their reactions there and then**, the feedback arrives while the product is still in front of them rather than weeks later. **People are more willing to be honest in that setting than in a formal survey** — one comment prompts another, and the discussion goes deeper than a tick-box answer would. **The measurable end is the product and the service:** the honest feedback lets Violet Cakes **change the flavour of its cookies and improve its level of service**, which attracts more customers in the first place.

| Step | The move |
|---|---|
| **1. Point** | A focus group gathers **opinions from selected customers who have used the service** |
| **2. Strand A** | Products handed round **there and then** → feedback arrives immediately |
| **3. Strand B** | Discussion prompts discussion → **honest, deeper feedback than a survey** |
| **4. Measurable end** | **Flavour or service changed** → more customers attracted |

**Second acceptable chain:** hearing the customer's own words → **Violet Cakes learns what customers value that it had not thought of** → the next decision is **based on a real reaction, not an assumption** → less wasted spend on the wrong change.

> ⭐ **Focus groups are qualitative — depth, not numbers.** If your answer mentions "a large sample" or "statistical validity" you have written about **questionnaires**, which is a different question with a different answer.

---

## 106. JOB PRODUCTION — the benefits

**Asked:** *"Analyse the benefits to Violet Cakes of using job production for some of its products."* — **June 2026 P1, 4(b)**

**The AO2 anchors:** Violet Cakes can make **wedding cakes specific to the requirements of its customers**; and the **chefs may be motivated by working on unique cake designs** for special occasions.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Job production means each item is made to order, and **that is exactly what a wedding cake demands — a cake built to one customer's specification, not a batch of identical sponges**. **Because no two are the same, Violet Cakes can charge for the workmanship and the customer has no direct comparison to shop against**, which supports a much higher price than a mass-produced cake could carry. **The measurable end is on both sides of the business at once:** customers are satisfied enough to **recommend the cakes to others**, giving Violet Cakes a stream of orders it did not have to advertise for; and **the chefs enjoy making unique designs, so they stay rather than moving to a competitor** — which means Claire keeps the skilled staff the business depends on.

| Step | The move |
|---|---|
| **1. Point** | Job production = **each cake made to one customer's specification** |
| **2. Strand A** | Unique work → **no direct comparison → higher price achievable** |
| **3. Strand B** | Different every time → **chefs motivated → skilled staff retained** |
| **4. Measurable end** | **Recommendations bring orders** + **staff turnover avoided** |

**Second acceptable chain:** bespoke cakes → **waste lower than batch production**, because nothing is made until it is ordered → cost per cake falls **without** cutting quality.

> ⚠️ **Job production and batch production are different answers.** The scheme marks *bespoke, one-off, made to order*. If your chains would also be true of batch production, you have not answered this question.

---

## 107. PARTNERSHIP — the advantages of starting out as one

**Asked:** *"Analyse the advantages for Steve Jobs and Steve Wozniak of starting the business as a partnership."* — **June 2026 P2R, 1(g)**

**The AO2 anchors:** it would have allowed them to **share their ideas on technology and work through solutions together**; and **as the partners had dropped out of college and had to work from a garage, it is likely they had few funds** to develop the technology.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> A partnership lets two people pool what they each bring, and **for Jobs and Wozniak that meant combining a creative mind with a technological one on the same problem**. **Because they had dropped out of college and were working from a garage with few funds, neither could have developed the technology alone** — one partner's idea could be tested against the other's technical judgement the same day. **A partnership also shares the money and the risk between them**, so the cost of components or a failed design does not fall entirely on one person. **The measurable end is survival in a new market:** the sharing of funds and risk **gave them a better chance of succeeding in the electronics market** than either would have had on their own.

| Step | The move |
|---|---|
| **1. Point** | A partnership **pools different strengths** — creative and technical |
| **2. Strand A** | Few funds → **shared money and shared risk** → the firm can afford to try |
| **3. Strand B** | Two minds on one problem → **faster solutions, better products** |
| **4. Measurable end** | **A better chance of success** in a new and competitive market |

**Second acceptable chain:** a partner covers the work the other cannot → **expertise without employing a specialist** → costs stay low **while** the business is too small to pay salaries.

> ⭐ **This is the question where a bare definition of "partnership" is most tempting.** It earns nothing here. Use **the garage, the lack of funds, and the college drop-out** — the scheme's own AO2 — and the answer becomes unanswerable-generic-proof.

---

## 108. MULTINATIONAL — the advantages of becoming one

**Asked:** *"Analyse the advantages for Apple of being a multinational company (MNC)."* — **June 2026 P2R, 3(d)**
**Also asked:** *"Analyse the benefits for LEGO of being a multinational business."* — June 2022 P2 1(g) · *"Analyse the benefits for Saha of becoming a multinational business."* — Nov 2024 P1 4(b) · *"Analyse two benefits to Rabanne of being a global business."* — June 2025 P2R 1(g)

> **This topic has come up four times in four years, on four different businesses. Learn it once and it answers all four.**

**The AO2 anchors (Apple):** access to **lower labour and production costs in China and Vietnam** for manufacturing its laptops; and a **larger consumer market** for its smartphones and smartwatches.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Manufacturing in China and Vietnam lets Apple pay **lower labour and production costs than it would in the US**, so the cost of building each laptop falls. **That cost saving is not passed entirely to the customer — it is kept as margin**, which is what allows Apple to **fund the continued updating of its products and stay ahead on innovation**. **The second half of the same advantage is reach:** selling into many countries gives Apple a **far larger consumer market for its smartphones and smartwatches**, and high global sales volumes let it **mass-produce the iPhone and drive the unit cost down further**. **The measurable end is a cycle, not a single gain** — lower unit costs and larger volumes reinforce each other, so Apple stays profitable while competing on specification rather than on price.

| Step | The move |
|---|---|
| **1. Point** | Being an MNC **cuts unit costs** — cheaper labour and production abroad |
| **2. Strand A** | Saving retained as margin → **funds innovation / product updating** |
| **3. Strand B** | Global sales → **volume → economies of scale → lower unit cost** |
| **4. Measurable end** | **Unit cost falls while quality rises** — profitable at a global scale |

**Second acceptable chain:** spreading sales across many countries → **a downturn in one market is cushioned by the others** → revenue is more stable, so planning and investment are safer.

> ⭐ **What changes between the four papers is only the AO2.** Use **the businesses' own facts**: Apple's China and Vietnam plants; LEGO's factories and global brand; Saha's robots for hotels; Rabanne's cosmetics sold worldwide. **The chain is identical.**

---

## 109. FLOW PRODUCTION — the disadvantages

**Asked:** *"Analyse the disadvantages for Apple of using flow production when manufacturing products."* — **June 2026 P2R, 4(b)**

**The AO2 anchors:** the **machinery and robotics to make the laptops is expensive**; and **the method may not be flexible enough**, because Apple is **constantly updating its iPhones**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Flow production is a continuous line, so **Apple must buy the machinery and robotics for that line up front, at very high cost**, and those costs are committed before a single laptop is sold. **The line is also built to produce one design**, which is a problem for a business that **constantly updates its iPhones** — because the equipment cannot simply be re-set for a new model. **The measurable end comes in two places.** First, the cost of the line and the disruption of changing it **push up the unit cost of the goods**, which makes it harder for Apple to compete with businesses such as **Oppo selling cheaper smartphones**. Second, **every time a new model arrives Apple may have to change machinery, which causes delays in production** — and a delayed launch is lost sales in a market where the new model is the reason people buy.

| Step | The move |
|---|---|
| **1. Point** | Flow production needs **expensive, single-purpose machinery** |
| **2. Strand A** | High fixed cost + re-tooling → **unit cost rises → harder to compete on price** |
| **3. Strand B** | The line is not flexible → **constant updates mean changing machinery → delays** |
| **4. Measurable end** | **Higher unit cost** and **late launches** — both cost sales |

**Second acceptable chain:** a continuous line **cannot be paused** → a fault anywhere stops the whole line → **output falls sharply** for as long as the fault lasts.

> ⚠️ **"Flow production makes boring, repetitive jobs"** is the standard textbook answer and **it is not what this scheme marks.** The scheme marks **cost and inflexibility**, because Apple's problem is a product that keeps changing.

---

## 110. PRIVATE LIMITED COMPANY — the benefits

**Asked:** *"Analyse the benefits to Nando's of being a private limited company."* — **June 2026 P2, 1(g)**

**The AO2 anchors:** Nando's can **sell shares to family and friends to raise capital** to build new restaurants; and **moving away from a partnership** gives Robert Brozin and Fernando Duarte **limited liability**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> As a private limited company Nando's can **sell shares to family and friends**, which raises capital in a way a partnership cannot — and that money can go straight into **building new restaurants in Canada and Asia**. **The same change gives the two owners limited liability**, so if the business fails they stand to lose only what they invested rather than their personal possessions. **That protection is not a small administrative detail; it changes who is willing to put money in.** **The measurable end is the flow of investment:** because an investor's personal assets are protected, **more investors are attracted to the business**, which funds the continued building of restaurants — and each new restaurant is another source of revenue.

| Step | The move |
|---|---|
| **1. Point** | An Ltd can **sell shares** — capital a partnership cannot raise |
| **2. Strand A** | The capital raised **funds new restaurants in Canada and Asia** |
| **3. Strand B** | Limited liability **protects the owners' personal possessions** |
| **4. Measurable end** | Protection → **more willing investors** → more restaurants → more revenue |

**Second acceptable chain:** the business becomes a separate legal entity → it **continues trading even if an owner leaves or dies** → the expansion plans are not put at risk by one person's circumstances.

> ⭐ **"Nando's will have limited liability" on its own is a definition, and definitions do not score.** The mark is for **what the protection causes** — investors willing to put money in.

---

## 111. INDUCTION TRAINING — the benefits to the business

**Asked:** *"Analyse the benefits to Nando's of providing induction training for new employees."* — **June 2026 P2, 3(d)**
**Also asked:** *"Analyse the benefits for TUI from including health and safety training for its employees in their induction training."* — June 2024 P2 1(g) · *"Analyse why Tata Motor Company ensures that its staff have a detailed induction programme."* — June 2019 P2 4(b)

**The AO2 anchors (Nando's):** induction training is likely to cover **health and safety in its kitchens**; and new employees are **introduced to other Nandocas before they start serving customers**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Induction training happens before a new employee starts the job, so at Nando's it will cover **health and safety in the kitchens** — which means **a new recruit knows what to do when something goes wrong on their first shift, rather than finding out at the moment it happens**. **The scheme's second anchor is the social one: being introduced to other Nandocas before serving customers means the new starter already feels part of the team.** **That feeling is not sentiment — it decides how they behave in front of paying customers.** **The measurable end is service quality:** a new recruit who feels comfortable and knows the kitchen rules **serves customers better from day one**, and better service in a restaurant chain is what brings people back — so the cost of the induction is recovered through repeat custom rather than through fewer accidents alone.

| Step | The move |
|---|---|
| **1. Point** | Induction happens **before** the first shift → the recruit is prepared |
| **2. Strand A** | Health and safety covered → **can deal with emergencies when they arise** |
| **3. Strand B** | Introduced to the team → **feels part of the team → more confident** |
| **4. Measurable end** | **Better customer service** → repeat custom |

**Second acceptable chain:** a prepared new starter **needs less supervision** from an experienced Nandoca → existing staff are not taken off their own work → **the restaurant runs at full capacity from day one**.

> ⭐ **Induction is not on-the-job training.** Induction is **before they start** — rules, safety, meeting the team. If your chains would still work for "training", you have answered a different question. *(See entries on the training cluster for on-the-job, off-the-job and external recruitment.)*

---

## 112. EXPANSION — the benefits to the host economy

**Asked:** *"Analyse how the Malaysian economy may benefit from Nando's expansion."* — **June 2026 P2, 4(b)**
**Also asked:** *"Analyse the benefits to countries where Kraft Heinz is located."* — Nov 2023 P2 4(b) · *"Analyse the benefits for India of these plans."* — Nov 2024 P2 1(g)

> **Note the party.** This is the only June 2026 question where the **beneficiary is a country, not the business.** Candidates who analyse Nando's profits here have answered a different question — and **a contextualised answer about the wrong party scores zero** (five recorded instances in this qualification).

**The AO2 anchors:** more people **recruited by Nando's in Malaysia** to work in the restaurants; and **more people paying taxation to the Malaysian government** as chefs or waiters.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Nando's expansion means it **recruits more chefs and waiters in Malaysia**, and every one of those jobs is a person moved out of unemployment. **Because those workers now earn a wage, they pay income tax to the Malaysian government** — so the benefit to the economy is not only the jobs themselves but **the tax revenue that comes with them**. **The measurable ends are two and both are national, not corporate.** Falling unemployment means **more money being spent in Malaysian shops and services**, which supports other businesses entirely unconnected to Nando's. And **the additional tax the government collects can be spent on schools and hospitals**, which raises the standard of living in Malaysia over the long term.

| Step | The move |
|---|---|
| **1. Point** | Expansion → **Nando's recruits staff in Malaysia** |
| **2. Strand A** | Wages paid → **income tax collected** → government revenue |
| **3. Strand B** | Unemployment falls → **higher spending in the wider economy** |
| **4. Measurable end** | Tax spent on **schools and hospitals → standard of living rises** |

**Second acceptable chain:** Nando's needs local suppliers → **Malaysian farmers and food producers gain a customer** → their income and their employees' income also rise.

> ⚠️ **The whole answer must stay on Malaysia.** The moment a sentence is about Nando's profitability, you have left the question. **Read who the beneficiary is before you write a word.**

---

# BATCH 5b — 6-MARK ANALYSE, PART 2

**7 entries — the twelve 6-mark questions of May–June 2019, collapsed into seven topics.** This is the first batch where the tier's *repetition* shows: twelve blocks, but **Statement of Comprehensive Income**, **break-even** and **profitability ratios** each appear once per paper, and **customer satisfaction** and **internal sources of finance** are the same topic under two different businesses.

> ### ⭐ WHERE THE OLD PAPERS DIFFER FROM THE NEW ONES
> In 2019 the mark schemes print the **AO2 bullets without naming the case-study business** — *"Lavender are able to see if they have enough money to expand into other parts of Malaysia"* rather than *"Apple may have access to lower labour costs in China and Vietnam"*. **That is the older scheme's style, not a licence to write generally.** The application mark is still earned by using **the business's own facts**, and the facts are in the case study.

---

## 113. CUSTOMER SATISFACTION — why it matters

**Asked:** *"Analyse why customer satisfaction might be important to Lavender."* — **May–June 2019 P1R, 1(g)**

**The AO2 anchors:** satisfied customers are **more likely to repeat purchase** cakes from Lavender; and Lavender is **expanding into different types of food outlets — L.bistro, L.cafe and L.table**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> A satisfied customer at Lavender buys again, so **the revenue arrives without Lavender having to spend anything to win it back**. **What makes that worth more than one repeat sale is the group:** Lavender is opening **L.bistro, L.cafe and L.table**, so a customer who is happy in one outlet is far more likely to try the others — **one satisfied customer becomes a customer of three businesses, not one**. **Satisfaction also replaces advertising.** A customer who has enjoyed the cake **recommends it to friends and family by word of mouth**, which is a channel Lavender does not pay for, so **Lavender can spend less on promotion and still grow** — and money not spent on promotion is money left in the business.

| Step | The move |
|---|---|
| **1. Point** | Satisfaction → **repeat purchase, at no cost of acquisition** |
| **2. Strand A** | Lavender is opening **three more outlets** → one happy customer becomes three customers |
| **3. Strand B** | Recommendation **replaces paid promotion** |
| **4. Measurable end** | **Lower promotional spend + higher revenue** from the same customer base |

**Second acceptable chain:** satisfaction → **fewer complaints and returns** → staff time is spent serving rather than fixing → **the outlet runs at lower cost** as well as higher sales.

> ⭐ **The three outlets are the answer's spine.** Without L.bistro / L.cafe / L.table you have written a general essay about customer service and left the application marks on the table.

---

## 114. STATEMENT OF COMPREHENSIVE INCOME — how a business uses it

**Asked:** *"Analyse how the Statement of Comprehensive Income can be used by Lavender when considering its expansion."* — **May–June 2019 P1R, 3(d)**
**Also asked:** *"Analyse how LEGO could use a Statement of Comprehensive Income when considering the development of new toys."* — June 2022 P2 3(d) · *"Analyse why IKEA uses statements of comprehensive income to assess its business performance."* — May 2023 P2 4(b)

**The AO2 anchors:** Lavender can **see whether it has enough money to expand** into other parts of Malaysia; and it can **use the figures to show investors how successful it is** and that it is capable of expanding.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> The Statement of Comprehensive Income shows **what Lavender earned and what it spent over the year, ending in a profit figure** — so before committing to expansion it can **see whether the money is actually there**. **That check matters because expansion brings costs the current figures do not yet contain:** new outlets mean **higher overheads and outgoings**, so **the net profit available to fund the expansion may be lower than the headline figure suggests**. **The statement's second use is with other people's money.** A strong and improving profit figure is **evidence Lavender can show to investors** that it is capable of expanding — which is what persuades them to put funds in.

| Step | The move |
|---|---|
| **1. Point** | The statement reveals **whether there is enough profit to fund expansion** |
| **2. Strand A** | Expansion adds **overheads and outgoings** → real funding headroom is smaller than it looks |
| **3. Strand B** | A strong statement is **evidence for investors** → finances the expansion |
| **4. Measurable end** | **A decision made on numbers** rather than on optimism |

**Second acceptable chain:** comparing this year's statement with **last year's** → shows whether performance is improving or worsening → the expansion is timed to a good year **or postponed out of a bad one**.

> ⚠️ **The Statement of Comprehensive Income is the *profit* statement — income and expenses over a period.** It is **not** the Statement of Financial Position (assets, liabilities, what the business owns and owes on one day). Mixing the two up loses the application mark. *Examiner-named content gap in multiple reports.*

---

## 115. INTERNAL SOURCES OF FINANCE — the benefits

**Asked:** *"Analyse the benefits to Lavender of using internal sources of finance for its expansion plans."* — **May–June 2019 P1R, 4(b)**
**Also asked:** *"Analyse the benefits to NOF of using personal savings to expand its product range."* — June 2021 P1 4(b) · *"Analyse the impact on Aude Rose of using its retained profits for this proposed development."* — May 2023 P1R 3(d)

**The AO2 anchors:** Lavender will **know the amount of internal finance it has available**; and **the money does not have to be borrowed or negotiated**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Internal finance — retained profit already sitting in the business — is **money Lavender knows it has, because it can see the balance**. **That certainty is the first benefit: there is no application to be approved and no lender to persuade**, so **the funds are available immediately** rather than after a process that can take weeks. **The second benefit is what it does not create.** Because the money is not borrowed, **Lavender pays no interest and faces no monthly repayment**, so **the expansion does not have to generate profit fast enough to service a debt in its early months** — a new L.cafe that takes a year to find its customers can be allowed that year. **The measurable end is lower risk:** costs are lower, and the business keeps the whole of the return rather than losing part of it to a lender.

| Step | The move |
|---|---|
| **1. Point** | The business **already knows the money is there** |
| **2. Strand A** | No negotiation → **available straight away**, so expansion is not delayed |
| **3. Strand B** | No borrowing → **no interest, no repayments** |
| **4. Measurable end** | **Lower cost and lower risk** — the return stays with Lavender |

**Second acceptable chain:** using retained profit **does not increase what Lavender owes** → the Statement of Financial Position stays strong → **it is still able to borrow later** for a bigger opportunity, having kept its borrowing capacity.

> ⚠️ **The limitation is real but it is not what this question asks.** Internal finance is *limited to what the business has saved* — that is the counter-argument, and it belongs in a 9-mark or 12-mark answer. Here the question says **benefits**, so the drawback costs you time and adds no mark.

---

## 116. SATISFYING CUSTOMER NEEDS — why it matters

**Asked:** *"Analyse the importance to Backyard Shoez of satisfying customer needs."* — **May–June 2019 P1, 1(g)**

**The AO2 anchors:** Backyard Shoez is **located in three shopping malls where there are other shoe shops**; and it **needs to maintain a high standard at all times** to encourage customers to buy.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Backyard Shoez trades **in three shopping malls, each with other shoe shops nearby**, so a customer who is not satisfied does not have to go far to buy elsewhere — **they can simply walk into the next unit, and that makes every sale contestable**. **Meeting customer needs is therefore not a courtesy; it is what stops the sale crossing the corridor.** **The second effect is on the customers Backyard Shoez already has.** A customer whose needs are met **keeps coming back**, so **loyalty builds a base of repeat revenue** that a competitor's lower price finds much harder to take away. **The measurable end is on sales and revenue:** holding the customer base protects the current turnover, and repeat customers **cost nothing to win again**, so more of each sale is kept as profit.

| Step | The move |
|---|---|
| **1. Point** | **Other shoe shops in the same three malls** → the customer can switch instantly |
| **2. Strand A** | Unmet needs → the customer **buys from the shop next door** |
| **3. Strand B** | Met needs → **loyalty and repeat purchase** → a defended revenue base |
| **4. Measurable end** | **Sales and revenue protected**, at no extra selling cost |

**Second acceptable chain:** high standards → **positive word of mouth in the mall** → customers arrive already intending to buy → **less spent on promotion**.

> ⭐ **Compare this with entry 113.** Both are "customer satisfaction" questions, but **Lavender's answer turns on multiple outlets and Backyard Shoez's turns on being surrounded by competitors.** *The chain is the same shape; the AO2 is completely different.* That is the whole skill at this tariff.

---

## 117. BREAK-EVEN ANALYSIS — what it is useful for

**Asked:** *"Analyse the benefits to Backyard Shoez of using break-even analysis to plan the launch of its new shoes."* — **May–June 2019 P1, 3(d)**

**Also asked in reverse:** *"Analyse the limitations for HRMW of using break-even charts when planning the manufacture of tennis racquets."* — May–June 2020 P2R 3(d) · *"Analyse the limitations for Irsi Chocolatier of using break-even charts to decide whether it should sell the new product."* — May 2023 P1 3(d) · *"Analyse how useful break-even calculations can be for NOF when deciding whether to include ice cream in its product range."* — June 2021 P1 3(d)

> **The same topic has been asked four times — twice as benefits and twice as limitations. Learn both directions; the questions alternate.**

**The AO2 anchors:** Backyard Shoez **will be able to see that it needs to sell 125 pairs before it can break even**; and it **can ask "what if" questions and see what impact various price changes have on the break-even point**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Break-even analysis converts the launch into **one number: 125 pairs of shoes must be sold before Backyard Shoez makes a profit**. **That number is the value of the tool — it lets the owner compare the target with what the three mall shops can realistically sell**, and decide *before* ordering stock whether the launch is worth attempting at all. **Its second use is as a rehearsal.** Because the calculation can be re-run, Backyard Shoez can **ask "what if" questions — what if the price rises, what if the supplier's cost rises — and see what each change does to the 125**. **The measurable end is a better pricing decision:** the owner can **raise or lower the price and see whether the business is still moving into profit**, which is also how it stays competitive with the other shoe shops in the malls.

| Step | The move |
|---|---|
| **1. Point** | Break-even gives **one target number — 125 pairs** |
| **2. Strand A** | The target can be **compared with achievable demand** before stock is bought |
| **3. Strand B** | "What if" re-runs show the effect of **price and cost changes** |
| **4. Measurable end** | A **price set with the numbers known** → profit rather than guesswork |

**Second acceptable chain:** the same calculation shows **how far sales can fall before the business makes a loss** → the owner knows the **margin of safety** and can judge how much risk the launch carries.

> ⚠️ **Two standard traps, both recorded.** **(1)** Break-even is a *forecast*, not a certainty — it assumes costs and price stay constant. If you are asked for **limitations**, that assumption *is* your answer. **(2)** **Learn the formula: break-even output = fixed costs ÷ contribution per unit.** The formulae sheet gives only the six accounting ratios and does **not** include break-even — an examiner-named content gap.

---

## 118. PROFITABILITY RATIOS — what they are useful for

**Asked:** *"Analyse the usefulness of profitability ratios to Backyard Shoez."* — **May–June 2019 P1, 4(b)**
**Also asked:** *"Analyse the usefulness to TBTS of the acid test ratio."* — June 2022 P1 4(b) · *"Analyse the usefulness of the gross profit margin to PPS."* — June 2024 P1R 1(g)

**The AO2 anchors:** Backyard Shoez can **work out how much profit it has made** from buying and selling shoes **and compare it with previous years**; and ratios can show **whether there is a need to take out short-term finance**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> A profitability ratio turns the raw figures into **a percentage that can be compared** — so Backyard Shoez can see **how much profit it makes on each pair of shoes**, and set that against **what it made in previous years**. **On its own, a profit figure cannot tell you whether the business is getting better or worse; the ratio can**, because it strips out the effect of simply selling more. **The second use is as a warning light.** The same ratios show whether there is **a need to take out short-term finance** — a margin falling while sales rise tells the owner that costs are running ahead, before the bank balance shows it. **The measurable end is the expansion decision:** used **before** expanding, the ratios show whether the financial position can carry it, and **investors weigh exactly the same information** when judging how much return they will receive against the risk.

| Step | The move |
|---|---|
| **1. Point** | A ratio is **comparable** — this year against last year |
| **2. Strand A** | Shows **a decline even when sales rise** → an early warning |
| **3. Strand B** | Warns when **short-term finance may be needed** |
| **4. Measurable end** | A **better-informed expansion decision**, and evidence for investors |

**Second acceptable chain:** the ratio lets Backyard Shoez **compare itself with rival shoe shops** on the same measure → the owner sees whether the problem is the business **or the whole sector**.

> ⚠️ **Know which ratio you have been given.** **Gross profit margin** = gross profit ÷ revenue × 100 — what is left after the *cost of the goods*. **Acid test** = (current assets − inventory) ÷ current liabilities — can the business pay its debts **without selling stock**. Quoting the wrong formula is a calculation mark lost, and **the final answer line is what is marked**.

---

## 119. KAIZEN — why a business encourages its suppliers to use it

**Asked:** *"Analyse why Yellow might encourage its clothing manufacturers to use Kaizen."* — **May–June 2019 P2R, 1(g)**
**Also asked:** *"Analyse how Kraft Heinz could benefit from reducing its waste."* — Nov 2023 P2 3(d)

**The AO2 anchors:** the **quality of the T-shirts will be better**; and there will be a **reduction in the costs of making the T-shirts**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Kaizen means **continuous improvement — small changes made all the time by the people doing the work**, rather than one large redesign. Applied at Yellow's clothing manufacturers, those small changes **raise the quality of the T-shirts**, because the faults that recur on the line are found and fixed by the staff who see them every day. **Yellow's reputation is built on the clothes it puts its name to**, so **better T-shirts protect the brand and lead to higher sales**. **The second effect is on cost.** Continuous improvement **reduces wasted cloth, wasted time and rejected garments**, and **fewer faulty T-shirts means fewer returns** — which cuts the cost of making each T-shirt and **increases the manufacturer's profitability**. **The measurable end is that Yellow gains on both sides at once:** it pays less per T-shirt and sells more of them, and its supplier keeps more of the price as profit — which is why the supplier has a reason to keep improving.

| Step | The move |
|---|---|
| **1. Point** | Kaizen = **continuous small improvements by the workforce** |
| **2. Strand A** | Better quality → **Yellow's reputation improves → higher sales** |
| **3. Strand B** | Less waste and fewer faults → **lower cost per T-shirt** |
| **4. Measurable end** | **Lower cost and higher sales at once** |

**Second acceptable chain:** Kaizen gives the line workers **a say in how the work is done** → they are more motivated → **labour productivity rises** → more T-shirts from the same hours.

> ⚠️ **Kaizen is not quality control and not TQM.** Quality control *inspects faults out* at the end; Kaizen *improves the process continuously* so there are fewer faults to find. **An examiner-named content gap — the vocabulary is expected and often absent.**

---

# BATCH 5c — 6-MARK ANALYSE, PART 3

**8 new entries — May–June 2020's twelve blocks, covering all twelve.** Four of the twelve were **the same topic as an entry already banked**, so they are pointed at those entries rather than repeated:

| Block | Topic | Where it now lives |
|---|---|---|
| 25 P1R 1(g) *importance of environmental factors (Loaf)* | environmental responsibility | **entry 120** |
| 26 P1R 3(d) *how useful the information in Figure 2 is (Loaf)* | ratio comparison — operating profit margin | **entry 118** |
| 27–31, 33–36 | six new topics + two merges | **entries 121–127** |
| 32 P2R 3(d) *limitations of break-even charts (HRMW)* | break-even — the limitation direction | **entry 117** |
| 35 P2 3(d) *why Emirates would want to be more environmentally friendly* | environmental responsibility | **entry 120** |

> ### ⭐ THE PATTERN THIS PAPER PAIR EXPOSES
> May–June 2020 asked **the same topic four times** — break-even (32), profitability (26), cash (29) and financial documents (33) — **once on each of its four papers**, because the four papers share a syllabus but not a case study. **That is the justification for this whole bank: learning the chain once answers every paper it appears on, and it will appear again.**

---

## 120. ENVIRONMENTAL RESPONSIBILITY — why it matters to a business

**Asked:** *"Analyse the importance of environmental factors for Loaf."* — **May–June 2020 P1R, 1(g)**
**Asked the other way round:** *"Analyse why Emirates would want to be more environmentally friendly."* — **May–June 2020 P2, 3(d)**

**The AO2 anchors (Loaf):** there is **more interest in businesses becoming "green"** and Loaf provides somewhere for the community to **recycle**; Loaf runs the **"Waste Not" scheme**, giving away waste instead of disposing of it.

**The AO2 anchors (Emirates):** Emirates **recycles all waste from its aircraft**; it wants to **maintain its reputation** as a business that cares about the environment and does this by **reducing fuel consumption**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Customers have become more interested in businesses that are **seen** to be green, so a business that acts on it **is rewarded in the market rather than merely avoiding criticism**. **Loaf's "Waste Not" scheme is the clearest form of this: it gives waste away instead of paying to dispose of it**, so the business **cuts a cost at the same time as doing something the local community can actually see**. **Customers who watch their own area being helped are more willing to buy from Loaf**, which is why the scheme is worth more than the money it saves. **The measurable end is that the community and the local area are visibly better off, so customers keep choosing Loaf** — and because it is helping charities and meeting its social objectives as well, the business's reputation does the advertising for it.

| Step | The move |
|---|---|
| **1. Point** | Green behaviour is **now something customers look for** |
| **2. Strand A** | Giving away waste **cuts disposal cost while being visible locally** |
| **3. Strand B** | A visibly helped community → **customers choose the business** |
| **4. Measurable end** | **Cost down and reputation up**, with no paid promotion |

**Second acceptable chain (Emirates):** recycling aircraft waste **protects a reputation the airline has spent decades building** → passengers who care about the environment **choose Emirates over a rival** → **higher passenger numbers at the same fare**.

> ⚠️ **The word "environmental" hides two different questions.** *"Importance of environmental factors"* means **what is happening outside the business** — legislation, customer attitudes, pressure groups. *"Why be more environmentally friendly"* means **what the business gains by acting**. This entry answers both; **the case facts are what tell you which one you have been asked**, because Loaf's scheme is an action and Emirates' recycling is too.

---

## 121. CASUAL STAFF — the benefits of employing them

**Asked:** *"Analyse the benefits for Loaf of employing casual staff."* — **May–June 2020 P1R, 4(b)**

**The AO2 anchors:** Loaf can use casual staff **to fill roles such as chefs for the cooking class** and can **ask them to work at short notice**; and it can use **a number of chefs with different skills** to run different classes.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> A casual worker is **called in when there is work rather than kept on the payroll**, so **Loaf does not pay a salary to a chef on the days no cooking class runs**. **That is the central benefit: the cost moves with the demand instead of against it** — a quiet week costs Loaf little, while a full timetable is staffed properly. **The second benefit is the range of skills Loaf can buy for the same money.** Because each chef is brought in for a particular class, **Loaf can run different cooking classes with chefs who specialise in each one**, rather than relying on one salaried chef to cover a menu they know only partly. **The measurable end is flexibility and a better product:** Loaf can put on the classes customers actually want, at short notice, **without carrying a wage bill it cannot fill** — which protects margin on the classes it does run.

| Step | The move |
|---|---|
| **1. Point** | Casual staff are **paid only when used** — the wage bill follows demand |
| **2. Strand A** | No salary on quiet days → **costs stay low outside the class timetable** |
| **3. Strand B** | Each chef bought for one specialism → **more classes, better taught** |
| **4. Measurable end** | **Flexibility to meet demand** at a cost the business can carry |

**Second acceptable chain:** casual chefs can be **called at short notice** → Loaf can accept a late booking it would otherwise turn down → **revenue captured that a salaried-only team would lose**.

> ⚠️ **"Casual staff are cheaper" is not enough on its own** — that is knowledge. The mark is for **why** the cost moves with demand, and for **what the skill range lets Loaf do that it could not do otherwise**. Compare with entry on **seasonal staff** and **temporary employees** in the 3-mark tier: same family, different question.

---

## 122. LOCATION — why it matters, and what decides it

**Asked:** *"Analyse the importance of location for TADS."* — **May–June 2020 P1, 1(g)**
**Also asked:** *"Analyse two factors that could influence Cadbury when locating a new factory."* — June 2022 P2R 1(g) · *"Analyse the benefits for Huawei of locating its factories near to its labour sources."* — Nov 2021 P2 1(g)

**The AO2 anchors (TADS):** TADS is located in a **wealthy area near to people with more disposable income**; and it **needs to be far away from competitors** in the music school industry.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> A drumming school sells a **specialised service to a local market**, and **parents are unlikely to travel far to bring a child to a lesson every week** — so location decides how many customers TADS can ever have. **Being in a wealthy area matters for a second reason: the families nearby have more disposable income**, which means they can afford lessons that are a choice rather than a necessity. **The other half of the decision points the opposite way.** TADS must be **far from other drumming schools**, because not everyone wants to learn the drums — the market for a specialised instrument is small, and **two schools in one area would split a market that is already narrow**. **The measurable end is that a good location raises demand while a poor one caps it:** the wrong side of town could mean full classes and higher fees, the wrong distance from a rival could mean both schools struggle.

| Step | The move |
|---|---|
| **1. Point** | A local, specialised service → **customers must live close enough to attend** |
| **2. Strand A** | Wealthy area → **more disposable income → lessons are affordable** |
| **3. Strand B** | Far from rivals → **the small, specialised market is not split** |
| **4. Measurable end** | **Demand is higher and defended** at the business's chosen site |

**Second acceptable chain (Cadbury's factory):** locate where **raw materials and labour are available** → lower transport and wage costs → **the chocolate can be produced more cheaply** → a better margin on every bar.

**Second acceptable chain (Huawei):** factories **near the labour sources** → workers arrive without relocating → **the business gets the skills it needs without paying relocation costs** → lower unit cost.

> ⚠️ **Location questions always have two directions — pull towards customers, push away from rivals or towards materials.** An answer that only says "close to customers" answers half the question. **The mark scheme's second AO2 bullet is always the one candidates miss.**

---

## 123. CASH — why it is important to a business

**Asked:** *"Analyse the importance of cash to TADS."* — **May–June 2020 P1, 3(d)**
**Also asked:** *"Analyse the importance of cash to PPS."* — June 2024 P1R 4(b) · *"Analyse the importance of cash to the success of Ocean Vibes."* — Nov 2025 P1 4(b)

> **This topic has appeared three times in six years, on three different businesses. The chain does not change; only the bills do.**

**The AO2 anchors:** if TADS has **sufficient cash it can pay its electricity bills for the music studio**; if it **runs out of cash it cannot pay its music teachers**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Cash is what a business pays its bills **with, on the day they fall due** — and for TADS that means **the electricity for the music studio and the wages of the teachers who take the lessons**. **Running out of cash does not make the business unprofitable; it makes it stop.** **The consequence is immediate and physical: if TADS cannot pay the electricity bill the power is cut, and if it cannot pay its teachers they stop coming — so no lessons take place at all.** **That is what makes cash different from profit.** A business can be owed money by customers and still have no cash in the bank, and **the measurable end is that a profitable business trading on credit can still fail** because it cannot meet a payment on the day it is due. Cash is the difference between a business that is doing well and a business that is still open.

| Step | The move |
|---|---|
| **1. Point** | Cash is what **pays the bills on the due date** |
| **2. Strand A** | No cash → **electricity cut, teachers unpaid** |
| **3. Strand B** | No teachers or power → **no lessons can be delivered at all** |
| **4. Measurable end** | **Trading stops** — even if the business is owed money and is profitable on paper |

**Second acceptable chain:** holding cash lets TADS **pay for an opportunity the moment it appears** — a set of drums at a discount, or a room becoming free — so **cash buys the chances that a business without it has to refuse**.

> ⚠️ **Never write "cash is the money a business has" and stop.** The whole mark is in **the failure mechanism** — unpaid bill → service withdrawn → no revenue. And never confuse cash with profit: **a profitable business can be insolvent**, and that distinction is what the examiners are testing.

---

## 124. BELOW-THE-LINE PROMOTION — the benefits

**Asked:** *"Analyse the benefits for TADS of using below-the-line promotion."* — **May–June 2020 P1, 4(b)**

**The AO2 anchors:** TADS could use **sales promotions such as coupons in the local newspaper Ollie writes a column for**; and it could **go to music festivals to showcase the skills of its students**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Below-the-line promotion targets **specific people with a direct offer**, rather than paying to be seen by everyone. **Coupons in the local newspaper are the clearest case: only readers of that paper see them, and those readers are the families living near the studio** — so the money buys attention in exactly the area TADS can serve. **Because Ollie writes a column in that paper, the coupons also carry his personal recommendation**, which is a credibility that a paid advertisement cannot buy. **The second route widens the reach while staying cheap.** Performing at music festivals puts TADS' students on a stage, and **spectators see what the teaching has actually produced** — which is evidence, not a claim. **The measurable end is students:** coupons convert readers into bookings, and the festival show converts spectators who had never considered drumming into enquiries.

| Step | The move |
|---|---|
| **1. Point** | Below-the-line targets **a specific, reachable audience** |
| **2. Strand A** | Local newspaper coupons → **only local families see them → every view is a prospect** |
| **3. Strand B** | A festival performance shows **what the teaching produces — proof, not promise** |
| **4. Measurable end** | **More students enrolled** for a small, controlled spend |

**Second acceptable chain:** below-the-line spend is **measurable** — TADS can count the coupons returned → it learns **which promotion actually works** → **future marketing budgets go where the students came from**.

> ⚠️ **Know the line.** **Above-the-line** = paid mass media (TV, national press, billboards) — *seen by many, targeted at nobody*. **Below-the-line** = targeted, direct, usually cheaper (coupons, samples, exhibitions, direct mail). Getting the side wrong loses the application mark. *Examiner-named content gap: "above-the-line".*

---

## 125. BRANDING — why it is important to a business

**Asked:** *"Analyse the benefit to HRMW of branding the products it sells."* — **May–June 2020 P2R, 1(g)**
**Also asked:** *"Analyse the importance of branding for Irsi Chocolatier."* — May 2023 P1, 1(g)

**The AO2 anchors (HRMW):** branding **differentiates its football products from those of its competitors**; and it helps customers **recognise its own logo, which appears on all its products**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> A brand is the logo and name a customer recognises **before they read a price**, and that recognition is what **separates HRMW's footballs from an identical unbranded one on the next shelf**. **The value of that separation shows up in two places.** First, **customers who know the brand are willing to buy the hockey stick too**, because the logo carries the reputation of the football with it — so one strong product **sells the whole range**. Second, **advertising becomes easier and cheaper**, because the business no longer has to explain who it is: **it only has to say what the new product does**. **The measurable end is that customers choose the branded product over an unbranded equivalent**, which lets HRMW charge for the reputation rather than competing on price alone.

| Step | The move |
|---|---|
| **1. Point** | A brand is **recognition before price** — it differentiates |
| **2. Strand A** | The logo carries the reputation onto **every other product in the range** |
| **3. Strand B** | Recognition makes **each advertisement work harder for the same spend** |
| **4. Measurable end** | **Customers choose branded over unbranded** → price power |

**Second acceptable chain:** a recognised brand is **a promise of consistent quality** → customers who have been satisfied once **buy again without comparing** → lower customer-acquisition cost on every repeat sale.

> ⭐ **The two halves the scheme rewards are differentiation and recognition.** "Branding makes the business famous" is neither — it is a slogan. **Differentiated from what, and recognised by whom, and then what does the customer do?**

---

## 126. FINANCIAL DOCUMENTS — why a bank is interested in them

**Asked:** *"Analyse why a bank would be interested in HRMW's financial documents if it were to apply for a loan."* — **May–June 2020 P2R, 4(b)**

**The AO2 anchors:** a bank **needs details of HRMW's financial situation to assess the risk of granting the loan**; and it would look at **several years' accounts to see a pattern or trend and whether there are large debts**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> A bank is deciding **whether it will be paid back**, and the financial documents are the only evidence it has — so it reads them **to price the risk of the loan**. **One year tells it very little, which is why the bank asks for several:** a single good year can be luck, **but the same trend repeated shows whether HRMW is reliably profitable or simply had one good season**. **The bank is looking for two things at once.** It wants to know **whether the business generates enough funds to pay back the interest as well as the loan**, and it wants to see **whether HRMW already has large debts**, because a business owing money elsewhere is a business behind in the queue for repayment. **The measurable end is the terms HRMW is offered:** a business that can show years of successful trading **may receive a lower rate of interest**, because the bank has less reason to charge for risk.

| Step | The move |
|---|---|
| **1. Point** | The documents are the bank's **only evidence of the risk** |
| **2. Strand A** | Several years → **a trend, not one lucky year** |
| **3. Strand B** | Existing debts + ability to pay **interest as well as capital** |
| **4. Measurable end** | Proven trading record → **a lower interest rate** on the loan |

**Second acceptable chain:** the documents also show **what the loan is secured against and how much the business owns** → the bank can recover its money if HRMW fails → **it is more willing to lend at all**, not just at a lower rate.

> ⚠️ **Answer the question that was asked: why the BANK cares, not why the business keeps accounts.** The difference is that the bank is **pricing risk**, and every chain you write must end in something the bank does — lending, refusing, or charging more.

---

## 127. INTERVIEWING CANDIDATES — why it is central to recruitment

**Asked:** *"Analyse why Emirates considers interviewing pilots as an important part of the recruitment process."* — **May–June 2020 P2, 4(b)**
**Also asked:** *"Analyse why Starbucks thinks it is important to interview candidates that have applied for a job with them."* — June 2025 P2, 4(b)

**The AO2 anchors (Emirates):** it gets **the opportunity to employ only those pilots with the skills it wants**; and **Emirates' staff can ask the pilots questions to judge whether they meet the airline's needs**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> A CV or application form shows **what a candidate has done**, but a pilot's job depends on **how they behave under pressure and how they work with a crew** — and that cannot be written down. **The interview is where Emirates' own staff ask the questions that test it**, drawing out how a candidate would react rather than taking their word for it. **That questioning matters more in this job than in most: choosing wrongly is not a wasted salary, it is a safety and reputational risk** that no amount of later training fully removes. **The measurable end is the quality of the crew Emirates ends up with** — pilots who meet the airline's needs serve passengers better, and **better service wins market share** from rival airlines flying the same routes.

| Step | The move |
|---|---|
| **1. Point** | Paper shows **what** a candidate did; an interview shows **how** they behave |
| **2. Strand A** | Emirates' own staff probe with questions → **judge fit beyond the CV** |
| **3. Strand B** | A wrong hire in a safety-critical job is **not recoverable by training** |
| **4. Measurable end** | **Better service → greater market share** |

**Second acceptable chain:** seeing the candidate in person reveals **attitude and communication** → the recruiter can judge whether they fit the airline's culture → **new staff settle faster and stay longer**, which cuts repeated recruitment costs.

> ⭐ **The scheme's phrase is "only those pilots with the skills it wants".** *Selection* is the point of an interview — **not "the business gets to know the candidate"**, which is a description rather than a consequence.

---

> ### ⚠️ CORRECTION TO BATCH 5b — four blocks were left uncovered
>
> Batch 5b claimed *"the twelve 6-mark questions of May–June 2019, collapsed into seven topics"*. **That was wrong, and it is exactly the kind of error this bank exists to prevent.** Seven entries covered **eight** blocks (13, 14, 15, 16, 17, 18, 19, 24). **Four were left uncovered** — and they are now entries **128–131** below:
>
> | Block | Question | Now |
> |---|---|---|
> | 20 P2R 3(d) | *Analyse why Yellow sells to all demographics.* | **entry 128** |
> | 21 P2R 4(b) | *Analyse the disadvantage for Yellow of customers using social media.* | **entry 129** |
> | 22 P2 1(g) | *Analyse the importance of good public relations for Tata Motor Company.* | **entry 130** |
> | 23 P2 3(d) | *Analyse how Tata Motor Company could use the financial information in Figure 2.* | **entry 131** |
>
> **The block count is the authority, not the entry count.** A topic that absorbs four blocks still leaves the other eight blocks needing their own entries, and *"collapsed into seven topics"* quietly assumed otherwise.

# BATCH 5d — 6-MARK ANALYSE, PART 4

**The four recovered 2019 blocks, plus June 2021's six and the first of June 2022's — nine new entries covering fourteen blocks.**

---

## 128. MASS MARKETING — why a business sells to everyone

**Asked:** *"Analyse why Yellow sells to all demographics."* — **May–June 2019 P2R, 3(d)**

> **Note the framing.** The question asks *why* — so the answer is the **business reason for targeting everyone**, not a description of mass marketing.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Selling to every demographic means **Yellow does not have to decide who its customer is** — T-shirts are bought by teenagers, by parents buying for children, and by adults buying for themselves, so **one design and one production run serves all of them**. **That has a direct cost consequence: the range does not have to be split into sizes of market, so each line is made in far larger volumes.** **Higher volume per line is what lets Yellow buy materials in bulk and keep the unit cost down** — which is what makes its prices competitive enough to sell to everyone in the first place. **The measurable end is reach and cost reinforcing each other:** selling to all demographics gives the volume that lowers unit cost, and the low unit cost is what allows it to keep selling to all demographics rather than retreating to a niche.

| Step | The move |
|---|---|
| **1. Point** | Targeting everyone → **no market to choose and no customer to exclude** |
| **2. Strand A** | One design serves all buyers → **larger volumes per line** |
| **3. Strand B** | Volume → **bulk buying → lower unit cost** |
| **4. Measurable end** | **Competitive prices → wider reach still** |

**Second acceptable chain:** mass appeal **spreads the risk** — a fashion trend that fails to sell in one segment still sells in another → **the business is less exposed to a single taste changing**.

> ⭐ **Compare with the niche/segmentation material.** Entry on **market segmentation** (3-mark tier) is the opposite strategy. **Both are legitimate** — the mark is for the *reason*, not for preferring one.

---

## 129. SOCIAL MEDIA AND REVIEWS — the effect on a business

**Asked:** *"Analyse the disadvantage for Yellow of customers using social media."* — **May–June 2019 P2R, 4(b)**
**Also asked:** *"Analyse the impact of customers using social media to review Can Culleretes."* — June 2022 P1R 3(d) · *"Analyse the disadvantages to M&M of using social media."* — May 2023 P2R 1(g)

**The AO2 anchors (Can Culleretes):** social media **can increase the number of reviews** of its meals and services; **negative reviews of the food served could be left**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Social media gives every customer **a public voice, whether or not they know anything about the business** — so the reviews multiply, and **most of them will be written by people who had a problem rather than by the satisfied majority**. **Can Culleretes is exposed in a particular way because it depends on tourists.** A visitor choosing where to eat in an unfamiliar city **has no experience of their own to rely on, so the reviews are the only evidence they have** — and **a few bad ones can send them to another restaurant, which is a sale lost before the customer ever walked past the door.** **The measurable end is also a trap in the other direction:** the positive reviews exist too, but **when both are present the doubt spreads, and tourists begin to doubt the good reviews as well**, so the damage is not limited to the bad ones.

| Step | The move |
|---|---|
| **1. Point** | Social media gives **every customer a public voice** |
| **2. Strand A** | Tourists have **no experience of their own** → reviews become the deciding evidence |
| **3. Strand B** | A few bad reviews → **customers go elsewhere before arriving** |
| **4. Measurable end** | **Sales lost at the decision stage**, and doubt spread to the good reviews |

**Second acceptable chain:** a negative review is **permanent and searchable** → it is seen by customers for years, unlike a complaint made privately → **one bad night keeps costing sales long after the problem is fixed**.

> ⚠️ **The question almost always says "disadvantage" or "impact" — read which.** An *impact* question wants **both directions**, because the scheme's AO2 lists the extra reviews *and* the negative ones. A *disadvantage* question wants you to drive the negative chain hard. **The same facts, used differently.**

---

## 130. PUBLIC RELATIONS — why it matters

**Asked:** *"Analyse the importance of good public relations for Tata Motor Company."* — **May–June 2019 P2, 1(g)**

> **Public relations is not advertising and not sponsorship.** PR is **managing how the business is seen** — the press, the public, the reputation — and it is the only promotion method that **cannot be bought outright**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Public relations is how a business **manages what the public and the press think of it**, and for a car manufacturer **that is not a marketing side-issue: what people believe about a car affects whether they will sit in one**. **Tata's reputation is built or damaged in the press rather than in its own advertising**, and the difference shows up hardest when something goes wrong — **a recall, an accident, or a safety concern reaches the public through journalists, and a business with good PR is given a fair hearing while one without it is judged guilty in the coverage.** **The measurable end is that good PR protects sales that a rival's bad headline would destroy**, and it does so more cheaply than any advertising campaign: a favourable article **costs nothing to place and is believed more than a paid advertisement**, because it is written by someone with no money in the outcome.

| Step | The move |
|---|---|
| **1. Point** | PR shapes **what the public and press believe**, not what they are told |
| **2. Strand A** | A crisis reaches the public **through journalists** — PR decides how it lands |
| **3. Strand B** | Favourable coverage is **free and more credible than paid advertising** |
| **4. Measurable end** | **Sales protected in a crisis**, at no media cost |

**Second acceptable chain:** good PR **attracts and keeps staff and investors**, because people prefer to be associated with a business that is well regarded → recruitment and funding both get easier.

> ⭐ **Keep the three apart for the exam.** **Sponsorship** = paying to be linked to an event (entry 101). **Advertising** = paying for space (entries on above/below-the-line). **Public relations** = **earning** favourable coverage; you influence it, you do not buy it.

---

## 131. USING FINANCIAL INFORMATION — how the figures inform decisions

**Asked:** *"Analyse how Tata Motor Company could use the financial information in Figure 2."* — **May–June 2019 P2, 3(d)**
**Also asked:** *"Analyse how useful the information in Figure 2 is to Loaf."* — May–June 2020 P1R 3(d) · *"Analyse the likely benefits to Emirates of using financial information when making business decisions."* — May–June 2020 P2 1(g) · *"Analyse how Artify Studio could use the information in Figure 1 to assess the performance of the business."* — Nov 2021 P1 3(d)

> **These four questions all say "the information in Figure N". That is a signal:** the figures **must be quoted**, and the mark scheme's AO2 bullets are built on them.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> The figures turn a decision from an opinion into **something that can be measured and compared**. Taken on its own, **a number tells Tata nothing useful** — what makes it information is the comparison, **against last year, or against a rival, or against the target the business set itself**. **That comparison is what identifies a problem before it becomes a crisis.** If a margin is falling while sales are rising, **the figures show that costs are running ahead of revenue — which no glance at the bank balance would reveal**, because the business is still taking more money each month. **The measurable end is the decision that follows:** Tata can see whether a route or a model **should be continued, re-priced or dropped**, and it can judge whether it needs to take action in the coming year rather than discovering the problem afterwards.

| Step | The move |
|---|---|
| **1. Point** | A figure only becomes information **when compared** — last year, a rival, or a target |
| **2. Strand A** | Comparison **reveals a trend before it becomes a crisis** |
| **3. Strand B** | It shows problems **the bank balance hides** — margins falling while sales rise |
| **4. Measurable end** | A decision to **continue, re-price or cut**, made on evidence |

**Second acceptable chain:** the figures tell Tata **whether it needs short-term finance** — and by how much — so an application to the bank is for **a calculated amount rather than a guess**, which is more likely to be approved.

> ⚠️ **Quote the figures.** A candidate who writes *"the information helps them make decisions"* without ever naming **the ratio, the percentage or the year** has answered nothing. **The AO2 mark lives in the number.**

---

## 132. MARKETING — the importance of it

**Asked:** *"Analyse the importance of marketing to NOF."* — **May–June 2021 P1, 1(g)**

**The AO2 anchors:** the result of marketing would **enable NOF to adapt its overnight accommodation to what the customers want**; and marketing can be used to **make customers aware of its organic honey**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Marketing does two jobs for NOF, and they are different jobs. **The first is finding out what customers want — because marketing starts with research, not with advertising**, and that is what allows NOF to **adapt its overnight accommodation to what guests actually want** rather than to what Amanda and Ken assume they want. **Being wrong about that is expensive: accommodation is fixed once built.** **The second job is telling people what exists. NOF sells organic honey, and honey is the kind of product a guest buys on recognition** — so unless marketing **makes them aware of it**, the honey stays on the shelf beside a farm the guest has just enjoyed staying on. **The measurable end is two revenue streams rising together:** more bookings for the rooms, and **more of each guest's spend going to NOF's honey** rather than being taken home as a memory.

| Step | The move |
|---|---|
| **1. Point** | Marketing is **research as well as promotion** |
| **2. Strand A** | Research → **accommodation adapted to real demand** (costly to get wrong) |
| **3. Strand B** | Promotion → **guests aware of the honey, which needs recognition** |
| **4. Measurable end** | **Bookings up and spend per guest up** |

**Second acceptable chain:** marketing **builds the brand** so that NOF is chosen over another farm stay on a booking site → the business **stops competing on price alone**.

> ⚠️ **"Marketing is advertising" is the single most expensive misconception in this course.** Marketing = **identifying, anticipating and satisfying customer needs profitably** — the marketing mix, research, segmentation and the rest. **If your answer is only about promotion, you have answered a third of the question.**

---

## 133. TRAINING EMPLOYEES — the benefits of training all of them

**Asked:** *"Analyse the benefits to NEXT of training all its employees."* — **May–June 2021 P2, 1(g)**

**The AO2 anchors:** if NEXT trained all its employees, **they are trained in a consistent fashion so they can operate in the same way across 70 countries**; and employees attending these sessions **gain customer service skills they can use in NEXT shops**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> The word that carries this question is **"all"**. Training *every* employee means the standard is **consistent — so a customer who walks into a NEXT in one of the 70 countries gets the same experience as one at home**, which is the whole basis of a brand that trades internationally. **Inconsistency is what damages a chain: a good shop and a poor shop under one name cost the brand the trust the good shop earned.** **The second benefit is what the training actually puts into the staff.** Customer service skills **let an assistant do more than hand over a product — they can advise, suggest and sell**, which is where sales technique turns a browsing customer into a buying one. **The measurable end is higher sales at the existing wage bill:** the same employees, serving better, **selling more from the same stock and the same hours** — which is why training is an investment rather than a cost.

| Step | The move |
|---|---|
| **1. Point** | Training **all** staff → **one consistent standard across 70 countries** |
| **2. Strand A** | Consistency protects the brand; inconsistency **costs it the trust it has built** |
| **3. Strand B** | Customer service skills → **staff can sell, not just serve** |
| **4. Measurable end** | **Higher sales from the same payroll** |

**Second acceptable chain:** trained staff **handle complaints without escalating them** → fewer problems reach head office and fewer customers leave → **the cost of fixing mistakes falls** as well.

> ⭐ **Command-word discipline:** this says *benefits*, so you may stop at the gain. Compare entry **111 (induction)** — induction is **before** the job; training is **an ongoing investment in someone already doing it**. **Do not write one answer for both.**

---

## 134. COMMUNICATION BARRIERS — why a business removes them

**Asked:** *"Analyse why NEXT would want to remove any communication barriers within its organisation."* — **May–June 2021 P2, 3(d)**

**The AO2 anchors:** as NEXT **trades in different countries it needs employees to speak the language of that country**; and **if NEXT has long chains of command, messages from head office could take too long to reach shop assistants**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> A communication barrier is **anything that stops a message arriving intact** — and in a business trading in different countries there are two of them stacked on top of each other. **The first is language.** If staff in a store cannot speak the language of the customers around them, **the shop cannot serve them at all**; and if head office and the store do not share a language, **instructions arrive either late or wrong**. **The second is the chain of command.** A message from head office **passes through every layer on the way down to a shop assistant**, and **each layer is a chance for it to be delayed or to become unclear and inaccurate** — so the instruction the assistant finally receives is not the one that was sent. **The measurable end is fewer errors and more sales:** staff who understood the instruction **do the right thing the first time**, and staff who can speak to the customer **make the sale that an incomprehensible conversation would have lost**.

| Step | The move |
|---|---|
| **1. Point** | A barrier = **anything that stops a message arriving intact** |
| **2. Strand A** | Language → **cannot serve the local customer, cannot receive instructions** |
| **3. Strand B** | Long chain of command → **delay and distortion at every layer** |
| **4. Measurable end** | **Errors avoided and sales completed** |

**Second acceptable chain:** removing barriers lets **information flow upwards too** — shop assistants tell head office what customers are asking for → **decisions are made on what is really happening** rather than on head-office assumption.

> ⚠️ **Name the barrier, then break it.** *"Communication is important"* earns nothing. **Language, chain of command, noise, jargon, too many layers** — pick the ones the case supports and show what each one costs.

---

## 135. INTEREST RATES — the effects of a change in them

**Asked:** *"Analyse the effects for NEXT of an increase in UK interest rates."* — **May–June 2021 P2, 4(b)**
**Also asked:** *"Analyse the effect on TUI customers of an increase in interest rates."* — June 2024 P2 3(d) · *"Analyse the effect of a decrease in interest rates on Artify Studio."* — Nov 2021 P1 1(g)

> **Three blocks, and one of them asks about the *customers* rather than the business. Read who the question names.**

**The AO2 anchors (NEXT, rates rise):** consumers will **spend less on items such as clothing**; and consumers are **less likely to purchase NEXT furniture on credit**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> An interest-rate rise reaches NEXT through **two routes, and only one of them is about NEXT's own borrowing**. The first and larger effect is on **the customer's wallet**: higher rates mean **higher repayments on a mortgage or a loan**, so **households have less left to spend, and clothing is one of the first things they cut** — NEXT loses sales it did not do anything to lose. **The second effect is on credit specifically.** Furniture bought on credit becomes **more expensive to finance**, so **customers postpone those purchases altogether**, which is why the effect hits the big-ticket lines hardest. **The measurable end is unsold stock and lower profit:** reduced sales leave NEXT **holding inventory it bought in advance of demand that did not arrive**, and stock sitting in a warehouse costs money without earning any.

| Step | The move |
|---|---|
| **1. Point** | Higher rates → **higher repayments → less household income to spend** |
| **2. Strand A** | Discretionary spending is cut first → **clothing sales fall** |
| **3. Strand B** | Credit becomes dearer → **big-ticket items postponed** |
| **4. Measurable end** | **Unsold inventory and lower profit** |

**Second acceptable chain (if the question is about the business's own borrowing):** NEXT pays **more interest on any variable-rate loan** → costs rise **without any change in sales** → the profit margin narrows on exactly the same turnover.

**Second acceptable chain (TUI's customers):** higher rates make **borrowing for a holiday dearer**, so **customers choose a cheaper destination or postpone the trip** → TUI fills fewer seats and must discount to fill them.

> ⚠️ **Direction matters, and the question sets it.** *"An **increase**"* and *"a **decrease**"* are opposite answers — the Nov 2021 Artify question is about a **decrease**, where **the cost of borrowing falls and demand rises**. Getting the direction wrong makes every chain you write wrong, and **an answer built on a reversed premise scores nothing.**

---

# BATCH 5e — 6-MARK ANALYSE, PART 5

**7 entries covering 11 blocks — the rest of June 2022, and the end of June 2021.** Two of these are the tier's heaviest repeats: **motivating employees appears four times** and **robotics twice**.

---

## 136. TECHNOLOGY AND PRODUCTIVITY — the impact of an app on how work is done

**Asked:** *"Analyse the likely impact on productivity if Can Culleretes launch this app."* — **June 2022 P1R, 1(g)**

**The AO2 anchors:** the app means **waiters do not have to take orders at the customer's table**; and **as soon as customers place the order the kitchen receives it immediately**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Productivity is **output per worker per hour** — so the question is what the app lets each waiter do more of. **Right now a waiter walks to a table, takes an order by hand and carries it to the kitchen; the app removes that trip entirely, because the order reaches the kitchen the moment the customer places it.** **Two things happen at once, and both raise productivity.** First, **the same number of waiters serves more tables in a night**, because the time previously spent walking and writing is spent serving. Second, **the kitchen starts cooking sooner**, so the gap between ordering and eating shrinks — **tables turn over faster, which means more covers from the same floor space and the same staff**. **The measurable end is lower cost per customer served:** the wage bill has not changed, but the revenue the same team generates has — which is precisely what an increase in productivity means.

| Step | The move |
|---|---|
| **1. Point** | Productivity = **output per worker**, so remove the wasted movement |
| **2. Strand A** | The app **removes the order-taking trip** → waiters serve more tables |
| **3. Strand B** | The kitchen receives the order instantly → **food reaches the table sooner** |
| **4. Measurable end** | **Table turnover rises** → more covers from the same payroll |

**Second acceptable chain:** orders taken by app **cannot be misheard or mis-written** → fewer wrong dishes → **less food wasted and fewer meals remade** → a cost saving on top of the time saving.

> ⚠️ **Productivity is not production.** Producing *more* while hiring *more* is not a productivity gain. **The definition to hold in your head: output ÷ input — more from the same, or the same from less.** An answer that says "they can serve more customers" without holding the staff constant has missed it.

---

## 137. RESPONDING TO CHANGES IN THE MARKET — why it matters

**Asked:** *"Analyse the importance of Can Culleretes responding to changes in its market."* — **June 2022 P1R, 4(b)**

**The AO2 anchors:** Montserrat and Alicia **need to keep up with changing customer tastes if they want to remain competitive**; and **as the second oldest restaurant in Spain it may place no importance in responding to changes**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> A market does not stand still, so **a restaurant that does not change is not staying the same — it is falling behind what customers now expect**. **Can Culleretes has a specific reason to be complacent, and that is exactly the danger: as the second oldest restaurant in Spain it has decades of goodwill and a family reputation** to rely on, which is precisely what makes it easy to assume the customers will keep coming. **The market does not owe it that.** Tastes move, and the restaurant **sits in a busy area where other restaurants are competing for the same visitors** — so customers who find the menu dated **walk into the next place rather than giving it another chance**. **The measurable end runs both ways.** Responding keeps it competitive and keeps tourists choosing it over the neighbours; not responding **turns a long history into a reason customers assume it is old-fashioned** — and a reputation that took generations to build is spent in a single season.

| Step | The move |
|---|---|
| **1. Point** | Standing still = **falling behind a moving market** |
| **2. Strand A** | Its long history makes **complacency the natural mistake** |
| **3. Strand B** | In a busy area, a dated offer → **customers go next door** |
| **4. Measurable end** | **Competitiveness retained** — or goodwill spent in one season |

**Second acceptable chain:** responding means **changing the menu, the pricing or the service to match what customers now want** → the restaurant **attracts a newer, younger customer** alongside its regulars → the customer base **widens instead of ageing**.

> ⭐ **This entry pairs with entry 120 (external factors) and entry 138.** *"Changes in the market"* means **the customer side** — tastes, competitors, expectations. **External factors** is broader: economic, legal, technological, social. **Read which one the case supports.**

---

## 138. EXTERNAL FACTORS — the likely impact on business decisions

**Asked:** *"Analyse the likely impact of external factors on business decisions made by TBTS."* — **June 2022 P1, 1(g)**

**The AO2 anchors:** **social factors can help TBTS** as changes in society show customers **might be demanding more environmentally friendly toys**; and **technological advances could increase the cost of buying, or the price of, a range of toys**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> External factors are things the business **cannot control but must react to**, and TBTS is exposed on two at once. **On the social side the change is in TBTS's favour: customers are increasingly demanding environmentally friendly toys**, so a toystore that stocks them **is acting responsibly and selling high-quality goods at the same time** — which brings more customers in **and gives it a reason to be chosen over a rival**. **The technological factor cuts the other way.** Toys that embed new technology **cost more to buy in the first place**, and **if the technology moves rapidly the stock TBTS bought becomes unwanted** — because customers buy the newer version instead. **The measurable end is a decision TBTS has to make deliberately:** order cautiously and risk running out, or order heavily and risk **being left with stock it cannot sell at any useful price**. Either way, **the external factor has decided something the owner would rather not have had to think about.**

| Step | The move |
|---|---|
| **1. Point** | External factors are **outside the business but inside the decision** |
| **2. Strand A** | Social shift to green toys → **brings customers, if TBTS reacts** |
| **3. Strand B** | Technology moving fast → **expensive stock that goes out of date** |
| **4. Measurable end** | A **stock decision forced by the outside world**, not by choice |

**Second acceptable chain:** an economic factor — a recession, or a fall in disposable income — **moves parents from premium toys towards cheaper ones**, so TBTS must decide whether to **cut prices, narrow the range or accept lower sales**.

> ⚠️ **"External factors" is a category, not an answer.** You must **name the factor** (social, technological, economic, legal, environmental) and **then show what it does to this business**. A list of five factors with no chains scores in the bottom level — **and bullets disqualify the top levels outright.**

---

## 139. MOTIVATING EMPLOYEES — the importance of it

**Asked:** *"Analyse the importance of TBTS motivating its employees."* — **June 2022 P1, 3(d)**
**Also asked:** *"Analyse the importance to Kumaran, the owner of Café Pinch, of having motivated employees."* — June 2024 P1 1(g) · *"Analyse the importance to Aude Anglaret of motivating her employees."* — May 2023 P1R 1(g) · *"Analyse the benefits for Premier Inn of motivating its employees."* — Nov 2024 P2 3(d)

> **This topic has been asked on four separate papers — TBTS, Café Pinch, Aude Rose and Premier Inn. It is the most repeated topic in the 6-mark tier. Learn the chain once and it answers all four.**

**The AO2 anchors (TBTS):** motivated employees **can better meet the needs of customers who want to buy toys**; **if TBTS does not have motivated employees it could lead to lower sales**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> A demotivated employee **is still being paid — they are simply not doing what they are capable of**. In a toy shop that shows up at the counter: a member of staff who cannot be bothered **fails to answer a customer's question properly, and the customer leaves without buying** — so **motivation is not a welfare issue, it is a sales issue**. **The second effect is on how much work gets done.** An unmotivated team **produces less per hour**, which means **TBTS gets less output from the same wage bill** and **finds it harder to hit its own targets, whatever those targets are**. **The measurable end is straightforward: motivated staff sell more**, because they are willing to spend time with a customer and to help them find what they came for — and **the same payroll that produces low sales when staff are unhappy produces high sales when they are not**, which makes motivation one of the cheapest levers the business has.

| Step | The move |
|---|---|
| **1. Point** | A demotivated worker **is still paid, but produces less** |
| **2. Strand A** | Poor service → **a customer leaves without buying** |
| **3. Strand B** | Lower output per hour → **the same wage bill buys less work** |
| **4. Measurable end** | **Sales and goals**, from an unchanged payroll |

**Second acceptable chain:** motivated staff **stay** → TBTS avoids the cost of recruiting and retraining a replacement → **the skills stay in the business and the wage bill stays stable**.

> ⚠️ **Do not list Herzberg, Taylor or Maslow here.** Those are for the 3-mark "motivating employees" question, where the mark is for the **method**. **This question asks what motivation does for the business**, so the mark is in the **consequences** — retention, productivity, service, sales.

---

## 140. LEGISLATION — why a government introduces it

**Asked:** *"Analyse why some governments have introduced legislation to reduce the amount of sugar in chocolate."* — **June 2022 P2R, 3(d)**

> **Read the party again.** The question is **why a GOVERNMENT acts** — not why Cadbury complies. The beneficiary is the country and its citizens.

**The AO2 anchors:** legislation to reduce sugar **would reduce the sugar levels for its customers**; and it **would help reduce the demand on, and impact on, the health service** as fewer customers need its services.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> A government legislates when **industry will not do it voluntarily**, and the target here is a product that is cheap, popular and eaten habitually. **Reducing the sugar in chocolate lowers the sugar its citizens consume without needing them to change what they choose** — and that is the point of legislating rather than campaigning: **it works on people who ignore the advice.** **The second reason is the cost to the country.** Consuming too much sugar contributes to being **overweight**, which brings **diabetes and other illnesses** with it — and those **cost the health service money that then cannot be spent elsewhere**. **The measurable end is on the public finances:** fewer health-related illnesses **reduce the cost of treating them**, and the country's overall health improves, which raises **productivity and the standard of living** as well as easing the strain on hospitals.

| Step | The move |
|---|---|
| **1. Point** | Government acts because **industry will not act voluntarily** |
| **2. Strand A** | Legislation reaches people **who ignore advice and campaigns** |
| **3. Strand B** | Sugar → obesity → illness → **cost to the health service** |
| **4. Measurable end** | **Lower health costs and better public health** |

**Second acceptable chain:** a government also protects **children**, who cannot judge the long-term consequences of what they eat → the legislation **reduces harm to people who did not consent to the risk**.

> ⭐ **The same "who benefits" logic as entry 112 (Malaysia).** This qualification repeatedly sets questions where the business is **not** the beneficiary. **Check who the question names before writing the first sentence.**

---

## 141. OVERDRAFT — why a business uses short-term finance

**Asked:** *"Analyse why Cadbury may have needed to take out an overdraft."* — **June 2022 P2R, 4(b)**

**The AO2 anchors:** an overdraft allows Cadbury **to withdraw temporary funds from its bank account to pay suppliers for an unexpected delivery of cocoa**; and **if Cadbury needs to pay an unexpected bill to keep the factory working**. Also: **it is flexible as Cadbury will only pay interest on the amount they are overdrawn**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> An overdraft is **a facility, not a loan** — the business may draw on it when it needs to and repay when it can, and **it only pays interest on the amount actually overdrawn**. **That structure is what suits the problem Cadbury has: an unexpected delivery of cocoa, or a bill that must be paid to keep the factory running.** **Neither is planned, which is exactly why a fixed loan would be the wrong tool** — Cadbury would be paying interest on money it was not yet using, for a cost it did not expect to incur. **The measurable end is that production never stops.** The suppliers are paid on time, **the cocoa arrives and the factory keeps working**, which means **revenue keeps coming in while Cadbury sorts out its cash flow** — and the relationship with the supplier survives, which matters for the next delivery.

| Step | The move |
|---|---|
| **1. Point** | An overdraft is **flexible** — draw when needed, pay interest only on the amount used |
| **2. Strand A** | The cost is **unexpected** → a fixed loan would be the wrong shape |
| **3. Strand B** | Paying the supplier on time **keeps the factory running** |
| **4. Measurable end** | **Production and revenue continue** while cash flow recovers |

**Second acceptable chain:** an overdraft can be arranged **at short notice** → Cadbury can respond to an opportunity — **a discounted bulk purchase of cocoa** — that a loan application would take too long to fund.

> ⚠️ **Match the source of finance to the *timing* of the need.** **Short-term** (overdraft, trade credit) suits **unexpected, temporary gaps**. **Long-term** (loan, share capital, retained profit) suits **assets and expansion**. Choosing a long-term source for a temporary problem **costs interest unnecessarily** — and that reasoning is the difference between a 4 and a 6.

---

## 142. ROBOTICS — the benefits in manufacturing

**Asked:** *"Analyse the benefits to LEGO of increasing the use of robotics in the manufacture of toys and games."* — **June 2022 P2, 4(b)**
**Also asked:** *"Analyse the benefits to Rabanne of using robotics to manufacture its products."* — June 2025 P2R 4(b)

**The AO2 anchors:** increasing the use of robotics **reduces human error** in production; and robotics **increases the number of units that can be made**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> A robot does the same operation **the same way every time**, so the two things a production line loses to people — **variation and error — largely disappear**. **Fewer faults means fewer toys rejected**, and rejected toys are **the most expensive kind: the materials, the machine time and the labour have all been spent and there is nothing to sell.** **The second gain is speed. A robot does not tire, so it can run at a rate a human cannot hold for a full shift**, which means **more units come off the line in the same hours**. **The measurable end is manufacturing cost per toy falling** — because the waste falls and the fixed costs of the factory are spread over more units. And for a toy that must fit together with other toys, **consistency is not just cheaper, it is what makes the product work at all.**

| Step | The move |
|---|---|
| **1. Point** | Robots are **consistent** — no variation, no human error |
| **2. Strand A** | Fewer faults → **less rejected stock** — the costliest waste there is |
| **3. Strand B** | No fatigue → **higher output from the same hours** |
| **4. Measurable end** | **Lower manufacturing cost per unit**, and a product that fits |

**Second acceptable chain:** robots allow **production to continue overnight and at weekends** without a night-shift wage bill → capacity rises **without a proportional rise in labour cost**.

> ⚠️ **This is the "robotics benefits" question — the counter-argument (high set-up cost, job losses, inflexibility) is a different question.** Compare entry **109 (flow production disadvantages)**, which is exactly that reverse. **The scheme's own two AO2 bullets here are `human error` and `number made` — hit both and you have the level 3 answer.**

---

# BATCH 5f — 6-MARK ANALYSE, PART 6

**6 new entries covering May–June 2024's twelve blocks.** Six of the twelve were the same topic as an entry already banked — including **cash** for the third time and **motivating employees** for the fourth — and they are pointed at those entries rather than repeated:

| Block | Topic | Where it now lives |
|---|---|---|
| 55 P1R 1(g) *the gross profit margin to PPS* | profitability ratios | **entry 118** |
| 57 P1R 4(b) *the importance of cash to PPS* | cash | **entry 123** *(3rd appearance)* |
| 58 P1 1(g) *motivated employees (Café Pinch)* | motivating employees | **entry 139** *(4th appearance)* |
| 61 P2R 1(g) *problems if customer needs are not satisfied* | customer needs | **entry 116** |
| 64 P2 1(g) *health and safety training in induction* | induction training | **entry 111** *(4th appearance)* |
| 65 P2 3(d) *effect on TUI CUSTOMERS of higher interest rates* | interest rates | **entry 135** |

> ### ⭐ WHAT SIX MERGES OUT OF TWELVE IS TELLING YOU
> **Half of May–June 2024's six-mark questions were topics this bank had already answered** — from papers two, three and five years older. That is the whole economic case for working by topic instead of by question: **the examination is more repetitive than it looks from any single paper, and it is the repetition that makes a finite bank possible.**

---

## 143. MARKET RESEARCH — why the research has to be reliable

**Asked:** *"Analyse the importance of reliable market research to obtain this information."* — **May–June 2024 P1R, 3(d)**

**The AO2 anchors:** PPS will want to find **accurate local data about pet owners so it can target its customers better**; and **as PPS is a small business it may find it easier to speak to its customers individually** to find out the needs of their pets.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Market research is only worth what the decision built on it is worth — **so unreliable research is worse than none, because the business acts on it with confidence.** If PPS's data about **local pet owners is inaccurate**, it will target **the wrong customers, in the wrong place, with the wrong product** — and every subsequent cost, from stock to advertising, is spent on a plan that was wrong from the start. **The second half of the answer is the advantage a small business has.** PPS **can speak to its customers individually**, which is something a chain cannot do; and because the owner is talking directly to the people buying the treats, **the information is first-hand and current rather than bought second-hand.** **The measurable end is better decisions:** reliable data on **what pet owners actually spend and on what** lets PPS **stock and price for real demand** — and **spending patterns** are what tell a small business where its margin really comes from.

| Step | The move |
|---|---|
| **1. Point** | Unreliable research is **worse than none** — you act on it confidently |
| **2. Strand A** | Wrong data → **wrong customers, wrong stock, wrong place** |
| **3. Strand B** | A small business **can ask its own customers** — first-hand and current |
| **4. Measurable end** | **Stocking and pricing that match real spending patterns** |

**Second acceptable chain:** reliable research **reduces the risk of a new product or a price change** → PPS can test the idea on customers **before spending the money** → the cost of being wrong falls to the price of the research.

> ⚠️ **Two kinds of unreliability, and the question accepts either.** **Sample** — the wrong people, or too few of them. **Accuracy** — leading questions, out-of-date data, or a respondent saying what they think you want to hear. **Name one and show what it costs.**

---

## 144. MEASURING BUSINESS SUCCESS — the factors considered

**Asked:** *"Analyse two factors Café Pinch might consider when measuring its success."* — **May–June 2024 P1, 3(d)**
**Also asked:** *"Analyse factors that Aude Rose might consider when measuring the success of its business."* — May 2023 P1R 4(b)

> **The word "two" is an instruction, not decoration.** Two factors, each developed — **not one factor developed well and a fragment of a second.**

**The AO2 anchors:** Kumaran **can check the business objectives he has set**; and he can **compare the annual financial details, such as profit from 2018 to the present**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Success has to be **measured against something the owner chose in advance**, otherwise it is only a feeling. **The clearest measure for Café Pinch is the objectives Kumaran set when he opened it** — because a business that has hit its own targets is succeeding **on its own terms**, and one that has not **needs to know that before it commits any more money**. **The second factor is the financial record.** Comparing **profit from 2018 through to the present** shows **a trend rather than a snapshot**: a single good year can be luck or a one-off event, **but profit rising year on year shows there is genuine demand for what the café sells** — and demand is what produces **loyal customers**. **The measurable end is that Kumaran can make the next decision on evidence:** the objectives tell him whether he is on course, and the trend tells him whether the business is getting stronger or merely holding still.

| Step | The move |
|---|---|
| **1. Factor 1** | **The owner's own objectives** — success on the business's own terms |
| **2. Factor 2** | **Profit over several years** — a trend, not a snapshot |
| **3. What it shows** | Rising year on year → **genuine demand → loyal customers** |
| **4. Measurable end** | A **decision made on evidence**, not on feeling |

**Second acceptable chain:** a service business can measure **customer satisfaction or repeat bookings** instead of profit → a café that is full but unprofitable **learns that the problem is price or cost, not demand** → it treats the right illness.

**Second acceptable chain (Aude Rose):** measuring success by **how the business is running compared with how she saw good restaurants run** when she worked in them → **the owner is the benchmark** → an early warning she can judge without waiting for the accounts.

> ⚠️ **"Profit" alone is one factor, not two.** The scheme wants you to reach for **at least one non-financial measure** — objectives, market share, customer satisfaction, staff retention — **because a business can be profitable and still failing at what it set out to do.**

---

## 145. MARKET SEGMENTATION — how a business uses it

**Asked:** *"Analyse how Café Pinch could use market segmentation to target its customers."* — **May–June 2024 P1, 4(b)**

**The AO2 anchors:** Café Pinch can **look at the spend of the customers who take away its food and drink**; and it may want to **target customers who work in Berlin or tourists who visit the city**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Segmentation means **splitting a market into groups with something in common and serving each group deliberately**, rather than offering the same thing to everybody. **Café Pinch already has two groups with almost nothing in common: the people who work in Berlin and the tourists passing through.** The workers **buy quickly, repeatedly and to a budget — they are regulars**; the tourists **buy once, want something authentic, and are willing to pay more for it**. **Serving both from one menu means serving neither well.** **Segmenting lets Kumaran check whether his price range covers both:** if the takeaway spend of the workers is low and the tourists expect more, **he can see whether the menu is priced so that one group is being priced out** — too expensive for the regulars, or **too cheap to convince a tourist they are getting the real thing.** **The measurable end is that each group is served on purpose** — loyalty rewards for the people who come every day, **an authentic German experience for the visitors** — so the same café earns from both without either subsidising the other.

| Step | The move |
|---|---|
| **1. Point** | Segmentation = **serving each group deliberately, not everyone the same** |
| **2. Strand A** | Workers buy **often, cheaply, to a budget**; tourists buy **once, authentically** |
| **3. Strand B** | The price range must **not price either group out** |
| **4. Measurable end** | **Both segments served** — loyalty schemes and authentic experience |

**Second acceptable chain:** segmenting by **spending level** shows which items are bought by which group → Kumaran **stocks and prices the menu around the groups that actually pay** → less waste on items nobody in either group buys.

> ⚠️ **The segmentation bases to have ready: demographic (age, income, gender), geographic, psychographic (lifestyle), behavioural (how and when they buy).** Here the useful ones are **behavioural and geographic — workers versus visitors.** *Examiner-named content gap: "demographic segmentation".*

---

## 146. RECRUITMENT DOCUMENTS — how they help select the right person

**Asked:** *"Analyse why Jimmy Choo asks all candidates applying for a vacancy to complete an application form."* — **May–June 2024 P2R, 3(d)**
**Also asked:** *"Analyse how recruitment documents may help Samsung to hire the best employees for its business."* — Nov 2025 P2 1(g)

**The AO2 anchors:** a completed application form gives **important details of each applicant, such as address and previous employment**; and an applicant for **sales manager can include all their experience of selling handbags**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> The value of a standard application form is **the word "all": every candidate answers the same questions, so the answers can be put side by side.** **Jimmy Choo has 30 candidates and needs one appointment**, and comparison is only possible if the information is in the same order and covers the same ground. **That structure is what makes the form a selection tool rather than a formality.** It captures **address — which matters for a role that may involve travel or shifts — and previous employment**, including **the specific experience of selling handbags that the sales manager role needs**. **The measurable end is a shorter, better interview list:** Jimmy Choo can **compare the forms, see which applicant is more suited, and call only those in** — which saves the interviewing time that would have been spent on the candidates the form has already ruled out.

| Step | The move |
|---|---|
| **1. Point** | **All candidates answer the same questions** → the answers are comparable |
| **2. Strand A** | Captures **the specifics the role needs** — experience of the product |
| **3. Strand B** | Captures **the practical facts** — address, employment history |
| **4. Measurable end** | **A shortlist to interview**, and the time saved on the rest |

**Second acceptable chain:** the form **provides a written record** of what each applicant claimed → a shortlisted candidate can be **questioned on what they wrote** at interview → the business **tests the claims rather than accepting them**.

> ⭐ **Know the recruitment document family, because they are asked together.** **Job description** — what the role involves. **Person specification** — what the person must have. **Job advert** — how it is communicated to the market. **Application form / CV** — what the candidate offers. **Each question asks about one of them; do not answer about another.**

---

## 147. SHARE CAPITAL — the benefit of using it to grow

**Asked:** *"Analyse the benefit to Jimmy Choo of using share capital to fund its growth."* — **May–June 2024 P2R, 4(b)**

**The AO2 anchors:** as a **large multinational**, it might be **easier to raise the large amounts of share capital** needed to fund further expansion; and **as an established multinational** it should have **existing and new shareholders wanting to buy the shares**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Share capital is **money from selling part-ownership of the company**, and the amount it can raise **has no ceiling set by a lender's appetite**. **That is what makes it the right tool for rapid growth: a business expanding its clothing factories needs a large sum at once, which a single bank may be unwilling to lend against a plan.** **Jimmy Choo's position as an established multinational makes the route easier than it would be for anyone else** — there are **existing shareholders who already know the brand and new ones willing to buy in**, so the shares can actually be sold. **The measurable end is speed and cost together:** the funds arrive **fast enough to take advantage of increased demand for its products**, and **because it is share capital and not a loan, Jimmy Choo incurs no interest charges** — so more of the profit from the expansion stays inside the business.

| Step | The move |
|---|---|
| **1. Point** | Share capital has **no lender's ceiling** — suit a large, single sum |
| **2. Strand A** | Established multinational → **shareholders willing to buy** |
| **3. Strand B** | Funds arrive fast → **can seize increased demand** |
| **4. Measurable end** | **Growth funded with no interest to pay** |

**Second acceptable chain:** money raised by shares **does not have to be repaid** → a bad year does not put the business in breach of a repayment schedule → **the expansion can be allowed time to become profitable**.

> ⚠️ **The cost of share capital is not interest — it is ownership.** **Dividends and a reduced share of the profit for the original owners** is the counter-argument, and it belongs in a 9-mark or 12-mark answer. **This question asks for the benefit**, so lead with the amount, the speed and the absence of interest.

---

## 148. BOSTON MATRIX — how a business uses it

**Asked:** *"Analyse how TUI could make use of the Boston Matrix to review all the different holidays it offers."* — **May–June 2024 P2, 4(b)**

**The AO2 anchors:** TUI can use the **"Star" to decide which are the most profitable holidays in Turkey**; and it **will keep a "Cash Cow" such as a 14-day cruise** because it **generates a steady flow of income**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> The Boston Matrix takes **one product range and sorts it by market growth and market share**, and its value to TUI is that **it turns a long list of holidays into four groups with four different answers.** **The "Cash Cow" is the cruise: it sells steadily and needs little investment, so TUI keeps it on the books precisely because it generates a reliable flow of income** — that money is what funds everything else. **The "Star" is the holiday in Turkey that is growing and profitable: it is where the investment goes**, because a star today is the cash cow of the next few years. **The measurable end is a stopping decision, which is the hardest one for any business to make.** If some hotels in parts of Turkey are **less profitable than others**, the Matrix identifies them **as the place to stop** — so TUI can **move that hotel off the programme and find another**, and **use the revenue released to expand into different holiday experiences** rather than propping up a product that is not working.

| Step | The move |
|---|---|
| **1. Point** | The Matrix sorts a range into **four groups with four different actions** |
| **2. Strand A** | **Cash cow (the cruise)** → keep it, it funds the rest |
| **3. Strand B** | **Star (Turkey)** → invest, it is the next cash cow |
| **4. Measurable end** | **A stopping decision** — drop the weak hotel, fund the new experience |

**Second acceptable chain:** the remaining two boxes **identify the problem products** — low growth and low share — so TUI **knows which holidays to withdraw deliberately** rather than continuing to sell them out of habit.

> ⚠️ **Name the axes and the four boxes correctly.** **Market growth (high/low) against market share (high/low):** **Star** = high growth, high share · **Cash cow** = low growth, high share · **Question mark / problem child** = high growth, low share · **Dog** = low growth, low share. **Calling a dog a cash cow loses the application mark — and this is a named content gap in the examiners' reports.**

---
