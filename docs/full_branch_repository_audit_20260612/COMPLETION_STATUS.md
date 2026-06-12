# Repository Completion Status

**HEAD:** `6c04ff1cc19d1887bd5b1b2bd1d1f31dc2b6924a`  
**Audit date:** 2026-06-12

## Completed (evidence-based)

| Area | Status | Evidence |
|---|---|---|
| COAP manuscript | **Complete** | 45-page PDF; submission upload refreshed at 6c04ff1 |
| Online Resource 1 | **Complete** | 12-page PDF; ZIP validated; checksums frozen |
| Submission package (6 files) | **Complete** | `final_upload/` checksums documented |
| Algorithms (LR-TA, WMSF, IPSNS) | **Complete** | `src/mwfas/` + tests |
| EXP1b–EXP9 experiments | **Complete** | Committed summaries |
| EXP10 stochastic robustness | **Complete** | 1860/1860; summaries; COMPLETED.ok |
| EXP11 extraction calibration | **Complete** | `exp11_aggregate.json` |
| COAP IPSNS sensitivity (OAT) | **Complete** | 140 runs summarized |
| Formal analysis section | **Complete** | Propositions + OR1 proofs |
| pytest / CI | **Complete** | 90/1 local; CI green on 6c04ff1 |
| Cover letter + related manuscripts | **Complete** | PDFs in final_upload |
| Adversarial pre-submission audit | **Complete** | `docs/final_coap_adversarial_audit_20260612/` |
| Git push + remote sync | **Complete** | local = origin = 6c04ff1 |

## Incomplete or partial

| Item | Status | Notes |
|---|---|---|
| COAP IPSNS holdout summary | **Partial** | Checkpoints; no `summary/` |
| `experiments/combined/` digest | **Stale** | EXP1b–5 only |
| Public GitHub | **Private** | By author choice |
| CAIE/EJCO submission confirmation | **Author pending** | COMMENT in related work |
| Portal submission itself | **Author pending** | Files ready |
| Zenodo/DOI release | **Not done** | Not claimed |

## Planned but not done (or deferred)

| Plan | State |
|---|---|
| ESM_1 rename at portal | Optional per editor |
| Full EXP10 raw in OR1 | Explicitly omitted by policy |
| Second exact solver baseline | Scoped out of manuscript claims |
| Additional external baselines (GNNRank, etc.) | Documented exclusions |
| Page reduction below 45 | Deferred — soft risk only |

## Never planned / out of scope

- New approximation-ratio theorem
- Negative-weight MWFAS extension (future work only)
- Confidential reviewer letters in public repo

## Overall completion estimate

| Layer | % complete (qualitative) |
|---|---|
| Science + experiments for paper | **~98%** (holdout summary optional) |
| Manuscript + OR1 | **100%** |
| Submission artifacts | **100%** |
| Repository polish | **~85%** (stale dirs, metadata nits) |
| Post-submission public release | **~0%** (intentionally deferred) |

## Verdict

Repository is **submission-complete** with minor maintainability gaps that do not block COAP upload.
