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

> ✅ **THE 6-MARK TIER IS CLOSED.** All **114 blocks** are carried by entries **101–174** — verified by `layer_c_6mark_coverage.py`, which prints **114 covered / 0 remaining** and flags any dangling entry reference. **It was 74 entries for 114 blocks**, because **40% of the tier was a repeat of a topic already answered**: *multinational* and *motivating employees* **six times each**, *break-even* **five**, and *cash*, *SoCI*, *interest rates*, *branding*, *robotics*, *induction* and *host-economy benefit* **three or four times each**.

> ✅ **THE 9-MARK TIER BEHAVED DIFFERENTLY FROM THE OTHER TWO.** All **76** questions use **one framing** (*"justify which one of these two options…"*) with **one AO split** (AO2 3 · AO3 3 · AO4 3), so **the scaffolding in entry 175 is used 76 times**. But the tier holds **58 distinct option pairs across 76 blocks** — **it barely repeats its content**, unlike the 3-mark tier (152 → 97) and the 6-mark tier (114 → 74). **What repeats is the DECISION TYPE**: sources of finance is one decision type carrying **13 pairs**, and promotion + pricing together are two decision types carrying **21 blocks in 17 pairs**. **Every decision type is now closed** — see the tier summary below.
>
> ✅ **FOUR decision types were closed first, and the ordering is the point** — **sources of finance** (13 pairs · 14 blocks) · **promotion + pricing** (17 pairs · 21 blocks) · **market research + measuring success** (4 pairs · 9 blocks) · **job design, motivation and contracts** (9 pairs · 14 blocks). **That was 55 of the 76 blocks — 72% of the tier — and every one of the four largest decision types in the qualification is carried in full.**

> ✅ **THE 9-MARK TIER IS CLOSED.** All **76 blocks** are carried by entries **175–227** — verified by `layer_c_9mark_coverage.py`, which prints **76 planned / 76 covered / 0 remaining**. **It was 53 entries for 76 blocks across 58 distinct option pairs**, so this tier compresses far less than the other two **(3-mark 152 → 97 · 6-mark 114 → 74 · 9-mark 76 → 58)** — because **the option pair genuinely varies.** **What repeats is the decision type**, and all fifteen are now closed: sources of finance · promotion · pricing · market research · success measures · job design · motivation · contracts · training · production · operations · recruitment · communication · place · product · structure.

> ✅ **THE 12-MARK TIER IS CLOSED.** All **38 blocks** are carried by entries **228–252** — verified by `layer_c_12mark_coverage.py`, which prints **38 planned / 38 covered / 0 remaining** and separates *planned* from *covered by a written entry* so that a claim made in advance can never masquerade as an answer. **It was 25 entries for 38 blocks, across 22 distinct topics** — a much smaller compression gain than the other tiers, because **the 12-mark stem usually names one topic and one business, and Pearson does not repeat them.** Three topics do carry two or three papers each (**quality → competitive advantage**, **location**, **the market**), and those entries hold a per-paper comparison table rather than three separate essays.
>
> **Entry 228 is the scaffold for the whole tier** — five command forms, one four-way AO split (3 · 3 · 3 · 3), and the **four official AO4 routes**: *(1) the drawback of the same thing (2) a more important factor (3) the named condition (4) argue against the premise.*

**Progress against those 380 blocks:**

| Tier | Blocks | Written | Remaining |
|---|---|---|---|
| 3-mark Explain | 152 | ✅ **152** | 0 |
| **6-mark Analyse** | **114** | ✅ **114** | 0 |
| **9-mark Justify** | **76** | ✅ **76** | **0** |
| **12-mark Evaluate** | **38** | ✅ **38** | **0** |
| **TOTAL** | **380** | ✅ **380** | **0** |

> ## ✅ LAYER C IS COMPLETE — 380 OF 380 BLOCKS
> **All four tiers are closed, each verified by its own machine-run coverage script.** Nothing in the bank is carried by hand any more: **252 entries** cover **380 governed blocks** across **38 papers**, and every script also checks the other direction, so a dangling entry reference fails loudly.
>
> **Compression, tier by tier — the whole reason this file is organised by topic and not by question:**
>
> | Tier | Blocks | Entries | How it compresses |
> |---|---|---|---|
> | 3-mark Explain | 152 | **97** | the topic repeats constantly — the same topic answers several papers |
> | 6-mark Analyse | 114 | **74** | 40% of the tier repeats a topic already answered |
> | 9-mark Justify | 76 | **53** | **the option pair** is the unit — 58 distinct pairs, and the decision type repeats even when the pair does not |
> | 12-mark Evaluate | 38 | **25** | the **topic** is the unit again — 22 topics, three of them on two or three papers |
> | **Total** | **380** | **252** | **one entry per topic, never one entry per question** |
>
> **Reproduce all four with:** `layer_c_coverage.py` · `layer_c_6mark_coverage.py` · `layer_c_9mark_coverage.py` · `layer_c_12mark_coverage.py` (run from the folder above; each accepts `--audit`).

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
| **5g** | **6-mark Analyse — May–June 2025, all four papers** | ✅ **8 entries (149–156)** |
| **5h** | **6-mark Analyse — May 2023, all four papers** | ✅ **6 entries (157–162)** |
| **5i** | **6-mark Analyse — the four November papers** | ✅ **12 entries (163–174)** |
| **6** | **6-MARK TIER — CLOSED at 114/114 blocks** | ✅ **done** |
| **7a** | **9-mark Justify — the universal scaffold + the sources-of-finance cluster** | ✅ **13 entries (175–187)** |
| **7b** | **9-mark Justify — promotion (12 pairs) + pricing (9 pairs)** | ✅ **17 entries (188–204)** |
| **7c** | **9-mark Justify — market research + measuring success** | ✅ **4 entries (205–208)** |
| **7d** | **9-mark Justify — job design, motivation, contracts** | ✅ **9 entries (209–217)** |
| **7e** | **9-mark Justify — the final 21 blocks** | ✅ **10 entries (218–227)** |
| **7 ✓** | **9-MARK TIER — CLOSED at 76/76 blocks** | ✅ **done** |
| **8a** | **12-mark Evaluate — the universal scaffold · quality/competitive advantage · TQM · location · research** | ✅ **6 entries (228–233)** |
| **8b** | **12-mark Evaluate — marketing, promotion, changing markets, competitive advantage, success measures, objectives, PR, market orientation** | ✅ **9 entries (234–242)** |
| **8c** | **12-mark Evaluate — the ten singleton topics** | ✅ **10 entries (243–252)** |
| **8 ✓** | **12-MARK TIER — CLOSED at 38/38 blocks. LAYER C COMPLETE — 380/380.** | ✅ **done** |

> ### 📐 THE FILE IS NOW IN STRICT NUMERICAL ORDER — `## 1.` to `## 252.`
> It was not, until this batch closed. Batches 7b–7e were **inserted before `## 196.`**, which stacked the tail as `…195 → 218–227 → 205–217 → 196–204`, and every later append landed at the end. **All entries are present and none were ever duplicated** (checked every time), but the physical order no longer matched the numbering, so `entries[-1]` was **not** the highest entry. **It has now been re-ordered in one move and re-verified: document order is strictly 1 → 252, no gaps, no duplicates, fences balanced.** **Lesson, kept: insert at the END of the file, never "before entry N" — and verify with `min`/`max`, never with `entries[-1]`.**

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

**Asked:** *"Explain one disadvantage of having a hierarchical organisational structure."* — May/June 2024 P1R

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

**Asked:** *"Explain one advantage of using a venture capitalist."* — May/June 2024 P1R · *"Explain one disadvantage for an entrepreneur of using venture capital to start their business."* — June 2026 P2R

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
**Also asked:** *"Analyse the usefulness to TBTS of the acid test ratio."* — June 2022 P1 4(b) · *"Analyse the usefulness of the gross profit margin to PPS."* — June 2024 P1 1(g)

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
**Also asked:** *"Analyse how Kraft Heinz could benefit from reducing its waste."* — Nov 2023 P2 3(d) · *"Analyse how [Kaizen] could affect **its** business."* — **Nov 2023 P1, 4(b)**, **AWG**, where the business runs Kaizen **in its own clothing workshop** rather than asking a supplier to — the same chains apply, and the AO anchors are the workshop staff's.

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

⭐ **WHEN THE BUSINESS RUNS KAIZEN ITSELF — AWG (Nov 2023 P1 4(b)).** The question there is *"Analyse how this could affect **its** business"*, and the scheme's own anchors are these: **employees in the clothing workshop will be able to discuss different manufacturing techniques and designs for the jumpers**, and **"a major advantage of Kaizen is efficiency" — it may improve the quality of children's clothing** (AO2). The chains then run to **innovative ideas that help AWG stand out from other competitors selling clothing**, and **attracting more customers who are seeking sustainable and long-lasting items of clothing** (AO3). **Note where the two cases differ, because the examiners do: Yellow is told what its suppliers should do; AWG is told what its own workshop will do. Same mechanism, different actor — and the actor is what the mark scheme marks.**

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
**Also asked:** *"Analyse the importance of cash to PPS."* — June 2024 P1 4(b) · *"Analyse the importance of cash to the success of Ocean Vibes."* — Nov 2025 P1 4(b)

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
**Also asked:** *"Analyse the importance to Kumaran, the owner of Café Pinch, of having motivated employees."* — June 2024 P1R 1(g) · *"Analyse the importance to Aude Anglaret of motivating her employees."* — May 2023 P1R 1(g) · *"Analyse the benefits for Premier Inn of motivating its employees."* — Nov 2024 P2 3(d)

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

**Asked:** *"Analyse the importance of reliable market research to obtain this information."* — **May–June 2024 P1, 3(d)**

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

**Asked:** *"Analyse two factors Café Pinch might consider when measuring its success."* — **May–June 2024 P1R, 3(d)**
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

**Asked:** *"Analyse how Café Pinch could use market segmentation to target its customers."* — **May–June 2024 P1R, 4(b)**

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

# BATCH 5g — 6-MARK ANALYSE, PART 7

**8 new entries covering June 2025's twelve blocks.** Four were topics already banked:

| Block | Topic | Where it now lives |
|---|---|---|
| 71 P1 3(d) *benefits of recruiting externally (Four Fitness)* | external recruitment | **entry 150** — same topic as block 68, one entry answers both |
| 73 P2R 1(g) *benefits of being a global business (Rabanne)* | multinational / global | **entry 108** *(5th appearance)* |
| 75 P2R 4(b) *benefits of robotics (Rabanne)* | robotics | **entry 142** *(3rd appearance)* |
| 78 P2 4(b) *why interview candidates (Starbucks)* | interviewing | **entry 127** *(3rd appearance)* |

> ### ⭐ THE ONE QUESTION IN JUNE 2025 THAT ASKS FOR BOTH SIDES
> Block **77** carries a weight the others do not, and the reason is a lesson the examiners repeat in every report. Of the twelve June 2025 six-mark questions, **eleven ask for a one-directional analysis** — *benefits*, *concerns*, *effects*, *importance*. **Block 77 asks why Starbucks promotes its own employees**, which the scheme's own bullets state as **loyalty and reduced advertising time and money**. The temptation to fill it with the *disadvantages* of internal promotion — no fresh ideas, resentment — is strong and would be **answering the wrong question**. **Match the direction the stem asks for. It is set deliberately.**

---

## 149. NEW TECHNOLOGY — the concerns before adopting it

**Asked:** *"Analyse the concerns CCT may have of introducing this app for its customers."* — **June 2025 P1R, 1(g)**

**The AO2 anchors:** customers **might be reluctant to download the app for a one-off biking experience**; and it **can be costly for CCT to introduce an app where customers can book the bicycles**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> CCT's customers are **people on holiday**, and that is what makes the app a risk rather than an obvious improvement. **A tourist hiring a bike for a day or two has no reason to download an app they will use once** — they will never be back to use it again, so **the app is work for the customer and a permanent cost for CCT**. **Most phones already hold too many apps, which makes "another one" easy to refuse**, and a customer who refuses it **cannot book at all if the app is the only way in**. **The second concern is that CCT is a bike tour business, not a software business.** CCT **may not have the experience to build an app, so it must pay a designer to create it and someone else to maintain it** — a cost that is **paid whether or not customers use it**, and which continues after the season ends. **The measurable end is that the app's fixed cost lands on a business whose customers are temporary**, so the revenue it brings must clear the development and maintenance bills before it makes anything at all.

| Step | The move |
|---|---|
| **1. Point** | The customers are **on holiday** — a one-off relationship |
| **2. Strand A** | No reason to download an app used once → **customers may refuse it entirely** |
| **3. Strand B** | CCT is **not a software business** → must pay to build and maintain it |
| **4. Measurable end** | **A permanent cost against temporary custom** |

**Second acceptable chain:** an app that fails **damages more than the app** — customers who could not book **leave with a poor impression of CCT itself** → the damage spreads to the tours, which are the actual business.

> ⭐ **The stem says "concerns", not "disadvantages of an app".** The concern in the mark scheme is **about the customers** — their reluctance, their holiday habits. **A generic list of technology drawbacks would miss the AO2 entirely.**

---

## 150. RECRUITING EXTERNALLY — the effects on the business

**Asked:** *"Analyse the possible effects on CCT of recruiting externally."* — **June 2025 P1R, 3(d)**
**Also asked:** *"Analyse the benefits to Four Fitness of recruiting externally."* — **June 2025 P1, 3(d)**

> **Two of June 2025's six 3(d) questions are the same question on two different papers.** The scheme's own bullets for both contain **the advantage and the drawback**, which tells you what shape the answer should take.

**The AO2 anchors (CCT):** external recruitment **provides a larger pool of potential candidates who may have specialised knowledge**; and **it may be expensive and time-consuming to advertise, shortlist and interview**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Recruiting externally means **looking outside the business**, and the first effect is on **who is available**. A candidate from outside brings **specialised knowledge CCT does not have — for example a marketing specialist who understands team-building activities** — which is the whole reason to look outside rather than promote from within. **That specialist can give CCT new ideas and a competitive edge in the bicycle tour market**, because they have seen how other businesses in the field do it. **The second effect is what the process costs.** Advertising, shortlisting and interviewing **take both money and time**, and for a business the size of CCT, **that time comes out of work on the current services and the current staff** — so the business is **weaker for a period in order to be stronger afterwards**. **The measurable end is the gamble:** CCT buys expertise it does not have, **and pays for it with money and management attention it could have spent developing what it already sells.**

| Step | The move |
|---|---|
| **1. Point** | External recruitment widens **who is available** |
| **2. Strand A** | Specialist skills → **new ideas and a competitive edge** |
| **3. Strand B** | The process costs **money and management time** |
| **4. Measurable end** | **Expertise gained, but current services go under-served meanwhile** |

**Second acceptable chain (Four Fitness):** the new manager comes with **ideas from outside the business** → but existing staff may feel **overlooked for the role** → **demotivation and the risk of losing them** is the price of bringing someone in above them.

> ⚠️ **"Effects" means both directions; "benefits" means the good one.** The scheme's bullets carry the cost in **both** questions, so include it — **but when the stem says *benefits*, lead with the benefit and let the drawback close the answer rather than open it.**

---

## 151. TECHNOLOGY FOR COMMUNICATION — choosing the channel

**Asked:** *"Analyse other forms of technology CCT can use to communicate its services."* — **June 2025 P1R, 4(b)**

**The AO2 anchors:** **social media can be used to target bicycle enthusiasts**; and **e-newsletters can keep previous customers up-to-date** on new bicycle services.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> The right technology is the one that **reaches the customers a business already has a relationship with, as well as the ones it does not.** **Social media reaches bicycle enthusiasts by interest** — CCT can put the tours in front of people whose profiles say they ride, **so the spend buys people who might actually book rather than passers-by**. **The channel that matters more to CCT, though, is the e-newsletter.** It goes **only to people who have already been on a tour**, so it costs almost nothing to send and **it reaches the warmest audience the business has** — people who know the tours work. **Used together the two do different jobs.** Social media **targets and personalises** by what a customer has searched for, so the message is relevant; the newsletter **brings back the customers who have already paid once**, encouraging them to **book another tour or recommend CCT to friends and family**. **The measurable end is repeat custom:** for a seasonal tour business, **the cheapest sale it will ever make is to a customer who has already been**.

| Step | The move |
|---|---|
| **1. Point** | Different channels reach **different audiences** — match the tool to the group |
| **2. Strand A** | Social media → **targets bicycle enthusiasts, and personalises the message** |
| **3. Strand B** | E-newsletter → **reaches past customers at almost no cost** |
| **4. Measurable end** | **Repeat bookings and recommendations** from the warmest audience |

**Second acceptable chain:** a **live booking and availability system on the website** → customers book without waiting for an email reply → **CCT captures the booking that a slower response would have lost** to a competitor.

> ⭐ **Do not answer "technology" with a list.** *Website, social media, e-newsletter, app, text, online chat* — **each reaches a different audience at a different cost, and the mark is in that match.** A list of five with no chains scores in the bottom level, and **bullets disqualify the top levels outright.**

---

## 152. SPAN OF CONTROL — analysing whether it works

**Asked:** *"Analyse the effectiveness of the wide span of control used by Gianni Polvani."* — **June 2025 P1, 1(g)**

> **This is the question the bank holds a verified 6/6 script for** — the candidate in the June 2025 report wrote **one point with developed strands, with application throughout**, and the examiner's comment is quoted at the head of this batch series. Read entry **70's companion** in `02_Verified_Exemplars.md` before writing your own.

**The AO2 anchors:** Gianni **will be able to empower his employees directly within the gym as there are no layers between him and them**; and **14 employees may be too many for Gianni to manage himself, especially as he has two gyms to run**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> A wide span of control means **Gianni manages a lot of people directly** — in his case fourteen staff across two gyms, with **no layers of management between him and them**. **That structure has a real advantage: because nothing sits between the owner and the employees, he can empower them directly**, and **decisions are made faster when they do not have to travel up and down a chain**. Staff who are trusted to decide **take ownership of their own work, which motivates them to bring new ideas into the gym** — ideas that someone three layers removed would never hear. **The problem is the arithmetic.** **Fourteen people is more than one manager can supervise closely**, and **Gianni also has two gyms to run**, so at any moment he is in the wrong one for half his staff. **The measurable end is where the structure fails: supervision thins out**, and **employees who are under-supervised become less productive** — so the same design that creates the motivation is also what removes the attention that keeps it on course.

| Step | The move |
|---|---|
| **1. Point** | Wide span = **many staff, no layers between owner and them** |
| **2. Strand A** | Direct empowerment → **faster decisions → motivation and new ideas** |
| **3. Strand B** | 14 staff and 2 gyms → **he cannot supervise them all** |
| **4. Measurable end** | **Reduced supervision → lower productivity** |

**Second acceptable chain:** fewer managers **saves salary cost**, because Gianni is not paying middle managers to relay instructions → **the gyms run at a lower overhead** → but **he becomes the bottleneck** for any decision only he can make.

> ⭐ **"Effectiveness" questions are the only ones at this tariff that want a verdict.** You do not have to choose between good and bad, but you must **analyse both halves and let the final line say where the balance falls for this business.**

---

## 153. HEALTH AND SAFETY — why a business complies

**Asked:** *"Analyse why Four Fitness complies with health and safety laws."* — **June 2025 P1, 4(b)**

**The AO2 anchors:** it **regularly inspects gym equipment to make sure it is safe** and keeps **safety signs on the treadmills clear**; and Gianni **could train all his instructors in relevant health and safety procedures**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> A gym is **a building full of heavy moving equipment and untrained members**, so Four Fitness cannot rely on people to be careful — **the risk has to be designed out**. **Regular inspection of the equipment and clear signage on the treadmills** is how it does that, and **the reason is not legal duty alone: a customer injured on a machine is a customer who will not renew, and who may tell others why**. **The second half of the answer is on the staff side.** Training **all the instructors in health and safety procedures** means that **when an injury does happen, the person standing next to it knows what to do and gives first aid properly** — which is the difference between **an incident and a worse one**. **The measurable end is protection from two directions at once:** fewer customers injured means **fewer complaints, less risk of being sued, and no drop in customer numbers**; and staff who know what to do in an emergency **work with more confidence**, which is its own reason to comply.

| Step | The move |
|---|---|
| **1. Point** | A gym's risk **has to be designed out** — equipment and signage |
| **2. Strand A** | An injured customer **does not renew — and tells others why** |
| **3. Strand B** | Trained instructors → **an incident does not become a worse one** |
| **4. Measurable end** | **Fewer claims, protected customer numbers**, confident staff |

**Second acceptable chain:** complying is **cheaper than not complying** — failing an inspection can bring **a fine, a closure order or a refusal of insurance**, any of which stops the gym trading entirely.

> ⚠️ **Do not answer with the law.** The question asks **why the business complies**, which means what the business gets. *"Because it is illegal not to"* is a one-line answer scoring nothing. **The mark is in the consequences — injuries, claims, reputation, insurance, confidence.**

---

## 154. USING RESOURCES EFFECTIVELY — the importance of it

**Asked:** *"Analyse the importance for Rabanne of using its resources effectively."* — **June 2025 P2R, 3(d)**
**Also asked:** *"Analyse why Kraft Heinz could benefit from reducing its waste."* — Nov 2023 P2 3(d)

**The AO2 anchors:** Rabanne uses resources effectively by **not wasting packaging material** for its handbags and accessories; and by **developing higher quality packaging** for its fragrances.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Resources used effectively are **resources that do not have to be bought twice** — so the effect of avoiding waste is **an immediate cost saving**, because **packaging material that is used well is material that does not have to be replaced**. **For a luxury brand the saving is not the whole story, and the second half of the answer is the one that matters most.** **Higher-quality packaging** does two things at once: it **reduces the number of damaged bottles and accessories that must be replaced, which cuts cost**, and it **makes the product look like what it is** — a prestige item — which is **why a customer is willing to pay the price at all**. **The measurable end runs in three directions:** lower costs, fewer replacements, and a stronger brand image — **and using resources effectively turns out to be as much about reputation as about money.** Wasting less **also makes the business more environmentally friendly**, which matters to the customers luxury brands sell to.

| Step | The move |
|---|---|
| **1. Point** | No waste = **materials not bought twice → direct cost saving** |
| **2. Strand A** | Better packaging → **fewer damaged bottles needing replacement** |
| **3. Strand B** | Presentation **is** the luxury product → **the price the brand charges** |
| **4. Measurable end** | **Lower cost, stronger image, greener reputation** |

**Second acceptable chain:** using resources effectively includes **labour and machine time** — shorter changeovers and less rework **release capacity without buying another machine** → **output rises with no rise in fixed cost**.

> ⭐ **"Resources" is wider than "materials":** people, machines, time, money and materials. **The case decides which one to reach for** — and Rabanne's case points at packaging, which is why the scheme's bullets are about packaging and not about staff.

---

## 155. BATCH PRODUCTION — the benefits

**Asked:** *"Analyse the benefits for Starbucks of using batch production."* — **June 2025 P2, 1(g)**

**The AO2 anchors:** batch production means Starbucks **can produce cakes at a lower cost per unit**; and it **maximises the use of kitchen equipment and reduces waste of ingredients** for sandwiches.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Batch production makes **a set quantity of one item, then switches to another** — and for a food business that shape fits the job exactly. **Making cakes in batches lowers the cost of each one, because the equipment is set up once and used to capacity** before it is changed, **so the kitchen and the ovens are never sitting idle between jobs**. **The second gain is on ingredients.** Producing in planned quantities means **less waste — the sandwich fillings are prepared for a known number, not guessed at** — and **ingredient waste is money that has been bought and then thrown away**. **The measurable end is the one that matters most to Starbucks: uniformity.** Because each batch is made to the same recipe in the same way, **the cakes and sandwiches taste the same in every location**, and **a customer who buys the same item in a different shop is not disappointed** — which is what makes a chain a chain rather than a collection of shops.

| Step | The move |
|---|---|
| **1. Point** | Batch = **one item at a time, in a set quantity** |
| **2. Strand A** | Set-up amortised over the batch → **lower cost per unit** |
| **3. Strand B** | Planned quantities → **less ingredient waste** |
| **4. Measurable end** | **Identical products everywhere** — the basis of a chain |

**Second acceptable chain:** batches can be **timed to demand** — cakes made in the morning for the lunch rush → **fresher stock and less unsold at the end of the day** than a single huge production run.

> ⚠️ **Batch is neither job nor flow.** **Job** = one bespoke item (a wedding cake). **Batch** = a set quantity, then switch. **Flow** = continuous, one standard product. **Starbucks makes cakes in batches; it does not make one bespoke cake, and it does not run a continuous line.** Getting the method wrong makes every chain in your answer wrong.

---

## 156. PROMOTING FROM WITHIN — why a business does it

**Asked:** *"Analyse why Starbucks wants to promote its existing employees."* — **June 2025 P2, 3(d)**

**The AO2 anchors:** promoting its own employee to **Assistant Manager means they remain loyal to Starbucks**; and it **reduces the cost of advertising for new employees** who have experience of coffee shops.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Filling a vacancy from inside means **the person appointed already knows the business**, so the first benefit is **what Starbucks does not have to buy: the advertising, the shortlisting and the induction that a new manager from outside would need**. **The second is what the promotion does to everyone else.** An employee who is **promoted to Assistant Manager** has a career in front of them, and **that is what loyalty is built on — the visible proof that working well is rewarded here**. **It reaches past the individual as well.** **Every other member of staff watches how the promotion was decided**, so promoting from within **tells the whole team that effort is noticed**, and demotivation and resignations come down with it. **The measurable end is on the payroll and the training budget:** Starbucks **fills a management post without recruiting**, **keeps a manager who is already familiar with how it works and what it aims for**, and **saves the time and money of training someone who has never made a Starbucks coffee.**

| Step | The move |
|---|---|
| **1. Point** | Inside appointment → **no advertising, shortlisting or induction to pay for** |
| **2. Strand A** | A visible career → **loyalty** |
| **3. Strand B** | The rest of the team sees it → **motivation across the shop** |
| **4. Measurable end** | **A manager who already knows the aims of the business**, at no recruitment cost |

**Second acceptable chain:** the promoted employee is **already familiar with how the business works**, so **they become effective in the role sooner** than an outsider → **the shop is not weakened during a management change**.

> ⚠️ **The scheme's bullets here are `loyalty` and `reduced cost of advertising` — both advantages.** An answer built on the *drawbacks* of internal promotion — no new ideas from outside, possible resentment among those not chosen — **would be answering the opposite question.** **Note that entry 150 (recruiting externally) is its mirror image: the same business decision, and the exam has asked about both sides in the same session.**

---

# BATCH 5h — 6-MARK ANALYSE, PART 8

**6 new entries covering May 2023's twelve blocks.** Six were already banked — and this paper shows the repeats at their densest:

| Block | Topic | Where it now lives |
|---|---|---|
| 79 P1R 1(g) *motivating her employees (Aude Anglaret)* | motivating employees | **entry 139** *(5th appearance)* |
| 81 P1R 4(b) *factors when measuring success (Aude Rose)* | measuring success | **entry 144** |
| 82 P1 1(g) *importance of branding (Irsi Chocolatier)* | branding | **entry 125** |
| 83 P1 3(d) *limitations of break-even charts (Irsi)* | break-even | **entry 117** *(5th appearance)* |
| 85 P2R 1(g) *disadvantages of social media (M&M)* | social media | **entry 129** |
| 90 P2 4(b) *SoCI to assess performance (IKEA)* | Statement of Comprehensive Income | **entry 114** *(4th appearance)* |

> ### ⭐ FIVE OF MAY 2023'S TWELVE WERE TOPICS ALREADY ANSWERED BY A PAPER UP TO FIVE YEARS OLDER
> **Motivating employees** has now appeared **five times** — TBTS, Café Pinch, Aude Rose, Premier Inn and Aude Anglaret — and **break-even five times**. Nothing about the chain changes between them. **What changes is the AO2**, and that is the whole of the skill: the examiners are not testing whether you know what motivation is, they are testing whether you can attach it to **florists producing bunches of flowers**, **waiters in a Berlin café**, or **gym instructors in Italy**.

---

## 157. RETAINED PROFITS — the impact of using them

**Asked:** *"Analyse the impact on Aude Rose of using its retained profits for this proposed development."* — **May 2023 P1R, 3(d)**

**The AO2 anchors:** by using retained profit **Aude Rose can buy the flowers straight away**; and **retained profit can only be used to buy a wider range of flowers if it exists**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Retained profit is **money the business has already earned and not yet spent** — so using it means **the flowers can be bought straight away, with no application to a bank and no waiting for approval**. **That speed matters in a flower business, where stock is perishable and a range has to be in the shop before customers ask for it.** **The second effect is what the money does not cost.** Because retained profit **does not have to be repaid, any profit the new range makes goes back into the flower shop** rather than out to a lender in interest — so **the development pays for itself faster than a loan would**. **But the scheme's second bullet is the sting, and it is where an "impact" answer earns its top level: the money only exists if the business has earned it.** **Aude Rose can only widen its range if there is enough retained profit to do it** — and if there is not, **the business must wait to accumulate more, which means the opportunity passes while it saves.**

| Step | The move |
|---|---|
| **1. Point** | Retained profit is **already earned and in hand** → buy immediately |
| **2. Strand A** | No loan → **no interest, no repayments** → profit returns to the business |
| **3. Strand B** | **The limit: the money must exist** — it is capped by past profit |
| **4. Measurable end** | Range widened now, **or the opportunity missed while saving for it** |

**Second acceptable chain:** spending the retained profit leaves **less of a cushion for a bad month** → if sales fall, the business has **less to fall back on** → it may have to borrow later, at the worst possible time.

> ⚠️ **Internal sources of finance are the only ones whose limitation is built into the source itself.** A loan is capped by what a bank will lend; **retained profit is capped by what the business has made.** On an *impact* question, **that limitation is half the answer** — and it is the half most candidates leave out.

---

## 158. PLACE — the importance of it in the marketing mix

**Asked:** *"Analyse the importance of place to Irsi Chocolatier."* — **May 2023 P1, 4(b)**
**Also asked:** *"Analyse the importance of location for TADS."* — May–June 2020 P1 1(g) · *"Analyse the factors that could influence Cadbury when locating a new factory."* — June 2022 P2R 1(g)

> **Place in the marketing mix is not the same as location for a factory.** For a retailer, *place* is **how the customer gets the product** — the shop, the website, the delivery van. **A factory location question is about cost; a place question is about the customer.** Read which one you have.

**The AO2 anchors:** Irsi is **located in a busy area with competitors nearby and wants customers drawn to it over the other chocolate shops**, so it will not want to move; and **as a small business with only 3 employees, it may want to consider its online place** as well as the physical shop.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Place is **the route the product travels to reach the customer**, and for Irsi's shop it does two jobs at once. **The physical shop is a fixed asset with a reputation attached to it: the business has traded from the same location since 1989, and locals and tourists come back to it year after year because that is where the chocolates they remember were bought.** **Moving would throw that away — and with competitors close by in a busy area, the shop has to keep drawing customers past them rather than relying on being found.** **The second half of place is where Irsi is weakest.** With **only three employees**, the business **can serve the customers who walk in and no more**, so **an online shop and its local delivery service let it sell to people who are not in the street** — and **that reach is what keeps a small shop competitive against bigger rivals.** **The measurable end is a wider market from the same three staff:** the shop keeps the regulars, and the website **sells to people the shop will never see.**

| Step | The move |
|---|---|
| **1. Point** | Place = **the route the product takes to the customer** |
| **2. Strand A** | The 1989 shop **is the reputation** → moving loses it |
| **3. Strand B** | Three staff → **online plus local delivery widens reach** |
| **4. Measurable end** | **Same staff, customers beyond the street** |

**Second acceptable chain:** place also decides **which customers can be reached at all** — tourists who plan before they travel **find the website first** → a poor online presence **means they choose a competitor before they ever arrive**.

> ⚠️ **The four Ps are product, price, place and promotion — and place is not promotion.** A website that *sells* is place; a social media post that *tells people about the shop* is promotion. **The scheme's bullets here are about where the customer buys, and mixing the two loses the application mark.**

---

## 159. COMPARING WITH COMPETITORS — why a business benchmarks

**Asked:** *"Analyse why M&M would want to compare its business with other vehicle manufacturers."* — **May 2023 P2R, 3(d)**
**Also asked:** *"Analyse why M&M wants to continue planting trees."* — May 2023 P2R 4(b)

**The AO2 anchors:** M&M can **compare its sales of cars with other businesses such as the Ford Motor Company**; and **if Fiat introduces different models of tractors, M&M may consider changing the design of its own**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> A figure on its own **cannot tell a business whether it is doing well — only a comparison can**. Comparing its car sales with **Ford** tells M&M **whether it is gaining or losing ground**, which is information that its own accounts cannot supply no matter how detailed they are. **The second reason is that competitors show what is coming.** If **Fiat introduces a new model of tractor, M&M learns what customers in the market are being offered**, and **it may decide to change the design of its own tractors** — either to match it or to attack the gap Fiat has left. **The measurable end is the action that follows the comparison.** If M&M's figures are **not as good as Ford's, it can respond — offering discounts or other incentives to customers** — and it can do so **before the gap becomes a loss**, rather than after. **The scheme adds the caution: there is no guarantee that M&M's new tractor will compete with Fiat's** — because a rival's success **cannot simply be copied**.

| Step | The move |
|---|---|
| **1. Point** | A figure is meaningless **without a comparison** |
| **2. Strand A** | Rival sales → **shows whether M&M is gaining or losing ground** |
| **3. Strand B** | Rival products → **shows what customers are being offered** |
| **4. Measurable end** | **A response — discounts, incentives or a redesign — before the loss** |

**Second acceptable chain:** comparing against rivals **tests whether M&M's own costs are competitive** → a manufacturer with higher unit costs **cannot match a rival's price without losing money** → so the comparison **decides whether M&M can compete on price at all**.

> ⭐ **There is a naming trap here and the bank has a rule for it: M&M's own case mixes vehicle manufacturers, and the scheme names FORD for cars and FIAT for tractors.** Use the right name for the right product — **a wrong business name is not application, it is a mistake.**

---

## 160. ENVIRONMENTAL ACTION — why a manufacturer keeps doing it

**Asked:** *"Analyse why M&M wants to continue planting trees."* — **May 2023 P2R, 4(b)**
**Also asked:** *"Analyse why Emirates would want to be more environmentally friendly."* — May–June 2020 P2 3(d) · *"Analyse the importance of environmental factors for Loaf."* — May–June 2020 P1R 1(g)

**The AO2 anchors:** planting trees is **good for M&M's image, its customers and the sale of its cars**; and it **would improve the environment and air quality in countries where M&M has factories**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> A vehicle manufacturer has **a credibility problem that planting trees addresses directly: it pollutes, and everyone knows it**. **Paying for trees is a visible answer to that — it improves the environment and the air quality in the countries where M&M's factories are**, so the benefit is felt **where the business is actually operating rather than somewhere convenient**. **The second reason is what the trees are for commercially.** The scheme's bullets are explicit that this is **good for the image, for the customers and for the sale of the cars** — because **customers who care about the environment are more likely to buy from a company they can see is trying** to reduce the damage it does. **The measurable end is a defence rather than a gain:** M&M **still pollutes when it makes vehicles**, and no amount of tree planting changes that — but **the business can show that it is reducing the damage rather than ignoring it**, which protects it from the customers, and eventually the rules, that would otherwise turn against it.

| Step | The move |
|---|---|
| **1. Point** | A vehicle maker **pollutes, and everyone knows it** |
| **2. Strand A** | Trees planted **where the factories are** → a visible, local improvement |
| **3. Strand B** | Green image → **customers more willing to buy** — the scheme's own link |
| **4. Measurable end** | **Damage reduced and defended against**, not eliminated |

**Second acceptable chain:** planting trees **builds goodwill with the governments and communities of the countries M&M operates in** → the business is **less likely to face tighter regulation or local opposition** to its factories.

> ⚠️ **Never claim the environmental action makes the business clean.** The scheme's own bullet says it plainly: *"even though the manufacture of vehicles and tractors does pollute the atmosphere, M&M are trying to reduce the amount of damage done."* **An answer that overstates the benefit is less accurate than the mark scheme — and accuracy is what is being marked.**

---

## 161. FRANCHISING — the benefits to the FRANCHISOR

**Asked:** *"Analyse the benefits to IKEA of all its stores being franchises."* — **May 2023 P2, 1(g)**

> **Read who benefits.** This is the **franchisor's** question — IKEA selling the right to trade under its name. The 3-mark tier already holds the **franchisee's** advantage (entry 10). **Two questions, same business relationship, opposite sides.**

**The AO2 anchors:** franchises **allow IKEA to sell its flat-pack products throughout the world**; and **all franchisees pay a percentage of their profit to IKEA for the use of its name and furniture**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Franchising lets IKEA **grow without paying for the growth**. The franchisee **funds the store, the staff and the stock**, so IKEA can **have its flat-pack furniture sold all over the world without raising the money to build each shop itself**. **The second benefit is the income that comes back without any of that risk.** **Every franchisee pays a percentage of its profit for the use of the IKEA name and furniture** — so IKEA **earns from stores it does not run, and from regions it has never had to learn**. **The measurable end is scale without capital:** many retail stores selling IKEA furniture **create wealth for the business and revenue from every franchised store**, which **makes IKEA more successful on its own balance sheet than a chain of company-owned shops of the same size could** — because the money that would have been tied up in buildings is free.

