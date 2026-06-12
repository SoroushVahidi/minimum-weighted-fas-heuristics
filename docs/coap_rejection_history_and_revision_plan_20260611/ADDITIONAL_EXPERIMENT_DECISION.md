# Additional Experiment Decision

**Audit date:** 2026-06-11  
**Constraint:** No experiments launched during this audit. Recommendations only.

Legend: **Mandatory | Strongly recommended | Optional | Unnecessary**

---

| # | Experiment | Verdict | Prior criticism addressed | Scientific value | Burden | Delay submission? | Omission justified? |
|---|------------|---------|---------------------------|------------------|--------|-------------------|---------------------|
| 1 | Complete EXP10 DRMacIver analysis | **Mandatory** | RR-018, RR-028; CAIE/EJCO baseline fairness | Validates 37/55/1 robustness | Low (running) | Yes — wait for completion | No |
| 2 | Complete/verify Stage-2 holdout postprocess | **Strongly recommended** | RR-023 parameter sensitivity | Justifies IPSNS defaults | Low (1290 runs done) | Minor — writing only | Partially — EXP2 subset rationale exists |
| 3 | Independent igraph exact-IP cross-check | Optional | Exact validation depth | Marginal vs EXP3/EXP8 | Medium | Could add 1–2 days | Yes — DP+MIP sufficient |
| 4 | Additional MILP solver (Gurobi/CPLEX) | Unnecessary | RR-011 medium exact | Low incremental | High | Yes | Yes — HiGHS/scipy documented |
| 5 | Baharev exact-method comparison | Optional | Exact literature completeness | Low for sparse heuristic paper | Medium | Yes | Yes — BSNA21 cited; not baseline |
| 6 | sfas external heuristic | Optional | RR-025 baseline gap | Depends on sfas identity | Unknown | Maybe | Yes if documented exclusion |
| 7 | Another LOP-specific method (LOP_MA-EDM) | Unnecessary | Dense LOP baseline | Already disclosed not rerun | High | Yes | Yes — LOLIB already shows DRMacIver dominance |
| 8 | Additional large real-world sparse graphs | Optional | RR-005 scale/breadth | Diminishing returns | High | Yes | Yes — 105 public instances + EXP9 |
| 9 | More stochastic seeds (>20) | Unnecessary | RR-028 | Low if EXP10 shows stability | Medium | Yes | Yes after EXP10 if variance observed |
| 10 | More ablations | Unnecessary | RR-012 component question | EXP2+EXP7 cover this | Medium | Yes | Yes |
| 11 | Runtime scaling experiment | Optional | Runtime fairness questions | Moderate narrative support | Low (data exists) | No — use EXP1b/EXP6 | Yes — runtime already reported |
| 12 | Memory scaling experiment | Unnecessary | None documented | Low | Medium | Yes | Yes |
| 13 | Additional dense benchmarks | Unnecessary | RR-004 scope | Would reinforce DRMacIver advantage | High | Yes | Yes — LOLIB sufficient as boundary |
| 14 | More exact small instances | Unnecessary | EXP3 coverage | Marginal | Low | No | Yes — 56/57 sufficient |
| 15 | More medium-instance MIP validation | Optional | RR-011 | Moderate | Medium (~hours) | Maybe | Yes — EXP8 15 instances adequate |
| 16 | Parameter transfer experiment | Unnecessary | Holdout covers tuning | Holdout is the transfer study | Done | No | Yes |
| 17 | Component-removal ablation for IPSNS | Unnecessary | RR-012 | EXP2 ipsns_no_scc_priority etc. | Done | No | Yes |
| 18 | Correctness regression tests | **Strongly recommended** | RR-019 reproducibility | High for artifact credibility | Low–medium | Minor | No if claiming full reproducibility |

---

## Summary

**Mandatory before submission:** EXP10 only (already in progress).

**Strongly recommended:** Holdout postprocess integration; smoke/correctness tests (code, not experiment).

**Do not launch** merely to enlarge the paper: GNNRank, Baharev rerun, extra dense suites, memory scaling, sfas unless identity resolved and reviewer-critical.

---

## EXP10 dependency graph

```
EXP10 complete
  ├── validate_drmaciver_runs.py
  ├── summarize_drmaciver_phase.py
  ├── finalize_exp10.py
  ├── Manuscript §5–§6 integration
  └── Online Resource 1 packaging
```

Holdout can proceed in parallel with EXP10 (data already collected).

---

## If EXP10 shows DRMacIver variance materially changes win record

**Mandatory manuscript adjustment:** Revise §6 paired-comparison language to distribution-based claims (median wins, seed stability) — do not suppress. This is still publishable with bounded claims.

If IPSNS remains deterministic and DRMacIver varies, emphasize IPSNS reproducibility vs external heuristic stochasticity — already scientifically interesting.
