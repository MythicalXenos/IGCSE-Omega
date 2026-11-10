# Situation evaluation with simulations — 4EB1

**1 November 2026.** No plan in this file; evaluation only. Simulations are Monte Carlo, 200,000
trials each, run in Python against empirical component distributions derived from the learner's own
four mocks and their stated best-ever components. Boundary set: June 2025 (9 = 69, 8 = 64, 7 = 59,
6 = 56, 5 = 53, 4 = 50), which is within one mark of every series since 2023.

---

## 1. The data being evaluated

| Source | Value |
|---|---|
| Mock totals | 52, 55, 56 (four mocks; one figure not retained) |
| Section A typical | **15/40**, best 23/40 |
| Section A best components | ret 5, Q3 6, Q6 6, Q7 6 |
| Section B | typical 19/30, best 22/30 (speech; **AI-marked, unverified**) |
| Section C | typical 17–19/30, best 19/30 |

## 2. First finding: the totals are remarkably stable

52, 55, 56 is a **spread of four marks** across four sittings. Standard deviation ≈ 2.

For comparison, candidates at this level typically swing 8–10 marks between mocks. This learner does
not. **Reliability is high.** That is a strength with a sharp corollary: because performance does not
swing much, **improvements will also not swing much — they will stick.** A system that lifts the mean
by five marks lifts almost every future sitting by five marks.

It also means regression to the mean is not protecting them: 55 is not a lucky day above a 50 average.
**55–56 is the true level.**

## 3. Second finding: 64 was never a real score

The tempting arithmetic is best-A (23) + best-B (22) + best-C (19) = **64, a grade 8**. This is the
**max-of-each-component fallacy**. Those three maxima occurred in different sittings, and there is no
evidence they have ever co-occurred. Summing separate maxima estimates something no candidate has
ever scored.

The simulation makes the cost visible. Treating each component as drawn from the observed distribution,
the *simulated* outcome distribution is:

| Scenario | Mean | P(9) | P(8+) | P(7+) | P(6+) |
|---|---|---|---|---|---|
| **Baseline (current habits)** | **55.9** | **0.0%** | **0.0%** | 14.4% | 55.2% |
| + timing discipline on Q7 | 55.9 | 0.0% | 0.1% | 14.4% | 55.1% |
| + AO5 proofread (+2 on B and C) | 59.9 | 0.0% | 7.1% | 70.3% | 96.7% |
| + Q3/Q6 template (+1 each) | 57.9 | 0.0% | 1.1% | 39.3% | 83.0% |
| **All three together** | **61.9** | **0.3%** | **25.3%** | 91.7% | 99.8% |

**This contradicts the optimistic reading given earlier in the session, and the simulation is right.**
The earlier claim — "your best-ever composite is 65, so grade 9 is +4" — was an artefact of summing
maxima. Withdraw it.

The honest position: **current habits produce a grade 5–6. Discipline-and-template interventions
produce a reliable grade 7 and a one-in-four chance of a grade 8. They do not produce a grade 9**,
because all of them shift consistency rather than the per-component ceiling.

## 4. What a grade 9 actually requires

Working backwards from 69, and respecting the way the grids allocate marks:

| Component | Their observed **maximum** | Needed for 69 | Level jump |
|---|---|---|---|
| Retrieval | 5/5 | 5/5 | none |
| Q3 | **6/10** (Level 3) | **7/10** (Level 4) | +1 level |
| Q6 | **6/10** (Level 3) | **7/10** (Level 4) | +1 level |
| Q7 | **6/15** (Level 2 top) | **9/15** (Level 3) | +1 level |
| Q8 | **22/30** (unverified) | **23/30** | marginal |
| Section C | **19/30** (AO4 ~14, AO5 ~5) | **22/30** (AO4 15, AO5 7) | +1 level on AO5 |

Consistent vectors that sum to 69: (A 24, B 23, C 22) · (A 23, B 23, C 23) · (A 25, B 22, C 22).

**The requirement is Level 4 in Section A and Level 3–4 on Q7.** The learner has *never* produced a
Level 4 Section A answer in any recorded sitting. That is the true distance to a grade 9, and no
amount of timing discipline closes it.

## 5. Simulation of a raised ceiling

If Q3/Q6 sit at 6–8, Q7 at 8–11, B at 21–24 and C at 20–23 — i.e. the profile implied by the vector
table — the simulated outcome is:

| Scenario | Mean | P(9) | P(8+) | P(7+) |
|---|---|---|---|---|
| Ceiling raised to Level 4 (Section A) + AO5 discipline | **71.3** | **92.7%** | 100% | 100% |

**Interpretation.** The paper is not tightly bunched at the top: once the components actually reach
Level 4, a grade 9 stops being a lottery and becomes the expected result. Grade 9 in 4EB1 is not won
by brilliance; it is won by getting *one level up* in four places simultaneously. That is why the
outcome distribution is bimodal — you either have Level 4 Section A or you do not, and the boundary
sits almost exactly between the two states.

## 6. Evidential threats to this evaluation

1. **Four mocks, one examiner.** All figures come from school marking, which may be generous or harsh
   by a level. No script has been marked against the printed grids independently.
2. **The 22/30 is AI-marked.** Models grade AO4 generously. If the true figure is 19, every simulated
   P(9) in §5 falls.
3. **Component maxima are self-reported** and may be remembered selectively.
4. **The Q7 timing mechanism is assumed, not observed.** The simulation models Q7 degradation via
   overrun on Q3/Q6; that is plausible from the pattern (6 once, 2–4 otherwise) but unverified. A
   20-minute cold Q7 would test it directly.
5. **Boundaries assumed constant.** Safe: 9 has been 68–70 since 2023. A harder paper moves the
   boundary down, not the rank order.

## 7. What the evaluation concludes

- **Level:** reliably grade 5–6. Mean simulated 55.9, matching the observed 52–56.
- **Strength:** high consistency. Improvements will persist rather than evaporate.
- **Weakness:** Section A at 15/40 — the learner operates roughly one full level below their own
  Section B/C standard in the section worth 40 marks.
- **The real ceiling problem:** the observed maximum in every levels-based component is **Level 3**
  (Q7: Level 2). Grade 9 needs Level 4. Consistency work cannot substitute for that.
- **Realistic range in the near term:** 7 with discipline, 8 in a good sitting, 9 only if a Level 4
  answer becomes producible on demand — and the simulation says that when it does, the grade follows
  almost automatically (92.7%).

**The one-line finding:** this is not a candidate short of technique or short of time. It is a
candidate whose *best ever* answer in each levels-based question is one level below the grade they
want, and who has never yet had to produce a Level 4 answer to get a mark they were satisfied with.
