# Baseline Fairness Protocol

**Audit date:** 2026-06-11  
**Scope:** Fairness requirements and recommended protocols for all current and future baseline  
comparisons in the COAP manuscript.  
**Status:** Prescriptive — describes what the comparison protocol should satisfy, identifies  
where the current experimental program meets or falls short, and recommends corrective actions.

---

## Principle 1: Algorithm category labeling

### Requirement

Every baseline must be classified into exactly one of four categories in the manuscript,  
and that classification must be consistent across §5 (design), §6 (results), and supplementary:

| Category | Description | Examples |
|---|---|---|
| **External independent heuristic** | Published method from separate authors with public code; run unchanged | DRMacIver/FAS, igraph Eades |
| **In-repo local adaptation** | Method designed or adapted by the authors for this study | Borda net-score, weighted_eades, random_multistart |
| **Exact / certified reference** | Solver that certifies optima (possibly with time cap) | Bitmask DP, HiGHS MIP |
| **Internal method** | The paper's own contribution | LR-TA, WMSF, IPSNS |

### Current compliance

| Baseline | Correct category | Manuscript label | Compliant? |
|---|---|---|---|
| `drmaciver_fas` | External independent heuristic | "External method" | Yes |
| `igraph_approx_eades` | External independent heuristic | "Library baseline" | Yes |
| `borda_net_score` | In-repo local adaptation | "Simple baseline" | Partial — "simple" does not distinguish "in-repo" from "external" |
| `weighted_eades` | In-repo local adaptation | "Adaptation" | Yes (correctly labeled as adaptation) |
| `random_multistart` | In-repo local adaptation | "Calibration anchor" | Yes |
| Bitmask DP | Exact / certified reference | "Certified reference" | Yes |
| HiGHS MIP | Exact / certified reference | "Time-capped MIP baseline" | Yes |

### Action required

**B-09:** Ensure `borda_net_score` is clearly identified as an "in-repo adaptation" rather than  
an independent published method, consistently across §5 and any supplementary tables.

---

## Principle 2: Weight handling transparency

### Requirement

For any baseline applied to weighted instances, the manuscript must state whether:
1. The method minimizes weighted backward arc sum (MWFAS objective)
2. The method minimizes arc cardinality (unweighted FAS) and is applied to weighted instances  
   only as a heuristic
3. The method uses weights in its score function but without a weight-minimization guarantee

### Current compliance

| Baseline | Weight handling | Disclosed in manuscript? |
|---|---|---|
| `drmaciver_fas` | Directly uses pairwise weight matrix; minimizes weighted ordering score | Yes — "weighted-ordering method" |
| `igraph_approx_eades` | Passes weights to Eades; algorithm is structurally unweighted | Partially — manuscript notes Eades is "unweighted" for the in-repo adaptation but igraph version's status is less explicit |
| `weighted_eades` | Uses arc weights in net-score computation; no weight-minimization guarantee | Yes — "labeled explicitly as an adaptation because the original ELS93 algorithm is unweighted" |
| `borda_net_score` | Uses out_w − in_w net score; no FAS guarantee | Implicit in "simple baseline" label |
| `random_multistart` | No weight use; random permutation | Implicit in "calibration anchor" label |

### Action required

**B-08:** Add a sentence clarifying that igraph's `method="eades"` uses weights but that the  
Eades algorithm does not have a weight-minimization guarantee. Suggested addition to §5  
baseline description:

> "The python-igraph Eades implementation accepts arc weights but the Eades algorithm is  
> structurally designed for unweighted digraphs; the weights are passed but do not carry  
> a weighted-FAS-minimization guarantee."

---

## Principle 3: Determinism and reproducibility

### Requirement

For each baseline:
1. State whether the method is deterministic given the same input
2. If non-deterministic: state the number of runs used and how variability is handled
3. If a time limit is used: state the limit explicitly and report cases that exceeded it

### Current compliance

| Baseline | Deterministic? | Runs in EXP4 | Variability handling | Compliant? |
|---|---|---|---|---|
| `drmaciver_fas` | **No** — uses `srand(time\|pid)` | **1 run per instance** | None — single run; variability undisclosed | **No** — B-07 |
| `igraph_approx_eades` | Yes — igraph Eades is deterministic | 1 | N/A | Yes |
| `weighted_eades` | Yes (deterministic net-score sort) | 1 | N/A | Yes |
| `borda_net_score` | Yes (deterministic net-score sort) | 1 | N/A | Yes |
| `random_multistart` | Yes (seeded) | 1 (100 internal trials, fixed seed) | Fixed seed documented | Yes |
| IPSNS | Yes (seeded rng_seed) | 1 | Fixed seed documented | Yes |

### Action required

**B-07:** The manuscript must acknowledge that DRMacIver uses time/PID-based random seeding,  
meaning results may vary between runs. Current EXP4 uses one run per instance. Suggested  
disclosure in §5 or supplementary:

> "DRMacIver/FAS uses an internal random seed derived from system time and process ID, so  
> results may vary between runs. EXP4 records one run per instance; a multi-run sensitivity  
> check on 20 representative instances confirmed that the observed ordering quality was  
> stable across runs [or: should be added]."

**If the multi-run check has not been performed:** It is strongly recommended before submission.  
See `POST_HOLDOUT_BASELINE_PLAN.md` task P-04.

