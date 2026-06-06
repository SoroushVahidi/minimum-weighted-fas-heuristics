# Venue Decision Notes

**Date:** 2026-06-06  
**Paper:** MWFAS heuristics — LR-TA + IPSNS framework  
**Decision needed:** Primary journal target for submission

---

## Venue Comparison

### Computers & Industrial Engineering (CAIE)

| Field | Notes |
|-------|-------|
| Publisher | Elsevier |
| Scope | Computational methods for industrial engineering, combinatorial optimization, heuristics |
| Impact | Moderate; broad engineering audience |
| Fit for this paper | **Strong** — weighted ordering, precedence conflict, scheduling heuristics are direct CAIE topics |
| Reviewer expectations | Practical utility, clean experiments, solid heuristic design |
| Approximate acceptance rate | Moderate (CAIE has higher acceptance rate than C&OR for well-executed computational studies) |
| Review turnaround | Typically faster than C&OR |
| History signal | Prior interactions with CAIE reviewers on related MWFAS work (email history) |
| Theory requirement | Low — heuristic paper with empirical validation sufficient |
| Baseline depth requirement | Moderate — current EXP4 baseline set is sufficient |

### Computers & Operations Research (C&OR)

| Field | Notes |
|-------|-------|
| Publisher | Elsevier |
| Scope | Operations research methods, combinatorial optimization, metaheuristics |
| Impact | Higher than CAIE; more visible in OR community |
| Fit for this paper | **Moderate-to-strong** — feedback arc set is a core CO problem; LNS and local-ratio are standard OR tools |
| Reviewer expectations | Stronger novelty signal; may request approximation bounds or more recent baselines |
| Approximate acceptance rate | Lower than CAIE |
| Review turnaround | Longer |
| History signal | Limited prior interactions with C&OR |
| Theory requirement | Moderate — reviewers may request formal analysis or gap bounds |
| Baseline depth requirement | High — may request learning-based baselines (GNNRank) or larger instances |

---

## Signal from Email History

Prior CAIE reviewer interactions on related MWFAS work suggest:
- CAIE reviewers are familiar with the problem area.
- Feedback has been on experimental completeness and framing, not theoretical novelty.
- C&OR has been considered but not pursued; no established prior interactions.

Given the goal of **avoiding another rejection** after previous rounds, CAIE is the
lower-risk primary target.

---

## Recommendation

**Primary target: Computers & Industrial Engineering (CAIE)**

Rationale:
- Strong scope fit for weighted ordering in engineering systems.
- Reviewer expectations align with the current experimental portfolio (5 experiments, clean baselines).
- Lower risk of "insufficient novelty" rejection given focus on computational methodology.
- Prior reviewer familiarity reduces cold-start risk.
- The LOLIB transfer test (EXP5) broadens scope without requiring deep theory.

**Ambitious alternative: Computers & Operations Research (C&OR)**

Consider C&OR if any of the following are added before submission:
- GNNRank comparison as an additional learning-based baseline.
- A formal gap bound or approximation analysis for LR-TA.
- Substantially expanded benchmark (e.g., LOLIB dense + DIMACS sparse combined analysis).
- A practical application case study (e.g., scheduling or VLSI layout).

---

## CAIE Framing Recommendations

To maximize CAIE fit, frame the paper around:

1. **Problem framing:** "weighted cyclic ordering" or "weighted precedence conflict resolution"
   in directed graphs — applies to scheduling, circuit design, tournament seeding.

2. **Contribution framing:** "a reproducible computational framework with guaranteed
   non-worsening" — the incumbent protection is the formal guarantee; emphasize it.

3. **Practical relevance:** Mention industrial applications in the introduction:
   - VLSI logic synthesis (circuit feedback)
   - Scheduling with precedence and cyclic dependencies
   - Ranking under paired comparison data (LOP interpretation)
   - Supply chain cycle breaking

4. **Reproducibility as a contribution:** All code and data are public; experiments
   are scripted and reproducible — this is valued at CAIE.

5. **Scope statement:** Be upfront that the method targets sparse directed graphs.
   EXP5 (LOLIB) defines scope boundaries, not failure — present it proactively.

---

## What to Verify Before Final Cover Letter

The following claims about CAIE scope should be verified against the current
Aims & Scope statement before writing the cover letter:

- [ ] Confirm CAIE explicitly covers heuristics for combinatorial optimization
- [ ] Check current Editor-in-Chief and area editors for fit
- [ ] Verify word/page limits for CAIE (typical: 10,000–12,000 words, 8–10 tables/figures)
- [ ] Verify CAIE open-access options and fees if applicable

> **Note:** The impact factors and acceptance rates cited above are approximate
> and should be verified against current journal statistics before final submission.

---

## If CAIE Rejects

If CAIE rejects, the fallback sequence is:

1. **C&OR** — revise manuscript to increase theoretical depth or add GNNRank.
2. **Journal of Heuristics** — heuristic-focused; strong fit for LNS + local-ratio work.
3. **Engineering Optimization** — applied OR; similar scope to CAIE but more engineering-focused.
4. **Optimization Letters** — shorter format; could present core results as a letter.
