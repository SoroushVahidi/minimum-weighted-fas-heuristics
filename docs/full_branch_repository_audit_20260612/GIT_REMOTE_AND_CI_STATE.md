# Git, Remote, and CI State

**Audit date:** 2026-06-12  
**Repository path:** `/home/soroush/minimum-weighted-fas-heuristics`  
**Remote:** `https://github.com/SoroushVahidi/minimum-weighted-fas-heuristics`

## Summary

| Item | Value |
|---|---|
| Branch | `main` |
| Local HEAD | `6c04ff1cc19d1887bd5b1b2bd1d1f31dc2b6924a` |
| `origin/main` | `6c04ff1cc19d1887bd5b1b2bd1d1f31dc2b6924a` |
| Local/remote match | **Yes** |
| Working tree | **Clean** |
| Staged changes | None |
| Untracked files | `docs/full_branch_repository_audit_20260612/` (this audit; not committed per task scope) |

> **Note:** User query cited expected SHA `6c04ff1...692a`; actual full SHA ends in `6924a`.

## Remotes and upstream

| Remote | URL | Upstream |
|---|---|---|
| `origin` | `https://github.com/SoroushVahidi/minimum-weighted-fas-heuristics.git` | `main` tracks `origin/main` |

## Recent commit history (20)

```
6c04ff1 paper: address final COAP submission audit
f306c15 Finalize COAP manuscript, Online Resource 1, and submission package.
80b3144 Add sensitivity instance list omitted by csv gitignore
90af464 Add completed COAP IPSNS sensitivity experiment
92e9c5a Add formal correctness and complexity analysis for COAP
76a3412 Polish COAP template and manuscript layout
7e8e0b7 Create Springer COAP manuscript version
581ee35 Track final EJCO submission package
5e1fcc1 Finalize EJCO submission package
623f044 Prepare EJCO source and reproducibility packages
5c61925 Prepare EJCO title page and declarations
9bc756c Prepare EJCO cover letter and highlights
75fbc14 Replace AI-generated flowchart with TikZ figure
35bac85 Retarget manuscript framing for EJCO
b66cace Refresh anonymous reproducibility artifact
fd3c8f7 Add PDF highlights file
6934679 Replace Figure 1 with clean flowchart image
74fb082 Lightly polish manuscript tone
1baaddb Add files via upload
bc310a1 Refine Figure 1 restore-path routing
```

## Tags, releases, LFS, submodules

| Item | Status |
|---|---|
| Tags | None |
| GitHub releases | None observed |
| Git LFS | Initialized; no pending objects |
| Submodules | None |
| Nested Git repos | None detected in worktree |
| Worktrees | Single: `/home/soroush/minimum-weighted-fas-heuristics` |
| Merge/rebase/cherry-pick | None in progress |

## Git hooks

Only default **sample** hooks present (`.git/hooks/*.sample`). No active custom pre-commit or pre-push hooks affecting reproducibility.

## Ignored publication-relevant paths (`.gitignore`)

| Pattern | Effect |
|---|---|
| `experiments/*/raw/` | EXP10 and others: raw JSON not tracked |
| `experiments/*/checkpoints/` | Local checkpoint dirs ignored (EXP10 checkpoints exist locally) |
| `experiments/*/external_tools/` | DRMacIver clone not tracked |
| `experiments/*/logs/` | Run logs ignored |
| `*.csv` (with exceptions) | Most CSV ignored; experiment summaries whitelisted |
| `logs/`, `*.log` | Build/test logs ignored (audit log exceptions added for prior audit) |
| LaTeX aux files | `*.aux`, `*.bbl`, etc. |
| `submission_package/files_for_upload/*.pdf` | Some EJCO upload copies ignored |

## GitHub Actions (latest on `main`)

| Run ID | Workflow | Commit | Status | Duration |
|---|---|---|---|---|
| **27393186733** | Tests | `6c04ff1` | **success** | ~29 s |
| 27392697566 | Dependency Graph (pip) | `f306c15` | success | ~65 s |
| 27392696517 | Tests | `f306c15` | success | ~31 s |

**Tests workflow (27393186733):**

- Jobs: `test (3.11)`, `test (3.12)` — both success
- URL: https://github.com/SoroushVahidi/minimum-weighted-fas-heuristics/actions/runs/27393186733
- Expected outcome: 90 passed, 1 skipped (matches local)

## Local pytest (this audit)

```
PYTHONPATH=src python3 -m pytest --ignore=experiments/exp4_external_baselines/external_tools -q
→ 90 passed, 1 skipped, 2 warnings (~1.7 s)
```

Skipped: `tests/regression/test_exp10_namespace.py` (DRMacIver runner not active).