| Step | The move |
|---|---|
| **1. Point** | The franchisee **pays for the shop** — IKEA does not |
| **2. Strand A** | Royalty on every franchisee's profit → **income from stores IKEA does not run** |
| **3. Strand B** | Global reach **without IKEA learning each market alone** — locals run it |
| **4. Measurable end** | **Growth without capital tied up in property** |

**Second acceptable chain:** franchisees **know their own local market** better than a head office in Sweden would → sites and ranges **suit local demand** → more of the stores succeed, and **IKEA's royalty income rises with them**.

> ⚠️ **The franchisee's answer is "a tried and tested business, advice and training, lower risk of failure" (entry 10). The franchisor's answer is "growth without capital, and a royalty on someone else's profit."** **They are mirror images — and writing the wrong one wastes the whole question.**

---

## 162. SHORTLISTING — why a business does it before interview

**Asked:** *"Analyse why IKEA shortlists candidates for positions in its factories."* — **May 2023 P2, 3(d)**
**Also asked:** *"Analyse why Jimmy Choo asks all candidates to complete an application form."* — June 2024 P2R 3(d) · *"Analyse how recruitment documents may help Samsung."* — Nov 2025 P2 1(g)

**The AO2 anchors:** shortlisting **saves IKEA time by only calling applicants for interview if they have the experience or qualifications**; and IKEA **will shortlist candidates that match the job description** of a carpenter in its factories.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> A vacancy at IKEA can draw **far more applications than it can interview**, so the shortlist exists to **cut the pile down to the people worth spending time on**. **The test applied is the job description** — for a factory carpenter that means **the experience or the qualifications to work with flat-pack furniture** — and **anyone who does not match it is not called in**. **That is where the saving is realised.** **Only the matching applicants are interviewed, so the time IKEA's Human Resources team spends filling one factory post falls sharply** — and their time is a cost the business pays whether it is recruiting or not. **The measurable end is a better use of management time, and a better appointment.** Shortlisting also **checks that what the applicant wrote on the form actually matches the job they applied for** — which is how an application **that reads well but does not fit the role** is caught **at the desk rather than in the interview room**.

| Step | The move |
|---|---|
| **1. Point** | More applicants than can be interviewed → **the pile must be cut** |
| **2. Strand A** | The **job description is the test** — experience and qualifications |
| **3. Strand B** | Only matching candidates interviewed → **HR time saved** |
| **4. Measurable end** | **Faster, cheaper appointment — and the right one** |

**Second acceptable chain:** shortlisting **makes the interviews comparable**, because every candidate called in has already been tested against the same requirements → the decision is **made on fit for the role rather than on who interviewed well**.

> ⚠️ **Shortlisting is a *filter*, not a *search*.** It happens **after** the advert and the applications, and **before** the interview. **The application form collects the information (entry 146); shortlisting is what is done with it.** Two different questions — the exam has asked both.

---

# BATCH 5i — 6-MARK ANALYSE, PART 9 — **THE TIER IS COMPLETE**

**12 new entries covering all 24 remaining blocks — the November papers of 2021, 2023, 2024 and 2025.** Eleven of the 24 were topics already banked:

