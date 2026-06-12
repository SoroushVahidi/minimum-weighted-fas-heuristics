# Manuscript Scientific Audit (COAP)

**Audit date:** 2026-06-10 (updated 2026-06-11 with novelty/prior-work findings)  
**Manuscript:** `paper_coap/main.tex` (40 pages, SHA `b596f694...`)

Independent read; prior AI audits not treated as authoritative.

## Contribution hierarchy (observed)

1. **LR-TA** — novel topological add-back on local-ratio reduction (engineering contribution)
2. **WMSF seed** — complementary feasible ordering / internal baseline
3. **IPSNS** — incumbent-protected SCC-local destroy-repair
4. **Empirical** — strong sparse benchmark performance + scope boundaries (LOLIB, exact validation)

Introduction explicitly **disclaims new approximation-ratio theorem** — appropriate.

## Strengths

- Clear problem statement and sparse vs dense scope distinction
- Formal analysis section added (`04_formal_analysis.tex`) — feasibility, add-back, IPSNS monotonicity
- Broad experimental program (EXP1–9)
- Honest limitation language on exact validation and dense transfer
- Reproducibility artifact referenced (needs COAP update)
- Related work cites Demetrescu–Finocchi without overclaiming transfer

## Weaknesses by severity

### Blocking

| ID | Issue |
|---|---|
| N-01 | **arXiv:2412.16181 (Vahidi & Koutis) not cited in COAP** — confirmed author predecessor; absent from bibliography; must be cited and disclosed (see `NOVELTY_AND_PRIOR_WORK_AUDIT.md`) |
| N-02 | **JOCO predecessor (Vahidi, LR-TA manuscript) not cited** — LR-TA is algorithmically identical; confirmed by archive ZIP; must be disclosed |
| N-03 | **Elsevier predecessor (IPSNS/WMSF) not cited** — IPSNS inherited from this predecessor; must be disclosed |
| M-01 | **Related-manuscript overlap undisclosed** for COAP portal requirement (reinforced by N-01–N-03) |
| M-02 | **Parameter justification incomplete** — 400-iter default cited from ablation; holdout not finished |
| M-03 | **No automated proof-to-code test gate** — formal claims rely on manual audit |

### Major

| ID | Issue |
|---|---|
| M-04 | **Demetrescu–Finocchi** cited as methodological prior but no formal transfer — acceptable if disclaimer kept (confirmed: DF03 guarantee not established; see `DF_VS_LRTA_OPERATIONAL_COMPARISON.md`) |
| M-05 | **Baseline strength**: only 2 external heuristics; sfas identity unresolved (B-06); igraph exact_ip classified as exact validation not heuristic comparison (see EXACT_BASELINE_FEASIBILITY.md) |
| M-06 | **Salami-slicing risk** vs predecessor JOCO/Elsevier repos — needs transparent disclosure (risk assessed as moderate but manageable with proper disclosure in `RELATED_MANUSCRIPT_CONTRIBUTION_MATRIX.md`) |
| M-07 | Destroy-fraction reproducibility wording **contradicts code** — destroy fractions are deterministic constants; only SCC selection is randomized (confirmed N-06) |
| M-08 | WMSF stabilize step not covered by add-back proposition — theory gap |
| N-04 | **Add-back ordering description** — if "residual" or "reduced weight" language appears anywhere, must be corrected to "original weight" (confirmed: all code uses W0) |
| N-05 | **Topological shortcut iff claim** — if "iff rank(u)<rank(v)" language appears, must be corrected to "sufficient condition" |
| N-06 | **Destroy causal language** — remove any text saying heavy arcs are reactivated "via" or "through" light arcs; the two operations are independent |

### Moderate

| ID | Issue |
|---|---|
| M-09 | Novelty of LR-TA add-back vs prior local-ratio FAS literature needs sharper differentiation |
| M-10 | IPSNS novelty vs generic LNS — contribution is incumbent protection + SCC locality |
| M-11 | Statistical reporting could include medians/CIs |
| B-07 | DRMacIver non-determinism not disclosed (`srand(time\|pid)`; one run per instance) — must add note in §5 |
| B-09 | borda_net_score not consistently labeled "in-repo adaptation" across all manuscript locations |
| M-12 | EXP6 budget curve suggests saturation at low iterations — manuscript still emphasizes 400 |
| M-13 | Some repetition between algorithm section and formal analysis |

### Minor / optional

| ID | Issue |
|---|---|
| M-14 | GNNRank and other citations in bib not all discussed in depth |
| M-15 | Application case (EXP9) illustrative but small |
| M-16 | Tone occasionally defensive — generally acceptable |

## Demetrescu–Finocchi status

Appropriately **not claimed** as proved guarantee. Formal integration would require Phase-I-only LR minimal-FAS theorem + explicit separation of add-back/heuristic layers — **not present**.

## Overclaiming check

| Claim | Supported? |
|---|---|
| 96/97 best on sparse benchmark | Yes — EXP1b/EXP4 summaries |
| 56/57 exact optimal | Yes — EXP3 |
| Non-worsening vs seeds | Code + Prop. 3; needs tests |
| Parameter defaults optimal/justified | **No** until holdout |
| Approximation ratio | Correctly disclaimed |

## Recommended manuscript actions (post-holdout)

1. Complete related-manuscript disclosure section / cover letter
2. Fix destroy-fraction / seed reproducibility wording
3. Integrate holdout results or retain 400-iter default with honest limitation
4. Scope Prop. 2 to minimize steps; describe Stabilize separately
5. Optional: shorten repetition between §4 algorithm and §4 formal analysis
