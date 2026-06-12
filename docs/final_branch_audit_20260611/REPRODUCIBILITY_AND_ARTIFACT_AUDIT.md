# Reproducibility and Artifact Audit
**Date:** 2026-06-11

---

## 1. Environment Specification

| Item | Present? | Content |
|------|---------|---------|
| `requirements.txt` | ✓ YES | `numpy`, `pandas`, `networkx`, `pyyaml`, `tqdm` (no version pins) |
| `setup.py` | ✓ YES | Package setup for `mwfas` namespace |
| Python version | NOT SPECIFIED | Needed for reproducibility |
| OS pinned | NOT SPECIFIED | Experiments run on Ubuntu (inferred from `uname`); not documented |
| DRMacIver binary | Commit `16ff24a` cited in paper | Binary present at `scripts/drmaciver_fas`; see section 5 |
| HiGHS version | Not specified | Used in EXP8; version affects result |

**Issues:**
- No version pins in `requirements.txt` — a reader installing today may get different numpy/pandas/networkx behavior
- Python version not documented anywhere
- DRMacIver binary is a compiled artifact; source is external (GitHub); commit pinned in paper text but not in `requirements.txt` or config

## 2. Benchmark Data Reproducibility

| Dataset | Source | Reproducible? |
|---------|--------|--------------|
| `graph-benchmarks` core instances | External GitHub repo | ✓ Cited with URL and commit |
| LOLIB 2010 instances | External (lolib.org) | ✓ Cited with URL |
| WikiVote SNAP | SNAP dataset | ✓ Cited with URL |
| Instance paths in EXP10 config | Absolute paths (`/home/soroush/benchmark_sources/`) | ✗ NOT portable |

**Issue:** `experiments/exp10_stochastic_robustness/config/common_93_instances.txt` uses absolute machine-local paths. A reader running on a different machine must edit this file. This is documented behavior (the README or supplementary should note it), but it degrades out-of-box reproducibility.

## 3. Experiment Scripts

| Script | Resumable? | Deterministic? | Documented? |
|--------|-----------|---------------|------------|
| `run_ipsns_repetitions.py` | ✓ Checkpoint system | ✓ Fixed seed sequence 0-19 | Partial |
| `run_drmaciver_repetitions.py` | ✓ Checkpoint system | ✗ DRMacIver uses `srand(time|pid)` | Partial |
| `postprocess.py` | N/A (idempotent) | ✓ | Partial |
| `validate_environment.py` | N/A | N/A | ✓ Good: 7 pre-flight checks |
| EXP1b–EXP9 runners | Varies | ✓ (IPSNS fixed seed in EXP1b+) | Partial |

## 4. Run Command Completeness

The README.md at the repository root should document:
1. How to install the environment
2. How to run EXP1b–EXP9 (the main results)
3. How to run EXP10 (stochastic robustness)
4. How to build the manuscript PDF

Current state of README not verified for completeness; a prior audit found `run_repro_tmux.sh` and similar helper scripts at the root, but their documentation completeness was not assessed.

## 5. DRMacIver Binary Reproducibility

| Item | Status |
|------|--------|
| Binary in repo | ✓ Present at `scripts/drmaciver_fas` |
| Source commit cited | ✓ Commit `16ff24a92fde886e58819180a9fe686e60991c5c` in manuscript |
| Binary OS-specific | ✓ Linux x86-64 only; not portable to macOS/Windows |
| Rebuild instructions | NOT PRESENT — reader cannot rebuild from source without visiting GitHub |
| Hash/checksum | NOT PRESENT — no sha256 for binary provided |

**Recommendation:** Add a `sha256sum` of the DRMacIver binary to the supplementary artifact so readers can verify they have the correct binary.

## 6. Artifact Structure (EJCO Package — Stale)

`submission_package/ejco_reproducibility_artifact/` contains:
- `scripts/` — experiment runner scripts (EJCO-era versions)
- `src/` — algorithm source (EJCO-era snapshot)
- `README.md` — instructions
- `requirements.txt`

**Issue:** This artifact predates the COAP manuscript version, the COAP IPSNS sensitivity holdout, and EXP10. It must not be used as the COAP supplementary material without a full refresh.

## 7. COAP Artifact Requirements (Not Yet Met)

For a computational optimization paper in COAP with a reproducibility claim in the abstract ("A fully reproducible artifact accompanies the paper"), the supplementary material must:

| Requirement | Status |
|-------------|--------|
| Latest algorithm source (`src/mwfas/`) | Must match submitted code | Pending |
| All experiment scripts (EXP1b–EXP10) | EXP10 not complete yet | Pending EXP10 |
| Processed results (EXP1b–EXP9 summaries) | Available in repo | Ready |
| EXP10 results | Not available yet | Pending |
| DRMacIver binary + hash | Binary present | Hash missing |
| README with run instructions | Needs COAP update | Pending |
| Python version specification | Not currently documented | Pending |

## 8. Checkpoint System Assessment

The checkpoint system (per-run `.done` sentinel files + JSON records, atomic `os.replace()` writes) is correctly implemented and has been verified in operation (EXP10 IPSNS runner is currently at 1279/1860). This system is adequate for reproducibility purposes: incomplete runs can be resumed without data loss or duplication.

## 9. Experimental Protocol Reproducibility

| Protocol Aspect | Documented in §5? | Reproducible? |
|----------------|------------------|--------------|
| IPSNS iterations (400) | ✓ | ✓ |
| IPSNS topK_scc (15) | ✓ | ✓ |
| Random seed for IPSNS (seed 0 per instance in EXP4) | Needs clarification | ✓ (seed=0 default) |
| DRMacIver commit | ✓ | ✓ |
| DRMacIver single run per instance (EXP4) | **NOT STATED** | Partially |
| Machine spec | ✓ | ✓ |
| Exact Python/library versions | ✗ NOT STATED | ✗ |

## 10. Clean-Machine Test

A clean-machine test (installing environment from scratch and running all experiments) has **not been performed** for the COAP version. The EJCO artifact was presumably tested, but changes since EJCO (COAP sensitivity holdout, EXP10 addition) mean the artifact needs reverification.

**Recommendation:** Before final submission, perform a clean-environment test:
```bash
python -m venv env && source env/bin/activate
pip install -r requirements.txt
python validate_environment.py
python -m pytest tests/  # once tests exist
```

## 11. Summary

| Category | Status |
|----------|--------|
| Requirements specified | Partial (no version pins, no Python version) |
| DRMacIver reproducibility | Partial (commit cited, no binary hash) |
| Instance data portable | ✗ Absolute paths in EXP10 config |
| Artifact ready | ✗ EJCO artifact stale; COAP artifact not created |
| Checkpoint system | ✓ Correct |
| Clean-machine test | ✗ Not performed |
