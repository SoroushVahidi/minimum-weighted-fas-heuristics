# Repository Audit — minimum-weighted-fas-heuristics
**Date:** 2026-06-06  
**Auditor:** Claude Sonnet 4.6 (automated)  
**Working directory:** `~/minimum-weighted-fas-heuristics`  
**GitHub:** `SoroushVahidi/minimum-weighted-fas-heuristics` (PRIVATE)

---

## Executive Summary

The repository is in **good shape** for a paper-supporting codebase. EXP1b (the
definitive benchmark with full WMSF seed) has **finished and been pushed**.
Imports work, all three scripts run cleanly on a tiny audit graph. The package
structure is clean with no circular imports.

**Main issues** (none are blockers for citation, but EXP2 is needed before
full paper submission):

| Priority | Issue |
|---|---|
| Medium | EXP2 ablation not yet run; 2 of 8 variants require code changes first |
| Low | `reproduce_all.py` relies on `wmsf_seed_mode` default instead of passing it explicitly |
| Low | `.gitignore` lacks `*.log` and `venv/` exclusions |
| Low | `setup.py` `install_requires` only lists `pandas`; `numpy` / `networkx` etc. are in `requirements.txt` but not enforced on install |
| Cosmetic | `find_any_cycle_eids_global` in `ipsns.py` duplicates `find_any_cycle_eids` in `lrta.py` (near-identical) |

---

## 1. Git and GitHub Status

| Field | Value |
|---|---|
| Current branch | `main` |
| HEAD commit | `7129e76100b8571ce41169bdb8617500efe32f0b` |
| Sync with origin | Up-to-date (nothing to push) |
| Last push | 2026-06-06T17:00:17Z |
| GitHub visibility | **PRIVATE** |
| Default branch | `main` |

**Untracked files** (not committed; not accidentally included):

```
experiments/exp1_core_benchmark/exp1_core_benchmark.log
experiments/exp1b_core_benchmark_full_wmsf_seed/logs/
results/
```

These are correctly excluded or untracked. No staged/unstaged changes.

**Recent commit history:**

```
7129e76  Add EXP1b full WMSF seed benchmark results        ← HEAD
c787c0f  Use full WMSF seed in IPSNS
87317f3  Diagnose EXP1 anomaly cases
b1d36e9  Add EXP1 core benchmark results
aeeacd5  Prepare EXP2 ablation experiment plan
```

---

## 2. File Tree Summary

| Metric | Value |
|---|---|
| Tracked files | 69 |
| Total disk usage | 14 MB |
| Untracked directories | `results/`, `experiments/exp1b_.../logs/` |

**Largest tracked files** (by size):

| File | Size (bytes) |
|---|---|
| `experiments/exp1b_.../raw/.../s38417_*.csv` (×3) | 268 858 each |
| `experiments/exp1_.../raw/.../s38417_*.csv` (×3) | 268 858 each |
| `Fast_Local_Ratio_...JOCO.zip` | 202 128 |
| notebooks (×2) | ~82 000 each |

**Are large raw outputs accidentally tracked?** No. The raw per-instance ranking
CSVs are present under `experiments/*/raw/` because git tracks them via an
exception in `.gitignore` (`!experiments/*/tables/*.csv` and
`!experiments/*/summary/*.csv` are whitelisted; raw CSVs are excluded by the
`*.csv` blanket rule). Wait — the raw ranking CSVs (`experiments/*/raw/full_benchmark/raw/*.csv`)
are actually tracked in git. Checking git-tracked files confirms this: they are
not present in `git ls-files`. The raw files are **not tracked**; only summary
and table CSVs are tracked.

**`.gitignore` coverage:**

| Pattern | Covered? |
|---|---|
| `__pycache__/` | Yes |
| `*.py[cod]`, `*.pyo` | Yes |
| `.pytest_cache/`, `.mypy_cache/` | Yes |
| `*.egg-info/`, `dist/`, `build/` | Yes |
| `results/raw/`, `results/processed/` | Yes |
| `experiments/*/raw/` | Yes |
| `*.csv` (blanket, with exceptions) | Yes |
| `*.log` | **No** — logs are untracked only because they live in gitignored dirs or were never added; no explicit rule |
| `venv/`, `.venv/` | **No** — no virtual-environment exclusion |
| Large benchmark `.d` files | Excluded by not being in the repo at all |

**Recommendation:** Add `*.log` and `venv/` / `.venv/` to `.gitignore`.

---

## 3. Python Package Audit

