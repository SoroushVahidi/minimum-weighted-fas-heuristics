# Simulated Reviewer 1 — Algorithms and Novelty

**Profile:** Skeptical graph algorithms / combinatorial optimization reviewer.

## Audit items

| # | Topic | Classification | Notes |
|---|---|---|---|
| 1 | MWFAS problem definition | already resolved | §3, Eq. (1)–(4); ordering equivalence stated |
| 2 | Nonnegative-weight assumption | already resolved | Stated in problem definition, experiments, README |
| 3 | Minimal vs. minimum | already resolved | WMSF “minimal-and-stable” vs. MWFAS “minimum” distinguished |
| 4 | LR-TA provenance | already resolved | Demetrescu–Finocchi \cite{DF03}; author LR-TA manuscript disclosed |
| 5 | Demetrescu–Finocchi guarantee qualification | already resolved | No false approximation theorem claimed |
| 6 | WMSF provenance | already resolved | Cavallaro–Cutello \cite{CC25}; engineered variant labeled |
| 7 | WMSF L1/L2 policy | already resolved | Documented in §4 and OR1 S3 |
| 8 | IPSNS mechanism | already resolved | Destroy A/B, SCC repair, incumbent protection in §4 |
| 9 | SCC neighborhood definition | already resolved | Fixed original-graph SCC neighborhoods |
| 10 | Destroy A and Destroy B | already resolved | Pseudocode and prose in §4 |
| 11 | SCC-local repair | already resolved | Restricted LR-TA + add-back inside SCC |
| 12 | Incumbent rollback | already resolved | Strict improvement only; Prop. monotonicity |
| 13 | Complexity statements | already resolved | Implementation-faithful bounds in §4 |
| 14 | Topological extraction | already resolved | Eq. (3)–(4); EXP11 calibration |
| 15 | Removed-set vs. order objective | already resolved | Central clarification; not objective-neutral |
| 16 | EXP11 scope | already resolved | 6-instance calibration; zero backward-weight change |
| 17 | Formal propositions | already resolved | Supporting, not main theoretical claim |
| 18 | Novelty claims | already resolved | IPSNS integration; seeds attributed |
| 19 | Correctness claims | already resolved | Propositions with OR1 proofs |
| 20 | Termination claims | already resolved | Iteration budget T; no false global optimality |

## Pre-correction item (fixed)

| Topic | Was | Fix |
|---|---|---|
| EXP10 described as “ongoing” in §2.1 | valid and important | Updated to “completed stochastic-robustness study (EXP10)” |

## Likely review comments (non-blocking)

- Request clearer separation of IPSNS from generic LNS literature (partially addressed in contribution bullet).
- May ask for additional dense-graph adaptation (acknowledged as future work / LOLIB boundary).

## Verdict

**No submission-blocking algorithmic objections.** Reviewer 1 would likely recommend minor clarity edits, not rejection.
