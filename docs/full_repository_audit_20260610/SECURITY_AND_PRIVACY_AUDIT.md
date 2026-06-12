# Security and Privacy Audit

**Audit date:** 2026-06-10  
**Method:** Pattern grep on tracked/untracked text files; git log keyword scan (no secret values printed).

## Findings

| ID | Severity | Finding | Location | Redacted detail |
|---|---|---|---|---|
| SEC-01 | Moderate | **Author email in manuscript PDF** | `paper_coap/main.pdf`, `main.tex` | sv96@njit.edu — intentional for submission |
| SEC-02 | Moderate | **Absolute home paths** | `configs/benchmark_instances_found_all.txt`, COAP CSV configs, launch metadata | `/home/soroush/...` |
| SEC-03 | Low | **Machine-specific benchmark path** | Multiple experiment configs | External clone path |
| SEC-04 | Low | **pip_freeze in logs** | `logs/coap_ipsns_sensitivity/pip_freeze.txt` | Environment snapshot; may list many packages |
| SEC-05 | None observed | API keys / tokens / SSH private keys | Repo-wide grep | No matches in source |
| SEC-06 | None observed | `.env` files | `.gitignore` excludes `.env` | Not tracked |
| SEC-07 | Low | **Large logs untracked** | `logs/coap_ipsns_holdout/` | No secrets observed |
| SEC-08 | Info | Git history `sk-` matches | Commit messages only | Benign |

## Anonymization state

| Asset | Anonymized? |
|---|---|
| `paper_coap/main.pdf` | **No** — author-visible (COAP policy) |
| `submission_files_for_download/main_anonymized.pdf` | Yes — historical |
| EJCO anonymous artifact | Designed anonymous |

## Repository hygiene

| Item | Status |
|---|---|
| Large binary blobs in Git | PDFs, PNGs, ZIPs — acceptable |
| `external_tools/` gitignored | Good — avoids vendoring .git hooks |
| Predecessor archives | Contain old manuscript author info — expected |

## Recommendations

1. Scrub absolute paths from **tracked** CSVs before public ESM (use env var or relative instructions)
2. Do not commit `pip_freeze` with unrelated ML packages to main logs (sensitivity log appears broad)
3. Run `gitleaks` or `trufflehog` before public release (not run in this pass)
4. Keep `.env` gitignored

## Accidentally committed secrets (history)

No evidence of API keys in tracked files. Full history scan not exhaustive; recommend pre-release secret scan.
