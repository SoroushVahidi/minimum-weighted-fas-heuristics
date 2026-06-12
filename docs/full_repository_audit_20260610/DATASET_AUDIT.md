# Dataset Audit

**Audit date:** 2026-06-10

## Dataset inventory

| Dataset | Origin | In-repo? | Instances | Citation / license |
|---|---|---|---:|---|
| graph-benchmarks (sparse) | `alidasdan/graph-benchmarks` | **External path** in `configs/benchmark_instances_found_all.txt` | 123 listed → 105 unique → 97 standard | Documented in `docs/baselines_and_datasets_references.md`; GitHub repo |
| LOLIB 2010 | Martí LOLIB / Dropbox mirror | **Yes** — `experiments/exp5_lolib_dense/converted/` | 50 (+ tiny test) | Martí 2012; conversion scripts in experiment |
| SNAP wiki-vote | Leskovec et al. | **Yes** — `experiments/exp9_application_case/converted/` | 2 subgraphs | SNAP; academic use |
| EXP2 ablation subset | Subset of graph-benchmarks | External paths | 10 | Same as sparse |
| COAP sensitivity instances | EXP2 ten | Listed in `coap_ipsns_sensitivity/config/instances.csv` | 10 | Screening subset |
| COAP holdout instances | Stratified from eligible 87 | `coap_ipsns_holdout/config/*.csv` | 18 tuning + 25 holdout | Pre-registered |

## Preprocessing rules (observed)

| Rule | Handling |
|---|---|
| Parallel edges | Summed in `io.read_graph_dimacs_agg` |
| Self-loops | Active if weight > tol; removed in trivial SCCs |
| Zero weight | Deactivated when ≤ tol (default 1e-12) |
| Negative weight | 8 instances excluded from standard benchmark; Eades baseline rejects negatives |
| Node ordering | Sorted lexicographically for determinism |

## Checksums / provenance

- No global checksum manifest for external graph-benchmarks clone
- LOLIB converted files tracked in Git with `.meta.json` sidecars (EXP5)
- **Absolute paths** in tracked CSVs: `/home/soroush/benchmark_sources/graph-benchmarks/...` — breaks relocation

## Issues

| ID | Severity | Finding |
|---|---|---|
| D-01 | Major | External benchmark not vendored — reproducibility requires separate clone |
| D-02 | Moderate | Absolute home paths in tracked configs |
| D-03 | Minor | No checksum file for exact instance files used in experiments |
| D-04 | Low | LOLIB Dropbox mirror URL may change (documented access date) |

## Redistribution

- In-repo LOLIB/SNAP converted files: verify license before public ESM redistribution
- Full graph-benchmarks: link rather than vendoring (current approach)

## Missing

- Explicit LICENSE file for converted LOLIB instances in-repo
- Machine-readable manifest tying each manuscript table row to instance file hash
