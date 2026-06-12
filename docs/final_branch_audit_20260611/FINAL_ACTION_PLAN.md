# Final Action Plan — COAP Submission Readiness
**Date:** 2026-06-11  
**Based on:** MASTER_ISSUE_REGISTER.csv (25 issues: 2 BLOCKER, 3 CRITICAL, 4 MAJOR, 5 MODERATE, 5 MINOR, 4 INFO)

---

## Phase 1: Complete EXP10 (Prerequisite for Everything Else)

### 1.1 Resume/Complete EXP10 IPSNS Phase
- Process PID 24482 is at 1279/1860 and still running
- If it times out, restart with: `python3 experiments/exp10_stochastic_robustness/scripts/run_ipsns_repetitions.py`
- Checkpoint system will skip completed runs; may require multiple restarts for large instances (parker1986, s5378, s9234 each take ~50s/seed)
- Target: 1860/1860 `ipsns_*.done` files

### 1.2 Run EXP10 DRMacIver Phase
- After IPSNS phase complete: `python3 experiments/exp10_stochastic_robustness/scripts/run_drmaciver_repetitions.py`
- 1860 DR runs; 0.12s minimum inter-launch gap; estimated ~4-6 hours
- Target: 1860/1860 `drmaciver_*.done` files

### 1.3 Run EXP10 Postprocessing
- After both phases: `python3 experiments/exp10_stochastic_robustness/scripts/postprocess.py`
- Produces summary statistics, win/tie/loss distributions, median comparisons
- Output: `experiments/exp10_stochastic_robustness/results/`

---

## Phase 2: Manuscript Updates (After EXP10)

### 2.1 Fix DRMacIver Single-Run Disclosure (Issue M-01 / MOD-04)
**File:** `paper_coap/sections/05_experimental_design.tex`  
**Add one sentence** near the DRMacIver description:
> "DRMacIver/FAS was executed as a single run per instance using commit 16ff24a92fde886e58819180a9fe686e60991c5c; the tool uses a time-based random seed, so results may vary across runs."

### 2.2 Integrate EXP10 Results
- Update §6 (results) with EXP10 stochastic robustness findings
- Update §7 (discussion) with robustness analysis
- Add EXP10 section/table if results are materially different from single-run comparison
- If EXP10 confirms 37/55/1 pattern, add a sentence confirming robustness across 20 seeds

### 2.3 Verify HiGHS Citation (Issue MIN-04)
- Check `bibliography/references.bib` for HiGHS entry
- Add if missing: Huangfu Q, Hall JA (2018) Parallelizing the dual revised simplex method. Mathematical Programming Computation 10(1):119–142

### 2.4 Verify EXP2 Ablation Numbers (Issue MIN-02)
- Locate EXP2 raw output files
- Recompute ablation BW values (4271.5, 4525.1, 4239.2) from raw data
- Confirm against `MANUSCRIPT_NUMERICAL_TRACEABILITY.csv` entries marked ASSUMED

---

## Phase 3: Source Code and Repository (Before Committing)

### 3.1 Commit ipsns.py Diagnostic Instrumentation (Issue C-02)
```bash
git add src/mwfas/ipsns.py
git commit -m "Add EXP10 diagnostic counters to IPSNS (gated on return_info)"
```

### 3.2 Commit EXP10 Infrastructure
```bash
git add experiments/exp10_stochastic_robustness/
git add logs/coap_ipsns_holdout/
git add experiments/coap_ipsns_holdout/checkpoints/
git add experiments/coap_ipsns_holdout/results/
git commit -m "Add EXP10 stochastic robustness experiment"
```

### 3.3 Update requirements.txt (Issue M-03)
- Add version pins for all dependencies
- Add Python version comment: `# Tested with Python 3.10.x`
- Example:
  ```
  numpy>=1.24,<2.0
  pandas>=1.5,<3.0
  networkx>=3.0,<4.0
  pyyaml>=6.0
  tqdm>=4.64
  ```

