# SNCS Retargeting — Pass 1 Build and Validation Report

**Date:** 2026-06-17
**Branch:** `sncs-retargeting`

## Manuscript build

```
cd paper_sncs && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Result: **succeeded.** `main.pdf` written, 203,032 bytes, SHA-256 `26f314fba0f757a53cbd5c04b578e87352323534a292060bbdcd973a244f3efa`.

| Check | Result |
|---|---|
| Compile errors | None |
| Undefined references / citations | None found |
| Page count | 25 pages (COAP: 24 pages — the extra page is the longer structured abstract) |
| Overfull/underfull box warnings | Present, but identical in kind/location to the COAP build (e.g., the `table_baseline_provenance.tex` overfull hbox is byte-identical source to COAP's — confirmed via `diff`). No new layout regressions introduced by this pass's edits. |
| Title page | Rendered correctly (visually inspected, page 1) |
| Abstract / keywords | Rendered correctly, structured Purpose/Methods/Results/Conclusion labels visible (visually inspected, page 1) |
| Declarations page | Rendered correctly with new Ethics approval / Consent to participate / Consent for publication subsections (visually inspected, page 21) |
| References | Render correctly through entry [25] (visually inspected, page 25) |

Abstract word count (recomputed by script): **246 words**, within the SNCS 150–250 word guideline.

## Test suites

### Main pytest suite

```
PYTHONPATH=src python3 -m pytest --ignore=experiments/exp4_external_baselines/external_tools -q
```

Result: **90 passed, 1 skipped**, exit code 0. Matches the baseline documented in the repository root `README.md`.

### Online Resource 1 pytest suite

```
cd online_resource_1 && PYTHONPATH=src python3 -m pytest -q
```

Result: **79 passed, 7 skipped**, exit code 0.

### `compileall` syntax check

```
python3 -m compileall -q src scripts experiments online_resource_1/src online_resource_1/scripts online_resource_1/tests
```

Result: two pre-existing syntax errors in `experiments/exp4_external_baselines/external_tools/Feedback-Arc-Set/` (vendored third-party Python 2 code — `__getitem__(self, (i, j))` tuple-parameter syntax and a Python 2 `print` statement). This directory is explicitly excluded from the pytest run via `--ignore` in the repository's own documented test command and is not part of this codebase; not a regression from this pass.

### `online_resource_1/scripts/validate_artifact.sh`

First run reported `FAIL: cache files present` because the pytest runs immediately before it had populated `__pycache__`/`.pytest_cache` directories inside `online_resource_1/` (these are gitignored, not tracked, and were never part of `git status`). After removing those self-generated cache directories and re-running:

```
=== VALIDATION PASSED ===
```

All sub-checks passed: required files present, no `/home/soroush` absolute paths, no cache files, JSON parses, smoke validation passed (`dag_path.d`, `triangle.d`, `two_cycle.d`, topo-extraction smoke), test gate passed (79 passed / 7 skipped), and all principal table checks passed (EXP4 DR rel gap 21.6076, EXP3 56/57, EXP10 38/55/0 medians and 21.60% mean, EXP11 checks). Cache directories were removed again after this run; `git status` is clean of any cache artifacts.

### `git diff --check`

```
git diff --check
```

Result: exit code 0, no whitespace errors.

### Scope check — no unintended changes

```
git status --short
```

Confirms only the following are modified or newly added: `README.md` (modified), `docs/MANUSCRIPT_AND_ARTIFACT_STATUS.md` (modified), `paper_sncs/` (new, untracked), `docs/sncs_preparation_202606/` (new, untracked). `paper_coap/`, `src/`, `tests/`, `scripts/`, `experiments/`, `online_resource_1/` are byte-for-byte unmodified. A `git add -A --dry-run` listing was inspected line by line to confirm no cache files, `.pyc` files, or other build artifacts would be staged.

## Conclusion

The SNCS manuscript builds cleanly, all test suites pass at their documented baselines, the artifact validation gate passes, and no scope leakage outside `paper_sncs/` and the two documentation files occurred.
