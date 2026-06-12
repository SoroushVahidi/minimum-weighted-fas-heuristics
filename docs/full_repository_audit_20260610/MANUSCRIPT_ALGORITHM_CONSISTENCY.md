# Algorithm–Manuscript Consistency Audit

**Audit date:** 2026-06-10 (updated 2026-06-11 with novelty/prior-work corrections)

## Discrepancy table

| Manuscript claim | Manuscript location | Code location | Status | Severity | Recommended action |
|---|---|---|---|---|---|
| Phase I: ε=min cycle weight; deactivate ≤τ; ε≤τ removes one arc | `04_algorithmic_framework.tex`, Prop. 1 | `lrta.py` 238–259; `ipsns.py` LR paths | exact match | — | None |
| Phase II heavy-first add-back; forward rank; backward reachability; re-topo after backward | Alg. LR-TA; Prop. 2 | `lrta.py` 264–281; `wmsf_minimizeFas_scc`; `minimize_addback_inside_scc` | exact match | — | None |
| Add-back tie-break includes edge id | Manuscript tie-break prose | `lrta.py` 265 lacks `eid`; WMSF/IPSNS include `eid` | incomplete documentation | Low | Add `eid` to LR sort or soften claim |
| WMSF per-SCC pipeline; L1+L2 for single SCC | §4 framework | `wmsf.py` `_wmsf_pipeline_scc`, 467–472; `ipsns.py` `wmsf_seed_solution_full` | exact match | — | None |
| Default WMSF seed mode `full` | §4 | `ipsns.py` 680, 739–743 | exact match | — | None |
| SCC score = backward weight; top-K weighted sample | Alg. IPSNS | `ipsns.py` 787–801 | exact match | — | None |
| Destroy: heavy reactivate / light remove fractions | §4 | `ipsns.py` 624–640 | exact match | — | None |
| Destroy fractions reproducible via random seed | `04_algorithmic_framework.tex` ~121; invariants table | Fractions deterministic; only SCC choice uses RNG | **contradictory** | **Medium** | Fix manuscript wording |
| Rollback on invalid repair/topo; strict BW improvement | Prop. 3; Alg. IPSNS | `ipsns.py` 653–660, 824–847, 853–855 | exact match | — | None |
| Incumbent monotone BW | Prop. 3 | `_bw < best_bw - 1e-12`; output from `best_snapshot` | equivalent | Low | Note tolerance in proof |
| Termination ≤ T iterations; exit if all SCC scores 0 | Prop. 4 | `ipsns.py` 785–793 | exact match | — | None |
| τ = 1e-12 default | Formal analysis | All modules CLI defaults | exact match | — | None |
| Objective over all aggregated arcs | §3 problem | `evaluation.py` 19–23 | exact match | — | None |
| Prop. 2 covers WMSF Stabilize | Prop. 2 wording | `wmsf_stabilizeFas_scc` uses swap rule, not reachability add-back | incomplete documentation | Low | Scope prop to Minimize |
| DF03 approximation for full framework | Related work | No ratio proof in code | unverified (disclaimed in intro) | N/A | Do not add without proof |
| LR-TA entry = `local_ratio_fas_fast` | Formal analysis | IPSNS LR seed splits reduction + `wmsf_minimize_global` | equivalent | Low | Cross-ref in formal section |

## 2026-06-11 corrections from novelty audit

The following rows were corrected or added based on full code reading in the 2026-06-11 novelty
audit. See `DF_VS_LRTA_OPERATIONAL_COMPARISON.md` and `NOVELTY_AND_PRIOR_WORK_AUDIT.md`
for detailed derivations.

| Topic | Correction | Severity |
|---|---|---|
| Add-back ordering weight | Code sorts by `W0[eid]` (original weight), NOT reduced/residual weight. All three modules (`lrta.py` line 265, `wmsf.py` line 263, `ipsns.py` line 242) confirmed. If manuscript uses "residual" or "reduced" for add-back sort, fix required. | **High** |
| Topological-rank shortcut semantics | `rank[u] < rank[v]` is a **sufficient** condition for accepting reinsertion, not a necessary-and-sufficient condition. The iff claim is mathematically false. | **High** |
| Zero-edge removal | When `eps ≤ tol`, code removes only `cyc[0]`, not all zero-weight edges simultaneously. This deviates from DF03's simultaneous-removal assumption. | Medium |
| Destroy operations causal link | Destroy A (heavy reactivate) and Destroy B (light remove) are **independent** sequential operations. No causal or blocking relationship exists in the code. | **High** |
| IPSNS LR repair weight source | `local_ratio_repair_inside_scc` initializes `W = {eid: W0[eid]}` — resets to original weights at every repair call, not accumulated reduced weights. | Medium |
| DF03 approximation inheritance | **Not established**. Heavy-first add-back does not guarantee inclusion-minimality required by DF03's proof. See `DF_VS_LRTA_OPERATIONAL_COMPARISON.md`. | High (for any claim) |
| arXiv:2412.16181 not cited | This author predecessor is absent from COAP bibliography and manuscript. Blocking disclosure gap. | **Blocker** |
| JOCO predecessor not cited | LR-TA algorithm is identical to JOCO predecessor manuscript. Must be disclosed. | **Blocker** |

## Formal theory alignment summary

| Topic | Verdict |
|---|---|
| LR-TA feasibility/termination | Supported by code |
| Add-back acyclicity (Minimize steps) | Supported |
| Stale topo intentional on forward add-back | Supported |
| IPSNS monotonicity | Supported with tolerance |
| Complexity bounds | Conservative; supported structurally |
| DF03 transfer | **Not integrated** — blocked by add-back, ordering objective, IPSNS/WMSF layers |

See `MANUSCRIPT_SCIENTIFIC_AUDIT.md` for Demetrescu–Finocchi gap detail.
