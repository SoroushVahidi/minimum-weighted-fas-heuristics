# Exact Solver Audit
**File:** `src/mwfas/exact.py` (146 lines)  
**Date:** 2026-06-11

---

## 1. Algorithm: Bitmask DP for Minimum Weighted FAS

**Formulation:** Find vertex ordering minimizing total backward-arc weight.  
**Recurrence:** `dp[S] = max over v in S of (dp[S\{v}] + incoming_weight(v, S\{v}))`  
**Min FAS weight:** `total_weight - dp[(1<<n) - 1]`  
**Complexity:** O(n · 2^n) after precomputation; feasible for n ≤ 20.

## 2. Recurrence Correctness

| Item | Verdict |
|------|---------|
| `dp[S]` = max forward weight achievable by ordering the vertices in S | **CORRECT** — base case `dp[0] = 0.0`; transition places `v` last in S |
| `incoming(v, S\{v})` = sum of weights of arcs u→v for u in T | **CORRECT** — inner loop `while t:` extracts each set bit |
| `v` is "placed last" in the ordering of S | **CORRECT** — arcs from T to v become forward; arcs from v to T are backward (already counted in `dp[T]`) |
| Reconstruction via `last[S]` | **CORRECT** — reconstructs ordering from `S=full` backwards |

## 3. Handling Special Cases

| Case | Code | Verdict |
|------|------|---------|
| n = 0 | Returns `(0.0, 0.0, [])` immediately | CORRECT |
| n > 20 | Raises `ValueError` with message | CORRECT |
| Parallel arcs | `adj[u][v] += w` in setup loop | CORRECT — parallel arcs aggregated |
| Self-loops `(u, u, w)` | `adj[u][u] += w`; `total_w += w`; never contributes to forward weight (v not in T when v=u) | CORRECT — self-loops always in FAS |
| Zero-weight edges | `adj[u][v] += 0.0` — included in total_w computation but contribute 0 to any transition | CORRECT |
| Negative-weight edges | No explicit guard; included in `total_w`; can produce min_fas_w < 0 | MATCHES behavior — negative-weight instances are explicitly excluded from EXP3 validation |

**Self-loop analysis:** For a self-loop (u, u, w): `total_w += w`, but `adj[u][u]` only contributes to `incoming(u, T)` when u is in T. Since T = S ^ {u}, u is not in T, so `adj[u][u]` never contributes to `dp`. Therefore `dp[full]` excludes self-loop weights, and `min_fas_w = total_w - dp[full]` includes self-loop weights. This is **correct** — self-loops cannot be in the forward direction and always belong in the FAS.

## 4. Consistency with evaluation.py

`evaluation.py::compute_forward_backward`: edge `(u, v, w)` is forward if `scores[u] < scores[v]`.
- Self-loops: `scores[u] < scores[u]` is False → backward. ✓ Consistent.
- The optimal ordering from `exact_min_fas_dp` defines `optimal_scores[optimal_order[r]] = r`.
- Computing `compute_forward_backward(edges, optimal_scores)` should give `bw = min_fas_w`. ✓

**Cross-check in EXP3:** The exact report verifies IPSNS BW ≥ exact BW on all instances (IPSNS matches on 56/57). This is consistent because exact DP gives a lower bound. ✓

## 5. Consistency with EXP8 HiGHS MIP

EXP8 uses HiGHS as an ILP solver for medium instances. On the 7 proven-optimal instances, both exact DP (for small n) and HiGHS give the same result for the overlap. The `r20_60` instance appears in both EXP3 (exact DP: 1685.0) and EXP8 (MIP: 1685.0) — **consistent**. ✓

## 6. Objective Convention

The manuscript uses "backward weight" as the minimization objective throughout. The exact DP maximizes forward weight then converts: `min_fas_w = total_w - max_fw`. This is the correct dual formulation. ✓

## 7. igraph exact IP Assessment

The prior audit classified `python-igraph method="ip"` as exact validation only (EXP3-scope), not a heuristic comparison baseline. This remains correct:
- igraph's `feedback_arc_set(method="ip")` calls an integer program solver
- Appropriate for small n validation, not for large-instance comparison
- Not used in EXP4 or EXP1b as a competing heuristic
- EXP3 uses the in-house bitmask DP, not igraph IP

## 8. Overall Verdict

**Exact DP is correctly implemented.** The recurrence is correct. All edge cases are handled appropriately. The formulation is consistent with evaluation.py and with EXP8 HiGHS results. The n≤20 limitation is enforced. The EXP3 results (56/57 IPSNS optimal, mean gap 0.0006%) are trustworthy.
