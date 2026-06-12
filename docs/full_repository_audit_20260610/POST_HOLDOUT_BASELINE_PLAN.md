# Post-Holdout Baseline Plan

**Audit date:** 2026-06-11  
**Scope:** Prioritized action plan for baseline additions and improvements following completion  
of the COAP stage-2 holdout experiment (`coap_ipsns_holdout`).  
**Constraint:** This plan is documentation only. No experiments, installs, or code changes are  
authorized here. All actions below are post-holdout recommendations.

---

## Prerequisites

This plan assumes:
1. `logs/coap_ipsns_holdout/COMPLETED.ok` exists (holdout experiment complete)
2. Holdout post-processing (Phase 2 in ROADMAP.md) is complete
3. Parameter defaults have been finalized based on holdout evidence
4. Novelty/disclosure corrections (Phase 0) have been applied to the manuscript

---

## Priority classification

| Priority | Criterion |
|---|---|
| **P1 (Before submission)** | Required to address a known Blocker or Major issue; or provides evidence without which a claim is unsupported |
| **P2 (Recommended before submission)** | Strengthens a currently moderate weakness; low implementation cost |
| **P3 (Post-submission or reviewer-response)** | Adds incremental value; not required for initial submission |
| **P4 (Optional — lower confidence)** | May be infeasible or offer marginal value; investigate before investing time |

---

## Task P-01: Clarify and resolve sfas identity

**Priority: P1 (Before submission)**  
**Issue referenced:** B-06 (sfas unidentified)  
**Effort:** 1–2 hours  

| Step | Action |
|---|---|
| 1 | Author determines what `sfas` was intended to be (CC25 external code? fas-smartAE? another method?) |
| 2a | If CC25 external code: locate public CC25 code; assess weighted-digraph support; if available, run on EXP4 instances; otherwise document exclusion |
| 2b | If fas-smartAE: document exclusion (unweighted + networkit unavailable); add explanation in §5 |
| 2c | If something else: add paper reference and implementation plan |
| 3 | Update ROADMAP.md Phase 5 with confirmed identity and decision |
| 4 | Update BASELINE_AUDIT.md and MISSING_BASELINE_REGISTER.csv with resolution |

**Decision rule:** If CC25 code is publicly available and supports weighted digraph input,  
running it would provide the most value (validates WMSF reimplementation and adds independent  
external comparison). If not available or unweighted, document the exclusion clearly.

---

## Task P-02: Add DRMacIver weight-guarantee disclosure

**Priority: P1 (Before submission)**  
**Issue referenced:** B-07 (DRMacIver non-determinism), B-08 (igraph Eades weight)  
**Effort:** 30 minutes (manuscript text only)  

Add to §5 experimental design (baseline description) the following disclosures:

1. DRMacIver uses `srand(time|pid)` — results may vary between runs. EXP4 records one run per instance.
2. igraph `method="eades"` passes weights but the Eades algorithm is structurally unweighted.

Suggested text for §5:

> "DRMacIver/FAS uses an internal time- and process-ID-based random seed; results may vary  
> between runs. All EXP4 comparisons report a single run per instance. The python-igraph  
> `feedback_arc_set(method='eades')` call accepts arc weights, but the Eades algorithm does  
> not carry a formal weight-minimization guarantee; the weights influence the igraph-internal  
> implementation but not via a provably weight-optimal procedure."

---

## Task P-03: DRMacIver multi-run reproducibility check

**Priority: P2 (Recommended before submission)**  
**Issue referenced:** B-07  
**Effort:** 2–4 hours (running + analysis)  
**Prerequisite:** Holdout complete; no runtime impact on running experiment

Run DRMacIver 3–5 times on a representative 20-instance subset of the standard sparse benchmark.  
Report:
- Mean and range of backward weight across runs for each instance
- Whether the 93-instance mean BW (53,173) is stable
- Whether the win/tie/loss counts (37W/55T/1L vs IPSNS) are stable

**If results are stable across runs:** Add to supplementary (or §5 note): "Reproducibility  
check on 20 instances confirmed that DRMacIver results are stable across 3–5 runs."

**If results vary:** Report the range and use average-across-runs for the main comparison, or  
acknowledge the limitation explicitly.

---

## Task P-04: igraph exact IP cross-validation (optional sanity check)

**Priority: P3 (Post-submission)**  
**Issue referenced:** B-06 sub-item (igraph exact IP)  
**Effort:** 1–2 hours  
**Prerequisite:** python-igraph 1.0.0 installed (confirmed available)

Run `feedback_arc_set(method="ip")` on the 57 EXP3 instances (n≤20). Compare results against  
bitmask DP optima. This is a sanity check for EXP3, not a new baseline.

**If igraph IP agrees with bitmask DP on all 57 instances:** Add note in supplementary:  
"Independent verification using igraph exact ILP confirms bitmask DP optima on all 57 instances."

**If disagreement on any instance:** Investigate; the lower BW is the correct optimum; correct  
the EXP3 summary accordingly.

