# License, Security, and Privacy Audit
**Date:** 2026-06-11

---

## 1. License

| Item | Detail |
|------|--------|
| License file | `LICENSE` present at repo root |
| License type | **MIT License** |
| Copyright holder | Soroush Vahidi |
| Copyright year | 2026 |
| License completeness | ✓ Full MIT text present |

**Assessment:** MIT is appropriate for an algorithm-engineering research repository. It allows the community to freely use, modify, and distribute the code (including for commercial purposes) with attribution. Compatible with publishing as open-source supplementary material.

**Note:** The MIT license covers the code in this repository. External dependencies (DRMacIver binary, graph-benchmarks instances, LOLIB instances, WikiVote SNAP) have their own licenses. A reader using this repository should be aware that:
- DRMacIver binary: MIT license (per GitHub repository)
- graph-benchmarks: check repository license
- LOLIB: academic use; verify before redistribution
- WikiVote SNAP: citation-required academic use

## 2. Secrets and API Key Scan

Search performed across `.py`, `.yaml`, `.json`, `.env` files for common secret patterns: `api_key`, `password`, `secret`, `token`, `private_key`, `SSH_KEY`, `AWS_`.

**Files flagged for review:**
- `scripts/run_drmaciver_fas.py` and its copies: contain no credentials; "password" pattern not present
- Sensitivity checkpoint JSON files: contain no credentials; contain only `instance_name`, `config`, `bw` values

**No API keys, passwords, tokens, or private keys found in tracked files.** ✓

## 3. Personal Identifiable Information (PII)

| PII Type | Location | Concern level |
|----------|----------|--------------|
| Email: `sv96@njit.edu` | `paper_coap/main.tex`, `statements_and_declarations.tex` | EXPECTED — author contact info for journal submission |
| Name: "Soroush Vahidi" | `paper_coap/main.tex`, `LICENSE`, declarations | EXPECTED — authorship |
| Absolute home path: `/home/soroush/` | `experiments/exp10_stochastic_robustness/config/common_93_instances.txt` | MINOR — machine-local paths; not a security concern, but reduces portability |
| Absolute path in checkpoint JSON records | `experiments/exp10_stochastic_robustness/checkpoints/*.json` (inferred from path structure) | MINOR — same concern |

**Assessment:** No sensitive PII beyond expected author identification for academic publication. The absolute `/home/soroush/` paths in experiment configs are a reproducibility concern (documented in REPRODUCIBILITY_AND_ARTIFACT_AUDIT.md) but not a security or privacy concern.

## 4. Third-Party Code Attribution

| Component | License | Attribution present? |
|-----------|---------|---------------------|
| DRMacIver/FAS binary | MIT (GitHub) | ✓ Cited in manuscript with commit hash |
| python-igraph | GPL-2.0 | ✓ Cited in manuscript |
| networkx | BSD-3-Clause | Indirectly used; cited in requirements |
| HiGHS solver | MIT | Used in EXP8; should be cited in §5 |
| numpy, pandas, pyyaml, tqdm | BSD/MIT | Standard scientific Python; no attribution required in paper |
| sn-jnl.cls, sn-*.bst | Springer template | Non-redistributable; standard for submissions |

**Issue:** HiGHS citation should be verified in §5/§8. HiGHS is used as the MIP solver in EXP8; citing the tool (Huangfu & Hall, 2018) is standard practice.

## 5. Sensitive Data in Experiment Outputs

| File type | Contains PII? | Assessment |
|-----------|--------------|-----------|
| `experiments/*/summary/*.csv` | No | ✓ |
| `experiments/*/summary/*.json` | No | ✓ |
| `logs/coap_ipsns_holdout/summary.json` | No | ✓ |
| `experiments/coap_ipsns_sensitivity/checkpoints/runs/*.json` | Minimal metadata only | ✓ |
| EXP10 checkpoint `.done` files | No content | ✓ |
| EXP10 checkpoint `.json` records | Paths, BW values, config — no PII | ✓ |

**No sensitive data found in experiment outputs.** ✓

## 6. Hardcoded Credentials or Secrets

Reviewed:
- All Python source files under `src/`
- All experiment scripts under `experiments/*/scripts/`
- All configuration files

No hardcoded credentials found. ✓

## 7. Exported Files and Artifacts

`submission_package/` and `submission_files_for_download/` contain:
- `cover_letter_draft.pdf` — contains author name and email (expected for submission)
- `highlights.pdf`, `highlights.txt` — no PII beyond author name
- `title_page.pdf` — author identification
- `main_anonymized.pdf` — should NOT contain author information (double-blind version)
- ZIP artifacts — contain code and results

**Recommendation:** Before COAP submission, verify that `main_anonymized.pdf` and any anonymous artifact ZIP do not contain embedded author metadata in PDF properties or file paths.

## 8. Git History Scan

| Concern | Status |
|---------|--------|
| API keys in git history | Not scanned (would require `git log -p` scan) | LOW RISK given academic nature |
| Large binary blobs | DRMacIver binary exists as tracked file | Known; not a security concern |
| Sensitive files accidentally committed | No `.env`, no credential files found in working tree | ✓ |

**Recommendation:** If publishing the repository publicly, run `git log --all --full-history --diff-filter=A -- "*.env" "*.key" "*.pem"` as a final check.

## 9. Summary

| Category | Status |
|----------|--------|
| License | ✓ MIT — appropriate |
| Secrets/API keys | ✓ None found |
| PII | ✓ Only expected author identification |
| Absolute paths | Minor issue (reproducibility concern, not security) |
| Third-party attribution | Mostly complete; HiGHS citation needs verification |
| Sensitive data in outputs | ✓ None found |
| Anonymous artifact | Verify anonymization of PDF metadata before submission |