| Block | Topic | Where it now lives |
|---|---|---|
| 91 P1 1(g) *effect of a DECREASE in interest rates (Artify)* | interest rates | **entry 135** *(4th appearance)* |
| 92 P1 3(d) *gross profit margin (Artify)* | profitability ratios | **entry 118** *(4th appearance)* |
| 94 P2 1(g) *locating factories near labour sources (Huawei)* | location | **entry 122** |
| 99 P1 4(b) *how Kaizen could affect the business (AWG)* | Kaizen | **entry 119** *(2nd appearance)* |
| 101 P2 3(d) *benefit of reducing waste (Kraft Heinz)* | resource efficiency | **entry 154** |
| 102 P2 4(b) *benefits to countries where it is located* | host-economy benefit | **entry 112** *(3rd appearance)* |
| 105 P1 4(b) *becoming a multinational (Saha)* | multinational | **entry 108** *(6th appearance)* |
| 106 P2 1(g) *benefits for India (Premier Inn's plans)* | host-economy benefit | **entry 112** |
| 107 P2 3(d) *motivating employees (Premier Inn)* | motivating employees | **entry 139** *(6th appearance)* |
| 111 P1 4(b) *importance of cash (Ocean Vibes)* | cash | **entry 123** *(4th appearance)* |
| 112 P2 1(g) *recruitment documents to hire the best (Samsung)* | recruitment documents | **entry 146** *(2nd appearance)* |

---

## 163. TRAINING — the advantages of on-the-job training

**Asked:** *"Analyse the benefits for Artify Studio of on-the-job training for new employees."* — **Nov 2021 P1, 4(b)**
**Also asked:** *"Analyse the advantages to Ocean Vibes of using on-the-job training for new workers."* — Nov 2025 P1, 3(d) · *"Analyse why Huawei offers its new employees in the design department **off-the-job** training."* — Nov 2021 P2, 3(d) *(see entry 164 — the opposite method)*

**The AO2 anchors (Artify):** Artify can **use the existing employees at its Kampong Glam studio to train the new employees**; and this **gives Tay Hui Jae the chance to see if the new employees are skilled enough**.

**The AO2 anchors (Ocean Vibes):** new tour guides **learn from existing guides on the boats how to give an enjoyable tour**; and it is **less expensive than learning from an external business**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> On-the-job training means **the new worker learns by doing the real job, beside someone who already does it well**. **For Ocean Vibes that is the only place the job can be learned: a tour guide's skill is pointing out dolphins and birds to passengers on a moving boat**, and no classroom reproduces that. **The second benefit is what it costs — and here the scheme is specific: it is less expensive than sending people to an external business.** **Ocean Vibes pays its own existing guides to train rather than paying a college's fees**, and the trainee is **working on the boats while learning** rather than being away. **The measurable end is twofold.** **Tay Hui Jae can see for herself whether the new employees are skilled enough to work in the studio** — the owner watches the actual work being done, which no certificate proves. And at Ocean Vibes, **the guides reach the standard needed to give excellent customer service, which improves profitability because the training cost stayed low.**

| Step | The move |
|---|---|
| **1. Point** | Learning **by doing the real job**, beside someone who does it |
| **2. Strand A** | **No external fees** — the business's own staff deliver it |
| **3. Strand B** | The trainee **works while learning**, and the owner **sees the real work** |
| **4. Measurable end** | **Lower training cost + verified competence** |

**Second acceptable chain:** the trainee learns **the way this particular business does it** → consistency across staff → **customers get the same standard every time**, which is what builds a reputation.

> ⚠️ **On-the-job vs off-the-job is a named content gap in the reports, and the exam asks both directions.** On-the-job = **in the workplace, doing the real job, usually cheaper, learning the employer's own methods**. Off-the-job = **away from work, at a college or training centre, expert tutors, but the employee is absent and it costs fees.** **Entry 164 is its mirror. Do not blend them.**

---

## 164. TRAINING — why a business chooses off-the-job training

**Asked:** *"Analyse why Huawei offers its new employees in the design department off-the-job training."* — **Nov 2021 P2, 3(d)**

**The AO2 anchors:** this **involves new employees being trained outside Huawei at an external college by tutors and experts in modern technology**; and **employees can learn at their own pace the detail and requirements of producing smartphones and tablets**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Off-the-job training sends the employee **away from the workplace to learn from people whose job is teaching**, and Huawei's design department is exactly the case that needs it. **The technology inside smartphones and tablets changes faster than any single business can keep ahead of, so the expertise has to be bought in from tutors and specialists** — Huawei's own designers can teach how it works today, not what is coming next. **The second benefit is the freedom the classroom gives the learner.** Away from the production line, **an employee can learn at their own pace and get to grips with the detail**, instead of picking up whatever they can between tasks. **The measurable end is on both the trainee and the team they leave behind.** Because the new employee is not on the shop floor, **Huawei's existing staff can concentrate on their own work and do not have to supervise or train anyone** — and the trainee **does not have to worry about making mistakes that would cost Huawei money while they are still learning.**

| Step | The move |
|---|---|
| **1. Point** | Away from the workplace, taught by **people whose job is teaching** |
| **2. Strand A** | Specialist tutors know **the newest technology**, not just Huawei's current method |
| **3. Strand B** | No pressure of production → **learn at their own pace, mistakes cost nothing** |
| **4. Measurable end** | **Existing staff undisturbed + trainee fully competent** |

**Second acceptable chain:** off-the-job training **often leads to a recognised qualification** → the employee gains something that is theirs, which **motivates them to stay** and makes Huawei more attractive to future recruits.

> ⚠️ **The scheme's third bullet is the one candidates miss: it is not just about the trainee.** *"Huawei's present employees concentrate on their work, and do not have to supervise or train new employees"* — **the productivity of the existing team is protected.** That is a cost saving, and it earns a mark.

---

## 165. QUALITY CONTROL — why a manufacturer protects quality

**Asked:** *"Analyse why Huawei would want good quality control when producing its smartphones."* — **Nov 2021 P2, 4(b)**
**Also asked:** *"Analyse the importance of making sure guests have a quality service (Premier Inn)."* — Nov 2024 P2, 4(b)
**Related:** entry **119 (Kaizen)** and the **quality** entries in `10_`'s 3-mark tier — *quality control is checking faults out; Kaizen and TQM are about stopping them arising.*

**The AO2 anchors:** if Huawei **gains a reputation for good quality products, more customers are likely to purchase its smartphones**; and **to repair faulty smartphones would be expensive**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Quality control means **checking the product before it reaches the customer and stopping the faulty ones going out**, and for a smartphone maker it guards two things at once. **The first is money.** **Repairing or replacing a faulty phone is expensive, and the cost lands twice** — the customer is sent a working phone, and the faulty one is scrapped, so **the business has paid to make the same product twice**. **The second is the reputation, and it is the larger of the two.** If the standard slips, **customers stop trusting the reliability of Huawei's phones and switch to another brand** — and in a market where a phone is judged over two years of use, **that trust is the whole product**. **The measurable end is what a repair costs in patience:** **customers who have to wait for a phone to be repaired tell other people about the wait as well as the fault**, so a single bad unit **does more damage to the brand than the repair itself costs.**

| Step | The move |
|---|---|
| **1. Point** | Quality control **stops faults reaching the customer** |
| **2. Strand A** | A faulty unit is **paid for twice** — made, then replaced |
| **3. Strand B** | Loss of trust in reliability → **customers switch brand** |
| **4. Measurable end** | **A damaged reputation costs more than the repair** |

**Second acceptable chain (Premier Inn — quality of *service*):** helpful reception staff and the amenities a guest expects **make a guest return** → **repeat bookings raise profit** → and guests **tell friends and family**, which is promotion the hotel did not pay for.

> ⚠️ **"Quality is important" is not an answer.** The scheme gives you **the cost of repair** and **the reputation effect** — **use both, and drive each to something measurable.**

---

## 166. E-COMMERCE — the advantages of selling online

**Asked:** *"Analyse the advantages to AWG of using e-commerce to sell its products."* — **Nov 2023 P1, 1(g)**

**The AO2 anchors:** AWG **sells its shirts online to customers based in other countries**; and **uses a website to advertise its baby clothes to attract new customers**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Selling online **removes the two things that stop a small clothing business from trading abroad: distance and shop cost**. AWG's shirts **reach customers in other countries without AWG ever opening a store there** — and **the scheme's second bullet is the reason that matters financially: selling online is far less expensive than opening stores overseas**, where rent, staff and local taxes all have to be paid before a single shirt is sold. **The second advantage is that the website works as an advertisement as well as a shop.** It **shows the baby clothes to new customers who would never have found the business otherwise**, so **recognition of AWG builds internationally** — and recognition, for a clothing brand, is what turns a browser into a buyer. **The measurable end is sales revenue rising while the fixed costs stay where they are:** AWG sells to more countries **without acquiring more shops**, so each additional sale **contributes far more to profit than an extra sale through a new store would.**

| Step | The move |
|---|---|
| **1. Point** | Distance and shop cost **both disappear** — no overseas stores needed |
| **2. Strand A** | Website advertises as well as sells → **recognition grows internationally** |
| **3. Strand B** | Reach **without the fixed cost** of premises abroad |
| **4. Measurable end** | **More sales revenue at a lower cost per sale** |

**Second acceptable chain:** an online shop **never closes** → AWG sells to customers in other time zones **while its own staff sleep** → **the same stock and staff generate revenue for more hours of the day**.

> ⭐ **E-commerce questions reward the *comparison* with physical retail.** *"You can sell to more people"* is knowledge. **"You can sell abroad without the rent, staff and local taxes of an overseas store"** is the analysis, because it says **what the business does not have to pay for.**

---

## 167. EXCHANGE RATES — the impact of a depreciation

**Asked:** *"Analyse the impact on AWG of a depreciation of the ISK."* — **Nov 2023 P1, 3(d)**

> **This is one of the examiners' named content gaps: "depreciation of currency" appears in the reports as a topic candidates handle poorly.** It is also the only question in the tier where **the same event helps and hurts the same business at once** — which is precisely why it is set.

**The AO2 anchors:** exchange rates **affect the price AWG pays for importing the wool and other materials** it buys to make clothing; and **the cost of the jumpers bought by customers in other countries will be impacted**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> A depreciation means **the krona is worth less against other currencies**, and it cuts both ways for a clothing maker that **imports its materials and exports its finished jumpers**. **On the import side it hurts.** AWG **buys wool and other materials from abroad**, so a weaker krona **raises the price it pays for every metre of fabric** — **an increase in cost that AWG has not caused and cannot avoid** — and, unless it absorbs that, **it may have to raise the price of its own clothing**. **On the export side it helps.** **A weaker krona makes AWG's jumpers cheaper for customers buying in other currencies**, so **overseas demand rises** and AWG can sell more abroad than it could at the old rate. **The measurable end is which effect is larger:** if AWG **imports more than it exports, the depreciation costs it money**; if it sells more than it buys in, **the extra demand outweighs the higher material cost** — and either way **the business is exposed to a rate it does not control.**

| Step | The move |
|---|---|
| **1. Point** | A depreciation **cuts both ways** — cheaper to sell abroad, dearer to buy abroad |
| **2. Strand A** | **Imported wool costs more** → cost rises → price may have to rise |
| **3. Strand B** | **Exports are cheaper abroad** → overseas demand rises |
| **4. Measurable end** | **The net effect depends on whether AWG imports or exports more** |

**Second acceptable chain:** the exposure itself is a risk → AWG may **switch to local suppliers to avoid the exchange rate altogether** → but that may cost more or reduce quality, so **the business trades one risk for another**.

> ⚠️ **Get the direction right first, and say it out loud: a depreciation makes a country's exports CHEAPER and its imports MORE EXPENSIVE.** An answer that reverses this **fails every subsequent step**, and a wrong opening premise is the one error you cannot recover from. **Then apply it to the specific business — what does AWG buy in, and what does it sell out?**

---

## 168. SOCIAL MEDIA AS A RESEARCH TOOL — the benefits

**Asked:** *"Analyse the benefits to Kraft Heinz of using social media to collect market research data."* — **Nov 2023 P2, 1(g)**

> **Note what this is and is not.** The 3-mark tier and entry **129** cover social media as **promotion** and as **a reputational risk**. **This question is about using it to gather data** — a research tool, not an advertising channel. **The scheme's bullets are all about collecting views and analysing them.**

**The AO2 anchors:** social media is **widely used around the world and enables Kraft Heinz to collect global data quickly** about a new variety of tomato sauce; and it can **set up links with a variety of people to collect their views on changes made to Mac & Cheese**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Social media gives Kraft Heinz **a panel of consumers it never had to recruit** — the data comes **from people already talking about food in public, at global scale, and it arrives quickly** rather than after a research agency's timetable. **That speed is worth real money on a new product.** A tomato sauce in test **can be judged by consumers in several countries within days**, which means Kraft Heinz **learns whether to carry on with it or stop it before the tooling and the marketing spend are committed**. **The second advantage is the variety of the sample.** By **setting up links with many different people**, Kraft Heinz hears from **far more kinds of customer than it could interview in person** — and the reaction to a change in **Mac & Cheese** is only useful if it comes from the people who actually buy it. **The measurable end is a cheaper, faster research cycle:** the business can **analyse the views and adjust the product while it is still cheap to change**, instead of discovering the problem after launch.

| Step | The move |
|---|---|
| **1. Point** | A **ready-made global panel** — no recruitment, and fast |
| **2. Strand A** | Test a product with consumers **in days, across countries** |
| **3. Strand B** | A **wide range of customers**, not a small in-person sample |
| **4. Measurable end** | **Adjust or stop the product before the money is committed** |

**Second acceptable chain:** social media research is **far cheaper than commissioning face-to-face interviews or surveys** → the money saved goes into the product rather than into finding out about it → **more research can be done for the same budget**, so fewer decisions are made blind.

> ⚠️ **"Social media" questions come in three flavours and the exam sets all three:** as **promotion** (entry 129's reverse), as a **reputational risk** (entry 129), and as **a research tool** (this entry). **Read the verb and the object — here it is "collect market research data".**

---

## 169. PRIMARY RESEARCH — choosing the right method

**Asked:** *"Analyse two methods of primary research that could be of benefit to Saha when developing its products."* — **Nov 2024 P1, 1(g)**

> **The word "two" is an instruction.** Two methods, each developed — the scheme's two bullets are **interviews with current customers** and **focus groups with customers from restaurants and hotels**.

**The AO2 anchors:** Saha could **interview current customers who use the robots in hospitals** to understand how moving supplies between departments could be improved; and **focus groups could include customers from restaurants and hotels** to discuss potential new features.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Primary research means **finding out from the customers themselves, first-hand**, and Saha's customers know things no desk research can supply. **Interviews with the hospitals already using the robots** are the first method, and their value is **depth on a defined problem**: Saha can ask **exactly how moving supplies between departments could be improved**, and follow up on the answer, because it is talking to **the people who watch the robots work every day**. **The second method, a focus group, does a different job.** Bringing **customers from restaurants and hotels together** puts **users from different settings in one room**, and **the discussion between them is where new features come from** — one customer's complaint prompts another's idea, which **no questionnaire would capture**. **The measurable end is in the product:** the interviews **direct the redesign towards the problem the hospitals actually have**, and the focus group **generates the features that make the next model worth buying** — which is how the research pays for itself in sales rather than in reports.

| Step | The move |
|---|---|
| **1. Method 1** | **Interviews** with existing hospital users → depth on a **known** problem |
| **2. Method 2** | **Focus groups** mixing restaurants and hotels → **new ideas from discussion** |
| **3. What each gives** | Interviews = detail · Focus groups = ideas |
| **4. Measurable end** | **Products designed to real needs → sales** |

**Second acceptable chain:** primary research is **specific to Saha's own product and customers**, unlike published secondary data that covers the whole robotics industry → **the findings can be acted on directly** because they are about *these* robots in *these* hospitals.

> ⚠️ **Primary vs secondary, and the research methods, are named gaps.** **Primary** = collected first-hand for this purpose (interviews, questionnaires, focus groups, observation, trials). **Secondary** = already exists (government data, trade reports, competitor websites, internal records). **Asking customers is primary; reading about the market is secondary.**

---

## 170. BUSINESS FAILURE — the reasons it happens

**Asked:** *"Analyse two possible reasons that may lead to business failure for Saha."* — **Nov 2024 P1, 3(d)**

**The AO2 anchors:** **many new competitors, such as NIO, are entering the robot market and challenging Saha for market share**; and **as Saha has ambitious plans to expand, it may encounter cash flow problems due to increased outflows** for advertising and materials.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **The first reason is competition, and Saha's market makes it acute: NIO and others are entering robotics, and a new entrant usually attacks on either price or technology.** **If a rival develops a robot that is technologically superior, or less expensive, Saha loses the customers it has** — and in a market where products are bought on specification, **being overtaken is not a gradual decline; the customers simply stop buying.** **The second reason comes from Saha's own growth plan.** **Expanding to other continents requires spending heavily on advertising and materials before any of the new revenue arrives**, and **that gap is where businesses die: the outflows come first, the sales come later**. **The measurable end is insolvency, not unprofitability.** **A shortage of cash means Saha cannot pay what it owes on the day it is due**, and **a business with a full order book and no liquidity can still be forced to stop trading** — **which is why cash flow, not ambition, is what decides whether the expansion is survivable.**

| Step | The move |
|---|---|
| **1. Reason 1** | New entrants (NIO) **attack on price or technology** |
| **2. Reason 2** | Expansion spends **before** the revenue arrives |
| **3. The mechanism** | **Outflows come first** → a cash gap |
| **4. Measurable end** | **Insolvency** — the business stops, even with customers |

**Second acceptable chain:** a small business expanding into other continents **stretches its management** — the same people doing more **leads to mistakes in pricing, stock or quality**, any of which can cost the customers it was trying to win.

> ⚠️ **This is the same mechanism as entry 123 (the importance of cash) read in reverse.** **Failure here is a cash failure, not a lack of profit** — and **naming insolvency rather than "they will make a loss" is what shows you understand the difference.**

---

## 171. QUALITY SERVICE — why it matters in hospitality

**Asked:** *"Analyse the importance of making sure guests have a quality service when staying at a Premier Inn."* — **Nov 2024 P2, 4(b)**

**The AO2 anchors:** if the **reception staff are helpful and accommodating**, guests are **more likely to return**; and if the **room has all the amenities guests require, such as tea and coffee facilities**, that matters too.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> In a hotel, **the service is the product** — a guest cannot take the room home and inspect it later, so **their judgement is formed in the hours they are there, and it is formed about people as much as furniture**. **Two things decide it, and they are both in the scheme's bullets.** The first is **the room itself: whether the amenities the guest expects, such as tea and coffee, are actually there** — because a missing kettle is not a small thing at eleven at night, it is **the difference between a hotel that thought about them and one that did not**. **The second is the staff: helpful, accommodating reception staff are what turn an ordinary stay into one a guest remembers well**, and **only one of the two has to go wrong for the whole stay to be judged badly**. **The measurable end is repeat business and free promotion:** guests who were looked after **book again and raise the number of bookings and the profit**, and they **tell friends and family about the service they received** — which is the cheapest marketing a hotel chain will ever get.

| Step | The move |
|---|---|
| **1. Point** | In a hotel **the service is the product** — judged as it is delivered |
| **2. Strand A** | The room's **amenities** — what the guest expects to find |
| **3. Strand B** | The **staff** — helpful and accommodating |
| **4. Measurable end** | **Repeat bookings + word of mouth** |

**Second acceptable chain:** quality service **reduces complaints and refunds** → staff spend their time serving rather than resolving → **the hotel runs at a lower cost as well as a better reputation**.

> ⭐ **A "quality of service" question wants you to break the service into its parts** — what the guest finds (the room, the amenities) and **how they are treated (the staff)**. **Naming both, from the scheme's own bullets, is the difference between a level 2 and a level 3 answer.**

---

## 172. EMPLOYEE SATISFACTION — why a business measures it

**Asked:** *"Analyse why Ocean Vibes should measure employee satisfaction."* — **Nov 2025 P1, 1(g)**

> **Note the verb: MEASURE, not *improve*.** The question is about **finding out** what staff think — and what the business does with the answer.

**The AO2 anchors:** measuring satisfaction **will help Ocean Vibes retain its tour guides who operate the dolphin and bird tours**; and **if employees are satisfied, they will be motivated to provide good quality boat tours**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> A business **cannot manage what it does not know**, and **unhappy staff rarely say so before they leave**. Measuring satisfaction **is how Ocean Vibes finds out that its tour guides are thinking of going** while there is still time to do something about it — **which matters more here than in most businesses, because the guides are the product**. **The second reason is what satisfaction does to the work itself.** Guides who are **satisfied are motivated to provide good quality boat tours**, and **the customers on a dolphin or bird tour are judging exactly that** — the guide's knowledge, patience and enthusiasm. **The measurable end runs through three stages.** Holding on to the guides **reduces the recruitment and training costs of replacing them**, which **raises profitability**; better tours produce **good reviews**; and good reviews **encourage recommendation and increase sales** — so the questionnaire that measures satisfaction is really **the first step in a chain that ends in revenue.**

| Step | The move |
|---|---|
| **1. Point** | You **cannot manage what you do not measure** — staff leave without warning |
| **2. Strand A** | Spotting dissatisfaction early → **the guides are retained** |
| **3. Strand B** | Satisfied guides **give better tours** — they *are* the product |
| **4. Measurable end** | **Lower recruitment cost + reviews → more sales** |

**Second acceptable chain:** measuring satisfaction **tells Ocean Vibes what specifically to change** — pay, rota, equipment — so **any money spent on improving conditions goes where the problem actually is**, rather than being spread across everything.

> ⚠️ **"Measure" is the command word, and it carries a mark.** A business measures **so that it can act on the result** — **the diagnosis is the point.** An answer that only says *"happy staff work harder"* has answered a question about **motivation** (entry 139), not about **measurement**.

---

## 173. PROFIT — why it is important

**Asked:** *"Analyse why profit is important to Samsung."* — **Nov 2025 P2, 3(d)**

**The AO2 anchors:** Samsung **invests large amounts of funding to design and develop innovative electronic products**; and it **is a public limited company and the leading manufacturer of TVs**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> For a business like Samsung, **profit is not the reward at the end — it is the fuel at the start of the next product**. **Designing and developing innovative electronics takes enormous funding before anything can be sold**, and **every smartphone or TV in the shops was paid for by the profit from the model before it**. **That is why a fall in profit is more serious for Samsung than for a business selling a simpler product: the next generation gets funded out of this one.** **The second reason is what Samsung's ownership makes possible.** **As a public limited company, it can attract funds from investors — and investors are enticed by the possibility of high returns.** **Profit is the evidence that produces those returns, so strong profit draws in further funding on top of what Samsung earns itself.** **The measurable end is a cycle:** high profit **funds new technology, which keeps it competitive in the electronics market**, which **generates the next round of profit** — and a business that cannot turn that cycle **loses ground to rivals within one product generation.**

| Step | The move |
|---|---|
| **1. Point** | Profit **funds the next product**, not just this one |
| **2. Strand A** | Design and development are paid for **before any sale happens** |
| **3. Strand B** | As a plc, **high returns attract investor funds** |
| **4. Measurable end** | **Competitiveness in the next generation**, funded from this one |

**Second acceptable chain:** profit **provides a cushion** for a product that fails → Samsung can **absorb a flop without cutting staff or development** → which **protects the long-term innovation the business depends on**.

> ⚠️ **"Profit is the difference between revenue and costs" is a definition and earns nothing at this tariff.** The scheme's bullets are **reinvestment in innovation** and **attracting investors** — **both consequences, both forward-looking.** Compare the 3-mark tier, where the *method* of increasing profit **is** what is marked.

---

## 174. MARKET RESEARCH — its purpose

**Asked:** *"Analyse the purpose of market research for Samsung."* — **Nov 2025 P2, 4(b)**
**Also asked:** *"Analyse the importance of reliable market research (PPS)."* — June 2024 P1 3(d) · *"Analyse two methods of primary research (Saha)."* — Nov 2024 P1 1(g)

> **Three research questions across three papers, each testing something different:** **entry 143** = whether the data can be trusted · **entry 169** = which method to use · **this entry** = what the research is *for*.

**The AO2 anchors:** Samsung is able to **identify and understand its customers' needs** in what they look for when buying a laptop or TV; and market research **will help Samsung identify potential gaps in the competitive smartphone market**.

> **Model answer — 6 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> Market research exists **to replace a guess about the customer with evidence**, and for Samsung the guess would be an expensive one. **Its first purpose is to identify and understand what customers actually look for when buying a laptop or a TV** — because **the features a design team finds impressive are not always the ones that sell**, and a product built around the wrong feature **cannot be fixed after launch**. **The second purpose is finding gaps.** Research lets Samsung **see what the competitive smartphone market is not offering**, and **a gap is a product the rivals have not built** — the cheapest kind of advantage there is, because **there is no competition to fight on price yet**. **The measurable end is a product that sells on purpose rather than by luck.** Knowing **which features customers prefer increases demand for the product**, and identifying a gap lets Samsung **build a unique selling point that attracts customers the others are not reaching** — which is what turns a research budget into a market position.

| Step | The move |
|---|---|
| **1. Point** | Research **replaces a guess with evidence** — and guesses are expensive in electronics |
| **2. Strand A** | **Customer needs identified** → features built around what sells |
| **3. Strand B** | **Gaps in the market found** → a product with no direct rival |
| **4. Measurable end** | **Higher demand + a USP that attracts new customers** |

**Second acceptable chain:** research **tests a product or a price before launch** → Samsung can **find out whether it will sell without gambling the whole development budget** → so **the cost of being wrong falls from a failed product to a failed survey.**

> ⭐ **The three research questions side by side:** **purpose** = why do it at all · **reliability** = is the answer trustworthy · **method** = how do you collect it. **Each has a different answer, and the exam has now set all three.**

---

# ✅ THE 6-MARK TIER IS COMPLETE

| | |
|---|---|
| **Blocks in the tier** | **114** — derived from the 38 mark schemes, validated at 80 marks per paper |
| **Blocks carried by an entry** | **114 · 100%** |
| **Blocks needing an entry of their own** | 68 |
| **Blocks covered by an existing entry** | 46 |
| **Entries used** | **74** — numbers 101–174 |

**What that compression means.** 114 six-mark questions became **74 entries**, because **40% of them were repeats of a topic already answered** — *multinational* six times, *motivating employees* six times, *break-even* five times, *interest rates*, *cash*, *SoCI*, *branding* and *robotics* three times each. **No candidate ever sits six papers, but the topic they are examined on has been set six times, and the chain that earns the marks is the same every time.**

**How to use this tier under pressure.** Read the **question stem** for two things before writing: **the direction** (*benefits* / *concerns* / *impact* / *effectiveness*) and **the party** (the business, its owners, its customers, a country). Half the errors recorded in this tier come from answering the wrong direction or **analysing the wrong party** — entry **112**, entry **140** and entry **135** are the three clearest cases.

> ### THE ONE RULE FOR EVERY 6-MARK ANSWER, EARNED FROM THE 6/6 IN THE ARCHIVE
> **One point, developed in strands, with application throughout — and end on something measurable.** *"The candidate has provided 1 point with developed strands… Candidates are reminded that there are no marks for knowledge in this question."* **Two points each developed once scored 5/6. Depth beats breadth, and every entry above is built in that shape.**

---

# BATCH 7 — 9-MARK JUSTIFY, PART 1

**1 scaffold entry + 11 option-pair entries, covering every sources-of-finance question in the qualification.**

> ### ✅ THE 9-MARK TIER IS THE MOST UNIFORM IN THE QUALIFICATION — AND THE LEAST REPETITIVE
> All **76** nine-mark questions use **one framing and one framing only**: *"Justify which one of these two options X should choose."* There is no variation in the command, the AO split (**AO2 = 3 · AO3 = 3 · AO4 = 3**) or the level descriptors. **So the scaffolding below is worth learning once and using 76 times.**
>
> **But unlike the 3-mark and 6-mark tiers, the nine-mark tier barely repeats its content.** In the option pairs there are **55 distinct combinations across 76 blocks** — the same business decision (a source of finance) is set with **eleven different pairs**. **What repeats is the DECISION TYPE, not the pair.** That is why this batch is organised by decision type, and why the entries below are grouped: *sources of finance* is one decision type with eleven pairs inside it.

---

## 175. ⭐ THE UNIVERSAL 9-MARK SCAFFOLD — read this before any Justify answer

**The framing, in full, is always:** *"Option 1: … Option 2: … **Justify which one of these two options X should choose.**"* Sometimes the stem adds *"You should use the information provided as well as your own knowledge of business."* — **that sentence is a instruction, not a formality: it is telling you the AO2 mark cannot be earned from general knowledge.**

### What the three AO marks are actually for

| AO | Marks | What it means in a Justify answer |
|---|---|---|
| **AO2** — application | **3** | **Case facts used as evidence for the option you favour.** Not the business's name — the *facts*. |
| **AO3** — analysis | **3** | **A chain of reasoning** from the option to a consequence for this business. |
| **AO4** — evaluation | **3** | **The judgement, the counter-argument, and a NAMED CONDITION.** |

### ⭐⭐ THE STRUCTURE THAT SCORES — four moves, in this order

| Move | What you do | Why it earns the mark |
|---|---|---|
| **1.** | **State your choice immediately.** *"CCT should sell the unused equipment."* | AO4 needs a decision. **Do not leave it to the end** — an answer that only decides in the last line leaves the examiner hunting for it. |
| **2.** | **Give the case-specific reason for it** — the fact from the case that makes *this* option right *for this business*. | AO2. The fact must be from the case, **not the business's name**. |
| **3.** | **Dismiss the other option with the scheme's own counter-argument** — *"however, …"*. | **This is the AO4 the mark schemes print for every single block.** Every AO4 bullet in all 76 questions begins *"However…"*. |
| **4.** | **Name the CONDITION your judgement depends on.** | ⭐ **The single mark most candidates miss, and the reason a 9/9 looks different from a 7/9.** |

### ⭐⭐ THE NAMED CONDITION — the one thing that separates 9 from 7

**The rule, proved from the verified 9/9s:** *a top-band evaluation scores only on a condition specific to **this business** and **this option**.* The test is simple —

> **Could your final condition be pasted onto a different question without changing a word? If yes, it is not a condition — it is a platitude, and it scores nothing.**

**A platitude:** *"This depends on whether the business can afford it."* — **worthless.**
**A named condition:** *"**However, the success of this depends on how much employees get to voice their own concerns in business.**"* — Rabanne, 9/9, and it is a condition because **it could only be written about weekly meetings.**

**So end on the specific fact or number that would have to hold.** *"This works **provided the €7 500 is genuinely available in savings**"* · *"This depends on **whether the electric bicycles at £550 each are actually cheaper than repairing the tour route**"* — **the number and the case fact are what make it un-pasteable.**

### The 9/9 conclusion — three sentences, and they do three jobs

The verified full-mark conclusions are all **three sentences long** and run in this order:

1. **The choice, and the reason** — *"Rabanne should hold weekly meetings as it gives employees this sense of belonging as their opinions are physically heard."*
2. **The other option, dismissed** — *"Whereas communication via messages can get lost in inboxes which leads to manufacturers missing important business objectives announcements."*
3. **The named condition** — *"However, the success of this depends on how much employees get to voice their own concerns in business."*

### ⚠️ THE FIVE WAYS THIS QUESTION IS LOST

1. **Analysing the wrong party** — several stems ask what is best for the *owners*, the *employees* or the *country*. **Check who benefits.**
2. **Deciding at the end** (or not at all). AO4 needs a choice, visibly.
3. **Writing two mini-essays with no comparison.** The marks are for **choosing**, so the analysis of each option exists to support a decision.
4. **A generic conclusion** — see the pastability test above.
5. **Bullets.** They **disqualify the top levels** outright, on every tariff.

> ⭐ **One more structural fact worth knowing:** across all 76 blocks, **2(f) is almost always a marketing or finance choice** (promotion, pricing, research, sources of finance) and **3(e) is almost always an operations or HR choice** (job design, training, recruitment, production, contracts). **If you are running short of time, that tells you what the question is likely to be about before you read it.**

---

## 176. SOURCES OF FINANCE — venture capital vs a bank loan

**Asked:** *"Option 1: venture capital · Option 2: loan capital. Justify which one of these two options the owners should choose."* — **Nov 2025 P1, 2(f)**, Ocean Vibes ($£$*dolphin and bird tours*)
> **⚠️ Do not confuse this with *venture capital vs crowdfunding*, which was asked on the same series.** That pair — June 2026 P1R, Spud Bros — is **entry 185**, and it is a different question with a different answer, because **neither option charges interest**. **Check which two options you have been given before you write a single line.**

**The AO2 anchors (Ocean Vibes):** the owners may **appeal to an individual who wishes to invest in a business concerned with the welfare of birds and dolphins**; a loan would let them **buy new boats to offer more boat tours**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **The owners of Ocean Vibes should take the venture capital.** The decisive fact is **what the investor brings beyond money: this is a business whose whole appeal is the welfare of birds and dolphins**, and an investor who has chosen it *for that reason* is **someone who will fund the boats and support the positioning rather than pushing the business towards whatever makes the fastest return**. **A loan would do the opposite in one important respect.** It arrives with **interest to be paid on top of the amount borrowed, which raises costs and reduces profitability** — and a boat tour business **carries fixed costs whatever the weather or the season does**, so a repayment schedule is a cost that must be met in the months when tours cannot run. **However, the venture capitalist may wish to take some control of the business, which may cause disagreement within it** — and for **owners who built a business around a conservation principle, that control is the real price being paid.** **For that reason I would still choose the venture capital, but only as long as the investor's interest genuinely matches the tours' welfare focus — because the moment the investor wants to cut the wildlife spend to protect the return, the business has lost the thing that makes anyone book it.**

| Move | The answer |
|---|---|
| **1. Choice** | **Venture capital** — stated in the first sentence |
| **2. AO2 + AO3** | Investor **chosen the business for its welfare focus** → funds the boats **without forcing a return at the cost of the positioning** |
| **3. Counter-argument** | The loan **adds interest → higher costs → lower profitability**, on a business with fixed costs out of season |
| **4. Named condition** | ⭐ **Provided the investor's interest genuinely matches the welfare focus** — not "provided it is affordable" |

**Second acceptable chain:** a bank loan **leaves the owners in full control of the tours they designed** → no disagreement over direction → **but the interest is a cost the tours must cover in every season.**

> ⚠️ **The AO4 for both options is in the scheme and both must appear.** The venture capitalist **"may take a percentage of the business in return for the capital, which gives the owners less independence or control"**; the loan **"will incur interest rates that have to be paid in addition to the loan amount which will increase costs and possibly reduce profitability."** **An answer that only criticises the option it rejects has used half the AO4.**

---

## 177. SOURCES OF FINANCE — crowdfunding vs a bank loan

**Asked:** *"Option 1: crowdfunding · Option 2: loan capital."* — **Nov 2024 P1, 2(f)**, Saha ($£$*robots for hotels, restaurants and homes*)

**The AO2 anchors:** Saha may **appeal to the public for funding to expand its sale of robots into all continents**; a loan could **build new factories to manufacture the new robots for homes**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **Saha should use the loan capital.** The reason is the scale of what the money has to do: **the plan is to expand robot sales into all continents**, and that requires **factories — bricks, machinery and a build programme** — not a single popular product. **Crowdfunding raises money in exchange for interest and enthusiasm, not collateral, and it suits a defined, attractive, single purpose.** A factory programme is **neither** — it is expensive, staged and unglamorous — so **crowdfunding is the wrong shape of finance for it. A loan is the right shape because it can be sized and repaid over the life of the asset it buys.** **However, crowdfunding carries no interest at all**, and Saha would keep **every penny of the profit from the expansion** rather than paying a lender for the privilege. **However, the loan will incur interest rates that have to be paid in addition to the loan amount, which will increase costs and reduce profitability** — and **for a business whose robots are priced against rivals such as NIO, a permanent interest cost is a permanent disadvantage on price.** **I would still choose the loan, provided the factory programme is staged so that each stage generates sales before the next is funded — because if Saha borrows the whole amount before the first factory is earning, the interest falls due on assets that are not producing yet.**

| Move | The answer |
|---|---|
| **1. Choice** | **Loan capital** — first sentence |
| **2. AO2 + AO3** | **Factories across continents** = large, staged, unglamorous → **matches a loan, not a public appeal** |
| **3. Counter-arguments** | Crowdfunding = **no interest, keep all profit**; loan = **interest on top of capital → higher costs → lower profitability** |
| **4. Named condition** | ⭐ **Provided the build is staged so each factory earns before the next is funded** |

**Second acceptable chain:** crowdfunding **also markets the business to the public who funded it** → they become customers and advocates → but **"there is no guarantee that sufficient funds would be raised … to allow Saha to pursue its ambitious expansion plans"**, and **a campaign that misses its target can leave the business with nothing at all.**

> ⭐ **The shape test is the transferable skill: match the SIZE, the STAGING and the ASSET to the source of finance.** Crowdfunding suits **a defined, attractive, one-off purpose**; a loan suits **a sized, staged, resaleable asset**. **Learn the test, not the answer.**

---

## 178. SOURCES OF FINANCE — personal savings vs a bank loan

**Asked:** *"Option 1: using Rachel's personal savings · Option 2: taking out a small bank loan."* — **June 2024 P1, 3(e)**, PPS ($£$*pet products, €7 500 for CCTV and kennels*)
**Also asked:** *"Two sources of finance: Option 1: personal savings · Option 2: a loan. Justify which one of these two options Claire should choose."* — **June 2026 P1, 3(e)**, Violet Cakes ($£$*a second café in London*)

> **This pair has been set twice in three years, on two different businesses. It is the most repeated pair in the tier.** The scheme's AO4 for both questions is the same: **the savings may not be enough and may leave the business with no surplus for emergencies; the loan adds interest, which raises costs.**

**The AO2 anchors (PPS):** personal savings give **quick access to the €7 500 needed to buy the CCTV package and build the kennels**; the bank loan is **for an agreed period at a fixed rate of interest**.
**The AO2 anchors (Violet Cakes):** personal savings mean **immediate access to pay for the rent and marketing of the second cafe**; Claire **may secure the loan at a low fixed rate because the business has traded successfully since 2010**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **Rachel should use the personal savings.** The decisive fact is **what the money is for: CCTV and a kennel block, neither of which earns anything on its own — they make the existing pet business safe and usable.** **That makes speed matter more than cost, because the benefit starts the moment the kennels open and the risk is being taken today.** **The savings are the only option that produces the money immediately, with no application, no approval and no delay.** **However, the cost of the work is high, and Rachel may not have enough saved to finance it all** — and **spending the entire reserve leaves the business with nothing for an emergency**, which for a kennels business means **a broken boiler in January would have to be borrowed for at the worst possible moment.** **I would still choose the savings, but only on the condition that Rachel keeps back a stated reserve for emergencies and funds any shortfall by some smaller source — because a kennel block paid for by leaving the business unable to handle a surprise is a repair funded by a bigger risk.**

| Move | The answer |
|---|---|
| **1. Choice** | **Personal savings** — first sentence |
| **2. AO2 + AO3** | **CCTV and kennels earn nothing alone** → they enable the existing business → **speed matters more than cost** |
| **3. Counter-arguments** | Savings: **may not be enough, and leaves no surplus for emergencies**; loan: **interest adds to costs** |
| **4. Named condition** | ⭐ **Provided a stated reserve is kept back and any shortfall funded separately** |

**Second acceptable chain (Violet Cakes):** Claire is **an established, successful business since 2010** → **the bank will lend at a LOW FIXED RATE** → the interest cost is therefore predictable and cheap → **and the savings stay intact for the café's first quiet months, which is exactly when a new site needs a cushion.**

> ⭐ **Notice how the two businesses point to opposite answers on the same pair.** PPS is **a one-off safety-and-capacity purchase** → savings. Violet Cakes is **an established business with a cheap rate on offer** → the loan starts to look better. **The option pair does not determine the answer; the case does.** That is why memorising "always choose the loan" would fail — and why this bank gives you the case facts, not a rule.

---

## 179. SOURCES OF FINANCE — crowdfunding vs an overdraft

**Asked:** *"Option 1: crowdfunding · Option 2: an overdraft."* — **May–June 2019 P1, 3(e)**, Backyard Shoez ($£$*shoes, three mall shops*)

**The AO2 anchors:** crowdfunding is **a quick way to raise finance to buy new shoes and the latest fashion**; an overdraft gives **a temporary facility to withdraw funds from the bank to buy the required amount of stock**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **Backyard Shoez should take the overdraft.** The decisive fact is **what the money buys: stock — new shoes and the latest fashion — which is sold on and turned back into cash within weeks.** **An overdraft is built for exactly that cycle: it is a temporary facility that the business draws on when the stock must be bought and repays when the stock sells.** **Crowdfunding is built for the opposite cycle.** It raises a lump sum in exchange for a campaign, and **it is a high-risk way of obtaining finance, because a campaign that fails to reach its target can raise nothing at all** — which, for a shop that needs stock on the shelves now, **means the expansion plan is delayed by a marketing exercise it may lose.** **However, the bank can demand repayment of an overdraft at any time, and the interest rates on overdrafts are usually high** — so the flexibility is real but it is rented, not owned. **I would still choose the overdraft, provided the stock turns over fast enough to clear the balance within the season — because an overdraft only stays cheap while it is repaid quickly, and a fashion line that does not sell converts a cheap facility into an expensive debt.**

| Move | The answer |
|---|---|
| **1. Choice** | **The overdraft** — first sentence |
| **2. AO2 + AO3** | Stock **sells and returns to cash in weeks** → matches a **temporary revolving facility** |
| **3. Counter-arguments** | Crowdfunding **may raise nothing if the target is missed**; the overdraft is **repayable on demand at high rates** |
| **4. Named condition** | ⭐ **Provided the stock turns over fast enough to clear the balance within the season** |

**Second acceptable chain:** crowdfunding **brings customers as well as cash** — the people who fund a small shoe shop become shoppers → but **a mall shop's customers must be local**, and **an online campaign reaches people who will never walk into the three shops.**

> ⚠️ **The overdraft's AO4 is the one candidates forget: "the bank can demand repayment at any time."** **That is a genuine risk and it is printed in the scheme** — an answer that treats the overdraft as simply "flexible" has not evaluated it.

---

## 180. SOURCES OF FINANCE — retained profit vs a bank loan

**Asked:** *"Option 1: using retained profits · Option 2: getting a bank loan."* — **June 2022 P1, 2(f)**, TBTS ($£$*toy shops, buying from new suppliers*)

**The AO2 anchors:** retained profits let TBTS **buy the toys immediately to sell in its toy shops**; with the bank loan **TBTS will have to wait for a decision before buying the toys from new suppliers**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **TBTS should use the retained profits.** The decisive fact is **timing against a seasonal trade: toys are bought to be sold, and a toy shop that cannot stock a new line by the season has lost that line's whole year.** **Retained profit is the only one of the two that is available the same day, because it is already in the business** — there is no application, no credit assessment and no waiting for a decision. **A bank loan, by contrast, means TBTS waits for the bank before it can buy from the new suppliers at all**, and **the interest has to be paid back on top, which adds an additional cost.** **However, TBTS can only use retained profits if there are any in the first place, and building them up takes time** — so if the shop has had a poor year, the option does not exist. **I would still choose the retained profits, but only if they cover the stock order without emptying the reserve — because a toy shop that spends every penny of its past profit on this year's line has nothing left to buy next year's, and the loan it takes then will be at a worse rate for having no cushion.**

| Move | The answer |
|---|---|
| **1. Choice** | **Retained profits** — first sentence |
| **2. AO2 + AO3** | Toys are **seasonal stock** → **available the same day beats waiting for a decision** |
| **3. Counter-arguments** | Retained profit **may not exist / takes time to build**; the loan **adds interest as an extra cost** |
| **4. Named condition** | ⭐ **Provided it covers the stock order without emptying the reserve** |

**Second acceptable chain:** the loan **can be repaid over a long period, so TBTS can budget for the interest** → that certainty is worth something → **but the shop still pays more in total than if it had funded the stock itself.**

---

## 181. SOURCES OF FINANCE — retained profit vs selling unused assets

**Asked:** *"Option 1: retained profit · Option 2: selling off assets that are no longer used."* — **May–June 2020 P2R, 3(e)**, HRMW ($£$*sports goods, R&D for new tennis racquets*)
**Also asked:** *"Option 1: selling off unused bicycle equipment · Option 2: retained profit."* — **June 2025 P1R, 3(e)**, CCT ($£$*electric bicycles at £550 each*)

> **Note how the two papers put the SAME two options in opposite orders — and how the named condition differs completely between them, because the numbers do.** This is the clearest illustration in the bank that **the condition must come from the case.**

**The AO2 anchors (HRMW):** the retained profit **could be used straight away to pay for the R&D**; selling assets the business **owns and no longer uses makes good business sense**.
**The AO2 anchors (CCT):** selling unused equipment **can provide cash to buy the bicycles**; retained profit gives **immediate access to the funds**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **HRMW should use the retained profit.** The decisive fact is **what the money is for: research and development of new tennis racquets.** **R&D does not produce anything saleable while it is being done, so the business must be able to fund it without a deadline hanging over it — and retained profit is money that has no repayment date attached.** **Selling assets has the appearance of good sense, because the assets are no longer used, but the timing is not in HRMW's control: there is no guarantee it can sell them in time**, which means **it may have to find alternative funding anyway, having wasted the weeks the R&D needed.** **However, there may be insufficient retained profit, and HRMW would then have to take out a loan, which could be expensive** — so the option is only as good as the balance. **I would still choose the retained profit, on the condition that it covers the full R&D programme for one racquet rather than part of it — because a racquet that is half-developed earns nothing, while a racquet that is finished earns from the first sale.**

| Move | The answer |
|---|---|
| **1. Choice** | **Retained profit** — first sentence |
| **2. AO2 + AO3** | **R&D sells nothing while it is happening** → needs money **with no repayment date** |
| **3. Counter-arguments** | Retained profit **may be insufficient → then a loan, which is expensive**; asset sales **may not complete in time** |
| **4. Named condition** | ⭐ **Provided it covers the full R&D for one racquet, not part of it** |

**The same pair on CCT's numbers — and a different condition.** For CCT the AO4 is quantified: **the electric bicycles cost £550 each, so CCT "may not have many surplus assets to sell off that will cover the cost for all of the bicycles, leaving them less competitive"**; and **"if CCT uses all of its retained profit to purchase the bicycles, it will not have any funding to cover any unforeseen circumstances or emergencies."** **So the CCT condition is the reserve, and the HRMW condition is completing the development.** **Same options, different condition, because £550 per bicycle is a number and R&D is a process.**

> ⭐ **This is the entry to reread if you want to see how the named condition actually works.** Neither conclusion could be pasted onto the other question, and both are built from a fact in the case.

---

## 182. SOURCES OF FINANCE — crowdfunding vs retained profit

**Asked:** *"Option 1: crowdfunding · Option 2: the owner's own retained profits."* — **Nov 2021 P1, 3(e)**, Artify Studio ($£$*new art sets, a small studio in Kampong Glam*)

**The AO2 anchors:** crowdfunding is **a quick way to raise finance for new art sets**; the owner **could invest his own retained profits earned from previous years**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **Tay Hui Jae should use the retained profits.** The decisive fact is **the size and identity of the business: Artify Studio is a small studio, and it is his.** **Crowdfunding works on reach — it raises money from people who have never been to the studio — and a small business in one area "may not have enough presence to gain the funding needed".** **Worse, a crowdfunding campaign is all-or-nothing on a target: if the target is not met, the business "may end up with nothing" at all** — so it spends the campaign's effort and ends with no art sets. **Retained profits, by contrast, are certain: they are already earned, already in the business, and involve no campaign to lose.** **However, there is no guarantee the new art sets will sell — customers may prefer their children to attend the studio sessions instead** — which means **the owner's own money is the money at risk.** **I would still choose the retained profits, on the condition that Tay Hui Jae tests the art sets in the studio's own sessions first — because the risk of the product not selling is the real risk here, and it can be reduced for the price of a few weeks of classes rather than the whole cost of the stock.**

| Move | The answer |
|---|---|
| **1. Choice** | **Retained profits** — first sentence |
| **2. AO2 + AO3** | A **small local studio has no crowdfunding reach**, and a missed target raises **nothing** |
| **3. Counter-arguments** | Retained profit **puts the owner's own money at risk if the sets do not sell** |
| **4. Named condition** | ⭐ **Provided the sets are tested in the studio's own sessions first** |

**Second acceptable chain:** crowdfunding **markets the studio at the same time as raising the money** — backers learn its name → **but that audience is online and the studio's customers walk in from the neighbourhood**, so **the marketing reach is not the reach the business needs.**

> ⚠️ **The crowdfunding AO4 appears in three separate questions and is always the same two points: the amount raised may be insufficient, and a missed target means nothing is raised.** **Those two sentences are the whole counter-argument — learn them as a pair.**

---

## 183. SOURCES OF FINANCE — crowdfunding for a small business

**Asked:** *"Option 1: crowdfunding · Option 2: an overdraft."* — May–June 2019 P1 3(e) *(see entry 179)*
**The standalone point, worth keeping separately:** crowdfunding is the **only** source of finance in this qualification whose **failure mode is raising nothing at all.**

**When crowdfunding is the right answer:** the purpose is **defined, attractive and communicable in a sentence or an image** *(a new studio, a community project, a distinctive product)* · the business **already has an audience** to appeal to · and **the business wants customers as well as cash**, because backers become buyers.

**When it is the wrong answer:** the need is **large and staged** *(factories, as in Saha)* · the need is **unglamorous and urgent** *(stock on the shelf today, as in Backyard Shoez)* · or the business **has no reach to draw on** *(a small local studio, as in Artify).*

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]` *(template, for any crowdfunding pair)*
> **The business should [choose / not choose] crowdfunding, and the decisive fact is [the purpose and the audience the case gives you].** **Crowdfunding's strength is that it converts an attractive idea into capital from people who want it to exist — and those people then buy the product**, so the money and the first customers arrive together. **Against that, "there is no guarantee that sufficient funds would be raised", and a campaign that misses its target raises nothing — so the business has spent the effort and still has no finance.** **However, [the other option's counter-argument from the scheme].** **I would [choice], provided [the named condition drawn from the case's own figure].**

> ⭐ **This is the only entry in the bank that is a template rather than a worked answer, and it is here because crowdfunding is the source of finance most likely to appear in a pair this bank has not yet seen.** **Use it with the case facts in front of you, never on its own.**

---

## 184. SOURCES OF FINANCE — the full comparison table

**Keep this table in your head; every pair above is two rows of it.**

| Source | Speed | Cost | What you give up | Its failure mode |
|---|---|---|---|---|
| **Personal savings** | **Immediate** | **None** | **Your own money and your reserve** | **May not be enough; leaves no surplus for emergencies** |
| **Retained profit** | **Immediate** | **None** | **The business's cushion** | **May not exist; takes time to build up** |
| **Selling unused assets** | **Uncertain** | **None** | **An asset you may want later** | **No guarantee of selling in time** |
| **Bank loan** | **Slow — a decision is required** | **Interest on top of the capital** | **Control stays with you** | **Interest increases costs, may reduce profitability** |
| **Overdraft** | **Fast, flexible** | **Interest on the amount drawn; usually high** | **Nothing, until it is called in** | **Repayable on demand at any time** |
| **Venture capital** | **Fast, if the investor is found** | **No interest** | ⭐ **Control, and a percentage of the business** | **The investor may interfere with decisions and objectives** |
| **Crowdfunding** | **Fast in time, uncertain in outcome** | **No interest** | **Nothing** | ⭐ **May raise insufficient funds; a missed target means nothing is raised** |
| **Franchising** *(as a growth source)* | **Fast** | **None to you — the franchisee pays** | **Control of how the brand is run** | ⭐ **You rely on the franchisee running it well and not causing bad publicity** |

> ⭐ **Two rows carry the AO4 worth 3 marks on their own: VENTURE CAPITAL costs you control, and CROWDFUNDING may raise nothing.** **The scheme prints them in question after question, on business after business.** If you remember nothing else from this batch, remember those two.

---

> ### ⚠️ CORRECTION — entry 176 covered the wrong pair for one of its two blocks
> Entry **176** was headed *"venture capital vs a bank loan"* and listed two blocks. **Only one of them is that pair.** Block 1 (June 2026 P1R, Spud Bros) is **venture capital vs CROWDFUNDING** — its stem prints *"Option 1: venture capital · Option 2: crowdfunding"*. **The pair is different, so the answer is different**, and it is now entry **185** below. **This is the same class of error as the Batch 5b miscount:** a topic label that absorbed a block it did not describe. **The block's own stem is the authority — not the topic name I gave it.**

---

## 185. SOURCES OF FINANCE — venture capital vs crowdfunding

**Asked:** *"Option 1: venture capital · Option 2: crowdfunding. Justify which one of these two options the brothers should choose."* — **June 2026 P1R, 2(f)**, Spud Bros ($£$*potato vans, expanding internationally*)

> **Read the options carefully — this is the pair that catches people out.** Both options bring in **outside money and neither charges interest**, so the usual "interest vs no interest" argument does not apply. **The two options differ in WHO the money comes from and WHAT they take in return.**

**The AO2 anchors:** a venture capitalist **may give advice on how to develop the potato business**; **people who have seen the business on social media sites such as TikTok may be persuaded to invest in Jacob and Harley**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **The brothers should take the venture capital.** The decisive fact is **what they need alongside the money: Spud Bros is expanding internationally, and the brothers are two people taking a family food business into markets they have never traded in.** **A venture capitalist "may give advice on how to develop the potato business", which is experience the brothers cannot buy** — and it **helps them decide on location and marketing strategies for the expansion plans**, which are exactly the decisions an unfamiliar market punishes. **Crowdfunding has a real advantage the venture capitalist does not: "small investments from many people will allow the business to expand throughout the UK without the need to pay back the investment"** — and those backers become customers. **However, the amount raised through crowdfunding may be insufficient to meet the capital required to expand internationally** — and international expansion is precisely the purpose here, so **the funding model is the wrong size for the plan.** **I would still choose the venture capital, but only on the condition that the brothers keep a controlling share of the business — because the scheme warns the venture capitalist will "take a percentage of the business in return for the capital" giving them "less independence or control", and a potato brand built on the brothers' own personalities cannot survive being run by someone else.**

| Move | The answer |
|---|---|
| **1. Choice** | **Venture capital** — first sentence |
| **2. AO2 + AO3** | **International expansion into unfamiliar markets** → the investor brings **advice and market experience**, not just money |
| **3. Counter-arguments** | Crowdfunding = **no repayment and backers become customers**, but **may raise insufficient funds for international expansion**; VC = **gives up a percentage and independence** |
| **4. Named condition** | ⭐ **Provided the brothers keep a controlling share** |

**Second acceptable chain:** crowdfunding's backers **found the brand through TikTok, so they are already the audience** → they buy as well as fund → **but "small investments from many people" scale to a UK roll-out, not to a US and Canada launch.**

> ⭐ **The distinguishing question for this pair: WHAT IS THE MONEY FOR, and IS IT BIG ENOUGH?** Crowdfunding suits **a UK-wide or community-scale step**; venture capital suits **an international move that needs both capital and guidance**. **Both take something from the owners — crowdfunding takes nothing but is small; venture capital is large but takes a share.**

---

## 186. GROWTH — venture capital vs franchising

**Asked:** *"Option 1: use venture capital to open new stores · Option 2: start offering franchises. Justify which one of these two options AWG should choose."* — **Nov 2023 P1, 2(f)**, AWG ($£$*Icelandic baby clothes and jumpers*)

> **This is the pair where the two options look most similar and are most different.** Both **fund new stores without a bank**, and both **cost AWG nothing in interest** — but one **keeps the stores and gives away control**, while the other **gives away the stores and keeps the brand.**

**The AO2 anchors:** a venture capitalist **may provide the funds to build the new stores** *and* **may have knowledge of the needs of Icelandic customers**; **a franchisee will pay AWG a fee for the right to sell its baby clothes**, which **allows AWG to increase its revenue from those fees**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **AWG should use the venture capital to open its own stores.** The decisive fact is what AWG is selling: **baby clothes whose appeal is a particular Icelandic identity, sold under its own name.** **A franchisee pays a fee for the right to sell that name — and everything the customer experiences in that shop is then being delivered by someone whose only obligation is the contract.** **The venture capital route keeps the shops AWG's own**, so **the product, the presentation and the brand stay under the control of the business that built them.** **And the investor brings a second thing the franchisee does not: the scheme notes a venture capitalist "may also have knowledge of the needs of Icelandic customers"** — which is directly useful to a business **whose whole proposition is being Icelandic.** **However, the venture capitalist "may want to take some control of the business and interfere with the decision making and objectives"** — and that is the genuine cost, because **AWG would be handing influence over those decisions to someone who is not Icelandic.** **I would still choose the venture capital, provided AWG negotiates the investment without giving away decisions on product and brand — because the fees from franchising grow revenue quickly, but "AWG are reliant on the franchisee running the business well and not causing bad publicity, which might impact its brand's reputation", and a damaged reputation is not recoverable by rewriting a contract.**

| Move | The answer |
|---|---|
| **1. Choice** | **Venture capital to open its own stores** — first sentence |
| **2. AO2 + AO3** | The product **is** the Icelandic identity → **owning the shops protects it**; and the investor **knows Icelandic customers** |
| **3. Counter-arguments** | VC = **takes control and interferes with objectives**; franchising = **AWG relies on the franchisee not damaging the brand** |
| **4. Named condition** | ⭐ **Provided AWG keeps decisions on product and brand** |

**Second acceptable chain:** franchising **turns AWG's fee income into revenue that arrives without AWG funding a single shop** → the growth is fast and the capital risk is the franchisee's → **but every new franchisee is a new person whose mistakes carry AWG's name.**

> ⭐ **The decisive test for this pair: WHOSE NAME IS ON THE DOOR?** If the brand *is* the product, **own the stores** (venture capital). If the brand can survive being delivered by someone else because the **system** is the product — as with IKEA's flat-packs (entry 161) — then **franchising is the faster and cheaper route.** **Note how entry 161 and this entry give opposite answers to the franchising question, because the businesses are different.** That contrast is the whole skill of this tariff.

---

## 187. ✅ THE FINANCE CLUSTER — CLOSED

**13 option pairs across 14 blocks — every source-of-finance Justify question in the qualification.**

| # | Option pair | Block(s) | Entry |
|---|---|---|---|
| 1 | Venture capital vs **crowdfunding** | 1 · Spud Bros | **185** |
| 2 | Venture capital vs **a bank loan** | 73 · Ocean Vibes | **176** |
| 3 | Venture capital vs **franchising** | 65 · AWG | **186** |
| 4 | Crowdfunding vs **a bank loan** | 69 · Saha | **177** |
| 5 | Crowdfunding vs **an overdraft** | 12 · Backyard Shoez | **179** |
| 6 | Crowdfunding vs **retained profit** | 62 · Artify Studio | **182** |
| 7 | Personal savings vs **a bank loan** | 4 · Violet Cakes · 38 · PPS | **178** |
| 8 | Retained profit vs **a bank loan** | 31 · TBTS | **180** |
| 9 | Retained profit vs **selling unused assets** | 22 · HRMW · 46 · CCT | **181** |
| — | *Crowdfunding template* | *(any unseen pair)* | **183** |
| — | *The full comparison table* | *(all of the above)* | **184** |

> ### ⭐ WHAT FOURTEEN FINANCE QUESTIONS CAN BE REDUCED TO — THREE TESTS
> **1. How fast is it needed, and how fast does each source arrive?** *(stock on the shelf today → savings or overdraft; factories and R&D → loan or retained profit)*
> **2. What does it cost, and is the cost money or control?** *(interest, or a share of the business)*
> **3. What is the FAILURE MODE?** *(a loan adds interest you must pay whatever happens; crowdfunding may raise **nothing at all**; an overdraft is **repayable on demand**.)*
>
> **Question 3 is the one candidates never ask, and it is where the AO4 lives.** Every mark-scheme counter-argument in this cluster is a failure mode.

---

# BATCH 7b — 9-MARK JUSTIFY, PART 2 — PROMOTION AND PRICING

**14 entries covering 21 blocks — every promotion and pricing Justify question in the qualification.**

> ### ⭐ WHY PRICING IS THE MOST REPETITIVE DECISION TYPE IN THIS TIER
> **Cost plus pricing appears in four different pairings** (against price skimming twice, against promotional pricing, against competition pricing) and **promotional pricing in three**. That is not an accident of the papers: **the examiner is testing the same two ideas from different angles**, and the scheme's counter-arguments for each are almost word-for-word identical across papers five years apart.
>
> **Learn the counter-arguments as fixed pairs and the pricing questions become a matching exercise:**

| Method | Its strength | Its fixed weakness — printed in the scheme, paper after paper |
|---|---|---|
| **Cost plus** | **Guarantees the cost is covered** — you know each sale makes something | ⭐ *"Does not account for what the customer is willing to pay"* / *"does not guarantee that sales are going to be made, especially if a competitor is cheaper"* |
| **Price skimming** | **High price while the product is new and distinctive** | ⭐ *"May limit the number of potential customers as the price is too high"* |
| **Promotional / lower price** | **Gains sales quickly and switches customers from rivals** | ⭐ *"Profit per unit is lower"* and ⭐ *"once the price reverts to normal, sales may reduce"* |
| **Competition pricing** | **Customers see it as comparable, so it competes on the shelf** | ⭐ *"As AWG use sustainable materials the manufacturing cost may be high, which means selling at a competitive price may not be feasible"* |
| **Price matching** | **Removes price as the reason to go elsewhere** | ⭐ *"There is no guarantee that customers will book with Premier Inn as they may prefer the facilities at another hotel"* |
| **Penetration / introductory** | **Entices people to try the product for the first time** | ⭐ *"Some customers may associate a low price with low-quality"* |

---

# BATCH 7c — 9-MARK JUSTIFY, PART 3 — THE PROMOTION CLUSTER COMPLETED

**8 entries covering the eight promotion blocks not already carried by entries 202–204.** With these, **every promotion and pricing Justify question in the qualification is covered.**

> ### ⭐ THE PROMOTION CLUSTER HAS ONE RECURRING ARGUMENT
> Read the eight counter-arguments below together and a single idea appears in almost all of them: **promotion that BUYS attention cannot guarantee what the attention does.** The scheme says it in six different ways —
>
> *"There is no guarantee that because an event has been sponsored by Kraft Heinz people will purchase its products"* · *"There is no control over social media and what is being said about Emirates by the users of social media"* · *"NEXT cannot be certain that all its customers who want to receive the wedding list service will read the newsletter, as there is no guarantee or way of checking that they have seen it"* · *"Not everybody uses social media so many people would not be aware of the advert"* · *"It may not bring in new customers or improve its image if the exhibition was poorly attended"* · *"There is no guarantee that customers are going to use the coupon or even visit the store, so the advertising costs would be wasted."*
>
> **Learn it as one sentence: you pay for the delivery, not for the result.** That is the ground the examiners argue on in this cluster, and it is where your AO4 marks are.

---

## 188. PROMOTION — attracting passing trade vs free promotional space

**Asked:** *"Option 1: offer food to passing trade to entice them into the bakery · Option 2: the charity shops Loaf works with could display the posters for free."* — **May–June 2020 P1R, 2(f)**, Loaf

**The AO2 anchors:** offering food **could entice passing trade into the bakery**; the charity shops **could display the posters for free**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **Loaf should use the charity shop posters.** The decisive fact is **the cost, and what Loaf can afford to spend on being seen.** **The posters are free — the charity shops it already works with have the windows and the footfall, and Loaf pays nothing to appear in them.** **Sampling, by contrast, costs twice: "someone outside giving out the samples means that the person is not working in the bakery selling goods, which could be considered a waste of time, and they are also giving out free food, which can be expensive."** **That is a wage and a product given away at once, for a method whose success depends on the passer-by stopping.** **However, the scheme's objection to the posters is real: "it is a cheaper method of advertising but may not bring in the clientele that Loaf would want to purchase its goods"** — the charity shop's visitors are not necessarily Loaf's customers. **I would still choose the posters, on the condition that the charity shops chosen are ones whose own customers already buy bread and cakes — because free advertising in the wrong window is worth exactly what it costs, while sampling converts only the people who were already close to buying.**

| Move | The answer |
|---|---|
| **1. Choice** | **The free charity-shop posters** — first sentence |
| **2. AO2 + AO3** | Posters are **free, using shops Loaf already supports**; sampling **costs a wage and the food** |
| **3. Counter-arguments** | Posters → **may not reach Loaf's kind of customer**; sampling → **staff taken off selling, food given away** |
| **4. Named condition** | ⭐ **Provided the charity shops' own customers already buy bread and cakes** |

**Second acceptable chain:** sampling **lets a customer taste the product, and taste is what a bakery sells** → it converts far better than a poster among people who are interested → **but only if the person handing out samples is not needed at the counter, which in a small bakery they usually are.**

> ⭐ **This is the one pair in the cluster where the CHEAPER option wins, and the reason is that the expensive one costs twice** — money *and* the labour that would otherwise be selling. **Wherever a small business is choosing a promotional method, ask what it costs in staff time as well as in cash.**

---

## 189. PROMOTION — pop-up events across the country vs new cookery courses

**Asked:** *"Option 1: pop-up events showcasing bakery products across the country · Option 2: introducing different cookery courses to target new customers."* — **May–June 2020 P1R, 3(e)**, Loaf

**The AO2 anchors:** pop-up events **will lead to higher sales**; different cookery courses **will target new customers wanting to learn new skills**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **Loaf should introduce the cookery courses.** The decisive fact is **what Loaf already owns: a bakery, a kitchen and the teaching space it is already using for cooking classes.** **New courses use everything the business already has, so the cost is the ingredients and the teacher's time — and the customers pay in advance to attend.** **Pop-up events do the opposite: they take the business to places it does not know, and "as Loaf may not be known, and the costs of running these pop-up events across the country could be higher than the revenue from them, leading to a negative net cash flow."** **A national tour of pop-ups is a large, uncertain outlay for a business whose name is not yet recognised outside its own area.** **However, the courses have their own trap, and it is the one the scheme flags: "this may not increase net cash flow because Loaf will still have to run the classes even if they are not full, so could end up spending more on the teachers and food, resulting in higher costs."** **A half-empty class costs the same as a full one.** **I would still choose the courses, on the condition that Loaf takes bookings in advance so a class only runs when it is paid for — because the difference between these options is that one puts Loaf's money at risk nationally, and the other puts the customer's money in first.**

| Move | The answer |
|---|---|
| **1. Choice** | **The cookery courses** — first sentence |
| **2. AO2 + AO3** | Uses **the kitchen and space Loaf already has**, with customers paying in advance |
| **3. Counter-arguments** | Pop-ups → **costs may exceed revenue → negative net cash flow**; courses → **half-empty classes cost the same as full ones** |
| **4. Named condition** | ⭐ **Provided bookings are taken in advance so a class only runs when paid for** |

**Second acceptable chain:** pop-ups **take the products to places where nobody knows the bakery at all** → that reach is the only way to grow beyond the local area → **but a business that is not known cannot rely on a crowd turning up to buy.** The scheme's own phrasing is the giveaway: *"as Loaf may not be known"*.

---

## 190. PROMOTION — special offers vs social media

**Asked:** *"Option 1: increase special offers to encourage more passengers to fly · Option 2: use social media to advertise to a large number of potential passengers."* — **May–June 2020 P2, 3(e)**, Emirates

**The AO2 anchors:** special offers **encourage more passengers to fly with Emirates**; **many passengers use social media, so it is a good way to advertise to a large number of people**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **Emirates should increase its special offers.** The decisive fact is **what an airline is selling and how it is chosen: a seat on a route, compared by price against other airlines flying the same route.** **A special offer acts on that comparison directly — it changes the price the passenger sees at the moment of booking**, which is the moment the choice is made. **Social media reaches a very large audience, but the scheme's own objection cuts to the heart of it: "there is no control over social media and what is being said about Emirates by the users of social media."** **Emirates would be paying to be present on a platform where the conversation is not its own** — and for an airline, a single widely shared bad experience does more damage than a campaign does good. **However, "although special offers help, it is the service and the way passengers are treated that improves the airline's status"** — so the offer brings people onto the plane, but it does not make them come back. **I would still choose the special offers, on the condition that they are used to FILL seats that would otherwise fly empty — because a discount on a route that would have sold out is a discount given away for nothing, while an empty seat earns nothing at all.**

| Move | The answer |
|---|---|
| **1. Choice** | **The special offers** — first sentence |
| **2. AO2 + AO3** | Seats are **chosen on price against other airlines on the same route** → an offer acts at the point of booking |
| **3. Counter-arguments** | Social media → **no control over what users say**; offers → **service, not price, is what builds the airline's standing** |
| **4. Named condition** | ⭐ **Provided they fill seats that would otherwise fly empty** |

**Second acceptable chain:** social media **reaches passengers Emirates could never have afforded to advertise to individually** → and an airline's reputation travels far on it → **but that is exactly the problem: reputation travels equally far when it is damaged.**

> ⚠️ **The scheme's social-media counter-argument — "no control over social media and what is being said" — is the fixed AO4 for every social-media option in this tier** *(compare entry 204's sibling and the M&M material)*. **Memorise it: with social media you rent the audience and you do not own the conversation.**

---

## 191. PROMOTION — targeted online advertising vs e-newsletters

**Asked:** *"Option 1: targeted online advertising, sending information only to customers who have purchased furniture or signed up to the website · Option 2: e-newsletters, a cost-effective way of sending information to interested customers."* — **May–June 2021 P2, 2(f)**, NEXT

**The AO2 anchors:** targeted online advertising **reaches only those customers who have bought furniture or signed up**; e-newsletters are **a cost-effective way of sending information, and can include details of the wedding list service**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **NEXT should use the e-newsletters.** The decisive fact is **what is being promoted: the wedding list service, which is not a product on a shelf but a service that a customer has to be told about at a moment when they are planning a wedding.** **An e-newsletter goes to everyone who has asked to hear from NEXT, so it reaches customers as they are planning rather than only when they are shopping.** **Targeted online advertising narrows the audience the other way — and the narrowing is its weakness: "it does not reach all the customers of NEXT who might wish to purchase furniture."** **It is aimed at people who have already bought furniture or signed up, so a customer about to marry who has not yet bought anything from NEXT never sees it.** **However, the newsletter has its own limitation, stated plainly: "NEXT cannot be certain that all its customers who want to receive the wedding list service will read the newsletter, as there is no guarantee or way of checking that they have seen it."** **I would still choose the e-newsletter, on the condition that the subject line and the content make the wedding service the reason to open it — because with both methods the message reaching the inbox is only the first step, and the newsletter at least reaches the whole list.**

| Move | The answer |
|---|---|
| **1. Choice** | **The e-newsletters** — first sentence |
| **2. AO2 + AO3** | A wedding list is **a planning decision, not a shopping one** → the newsletter reaches the customer **before** they buy |
| **3. Counter-arguments** | Targeting → **misses customers who have not bought yet**; newsletter → **no guarantee it is read or opened** |
| **4. Named condition** | ⭐ **Provided the content makes the wedding service the reason to open it** |

**Second acceptable chain:** targeted advertising **wastes nothing, because every recipient has already bought furniture and is therefore a proven customer** → the click-through rate is higher → **but NEXT's growth depends on customers who have NOT bought yet, and targeting deliberately excludes them.**

> ⭐ **This pair is not really about cost or reach — it is about WHERE IN THE CUSTOMER'S LIFE each method speaks.** **Targeting catches the customer after they have started buying; a newsletter can catch them before.** **For a service tied to a life event — a wedding, a new baby, a move — the before matters more.**

---

## 192. PROMOTION — a new product range vs a price discount

**Asked:** *"Option 1: introduce a vegan range to address a new market · Option 2: give a 7.5% discount to draw more customers in at a quiet time."* — **June 2024 P1R, 2(f)**, Café Pinch

> **Note that these two options are not the same KIND of thing** — one changes the product, the other changes the price. **The question is really whether Café Pinch's problem is that it has nothing new to sell, or that not enough people are coming through the door at certain hours.**

**The AO2 anchors:** a vegan range **addresses a new market for the café**; a 7.5% discount **can draw more customers into the café at a time when it might not be busy**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **Café Pinch should introduce the vegan range.** The decisive fact is **what the discount can and cannot do: 7.5% off brings people in during a quiet period, but it brings in the SAME customers, and it brings them in cheaper.** **The café has not gained a market — it has given up margin on customers it already had.** **A vegan range reaches people who currently walk past, and the scheme's framing is that it "addresses a new market for the café".** **Once a vegan customer has been in and been served well, they can become a regular at full price** — which is a permanent addition to the customer base rather than a temporary one. **However, "whilst this might draw in more customers, Café Pinch needs to ensure it spends some time researching the products its customers want as well as what the competitors nearby are selling"** — a new range built on assumption rather than research may simply not sell. **And the discount has its own trap: "despite this leading to a potential increase in competitiveness, as Café Pinch is only small, they may not be able to cope with the increased demand at this time",** which would damage the service. **I would still choose the vegan range, on the condition that the research comes before the menu — because a new range that nobody wants has cost the café money, while a discount has only cost it margin on sales it would mostly have made anyway.**

| Move | The answer |
|---|---|
| **1. Choice** | **The vegan range** — first sentence |
| **2. AO2 + AO3** | A discount **brings back the same customers, cheaper**; a new range **adds customers permanently** |
| **3. Counter-arguments** | New range → **must be researched, or it will not sell**; discount → **small café may not cope with the demand it creates** |
| **4. Named condition** | ⭐ **Provided the research comes before the menu** |

**Second acceptable chain:** the discount **fills the café at the hours when it is empty, and an empty table earns nothing** → the margin lost is only lost on sales that were not going to happen → **but a 7.5% discount is small enough that customers may not notice it at all, in which case it costs margin and changes nothing.**

> ⚠️ **The scheme's caveat about a small business not coping with increased demand is easy to miss and easy to write.** **A promotional question for a SMALL business should always test the discount against capacity** — bringing in more customers than you can serve damages exactly the reputation the promotion was meant to build.

---

## 193. PROMOTION — an event vs leaflets

**Asked:** *"Option 1: hold an event to increase awareness of her flower shop · Option 2: hand out leaflets to passing tourists."* — **May 2023 P1R, 2(f)**, Aude Rose

**The AO2 anchors:** the event **will increase the awareness of her flower shop**; leaflets **can be handed out to passing tourists to draw them to the flower shop**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **Aude Rose should hold the event.** The decisive fact is **where the shop is and who is nearby: a flower shop in Paris with tourists passing it, in a city where flowers are bought on sight rather than researched.** **An event makes the shop itself memorable — flowers are a visual product, and an arrangement or a display people stop to look at is the closest thing to a sample the business has.** **Leaflets are the cheaper option, but the scheme's objection is precise and it is about cost as well as effect: "this would mean that someone would have to take time out of the shop to hand out the leaflets, or increase costs by paying someone to hand them out."** **In a small flower shop the person handing out leaflets is the person who serves customers**, so the true cost is the sales that did not happen inside. **However, "these events can be expensive to sponsor, so whilst sales may increase there is no guarantee profits will increase"** — an event is an upfront cost against an uncertain return. **I would still choose the event, on the condition that it can be built from stock the shop already holds — because Aude Rose's advantage is that its product is decorative, and an event that shows the arrangements costs materials rather than hiring a venue.**

| Move | The answer |
|---|---|
| **1. Choice** | **The event** — first sentence |
| **2. AO2 + AO3** | Flowers are **visual and bought on sight** → an event is **the closest thing to sampling the product** |
| **3. Counter-arguments** | Event → **expensive, no guarantee profit rises**; leaflets → **take the serving staff off the shop floor** |
| **4. Named condition** | ⭐ **Provided it is built from stock the shop already holds** |

**Second acceptable chain:** leaflets **reach tourists who are walking past anyway, so the audience is already in the right place** → distribution is targeted by geography alone → **but a leaflet is thrown away, whereas a display is remembered and photographed — and for a Paris flower shop, being photographed is free promotion.**

---

## 194. PROMOTION — social media vs coupons

**Asked:** *"Option 1: use social media to advertise its wide range of chairs worldwide · Option 2: use coupons giving 10% off bedroom furniture."* — **May 2023 P2, 2(f)**, IKEA

> **Read the two options again: one is untargeted reach, the other is a price cut dressed as a promotion.** **The question is whether IKEA's problem is that people do not know about the furniture, or that they know and are not yet buying.**

**The AO2 anchors:** social media **may reach out to a worldwide audience**; coupons give **10% off any bedroom furniture**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **IKEA should use the social media advertising.** The decisive fact is **what furniture buying needs: a customer who has decided to buy and is comparing ranges.** **A 10% coupon reduces the price of everything in the bedroom range for everyone who takes it — including every customer who was going to buy anyway, which is margin given away for nothing.** **Its weakness is stated in the scheme: "there is no guarantee that customers are going to use the coupon or even visit the store, so the advertising costs would be wasted", and the coupon is only printed and distributed at a cost before anyone uses it.** **Social media reaches the wide audience the scheme describes, and for IKEA the range itself is the advertisement** — chairs and bedroom furniture are visual, and a worldwide audience can see the product without going anywhere. **However, "not everybody uses social media so many people would not be aware of the advert to purchase furniture"** — the reach is wide but it is not everyone. **I would still choose social media, on the condition that the posts lead to a measurable route such as the website or the store locator — because reach with no path to purchase is not promotion, it is just attention.**

| Move | The answer |
|---|---|
| **1. Choice** | **The social media advertising** — first sentence |
| **2. AO2 + AO3** | Furniture is **visual** → the range advertises itself; a blanket coupon **discounts sales that would have happened** |
| **3. Counter-arguments** | Social media → **not everyone uses it**; coupons → **no guarantee they are used; distribution costs incurred first** |
| **4. Named condition** | ⭐ **Provided the posts lead to a measurable route to purchase** |

**Second acceptable chain:** a coupon **brings customers into the store, where they buy more than the discounted item** → the bedroom furniture is the bait and the basket is the profit → **but furniture is a considered purchase, and a 10% saving rarely decides one that was not going to happen.**

> ⭐ **The decisive comparison in this pair is between reach and margin.** **Coupons always work on people who were already going to buy; advertising works on people who were not.** **Ask which group the business needs, and the answer follows.**

---

## 195. PROMOTION — local sponsorship vs a wider exhibition

**Asked:** *"Option 1: sponsorship to increase awareness in the Kampong Glam area · Option 2: an exhibition that can make the business known to a wider market of artists."* — **Nov 2021 P1, 2(f)**, Artify Studio

**The AO2 anchors:** sponsorship **would increase awareness of Artify Studio to those in the Kampong Glam area**; the exhibition **can allow a business to become known to a wider market of artists**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **Artify Studio should sponsor locally.** The decisive fact is **the geography of the business: a studio in Kampong Glam sells to people who can physically come to it, and the local audience is the only one that can become customers.** **Becoming known to a wider market of artists is worth little if those artists are not nearby** — a wider reputation that cannot be converted into attendances is not revenue. **And the scheme's objection to the exhibition is the mirror of that: "it would mean taking time out of the business, and it may not bring in new customers or improve its image if the exhibition was poorly attended."** **An exhibition costs preparation time and can simply fail to draw anyone.** **However, "sponsorship can cost the business a lot depending on the size of the art show, and this could be a cost that the business cannot afford"** — so the local route is not free either. **I would still choose the local sponsorship, on the condition that the cost is capped at a show small enough that the studio's name is prominently on it — because being one of many names at a large event is not the same as being the sponsor the neighbourhood notices.**

| Move | The answer |
|---|---|
| **1. Choice** | **Local sponsorship** — first sentence |
| **2. AO2 + AO3** | A studio **sells to people who can come to it** → a wider reputation **cannot be converted** |
| **3. Counter-arguments** | Sponsorship → **may cost more than the business can afford**; exhibition → **takes time and may be poorly attended** |
| **4. Named condition** | ⭐ **Provided the cost is capped at a show small enough for the studio's name to be prominent** |

**Second acceptable chain:** the exhibition **connects Artify with other artists, which builds its standing in the art world** → that standing attracts students and teachers alike → **but standing is earned over years, while rent is paid monthly, so the local audience converts faster.**

> ⭐ **This is the "local versus wider" pair, and it appears whenever a business has a physical location its customers must visit.** **Reputation beyond the catchment area is not wrong — but it is not revenue either, and this tier always rewards the option that can be converted into a sale.**

---

## ✅ THE PROMOTION AND PRICING CLUSTERS — COMPLETE

**17 entries across 21 blocks.** Every promotion and pricing Justify question in the qualification is now carried:

| Option-pair family | Entry |
|---|---|
| Free presence vs paid sampling *(Loaf)* | **188** |
| Product expansion vs pop-up events *(Loaf)* | **189** |
| Special offers vs social media *(Emirates)* | **190** |
| Targeted advertising vs e-newsletters *(NEXT)* | **191** |
| New product vs discount *(Café Pinch)* | **192** |
| Event vs leaflets *(Aude Rose)* | **193** |
| Social media vs coupons *(IKEA)* | **194** |
| Local sponsorship vs wider exhibition *(Artify)* | **195** |
| Low opening price vs half-price add-on *(Nando's)* | **196** |
| Cost plus vs promotional pricing *(Tata · TUI · Huawei)* | **197** |
| Introductory price vs brand recognition *(NOF)* | **198** |
| Cost plus vs price skimming *(LEGO · Saha)* | **199** |
| Competition pricing vs cost plus *(AWG)* | **200** |
| Price matching vs discount *(Premier Inn)* | **201** |
| Free giveaway vs mass advertising *(Apple)* | **202** |
| Celebrity endorsement vs free giveaway *(Samsung)* | **203** |
| Charity sponsorship vs special offers *(Kraft Heinz · PPS)* | **204** |

> ### ⭐ THE ONE QUESTION THAT DECIDES EVERY PRICING AND PROMOTION ANSWER
> **Is the business trying to reach people who do not know it, or to convert people who do?**
>
> **Converting** → act at the point of decision: an offer, a coupon, a discounted add-on, a giveaway attached to the purchase. **The risk is that you discount sales you would have made anyway.**
> **Reaching** → act before the decision: social media, an event, an exhibition, a newsletter. **The risk is that you pay for delivery and cannot guarantee the result — *"you pay for the delivery, not for the result".***
>
> **Every AO4 in this cluster is one of those two risks.** **Name which one applies, and the evaluation writes itself.**

---
# BATCH 7d — 9-MARK JUSTIFY, PART 4 — MARKET RESEARCH AND MEASURING SUCCESS

**4 entries covering 9 blocks — every research and success-measurement Justify question in the qualification.**

> ### ⭐ THE RESEARCH CLUSTER IS THE SINGLE MOST REPEATED IN THE WHOLE TIER
> **Nine blocks, but only four underlying decisions.** The pair *primary research versus secondary research* appears **five separate times** — Lavender, Tata, NOF, TUI and Aude Rose — across **four different series spanning six years**, and the scheme's counter-arguments are recognisably the same every time:

| Method | Its strength | Its fixed weakness |
|---|---|---|
| **Questionnaires / primary** | **You ask the people you actually want to know about** — their views, their prices, their opinions | ⭐ *"People may not have time to fill it in"* / *"may not want to fill in the questionnaires whilst they are shopping"* / *"not filled in correctly"* |
| **Secondary research / the internet** | **Fast, cheap, wide — "much easier to collate", "a large selection of websites"** | ⭐ *"You could spend a lot of time looking at information which is not relevant … or is out of date"* / *"gives no specific information on the demand … by its existing customers"* |

---

## 196. PRICING — an introductory/low price vs another tactic

**Asked:** *"Option 1: charge a low price for its meals when it first opens a new restaurant · Option 2: offer a half-priced drink when a person orders a meal on their first visit."* — **June 2026 P2, 2(f)**, Nando's

> **Both options are promotional pricing — the difference is what is discounted, not whether.** **Option 1 cuts the price of the MAIN product; option 2 keeps the meal price intact and gives away something beside it.** That distinction is what the answer turns on.

**The AO2 anchors:** Nando's **may charge a low price for its meals when it first opens**; or it **could offer a half-priced drink when a person orders a meal on their first visit.**

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **Nando's should offer the half-priced drink rather than discounting the meals.** The decisive fact is **what the two options do to the price the customer learns.** **Opening with low meal prices teaches customers what a Nando's meal is worth — and the scheme warns that "some customers may associate a low price with low-quality food and may not visit the new restaurant".** **Once that impression is set, raising the price to its normal level reads as a price rise rather than as a return to normal.** **The half-priced drink avoids that entirely, because the meal keeps its real price and the customer has simply been given something extra on the first visit.** **However, the drink offer has its own weakness: "customers may not continue dining at Nando's once the promotional offer ends"** — because the incentive was the drink, not the restaurant. **I would still choose the half-priced drink, on the condition that the first visit is good enough to earn the second — because a chicken restaurant lives on repeat custom, and the offer only works if what it is promoting is worth coming back for.**

| Move | The answer |
|---|---|
| **1. Choice** | **The half-priced drink** — first sentence |
| **2. AO2 + AO3** | Discounting meals **teaches a low price → reads as "cheap quality" → then a rise reads as a price rise**; the drink offer **protects the meal's real price** |
| **3. Counter-arguments** | Low meal price → **low-quality association**; drink offer → **customers may not return once it ends** |
| **4. Named condition** | ⭐ **Provided the first visit earns the second** — because this business runs on repeat custom |

**Second acceptable chain:** a low opening price **fills the restaurant and builds a reputation through word of mouth** → a full restaurant is its own advertisement → **but the customers who arrive are price-sensitive ones, and they are the hardest group to raise prices on.**

> ⭐ **The comparison in this question is between discounting the PRODUCT and discounting the ADD-ON.** **Protecting the main price preserves what customers think the product is worth** — that is the whole argument, and it transfers to any pair shaped this way.

---

## 197. PRICING — cost plus vs promotional or lower pricing

**Asked:** *"Option 1: cost plus pricing · Option 2: promotional pricing."* — **May–June 2019 P2, 2(f)**, Tata Motor Company ($£$*new vehicles*)
**Also asked:** *"Option 1: a price comparable to other travel agents · Option 2: a cheaper price to attract customers from rivals."* — **June 2024 P2, 2(f)**, TUI
**Also asked:** *"Option 1: a realistic price · Option 2: a cheaper price to switch customers from their present brand."* — **Nov 2021 P2, 3(e)**, Huawei

> **Three papers, three businesses, the same decision shape: a price that covers the cost against a price that wins the sale.** **The scheme's counter-arguments are near-identical every time**, which is why one entry answers all three.

**The AO2 anchors:** with cost plus **the company knows the cost of making the vehicle has been covered**; promotional pricing **is a good strategy for selling new vehicles**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **Tata should use cost plus pricing for its new vehicles.** The decisive fact is **what is being sold: a vehicle is a high-cost product, and a single model sold below its manufacturing cost loses money that no volume of sales recovers unless the price is above cost.** **Cost plus guarantees the cost is covered on every unit** — and **that certainty is what allows a manufacturer to plan production, order components and pay a workforce before a single car is sold.** **Promotional pricing would generate sales faster, and for a new model that matters, because dealers want cars that move.** **However, "even though the sales may be higher, the profit per vehicle will be lower"** — and on a vehicle, **the profit per unit is where the whole business model sits.** **However, the scheme also cautions that cost plus "does not guarantee that sales are going to be made, especially if a competitor is cheaper, therefore selling more vehicles"** — so the price is safe but the volume is not. **I would still choose cost plus, on the condition that the price is checked against the closest competitor's model before launch — because a price that covers the cost of a car nobody buys covers nothing at all.**

| Move | The answer |
|---|---|
| **1. Choice** | **Cost plus** — first sentence |
| **2. AO2 + AO3** | A vehicle is **high-cost per unit** → cost plus **protects the margin on every car** → funds components and wages **before any sale** |
| **3. Counter-arguments** | Promotional pricing → **lower profit per vehicle**; cost plus → **may sell nothing if a rival is cheaper** |
| **4. Named condition** | ⭐ **Provided the price is checked against the closest competitor before launch** |

**Second acceptable chain (Huawei or TUI):** a **cheaper price switches customers from the brand they currently own** → the switch is the hardest thing to buy in a mature market → **but "promotional pricing may generate sales for the length of the promotion, and once the price reverts to normal it may reduce sales"** — so the switch has to be made permanent by the product, not the price.

> ⚠️ **The sentence *"once the price reverts to normal, sales may reduce"* appears in the scheme for TUI and for Huawei, word for word.** **It is the single most repeated counter-argument in the pricing cluster — use it every time promotional pricing appears.**

---

## 198. PRICING — an introductory price vs relying on brand recognition

**Asked:** *"Option 1: offer an introductory price to entice shoppers to try the popcorn · Option 2: rely on customers recognising the farm's name when comparing to its competition."* — **May–June 2021 P1, 2(f)**, NOF

> **This is the only pair in the tier where one option is not a price at all.** **Option 2 is the decision to charge a normal price and let the brand do the work** — so the question is really: **is the brand strong enough to skip the discount?**

**The AO2 anchors:** an introductory price **could entice shoppers in the farm shop to try the popcorn**; customers **might recognise the farm's name so will buy the popcorn when comparing to its competition**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **NOF should use the introductory price.** The decisive fact is **what the popcorn is: a product the farm has never sold before, sitting on a shelf beside brands that shoppers already know.** **NOF's name is recognised for the FARM — for its honey and its rooms — and "as they do not have an established brand of popcorn, customers may choose to buy a more popular branded popcorn they know".** **Recognition of the business does not transfer automatically to a new product category**, which is the assumption option 2 makes. **An introductory price gives the shopper a reason to take the risk on the unfamiliar bag**, and **trying it is the only thing that can convert the farm's reputation into popcorn sales.** **However, "the profit on each bag of popcorn will be low even though sales may increase, so in the short term profits might suffer"** — and that is a real cost, paid before any benefit arrives. **I would still choose the introductory price, on the condition that it is time-limited to the season the popcorn launches in — because a permanent low price on popcorn would simply become the price of popcorn, while a temporary one ends once the farm's reputation has done the work.**

| Move | The answer |
|---|---|
| **1. Choice** | **The introductory price** — first sentence |
| **2. AO2 + AO3** | The farm's **name is not a popcorn brand** → recognition **does not transfer to a new category** → a reason to try is needed |
| **3. Counter-arguments** | Introductory price → **low profit per bag, short-term profits suffer**; brand route → **customers may choose a known brand instead** |
| **4. Named condition** | ⭐ **Provided it is time-limited to the launch season** |

**Second acceptable chain:** an introductory price **brings shoppers into the farm shop where the honey and rooms are also sold** → **the loss on the popcorn is recovered on the rest of the basket** → which is why a farm shop can afford a loss-leader a standalone popcorn brand could not.

> ⭐ **The idea to take away: brand recognition is SEGMENT-SPECIFIC.** *"Customers know the farm"* is not *"customers know the popcorn"*. **Wherever a question asks you to rely on an existing reputation to sell something new, that gap is your argument.**

---

## 199. PRICING — cost plus vs price skimming

**Asked:** *"Option 1: cost plus pricing · Option 2: price skimming on release."* — **June 2022 P2, 2(f)**, LEGO ($£$*the new Princess Leia toy*)
**Also asked:** *"Option 1: price skimming to charge a high price for its new home robots · Option 2: cost plus to ensure all costs are considered."* — **Nov 2024 P1, 3(e)**, Saha

> **The two questions put the options in opposite orders — and they point at OPPOSITE answers, which is the point.** LEGO sells **a collectible character toy**; Saha sells **a household robot**. **Same pair, different product, different decision.**

**The AO2 anchors (LEGO):** cost plus is **easy to apply and LEGO will know the cost of manufacturing the Princess Leia toy is covered when sold**; price skimming means **the toy is sold at a high price when it is released**.
**The AO2 anchors (Saha):** skimming **enables Saha to charge a high price for its new home robots**; cost plus **ensures all costs such as metal and assembly are considered**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **LEGO should use price skimming on the Princess Leia toy.** The decisive fact is **the product: a licensed character toy launched to a fan base that wants it on release day, before anyone else has it.** **That audience will pay a premium for being first, and the premium is only available in the weeks around launch** — after that, the same toy sits in the same shops as every other set. **Price skimming takes the money that willingness to pay creates, while it exists.** **Cost plus would leave that on the table, because as the scheme notes it "does not account for what the customer is willing to pay" — it prices from LEGO's costs, not from the customer's desire, so a toy fans would have paid double for goes out at cost plus a fixed markup.** **However, "this strategy might limit the number of potential customers wanting to buy the product as the price is too high"** — and a licensed toy that sells too few units **may not justify the licence fee at all.** **I would still choose skimming, on the condition that the price is cut deliberately once the launch window closes — because LEGO has a fan base that will wait if the price never falls, and a collector's market is worth less than a mass market over the life of the set.**

| Move | The answer |
|---|---|
| **1. Choice** | **Price skimming** — first sentence |
| **2. AO2 + AO3** | **Launch-window willingness to pay exists only briefly** → skim while it does |
| **3. Counter-arguments** | Skimming → **may limit customers because the price is too high**; cost plus → **does not account for what the customer will pay** |
| **4. Named condition** | ⭐ **Provided the price is cut once the launch window closes** |

**The Saha answer runs the other way — and the reason is the product.** Saha's robots are **a metal-and-assembly manufactured good sold into homes, against named rivals (Zoox, Vention)**, and the scheme warns that **"if the price is considered too high for its target audience it may lose sales to competitors"**. **A household robot is not a collectible: it competes on price with alternatives, so cost plus — which "ensures all costs such as metal and assembly are considered" — is the safer route**, with the caveat that **it may "limit revenue/profit" because it ignores willingness to pay.**

> ⭐ **The transferable test for skimming: is there a group who will pay a premium to be FIRST?** **Characters, launches, new technology that nobody else has — yes. A commodity sold against named rivals — no.** **Notice how the scheme's own counter-argument ("may limit the number of potential customers as the price is too high") is the SAME in both papers, and it is decisive in one and survivable in the other.**

---

## 200. PRICING — competition pricing vs cost plus

**Asked:** *"Option 1: competition pricing at similar prices to other clothing retailers · Option 2: cost plus with a markup for profit."* — **Nov 2023 P1, 3(e)**, AWG ($£$*Icelandic jumpers made from sustainable materials*)

> **This is the pricing question the bank most wants you to see, because the correct answer turns on a single fact buried in the case: the manufacturing cost is HIGH.**

**The AO2 anchors:** competition pricing would see AWG **selling clothing at similar prices to other clothing retailers**; cost plus would **calculate the costs of making the jumpers and add a markup for profit**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **AWG should use cost plus pricing.** The decisive fact is **what AWG makes its jumpers from: sustainable materials, which are more expensive than the conventional ones its competitors use.** **Competition pricing means matching other clothing retailers — but those retailers are not paying AWG's material costs, so a price that suits them may be below AWG's own cost of production.** **The scheme states it plainly: "as AWG use sustainable materials in its jumpers, the manufacturing cost of the clothing may be high, which means selling at a competitive price may not be feasible."** **Cost plus starts from AWG's real costs and adds a markup, so the business cannot accidentally sell below what it spent** — which is the minimum any business needs before it can think about profit. **However, cost plus removes the market from the decision: it "does not account for what the customer is willing to pay, and AWG could be losing out on possible increased revenue and profits."** **I would still choose cost plus, on the condition that AWG makes the sustainability itself the reason to pay the higher price — because the materials cost more, and if customers do not value the difference, AWG is paying a premium for a feature nobody is buying.**

| Move | The answer |
|---|---|
| **1. Choice** | **Cost plus** — first sentence |
| **2. AO2 + AO3** | **Sustainable materials cost more than rivals'** → matching the competition **may price below cost** |
| **3. Counter-arguments** | Cost plus → **ignores what the customer will pay, losing potential revenue**; competition pricing → **may not be feasible at AWG's cost base** |
| **4. Named condition** | ⭐ **Provided the sustainability is made the reason to pay more** |

**Second acceptable chain:** competition pricing **removes price as a reason for a shopper to choose a rival** → AWG competes on the product instead → **but only if the rival's price is above AWG's cost, which is exactly what the sustainable materials prevent.**

> ⭐ **This entry is the proof of the bank's central claim about this tier: the OPTION PAIR does not determine the answer — the CASE does.** **Cost plus is the "safe but unimaginative" option here; on Nando's or Huawei it would be the wrong choice.** **Read the case fact that makes the difference, then decide.**

---

## 201. PRICING — price matching vs a discount

**Asked:** *"Option 1: match the price of competitors for its rooms · Option 2: offer a discount on a 3-night stay."* — **Nov 2024 P2, 2(f)**, Premier Inn

> **Both options compete on price, so the difference is WHAT KIND of customer each attracts.** Matching is **permanent and open to everyone**; a discount on three nights is **temporary and aimed at a specific booking.**

**The AO2 anchors:** Premier Inn **will match the price of competitors for its rooms**; or it **could offer a discount on the price of a 3-night stay**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **Premier Inn should match competitors' prices.** The decisive fact is **what a hotel sells and when it is chosen: a room is booked against other hotels on a screen, and price is the first thing a guest compares.** **Matching removes price as the reason a guest books elsewhere, so the decision falls to the hotel's facilities and location — which is where Premier Inn wants to compete, because that is what it has invested in.** **It also applies to every booking rather than to a chosen few, so it defends the whole business rather than one slice of it.** **The 3-night discount does something different and narrower: it raises bookings among guests already planning a longer stay, and "even though the bookings may be higher there is no guarantee that the profit will be the same or higher"** — because the discount comes straight off the margin on the nights sold. **However, matching has its own limitation, and the scheme names it: "there is no guarantee that customers will book with Premier Inn as they may prefer the facilities at another hotel".** **I would still choose price matching, on the condition that it is applied only to like-for-like rooms in the same location — because matching a rival's price for a hotel with a pool, when Premier Inn has none, gives away margin to win a comparison it will lose anyway.**

| Move | The answer |
|---|---|
| **1. Choice** | **Price matching** — first sentence |
| **2. AO2 + AO3** | Hotels are **compared on a screen** → matching **removes price as the reason to go elsewhere** and applies to **all** bookings |
| **3. Counter-arguments** | Matching → **guests may prefer another hotel's facilities anyway**; discount → **bookings up but profit may not be** |
| **4. Named condition** | ⭐ **Provided it applies to like-for-like rooms in the same location** |

**Second acceptable chain:** the 3-night discount **lifts occupancy midweek, when hotels are emptiest** → an empty room earns nothing, so **any price is better than none** → **whereas matching every night gives away margin on nights that would have sold at full price anyway.**

> ⭐ **The distinction that wins this question: does the tactic apply to ALL sales or TARGETED ones?** **A blanket price change protects volume but permanently lowers margin; a targeted discount raises volume in the emptiest part of the business and leaves the rest untouched.** **Say which one the case's problem needs.**

---

## 202. PROMOTION — a free giveaway vs mass advertising

**Asked:** *"Option 1: a TV advert promoting its phones and laptops · Option 2: free headphones with a laptop."* — **June 2026 P2R, 2(f)**, Apple

**The AO2 anchors:** a TV advert **will target a large audience**; the free headphones **may encourage some young people to buy a laptop**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **Apple should use the free headphones.** The decisive fact is **who the laptop is being sold to: younger buyers, and the scheme warns that "many people, especially young people, no longer listen to or have any interest in TV advertisements", so a TV campaign "may not be cost effective and reach Apple's target audience".** **A television advert pays for a very large audience and delivers a very small share of it — and the share Apple needs is the one that is not watching.** **The headphones do the opposite: they reach nobody who is not already looking at the laptop, and they create the reason to complete the purchase at the moment of decision.** **However, "students may not be interested in promotional products, and the offer may not be a sufficiently good deal to persuade them to buy" — particularly as they may prefer cheaper alternatives to an Apple laptop in the first place.** **I would still choose the headphones, on the condition that they are a product this buyer actually wants — because a free accessory nobody values does not shift a laptop, it just gives away stock and reduces the effective price for people who would have bought anyway.**

| Move | The answer |
|---|---|
| **1. Choice** | **The free headphones** — first sentence |
| **2. AO2 + AO3** | **Young buyers do not watch TV ads** → mass reach is wasted; headphones **act at the point of decision** |
| **3. Counter-arguments** | TV → **not cost-effective for this audience**; giveaway → **students may not value it or may buy cheaper anyway** |
| **4. Named condition** | ⭐ **Provided it is an accessory this buyer actually wants** |

**Second acceptable chain:** the TV advert **builds the brand beyond the people buying this year** → brand advertising works over years, while a giveaway only works in the week it runs → **but a laptop is a considered purchase bought on specification and price, so brand awareness alone does not close it.**

> ⚠️ **The scheme's counter-argument for mass advertising is THE SAME POINT that makes it strong: the large audience.** *"Target a large audience"* is not a benefit if **the audience is not the customer.** **That reversal — a strength that is a weakness for this particular business — is worth 3 AO4 marks, and it appears in this cluster more than once.**

---

## 203. PROMOTION — paid celebrity endorsement vs a free giveaway

**Asked:** *"Option 1: pay fees to a celebrity for using its smartphones · Option 2: free game applications to encourage young people to buy a phone."* — **Nov 2025 P2, 2(f)**, Samsung

> **This is the closest pair in the tier to entry 206 — and the difference is instructive.** **Both pair a paid broadcast against a free gift; here the paid channel is a CELEBRITY rather than a TV slot.**

**The AO2 anchors:** Samsung **could pay fees to a celebrity for using its smartphones as a way of getting publicity**; **free game applications may encourage young people to buy a phone.**

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **Samsung should use the free game applications.** The decisive fact is **the age of the buyer: young people choose a phone largely on what it can do, and games are what it does.** **Free applications make the phone worth more at the moment of choosing, and that value is in the product itself rather than in an image attached to it.** **A celebrity endorsement buys attention and association, which is powerful for a brand that needs to be seen as desirable** — but **it is a fee paid to a person, and the association disappears the moment the contract ends or the celebrity moves to a rival's product.** **However, the games have their own limitation: they are free to the customer only if Samsung pays the developer, so the giveaway is a cost on every phone sold** — and **it narrows the margin on the units it is most trying to sell.** **I would still choose the games, on the condition that the phones they are bundled with are the mid-range models younger buyers actually buy — because a giveaway attached to a flagship nobody in that group can afford is a discount given to people who did not need persuading.**

| Move | The answer |
|---|---|
| **1. Choice** | **The free games** — first sentence |
| **2. AO2 + AO3** | **Young buyers choose on capability** → games make the phone worth more **in the product** |
| **3. Counter-arguments** | Celebrity → **fee paid, association temporary**; games → **cost on every unit, narrowing margin** |
| **4. Named condition** | ⭐ **Provided it is attached to the models this buyer can afford** |

**Second acceptable chain:** a celebrity endorsement **generates press coverage and social media attention that is not paid for directly** → the reach goes far beyond the advert → **but it is the celebrity the audience remembers, not the specification, which does not help a phone competing on features.**

> ⭐ **The celebrity's AO4 is worth learning as a fixed item: you PAY a fee, and the association ENDS.** **The scheme's whole objection to buying attention is that you rent it.** **The same logic applies to sponsorship (entry 208) and to TV advertising (entry 206).**

---

## 204. PROMOTION — sponsoring a charity or event vs special offers

**Asked:** *"Option 1: sponsor a local charity such as Animal Rescue · Option 2: increase special offers on its sauces."* — **Nov 2023 P2, 2(f)**, Kraft Heinz
**Also asked:** *"Option 1: free trial of a new dog food brand · Option 2: sponsor a local dog show."* — **June 2024 P1, 2(f)**, PPS

**The AO2 anchors (Kraft Heinz):** sponsoring **gains publicity and involvement in the local community**; special offers **may encourage more people to purchase its products**.
**The AO2 anchors (PPS):** a free trial **will appeal to dog owners who regularly purchase dog food**; sponsoring a dog show **will promote products such as dog collars**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **Kraft Heinz should increase its special offers.** The decisive fact is **what the money has to do: move tins of beans and bottles of sauce off shelves.** **A special offer works directly on that decision, because the customer is already standing in front of the product with the price in view** — the offer changes what they pay at the moment they were going to choose. **Sponsoring Animal Rescue buys something real but different: publicity and standing in the local community.** **The problem is the link, and the scheme states it: "there is no guarantee that because an event has been sponsored by Kraft Heinz people will purchase its products."** **Publicity is not the same as a reason to buy, and a shopper who has seen the company's name on a rescue campaign still chooses the sauce on price and taste.** **However, "special offers may help increase sales but they can cost Kraft Heinz additional costs which might not be recovered"** — so the offer is a straight trade of margin for volume. **I would still choose the special offers, on the condition that they are timed to the period when the products are actually competed for — because a discount on a product the shopper was always going to buy is simply a price cut, and it is permanent once customers are used to it.**

| Move | The answer |
|---|---|
| **1. Choice** | **The special offers** — first sentence |
| **2. AO2 + AO3** | Offers act **at the shelf, where the decision is made** |
| **3. Counter-arguments** | Sponsorship → **no guarantee people will buy**; offers → **cost that may not be recovered** |
| **4. Named condition** | ⭐ **Provided they are timed to when the product is genuinely being contended for** |

**Second acceptable chain (PPS):** sponsoring a **dog show** puts the products in front of **owners who already buy dog food and collars** — a targeted audience at a moment they are thinking about their dog → **but "it does cost to sponsor an event so PPS would need to incur cost upfront before they gain an increase in revenue", which a small business may not be able to carry.**

> ⚠️ **Note which way this one goes, and why: the scheme's own formulation makes the sponsorship link weak — "there is no guarantee … that people will purchase its products".** **When a counter-argument is printed in the scheme, it is the correct ground to argue on.** **This is the opposite conclusion from entry 186 (AWG), where venture capital beat franchising — because there the option being rejected damaged the BRAND, and here the option being rejected is merely indirect.**

---

## 205. MARKET RESEARCH — primary research versus secondary research

**Asked five times in six years:**
- *"Option 1: questionnaires to existing and potential customers face to face · Option 2: the internet, to gain wider sources of information about the area it wishes to expand into."* — **May–June 2019 P1R, 3(e)**, Lavender
- *"Option 1: obtain the information directly from the people about the cars they want and the price they are prepared to pay · Option 2: secondary research, easier to collate from other car manufacturing websites and reports."* — **May–June 2019 P2, 3(e)**, Tata Motor Company
- *"Option 1: questionnaires, approaching potential customers face to face to see what will attract them to visit the farm · Option 2: view a large selection of websites to look at other farms."* — **May–June 2021 P1, 3(e)**, NOF
- *"Option 1: the internet, to view a wide variety of customers' comments about their experiences · Option 2: customers complete a form at their leisure, giving details of the experiences they received."* — **June 2024 P2, 3(e)**, TUI
- *"Option 1: hand out questionnaires to customers that visit the shop · Option 2: using the internet to research new flower trends."* — **May 2023 P1R, 3(e)**, Aude Rose

> **Note how the same decision is written five different ways, and that the option ORDER changes.** TUI's question puts the internet first. **Read the options, not the pattern.**

**The AO2 anchors (Lavender):** primary research **allows Lavender to approach existing and potential customers face to face**; secondary research **allows it to gain wider sources of information about the area it wishes to expand into**.
**The AO2 anchors (Aude Rose):** questionnaires give **feedback straight away from customers buying flowers in the shop**; the internet lets it **view a large selection of flower-based websites**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]` *(written on Aude Rose; the structure transfers, the case facts do not)*
> **Aude Rose should use the questionnaires.** The decisive fact is **what the business is trying to find out and from whom: whether customers will buy a new range, which only its own customers can answer.** **Its customers are standing in the shop, buying flowers** — the scheme's own point is that this gives **"feedback straight away from customers when buying flowers"**, so the research and the customers are in the same place at the same time, at no travel cost. **The internet reaches a vast amount of flower information, but none of it is about Aude Rose's customers.** **The scheme's objection is decisive here: "whilst this research can give information about up-and-coming trends, it gives no specific information on the demand for the new trends by its existing customers, so could be a waste of time."** **Trends that exist in general may not be wanted by the people who actually walk into the shop.** **However, the questionnaire has its own weakness and it is a serious one: "customers may not know about the new trends, so cannot give any constructive feedback on the purpose of the research being conducted."** **Asking someone about something they have never considered produces an opinion, not evidence.** **I would still choose the questionnaires, on the condition that they are shown the new range rather than asked to imagine it — because the method only works if the customer has something real to react to.**

| Move | The answer |
|---|---|
| **1. Choice** | **The questionnaires** — first sentence |
| **2. AO2 + AO3** | The customers are **in the shop, buying flowers** → **immediate, relevant feedback** on **whether they will buy the new range** |
| **3. Counter-arguments** | Internet → **gives trends but nothing about this shop's customers → may waste time**; questionnaires → **customers may know nothing about the trends** |
| **4. Named condition** | ⭐ **Provided customers are shown the range rather than asked to imagine it** |

**The same decision, five different named conditions — and this is the entry to study if you want to see what a named condition really is:**

| Business | What the research is FOR | So the condition is |
|---|---|---|
| **Lavender** | expanding into **other parts of Malaysia** | *provided the questions are pitched at customers in the area being considered, not the ones already served* |
| **Tata** | designing and **pricing the next cars** | *provided the sample covers the buyers of the segment the new car is aimed at* |
| **NOF** | **what would attract visitors to the farm** | *provided it is asked of people who have never visited — existing customers already know* |
| **TUI** | **improving a day trip** | *provided the form is handed out on the trip itself, while the experience is fresh* |
| **Aude Rose** | a **new range** | *provided the customers are shown the range* |

> ⭐ **Five blocks, one decision, five different conditions — and not one of them could be pasted onto another.** **That is the proof that the named condition is not a phrase to memorise, it is a fact to find.** **Ask: what is this research FOR, and what would have to be true for it to actually work?**

**Second acceptable chain for any of the five:** secondary research **costs almost nothing and can be done today** → for a business with **no budget for research**, something is better than nothing → **but if the trend it reveals is not what this business's customers want, the whole exercise is wasted — and secondary research cannot tell you that.**

---

## 206. MARKET RESEARCH — questionnaires versus focus groups

**Asked:** *"Option 1: questionnaires, easy for passengers to complete · Option 2: focus groups, allowing passengers to give their opinions face-to-face."* — **May–June 2020 P2, 2(f)**, Emirates
**Also asked:** *"Option 1: hand out questionnaires to customers that visit the shops · Option 2: hold focus group meetings with parents and observe children playing with the new toys."* — **June 2022 P1, 3(e)**, TBTS

> **Both methods are primary research — so the usual "primary beats secondary" argument does not apply here.** **The comparison is depth against coverage, and which of the two the business actually needs.**

**The AO2 anchors (Emirates):** questionnaires are **easy for passengers to complete**; focus groups **allow passengers to give their opinions face-to-face**.
**The AO2 anchors (TBTS):** questionnaires **get feedback directly from the customers who buy the toys on behalf of children**; focus groups **let TBTS observe children playing with the new range**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]` *(written on TBTS)*
> **TBTS should hold the focus groups.** The decisive fact is **who the real user of the product is and who does the buying.** **A toy is bought by a parent and used by a child — and a parent cannot accurately describe what a child will pick up, play with and want again.** **A focus group lets TBTS "observe children playing with the new range of toys", which produces the one thing a questionnaire never can: evidence of what the child actually does.** **The questionnaire only collects what the parent says.** **However, "the responses from the children may not be valid as they are in a new setting and may find other things more interesting"** — children in a strange room behave differently from children at home, so **observed behaviour is not automatically real behaviour.** **And the questionnaire's weakness compounds the problem: "as TBTS have shops in busy locations like airports, people may not have the time to fill in the questionnaires or may rush it, therefore not giving them accurate feedback."** **I would still choose the focus groups, on the condition that the toy is taken home and observed there for a week — because a focus group that tells you what a child does in an unfamiliar room has replaced one uncertain answer with another.**

| Move | The answer |
|---|---|
| **1. Choice** | **The focus groups** — first sentence |
| **2. AO2 + AO3** | **Parents buy, children use** → observing children **produces evidence a parent cannot describe** |
| **3. Counter-arguments** | Children **behave differently in a new setting**; questionnaires at airport shops **are rushed and inaccurate** |
| **4. Named condition** | ⭐ **Provided the toy is taken home and observed there** |

**On Emirates the balance tips the other way, and the reason is the population.** **Focus groups can only include "a certain number of passengers and therefore might not give a true cross section of all classes of passengers"** — and an airline needs to know about **first class and economy, long-haul and short-haul**. **A small group cannot represent that spread.** So for Emirates: **questionnaires, on the condition that they are handed out to a genuinely mixed set of passengers across cabin classes** — with the scheme's warning that **"often they are not filled in correctly and do not give the information about flights needed"**, which is exactly what a badly designed form produces.

> ⭐ **The deciding question for this pair: does the business need DEPTH on a few people, or a CROSS-SECTION of many?** **A product decision about how something will be used → depth. A service decision about a whole customer base → cross-section.** **TBTS is testing a toy; Emirates is testing an airline.**

---

## 207. MARKET RESEARCH — questionnaires versus tasting the product

**Asked:** *"Option 1: use questionnaires to collect customer views on the new toppings · Option 2: offer free samples of new toppings and ask customers for their opinions."* — **June 2026 P1R, 3(e)**, Spud Bros

> **This pair is the newest in the qualification and the most literal: ask people what they think, or let them try it and then ask.** **The second option is still research — it is a taste test — which is why the scheme puts it in the research section.**

**The AO2 anchors:** questionnaires **allow people to provide quantitative and qualitative feedback on the new toppings**; free samples **may encourage more people to taste the food**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **Spud Bros should offer the free samples.** The decisive fact is **what is being researched: taste — and taste cannot be reported, it has to be experienced.** **A customer who has not eaten the new topping is guessing, and a questionnaire then records that guess as data.** **Free samples "encourage more people to taste the food", so the opinion collected is a reaction to the actual product rather than to a description of it.** **The questionnaire does one thing the samples cannot: it collects "quantitative and qualitative feedback", meaning the answers can be counted and the reasons behind them captured — which matters if the brothers need to compare three new toppings against each other.** **However, "many people do not have the time to fill in a questionnaire and the response rate may be low for Spud Bros"** — a questionnaire with too few responses decides nothing. **However, giving free samples "will be costly" and will "take time to record participants' responses", which for a small family business is money and hours it cannot easily spare.** **I would still choose the samples, on the condition that the customers are asked their view immediately after tasting, before they walk away — because the taste is the research, and the opinion only has value while it is fresh.**

| Move | The answer |
|---|---|
| **1. Choice** | **The free samples** — first sentence |
| **2. AO2 + AO3** | **Taste must be experienced, not described** → samples produce **real reactions, not guesses** |
| **3. Counter-arguments** | Questionnaires → **low response rate**; samples → **costly for a small business, and recording responses takes time** |
| **4. Named condition** | ⭐ **Provided the opinion is captured immediately after tasting** |

**Second acceptable chain:** a free sample **is also a promotion, not just research** → the customer tastes, likes, and buys → **so the cost of the research is partly recovered in sales on the day**, which no questionnaire can do.

> ⭐ **The transferable test: is the thing being researched something the customer can REPORT, or something they can only EXPERIENCE?** **Price sensitivity, brand awareness and past behaviour can be asked about. Taste, feel, ease of use and enjoyment have to be tried.** **Match the method to the senses.**

---

## 208. MEASURING SUCCESS — customer satisfaction versus profit

**Asked:** *"Option 1: customer satisfaction · Option 2: profit."* — **June 2025 P1R, 2(f)**, CCT

> **This is the only 9-mark question in the qualification about MEASURING SUCCESS rather than doing something.** **Note that both measures are legitimate — the question is which tells CCT more about whether the business is working.**

**The AO2 anchors:** customer satisfaction **will indicate how happy customers are with the level of the bicycle touring service**; a high level of profit **will show CCT they can provide the tours at a cost lower than the price they are selling them for**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **CCT should measure customer satisfaction.** The decisive fact is **what the business is: a bicycle touring company whose product IS the experience of the tour.** **Satisfaction measures the thing the customer actually bought** — how happy they were with the tour — and **for a tour business, the customer's own verdict is not a proxy for quality, it is the quality.** **It also predicts the future rather than reporting the past: a satisfied customer recommends the tours, which produces the bookings CCT has not made yet.** **Profit, by contrast, is a lagging measure.** It tells CCT **that the pricing has worked over a period**, but **"profit can be affected by short-term fluctuations in the market, making it difficult to measure success over a longer period of time"** — a good season of weather can flatter a profit figure while the tours themselves are being run badly. **However, "it is difficult to measure customer satisfaction accurately as it relies on customers leaving reviews and providing honest feedback of their experiences"** — the measure depends on the customer bothering, and satisfied people are the least likely to bother. **I would still choose customer satisfaction, on the condition that the feedback is collected from every tour rather than waiting for reviews — because the customers who never write a review are as much part of the verdict as the ones who do.**

| Move | The answer |
|---|---|
| **1. Choice** | **Customer satisfaction** — first sentence |
| **2. AO2 + AO3** | **The experience IS the product** → satisfaction measures what was bought, **and predicts future bookings** |
| **3. Counter-arguments** | Satisfaction → **hard to measure; relies on reviews and honesty**; profit → **distorted by short-term market fluctuations** |
| **4. Named condition** | ⭐ **Provided feedback comes from every tour, not only from reviews** |

**Second acceptable chain:** profit **is the measure the owner can act on directly**, because it is a number in the accounts rather than an opinion → **but a tour business that is profitable this season and disliked by its customers will not be profitable next season.**

> ⚠️ **The profit caveat in this scheme — "affected by short-term fluctuations in the market" — is a genuinely unusual argument and worth remembering.** **It says profit is not wrong, it is UNRELIABLE as a long-term measure** — which is a more sophisticated point than "profit matters less than customers", and it is where the AO4 marks are.

---

## ✅ THE RESEARCH AND SUCCESS-MEASUREMENT CLUSTER — COMPLETE

**4 entries covering 9 blocks.** Nine blocks in the tier are research or success measurement, and they reduce to **four decisions**:

| Decision | Blocks | Entry |
|---|---|---|
| **Primary vs secondary research** | **5** — Lavender · Tata · NOF · TUI · Aude Rose | **205** |
| **Questionnaires vs focus groups** | **2** — Emirates · TBTS | **206** |
| **Questionnaires vs tasting the product** | **1** — Spud Bros | **207** |
| **Customer satisfaction vs profit** | **1** — CCT | **208** |

> ### ⭐ THE THREE QUESTIONS THAT DECIDE ANY RESEARCH CHOICE
> **1. WHO can answer this?** — Not "who is available". **Aude Rose needs its own customers, NOF needs people who have never visited, TBTS needs the child rather than the parent.** **If the wrong people are asked, the data is worthless however well it is collected.**
> **2. Can the customer REPORT it, or must they EXPERIENCE it?** — Price, brand and past behaviour can be asked about. **Taste, feel and enjoyment have to be tried.**
> **3. Do you need DEPTH on a few, or a CROSS-SECTION of many?** — **How something will be used → depth. What a whole customer base thinks → cross-section.**

---
# BATCH 7e — 9-MARK JUSTIFY, PART 5 — JOB DESIGN, MOTIVATION AND CONTRACTS

**9 entries covering 14 blocks — every job design, motivation and contract-type Justify question in the qualification.**

> ### ⭐ THE DOMINANT PAIR IN THIS CLUSTER: A BONUS VERSUS JOB ENRICHMENT
> **It appears four times — Backyard Shoez, Starbucks, IKEA and Huawei — across four series.** And the scheme's two counter-arguments are *identical in all four*:
>
> ⭐ **The bonus fails because not everyone can win it, or not everyone wants it:** *"employees may not be interested in a bonus as it requires more work and effort"* · *"not all employees are interested in bonus payments, as many are more interested in a good work-life balance"* · *"employees may not be interested in bonus payments if their bonus is based on everyone who works in the factory, as some employees may not work as hard as others"* · *"if an employee cannot continually achieve the highest sales then they may become demotivated."*
> ⭐ **Job enrichment fails because it suits some people and not others:** *"not all employees are motivated by non-financial methods such as job enrichment, they may prefer to have additional remuneration"* · *"some employees may resent not being chosen for job enrichment, and therefore may become demotivated."*
>
> **So the deciding question is never "which motivates people more" — it is WHOSE REWARD IS IT, and does it suit THIS workforce?** **That is what the case facts are for.**

---

## 209. MOTIVATION — a bonus versus job enrichment

**Asked four times:**
- *"Option 1: bonuses for whoever achieves the highest shoe sales in a month · Option 2: job enrichment, giving employees greater responsibilities."* — **May–June 2019 P1, 2(f)**, Backyard Shoez
- *"Option 1: bonus payments if the coffee shop increases its sales · Option 2: non-financial benefits such as job enrichment, so employees gain more skills and knowledge."* — **June 2025 P2, 2(f)**, Starbucks
- *"Option 1: the opportunity of earning a bonus to encourage carpenters to make more tables and chairs · Option 2: job enrichment, such as training present employees so they can work in the packing department."* — **May 2023 P2, 2(f)**, IKEA
- *"Option 1: financial methods such as bonus payments and piece rates · Option 2: non-financial benefits such as job enrichment."* — **Nov 2021 P2, 2(f)**, Huawei

> **Four papers, one decision, and the case facts point in genuinely different directions. This is the entry to read if you want to see how the same pair produces opposite answers.**

**The AO2 anchors (IKEA):** the bonus **encourages carpenters to make more tables and chairs**; job enrichment means **training present employees so they are able to work in the packing department**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]` *(written on IKEA)*
> **IKEA should use the bonus.** The decisive fact is **what the job is and why output is the problem: factory carpentry is measured in tables and chairs, and a bonus tied to making more of them rewards exactly the thing the business needs.** **It is also the reward the whole workforce can understand immediately — the scheme's own phrasing is that it "encourages them to make more tables and chairs", with no course to attend and no waiting to see whether the training worked.** **Job enrichment is the more thoughtful option and would give the carpenters a route into the packing department** — but **it changes where people work rather than how much they make, and the factory's output problem is a volume problem.** **However, "employees may not be interested in a bonus as it requires more work and effort"** — a reward for more output is only a reward to someone who wants more output. **However, that is the smaller risk here than the alternative: "not all employees are motivated by non-financial methods of motivation such as job enrichment; they may prefer to have additional remuneration."** **I would still choose the bonus, on the condition that it is paid on output the individual can actually control — because a factory bonus measured on the whole line's output rewards the carpenter for what the next shift did, and that is the version of it that demotivates.**