---

## Task P-05: borda_net_score labeling clarification

**Priority: P2 (Recommended before submission)**  
**Issue referenced:** B-09  
**Effort:** 15 minutes (manuscript text)

In §5 baseline description, explicitly label `borda_net_score` as "an in-repo adaptation" to  
avoid any suggestion that it is an independent external implementation:

> "The Borda net-score baseline (out-weight minus in-weight) is an in-repo simple ordering  
> heuristic, not an external published code."

---

## Task P-06: DRMacIver runtime in comparison table

**Priority: P3 (Post-submission)**  
**Issue referenced:** B-11 (runtime not in comparison table)  
**Effort:** 1 hour (extract runtime from EXP4 logs, add table column)

Add a mean-runtime column to `table_sparse_external_baselines.tex` for all methods including  
DRMacIver, to give a complete picture of the quality-runtime tradeoff.

---

## Task P-07: EC-02 claim verification (21.6% figure denominator)

**Priority: P1 (Before submission)**  
**Issue referenced:** EC-02  
**Effort:** 30 minutes (verify against EXP4 CSV)

The manuscript states DRMacIver is "about 21.61% above IPSNS" on completed standard instances.  
The EXP4 CSV column `mean_rel_gain_ipsns_pct = 21.6076` likely reports the **mean relative gain  
of IPSNS over DRMacIver computed on the 37 instances where IPSNS strictly improves** (not the  
mean over all 93 instances).

The overall mean BW figures (IPSNS: 37,697; DRMacIver: 53,173 on 93 instances) give a  
mean relative excess of approximately 41% ((53173 - 37697) / 37697 ≈ 41%), not 21.6%.

**Action:** Verify exactly how `mean_rel_gain_ipsns_pct` is computed in  
`experiments/exp4_external_baselines/postprocess_exp4_external.py`. Ensure manuscript text  
accurately describes the denominator (37-instance gain subset or 93-instance full subset).  
Correct the description if needed.

---

## Task P-08: Multiplicity-correction acknowledgment

**Priority: P3 (Post-submission or at reviewer request)**  
**Issue referenced:** B-11  
**Effort:** 15 minutes

In §6 statistical testing paragraph, add one sentence:

> "Paired tests are performed for the primary IPSNS vs. DRMacIver comparison only. No  
> multiplicity correction is applied across the full 8-method comparison table, consistent  
> with the descriptive rather than confirmatory role of the multi-method comparison."

---

## Task P-09: Post-holdout: decide whether sfas/CC25 run is needed for submission

**Priority: P1 decision gate**  
**Trigger:** After Phase 0 (predecessor disclosure) is complete

Once the arXiv:2412.16181 (Vahidi & Koutis) and JOCO predecessor disclosures are in place,  
reassess whether reviewers will require a comparison against the CC25 external code. If the  
COAP manuscript now transparently acknowledges that WMSF is a reimplementation of CC25, a  
reviewer may ask: "Did you compare against the original CC25 code?" 

**Decision tree:**
1. If CC25 has publicly available code supporting weighted digraphs → run on EXP4 instances  
   and report as "reimplementation consistency check"
2. If CC25 code is unavailable or unweighted → add explicit note: "CC25 external code is not  
   available in weighted-digraph form; WMSF in this study is a reimplementation of the CC25  
   algorithm verified against the paper description"
3. If CC25 code exists but differs significantly from wmsf.py → investigate discrepancy before  
   submission

---

## Timeline recommendation

| Phase | Tasks | When |
|---|---|---|
| Immediately (before finishing Phase 0) | P-01 (sfas identity), P-07 (EC-02 denominator) | As soon as Phase 0 begins |
| After Phase 0 (novelty disclosure) | P-02 (DRMacIver/Eades text), P-05 (borda labeling), P-09 (sfas/CC25 decision) | During manuscript editing |
| After Phase 2 (holdout post-processing) | P-03 (DRMacIver multi-run check) | Only if time permits |
| Post-submission or reviewer response | P-04, P-06, P-08 | As needed |

---

## Non-recommended actions

The following actions are **explicitly not recommended** based on this audit:

| Action | Reason not recommended |
|---|---|
| Add fas-smartAE (networkit) as weighted baseline | Unweighted algorithm; wrong objective for MWFAS comparison |
| Run LOP_MA-EDM on sparse benchmark | Structural mismatch (LOP format vs sparse DIMACS) |
| Add igraph exact IP as EXP4 heuristic comparison | Wrong category — exact method not heuristic; redundant with EXP3 |
| Run Baharev et al. exact solver | No public code available; EXP8 already covers medium-instance exact validation |
| Run SST16 web-scale FAS on benchmark | Designed for web-scale graphs; instances are medium-scale; paradigm mismatch |
| Run DF03 reference implementation | No known public implementation; would require implementing from paper |
| Remove DRMacIver from comparison | Despite non-determinism and 4 failures it is the strongest external comparison; removal weakens the paper |
