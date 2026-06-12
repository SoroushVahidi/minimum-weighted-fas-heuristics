# Manuscript Scientific Audit
**Date:** 2026-06-11  
**File:** `paper_coap/` (main.tex + 8 sections + tables + figures + declarations)

---

## 1. Scientific Positioning

| Claim | Verdict |
|-------|---------|
| IPSNS presented as primary new algorithmic contribution | ✓ CORRECT — Introduction §1.3 lists IPSNS as the main new element beyond LR-TA |
| LR-TA presented as inherited/refined work | ✓ CORRECT — §1: "the local-ratio principle is prior art"; attributed to DF03 |
| WMSF presented as Cavallaro-Cutello-derived seed | ✓ CORRECT — §2 and §5 explicitly label CC25; §5 states "not rerun for this study" |
| Propositions as supporting correctness lemmas (not new theorems) | ✓ CORRECT — "This is a monotonicity guarantee on the incumbent sequence, not an approximation-ratio or local-optimality guarantee" |
| Experiments as main contribution | ✓ CORRECT — abstract: "contribution is computational and algorithmic rather than a new approximation-ratio theorem" |
| Sparse instances as principal operating regime | ✓ CORRECT — explicitly scoped throughout |
| Dense LOLIB as limitation | ✓ CORRECT — §6.3, §7 explicitly state this as a scope boundary |

## 2. Claim Inventory

| Claim Text | Claim Type | Status |
|-----------|-----------|--------|
| "best observed backward weight among all tested methods on 96 instances" | Safe — qualified "among tested methods" | ✓ SAFE |
| "56 of 57, with a mean relative gap of approximately 0.0006%" | Safe — exact-validated subset only | ✓ SAFE |
| "DRMacIver/FAS is about 21.6% worse in mean backward weight" | Safe — correctly computed over 93 instances | ✓ SAFE |
| "zero incumbent-protection violations" | Safe — verified in EXP1b | ✓ SAFE |
| "not based only on a comparison among internal variants" | Safe — external DRMacIver included | ✓ SAFE |
| "SCC-local refinement is most effective on sparse directed graphs" | Safe after qualification — supported by correlation data in §7 | ✓ SAFE |
| "p < 0.001" (Wilcoxon, sign test) | Safe — consistent with 37/38 non-tied wins | ✓ SAFE |
| "mean runtime rises from 0.074 seconds for LR-TA... to about 20.2 seconds for IPSNS" | Safe — reported as within-study comparison | ✓ SAFE |
| "The contribution is computational and algorithmic rather than a new approximation-ratio theorem" | Safe — accurately states contribution scope | ✓ SAFE |

### Claims Requiring Qualification (Moderate)

| Claim | Issue | Recommendation |
|-------|-------|---------------|
| DRMacIver/FAS described as having "a local-optimality property with respect to single-element moves" | Cites tool documentation; not independently verified | Acceptable with citation |
| "single-run" limitation of DRMacIver EXP4 comparison | Not explicitly stated in §5/§6 | **Add: "DRMacIver was run once per instance using commit 16ff24a."** |
| "7/15 proven optimal" in EXP8 | 8 non-optimal also reported | ✓ Correctly reported |

### Claims Searched For and NOT Found (Good)

| Claim type | Present? |
|-----------|---------|
| "state of the art" (unqualified) | No — always qualified or contextualized |
| "novel algorithm" | No — contribution framed as "engineered framework" |
| "first to" | No |
| "global optimum" | No — "best observed" used |
| "approximation ratio" | No — explicitly disclaimed |
| "best known" (for LOLIB) | No — LOP-native solvers acknowledged as potentially better |

## 3. Algorithm Descriptions vs. Code

