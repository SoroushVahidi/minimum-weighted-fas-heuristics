# Full Repository Audit — Executive Summary

**Date:** 2026-06-10  
**Repository:** `SoroushVahidi/minimum-weighted-fas-heuristics`  
**Branch / HEAD:** `main` @ `80b3144` (matches `origin/main`)  
**Audit mode:** Read-only; no repository or experiment state changed.

## Bottom line

The repository contains a **coherent, manuscript-backed algorithm-engineering project** with canonical production code in `src/mwfas/`, a mature EXP1b–EXP9 experimental pipeline, and an **active COAP manuscript** in `paper_coap/`. Core sparse-benchmark claims are traceable to committed summaries. **COAP submission is not yet ready**: related-manuscript disclosure is deferred (and now confirmed as urgent — see §N-01 below), `ESM_1.zip` is missing, the EJCO reproducibility artifact/README is stale for COAP, automated tests and CI are absent, and the **stage-2 IPSNS holdout experiment is still running** (~42% complete at audit time).

**2026-06-11 novelty audit finding:** arXiv:2412.16181 (Vahidi & Koutis, Dec 2024) is an undisclosed author predecessor that is not currently cited in the COAP manuscript. This is a new blocker (N-01). Three additional disclosure blockers were identified (N-02, N-03) for the JOCO predecessor and Elsevier predecessor. Four algorithm-description corrections (N-04 through N-07) were also identified. See `NOVELTY_AND_PRIOR_WORK_AUDIT.md` for the full analysis and `MANUSCRIPT_POSITIONING_RECOMMENDATIONS.md` for recommended text.

## Repository state (facts)

| Item | Value |
|---|---|
| Working tree | Clean except untracked holdout outputs/logs |
| Size | ~253 MB workspace |
| Submodules / LFS | None |
| Largest tracked blobs | Anonymized PDFs, framework PNG, Springer template ZIP, COAP `main.pdf` |
| Tests | **No project test suite** (`tests/` absent; pytest collects 0 project tests) |
| CI | **No `.github/workflows`** |

## Active experiment

| Field | Value |
|---|---|
| Session | `coap_ipsns_holdout` (tmux) |
| Launch commit | `90af464` (clean; metadata in `logs/coap_ipsns_holdout/LAUNCH_METADATA.md`) |
| Expected runs | 1290 (1286 pending after 4 pilot skips) |
| Progress at audit | **540/1286** log lines; **544** checkpoints; **0** failures observed |
| Health | Process alive (PID 1488925); checkpoint growth continuing; ~594 GB disk free |
| Policy | **Do not change defaults or manuscript until holdout completes** (`paper_coap/notes/COAP_DEFAULT_SELECTION_DECISION.md`) |

## Canonical vs historical

| Canonical | Historical / duplicate |
|---|---|
| `src/mwfas/*.py` | `notebooks/*`, `archive/predecessor_projects/` |
| `paper_coap/` | `paper/` (CAIE/EJCO lineage), `submission_package/` (EJCO package) |
| `experiments/exp1b_*` | `experiments/exp1_core_benchmark/` (obsolete) |
| EXP1–9 summaries in Git | Raw `experiments/*/raw/` gitignored (local only) |

Core `src/mwfas/*.py` files are **byte-identical** to copies in `submission_package/ejco_reproducibility_artifact/src/mwfas/`.

## Completed vs missing

### Completed (manuscript-ready evidence)
- EXP1b core benchmark (105 instances, full WMSF seed)
- EXP2 ablation, EXP3 exact DP, EXP4 external baselines, EXP5 LOLIB
- EXP6 budget curve, EXP7 plain LS, EXP8 MIP, EXP9 application case
- COAP stage-1 parameter sensitivity (140/140 runs, conclusion **B** = screening only)
- Formal analysis section (`92e9c5a`) aligned with implementation (minor wording fixes needed)

### Running / incomplete
- **COAP stage-2 holdout** (~42% at audit)
- Related-manuscript overlap audit
- Demetrescu–Finocchi formal approximation transfer
- COAP submission package (`ESM_1.zip`, cover letter, reviewer list, related uploads)
- `sfas` identity unresolved — name has no paper/URL/code in repository (B-06)
- igraph `exact_ip` reclassified as exact validation (EXP3-scope), not heuristic comparison

### Broken / risky
- **No automated regression tests** for theorem-critical behavior
- **Absolute home paths** in tracked CSV configs (`/home/soroush/benchmark_sources/...`)
- Misleading prose: destroy fractions described as seed-reproducible (they are deterministic; only SCC selection is random)
- Multiple manuscript trees (`paper/`, `paper_coap/`, EJCO copies) — accidental use risk
- Raw experiment outputs not in Git — reproducibility depends on local disks or reruns

## Severity-ranked blockers for COAP submission

1. **arXiv:2412.16181 (Vahidi & Koutis) not cited or disclosed** (N-01) — new, confirmed blocker
2. **JOCO predecessor (Vahidi, LR-TA) not cited or disclosed** (N-02) — new, confirmed blocker
3. **Elsevier predecessor (Vahidi, IPSNS/WMSF) not cited or disclosed** (N-03) — new, confirmed blocker
4. **Related-manuscript disclosure not completed** (B-01) — original blocker now reinforced
5. **Springer supplementary `ESM_1.zip` not built** (B-02)
6. **Holdout experiment incomplete** (B-03) — parameter/default claims must not advance early
7. **No COAP-specific submission package** (B-05)
8. **No CI / test gate** (B-04) — reviewer confidence risk

**2026-06-11 baseline audit finding:** DRMacIver uses `srand(time|pid)` and is non-deterministic; one run per instance was recorded in EXP4; this is not disclosed in the manuscript (B-07, Moderate). The 21.6% DRMacIver gap claim is verified correct (mean per-instance relative excess over all 93 completed instances). All 25 empirical claims in EMPIRICAL_CLAIM_SAFETY_REGISTER.csv are either Safe or Safe-after-minor-qualification; no unsupported claims found in results section. See `BASELINE_EXECUTION_READINESS_AUDIT.md` for full baseline inventory and `EMPIRICAL_CLAIM_SAFETY_REGISTER.csv` for claim audit.

## Recommended immediate sequence

See `ROADMAP.md`. Phase 0: **predecessor disclosure (parallel with Phase 1)**. Phase 1: **finish holdout without disturbance**. Phase 2: post-process and decide defaults. Phase 3: related-manuscript disclosure + ESM build. Phase 5: resolve sfas identity + add DRMacIver/Eades disclosures in §5. Phase 4/9/10: final compliance/visual audit and upload package.

## Audit outputs

All deliverables live under `docs/full_repository_audit_20260610/`. Master tracking: `MASTER_ISSUE_REGISTER.csv`.