| Move | The answer |
|---|---|
| **1. Choice** | **The bonus** — first sentence |
| **2. AO2 + AO3** | Factory work is **measured in units**, and output is the problem → **the bonus rewards the exact thing needed** |
| **3. Counter-arguments** | Bonus → **requires more effort, may not be wanted**; enrichment → **not everyone wants non-financial rewards** |
| **4. Named condition** | ⭐ **Provided it is paid on output the individual controls, not the whole line's** |

**Backyard Shoez runs the other way — and the reason is that the bonus is a COMPETITION.** The scheme says it is for *"the person who has achieved the highest shoe sales"*, and warns that **"if an employee cannot continually achieve the highest sales then they may become demotivated and this could have the opposite effect."** **A prize that only one person can win demotivates everyone else by design.** **So for Backyard Shoez: job enrichment, provided the extra responsibility is offered to everyone rather than to a chosen few** — because the scheme's objection to enrichment is *"some employees may resent not being chosen."* **Both options in this pair fail in the same way — by excluding people — and the fix is the same.**

**Second acceptable chain (Huawei or Starbucks):** non-financial rewards **cost the business less and stay with the employee** — the skills cannot be taken to a rival the way a bonus can → **but they only work where the workforce is not primarily there for the money, which the case has to tell you.**