---

## Principle 4: Instance coverage and subset reporting

### Requirement

When a baseline does not complete all instances:
1. Report exact completion counts (N_complete / N_total)
2. Report reason for incompletions (timeout, error, not applicable)
3. Comparative statistics must use only the common completed subset

### Current compliance

| Situation | How handled | Compliant? |
|---|---|---|
| DRMacIver: 93/97 instances | 4 failures (2 DAG inputs rejected by wrapper, 2 large sparse timeouts) reported explicitly; paired tests use 93-instance subset | **Yes** — well-handled |
| 8 negative-weight instances excluded from "standard 97" | Explicitly excluded and noted in §5 | Yes |
| EXP8: 8 of 15 MIP instances timeout | Treated as incomplete evidence, not as infeasible | Yes |

---

## Principle 5: Time budget fairness

### Requirement

When comparing methods with different computational paradigms (heuristic vs. exact; fast vs. slow),  
the manuscript must acknowledge time budget differences rather than presenting a pure quality  
comparison.

### Current compliance

The manuscript correctly reports mean runtime per instance for all methods:
- LR-TA: ~0.08s per instance
- WMSF: ~1.24s
- IPSNS: ~20.2s
- DRMacIver: implicitly much faster on most instances (no explicit time limit except wrapper 300s)
- igraph Eades: fast (no reported time)

**Partial gap:** DRMacIver's mean runtime is not explicitly reported in the results section,  
making the quality comparison somewhat asymmetric (we know IPSNS spends 20s; we don't know how  
long DRMacIver spends on the 93 completed instances).

### Action required

**B-11 (new):** Report mean DRMacIver runtime alongside quality comparison in Table  
`table_sparse_external_baselines.tex` or as a supplementary note.

---

## Principle 6: Paired test scope and multiple comparisons

### Requirement

Paired statistical tests should:
1. Use per-instance pairs on a fixed common subset
2. Report both the test statistic and effect size or win/tie/loss counts
3. Acknowledge that testing multiple baselines inflates false-positive rate

### Current compliance

| Test | Common subset | Method | Win/tie/loss | Multiplicity correction? |
|---|---|---|---|---|
| IPSNS vs DRMacIver | 93 instances | Wilcoxon + sign test, two-sided | 37W/55T/1L | No explicit correction |
| IPSNS vs LR-TA | 97/105 | Descriptive win counts | 16W/81T/0L | No test (internal comparison) |
| IPSNS vs WMSF | 97/105 | Descriptive win counts | 36W/61T/0L | No test (internal comparison) |

**Finding:** The paired tests are appropriately conservative (two-sided). Win/tie/loss counts  
are reported. No multiplicity correction is applied across the 8-method comparison, which is  
standard practice but should be acknowledged.

### Recommended addition

In the statistical testing paragraph in §6, add:

> "Paired tests are performed for the primary external comparison (IPSNS vs. DRMacIver/FAS)  
> only. No multiplicity correction is applied across the full multi-method comparison table,  
> consistent with descriptive rather than confirmatory statistical practice."

---

## Principle 7: Methodology-appropriate metrics

### Requirement

The primary metric must be the problem objective: minimum weighted backward arc sum (backward  
weight = BW). Secondary metrics (win counts, relative excess, forward ratio) must be clearly  
labeled as secondary.

### Current compliance

**Compliant.** Primary metric throughout is BW (backward weight). Win counts, relative excess,  
and forward ratio are all labeled as secondary or "for interpretation." EXP5 also reports  
forward ratio as a secondary measure, appropriate for the LOP-transfer context.

---

## Principle 8: Scope boundary disclosure

### Requirement

The manuscript must state which problem instances and graph families each result applies to.  
A result on "sparse instances" must not be extrapolated to dense instances without evidence.

### Current compliance

**Compliant.** The manuscript draws a clear scope boundary:
- Primary claim: sparse nonnegative weighted digraphs (97 instances)
- Dense transfer: LOLIB 50 instances, explicitly labeled as a transfer test where IPSNS is not dominant
- Exact validation: 57 small instances (n≤20), labeled as near-optimality evidence not approximation guarantee

No overgeneralization observed in the results or conclusion sections.

---

## Protocol gaps summary

| Gap ID | Description | Severity | Principle |
|---|---|---|---|
| B-07 | DRMacIver non-determinism not disclosed; one run per instance | Moderate | 3 |
| B-08 | igraph Eades weight guarantee not stated | Low | 2 |
| B-09 | borda_net_score in-repo origin not clearly labeled "adaptation" vs "external" | Low | 1 |
| B-10 | DRMacIver runtime not reported in comparison table | Low | 5 |
| B-11 | No multiplicity-correction acknowledgment for multi-baseline testing | Low | 6 |

---

## Recommended corrective text block (for §5 or supplementary)

> "The external baselines are run under fixed conditions. DRMacIver/FAS uses an internal  
> time/PID-based random seed; results from a single run per instance are reported, as  
> described in the registry file. The python-igraph Eades implementation accepts arc weights  
> but the Eades algorithm does not carry a weighted-FAS-minimization guarantee. The in-repo  
> adaptations (Borda net-score, weighted Eades, random multistart) are designed and implemented  
> within this project and are not independent published codes."
