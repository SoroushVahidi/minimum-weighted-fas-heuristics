# Baseline Execution Readiness Audit

**Audit date:** 2026-06-11  
**Auditor:** Repository-grounded read-only audit; no code run, no software installed.  
**Scope:** All baselines claimed, planned, attempted, or mentioned in the COAP manuscript or
experiment infrastructure.

---

## Part A: Canonical baseline inventory (code-confirmed)

### A.1 Runnable baselines — status table

| ID | Category | Weighted? | Runnable? | Code location | EXP used | Notes |
|---|---|---|---|---|---|---|
| `borda_net_score` | **In-repo local adaptation** | Partial (uses edge weights for score only) | Yes | `src/mwfas/baselines.py:order_by_borda_net_score_from_dimacs` | EXP4 | NOT an external method; must not be labelled "external" |
| `weighted_eades` | **In-repo local adaptation** | Partial (arc weights in score) | Yes | `src/mwfas/baselines.py:weighted_eades_ordering_from_dimacs` | EXP4 | NOT the original ELS93 Eades implementation; an independent adaptation |
| `random_multistart` | **In-repo local adaptation** | N/A (random) | Yes | `src/mwfas/baselines.py:random_multistart_ordering_from_dimacs` | EXP4 | Calibration anchor; 100 trials seeded |
| `igraph_approx_eades` | External library heuristic | Formally unweighted (weights passed, algorithm structure is unweighted) | Yes | `scripts/run_igraph_eades.py` | EXP4, EXP5 | python-igraph 1.0.0; `method="eades"`; one-call external tool |
| `drmaciver_fas` | External C binary | Yes (passes per-arc weights as matrix) | Yes (binary present) | `scripts/run_drmaciver_fas.py` | EXP4, EXP5 | Commit 16ff24a; matrix-based pairwise ordering; **non-deterministic** (see A.2) |
| Bitmask DP | In-repo exact solver | Yes | Yes | `src/mwfas/exact.py` | EXP3 (57 instances, n≤20) | Not a heuristic baseline; certified-optimum reference |
| HiGHS MIP | In-repo MIP wrapper | Yes | Yes | `scripts/run_exp8_medium_mip_baseline.py` | EXP8 (15 instances, 120s cap) | scipy.optimize.milp via HiGHS; exact validation, not heuristic comparison |
| `lrta_adj_swap_ls` | EXP7 local search control | Yes | Yes | EXP7 scripts | EXP7 only | Adjacent-swap LS; not in EXP4 external comparison |
| `lrta_insert_ls` | EXP7 local search control | Yes | Yes | EXP7 scripts | EXP7 only | Single-vertex insertion LS |
| `bestseed_insert_ls` | EXP7 local search control | Yes | Yes | EXP7 scripts | EXP7 only | Best-seed insertion LS |

### A.2 DRMacIver non-determinism (newly identified — B-07)

The `baseline_registry.md` notes: "Deterministic for each invocation (but uses `srand(time|pid)` — results may vary slightly between runs on some instances)."

This means:
- EXP4 records one run per instance — if results differ across runs, the comparison is to a single non-reproducible sample.
- The manuscript describes DRMacIver as "locally optimal" (no single-element move improvement), which is a property of any specific run, not a deterministic output.
- This is not flagged in the manuscript as a limitation.
- **Action required:** Manuscript should note that DRMacIver results are from a single run and may vary between executions due to internal PRNG seeding.

### A.3 igraph Eades weight-handling clarification (newly identified — B-08)

python-igraph's `feedback_arc_set(method="eades")` passes arc weights to the igraph C library. However, the Eades (1993) algorithm is structurally designed for unweighted digraphs (greedy source/sink removal by net degree count). The igraph implementation accepts weights but the algorithmic guarantees are for unweighted inputs. On the 97-instance benchmark:
- `igraph_approx_eades` achieves mean BW 95,920 (n_times_best=40 out of 97)
- `weighted_eades` (in-repo adaptation using explicit weight-aware scoring) achieves mean BW 99,689 (n_times_best=42)

The similarity of results (and `igraph_approx_eades` sometimes beating `weighted_eades`) is consistent with an unweighted-core algorithm. The manuscript correctly notes this by explicitly labeling `weighted_eades` as an "adaptation."

**The manuscript label for igraph_approx_eades should clarify that the Eades algorithm does not have a weight-minimization guarantee, only that weights are passed to the igraph implementation.**