> ⭐ **The transferable test: does the reward EXCLUDE anyone?** **A prize for one winner demotivates the rest; enrichment offered to a few creates resentment among the others.** **The named condition for this entire pair is almost always about who gets it.**

---

## 210. JOB DESIGN — job rotation, job enrichment and added tasks

**Asked in three different pairings:**
- *"Option 1: adding additional tasks, such as supervising newly recruited employees · Option 2: employees could rotate between the store and the stock room."* — **May–June 2019 P2R, 3(e)**, Yellow
- *"Option 1: job rotation, moving from the stock room to the shop floor · Option 2: job enrichment, using their skills in displaying furniture and clothes in the shop windows."* — **May–June 2021 P2, 3(e)**, NEXT
- *"Option 1: moving to different jobs on or off the production line · Option 2: a bonus if car manufacturing targets are met."* — **May 2023 P2R, 3(e)**, M&M

> **Three blocks sharing one family of methods.** **The scheme's counter-arguments are the ones to learn, because they are specific to each method and they recur:**

| Method | What it does | Its fixed weakness |
|---|---|---|
| **Adding tasks** | Widens the job — supervision, extra duties | ⭐ *"There may come to a point where they demand more pay"* |
| **Job rotation** | Moves people between different jobs | ⭐ *"These new experiences and skills may mean that employees could decide to look for other jobs instead"* / *"may not be interested in job rotation as it may not increase their wages"* |
| **Job enrichment** | Gives more responsibility and autonomy | ⭐ *"This could incur additional costs of time and training"* / *"some employees may resent not being chosen"* |

**The AO2 anchors (NEXT):** job rotation lets employees **experience different jobs, moving from the stock room to the shop floor**; job enrichment lets them **utilise their skills of displaying furniture and children's clothes in the shop windows**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]` *(written on NEXT)*
> **NEXT should use job enrichment.** The decisive fact is **what NEXT sells and what its stores depend on: furniture and children's clothing have to be displayed to sell, and the skill of arranging a window or a showroom is exactly the skill the business needs more of.** **Job enrichment puts an employee's existing ability to use rather than moving them somewhere it is not needed** — and the scheme states the payoff as *"employees may find they utilise their skills of displaying the furniture and children's clothes in their shop windows."* **Job rotation does something different: it moves people around the store so nobody is stuck on one job all day.** **That relieves boredom, but it also means the person arranging the window this month is on the stock room the next.** **However, "this could incur additional costs for NEXT of time and training of the employees"** — enrichment is not free; giving someone more responsibility takes someone else's time to set up. **However, rotation has the more serious risk of the two: "these new experiences and skills may mean that employees could decide to look for other jobs other than remaining employed by NEXT."** **I would still choose job enrichment, on the condition that the responsibility given is genuinely theirs and not a manager's task passed down — because responsibility without authority is the version of enrichment that annoys people, and the scheme already warns that employees who are not chosen will resent it.**

| Move | The answer |
|---|---|
| **1. Choice** | **Job enrichment** — first sentence |
| **2. AO2 + AO3** | **Windows and showrooms sell the products** → use the skill the business depends on |
| **3. Counter-arguments** | Enrichment → **extra training cost, resented by those not chosen**; rotation → **trained staff may leave for other jobs** |
| **4. Named condition** | ⭐ **Provided the responsibility is genuinely theirs, not borrowed from a manager** |

**On Yellow the answer is rotation, for a specific reason: the shop and the stock room are two jobs that must both be covered, and the scheme notes rotation "helps the managers if staff are able to move from one job to another at busy times."** **The benefit there is operational flexibility, not motivation.** **On M&M the answer is likely rotation too — but the bonus is the option it is paired against, and the scheme warns employees "may not be interested in job rotation as it may not increase their wages", which makes the named condition about pay: rotation only works if it is not simply more work for the same money.**

> ⭐ **The decisive question for this family: is the business short of FLEXIBILITY or of EXPERTISE?** **Flexibility — cover for busy times and absence → rotation.** **Expertise — a skill the business's product depends on → enrichment.** **Motivation is a by-product either way, not the reason.**

---

## 211. MOTIVATION — extra holiday versus a bonus

**Asked:** *"Option 1: offer managers an extra five days' paid holiday a year · Option 2: pay a bonus to the managers whose restaurants achieve the highest levels of profit."* — **June 2026 P2, 3(e)**, Nando's

> **Both options target the same people — restaurant managers — and the question is what a manager is short of: time, or money.**

**The AO2 anchors:** extra holiday **will help provide the managers with a better work–life balance**; a bonus **will encourage the managers to attempt to sell more chicken, salad and wraps**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **Nando's should offer the extra holiday.** The decisive fact is **whether the bonus can actually be won: the scheme ties it to "the managers whose restaurants achieve the highest levels of profit", which is a contest with a small number of winners.** **Most managers will look at the target and conclude they cannot reach it** — and the scheme names exactly this: *"the restaurant managers may not believe they can achieve the highest levels of profit and this potential reward may not be sufficient to stop them leaving Nando's for a new job."* **A reward that most people cannot win is not a reward; it is a message.** **Holiday is different, because it is available to every manager on the same terms, and running a restaurant is a job with long hours and late finishes** — so **"better work-life balance" is something every one of them wants and can use.** **However, "managers may already have enough holidays to take and might not be persuaded to stay with the business for this reward"** — time off only motivates someone who does not already have enough of it. **I would still choose the extra holiday, on the condition that it can be taken in a block rather than scattered as single days — because a manager who cannot leave the restaurant for a week has not been given a holiday, only paperwork.**

| Move | The answer |
|---|---|
| **1. Choice** | **The extra holiday** — first sentence |
| **2. AO2 + AO3** | The bonus is **a contest most managers cannot win** → **only a few are motivated**; holiday is **available to all and suits the long hours of the job** |
| **3. Counter-arguments** | Holiday → **managers may already have enough**; bonus → **may be seen as unachievable and not worth staying for** |
| **4. Named condition** | ⭐ **Provided it can be taken in a block, not as single days** |

**Second acceptable chain:** the bonus **directly links pay to the profit the manager produces, so it costs Nando's nothing unless the restaurant has already earned more** → it is self-funding in a way holiday never is → **but a prize for the highest profit also creates competition between managers, which can make them unwilling to share staff or best practice.**

> ⚠️ **This is the clearest "unachievable target" AO4 in the tier, and it recurs.** **Whenever a scheme says a reward is for the HIGHEST or the BEST, the counter-argument writes itself: most people cannot win it, so most people are not motivated by it.** **Compare entry 209's Backyard Shoez block, where the same logic decides the question.**

---

## 212. MOTIVATION — commission versus a higher hourly rate

**Asked:** *"Option 1: commission to encourage teachers to find new pupils · Option 2: an increased hourly rate to encourage teachers to work longer hours."* — **May–June 2020 P1, 2(f)**, TADS

> **Both options are financial — so this is not financial against non-financial. It is PAY FOR FINDING WORK against PAY FOR DOING WORK**, and that difference decides it.

**The AO2 anchors:** commission **would encourage its teachers to find new pupils who want to learn music**; a higher hourly rate **would encourage music teachers to work for longer hours**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **TADS should use the commission.** The decisive fact is **what the business actually needs: a drumming school with too few pupils has a demand problem, not an hours problem.** **Commission pays for finding new pupils, which is the thing the school is short of** — and paying for a result means **TADS only pays out once a pupil has arrived and started paying fees.** **An increased hourly rate pays for time, whether or not there is any work for the teacher to do.** **That direction matters, because the scheme's own objection to the hourly rate is that "if TADS cannot increase the number of pupils it may not be able to retain all of the teachers it currently employs"** — **paying more per hour without more pupils simply raises the cost of serving the pupils it already has.** **However, "the commission is a one-off payment and once paid the teachers would only receive their hourly rate, which may not be sufficient to continue to be employed by TADS"** — so commission brings a teacher a pupil but does not make them stay. **I would still choose the commission, on the condition that it is paid on pupils who actually stay for a term — because a payment on signatures rather than on retained pupils pays teachers to recruit people who will not come back.**

| Move | The answer |
|---|---|
| **1. Choice** | **The commission** — first sentence |
| **2. AO2 + AO3** | The problem is **too few pupils, not too few hours** → pay for the result the business lacks |
| **3. Counter-arguments** | Commission → **one-off; the teacher's ongoing rate is unchanged**; hourly rate → **costs more with no more pupils, and may not be affordable** |
| **4. Named condition** | ⭐ **Provided it is paid on pupils who stay, not on sign-ups** |

**Second acceptable chain:** a higher hourly rate **rewards the teachers who are already good and therefore keeps them**, which matters in a school whose product is the quality of its teaching → **but it rewards loyalty rather than growth, and the scheme is clear that the enrolment problem is the one that would cost TADS its teachers.**

> ⭐ **The decisive question: what is the business short of — DEMAND or CAPACITY?** **Short of customers → pay for bringing them in (commission).** **Short of output or hours → pay for time (a higher rate).** **TADS has an empty class, not a tired teacher.**

---

## 213. COSTS — reducing wages by using part-time staff versus reducing commission

**Asked:** *"Option 1: employ part-time tour guides instead of full-time tour guides · Option 2: reduce the rate of commission paid to its sales team."* — **Nov 2025 P1, 3(e)**, Ocean Vibes

> **Read what this question is: the stem asks which cost to cut, not which reward to give.** **Both options save money — so the answer depends entirely on which saving damages the business less.**

**The AO2 anchors:** part-time guides **reduce the wages of the wildlife tour guides**; reducing commission from 5% **lowers the total variable costs of the boat tours**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **Ocean Vibes should reduce the commission rather than move to part-time guides.** The decisive fact is **who delivers the product: the tour guides ARE the dolphin and bird tours.** **A part-time guide is one who is not there on the day the guests wanted** — and the scheme warns that **"it is possible that part-time employees are less committed to the business if they prefer full time work, which may lead to tour guides leaving Ocean Vibes for alternative employment."** **The saving is real but it is bought by putting the touring at risk, and the tours are the entire revenue.** **Commission is different in one important way: it is a variable cost, paid only when the sales team has actually sold something** — so the saving follows the sales rather than preceding them. **However, that is also exactly why it is dangerous: "the sales team may be less motivated to work, which may lead to a reduction in the revenue and the profitability of boat tours for Ocean Vibes."** **Cutting the reward of the people who bring in money reduces the money coming in.** **I would still cut the commission, on the condition that the rate is reduced by a stated amount rather than tied to a sales target the team cannot influence — because a demotivated sales team costs more in lost bookings than the commission ever saved.**

| Move | The answer |
|---|---|
| **1. Choice** | **Reduce the commission** — first sentence |
| **2. AO2 + AO3** | **The guides ARE the tours** → part-time risks the product and the staff | 
| **3. Counter-arguments** | Part-time guides → **less committed, likely to leave**; commission cut → **sales team demotivated → revenue falls** |
| **4. Named condition** | ⭐ **Provided the cut is a stated amount, not a target the team cannot influence** |

**Second acceptable chain:** wage cost is **fixed and paid whether or not a single tour runs** → in a season with bad weather, part-time guides are the difference between a loss and a surplus → **but saving a fixed cost by removing the people who deliver the service is a saving taken from the product itself.**

> ⚠️ **This question is a cost-reduction question wearing a motivation question's clothes. Identify which one you have before writing** — otherwise you will argue about motivation theory when the examiner is asking which cut is survivable. **The scheme's own framing gives it away: both options are phrased as cost reductions, not rewards.**

---

## 214. CONTRACTS — full-time versus part-time staff

**Asked:** *"Option 1: full-time staff, meaning fewer employees in each store · Option 2: part-time staff, offering flexibility in the hours they work."* — **May–June 2019 P2R, 2(f)**, Yellow

**The AO2 anchors:** full-time staff means **fewer employees in each store**; part-time staff **offer flexibility in the hours they work**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **Yellow should employ part-time staff.** The decisive fact is **what a clothes shop's demand does: it rises at weekends, at lunchtimes and in the run-up to holidays, and almost nowhere in between.** **Part-time contracts let Yellow put staff on the floor exactly when customers are there**, and the scheme's framing — *"flexibility in the hours they work in each store"* — is the whole argument in six words. **Full-time contracts buy certainty of who is on shift, and "fewer employees in each store" means fewer people to manage and to train.** **However, "costs may be increased because they have to be paid regardless of demand in the stores"** — a full-time wage is paid in a quiet week exactly as it is in a busy one, which for a fashion retailer with a quiet season is the risk that matters most. **However, the part-time route has its own cost: "higher recruitment costs because part-time staff may be less committed to Yellow."** **I would still choose part-time staff, on the condition that the hours offered are enough that the good staff stay — because the recruitment cost the scheme warns about is a repeat cost, paid again every time a part-timer leaves.**

| Move | The answer |
|---|---|
| **1. Choice** | **Part-time staff** — first sentence |
| **2. AO2 + AO3** | Retail demand **peaks and troughs** → hours match the customers |
| **3. Counter-arguments** | Full-time → **paid regardless of demand**; part-time → **higher recruitment costs, less committed** |
| **4. Named condition** | ⭐ **Provided the hours are enough to keep good staff** |

**Second acceptable chain:** full-time staff **know the stock, the customers and the systems better** → fewer errors and better service → **but a store cannot be staffed to a peak all week simply to have experienced people on a Tuesday morning.**

---

## 215. CONTRACTS — permanent versus temporary contract

**Asked:** *"Option 1: offer the new chef a permanent contract · Option 2: offer the new chef a temporary contract."* — **May–June 2022 P1R, 3(e)**, Can Culleretes

**The AO2 anchors:** a permanent contract means **the chef will be more committed to the restaurant long term**; a temporary contract lets them **wait to see if the desserts are popular before hiring on a permanent basis**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **Can Culleretes should offer the temporary contract.** The decisive fact is **what the business is testing and what a mistake would cost it: a dessert chef has been hired to produce a new dessert range, and nobody yet knows whether customers will want it.** **A temporary contract lets the restaurant "wait to see if the desserts are popular or not before hiring on a permanent basis"** — so **the decision that cannot be undone is deferred until there is evidence for it.** **That matters more in a family business than in a chain: the scheme notes that "as Can Culleretes is a family run business they may be cautious of having someone come into the business on a permanent basis, especially if the new desserts do not meet customer expectations."** **In a restaurant run by the family that owns it, a permanent appointment is a personal commitment as well as a contract.** **However, "a skilled dessert chef may not like the uncertainty of a temporary contract and may choose to work elsewhere"** — and the best chefs are the ones with options. **I would still choose the temporary contract, on the condition that it states what would make it permanent — because a competent chef will accept a trial, and will not accept an open-ended one.**

| Move | The answer |
|---|---|
| **1. Choice** | **The temporary contract** — first sentence |
| **2. AO2 + AO3** | **The dessert range is untested** → defer the irreversible decision until there is evidence |
| **3. Counter-arguments** | Temporary → **a skilled chef may go elsewhere**; permanent → **a commitment the family business may regret** |
| **4. Named condition** | ⭐ **Provided the contract states what makes it permanent** |

**Second acceptable chain:** a permanent contract **secures commitment from the chef, who then invests in the restaurant's menu rather than just executing it** → **but a family restaurant that has traded for generations does not need to gamble its payroll on an untested dessert.**

> ⭐ **The decisive question: can the decision be UNDONE?** **Untested product, uncertain demand, a small business → temporary. Proven need, scarce skill, a role the business cannot function without → permanent.** **And the named condition is always the same: say what converts one into the other.**

---

## 216. CONTRACTS — part-time working versus job share

**Asked:** *"Option 1: part-time working, to provide flexibility for employees · Option 2: job share, so that if one employee is absent through illness the other can take their place."* — **May–June 2022 P2R, 2(f)**, Cadbury

> **Both options reduce hours — so the difference is COVER.** A part-timer's hours are theirs alone; a job share has two people who know the same role.

**The AO2 anchors:** part-time working **provides flexibility for employees**; with a job share, **if one employee is absent through illness the other members may be able to take their place**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **Cadbury should use job sharing.** The decisive fact is **what the roles being covered actually are: designing chocolate wrappers is skilled work that cannot be picked up by whoever is free that morning.** **A job share puts TWO people in the same role, so when one is ill, the other knows the work, the software, the brief and the deadlines.** **That is cover, not just flexibility** — and the scheme's own phrasing, that the other member "may be able to take their place", is a benefit no single part-timer can offer. **Part-time working gives the individual flexibility, which is what it is for** — and it is far simpler to arrange, with one contract and one set of hours. **However, "it may increase employment costs because of legal benefits that have to be offered to part-time employees"** — part-time is not free. **However, the job-share route carries the harder risk: "the two people job sharing will have to work as a team and liaise effectively."** **If they do not, the role has two owners and no accountability.** **I would still choose job sharing, on the condition that the two sharers are given overlapping hours to hand over — because a handover that happens by email at midnight is where job shares fail.**

| Move | The answer |
|---|---|
| **1. Choice** | **Job sharing** — first sentence |
| **2. AO2 + AO3** | **Skilled design work needs continuous cover** → two people who both know the role |
| **3. Counter-arguments** | Part-time → **higher employment costs and benefits**; job share → **the two must liaise and work as a team** |
| **4. Named condition** | ⭐ **Provided they get overlapping hours for a handover** |

**Second acceptable chain:** part-time working **is easy to offer and easy to withdraw, so it can be used across the whole workforce rather than one role** → the flexibility is available to hundreds of staff → **but it solves absence by hiring someone new each time, which the job share solves with the person already there.**

---

## 217. CONTRACTS — on-call staff versus student staff

**Asked:** *"Option 1: keep employees 'on call' for emergencies or staff shortages · Option 2: employ college and university students during the summer holidays."* — **June 2024 P2R, 2(f)**, Jimmy Choo

> **Both options give flexibility, and neither guarantees commitment — so the question is which sort of unreliability is easier to live with.**

**The AO2 anchors:** some employees **like the option of being on call**; students **wanting to work during the summer holidays would be grateful for the opportunity**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **Jimmy Choo should employ the students.** The decisive fact is **what the work is and when it is needed: producing handbags and clothes in the summer holidays is seasonal demand, and students are available in exactly that window, wanting exactly that work.** **The scheme captures the fit in one phrase — they "would be grateful for the opportunity" — and a worker who wants the hours in the weeks the business wants them is a worker who turns up.** **On-call staff look more convenient because they are existing employees who already know the work.** **However, the scheme's objection to them is fundamental: "casual employees do not get any guarantee of work from Jimmy Choo and this may make them lack commitment to do their work when they are employed."** **A worker with no guaranteed hours has no reason to answer the phone on the day they are needed** — and the moment they are needed is by definition an emergency, which is the worst time to find out. **However, "there is no guarantee that the part-time employees can work the hours or have the skills that Jimmy Choo needs"** — students are unskilled and will leave in September. **I would still choose the students, on the condition that a core of experienced staff remains to supervise and train them — because student labour is seasonal by definition, and the skills have to leave with them.**

| Move | The answer |
|---|---|
| **1. Choice** | **The students** — first sentence |
| **2. AO2 + AO3** | Seasonal production demand **matches the summer holiday exactly** → and they want the hours |
| **3. Counter-arguments** | On-call → **no guaranteed hours, so no commitment**; students → **no guarantee of skills or availability** |
| **4. Named condition** | ⭐ **Provided experienced staff stay to supervise and train them** |

**Second acceptable chain:** on-call staff **need no recruitment, no induction and no training, because they already work for the business** → the costs of taking on students are avoided → **but a workforce that is only called when there is a crisis will not plan around Jimmy Choo's needs, only its own.**

> ⭐ **The decisive question: which kind of unreliability can the business absorb?** **On-call staff are unreliable when you MOST need them; students are unreliable because they leave.** **The second is predictable and can be planned for — the first is not.**

---

## ✅ THE JOB DESIGN, MOTIVATION AND CONTRACTS CLUSTERS — COMPLETE

**9 entries covering 14 blocks.**

| Decision | Blocks | Entry |
|---|---|---|
| **A bonus vs job enrichment** | **4** — Backyard Shoez · Starbucks · IKEA · Huawei | **209** |
| **Job rotation vs enrichment vs added tasks** | **3** — Yellow · NEXT · M&M | **210** |
| Extra holiday vs a bonus | 1 — Nando's | **211** |
| Commission vs a higher hourly rate | 1 — TADS | **212** |
| Reducing wages vs reducing commission | 1 — Ocean Vibes | **213** |
| Full-time vs part-time staff | 1 — Yellow | **214** |
| Permanent vs temporary contract | 1 — Can Culleretes | **215** |
| Part-time vs job share | 1 — Cadbury | **216** |
| On-call vs student staff | 1 — Jimmy Choo | **217** |