### Structure

```
src/mwfas/
  __init__.py      # version = "0.1.0"
  io.py            # read_graph_dimacs_agg
  evaluation.py    # compute_forward_backward
  lrta.py          # LR-TA algorithm
  wmsf.py          # WMSF algorithm
  ipsns.py         # IPSNS algorithm
```

`baselines.py` does **not** exist (expected; all three algorithms are internal).

### Public entry points

| Function | Module | Purpose |
|---|---|---|
| `read_graph_dimacs_agg` | `io` | DIMACS reader; aggregates parallel arcs |
| `compute_forward_backward` | `evaluation` | Computes total/fw/bw weights |
| `paper_fas_ranking_from_dimacs_fast` | `lrta` | LR-TA end-to-end; writes ranking CSV |
| `wmsf_ranking_from_dimacs_fast` | `wmsf` | WMSF end-to-end; writes ranking CSV |
| `lns_merge_wmsf_lr_best_incumbent` | `ipsns` | IPSNS end-to-end; writes ranking CSV |

### Import paths
All internal imports use relative imports (`from .io import ...`). No circular
imports. `pandas` is imported lazily inside entry-point functions (not at module
level), which is correct for performance.

### Installation

```
python -m pip install -e .   → success (confirmed during audit)
```

`setup.py` declares only `pandas` in `install_requires`. `numpy`, `networkx`,
`pyyaml`, and `tqdm` are in `requirements.txt` but are **not actually imported**
by any core module — they are listed "for completeness" per README. This is
correct; the discrepancy is documented.

### IPSNS default `wmsf_seed_mode`

`lns_merge_wmsf_lr_best_incumbent` signature:
```python
def lns_merge_wmsf_lr_best_incumbent(..., wmsf_seed_mode="full", ...):
```
**Default is `"full"`** — confirmed. ✓

### Duplicate code

`find_any_cycle_eids_global` (ipsns.py:483) is a near-identical copy of
`find_any_cycle_eids` (lrta.py:54). The only difference is that the IPSNS
version tracks `touched` instead of `visited_nodes`. This duplication is minor
and intentional (the IPSNS version is a slightly adapted copy for internal
use). Consolidation would be a post-paper cleanup item, not a blocker.

### Comments / docstrings for reproducibility

All public functions have docstrings describing parameters, algorithm steps, and
return values. Internal helpers have at minimum a one-line docstring. The level
of documentation is **sufficient for paper reproducibility**.

---

## 4. Script Audit

### `scripts/run_lrta.py`

| Item | Value |
|---|---|
| CLI args | `--input` (required), `--output` (required), `--tol` (default 1e-12) |
| Deterministic | Yes |
| Error handling | No try/except; argparse covers missing required args |
| Output CSV | `Node ID, Order` |

### `scripts/run_wmsf.py`

| Item | Value |
|---|---|
| CLI args | `--input`, `--output`, `--ordering` (default `L2`), `--tol` |
| Deterministic | Yes |
| Error handling | No try/except |
| Output CSV | `Node ID, Order` |

### `scripts/run_ipsns.py`

| Item | Value |
|---|---|
| CLI args | `--input`, `--output`, `--seed-ordering` (L2), `--iters` (400), `--topk-scc` (15), `--destroy-addback-frac` (0.30), `--destroy-remove-frac` (0.02), `--tol`, `--rng-seed` (1), `--log-every` (10), `--wmsf-seed-mode` (default `full`) |
| Deterministic | Yes (given fixed `--rng-seed`) |
| Error handling | No try/except |
| Output CSV | `Node ID, Order` |
| `wmsf_seed_mode` default | **`full`** ✓ |

### `scripts/reproduce_all.py`

| Item | Value |
|---|---|
| CLI args | `--instances` (configs/benchmark_instances.txt), `--dataset-dir` (""), `--results-dir` (results/), `--ipsns-iters` (400), `--rng-seed` (1) |
| Uses full WMSF seed? | **Yes** — calls `lns_merge_wmsf_lr_best_incumbent` without overriding `wmsf_seed_mode`; the default is `"full"`. |
| Error handling | Yes — try/except per instance; errors recorded in summary CSV |
| Output | `results/processed/summary.csv` |

**Issue:** `reproduce_all.py` does not pass `wmsf_seed_mode="full"` explicitly.
It relies on the function default. If the default ever changes back to `"legacy"`,
the script would silently produce different results. Recommend adding `wmsf_seed_mode="full"`
explicitly to the `ipsns` kwargs dict.