| Section | Description | Code Matches? |
|---------|-------------|--------------|
| §4.1 LR-TA Phase 1 | "subtract minimum weight on cycle; at least one arc reaches ≤τ" | ✓ MATCHES `local_ratio_fas_fast` |
| §4.1 LR-TA Phase 2 | "heavy-first arc restoration using rank shortcut and reachability" | ✓ MATCHES `topo_order_active` + `make_reachability_checker` |
| §4.2 WMSF | "removeArcs-minimize-stabilize-minimize per SCC" | ✓ MATCHES `_wmsf_pipeline_scc` |
| §4.3 IPSNS | "best of two seeds, then SCC-BW-weighted LNS with strict-improvement acceptance" | ✓ MATCHES `lns_merge_wmsf_lr_best_incumbent` |
| §4.4 Formal analysis | Propositions 1-5 on termination, correctness, monotonicity | ✓ VERIFIED in IPSNS_AUDIT.md, LRTA_AUDIT.md |

## 4. Formal Propositions Assessment

| Proposition | Statement | Code Evidence | Verdict |
|-------------|----------|--------------|---------|
| Prop 1: LR-TA feasibility and termination | Phase 1 terminates in ≤m iterations; acyclic output | `active` decreases monotonically | ✓ CORRECT |
| Prop 2: Add-back correctness | Rank-forward or negative reachability → safe | Verified in LRTA_AUDIT.md | ✓ CORRECT |
| Prop 3: IPSNS feasibility and monotonicity | bw(π^(t+1)) ≤ bw(π^(t)) ≤ bw(π^(0)) | `best_snapshot` never updated except on strict improvement | ✓ CORRECT |
| Prop 4: IPSNS termination | Terminates after ≤T iterations | Fixed iteration count; loop bounds explicit | ✓ CORRECT |
| Prop 5: WMSF correctness (implicit) | Pipeline produces feasible FAS | Verified in WMSF_AUDIT.md | ✓ CORRECT |

## 5. Related Work Accuracy

See RELATED_WORK_AND_DISCLOSURE_AUDIT.md for full detail.

| Citation | Accuracy |
|---------|---------|
| DF03 (Demetrescu-Finocchi) | ✓ Correctly identified as methodological antecedent |
| CC25 (Cavallaro-Cutello 2025) | ✓ Cited as "not rerun"; WMSF derived from this lineage |
| BSNA21 (Baharev et al.) | ✓ Cited as exact treatment; not used as comparison |
| SST16 (Simpson-Srinivasan-Thomo) | ✓ Cited for web-scale context |
| DRMacIver | ✓ Cited with repo URL |
| BYGR98 (local-ratio foundations) | ✓ Cited without overclaiming |

## 6. Discussion and Limitations

The discussion section explicitly states:
- No new approximation guarantee (limitation)
- Nonneg-weight only (limitation)
- Exact validation limited to n≤20 (limitation)
- Dense LOLIB is a scope boundary, not a primary target (limitation)
- Future work: dense adaptation, more sparse families, parallel SCC refinement

**Assessment: Limitations are honestly and comprehensively stated. No overclaiming.**

## 7. Numerical Traceability

See MANUSCRIPT_NUMERICAL_TRACEABILITY.csv for full table. Summary: all headline numbers are traceable to committed experiment outputs.

## 8. Writing Quality Issues (Minor)

| Issue | Location | Severity |
|-------|----------|---------|
| "EXP7 asks whether IPSNS improvements over LR-TA can be matched by simpler order-local improvement heuristics" — slightly informal wording | §6.1 | Informational |
| The term "paper049" appears in code docstrings but not in manuscript — internal reference not exposed | wmsf.py docstring | Informational |
| "This result addresses baseline strength directly" — slightly assertive | §6.1 | Informational |

## 9. Overall Verdict

**The COAP manuscript is scientifically accurate, appropriately positioned, and submission-ready pending EXP10 integration.** All principal claims are verified. Formal propositions are correct. Related work is comprehensive and honest. Limitations are clearly stated. The contribution scope is consistently bounded throughout.