---

## Part B: sfas — identity resolution

### B.1 Search findings

An exhaustive grep for `sfas` and `SFAS` across all source code, experiments, bibliography, and documentation files finds the following occurrences:

| File | Occurrence type | Content |
|---|---|---|
| `docs/full_repository_audit_20260610/BASELINE_AUDIT.md` | Prior audit list | "Planned not implemented: sfas, igraph exact_ip" |
| `docs/full_repository_audit_20260610/HISTORICAL_IDEA_TRANSFER_AUDIT.md` | Prior audit list | "sfas / igraph exact_ip baselines — Do before submission if time" |
| `docs/full_repository_audit_20260610/MANUSCRIPT_SCIENTIFIC_AUDIT.md` | Prior audit issue M-05 | "sfas/exact_ip planned but absent" |
| `docs/full_repository_audit_20260610/ROADMAP.md` | Phase 5 heading | "External baselines (sfas, igraph exact_ip)" |
| `docs/full_repository_audit_20260610/EXECUTIVE_SUMMARY.md` | Missing items | "Planned baselines: sfas, igraph exact_ip" |

**No occurrence of `sfas` is found in:**
- Any Python source file (`src/mwfas/*.py`, `scripts/*.py`, `experiments/**/*.py`)
- Any bibliography file (`paper_coap/bibliography/references.bib`)
- Any manuscript LaTeX file
- Any experiment configuration, README, or run log
- Any external tool directory

### B.2 Candidate identifications (inference, not confirmed)

Three candidates are plausible given the project context:

1. **"Stable FAS" from Cavallaro & Cutello 2025 (CC25):** The CC25 paper introduces a "minimal-and-stable" WMSF algorithm. The `StabilizeFas` step in `wmsf.py` (lines ~350–420) implements the stable-swap rule from CC25. Running the published external CC25 code would give an independent test of the reimplementation. No CC25 code is present in the repository. Probability: **moderate**.

2. **fas-smartAE tool (present in `experiments/exp4_external_baselines/external_tools/fas-smartAE/`):** This tool uses networkit's SCC decomposition and implements a heuristic FAS algorithm. It is UNWEIGHTED (no arc weights in its data model; see `networkit_fas.py`). It is also unavailable (networkit not installed). If `sfas` was intended to refer to this tool, it fails both the "weighted" and "available" criteria. Probability: **low** (the abbreviation does not match "smartAE").

3. **Some other "stable FAS" or "sparse FAS" external tool not yet identified:** The name `sfas` could abbreviate "stable FAS," "sparse FAS," or a project-specific term. Without a paper reference or URL, the identity cannot be confirmed.

### B.3 Conclusion

**`sfas` has no established identity in the repository.** The name appears only in prior audit documents written during the manuscript preparation process. No paper, URL, code, or algorithm description is associated with it. It must be treated as identity-unknown until the author confirms what was intended.

**Recommended action (see POST_HOLDOUT_BASELINE_PLAN.md):** The author should clarify whether `sfas` was intended to be (a) the CC25 external code, (b) the fas-smartAE tool, or (c) another method. If it was intended to be the CC25 code, the correct action is to note that WMSF is already a reimplementation of CC25, making an external CC25 run a reimplementation check rather than an independent comparison. If it was intended to be fas-smartAE, it must be noted as unweighted.

---

## Part C: igraph exact IP feasibility summary

### C.1 What it is

python-igraph v1.0.0 exposes `Graph.feedback_arc_set(method="ip")` which solves exact integer programming for minimum feedback arc set. This is documented in `experiments/exp4_external_baselines/summary/external_access_report.md`:

> "Only `method='eades'` tested. The `method='ip'` (exact ILP) is available but belongs to exact comparisons (EXP3-style), not heuristic EXP4."

### C.2 Assessment

| Criterion | Assessment |
|---|---|
| Available | Yes — python-igraph 1.0.0 is installed |
| Weighted support | Yes — passes weights to ILP formulation |
| Feasible on full benchmark (97 instances) | **No** — ILP scales poorly; n>50 instances will timeout |
| Appropriate category | **Exact validation** (alongside bitmask DP and HiGHS MIP), not heuristic comparison |
| Incremental value vs EXP8 HiGHS | Moderate — provides an independent exact oracle up to n~20–30 |
| Integration cost | Low — one line change in existing wrapper |

### C.3 Recommendation