> ### ⭐ THE TESTS, IN ONE PLACE
> **A reward that only one person can win demotivates everyone else.** *(entries 209, 211)*
> **Pay for the result the business lacks — customers, output or hours.** *(entry 212)*
> **Never cut the reward of the people who bring the money in.** *(entry 213)*
> **Can the decision be undone? If not, buy evidence first.** *(entry 215)*
> **Which unreliability can the business absorb — unreliability at the moment of need, or unreliability that is scheduled?** *(entry 217)*

---
# BATCH 7e — 9-MARK JUSTIFY, PART 6 — **THE TIER IS COMPLETE**

**10 entries covering the last 21 blocks: training, production, operations, recruitment, communication, place, product and structure.**

---

## 218. TRAINING — on-the-job versus off-the-job, and induction

**Asked three times:** LEGO *(on-the-job keeps them producing vs off-site experts)* — **June 2022 P2, 3(e)** · Irsi Chocolatier *(on-the-job shows current techniques vs a college lecturer)* — **May 2023 P1, 3(e)** · Jimmy Choo *(induction in their own department vs off-site experts)* — **June 2024 P2R, 3(e)**

> **The pair changes name between papers — induction and off-site in one, on-the-job and off-the-job in another — but the decision is the same: learn it HERE, or learn it THERE.**

**The AO2 anchors (Irsi):** on-the-job **allows the new employee to see current chocolate-making techniques**; off-the-job **allows them to learn new techniques from lecturers at a college**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]` *(written on Irsi Chocolatier)*
> **Irsi should train the new employee off-the-job.** The decisive fact is **the size of the business: the scheme says Irsi "only has 3 employees" — and with three people, there is nobody who can be spared to teach.** **On-the-job training assumes a skilled person standing beside the trainee, and in a three-person shop that person is also making the chocolates, serving the customers and taking the orders.** **The scheme's warning is precisely this: "there may not be someone who can dedicate the time to train the new employee to the standard required."** **Off-the-job training removes that problem entirely — the lecturer is not taken away from production because they were never part of it.** **It also brings in "new techniques from lecturers at a college", which a business this small cannot generate from inside.** **However, "this can be costly as the employee will have to attend an external course rather than learn on the job"** — and for a three-employee business, one wage plus a course fee with no production from that person is a real cost. **I would still choose off-the-job training, on the condition that the course is short and specific to chocolate-making — because a small business cannot absorb a general qualification, but it can absorb a two-week course that makes the new recruit productive.**

| Move | The answer |
|---|---|
| **1. Choice** | **Off-the-job training** — first sentence |
| **2. AO2 + AO3** | **Three employees → nobody can be spared to teach** |
| **3. Counter-arguments** | Off-the-job → **costly, employee absent; course may not match the job**; on-the-job → **no one available to train to standard** |
| **4. Named condition** | ⭐ **Provided the course is short and specific to chocolate-making** |

**On LEGO the balance tips the other way, and the reason is the 15 factories.** The scheme gives on-the-job the advantage that **"the cost of training is reduced as employees remain on the premises producing the Princess Leia toy whilst being trained"** — and a business with **fifteen factories can always find a skilled person in one of them to train the next.** Its cost is that **"this can be time consuming and prevents the skilled employees from carrying out their job efficiently."** **Off-site brings in "new production methods not seen in the 15 LEGO factories" — but the scheme's objection is decisive: "the new employees may not gain the specific skills and knowledge which are needed for designing the new Star Wars toys for LEGO."** **General excellence is the wrong kind of excellence for a licensed product.** **So LEGO: on-the-job, provided the trainer's own output is backfilled while they teach.**

> ⭐ **The deciding fact is THE SIZE OF THE BUSINESS, and it points opposite ways.** **Too few staff to spare a trainer → off-the-job. Enough staff to have a trainer somewhere → on-the-job.** **Nothing about the method itself makes it better — it is whether this business can staff it.**

---

## 219. PRODUCTION — job, batch and flow production

**Asked three times:** Lavender *(tailor each outlet vs flow production for all)* — **May–June 2019 P1R, 2(f)** · Cadbury *(batch Dinky Deckers so production can be stopped vs a method ensuring enough supply)* — **June 2022 P2R, 3(e)** · Irsi Chocolatier *(batch for variety of shapes vs job for personalisation)* — **May 2023 P1, 2(f)**

> **The three blocks compare three different pairs of the same three methods. The transferable skill is knowing what each method costs and what it buys.**

**The AO2 anchors (Irsi):** batch production **allows different flavours and shapes of chocolate lollipops**; job production **allows Irsi to give customers the option of personalised lollipops**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]` *(written on Irsi Chocolatier)*
> **Irsi should use batch production.** The decisive fact is **what the customer is actually buying: a chocolate lollipop is an impulse purchase, taken from a display and paid for in seconds.** **Batch production gives "different flavours and shapes" — the variety that makes a display worth stopping at — while still producing in quantities that can be made ahead and kept ready.** **Job production offers something more attractive in principle: "customers the option of personalised chocolate lollipops."** **But the scheme's objection is fatal to it here: "lollipops are only small items so customers may not want to wait for them to be personalised and may prefer to buy off the shelf to make the transaction quicker."** **A product that sells on impulse cannot be made to order.** **However, batch production "could be more costly depending on the demand for different shapes and flavours"** — every change of shape is machine time that makes no lollipops. **I would still choose batch production, on the condition that the number of shapes is kept small enough that each batch is big — because a range of twenty shapes made in batches of ten costs more per lollipop than five shapes made in batches of forty.**

| Move | The answer |
|---|---|
| **1. Choice** | **Batch production** — first sentence |
| **2. AO2 + AO3** | **Lollipops sell on impulse** → variety to display, made ahead in batch |
| **3. Counter-arguments** | Batch → **costly if demand for shapes is low**; job → **customers will not wait for a small item** |
| **4. Named condition** | ⭐ **Provided the range of shapes is small enough to keep each batch big** |

**On Cadbury the answer is batch, and the reason is RISK not variety.** The scheme gives batch the advantage that **"if Dinky Deckers is not popular, they can limit or stop production"** — an exit that a continuous line cannot offer. Its cost is that **"this method can be more expensive because of time spent changing the machines."** **The rival option — one that guarantees "sufficient Dinky Deckers available for all its customers" — carries the risk the scheme names: "there is no guarantee on how popular the Dinky Deckers will be; Cadbury could be left with a large quantity of unsold chocolate."** **For an untested product, being able to stop matters more than being able to supply.**

**On Lavender the answer is job/bespoke, because the scheme's objection to flow is that it is "very difficult to change and cannot take into account regional tastes" — and Lavender is expanding across regions.** **Its rival, matching each outlet to local demand, keeps the products relevant but costs consistency, which the scheme notes "will make the movement of employees difficult."**

> ⭐ **The three questions to ask about any production method: can the product be made ahead? can it be made to vary? and can the business STOP if it does not sell?** **Impulse goods → batch. Personalised goods with a patient buyer → job. Untested products → whichever can be halted cheapest.**

---

## 220. OPERATIONS — Kaizen versus just-in-time

**Asked twice:** HRMW *(employees involved in improving production vs JIT so nobody waits for materials)* — **May–June 2020 P2R, 2(f)** · Samsung *(JIT for deliveries as required vs Kaizen for continuous improvement and less waste)* — **Nov 2025 P2, 3(e)**

> **Both are lean production methods, so both reduce cost — the difference is WHERE the saving comes from: the people, or the stockroom.**

**The AO2 anchors (Samsung):** JIT **allows Samsung to receive electronic parts as required on the assembly line**; Kaizen **encourages a culture of continuous improvement to help reduce waste**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]` *(written on Samsung)*
> **Samsung should use Kaizen.** The decisive fact is **what it makes and where the waste is: laptops and TVs are assembled from thousands of expensive components, and a defect found late wastes the whole unit's parts.** **Kaizen attacks waste at the point it is created, because the people on the line are the only ones who see where it happens** — and it improves continuously, so the saving compounds rather than being a one-off. **JIT offers a different and more immediate benefit: parts arrive as they are needed, so "Samsung does not pay to hold stock"** and no capital is tied up in a warehouse. **However, its counter-argument is a supply-chain risk the scheme states plainly: "if suppliers deliver in smaller batches this may increase the delivery cost of materials, which will increase the total cost of production."** **JIT trades inventory cost for delivery cost and for dependence on someone else's reliability — and for Samsung, a line that stops for want of a processor stops entirely.** **However, "introducing Kaizen will take time and require training of employees, which may increase costs for Samsung in the short term."** **I would still choose Kaizen, on the condition that it is introduced on one line first so the saving can be measured before the training bill is paid across the whole factory.**

| Move | The answer |
|---|---|
| **1. Choice** | **Kaizen** — first sentence |
| **2. AO2 + AO3** | **Thousands of parts per unit → late defects waste everything already spent**; the line workers see the waste |
| **3. Counter-arguments** | Kaizen → **training costs and time in the short term**; JIT → **smaller deliveries cost more and depend on suppliers** |
| **4. Named condition** | ⭐ **Provided it is piloted on one line before roll-out** |

**On HRMW the pair is framed differently — employee involvement against JIT — and the scheme's caveats are worth learning because they are the two things that go wrong with each:** for employee involvement, **"there is no guarantee that the employees are willing to help improve the production of sports products, thereby saving the business money"**; for JIT, **"JIT can only work provided employees making footballs work at the same rate and that the supplier delivers the leather on time."** **Both methods depend on somebody else doing their part.**

> ⭐ **The decisive question: is the biggest waste in the PROCESS or in the STOREROOM?** **Defects, rework and idle time → Kaizen. Capital tied up in stock → JIT.** **And note that both fail the same way — they hand control of the outcome to other people.**

---

## 221. RECRUITMENT — internal versus external

**Asked twice:** Kraft Heinz *(an internal appointee who understands sauce production vs external candidates via CV and interview)* — **Nov 2023 P2, 3(e)** · Premier Inn *(internal appointment within the worldwide hotels vs external via an employment agency)* — **Nov 2024 P2, 3(e)**

> **Both schemes carry the SAME two counter-arguments — learn them as a pair.** **Internal: "once that person is appointed it means there will be another vacancy … requiring additional recruitment."** **External: "the external manager appointed may not have the right knowledge and experience when they actually start work … which means they will have wasted a great deal of time"** and **"the new employee may not fit in with the other employees, which could cause problems within the work environment."**

**The AO2 anchors (Premier Inn):** an internal appointee **will have experience of how the hotel works**; using an agency **provides the opportunity to bring in additional skills of marketing the Premier Inn business**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]` *(written on Premier Inn)*
> **Premier Inn should recruit externally through the agency.** The decisive fact is **what the role needs that the business does not already have: the scheme frames the vacancy as bringing in "additional skills of marketing the Premier Inn business" — and marketing skill is not something an internal reception appointment supplies.** **Internal recruitment fills a job but does not change the capability of the business; it moves an existing set of skills into a different chair.** **It is also cheaper and faster, because the person already knows the hotel, the systems and the standards, and needs no induction.** **However, the internal route carries a cost the scheme names exactly: "if the employee does move to take on the new job the old job may have to be filled and this could mean more expense"** — one appointment becomes two. **However, the agency route's own risk is real: "the new employee may not fit in with the other employees, which could cause problems within the work environment."** **I would still choose the external route, on the condition that the agency brief includes the hotel's culture and not just the job description — because the skill is what Premier Inn is buying, and a skilled marketer who cannot work with the front desk is a skill wasted.**

| Move | The answer |
|---|---|
| **1. Choice** | **External recruitment** — first sentence |
| **2. AO2 + AO3** | The role needs **marketing skills the business lacks** → internal moves a chair, external changes capability |
| **3. Counter-arguments** | Internal → **creates a second vacancy to fill**; external → **may not fit the team, may lack the knowledge, wastes time** |
| **4. Named condition** | ⭐ **Provided the brief includes the hotel's culture, not just the job description** |

**On Kraft Heinz the answer is internal, for the reason the scheme gives first: "Kraft Heinz know that the person they appoint will understand how the production of sauces works"** — **the knowledge is product-specific and cannot be bought in a candidate's first week.** **Its condition is about the vacancy the appointment creates: backfill the original post, or the department is short of two people rather than one.**

> ⭐ **The decisive question: does the role need MORE of what the business already has, or SOMETHING it does not have?** **More of the same, and product knowledge matters → internal. A capability the business lacks → external.** **And both options cost something you did not plan for — the extra vacancy, or the settling-in risk.**

---

## 222. COMMUNICATION — a written channel versus a face-to-face meeting

**Asked twice:** Café Pinch *(a daily-updated staffroom noticeboard vs a weekly staff meeting)* — **June 2024 P1R, 3(e)** · Rabanne *(email, sent anywhere vs weekly face-to-face meetings)* — **June 2025 P2R, 2(f)**

> **Both pairs contrast the same two things: information that is STORED against information that is DISCUSSED.**

**The AO2 anchors (Café Pinch):** a noticeboard **keeps chefs and waiters updated with the most up-to-date information about sales or meals achieved**; a weekly meeting **allows them to ask questions on any updates**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]` *(written on Café Pinch)*
> **Café Pinch should hold the weekly staff meeting.** The decisive fact is **the split between the two groups the notice has to serve: chefs and waiters work different shifts and are rarely in the staffroom at the same time.** **A noticeboard is only read by whoever passes it — and the scheme's objection is exactly that: "unless all of the employees read the notices every day, or if Kumaran forgot to update the notices daily, then communication may not improve."** **A meeting guarantees the message reaches everybody who attends, and it does something a noticeboard cannot: "allows the chefs and waiters to ask questions."** **That matters most when the information is a change they have to act on** — a new target, a new dish, a new rota — because **a question asked now is confusion avoided later.** **However, the scheme's objection to meetings is practical and serious: "as all staff will be involved in the meetings they are likely to take place out of hours and some staff may not want to attend, therefore miss out on important information."** **I would still choose the meeting, on the condition that it is held at the changeover between shifts rather than out of hours — because a meeting nobody attends is a noticeboard with extra steps.**

| Move | The answer |
|---|---|
| **1. Choice** | **The weekly staff meeting** — first sentence |
| **2. AO2 + AO3** | Chefs and waiters **work different shifts** → a notice is read by whoever passes; a meeting **reaches everyone and allows questions** |
| **3. Counter-arguments** | Noticeboard → **depends on staff reading it and on daily updating**; meeting → **out of hours, so attendance fails** |
| **4. Named condition** | ⭐ **Provided it is held at the shift changeover** |

**On Rabanne the pair is email against meetings, and the scheme gives email the reach — "used by everyone and can be sent from one location to another" — with the counter that "if there is no internet signal then sending messages and receiving them would be difficult", and meetings the discussion — "people … give their opinion" — with the counter that "meetings are very time consuming and not everyone can make the meeting because of the distance between departments."** **Here the geographic spread is the deciding fact: departments that are far apart cannot meet weekly, so the condition is the same shape as above but the answer flips — email, provided that anything requiring a decision is followed by a meeting for those who can attend.**

> ⭐ **The decisive question: does the information need to be RECEIVED, or ACTED ON?** **Information people just need to have → write it down. Information people have to change what they do about → say it, and take questions.** **And the named condition is always attendance or updatability — the two ways each channel fails.**

---

## 223. PLACE — physical stores versus online sales

**Asked:** *"Option 1: more customers can visit the stores to view the smartwatches · Option 2: online purchases provide convenience for customers wishing to buy a laptop."* — **June 2026 P2R, 3(e)**, Apple

**The AO2 anchors:** stores let **more customers view the smartwatches**; online purchases **provide convenience for customers wishing to buy a laptop**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **Apple should sell through its stores.** The decisive fact is **what the products cost and how they are chosen: a smartwatch and a laptop are expensive goods, and the scheme names the hesitation exactly — "people may want to hold/look at the smartphone/smartwatch and may not feel at ease buying an expensive product online without seeing it first."** **The store removes that hesitation, and it does so for the products where the hesitation is largest.** **Online convenience is real — it removes the journey and the queue, and it is the reason a customer completes a purchase they might otherwise postpone.** **However, the scheme's objection to stores is a cost one: "it is costly to have/build stores and pay for sales staff within the stores, which may increase the price of the goods or reduce demand."** **I would still choose the stores, on the condition that the high-value products are the ones stocked for viewing — because a physical shop earns its cost on the items a customer will not buy unseen, and costs money on the items they would have bought online anyway.**

| Move | The answer |
|---|---|
| **1. Choice** | **The stores** — first sentence |
| **2. AO2 + AO3** | **Expensive goods are not bought unseen** → the store removes the hesitation where it is biggest |
| **3. Counter-arguments** | Stores → **building and staffing them raises the price or reduces demand**; online → **customers hesitate to buy expensive items unseen** |
| **4. Named condition** | ⭐ **Provided the high-value products are the ones put on display** |

**Second acceptable chain:** online sales **reach customers in countries where Apple has no store at all** → the market is every country rather than a list of cities → **but for a premium product, a customer who cannot try it is a customer who buys the cheaper rival instead.**

> ⭐ **The decisive fact in any place question: can the customer judge the product WITHOUT seeing it?** **Clothing, watches, cars, furniture, anything fitted → the store wins, because the sale is decided by touching it.** **Standardised goods the customer already knows → online wins, because the store adds cost without adding information.**

---

## 224. PLACE — choosing between two new locations

**Asked:** *"Option 1: open coffee shops in supermarkets · Option 2: open coffee shops in hospitals."* — **June 2025 P2, 3(e)**, Starbucks

> **Note that both options ARE viable — so the question is which location's customers will actually stop.** **The scheme's counter-arguments for both are worded almost identically, which tells you what the decision turns on.**

**The AO2 anchors:** supermarkets offer **customers who want a coffee after finishing their shopping**; hospitals offer **friends and relatives who have travelled a distance to get there**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **Starbucks should open in supermarkets.** The decisive fact is **what the two sets of customers are doing when they arrive. A supermarket shopper has completed a task and is leaving with time they chose to spend — the scheme's phrasing is customers "who want to have a coffee after finishing their shopping", which is a decision they have made themselves.** **A hospital visitor has not chosen to be there, and the scheme's point follows: "there is no guarantee that visitors to the hospital would want to stay and have a drink if their time was limited."** **People in a hospital are focused on somebody else, and a coffee is something they buy when they are already free to sit down.** **However, the supermarket option has its own objection, and it is a mild but real one: "there is no guarantee that customers will want to stop and have a coffee after shopping — they may prefer to go home."** **Shopping is tiring and carrying bags is not a coffee moment.** **I would still choose the supermarkets, on the condition that the shop is placed by the exit with seating, not in the middle of the aisles — because a supermarket coffee shop competes with the door, and it has to be easier to sit down than to leave.**

| Move | The answer |
|---|---|
| **1. Choice** | **Supermarkets** — first sentence |
| **2. AO2 + AO3** | Shoppers **finish a task and choose to spend time**; hospital visitors **are there for someone else and are time-limited** |
| **3. Counter-arguments** | Supermarket → **shoppers may just go home**; hospital → **visitors' time may be limited** |
| **4. Named condition** | ⭐ **Provided it is placed by the exit with seating** |

**Second acceptable chain:** hospitals **have a captive audience who are there for hours, and a coffee is the one comfort available on site** → the footfall is guaranteed even if the spend is not → **but the scheme is explicit that the time is the constraint, and a person waiting on news does not sit down for a latte.**

> ⭐ **Two location questions in the tier, and both turn on the same thing: will the customer have TIME and REASON to stop where you put the shop?** **Footfall is not custom — the supermarket and the hospital both have footfall, and only one of them has customers with time they chose to spend.**

---

## 225. PRODUCT — a new product, a widened range, or a trial

**Asked three times:** Violet Cakes *(write and sell a cookbook vs introduce a vegan range)* — **June 2026 P1, 2(f)** · TADS *(teach other musical instruments vs offer online lessons)* — **May–June 2020 P1, 3(e)** · Rabanne *(product trials in a limited location vs advertising a new perfume worldwide)* — **June 2025 P2R, 3(e)**

**The AO2 anchors (Violet Cakes):** customers **who bought the last book may be encouraged to buy the latest**; the business **may respond to changing food trends by providing cakes suitable for vegans**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]` *(written on Violet Cakes)*
> **Claire should introduce the vegan range.** The decisive fact is **what a cookbook does to the core business: the scheme's objection is that "if customers start to make their own cookies and buns, they will buy less from Violet Cakes, which may result in a decrease in sales."** **A cookbook teaches the customer to do the thing Claire sells for a living** — and the more successful the book, the more of the café's own trade it replaces. **A vegan range does the opposite: it sells to people who currently walk past the café because it has nothing for them.** **That is new revenue rather than transferred revenue.** **It also answers the trend the scheme names — cakes "suitable for vegans" are now something a café is expected to have, not a specialism.** **However, "the cost of researching and producing a variety of vegan cakes may be high, leading to high prices or low demand for the new range."** **I would still choose the vegan range, on the condition that it starts with three or four products rather than a full counter — because vegan baking uses different ingredients with different costs, and Claire needs to know the price and the shelf life before she commits the display to it.**

| Move | The answer |
|---|---|
| **1. Choice** | **The vegan range** — first sentence |
| **2. AO2 + AO3** | A cookbook **teaches customers to replace the café**; a vegan range **adds customers who currently have nothing to buy** |
| **3. Counter-arguments** | Cookbook → **customers make their own → sales fall**; vegan range → **research and production costs, pricing risk** |
| **4. Named condition** | ⭐ **Provided it starts with three or four products, not a full counter** |

**On TADS the pair is a wider range against a wider delivery, and the schemes give range the revenue — "teaching other musical instruments will bring in new music students and revenue" — against the cost that it "would need to find and pay additional teachers", while online lessons reach "more students" against "technical issues that might lead to lessons being interrupted and not delivered, giving TADS a bad reputation."** **For a drumming school, the online route's failure mode is reputation: a lesson that drops out mid-way is worse than no lesson, because the customer paid and watched it fail.**

**On Rabanne the pair is a local trial against worldwide advertising, and the scheme's objection to the trial is the one to learn: "because product trials are based in a limited location, the results may not be representative of all locations in all countries."** **A test that only samples one city cannot justify a global launch** — whereas the objection to advertising is distribution: **"if they cannot find the perfume in a shop, then they will not be able to purchase it."**

> ⭐ **The decisive question: does the new product ADD customers, or does it move the existing ones?** **A cookbook, a cheaper version, a product that competes with your own — transferred revenue.** **An entirely new audience — added revenue.** **And check whether the business can test the idea somewhere representative before committing.**

---

## 226. MARKETING — promotion versus product improvement

**Asked three times:** Can Culleretes *(more advertising vs opening for breakfast)* — **June 2022 P1R, 2(f)** · Four Fitness *(create a USP vs add video content to the website)* — **June 2025 P1, 2(f)** · M&M *(increase promotion vs add new car features)* — **May 2023 P2R, 2(f)**