### 3.4 Add DRMacIver Binary Checksum (Issue M-04)
```bash
sha256sum scripts/drmaciver_fas > scripts/drmaciver_fas.sha256
git add scripts/drmaciver_fas.sha256
```

---

## Phase 4: Create COAP Submission Artifact (Issue C-01, C-03)

### 4.1 Create Online Resource 1
Structure should include:
```
mwfas_artifact_coap/
├── README.md              # Installation + run instructions
├── requirements.txt       # With version pins
├── src/mwfas/             # Latest algorithm source
├── experiments/           # EXP1b-EXP10 scripts
├── results/               # Processed summaries
├── scripts/               # drmaciver_fas binary + .sha256
└── data/                  # Instance manifest (no absolute paths)
```

### 4.2 Replace Absolute Paths in Instance Config (Issue M-02)
- Provide a path-setting script or README instruction:
  ```bash
  # Set BENCHMARK_ROOT to your benchmark directory, then:
  sed -i "s|/home/soroush/benchmark_sources|${BENCHMARK_ROOT}|g" \
    experiments/exp10_stochastic_robustness/config/common_93_instances.txt
  ```

### 4.3 Anonymize Artifact for Double-Blind
- Remove author name from README
- Remove absolute paths that reveal username
- Rebuild anonymized PDF with no author metadata

---

## Phase 5: Tests (Issue B-02)

### 5.1 Create Minimal Test Suite
Priority tests (to support the 'fully reproducible artifact' claim):
```
tests/
├── test_exact.py          # Verify DP recurrence on 3-4 tiny known-optimal instances
├── test_lrta.py           # Verify LR-TA produces feasible output (no backward arcs)
├── test_wmsf.py           # Verify WMSF produces feasible output
├── test_ipsns.py          # Verify IPSNS non-worsening guarantee (20 runs)
└── test_io.py             # Verify DIMACS parser on known input
```
These do not need to be comprehensive; they establish a reproducibility baseline.

---

## Phase 6: Submission Package

### 6.1 Rewrite Cover Letter (Issue MIN-05)
- Context: COAP initial submission (or revised submission)
- Include prior submission disclosure (Issue MIN-01): "This paper was previously submitted to [journal names] and [rejected/withdrawn after review]. The current submission has been substantially revised to include..."
- Highlight EXP10 stochastic robustness analysis as new contribution relative to prior submissions

### 6.2 Rebuild Submission Files
```
submission_files_for_download/
├── main.pdf               # Final COAP version
├── main_anonymized.pdf    # Verify anonymization
├── cover_letter.pdf       # Rewritten for COAP
├── highlights.txt         # Update with EXP10 result
├── title_page.pdf         # Author info (for editorial)
└── Online_Resource_1.zip  # COAP artifact
```

### 6.3 Final Checklist Before Submitting
- [ ] `main.pdf` compiles cleanly with no LaTeX errors
- [ ] All figures render correctly
- [ ] Bibliography has no missing references
- [ ] All numbers in manuscript match MASTER_ISSUE_REGISTER + MANUSCRIPT_NUMERICAL_TRACEABILITY.csv
- [ ] Declarations complete
- [ ] ORCID link correct
- [ ] Anonymous artifact verified
- [ ] Cover letter mentions prior submissions

---

## Summary by Priority

| Priority | Issues | Actions |
|----------|--------|---------|
| **Must do before submission** | B-01, B-02, C-01, C-02, C-03, M-01, MOD-04, MIN-01, MIN-05 | EXP10 complete; tests; artifact; manuscript fixes; cover letter |
| **Should do** | M-02, M-03, M-04, MOD-03, MIN-02, MIN-03, MIN-04 | Version pins; checksum; path docs; verify ablation numbers |
| **Can defer** | MOD-01, MOD-02, MOD-05, INFO-01–04 | Minor cleanups; informational only |