If igraph exact IP is added, it should be run on the EXP3 small-instance subset (n≤20) to cross-validate bitmask DP results. On the 57 EXP3 instances, igraph exact IP can serve as a second independent exact oracle. This is a low-risk, low-cost sanity check, not a new baseline claim. See `EXACT_BASELINE_FEASIBILITY.md` for full assessment.

---

## Part D: fas-smartAE / networkit assessment

### D.1 Current status

| Property | Value |
|---|---|
| Tool location | `experiments/exp4_external_baselines/external_tools/fas-smartAE/` |
| Algorithm | SmartAE heuristic for FAS using networkit SCC decomposition |
| Weighted? | **No** — `networkit_fas.py` uses `Graph` API with no edge-weight support |
| Availability | **Unavailable** — `import networkit` fails; not installed |
| Paper | Unknown — no paper reference in tool files |
| Requirement | `networkit`, `sortedcontainers` (requirements.txt) |

### D.2 Conclusion

fas-smartAE is **doubly disqualified** as a primary comparison baseline:
1. **Unweighted:** Cannot minimize weighted backward arc sum — minimizes cardinality only
2. **Unavailable:** networkit not installed on the experimental machine

Even if networkit were installed, running an unweighted FAS algorithm on weighted instances and comparing backward *weight* (not cardinality) would be misleading. The comparison would not be fair.

**If fas-smartAE is added to the manuscript, it must be explicitly labeled as "unweighted FAS cardinality heuristic" and the comparison metric must be clearly stated.**

---

## Part E: Baseline labeling and manuscript fairness

### E.1 Current labeling issues

| Issue ID | Issue | Detail | Required fix |
|---|---|---|---|
| B-09 | Borda, weighted_eades, random_multistart mislabeled | These are in-repo adaptations, NOT external independent implementations | Manuscript section 5 correctly labels weighted_eades as "adaptation" but must maintain that consistency throughout |
| B-08 | igraph Eades weight guarantee not disclosed | The Eades algorithm does not have a weight-minimization guarantee; this is not stated explicitly | Add one sentence in §5 baseline description |
| B-07 | DRMacIver non-determinism not disclosed | Uses `srand(time|pid)`; one run per instance in EXP4 | Add note in §5 or supplementary |
| B-10 | 4 DRMacIver failures on 97 instances | Correctly reported (93-instance subset for comparison); documented in results | No action needed — already handled |

### E.2 External vs local adaptation classification

| Method | COAP manuscript label | Correct classification |
|---|---|---|
| `borda_net_score` | "Simple baseline" | In-repo local adaptation; not an external published algorithm |
| `weighted_eades` | "Adaptation" | In-repo local adaptation (correctly labeled) |
| `random_multistart` | "Calibration anchor" | In-repo local adaptation (correctly labeled) |
| `igraph_approx_eades` | "Library baseline" | External library call (correctly labeled) |
| `drmaciver_fas` | "External method" | External C binary (correctly labeled) |

---

## Part F: EXP7 local search controls

EXP7 tests three "plain" local search controls that are NOT in EXP4:
- `lrta_adj_swap_ls`: adjacent-swap LS on LR-TA seed — **no improvements found on 18 instances** (LR-TA is already adjacent-swap locally optimal)
- `lrta_insert_ls`: single-vertex insertion LS on LR-TA seed — 4 improvements; still loses to IPSNS on 5 large instances
- `bestseed_insert_ls`: insertion LS on best-of-WMSF-LRTA seed — 3 losses to IPSNS

These serve a distinct purpose: isolating whether IPSNS gains come from generic order-local improvements or SCC structure. They are correctly positioned in the manuscript as ablation controls, not as competing external methods.

---

## Summary of readiness findings

| Finding | Severity | Issue ID |
|---|---|---|
| sfas has no established identity — cannot be run | Major | B-06 (new) |
| igraph exact IP available but should go to EXP3/EXP8 validation, not EXP4 | Moderate | B-06 sub |
| DRMacIver is non-deterministic (srand time/pid); one run per instance not documented in manuscript | Moderate | B-07 (new) |
| igraph Eades weight guarantee not disclosed in baseline description | Low | B-08 (new) |
| fas-smartAE: unweighted + unavailable; unsuitable as weighted baseline | Informational | — |
| Borda/weighted_eades/random_multistart correctly classified as in-repo adaptations | Verified | — |
| EXP4 common subset (93/97 for DRMacIver) handled correctly | Verified | — |