**The AO2 anchors (M&M):** increasing promotion **means more people will know about M&M and the vehicles it has on sale**; introducing new features such as automatic door locking **may interest customers**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]` *(written on M&M)*
> **M&M should introduce the new features.** The decisive fact is **what a vehicle is and what decides a purchase: a car is bought after it has been driven or after someone has recommended it, and the scheme states the consequence of that — "there is no guarantee that people will buy the vehicles unless they have driven them or been recommended to buy one."** **Promotion makes people aware; awareness is not the step at which a car is chosen.** **A new feature, such as automatic door locking, gives the salesperson and the owner something to talk about and something to compare** — and it works on the customer who has already walked in, which is the customer who actually buys. **However, "designing this feature could be expensive and customers may not wish to buy the vehicle because of the increase in price."** **A feature that costs money to add and more money to sell is a feature that can reduce sales.** **I would still choose the new features, on the condition that they are added to the models where the competition already offers them — because a feature that a rival also has is a cost of staying in the market, while a feature no rival has is the only kind that can be charged for.**

| Move | The answer |
|---|---|
| **1. Choice** | **The new features** — first sentence |
| **2. AO2 + AO3** | Cars are **bought after driving or recommendation** → awareness is the wrong stage |
| **3. Counter-arguments** | Features → **expensive to design and raise the price**; promotion → **no guarantee people buy, only that they know** |
| **4. Named condition** | ⭐ **Provided they go on the models where rivals already offer them** |

**On Can Culleretes the pair is advertising against extending the offer, and the scheme's objections are both cost-based: advertising "can be expensive, so although revenue may improve it will be a cost for the business"; opening for breakfast means "as it is only a small restaurant they may need to employ more staff as well, but this could lead to an increase in costs."** **The deciding fact there is the customer: "an increase in advertising can reach new customers and tourists visiting Barcelona", whereas breakfast "can attract existing and new customers."** **New tourists cannot be reached by breakfast — only by being found — so the answer is advertising, provided the channel is one a visitor would actually see.**

**On Four Fitness the pair is a USP against a website upgrade, and the scheme's objection to the USP is the one that decides it: "if customers do not want access to this service as part of their membership they may feel they are being overcharged and the gym could be at risk of losing customers to its competitors, therefore decreasing its market share."** **An unwanted USP is a price rise with a label on it.** **The website, by contrast, is "currently for information only" and adding to it is a low-risk change — with the caveat that "advertising costs will increase to widely draw in customers", because a feature nobody visits the site to find does nothing.**

> ⭐ **The decisive question: is the business unknown, or is its product unremarkable?** **Unknown → promotion, and the problem is that awareness is not desire.** **Known but unremarkable → improve the product.** **And watch for the option that raises price without adding value — the scheme calls it feeling overcharged.**

---

## 227. STRUCTURE — a partnership versus a private limited company

**Asked:** *"Gianni Polvani operates Four Fitness as a sole trader. Option 1: a partnership with three like-minded health professionals who already work for Four Fitness · Option 2: a private limited company with shareholders."* — **June 2025 P1, 3(e)**

> **This is the only structure question in the tier, and the reason it is interesting is that the case hands you a fact that decides it: the proposed partners are HIS OWN EMPLOYEES.**

**The AO2 anchors:** as a partnership he **will have like-minded health professionals to share the decision making who already work for Four Fitness**; as a private limited company **he will have limited liability, as will his new shareholders**.

> **Model answer — 9 marks** `[CONSTRUCTED GRADE 9 TARGET]`
> **Gianni should form the private limited company.** The decisive fact is **who he would be taking as partners: the scheme describes them as "three like-minded health professionals who already work for Four Fitness" — which means the people sharing his decisions would be the people he manages.** **A partner cannot be given instructions, and a partnership with three employees turns a business with one decision-maker into one where the staff own the business** — and the scheme's own objection is precisely that **"the decision making may be wrong because the employees do not have sufficient business experience."** **A limited company keeps the roles separate: shareholders own it, Gianni runs it.** **It also gives him limited liability, "as will his new shareholders", so a failed gym no longer puts his personal assets at risk** — which matters more in a business with premises and equipment. **However, "he will have to find people interested in the business who want to become shareholders when setting up a private limited company, and this might be difficult as it is a small business."** **I would still choose the limited company, on the condition that Gianni keeps a controlling shareholding rather than an equal split — because a small business cannot afford a decision that has to be agreed by four people with three of them drawing a wage from it.**

| Move | The answer |
|---|---|
| **1. Choice** | **The private limited company** — first sentence |
| **2. AO2 + AO3** | The proposed partners **are his own employees** → authority and ownership would collide; limited liability protects his assets |
| **3. Counter-arguments** | Partnership → **the employees lack business experience and would share decisions**; Ltd → **hard to find shareholders for a small business** |
| **4. Named condition** | ⭐ **Provided Gianni keeps a controlling shareholding** |

**Second acceptable chain:** a limited company **can raise capital by selling shares, which a partnership cannot** → the gyms can be expanded without personal borrowing → **but a small business offering shares is asking people to buy into something with no market to sell out of, so the shareholders have to be found one at a time.**

> ⚠️ **The structural fact to carry into any ownership question: a partnership gives you partners, not employees.** **Where a case proposes partners who are currently staff, the argument against the partnership is not financial — it is that you can no longer manage the people who own half of your business.**

---

## ✅ THE 9-MARK TIER IS COMPLETE

| | |
|---|---|
| **Blocks in the tier** | **76** — derived from the 38 mark schemes, validated at 80 marks per paper |
| **Blocks carried by an entry** | **76 · 100%** |
| **Distinct option pairs** | **58** |
| **Entries used** | **53** — numbered 175–227 |

**What the compression means.** **58 different option pairs across 76 blocks, carried by 53 entries** — this tier compresses far less than the 3-mark (152 → 97) and the 6-mark (114 → 74) tiers, because **the option pair genuinely varies.** **But 1 question in 4 was still a repeat**, and the repeats cluster where you would expect: **a bonus against job enrichment four times · the source-of-finance questions fourteen times across thirteen pairs · primary against secondary research five times.**

**Every decision type in the qualification is closed:** sources of finance · promotion · pricing · market research and success measures · job design and motivation · contracts · training · production · operations · recruitment · communication · place · product · marketing · structure.

> ### ✅ THE COVERAGE IS VERIFIED BY SCRIPT, NOT BY HAND
> `python3 layer_c_9mark_coverage.py` reads the derived inventory, checks every one of the 76 blocks against a `COVERED` map, and prints **0 remaining**. Run it with **`--audit`** to print **each covered block's real option pair next to the entry claiming it** — the flag that exists because an entry headed *"venture capital vs a bank loan"* once listed a block whose actual pair was **venture capital vs crowdfunding**.

> ### ⭐ AND THE THREE THINGS THAT DECIDE ANY JUSTIFY ANSWER — the whole tier in three questions
> **1. WHO BENEFITS?** The business, its owners, its employees, its customers, or a country. **Several questions in this tier name a party that is not the business, and a contextualised answer about the wrong party scores zero.**
> **2. WHAT IS THE FAILURE MODE?** Every mark-scheme counter-argument in this tier is one: *interest you must pay anyway · a campaign that raises nothing · a facility repayable on demand · a reward most people cannot win · training the customer to replace you · a feature that raises the price and adds nothing.*
> **3. WHAT WOULD HAVE TO BE TRUE?** The named condition, drawn from a case fact or a figure — and **if it could be pasted onto another question, it is not a condition.**

---
# BATCH 8 — THE 12-MARK TIER (entries 228–252)

> **38 blocks — one `4(c)` on every paper.** The bank's last tier. **This is the tier with a permanent limit: there is no verified 12/12 for Paper 2 or Paper 2R** (Pearson's 12-mark exemplars are Paper 1 scripts; see `09_Verified_Tally.md`). Everything here is therefore a `[CONSTRUCTED GRADE 9 TARGET]` unless labelled otherwise.
>
> **The unit is the TOPIC, as in every other tier** — 38 blocks collapse to **22 topics carried by 25 entries**, because *location* alone appears on four papers and *quality* on four. **One essay per topic, with every paper's own markscheme anchors printed**, is what makes the tier complete; writing 38 separate essays would repeat the same chains a dozen times.

## 228. ⭐⭐ THE UNIVERSAL 12-MARK SCAFFOLD — what every Evaluate has in common

**Asked:** all 38 papers, question **4(c)**, `AO1 = 3 · AO2 = 3 · AO3 = 3 · AO4 = 3`.

**The framing varies; the shape does not.** Across 38 papers the command sits in five forms — *"Evaluate the **extent to which**…"* · *"the **importance** of…"* · *"the **impact** of…"* · *"the **benefits** for…"* · *"Evaluate **how / why / whether**…"* — and **all five are marked with the same four-way split.** So there is one architecture, and it is the architecture of the verified 12/12 (May 2023 P1, Irsi — rule 82).

```
PARA 1   The concept, in today's words + your answer in the same breath        AO1 + AO2
PARA 2   Applied to THIS business — a chain, not a claim                       AO2 + AO3
PARA 3   "However…" — turn against what you just argued                        AO3 (+AO2)
PARA 4   Decide, and NAME THE CONDITION                                        AO4
```

**Continuous prose only.** *"Some candidates are using bullet points or a numbering format which will not allow them to gain the higher levels."* (May 2023 P2 **and** P2R). **A bulleted 12-marker cannot reach Level 3, however good the content.**

### The four routes to AO4 — all four are official, and you need one

| Route | What it sounds like | Where the scheme shows it |
|---|---|---|
| **1. The drawback of the same thing** | *"However, [the option] also means…"* | **Every one of the 38 schemes** has an AO4 bullet opening *"However"* |
| **2. A more important factor** | *"…but other factors may matter more, such as…"* | Crumb: *"other factors such as **location of the cafe and the price** may be more important"* |
| **3. The named condition** | *"…and this depends on **X**, because…"* | Irsi 12/12: *"could be limited because it **depends on factors such as nature of employee**"* |
| **4. Argue against the premise** | *"…in fact the opposite may be true, because…"* | Pearson, on a 4/12: *"…**or if other factors should be taken into account as well**"* — stated outright as a route to Level 3 |

> ### ⭐ THE CONDITION TEST — the same test as the 9-mark tier
> **"It depends" is worth nothing. "It depends on whether customers in its area value quality over price" is AO4.** Ask: *could this condition be pasted onto another question?* If yes, it scores nothing.

> ### ⭐⭐ THREE THINGS THE TOP BAND REQUIRES, ALL CONFIRMED IN THE REPORTS
> **1. No separate "In conclusion" paragraph.** The 12/12's last paragraph *decides* — *"the effectiveness of using financial methods of motivation could be limited because…"*. **A summary paragraph is the ceiling**, at 12 marks as it was at 9 (rule 83).
> **2. AO2 must be woven, not stamped.** *"The name of the business does not provide context"* (June 2024 P1R). Naming Crumb in a sentence that would work for any business is not application.
> **3. ≈330–400 words in 12–14 minutes.** The 12/12 is ≈330 words in two and a half paragraphs. **Written lines are printed to size** — overrunning earns nothing and costs the time the answer needs.

**AO checkpoint before you move on:** *Have I said what the thing **is** (AO1) · applied it with a **chain** (AO2/AO3) · given the **other side** (AO3) · **decided and named a condition** (AO4)?* Four ticks, four AOs.

---

# ---- THE FAMILY THAT APPEARS MOST: QUALITY -------------------------------

## 229. QUALITY — will it give a competitive advantage, and can it be maintained?

**Asked:** *"Evaluate the extent to which quality will give **Violet Cakes** a competitive advantage."* — **June 2026 P1 4(c)**, cake business and cafe · *"Evaluate the importance for **NEXT** of maintaining quality throughout all of its manufacturing processes."* — **May 2021 P2 4(c)**, clothing and furniture, 70 countries · *"Evaluate the benefits for **TUI** of providing a quality service."* — **May 2024 P2 4(c)**, holidays, hotels and car hire.

> ⚠️ **June 2026 P1 carries two names for the same business** — the question paper says **Crumb** (owner: Alex), the mark scheme says **Violet Cakes** (owner: Claire). Same story, same paper code; the bank carries both. **Use the name printed on your own paper.** See `Source_Notes/ARCHIVE_LABEL_AUDIT_2026-10-14.md`.

> ## `[CONSTRUCTED GRADE 9 TARGET]` — June 2026 P1, Violet Cakes / Crumb
>
> Quality means a product is free from defects and meets or exceeds what the customer expects. At Violet Cakes it comes from high-quality materials — the fruit from England and Italy, the chocolate from France and Belgium — and from quality control, so that the cakes taste the same every time. Quality clearly matters to a business selling celebration cakes, but it is only one of the things that creates a competitive advantage.
>
> If the food served in the cafe is of a high quality, this should attract consumers to visit, and if the cookies and cakes are of a high quality this should lead to word-of-mouth recommendations. That is how a cake business grows without paying for advertising: a wedding guest who tastes the cake recommends the baker. It may also lead to more high-profile orders such as the wedding cakes it has supplied to celebrities, resulting in increased publicity and a larger market share. A reputation built this way is difficult for a rival to copy quickly, because it rests on years of consistent quality rather than on a price cut — and that is exactly what makes it a competitive advantage rather than a temporary gain.
>
> However, other factors such as the location of the cafe and the price of the cakes may be more important to potential customers. A customer choosing where to buy lunch weighs convenience and cost heavily, and may never taste the difference in quality before deciding. In addition, the cost of high-quality ingredients such as chocolate from France may increase the cost of the cakes, making them uncompetitive against businesses using cheaper ingredients, and if it raises prices to protect its margin, it risks losing the price-sensitive customers that quality was supposed to win.
>
> Overall, quality will give Violet Cakes a competitive advantage, but only to a limited extent. This depends on whether the customers who buy its cakes are willing to pay a premium for ingredients they can taste, and on whether the high-profile orders continue. In the short term the higher ingredient costs will reduce the profit margin, but in the long term a reputation for quality is the business's strongest and least imitable asset.

**The scheme's own content, per paper — use your paper's column:**

| | **Violet Cakes / Crumb** (2026 P1) | **NEXT** (2021 P2) | **TUI** (2024 P2) |
|---|---|---|---|
| **AO2 anchor** | high quality attracts consumers to the cafe; word-of-mouth recommendations | NEXT sells quality furniture and fashionable dress; a poor reputation means fewer customers in its worldwide shops | if holidays and experiences are good, customers return and book again |
| **AO3 chain** | reputation keeps it competitive against **Gail's Bakery**; a high-profile order (the scheme names the **Harry and Meghan** wedding cake) → publicity and market share | the same standard must be maintained by every manufacturer across **70 countries**; a poor reputation means closing shops, cutting outlets and sales | repeat bookings → recommendations to friends and family |
| **AO4 — "However"** | **other factors** — location and price — may matter more; French chocolate raises cost and makes it uncompetitive against **Flour Cafe** | maintaining the standard is **expensive** — constant inspection; and **once a poor reputation is gained it is very hard to regain loyalty** | good service to every customer is **expensive** — enough employees to meet their needs; once a poor reputation for car hire or lack of variety is gained, **loyalty is very hard to regain** |

⭐ **The three AO4s are three different arguments, and the paper picks one:** Crumb's is **price** (a more important factor), NEXT's is **cost of control** (the drawback of the same choice), TUI's is **cost plus irreversibility** (the drawback, sharpened). **A "quality is expensive" answer is not a substitute for the whole answer** — it is one paragraph of it.

⚠️ **The trap that turns an AO2 into a zero:** *"Quality is important to Crumb because it makes good cakes."* — no chain, and the business name is doing the work. **Build it:** *high-quality materials → a cake that tastes better than a rival's → customers recommend it at weddings → orders carry a premium price → a margin a cheaper rival cannot match.*

---

## 230. TQM — introducing it, and what it does to the factory while it is introduced

**Asked:** *"Evaluate the effects on **Saha** of introducing Total Quality Management (TQM) to its business."* — **November 2024 P1 4(c)**, robots for hotels, restaurants and homes.

> ## `[CONSTRUCTED GRADE 9 TARGET]`
>
> TQM should ensure that the robots are manufactured without any faults, and it involves training every employee in quality assurance so that waste and costs fall. For a manufacturer selling to hotels, hospitals and the home, a faulty robot is not a small problem — it is a customer who will not order again.
>
> If the robots are subject to quality checks throughout the production process, they should be delivered to the restaurants with no defects, which protects Saha's revenue from the cost of returns and repairs. Successful training of each employee should also lead to a reduction in waste in the production of the new robots built for the home. Together these may improve the reputation of Saha and attract more customers to buy the robots, increasing the revenue for its business, and trained employees who are focused on quality should result in zero defects of robots to ensure Saha meets its objective of making the robots long lasting — which matters most to the hotel and hospital customers who use them continuously.
>
> However, TQM involves disruption to the manufacturing facility as new processes are introduced, which could cause delays and late deliveries of robots to the hotel and hospital customers — and those are customers on contracts, not one-off buyers. The cost of training all employees in TQM also takes time and is costly, which could reduce profitability in the short term and increase the price of the robots, making Saha uncompetitive in the robot market against manufacturers who have not taken on the same costs.
>
> Overall, TQM will benefit Saha, but only in the long term. This depends on whether its customers buy on reliability or on price, and on how long the hotel and hospital contracts can tolerate disruption during the changeover. In the short term the disruption and the training cost will hurt profit, but in the long term zero-defect manufacturing is the only way a robot-maker protects the reputation its orders depend on.

| Move | The scheme's content |
|---|---|
| **AO1** | TQM = robots manufactured without faults; **every** employee trained in quality assurance |
| **AO2** | quality checks throughout production → delivered to restaurants with no defects; trained employees → less waste in the home-robot line |
| **AO3** | better reputation → more customers → higher revenue; zero defects → meets the objective that the robots are long lasting |
| **AO4** | **disruption** to the facility → delays and late deliveries to hotels and hospitals; training all employees is **time-consuming and costly** → lower short-term profitability and **higher prices → uncompetitive** |

⭐ **TQM appears in the bank twice over — here and as a 3-mark definition (`6_`, rules on quality).** The 12-mark version is *not* "what is TQM": it is **what it does to this factory while it is being introduced.** The disruption bullet is the paragraph most candidates never write.

---

# ---- THE SECOND FOUR-PAPER FAMILY: WHERE TO PUT THE BUSINESS -------------

## 231. LOCATION — four papers, one spine, four different reasons

**Asked:** *"Evaluate the factors **Tata Motor Company** would have to take into account when making decisions about where to locate a new factory."* — **May 2019 P2 4(c)**, cars · *"Evaluate the factors that **Loaf** would have to consider when deciding where to locate its second bakery."* — **May 2020 P1R 4(c)**, bakery and cookery classes, a social enterprise · *"Evaluate the factors **Jimmy Choo** would have to consider when making decisions on the location of a new factory."* — **May 2024 P2R 4(c)**, luxury handbags · *"Evaluate the factors that **Artify Studio** would have considered when deciding where to locate its second art studio."* — **November 2021 P1 4(c)**.

**The spine is identical on all four, and it is cost, not preference:** *the factor → why this business in particular needs it → what it saves or earns → what it costs elsewhere.*

| | **Tata Motor Company** (2019 P2) | **Loaf** (2020 P1R) | **Jimmy Choo** (2024 P2R) | **Artify Studio** (2021 P1) |
|---|---|---|---|---|
| **Factor 1 — labour** | needs a range of **skilled employees, e.g. engineers and designers** | needs **skilled bakers or chefs who can run the cooking classes** | needs a wide variety of skilled labour, **from machinists producing handbags to employees with financial skills** | needs **employees with art-based skills** to work at the studio |
| **Factor 2** | **accessibility** — near a port, motorways or railway, to bring materials in and move vehicles out | **proximity of competition** — may choose to locate **away from other bakeries** | **accessibility by road, rail and sea** — reduces the transport cost of dress material from suppliers | **availability of materials** — art supplies for its courses |
| **The chain** | near skilled labour → **reduces the overall costs** of the new factory; a continuous supply in and finished vehicles out | skilled labour already trained → **saves training costs**, money spendable elsewhere; no competition nearby → **greater chance of survival** | near skilled labour **reduces overall costs**; roads and rail nearby **make delivery of finished goods easier** | skilled labour → can **progress and expand the range of courses**; supplies → **all current courses can be offered, giving consistency between the two studios** |
| **AO4 — "However"** | land and infrastructure **cost more** near skilled labour, **adding to the cost** of the location; **infrastructure is one of many factors** and others may be more important | if **no skilled labour is available** the impact is negative — newly trained bakers will not have a trained baker's skills; and Loaf **may deliberately locate near competitors**, because as a social enterprise its aims differ from other bakeries | locating near skilled labour is **more expensive** — labour costs may be higher, **increasing overall costs**; and infrastructure may matter less than delivery to and from the factory | no skilled labour → **courses cannot run**; relocating to a **small mining town** may make art materials hard to source, so it could not offer its full range |

> ## `[CONSTRUCTED GRADE 9 TARGET]` — Jimmy Choo, the most recent of the four
>
> Location decisions matter to a luxury goods manufacturer because they set costs for years: a factory cannot be moved once the trained staff and supplier routes are built around it. For Jimmy Choo, making handbags that sell at a high price, the cost of labour and of moving materials are two of the factors that decide where the new factory should go.
>
> Jimmy Choo would need to locate its factory near to where labour can be found, because it needs a wide variety of skilled labour, from machinists producing handbags to employees with financial skills. If the factory is easily accessible it could reduce the transport costs of dress material from suppliers. By locating near to a skilled labour force in Italy the business could reduce its overall costs, and the finished handbags could be delivered more easily with roads and rail nearby — which matters for a product whose reputation rests on the quality of both the stitching and the finish.
>
> However, locating near to skilled labour could be more expensive, as the cost of labour may be higher, increasing overall costs and cancelling out part of the saving. Infrastructure may also matter less than other considerations: how close the factory sits to its suppliers, and how easily finished goods reach the airports and the shops that sell them, may be more important than the road and rail links themselves.
>
> Overall, labour is the most important factor for Jimmy Choo, but only if the wage cost does not consume the saving the skills create. This depends on whether the business competes on craftsmanship or on cost, and on how many skilled machinists are actually available in the area it is considering. In the short term the higher wages will raise costs, but in the long term a factory near genuinely skilled labour is what protects the quality the brand is built on.

⭐ **"Nearest to the market" is not on any of the four mark schemes.** What appears on all four is **labour** and **a second, business-specific factor** (transport · competition · materials). **Learn the spine, then learn each paper's second leg.**

⚠️ **The counter-argument differs by business type, and this is where AO4 lives:** Tata's is *cost of land near skills*; Loaf's is *no skilled labour available at all* — plus the twist that a social enterprise may *want* to be near competitors; Artify's is *a remote mining town cannot supply art materials*. **Write the one that fits your case, not the generic "it might be expensive".**

---

# ---- RESEARCH: TWO DIFFERENT 12-MARK QUESTIONS ---------------------------

## 232. MARKET RESEARCH METHODS — primary against secondary, and why "more research" is not automatically better

**Asked:** *"Evaluate the importance of primary market research to **Backyard Shoez**."* — **May 2019 P1 4(c)**, shoes sold in a mall · *"Evaluate the importance of using methods of market research for **Café Pinch** to meet customer needs."* — **May 2024 P1R 4(c)**, cafe serving breakfast, lunch and drinks.

| | **Backyard Shoez** (2019 P1) | **Café Pinch** (2024 P1R) |
|---|---|---|
| **AO1** | research the business does itself, e.g. a **questionnaire**; or methods that suit it, like **focus groups** | **primary** market research such as questionnaires; **secondary** market research such as the internet |
| **AO2** | question customers **in the mall** on their needs and wants for shoes; speak directly to people who buy its shoes, who then **feel valued** | speak directly to customers who come for breakfast, lunch and drinks; search for **specific menu information that other cafes in the area are offering** |
| **AO3** | primary research finds out **exactly what they need** and how to meet it; focus groups give **qualitative data** that helps design new shoes | questionnaire feedback on the menu gives **ideas to improve** and better meet customer needs; the internet lets them find **suppliers, and source one more local and cheaper** |
| **AO4** | **time-consuming**; and if local competitors already meet those needs, **no amount of research will help** target the new audience. **Without secondary research as well**, they cannot find out wider information on **competitors and suppliers** | **without secondary as well as primary**, they will not have wider research such as local competitors and their activity; there may be **too much information**, which **makes decision making harder and possibly less accurate** |

> ## `[CONSTRUCTED GRADE 9 TARGET]` — Backyard Shoez
>
> Primary market research is information the business collects itself, first-hand from its own customers — for Backyard Shoez, a questionnaire in the mall or a focus group. Secondary research is information someone else has already gathered. Because Backyard Shoez sells shoes face to face, primary research is the more useful of the two, but it has to be done properly to be worth the time.
>
> Backyard Shoez could question customers in the mall on their needs and wants for shoes, and will be able to speak directly to customers who buy its shoes, who will then feel valued. Using primary market research, Backyard Shoez can find out exactly what it needs and work out ways of meeting those needs, rather than guessing and buying stock that does not sell. Focus groups would give it qualitative data — the reasons behind a preference, not just a count of them — which is what helps with the design of new shoes, because a customer can explain why a particular sole or fit does not work.
>
> However, it can be time-consuming to find out what customers' needs are, and if these are already being met by competitors in the local area then no amount of market research will help Backyard Shoez to target its new audience. Research tells it what customers want; it cannot make those wants unserved. In addition, without doing secondary market research as well, Backyard Shoez cannot find out wider information such as what its competitors are charging or which suppliers could offer it better terms — both of which are cheaper to look up than to survey for.
>
> Overall, primary research is important to Backyard Shoez, but it is not sufficient, and this depends on whether the business is trying to serve a need nobody currently meets or to compete with the shops already in the mall. In the short term a questionnaire costs time and may confirm what the owners already suspect, but in the long term designing shoes around what local customers actually ask for is the cheapest way to avoid unsold stock.

⭐ **Café Pinch adds the third leg the four-mark version never has: data overload.** *"There might be too much information and this could make decision making harder and possibly less accurate"* — **the argument against research is not only its cost, it is the quality of the decision it produces.** Keep it for any question that offers the internet as an option.

⚠️ **Do not confuse this with Block 233.** Both are research, but the question is different: this one is *which method*, the next one is *why research before you launch*.

---

## 233. RESEARCH BEFORE LAUNCH — does it de-risk the product, or only delay it?

**Asked:** *"Evaluate why **Starbucks** carries out product trials that might reduce the risks from introducing new products."* — **May 2025 P2 4(c)** · *"Evaluate why **Huawei** would carry out market research before designing a new product."* — **November 2021 P2 4(c)**.

| | **Starbucks** (2025 P2) | **Huawei** (2021 P2) |
|---|---|---|
| **AO1** | if a business launches a new product it wants to know customers will buy it; **all new products need to be tested on the market, and the larger the sample the more accurate the results** | research finds out what customers' **needs and wants** are; it lets the business make **informed decisions** about actions it should take |
| **AO2** | it could have **wasted a great deal of money** introducing a new coffee customers did not like; if it introduces a new cake it needs to know customers are likely to purchase it | if it produced **a watch very few customers want** it could waste a great deal of money; it may **add features or change the size** of its smartphones from customers' comments |
| **AO3** | by carrying out **product trials** they can find out if the new coffee flavour will be bought; they need customers' opinions on the new product to see if it will sell | a flop would **damage Huawei's financial situation and hold back other products** such as tablets; getting it right **increases sales and keeps Huawei competitive** |
| **AO4** | **no guarantee** that because some customers disliked the new coffee it would not eventually have become popular; **no matter how much research is done, there is no guarantee customers will want to buy it** | producing **a watch no other business offers** could mean it **sells more and gains a competitive advantage** *(the scheme's counter-argument)*; and **no guarantee the research is worthwhile, as customers' tastes change constantly with new technology** |

> ## `[CONSTRUCTED GRADE 9 TARGET]` — Starbucks
>
> A product trial is a limited launch — the product is tested on a sample of the market before it is offered everywhere. Starbucks carries out product trials because a coffee chain's cost is not only the coffee: rolling a new drink out to every coffee shop means new ingredients, new staff training and new menus, and all of that spending happens before a single customer has tasted it.
>
> If Starbucks launches a new product it wants to know customers will buy it, and the larger the sample the more accurate the results. Without a trial, it could have wasted a great deal of money introducing a new coffee which customers did not like. If Starbucks introduces a new cake, it needs to know that customers are likely to purchase it. By carrying out product trials it can find out whether the new coffee flavour will be bought, and the opinions it gathers tell it whether the product will sell — which matters more in coffee than in most markets, because the menu changes constantly and a failed drink takes shelf space from a successful one.
>
> However, there is no guarantee that just because some customers did not like the new coffee it would not eventually become very popular. Tastes can change once a product is in front of customers, and a trial sample of a few hundred people cannot represent the millions who use its shops. More fundamentally, no matter how much research is done on a new product, there is no guarantee that customers will want to purchase the item, so a trial reduces the risk of a failure without removing it.
>
> Overall, product trials are worthwhile for Starbucks, but only as risk reduction rather than risk removal. This depends on how similar the trial customers are to the wider market and on how costly a full launch would be if the product failed. In the short term the trial costs money and slows the launch, but in the long term a chain that tests first wastes far less on the drinks customers quietly stop ordering.

⭐ **Huawei's AO4 contains the rarest move in the whole bank: the scheme argues *against* its own question.** *"Producing a watch that no other business is offering could mean that it sells more of the products and gains a competitive advantage"* — **research can talk a business out of its best idea.** Pearson's own advice on a 4/12 (*"if other factors should be taken into account as well"*) confirms this is a route, not a risk.

⚠️ **Both AO4s end in the same place, and it is the sentence to memorise for either paper:** *research cannot guarantee demand.*

---

# BATCH 8b — 12-MARK EVALUATE, PART 2 (entries 234–242)

## 234. MARKETING — what it is worth when the product is new, and when the customer is already yours

**Asked:** *"Evaluate the importance of marketing for **Cadbury** when introducing a new product."* — **May 2022 P2R 4(c)** · *"Evaluate the importance of marketing to **PPS** so it can keep its market share."* — **May 2024 P1 4(c)**, pet products and a pet hotel.

| | **Cadbury** (2022 P2R) — *new product* | **PPS** (2024 P1) — *holding on to share* |
|---|---|---|
| **AO1** | products customers will want to buy — **market research** identifies a gap in the market; chocolate bars people enjoy **keep them loyal** | marketing **informs customers** what the business offers; marketing **builds long-lasting customer relationships** |
| **AO2** | if research finds customers like **chocolate ice creams**, Cadbury could introduce them; loyal customers keep buying its range | PPS can remind customers about products such as **CCTV cameras in the pet hotel**; it can identify needs by giving customers **questionnaires** |
| **AO3** | buyers of the ice creams **recommend Cadbury** to friends; **loyal customers are more likely to try** whatever it launches next | greater **brand awareness** makes it stand out so existing customers stay; reliable information → **more accurate targeting → competitive edge over other pet businesses** |
| **AO4** | **bad publicity** about the ice creams could reduce sales and damage reputation; to keep loyalty it may have to offer **special deals or free gifts** on old and new products | **time-consuming** to market — approaching in-store customers or detailing the website; customers **may still try the new pet business if it charges a lower price** |

> ## `[CONSTRUCTED GRADE 9 TARGET]` — PPS
>
> Marketing is everything a business does to find out what customers want and to persuade them to buy: the research, the branding, the promotion and the relationships. For PPS, which already has customers and something to lose, marketing has a specific job — it is what stops the pet business down the road from taking them.
>
> Marketing informs customers of the products the business is offering, and it can build long-lasting customer relationships. PPS can remind customers with information about the products it offers, such as the CCTV cameras in the pet hotel, and it can identify customer needs by giving its own customers questionnaires to get feedback. That matters because a pet owner's decision is built on trust — they are handing over an animal — so being the business that asks and then acts on the answer is how it keeps its market share.
>
> It is important for PPS to create greater brand awareness to make it stand out against the competition so that existing customers remain with PPS. If PPS gathers enough reliable information from its customers, they may be able to identify customer needs and target its products and services more accurately, giving them a competitive edge over other pet businesses — for example by finding out that owners want grooming as well as boarding, and offering it before a rival does.
>
> However, it can be time-consuming to market the business, as PPS will need to approach the customers that come in store or provide detailed information on their website to keep it competitive. This may not work either: some of its customers may still try the new pet business if it is charging a lower price than PPS, because no amount of awareness makes a customer pay more for the same service.
>
> Overall, marketing is very important to PPS, but only if it is used on the right customers. This depends on whether its customers choose on service — where its reputation protects it — or on price, where a cheaper rival wins regardless. In the short term the research and the website take time that the staff could spend on pets, but in the long term knowing exactly what its customers want is what keeps them from trying the new business at all.

⭐ **The two papers ask the same AO1 in opposite directions.** Cadbury's marketing is *about a gap in the market*; PPS's is *about a relationship already held*. **Use the question to pick the direction: "introducing a new product" → research and trial; "keep its market share" → awareness and retention.**

---

## 235. PROMOTION — technology against the traditional mix, and why the *variety* matters

**Asked:** *"Evaluate the benefits to **Lavender** of using other forms of technology to promote its products."* — **May 2019 P1R 4(c)**, bakery with outlets and recipes · *"Evaluate the importance to **Kraft Heinz** of using a variety of different methods to advertise to its target customers."* — **November 2023 P2 4(c)**, including the tomato sauce advertised by Ed Sheeran.

| | **Lavender** (2019 P1R) | **Kraft Heinz** (Nov 2023 P2) |
|---|---|---|
| **AO1** | **social media** reaches a wider target market; **e-newsletters** keep customers up to date with new products | using a **variety** such as television advertisement attracts a variety of different people; posters or billboards |
| **AO2** | target a particular audience based on their **liking for food** and advertise directly to them; collect email addresses of customers or run questionnaires | the **Ed Sheeran** advertisement attracts a **younger person** who is keen on his music and would want to try the tomato sauce; a poster advertising a **new variety of baked beans**, displayed in towns and cities |
| **AO3** | **personalise** information from what a customer has searched for or bought before; reach current customers and encourage **repeat purchase** or to try other outlets or recipes | they are encouraged to try it **because someone famous has used it and they want to follow**; a poster carries a **short, sharp message seen repeatedly** as people pass by |
| **AO4** | needs employees with **technological skills**; **people ignore emails or website banners**; hard to reach new customers in new areas because it does not yet know who they are; **some customers prefer traditional methods such as leaflets inside the bakery**, where you hand them over, give a more personalised service, and **speak to them face to face to gain feedback** | **no guarantee sales increase just because a pop star has been in the advertisement**; posters **get damaged** and it is **difficult to evaluate their effectiveness** |

> ## `[CONSTRUCTED GRADE 9 TARGET]` — Lavender
>
> Digital promotion is any use of technology to reach customers — social media, e-newsletters, the business's own website — rather than leaflets, posters or press. For a bakery with several outlets and a range of recipes, the question is whether that technology reaches the right people better than a leaflet in the shop does, and whether the custom it brings is worth the trade-off.
>
> Social media can be used to gain a wider target market, and e-newsletters can keep customers up to date with new products. Lavender could target a particular audience based on their likes of food and advertise directly to them, and it could collect the email addresses of its customers or complete questionnaires to build that list. The advantage over a leaflet is precision: using technology in promotion, Lavender can personalise the information to the customer based on what they have searched for on the internet or what they have purchased previously from the bakery. It can then reach out to current customers and encourage them to repeat purchase or to try out its other outlets or different recipes — which is exactly the behaviour a growing bakery chain needs.
>
> However, Lavender would need to have employees with the necessary technological skills in order to use this as a method of promotion, and that is a cost and a delay. Some people ignore emails or banners on websites and may not pay attention to the promotion at all, and it could be difficult to reach the new customers in the new areas, as it does not yet know who they are. A lot of time might be spent using technology when some people prefer traditional methods such as leaflets inside the bakery: handing them out directly gives more of a personalised service and the chance to speak to customers face to face and gain feedback — which a newsletter cannot do.
>
> Overall, technology is beneficial to Lavender, but only as one part of its promotion. This depends on whether its customers are already online and already know the brand, and on whether it has the staff to run the channels properly. In the short term the skills and the time are a cost, but in the long term a bakery that can personalise what it sends will get repeat orders from customers it would otherwise have to keep winning back.

⭐ **The best AO4 in this entry is not "it costs money" — it is the *comparison*.** Pearson's own wording puts leaflets **head to head** with email: *you get the chance to speak to them face to face to gain feedback.* **When the question offers "a different method", the counter-argument is what the other method does better.**

⚠️ **Kraft Heinz is not "advertising is good".** Its question is specifically about **variety**, and the scheme's two AO4s are about **proof and wear-out**: a celebrity endorsement does not guarantee sales, and posters physically degrade and cannot be measured. **If your answer never mentions using more than one method, you have not answered this question.**

---

## 236. CHANGES IN THE MARKET — three papers, three different things that changed

**Asked:** *"Evaluate the importance of **Apple** responding to changes in the market."* — **June 2026 P2R 4(c)** · *"Evaluate how changes in consumer spending patterns and competition may affect a business such as **Emirates**."* — **May 2020 P2 4(c)** · *"Evaluate how **Four Fitness** may respond to the changes in the market."* — **May 2025 P1 4(c)**, a small gym owned by Gianni.

| | **Apple** (2026 P2R) | **Emirates** (2020 P2) | **Four Fitness** (2025 P1) |
|---|---|---|---|
| **The change** | changing **customer needs** and **spending patterns** — customers want new features, apps and folding devices, while some have **limited income and want cheaper phones** | **increased consumer spending** and the entry of **low-cost airlines** | customers expect **up-to-date equipment and knowledgeable instructors**, while many now **work out at home from internet videos at lower cost** |
| **AO2** | must consider changing trends when it designs a new smartphone; may need to consider **competitors' prices, such as Huawei's** | more spending → **more people taking overseas holidays**; a low-cost airline gives consumers **more choice** | Gianni needs up-to-date equipment and instructor knowledge; the online shift gives people a **cheaper alternative** |
| **AO3** | a **wider range of devices, such as foldables**, reaches new customers and increases competitiveness; if economic factors worsen, **fewer can afford a smartphone and Apple loses market share** | increased demand → **higher revenue**; but reduced market share → **lower revenue** | a growing industry could **draw health-conscious individuals to Four Fitness** over other gyms; the threat must be **addressed to keep customers** — e.g. its **own online videos at a small charge, from a qualified instructor** |
| **AO4** | Apple is **innovative and constantly updates its devices**, so it **may already be responding**; it has **many loyal customers willing to pay the high price**, and a **lower-priced smartphone may not be advantageous** | higher demand is **hard to serve** — a **shortage of pilots** because of the time taken to train them, and of **suitable aircraft**; if it offers the **best service** it could **regain its prime position**, since not everyone wants to fly low-cost | changes are **fast-paced**, and as a **small business** it **may not have the funds to keep up**; **bigger gyms offering more services at a more reasonable price** may outcompete it because they offer more choice |

> ## `[CONSTRUCTED GRADE 9 TARGET]` — Four Fitness
>
> A business has to respond to changes in the market because its customers' needs and its competitors' offers are not fixed. For Four Fitness the two changes that matter are what customers now expect from a gym, and how much they are willing to pay for it when the internet offers exercise at home for nothing.
>
> Gianni needs to make sure the gym equipment and the knowledge of the instructors are up to date so the new needs of customers are met. As more people use the internet to view fitness videos, there is now more choice between paying to go to the gym and working out from home at a lower cost. With a growing industry, keeping up to date could draw in health-conscious individuals to Four Fitness over the other gyms in the area. The online shift is also a threat that Four Fitness would have to address in order to keep its customers — one response being to introduce its own online videos, charging a small amount and offering an additional service from one of its qualified instructors, so that the customers who leave the gym to train at home do not leave the business as well.
>
> However, there are a lot of fast-paced changes in customer needs, and as Four Fitness is only a small business, it may not have the funds to keep up with all of them. New equipment and continual instructor training both cost money that a small gym may not have. Bigger gyms offering more services at a more reasonable price may also outcompete Four Fitness, as they may offer more choice — classes, pools and 24-hour access that one small gym cannot match on either scale or price.
>
> Overall, Four Fitness must respond, but it can only respond to some of what changes. This depends on whether its members value the personal attention only a small gym can give, or whether they are buying on equipment and price, where the bigger chains win. In the short term new equipment and online content reduce profit, but in the long term a small gym that keeps its instructors genuinely expert is the one that can charge for what home video cannot give.

⭐ **The same AO1 appears on three papers — "changes in customer needs" and "changes in consumer spending patterns" — and the AO4 differs completely.** Apple's is *we may not need to change*; Emirates' is *we may not be able to supply it*; Four Fitness's is *we may not be able to afford it*. **Read your case for its constraint before writing the counter-argument.**

---

## 237. COMPETITIVE ADVANTAGE — how it is gained, and how it is kept

**Asked:** *"Evaluate how **Yellow** may have gained a competitive advantage in the clothing market."* — **May 2019 P2R 4(c)** · *"Evaluate how **LEGO** has maintained a competitive advantage in the making of toys and games."* — **May 2022 P2 4(c)**.

| | **Yellow** (2019 P2R) — *gaining it* | **LEGO** (2022 P2) — *maintaining it* |
|---|---|---|
| **AO1** | customers buy Yellow clothing because of its **wide variety**; Yellow has **low manufacturing costs** | customers buy LEGO because it is **well known and has traded for a long time**; the toys are **good quality and should last** |
| **AO2** | clothing for **all the family** at **different price ranges**; it responds **quickly to changes in the fashion market** demanded by its customers | **'Toy of the Century' twice**, so people can **rely** on the products; **keeps up to date with new films** such as Harry Potter |
| **AO3** | customers want **a reasonable price** and to **shop for the whole family in one store**; responding quickly to demand changes puts it **ahead of competitors** | customers want toys they **know are reliable and well made**; **fans of the film will want the new LEGO toys** |
| **AO4** | **not all members of the family have the same taste** and some prefer different styles; **not all customers are driven by fashion** — many want clothing that **lasts a number of years** | **no guarantee** customers will buy, because the products are **expensive** and they **may want a cheaper product**; **if the film is not a success the toys may not sell**, and LEGO will have **wasted the time and investment** |

> ## `[CONSTRUCTED GRADE 9 TARGET]` — LEGO
>
> A competitive advantage is something a business does better than its rivals that customers are willing to pay for. LEGO's is unusual because it has lasted decades: it is the brand's reputation and the quality of the bricks themselves, reinforced every time a new film gives children a new reason to want a set.
>
> Customers purchase LEGO toys and games because they are well known and have been trading for a long time, and because the toys are of a good quality and should last a long time. LEGO has achieved 'Toy of the Century' twice, meaning that people can rely on the products made, and it keeps up to date by making toys to correspond to new films that are introduced, such as Harry Potter. That combination is what maintains the advantage: customers want to purchase toys and games that they know are reliable and well made, and fans of Harry Potter will want to purchase the new LEGO toys — bringing in children who had never asked for LEGO before, while the adults buying the sets are buying a brand they already trust.
>
> However, there is no guarantee that customers will buy some of the products, because they are expensive and they may want a cheaper product. Rival brands and generic bricks sell for a fraction of the price, and a parent comparing two boxes of bricks may not see the difference the brand is charging for. If the film is not a success, then the toys may not sell and LEGO will have wasted the time and investment in producing the toys — the licence, the design and the tooling all paid for before anyone knows whether the film will be watched.
>
> Overall, LEGO has maintained its competitive advantage well, but it depends on two things outside its control. This depends on the quality of the films it ties its sets to, and on whether parents continue to value the brand over a cheaper equivalent. In the short term the film tie-ins bring spikes of revenue, but in the long term it is the reliability of the brick itself, and the reputation that rests on it, that keeps customers coming back.

⚠️ **Single-word meanings matter here.** "Gained" (Yellow) invites an *origin* answer — low costs, quick response, wide range. "Maintained" (LEGO) invites a *sustainability* answer — reputation, quality, staying current. **Answer the verb you were given.**

---

## 238. MEASURING SUCCESS — the factors a business chooses, and what they leave out

**Asked:** *"Evaluate the factors that make a business, such as **HRMW**, successful."* — **May 2020 P2R 4(c)** · *"Evaluate the factors that **NOF** might consider when measuring the success of its farm shop."* — **May 2021 P1 4(c)**, a farm with a shop and overnight accommodation.

| | **HRMW** (2020 P2R) | **NOF** (2021 P1) |
|---|---|---|
| **AO1** | success can be judged by **changes in revenue**; and by **customer satisfaction** | the **profit produced by the farm shop**; the **growth of its product range** |
| **AO2** | between 2020 and 2022 HRMW's estimated revenue is **set to increase by 8.51%**; if customers are satisfied with the goods they **will return** | NOF can see how much profit the farm shop makes **compared with the overnight accommodation**; expanding its product range **shows it is currently successful in the products it already sells** |
| **AO3** | comparing revenue with competitors' gives an **indication of relative success**; happy customers **spread the word to family and friends → increased demand → increased sales** | comparing profit lets NOF **spend money improving the areas that need developing**; the willingness to expand **shows there is demand** and that it is **willing to take a risk** |
| **AO4** | revenue is **only part of success** — **shareholders receiving dividends** may **conflict with HRMW's plans for expansion**; **customer satisfaction may require changes in prices**, affecting revenue and profits and producing a **less successful business** | profit depends on **factors outside NOF's control, such as the weather**, which affects **how much the farm produces and how many people visit**; **no guarantee the growth will succeed** when **supermarkets sell the same products more cheaply** and other farms can afford to |

> ## `[CONSTRUCTED GRADE 9 TARGET]` — HRMW
>
> Success for a business is not a single number: it is whatever the owners decide matters — profit, revenue, satisfied customers, survival or growth. HRMW can judge its success by looking at changes in its revenue, and it can also measure it by customer satisfaction, and the two together say more about the business than either alone.
>
> Between 2020 and 2022 HRMW's estimated revenue is set to increase by 8.51%, which is the clearest evidence that it is growing rather than standing still. Customer satisfaction matters because if customers are satisfied with the goods, they will return — and in a market where customers can buy the same sort of product elsewhere, returning customers are cheaper to keep than new ones are to win. If HRMW compares its revenues with those of its competitors, it gives it an indication of its relative success: growing is one thing, growing faster than the competition is another. And if customers are happy with the sports products, they will spread the word to family and friends, which could increase demand for these products leading to increased sales — a measure that shows up in revenue only later.
>
> However, revenue is only a part of the success of the business. There are other factors to be considered, such as shareholders receiving dividends on their investment, and this may conflict with HRMW's plans for expansion: the money paid out to shareholders is money not spent on new stock or new premises. Customer satisfaction may also require changes in prices, and this could impact on revenue and profits, leading to a less successful business — a discount may please customers while lowering exactly the figure that was being used to measure success.
>
> Overall, using both measures together is a sound approach, but only if HRMW knows which one it is running the business for. This depends on whether its shareholders want income now or growth later, and on which of the two measures lags the other. In the short term revenue is the easier measure and the more volatile one, but in the long term customer satisfaction predicts the revenue that has not arrived yet.

⭐ **Both papers put a *limit* on measurement, and the two limits are different ideas.** HRMW's is **conflict between stakeholders** (dividends vs expansion). NOF's is **factors outside the business's control** (the weather, cheaper supermarkets). **Use your case's limit — the scheme marks the one it printed.**

---

## 239. MEASURING SUCCESS BY PROFIT ALONE — the strongest counter-argument in the tier

**Asked:** *"Evaluate why a business such as **Premier Inn** would only consider profit to measure its success."* — **November 2024 P2 4(c)**, a hotel chain opening hotels around the world.

> ## `[CONSTRUCTED GRADE 9 TARGET]`
>
> Profit is total revenue minus total costs, so it is the one measure that shows whether everything a business does is adding up to more than it spends. It is also the easiest measure to compare: between hotels, between years, and between the business and its rivals. That is why a chain such as Premier Inn might judge each of its hotels on profit alone.
>
> The more profit that is made from each Premier Inn will show how successful they are, because profit signifies if the total revenue of the business exceeds its total costs. Premier Inn will be able to see how much profit each hotel is making and compare it to other hotels, which turns one number into a league table of its own sites. That matters while it is planning to open more hotels in different parts of the world, because it will be able to see if these new hotels are making a profit — and only profit tells it whether a new site is paying for itself or being subsidised by the older ones. By comparing the profit from each of the Premier Inns it can use the profit to develop or increase the size of certain hotels, moving investment to where it earns most.
>
> However, an increase in profit is dependent upon many factors outside the control of Premier Inn, such as travel restrictions that stop people from travelling. A hotel chain can be run perfectly and still lose money because a border closed — and a measure that moves for reasons the business cannot control cannot be the only measure. There are also other ways to measure business success such as market share and customer satisfaction, which might be as equally important as financial measures: a hotel with a full car park and high satisfaction scores is building the repeat business that produces next year's profit.
>
> Overall, considering profit alone is not enough, although it is not unreasonable as a short-term management measure. This depends on how much competition the chain faces and how long-term its owners' plans are, because market share and satisfaction lead profit rather than follow it. In the short term profit is the fastest signal of whether a hotel is working, but in the long term a chain that cuts quality to protect the figure will watch the same figure fall.

⭐ **The question contains the trap in its own wording.** *"Why a business **would** only consider profit"* asks you to **explain the case for** using one measure — so the AO1/AO2/AO3 paragraphs must genuinely justify it, and only then does the "However" turn. **An answer that criticises profit from the first line has answered the opposite question.**

---

## 240. SOCIAL OBJECTIVES — success by something other than profit

**Asked:** *"Evaluate the extent to which social objectives may contribute to the success of **Spud Bros**."* — **June 2026 P1R 4(c)**, jacket potatoes in Preston, feeding the homeless and helping sick children · *"Evaluate the impact on **AWG** of having these social objectives when planning to grow the business."* — **November 2023 P1 4(c)**, clothing re-used from natural materials.

| | **Spud Bros** (2026 P1R) | **AWG** (Nov 2023 P1) |
|---|---|---|
| **AO1** | goals set by a business **to benefit society or the environment**; objectives that focus on the **community rather than profit** | social objectives aim to **benefit society**; they focus on **ethical factors other than profit** |
| **AO2** | **feeding the homeless in Preston** may attract more **ethically conscious consumers**; the **brand image improves** if it helps **sick children throughout the UK** | encouraging families to **re-use clothing made from natural materials** and **reduce waste**; in the workshops **waste is kept to a minimum and spare material is used to make hats and scarves** |
| **AO3** | more sales of food → the **extra revenue helps the brothers with their ambitious expansion plans**; **word-of-mouth recommendations** → a **competitive advantage in the food market** | meets the needs of **customers who care about the environment and want a sustainable range**; **minimising waste reduces costs, and the savings can be passed on to customers to encourage more sales** |
| **AO4** | **free meals increase costs** → **lower profit margins** and may **delay expansion in the UK and internationally**; **other factors may be more important** to success, including **proving quality meals and good customer service** | **natural material is more costly** → a **high price for the jumpers and dresses** → discourages some people → **slow growth**; **many people are not concerned about social objectives or the environment** and care more about **current fashion** → **decrease in sales revenue** |

> ## `[CONSTRUCTED GRADE 9 TARGET]` — Spud Bros
>
> Social objectives are goals set to benefit society or the environment rather than to make money — feeding people who cannot pay, or reducing what the business throws away. For Spud Bros, giving food to the homeless in Preston and helping sick children is not a marketing campaign: it is a cost, and the question is whether it earns back more than it spends.
>
> Feeding the homeless in Preston may help to attract more ethically conscious consumers, and the brand image of the business will improve if it helps sick children throughout the UK. That matters commercially because both effects reach customers the brothers would otherwise have to pay to find: this could result in more sales of food, and the extra revenue would help the brothers with their ambitious expansion plans. It will also result in word-of-mouth recommendations for the business, which will help it to gain a competitive advantage in the food market — a queue outside a stall that is known for giving food away is a queue that costs nothing to build, and rivals selling the same jacket potatoes cannot copy the story.
>
> However, providing free meals to the homeless will increase costs for the business, which will lead to lower profit margins and may delay the expansion plans in the UK and internationally — the food given away is food that was paid for. Other factors may be more important in determining the success of the business too, including proving quality meals and good customer service: a customer who came because of the charity and was served a poor jacket potato by a rude server will not come back, and no social objective survives that.
>
> Overall, social objectives contribute to Spud Bros' success, but only to a limited extent. This depends on whether the customers who notice the charity are also the ones buying the food, and on how much of the margin the brothers are prepared to give up while expanding. In the short term the free meals reduce profit, but in the long term the reputation they build is the cheapest advertising a small food business can get.

⭐ **AWG contains the counter-argument most candidates miss: the material itself.** *"It may be more costly to use natural material which may result in a high price"* — **the ethical choice raises the price of the product**, so the very customers it wins are the ones it may price out. Spud Bros' is a *cost* argument; AWG's is a *price* argument. **Both are "However", and they are not interchangeable.**

---

⚠️ **This question has a `[VERIFIED CANDIDATE EXEMPLAR]` printed beside it — read it before writing your own.** **June 2026 P1R Q4(c), Spud Bros — 11/12**, the highest-marked 12-mark script the bank holds, with its examiner comment: *"They offer balance in their argument with appropriate levels of context throughout the response."* **Note that this one DOES end with an explicit "In conclusion" paragraph — and it balances rather than summarises.** Compare the **6/12 printed on the same pages**: identical chains, no drawback, no second half of the argument. Both are transcribed in `02_Verified_Exemplars.md`; the mark scheme's own AO4 for this paper is at the head of this entry.

## 241. PUBLIC RELATIONS — the same facts as social objectives, a different question

**Asked:** *"Evaluate the effect for **Rabanne** of working hard to maintain and improve its public relations."* — **May 2025 P2R 4(c)**, donating to charities, refillable glass bottles and sustainable packaging.

> ## `[CONSTRUCTED GRADE 9 TARGET]`
>
> Public relations is how a business manages what the public thinks of it — the impression left by what it says, what it gives, and what it does to the environment. For a fragrance and fashion brand such as Rabanne, whose customers are buying a name as much as a scent, that impression is part of the product.
>
> By donating funds to various charities, Rabanne highlights to customers that it wants to help the communities it operates in, and by decreasing the impact on the environment by using sustainable material in its packaging, it answers the criticism that luxury goods are wasteful. The effect on the customer is direct: customers are more likely to purchase the aftershave Invictus because they know that Rabanne helps people out, and less packaging is used for its Lady Million perfume, which reduces both the cost of materials and the waste the customer has to throw away. Rabanne will also gain more interest from charities around the world because of the donations it makes, which could increase the number of people who want to purchase its perfume as they are seen to care for the environment — turning a donation into publicity that money alone could not buy.
>
> However, not everyone is interested in Rabanne's donations: they would be more interested in the perfumes and aftershaves the business produces. A customer choosing a fragrance buys on scent, price and brand image, and may never read the packaging note about refillable bottles. There is also no guarantee that a business caring for the environment will see a positive change in its sales volume — the rival that spends nothing on charity may simply undercut it, and a customer who agrees with the principle may still buy the cheaper bottle.
>
> Overall, working on public relations has a positive effect for Rabanne, but it is a supporting factor rather than a deciding one. This depends on whether its customers are buying the scent or the story, and on whether rivals' environmental records are visibly worse. In the short term the donations and the refillable packaging add cost, but in the long term, for a brand whose price depends on desirability, a good reputation is what keeps customers willing to pay it.

⚠️ **This paper's AO1 looks like social objectives — and its question does not.** The mark scheme's own AO1 is *donating funds as public relations* and *reducing environmental impact through packaging*: the subject is **reputation management**, not ethics. **Answer the question on the paper in front of you, even when the case facts are the same.**

---

## 242. MARKET ORIENTATION — does following the customer guarantee anything?

**Asked:** *"Evaluate the extent to which market orientation will guarantee the future success of **Nando's**."* — **June 2026 P2 4(c)**.

> ## `[CONSTRUCTED GRADE 9 TARGET]`
>
> Market orientation means considering the opinions and preferences of the target market — basing a product on customers' needs and wants rather than on what the business itself thinks is right for the customer. For a restaurant chain such as Nando's this shapes both the menu and the marketing, and the word that decides the answer is *guarantee*.
>
> Market orientation will allow Nando's to understand what foods and tastes consumers prefer, and researching new dishes will help Nando's to assess whether new meals on its menu may be successful before they are launched across every restaurant. This may allow Nando's to sell meals that suit the tastes of its customers and encourage repeat purchases, which matters in a restaurant market where customers can switch on one bad visit. Nando's can also make changes to its new dishes before launching them in all restaurants, reducing the risk of new dishes not being popular — a test kitchen is far cheaper than a failed national launch, and it means the menu improves on evidence rather than on instinct.
>
> However, researching trends and preferences takes time, and other restaurants may respond more quickly to changes in food trends. If a rival launches the same dish first, Nando's has paid the research cost without gaining the advantage, and in food the first mover is often the one people remember. Nando's may also prefer to use a product-orientated approach and focus on developing and improving dishes based on what it believes is superior quality and innovation, rather than primarily on customer preferences or market trends — and this is a real option for a chain whose whole reputation rests on a flavour that customers come to it for. Chasing every preference could blunt the thing that makes the brand distinctive.
>
> Overall, market orientation will help Nando's to a large extent, but it cannot guarantee future success. This depends on how quickly trends shift in its market and on whether it can act on its research faster than its rivals can. In the short term the research adds cost and delay to every launch, but in the long term a menu built on what customers actually order is a safer bet than one built on what the business believes is best.

⭐ **The word *guarantee* is the marker's instruction to argue a limit.** The scheme's AO4 gives two: research is **too slow** to be a promise, and the **product-orientated alternative may be better**. **Whenever a question says "guarantee" or "will", the answer must contain something that could still go wrong.**

---

# BATCH 8c — 12-MARK EVALUATE, PART 3: THE SINGLETONS (entries 243–252)

> **Ten topics that appear once in the whole qualification.** Each still gets a full model, because a topic that has appeared once on a past paper is a topic that can appear again — and the reasoning is what transfers, not the case.

## 243. DEMOGRAPHIC SEGMENTATION — slicing the market by who people are

**Asked:** *"Evaluate the importance to **IKEA** of using demographic segmentation when targeting its customers."* — **May 2023 P2 4(c)**.

| Move | The scheme's content |
|---|---|
| **AO1** | targeting certain groups such as **families with young children**; taking the **income of customers** into account, as it varies from country to country |
| **AO2** | **younger families** need tables and chairs that are **reasonably priced and suitable for young children**; customers with a **larger income may want expensive-looking tables and ornaments** to display their wealth |
| **AO3** | the **older generation** may need **reliable and comfortable chairs**; IKEA must take this into account when deciding **what furniture to sell in each country** |
| **AO4** | **not all families fit into a category**, so IKEA needs to provide for **all demographics wherever it is located**; **no guarantee customers will buy what is expected of them** |

> ## `[CONSTRUCTED GRADE 9 TARGET]`
>
> Demographic segmentation divides a market by measurable characteristics of people — age, income, family size, occupation. Using demographic segmentation, IKEA can target certain groups of people such as families with young children, and it will take into consideration the income of its customers, as this varies from country to country. For a furniture retailer selling in dozens of markets, that is a practical starting point.
>
> Younger families are going to need tables and chairs that are reasonably priced and suitable for young children, while some customers with a larger income may want expensive-looking tables and ornaments to display their wealth. These are two different shops within the same store, and segmentation is what tells IKEA to stock both and to place them where their customers will find them. It also guides what to send to each country: the older generation may need reliable and comfortable chairs to sit on, and IKEA will need to take this into account when deciding what items of furniture to sell in each country, rather than shipping the same catalogue everywhere.
>
> However, not all families fit into a category, and therefore IKEA needs to provide for all different demographics no matter where they are located. A single customer may be a young parent with a low income and a taste for design, and a range built strictly on one segment would lose them. There is also no guarantee that IKEA's customers will buy what is expected of them: people do not buy predictably, and a shopper segmented as a budget buyer may spend the most in the store on the day.
>
> Overall, demographic segmentation is important to IKEA, but it is a starting point rather than a guarantee. This depends on whether its customers are shopping for a home, where income and family size decide the purchase, or for an individual taste that cuts across every group. In the short term it makes the ranges and the warehouses more efficient, but in the long term the retailer that also watches how customers behave, and not only who they are, is the one whose ranges keep selling.

⚠️ **The four AO4s in this tier that begin "there is no guarantee" all mean the same thing — human behaviour is not determined.** Where the scheme prints it (IKEA, Cadbury, Starbucks, Kraft Heinz, M&M), **write it as the customer's choice, not as the business's failure.**

---

## 244. CHOOSING A LEGAL STRUCTURE — private limited company against staying as you are

**Asked:** *"Evaluate whether **TADS** should consider becoming a private limited company."* — **May 2020 P1 4(c)**, a one-man music business run by Ollie.

| Move | The scheme's content |
|---|---|
| **AO1** | a private limited company **suits small and medium-sized businesses**; in one, the **shareholders can only lose the money they invest** |
| **AO2** | as a **one-man business** becoming a private limited company means Ollie could **raise more funds from family and friends**; TADS would have a **separate legal identity**, so the **business could carry on if anything happened to Ollie** |
| **AO3** | Ollie can **control who the other owners will be**, choosing people with an **interest in music who can invest**; **his personal possessions are protected**, as are his shareholders' — the **risk for shareholders is reduced** |
| **AO4** | Ollie may **not get a lot of interest**, so cannot raise large amounts, which **slows his expansion plans**; he may find it **easier to take a bank loan** rather than change the legal ownership at all, **so he does not lose any control**; becoming Ltd means **more paperwork**, and **some information must be shared publicly** — **which could interest his competitors** |

> ## `[CONSTRUCTED GRADE 9 TARGET]`
>
> A private limited company is an incorporated business owned by its shareholders, whose shares are not sold to the general public. For Ollie, who currently owns TADS alone, the question is not which structure is better in general, but whether incorporation brings him the money he needs at a cost he can accept.
>
> A private limited company is a suitable type of ownership for small and medium-sized businesses, and in a private limited company the shareholders can only lose the money they invest. As a one-man business becoming a private limited company means Ollie could raise more funds from family and friends, and TADS will have a separate legal identity, meaning the business could carry on if anything happened to Ollie. That second point matters more than it looks: TADS's reputation and contacts are built on Ollie, and incorporation means the business survives him, which is what a lender or an investor needs to know.
>
> If TADS opts for a private limited company, then Ollie can control who the other owners will be, allowing him to choose people who have an interest in music and can invest in the business. Having Ltd status means that Ollie's personal possessions are protected, as are those of his shareholders, so the risk for shareholders is reduced — and that is what persuades people to put money into a small music business in the first place.
>
> However, Ollie may not get a lot of interest, so cannot raise large amounts of money, and this can slow down his expansion plans. He may find it easier to opt for another source of finance such as a bank loan rather than change the legal ownership of the business, so he does not lose any control of the business — and for a founder with a clear musical vision, that control may be worth more than the money. Becoming a Ltd will also involve an increase in paperwork, and some information will have to be shared publicly, which could be of some interest to Ollie's competitors.
>
> Overall, TADS should become a private limited company, but only if Ollie actually intends to bring in investors. This depends on whether he needs more capital than a bank will lend, and on whether he is willing to share decisions about the business to get it. In the short term the paperwork and the public accounts are an administrative cost, but in the long term limited liability and a separate legal identity are what allow a one-man business to grow beyond one man.

⚠️ **"Whether" questions are answered "yes, but…".** The correct first sentence names the choice and the condition under which it holds — *"should, but only if he actually intends to bring in investors"*. **A "maybe" answer scores no AO4.**

---

## 245. CENTRALISED OR DECENTRALISED — where decisions are made

**Asked:** *"Evaluate whether a centralised organisation structure will benefit **Samsung**."* — **November 2025 P2 4(c)**, factories in 74 countries, head office in Seoul.

| Move | The scheme's content |
|---|---|
| **AO1** | a centralised structure is one where **decisions are made at the headquarters**; usually **by the CEO and other senior managers** for the whole business |
| **AO2** | major decisions on the **design and development of smartphones** made in **South Korea to speed up decision making**; **economies of scale if TVs are standardised**, and marketing organised centrally |
| **AO3** | **reacts quickly to changes in technology** — vital in the competitive smartphone market to **maintain market share**; **lower unit costs allow lower TV prices**, helping it remain the **leading supplier** |
| **AO4** | **lack of authority lower down may demotivate managers** → **lower productivity, employees leaving, higher costs and lower profit**; **local managers outside South Korea may understand local needs better** and be better placed to attract customers |

> ## `[CONSTRUCTED GRADE 9 TARGET]`
>
> In a centralised organisation, decisions for the whole business are made at the headquarters — at Samsung, in Seoul, by the CEO and senior managers. With 270,000 employees and factories in 74 countries, the question is whether holding decisions at the centre is what keeps the products consistent and quick to market, or what stops the business hearing its customers.
>
> This means that major decisions on the design and the development of smartphones will be made in South Korea to speed up decision making, because the people with the fullest picture of the whole product range are the ones deciding what the next model contains. It also means that Samsung can benefit from economies of scale if TVs are standardised and the marketing can be organised centrally: one campaign for one product, wherever it is sold, costs far less than seventy-four separate ones. This will ensure Samsung can react quickly to changes in technology, which is of importance in the competitive smartphone market to ensure it maintains its market share, and a reduction in unit costs may help reduce prices of the TVs to help them remain the leading supplier in the industry — where in consumer electronics the price leader usually ends up being the volume leader too.
>
> However, a lack of authority lower in the organisation may demotivate managers, leading to lower productivity or employees leaving their jobs, resulting in higher costs and lower profit levels. A manager with a title but no decisions is not a manager for long. Local managers in the factories and offices outside South Korea may also have a better understanding of local needs and be in a better position to attract more customers — a marketing message written in Seoul may not travel, and a product designed for one market may be wrong in another.
>
> Overall, a centralised structure will benefit Samsung, but not everywhere and not equally. This depends on whether the product is genuinely the same worldwide, as with a flagship smartphone, or whether it has to adapt to local taste and local competition. In the short term centralising keeps standards and costs in line, but in the long term the business that lets its local managers decide what their customers need is the one that keeps them.

⭐ **The AO4 here is not financial — it is motivational.** *Lack of authority demotivates managers.* **The same fact is also the AO1 of the motivation and job-design entries (209–217)** — a decision taken away is a motivator removed. **Cross-reference the tiers: the same syllabus point scores in different places.**

---

## 246. GROWING THROUGH A FRANCHISE — selling the right to use your name

**Asked:** *"Evaluate the benefits to **Ocean Vibes** of operating as a franchise to further expand its business."* — **November 2025 P1 4(c)**, boat tours in Portugal, founded by Alfred and Pedro to connect tourism with science.

| Move | The scheme's content |
|---|---|
| **AO1** | a franchise **gives another person or business the right to sell its products or services**; the **franchisor receives set-up / royalty fees** from the franchisee |
| **AO2** | franchisees can **offer boat tours in other tourist resorts**, assisting growth; Ocean Vibes **receives revenue from franchisees operating in other resorts in Portugal** |
| **AO3** | the **brand name is extended to other areas of Portugal** and this **encourages customer loyalty**; the **fees can be invested in wildlife research**, fulfilling Alfred and Pedro's goal of **connecting tourism with science** |
| **AO4** | **risk of reputational damage if franchisees do not operate the boat tours responsibly**; there are **many competitors in the boat tour market** and **they may fail to find franchisees willing to pay the fees** |

> ## `[CONSTRUCTED GRADE 9 TARGET]`
>
> A franchise is a business that gives the right to another person or business to sell its products or services, in return for set-up and royalty fees. For Ocean Vibes, franchising is a way to grow across Portugal without the founders buying a second boat or being on it.
>
> Franchisees can assist in the growth of Ocean Vibes by offering boat tours in other tourist resorts, and Ocean Vibes will receive revenue from the franchisees operating in other tourist resorts in Portugal. That revenue arrives before the tours are run, because the set-up fee is paid up front and the royalty is a share of what the franchisee takes. This will allow the brand name of Ocean Vibes to be extended to other areas of Portugal and encourage customer loyalty, since a tourist who enjoyed a trip in one resort will book the same name in the next — and the fees received by Ocean Vibes can be used to invest in the research of wildlife to fulfil the goal of Alfred and Pedro, which is to connect tourism with science. Growth and the founders' purpose are paid for by the same mechanism.
>
> However, Ocean Vibes risks the chance of its reputation being damaged if the franchisees do not operate the boat tours in a responsible manner. The customers see the franchisee's boat, not the founders, and a skipper who disturbs the wildlife or cuts the tour short damages a name that Ocean Vibes cannot control. There are also many competitors in the boat tour market, and Alfred and Pedro may fail to find franchisees who are willing to pay the franchise fees to Ocean Vibes — a franchise with no track record outside one resort is a difficult sale to someone risking their own money.
>
> Overall, franchising is a beneficial route for Ocean Vibes, but it trades control for speed. This depends on whether the brand is strong enough to attract franchisees, and on how tightly the operating standards can be enforced once it does. In the short term the set-up fees fund expansion that would otherwise need a loan, but in the long term the business's value is the name, and a single irresponsible franchisee costs more than a boat.

⚠️ **Both AO4s are about *the other party*.** The franchisee may not exist, or may not behave. **Every "grow through someone else" option in the bank — franchising, venture capital, agency — carries the same two risks: you may not find them, and you cannot control them once you have.**

---

## 247. VENTURE CAPITAL — money that takes a share and an interest

**Asked:** *"Evaluate the impact of using venture capital as a source of finance to fund the opening of **Can Culleretes**."* — **May 2022 P1R 4(c)**, a family restaurant reopening with its original history.

| Move | The scheme's content |
|---|---|
| **AO1** | **investors give a business money in exchange for a share of the profits**; an **external** source of finance, **often used for opening new businesses** |
| **AO2** | investors may have **skills in the food industry** to ensure the venture is a success; they could have **ideas the family does not like, such as the opening hours** |
| **AO3** | **enough money to set up without having to pay back any interest**, giving more chance of success from the start; if investors are **too involved**, the **historical story behind the original business may be lost**, leading customers to stay away |
| **AO4** | the family must **pay investors a share of the profits**, which may **upset the family members who are working hard while the investors get the rewards**; if there was an **agreement to pay investors back and then take back full ownership**, this could ensure success **and keep the business in the family long term** |

> ## `[CONSTRUCTED GRADE 9 TARGET]`
>
> Venture capital is money put into a business by outside investors in exchange for a share of the profits and, usually, a say in how it is run. It is an external source of finance often used for opening new businesses — which is exactly Can Culleretes' situation — and it is the price of the investors' involvement, not the money itself, that decides whether it is a good idea.
>
> Investors may have the skills in the food industry to ensure Can Café is a success, bringing experience the family has not had to buy, and the business will have enough money to set up without having to pay back any interest, which helps it have more chance of being a success from the start. That last point is the real financial advantage: a bank loan has to be repaid whether or not the restaurant fills, while an equity investor is repaid out of profit — so in the first difficult months, the venture capital is far gentler on the cash flow.
>
> However, investors could have some ideas that the family does not like, such as the opening hours of the café, and if the investors are too involved in setting up the business it may lose the historical story behind the original business, leading to customers staying away. For a restaurant whose appeal is a family heritage, that is not a small risk. The family will also have to pay the investors a share of the profits, which may upset the other family members, as they are the ones working hard to set up Can Café while the investors get the rewards.
>
> Overall, venture capital has a positive impact on Can Culleretes, but only if the terms protect what makes the restaurant worth visiting. This depends on how much the family gives away, and on whether the investors want a return or a role. In the short term the money arrives without interest and the doors open sooner, but in the long term the arrangement only works if the owners have an agreement to buy the investors out.

⭐ **The scheme supplies the sophisticated answer itself:** *"if the owners had an agreement to pay the investors back and then take back full ownership it could ensure the success of both businesses as well as keeping them in the family in the long term."* **A conclusion that proposes a term — a buy-back, a written agreement — is AO4 at its strongest, because it makes the judgement conditional and specific at once.**

---

## 248. FINANCIAL DOCUMENTS — what they can and cannot tell you

**Asked:** *"Evaluate the usefulness of financial documents to help **Aude Rose** when deciding to open a second shop."* — **May 2023 P1R 4(c)**, a flower shop.

> ## `[CONSTRUCTED GRADE 9 TARGET]`
>
> Financial documents are the records a business produces from its trading: the statement of comprehensive income, the statement of financial position and the cash flow forecast. The statement of comprehensive income can show the profit or loss the business has made by the end of its financial year, and the figures can show how capable the business is of expanding — which is precisely what Aude Rose is trying to judge.
>
> This can help the business see how profitable the flower shop currently is, and that is the first question any second site has to answer: a business that cannot make a profit in one shop will not make two. The documents will also be useful to show Aude Rose how much profit it has to be able to put towards the expansion, or to inform a bank of how much it needs to lend — a lender will want the figures anyway, so preparing them is not wasted effort. The financial documents outline the current position of the business and could include a cash flow forecast projecting net cash flow in the future, which matters more than profit for a new shop: a second branch needs cash for rent, stock and staff long before it needs to be profitable, and the forecast is the only document that shows whether that cash will actually be there.
>
> However, there are other factors that need to be considered, such as the figures from previous years as well as the affordability of running the new shop — one year's profit shows what happened, not what will happen. Other factors need to be taken into consideration, such as the location of the competition, which could make it difficult for the second flower shop to survive as a new business in that particular area, and no financial document records how many rival florists already trade on that street.
>
> Overall, financial documents are useful to Aude Rose, but they are necessary rather than sufficient. This depends on how much of past performance is likely to repeat, and on whether the barrier to the second shop is money or customers. In the short term the documents are what persuades a lender and sets the budget, but in the long term the shop succeeds on the street it is on, not in the accounts it was planned with.

⭐ **This paper comes with a published 4/12 dissection (rule 85), and it names the exact fixes:** one use given → **give another**; no application → **apply directly to Aude Rose**; wrong document named → **profit belongs to the statement of comprehensive income, not the cash flow forecast**; no conclusion → **answer the question, or say other factors should be counted** *(Pearson's own route to Level 3)*. **This entry is built to contain all four.**

---

## 249. CASH FLOW FORECASTING — a prediction that changes what the business does

**Asked:** *"Evaluate why **M&M** uses cash flow forecasting to help inform decision making."* — **May 2023 P2R 4(c)**, tractors and cars with electronic devices.

> ## `[CONSTRUCTED GRADE 9 TARGET]`
>
> A cash flow forecast estimates the money coming in and going out, month by month, and the net cash flow left over. M&M needs it not because it is short of ideas but because every decision it is considering — a new feature, a new specialist employee — has to be paid for before it earns anything.
>
> Using their cash flow forecast, M&M can predict net cash flow for the future, and if M&M predict that the cash inflow will be high then they may decide to invest in other areas of the business. Depending on whether there is sufficient funds, they could introduce additional features on the tractors, or the funds could be used to employ specialist staff who have skills in developing electronic devices on the new cars being produced. That is the forecast's real use: it tells the business not whether an idea is good, but whether this is the month it can afford it.
>
> If there are not sufficient funds, then M&M may decide to wait until they have the funds available, and this would then maintain their image of introducing new and innovative features to the cars. Waiting deliberately is a decision the forecast makes possible — without it, a business finds out it could not afford the investment only when a supplier's invoice arrives.
>
> However, a cash flow forecast is only a prediction and does not guarantee that the funds will be there in the future. Sales may fall short, a customer may pay late, or a machine may break down, and none of those appear in the forecast until they happen. There is also no guarantee that there will be sufficient cash to cover all the costs of employing the staff, or that the new features will be liked by customers — the forecast can tell M&M whether it can afford to build the feature, but not whether anyone will buy the tractor because of it.
>
> Overall, M&M is right to use cash flow forecasting, but it is a tool for timing rather than for choosing. This depends on how accurate its sales predictions turn out to be and on how much cash the business has in reserve if they are wrong. In the short term the forecast prevents the business from running out of money, but in the long term the decisions it enables are what create the sales the next forecast predicts.

⚠️ **"Cash flow ≠ profit" is the syllabus point this paper is built on.** The forecast may show a healthy month while the business is making a loss, or the reverse. **Say what the forecast is *for* — timing — and the AO1 looks after itself.**

---

## 250. INTEREST RATES — the cost of borrowed money, and who feels it

**Asked:** *"Evaluate the impact on **CCT** of an increase in the Chinese interest rate."* — **May 2025 P1R 4(c)**, bicycle tours in China, considering a loan for electric bicycles.

| Move | The scheme's content |
|---|---|
| **AO1** | the **cost of borrowing money**; the **rate of interest charged by the banks** |
| **AO2** | a loan to buy **electric bicycles** becomes **more expensive** if interest rates rise; **people living in China** pay more for borrowing and **may have less disposable income to spend on touring the country** |
| **AO3** | **an increase in fixed costs** → **more revenue needed to break even**; **reduced demand for the bicycle tours** → **lower revenue** and a **greater risk of business failure** |
| **AO4** | if CCT **strongly believe the loan will help them expand**, the risk may be **worth taking**, as the **additional revenue can cover the higher interest rates**; a rise in Chinese rates **may not affect foreign tourists**, so it **may have little impact on demand** for CCT's tours |

> ## `[CONSTRUCTED GRADE 9 TARGET]`
>
> The interest rate is the price of borrowing money, and for a business about to take out a loan it is the single most important number in its plans. CCT is considering borrowing to buy electric bicycles, and an increase in Chinese interest rates raises the cost of that decision before a single tour is sold.
>
> If CCT wants to take out a loan to cover the cost of buying electric bicycles, it will be more expensive if interest rates increase. That is a permanent addition to its costs, and it matters most to a business with fixed loan repayments: leading to an increase in fixed costs, this means more revenue will be required to be able to reach the break-even point, so every tour has to sell more places simply to stand still. There is a second effect through CCT's own customers, because people living in China will have to pay more for borrowing money and may have less disposable income to spend on touring the country — so the same rise that increases CCT's costs also reduces its demand, and this could lead to a reduction in the demand for the bicycle tours, lowering the revenue for CCT and increasing the risk of business failure.
>
> However, if CCT strongly believe that taking out a loan will help them to expand, then it might be worth taking the risk, as the additional revenue can be used to cover the higher interest rates — the electric bicycles could attract customers that the current fleet cannot. An increase in interest rates in China may also not impact the foreign tourists that visit the country, and therefore this increase in rates may have little impact on the demand for CCT's bicycle tours, since those customers borrow, earn and spend in their own currencies.
>
> Overall, an increase in Chinese interest rates will have a negative impact on CCT, but a smaller one than it first appears. This depends on how much of its demand comes from Chinese customers rather than foreign visitors, and on whether the electric bicycles win enough extra bookings to pay for the more expensive loan. In the short term the loan's cost rises and break-even moves further away, but in the long term demand from overseas tourists is what decides whether the expansion was worth financing at all.

⭐ **Two AO4s, and the strongest one is not financial — it is about *who the customers are*.** Rates in China cannot affect the spending of a German tourist on a cycling holiday. **When a question mentions a national economy, check whether the case's customers live in it.**

---

## 251. FINANCIAL METHODS OF MOTIVATION — paying people to work harder

**Asked:** *"Evaluate the impact of **Irsi Chocolatier** using financial methods of motivation on its employees."* — **May 2023 P1 4(c)**. **This is the verified 12/12 paper** — the full transcript and the examiner's comment are in `02_Verified_Exemplars.md`, and the anatomy is in rule 82.

| Move | The scheme's content |
|---|---|
| **AO1** | a **bonus** can be given to employees; a **promotion** could be awarded to an employee |
| **AO2** | motivating employees **if they meet targets of making and selling a certain amount of chocolate each month**; Irsi could **promote the hardest-working employee in the chocolate shop** |
| **AO3** | employees work harder and **produce/sell more, increasing revenue**; the promoted employee gets **additional responsibilities and a potential pay rise**, making them **more loyal** because they are promoted for their work |
| **AO4** | **if the same employee keeps getting the bonus each month**, the rest may be **demotivated** if they feel they have no chance of getting it, **lowering productivity**; with **only three employees**, the other two may feel **demotivated and unrecognised**, possibly leading to **increased staff turnover and a recruitment issue** |

> ## `[CONSTRUCTED GRADE 9 TARGET]`
>
> Financial methods of motivation reward employees with money or the prospect of it — a bonus for hitting a target, or a promotion that carries a higher salary. In a business as small as Irsi Chocolatier, which has only three employees, both work on the same assumption: that one person's reward lifts the whole team.
>
> A bonus can be given to employees, and a promotion could be awarded to an employee. This can motivate the employees if they meet their targets of making and selling a certain amount of chocolate each month, and Irsi Chocolatier could promote the hardest-working employee in the chocolate shop. This may push employees to work harder and produce or sell more products in order to meet their targets, therefore increasing the revenue for Irsi Chocolatier. The promotion works differently but in the same direction: it will motivate the employee as they will be given additional responsibilities with a potential pay increase, making them more loyal to the business as they are being promoted for their work.
>
> However, if the same employee keeps getting the bonus each month, then this may demotivate the rest of the employees if they feel they do not have a chance at getting the bonus, leading to a decrease in productivity. A target-based reward that one person always wins stops being an incentive and becomes a fact about the workplace. This would only be for one employee, since the business currently has only three, so the other two may end up feeling demotivated and unrecognised, possibly leading to an increase in staff turnover and creating a recruitment issue for Irsi Chocolatier — and in a three-person business, losing one person is losing a third of the workforce.
>
> Overall, financial methods of motivation will benefit Irsi Chocolatier, but their effectiveness could be limited because it depends on factors such as the nature of the employee: some employees are motivated by money and will respond to a bonus, while others value responsibility, trust or job enrichment more. With so few staff, the business cannot afford to demotivate two of them to reward one.

> ## 🏆 What the 12/12 actually did — and it is about 330 words
> **The examiner's words:** *"a strong response and indicative of a level 3 response… been able to bring in their own business knowledge to support their response. There is good context throughout the response as well as a balanced argument with a clear evaluation."*
> **It has no conclusion paragraph.** Its last paragraph *decides* — *"the effectiveness of using financial methods of motivation could be limited because it depends on factors such as nature of employee"* — and then it stops.
> **It brings in knowledge the case never mentions** (job rotation, job enrichment, "given more responsibilities and trust") to support that condition, and it gives **both official AO4 routes in one answer**: the drawback of the same option (*"it could compromise quality of products and lead to higher defects / spoiled chocolates"*) and the named condition.

⚠️ **This is the one paper in the tier where a verified full-mark script exists — use it as the template.** The three things to copy are: **short**, **applied throughout**, and **the condition is named**.

---

## 252. COMMUNICATION — internal and external, and what happens when it is uneven

**Asked:** *"Evaluate the importance of good internal and external communication to **TBTS**."* — **May 2022 P1 4(c)**, a toy business with suppliers of toys and wooden materials.

| Move | The scheme's content |
|---|---|
| **AO1** | **internal** communication is between **owners and employees**; **external** is between **owners and stakeholders such as suppliers and customers** |
| **AO2** | TBTS must make sure all employees are **aware of the toys it sells and the aims of the business**; TBTS can use **various external methods to communicate with its suppliers** of toys and wooden materials |
| **AO3** | internal: **better relationships → lower staff turnover**, employees **feeling valued and part of a team**; external: good communication with suppliers **improves the relationship**, as it **keeps them up to date with its business activity** |
| **AO4** | communication **has to be good for all employees or some may feel left out**, leading to **animosity between employees**; if communication is poor **the relationship would not work** and TBTS **could lose suppliers** |

> ## `[CONSTRUCTED GRADE 9 TARGET]`
>
> Communication is the passing of information between the people a business depends on. Internal communication happens between owners and employees; external communication happens between the business and outside stakeholders such as suppliers and customers. TBTS depends on both — on a workforce that knows what it is selling, and on suppliers of toys and wooden materials it cannot afford to lose.
>
> TBTS needs to make sure all employees are aware of the toys it sells and the aims of the business, because a member of staff who does not know what the business is trying to achieve cannot help it get there. Good internal communication can create better relationships, leading to lower staff turnover and making employees feel more valued and part of a team — which matters in a small business where every person's knowledge is difficult to replace. Externally, TBTS can use various external methods to communicate with its suppliers of toys and wooden materials, and good communication with its suppliers could lead to an improved relationship between TBTS and its suppliers, as it keeps them up to date with its business activity: a supplier who knows a busy season is coming can hold stock and offer better terms.
>
> However, communication has to be good for all employees, or some may feel left out, leading to animosity between the employees. In a small team, information shared with one person and not another is read as favouritism, and the effect on the workplace is worse than if nothing had been said at all. If the communication is poor, the external relationship would not work either, and TBTS could find that it loses suppliers — a supplier who is never told about delays or changed orders stops prioritising the business that does not talk to them.
>
> Overall, good communication is very important to TBTS, but only if it is even and consistent. This depends on the size of the team and on how much TBTS depends on its few suppliers, since being one customer among many gives it little protection if the relationship sours. In the short term better communication costs time that the owners could spend on the business itself, but in the long term it is what keeps both the staff and the suppliers in place.

⚠️ **The two AO4s are mirror images: internal failure costs you *people*, external failure costs you *supplies*.** A one-sided answer — usually all internal — leaves half of AO2 on the table, because **the question says "internal **and** external" and means both.**

---

# ✅ BATCH 8 COMPLETE — THE 12-MARK TIER IS CLOSED

**38 blocks, 22 topics, 25 entries (228–252).** Verified by
`python3 layer_c_12mark_coverage.py`: **38 of 38 blocks covered by a written
entry, 0 remaining, 0 dangling.**

| | Blocks | Entries |
|---|---|---|
| **Quality and TQM** | 4 | 229 · 230 |
| **Location** | 4 | 231 |
| **Research** (methods · before launch) | 4 | 232 · 233 |
| **Marketing and promotion** | 4 | 234 · 235 |
| **The market** (change · advantage) | 5 | 236 · 237 |
| **Measuring success** | 3 | 238 · 239 |
| **Objectives and reputation** (social · PR) | 3 | 240 · 241 |
| **Strategy** (orientation · segmentation · ownership · structure · franchise) | 5 | 242 · 243 · 244 · 245 · 246 |
| **Finance** (venture capital · documents · cash flow · interest rates) | 4 | 247 · 248 · 249 · 250 |
| **People** (motivation · communication) | 2 | 251 · 252 |

> ## ⚠️ THE TIER'S PERMANENT LIMIT — STATE IT, NEVER HIDE IT
> **There is no verified 12/12 for Paper 2 or Paper 2R, in any series.** Pearson publishes 12-mark exemplars from **Paper 1** reports; both full-mark scripts in this bank are Paper 1. **Everything in this tier is a `[CONSTRUCTED GRADE 9 TARGET]`** — engineered from the mark scheme's own indicative content, the level descriptors, and the examiner reports. **No score is claimed for any of them.**
>
> ## ⭐ THE TWO ANCHORS EVERY MODEL ABOVE IS BUILT TO IMITATE
> **1. The verified 12/12 — Irsi, May 2023 P1 Q4(c)** (entry 251's paper). **≈330 words, no bullets, and NO conclusion paragraph** — its last paragraph decides (*"the effectiveness … could be limited because it depends on factors such as nature of employee"*) and stops. **It uses both official AO4 routes in one answer:** the drawback of the same option (*"it could compromise quality of products and lead to higher defects / spoiled chocolates"*) and the named condition.
>
> **2. The verified 11/12 — Spud Bros, June 2026 P1R Q4(c)** (entry 240's paper). **The highest-marked 12-mark script in the bank and the best 12-mark model in it**, because it is the closer of the two to a full-mark answer in the situation you will actually face. **It DOES end with an explicit "In conclusion" paragraph — which balances rather than summarises** (*"Although it causes a huge cost to provide free meal, the increase in sales due to support of customers may over the cost in long term"*). **So the rule is not "never write a conclusion". The rule is: a conclusion must WEIGH, never repeat.** The examiner's own words: *"They offer balance in their argument with appropriate levels of context throughout the response."*
>
> **And on the same two pages Pearson printed the 6/12** — the same chains, the same case, **not one drawback on the page**. **That pair is the clearest demonstration in the whole bank of where the marks live in this tier: the second half of the argument.**