---

## 5. Experiment Audit

### EXP1 — `experiments/exp1_core_benchmark/`

| Field | Value |
|---|---|
| Purpose | Initial core benchmark; 123 instances, legacy WMSF seed |
| Status | **Finished — superseded by EXP1b** |
| Instances | 105/123 (18 duplicates merged, 2 empty graphs corrected post-run) |
| Errors | 0 (after corrections) |
| Incumbent violations | 1 (explained: IPSNS internal WMSF seed was legacy/L2-only; standalone WMSF used full L1+L2+Stabilize pipeline — not a true algorithmic violation) |
| Summary files | `summary/exp1_core_benchmark_stats.json`, `summary/exp1_core_benchmark_summary.md`, `summary/exp1_raw_summary.csv`, `tables/exp1_core_benchmark_paper_summary.csv` |
| Raw outputs tracked? | No — raw CSVs are gitignored |
| Paper-ready? | **No** — superseded; do not cite EXP1 results in the paper |
| Log tracked? | No — `exp1_core_benchmark.log` is untracked |

### EXP1b — `experiments/exp1b_core_benchmark_full_wmsf_seed/`

| Field | Value |
|---|---|
| Purpose | Definitive benchmark with full WMSF seed matching standalone algorithm |
| Status | **FINISHED** (completed 2026-06-06 13:00 EDT, committed, pushed) |
| Instances | 105 (same set as EXP1; 123-instance list, 18 duplicates removed) |
| Errors | 0 |
| Incumbent violations | **0** |
| Git hash at run time | `c787c0f` |
| WMSF seed mode | `full` |
| Summary files | `summary/exp1b_core_benchmark_stats.json`, `summary/exp1b_core_benchmark_summary.md`, `summary/exp1b_raw_summary.csv`, `tables/exp1b_core_benchmark_paper_summary.csv`, `tables/exp1b_core_benchmark_wide_summary.csv` |
| Raw outputs tracked? | No — raw CSVs are gitignored |
| Paper-ready? | **Yes** |
| Log tracked? | No — `logs/` directory is untracked |

**EXP1b key results:**

| Metric | Value |
|---|---|
| n_instances | 105 |
| IPSNS improves over LR-TA | 16/105 instances |
| IPSNS improves over WMSF | 36/105 instances |
| IPSNS ≥ LR-TA (no-worse) | 105/105 |
| IPSNS ≥ WMSF (no-worse) | 105/105 |
| Mean gain over best seed (abs BW) | 595.42 |
| Mean relative gain over best seed | 0.42% |
| Mean IPSNS runtime | 20.2 sec/instance |
| Mean LR-TA runtime | 0.074 sec/instance |
| Mean WMSF runtime | 1.24 sec/instance |

### EXP2 — `experiments/exp2_ablation/`

| Field | Value |
|---|---|
| Purpose | Ablation study: contribution of each component |
| Status | **Prepared / NOT RUN** |
| Runnable variants | `lrta_full`, `wmsf_seed`, `best_seed_no_lns`, `ipsns_50iters`, `ipsns_100iters`, `ipsns_full` (6/8) |
| TODO variants | `lr_no_addback` (needs `add_back` flag in `lrta.py`), `ipsns_no_scc_priority` (needs `scc_select_mode` param in `ipsns.py`) |
| Instance subset | 10 instances (`configs/exp2_ablation_instances.txt`) |
| Output tables | Template only — no actual results yet |
| Paper-ready? | **No** |

### seedfix_full_wmsf — `experiments/seedfix_full_wmsf/`

| Field | Value |
|---|---|
| Purpose | Diagnostic: confirmed that full WMSF seed (L1+L2+Stabilize per SCC) matches standalone WMSF; documents EXP1 anomaly |
| Status | **Complete / Archived** |
| Key output | `seedfix_report.md`, `smoke_test_10inst.txt`, `diagnostic_seed_comparison_raw.txt` |
| Paper-ready? | Informational only; not a paper table |

### `results/` (untracked top-level results)

Contains outputs from a previous `reproduce_all.py` run. Untracked and
gitignored. Not a problem; can be regenerated.

---

## 6. Reproducibility Audit

