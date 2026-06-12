# Topological extraction audit — executive summary

**Date:** 2026-06-11  
**Branch:** `main` @ `80b3144d5fdbbe250faed8a4fe671dde2da76c89`

## Verdict

The Discrete Applied Mathematics reviewer concern is **mathematically valid in general** but **does not materially affect headline sparse benchmark results** under the repository's nonnegative setting and tested extraction alternatives.

## Key findings

1. **Reported objective:** All experiments report **ordering backward weight** \(\mathrm{bw}(\pi)\), recomputed via `compute_forward_backward` on the returned ranking. FAS-constructing methods build \((F,H)\) first, then extract \(\pi\) by Kahn sorting with **min-heap vertex-id tie-breaking**.

2. **Mathematics:** For active DAG \(H=(V,A\setminus F)\) and topological \(\pi\), \(B_\pi\subseteq F\) and \(w(B_\pi)\le w(F)\). Equality iff \(w(F\setminus B_\pi)=0\).

3. **Manuscript gap (fixed):** Problem definition now states the inequality and clarifies that extraction is not objective-neutral. OR1 S02/S06 corrected misleading removed-set equivalence wording.

4. **EXP11 (run):** On six nonnegative calibration instances, alternative Kahn tie-breakers and precedence-preserving insertion refinement on LR-TA final active DAGs produced **identical** \(\mathrm{bw}(\pi)\); \(w(F)-\mathrm{bw}(\pi)=0\) throughout.

5. **No algorithm change required.** No prior experiment rerun required.

## Deliverables

- Code: `src/mwfas/topo_extraction.py`, `tests/unit/test_topo_extraction_math.py` (13 tests)
- EXP11: `experiments/exp11_topological_extraction_sensitivity/`
- Manuscript: problem definition, framework, design, results (Table EXP11), discussion limitation
- OR1: S02, S06 updated
- Main PDF: 45 pages

## Next task

Sync OR1 artifact ZIP if submitting updated supplement; otherwise proceed to COAP cover letter and upload.