| Requirement | Met? | Notes |
|---|---|---|
| How to install dependencies | ✓ | README: `pip install -r requirements.txt && pip install -e .` |
| How to run one instance | ✓ | README: example commands for all three scripts |
| How to reproduce EXP1b | Partial | `run_exp1b_full_wmsf_seed_tmux.sh` exists; README doesn't mention it explicitly |
| How to run ablations (EXP2) | Partial | `experiments/exp2_ablation/README.md` documents it; main README does not |
| Where benchmark instances come from | ✓ | README: `alidasdan/graph-benchmarks` GitHub repo |
| Raw benchmark `.d` files included? | No | Only referenced; user must download |
| Original notebooks preserved | ✓ | `notebooks/local_ratio_original/` and `notebooks/ipsns_original/` |
| Repo visibility | PRIVATE | Must be made public before citation |

---

## 7. Code Quality and Reproducibility Issues

### TODO / FIXME items

| Location | Content | Priority |
|---|---|---|
| `experiments/exp2_ablation/configs/ablation_plan.yaml` | Two TODO variants need code changes | Medium (before EXP2 runs) |
| `experiments/exp2_ablation/summary/exp2_ablation_template.md` | All result cells are TODO | Medium (data needed) |
| `experiments/exp2_ablation/run_exp2_ablation_tmux.sh` | `NotImplementedError` for todo variants | Medium (expected) |

### Hard-coded paths

`docs/repository_notes.md` mentions the old path
`/mmfs1/home/sv96/Feedback-arc-set-paper/datasets/` as a *past issue now
resolved*. No hard-coded paths remain in `src/`, `scripts/`, or active configs.
The only occurrence is the historical note in `docs/`, which is appropriate.

### Legacy WMSF seed mode

| Location | Status |
|---|---|
| `src/mwfas/ipsns.py`: `wmsf_seed_mode="full"` default | ✓ Correct |
| `scripts/run_ipsns.py`: `--wmsf-seed-mode` default `"full"` | ✓ Correct |
| `experiments/exp1b_.../logs/exp1b_core_benchmark.log` | Confirms `wmsf_seed_mode default = 'full'` |
| `experiments/seedfix_full_wmsf/seedfix_report.md` | Explains the change |
| `scripts/reproduce_all.py` | Uses default (implicitly `"full"`) — not explicit |

**Recommendation:** In `reproduce_all.py`, change:
```python
("ipsns", lns_merge_wmsf_lr_best_incumbent, {"iters": ipsns_iters, "rng_seed": rng_seed, "log_every": 0}),
```
to:
```python
("ipsns", lns_merge_wmsf_lr_best_incumbent, {"iters": ipsns_iters, "rng_seed": rng_seed, "log_every": 0, "wmsf_seed_mode": "full"}),
```

---

## 8. Manuscript-Readiness Audit

### Is the repository ready to be cited?

**Not yet** — the repo is PRIVATE and EXP2 (ablation) has not been run. Once
the paper is submitted, the repo should be made public and a Zenodo/GitHub
release should be created.

### What must be fixed before citation?

1. Make the repo **public** before or upon paper submission.
2. Run **EXP2 ablation** (requires code changes for 2 TODO variants; 6 runnable
   variants can run now).
3. Optionally: add explicit `wmsf_seed_mode="full"` in `reproduce_all.py`.
4. Optionally: add `*.log` and `venv/` to `.gitignore`.

### Which experiments are complete?

| Experiment | Status |
|---|---|
| EXP1 (legacy seed) | Complete — **superseded** by EXP1b |
| EXP1b (full WMSF seed) | **Complete — definitive main benchmark** |
| seedfix diagnostic | Complete — archived |
| EXP2 ablation | **NOT RUN** |

### Which result should be cited as the main benchmark?

**EXP1b** (`experiments/exp1b_core_benchmark_full_wmsf_seed/`). EXP1 is
superseded and should not appear in the paper (or should be clearly marked
as a preliminary run).

### Exact commit hash for current results

```
7129e76100b8571ce41169bdb8617500efe32f0b
```

(Commit message: "Add EXP1b full WMSF seed benchmark results")

### Title/contribution framing

The code supports a paper on LR-TA + WMSF + IPSNS for the Minimum Weighted
Feedback Arc Set problem. The key contribution framing consistent with the code:

- **LR-TA** (Local-Ratio Topological Add-back): Phase 1 cycle reductions +
  Phase 2 add-back. Novel: the topological add-back pass.
- **WMSF**: reimplementation of the paper049 removeArcs/Minimize/Stabilize
  pipeline for weighted MFAS.
- **IPSNS**: LNS meta-heuristic combining both seeds with incumbent protection.
  Novel: SCC-local destroy+repair with a guaranteed non-worsening bound.

---

## 9. Known Issues

1. **EXP2 not run** — ablation study is critical for paper submission. Two variants
   need code changes (`lr_no_addback`, `ipsns_no_scc_priority`).
2. **`reproduce_all.py` implicit `wmsf_seed_mode`** — relies on function default
   instead of passing `"full"` explicitly.
3. **`.gitignore` gaps** — no `*.log` rule; no `venv/` rule.
4. **`setup.py` incomplete `install_requires`** — only `pandas` listed; `numpy`
   etc. are in `requirements.txt` but not enforced on `pip install`.
5. **Code duplication** — `find_any_cycle_eids_global` in `ipsns.py` vs
   `find_any_cycle_eids` in `lrta.py` are near-identical.
6. **EXP1 has 1 incumbent violation** — properly explained and fixed in EXP1b,
   but EXP1 summary still shows `"incumbent_protection_violations": 1`. The
   summary note explains this is not a true violation.
7. **Repo is PRIVATE** — must be made public before citation.

---

## 10. Recommended Next Actions

### Before paper submission (required)

1. **Run EXP2 ablation:**
   - First implement `lr_no_addback` flag in `lrta.py` and `ipsns_no_scc_priority` param in `ipsns.py`.
   - Then run `bash experiments/exp2_ablation/run_exp2_ablation_tmux.sh`.
   - Fill in `experiments/exp2_ablation/summary/exp2_ablation_template.md`.

2. **Make repo public** when ready to share.

### Recommended cleanups (low priority)

3. Add `wmsf_seed_mode="full"` explicitly in `reproduce_all.py` IPSNS kwargs.
4. Add `*.log` and `venv/` to `.gitignore`.
5. Consider adding `numpy` to `setup.py` `install_requires` (or remove it from
   `requirements.txt` if truly unused).
6. Optionally consolidate `find_any_cycle_eids_global` in `ipsns.py` to reuse
   `find_any_cycle_eids` from `lrta.py` (cosmetic cleanup; not urgent).

---

## 11. Exact Commands Run During Audit

```bash
# Session check
tmux ls
tmux has-session -t mwfas_exp1b

# Git/GitHub
git status
git branch -vv
git remote -v
git log --oneline --decorate --graph -20
git rev-parse HEAD
gh repo view SoroushVahidi/minimum-weighted-fas-heuristics --json ...

# File tree
find . -maxdepth 6 -type f | sort
git ls-files | wc -l
git status --porcelain
du -sh .
find . -type f -printf "%s %p\n" | sort -nr | head -30

# Package install and imports
python -m pip install -e .
python -c "from mwfas.io import ...; from mwfas.lrta import ...; from mwfas.wmsf import ...; from mwfas.ipsns import ...; print('imports ok')"

# Tiny audit run
cat > /tmp/audit_tiny_mwfas.d <<EOF  (3-node cycle graph)
python scripts/run_lrta.py --input /tmp/audit_tiny_mwfas.d --output /tmp/audit_lrta.csv
python scripts/run_wmsf.py --input /tmp/audit_tiny_mwfas.d --output /tmp/audit_wmsf.csv
python scripts/run_ipsns.py --input /tmp/audit_tiny_mwfas.d --output /tmp/audit_ipsns.csv --iters 10 --wmsf-seed-mode full

# Code quality
grep -R "TODO|FIXME|NotImplemented|placeholder|if applicable" -n src scripts experiments docs README.md
grep -R "/mmfs1|/home/sv96|Feedback-arc-set-paper|datasets/s" -n src scripts configs experiments docs README.md
grep -R "legacy|wmsf_seed_mode" -n src scripts experiments README.md docs
```

---

## 12. Final Verdict

| Category | Grade | Notes |
|---|---|---|
| Code correctness | ✅ Pass | Imports clean; tiny run correct; 0 violations in EXP1b |
| Package structure | ✅ Pass | Clean `src/mwfas` layout; no circular imports |
| Experiment completeness | ⚠️ Partial | EXP1b done; EXP2 not started |
| Reproducibility | ✅ Good | README documents install + run; instances referenced not bundled |
| Manuscript-readiness | ⚠️ Not yet | EXP2 needed; repo must go public |
| Git hygiene | ✅ Good | No large files accidentally tracked; no hard-coded paths in code |
| WMSF seed consistency | ✅ Pass | Default is `"full"` in both function and CLI |

**The repository is production-quality for EXP1b results. The remaining
pre-submission requirement is EXP2 (ablation study).**
