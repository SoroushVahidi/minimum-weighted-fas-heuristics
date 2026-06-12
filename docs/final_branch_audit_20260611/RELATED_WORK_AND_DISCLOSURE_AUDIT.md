# Related Work and Disclosure Audit
**Date:** 2026-06-11

---

## 1. Prior Predecessor Work Disclosure

The repository has been flagged in prior audits (docs/full_repository_audit_20260610/) for three predecessor disclosure concerns (N-01, N-02, N-03). Status as of this audit:

| Issue | Description | Status in Current Manuscript |
|-------|-------------|------------------------------|
| N-01 | LR-TA substantially overlaps prior author work on local-ratio FAS | The introduction explicitly states: "We do not claim local-ratio as new." DF03 cited as "closest methodological antecedent." **ADEQUATELY DISCLOSED.** |
| N-02 | WMSF derived from CC25 (Cavallaro-Cutello 2025) | §2 and §5 explicitly cite CC25 as "not rerun for this study" and the weighted seed as CC25-derived. **ADEQUATELY DISCLOSED.** |
| N-03 | Overlap with arXiv:2412.16181 | Not independently inspected in this audit; prior audit documents noted this concern. The manuscript makes no reference to a prior arXiv version in the main text or declarations. **Requires author confirmation that this is the first submission of this work.** |

## 2. Required Citation Coverage

| Work | Required? | In manuscript? | Accurate? |
|------|----------|---------------|---------|
| Demetrescu-Finocchi (DF03) | Yes — local-ratio FAS antecedent | ✓ Yes — §2 "closest methodological antecedent" | ✓ |
| Bar-Yehuda et al. BYGR98 | Yes — local-ratio foundations | ✓ Yes — §2 | ✓ |
| Cavallaro-Cutello 2025 (CC25) | Yes — WMSF derived from this lineage | ✓ Yes — §2, §5 | ✓ |
| Cavallaro-Cutello-Pavone 2024 | Yes — predecessor work | Not separately verified; CC25 cited | Check |
| Baharev et al. BSNA21 | Yes — exact treatment | ✓ Yes — §2, §5 | ✓ |
| Simpson-Srinivasan-Thomo SST16 | Yes — web-scale context | ✓ Yes — §2 | ✓ |
| DRMacIver/FAS tool | Yes — primary external baseline | ✓ Yes — §2, §5 | ✓ |
| python-igraph | Yes — library baseline | ✓ Yes — §2, §5 | ✓ |
| Eades-Lin-Smyth ELS93 | Yes — classical baseline | ✓ Yes — §2 | ✓ |
| LOLIB (MRD12, lolib_library) | Yes — dense benchmark | ✓ Yes — §2, §5 | ✓ |
| GNNRank22 | Yes — learning-based context | ✓ Yes — §2 (excluded with rationale) | ✓ |
| FLRS10 (tournament LS) | Yes — dense ordering context | ✓ Yes — §2, §7 | ✓ |
| LOP_MA-EDM | Yes — LOP-native solver disclosure | ✓ Yes — §7 explicitly notes it was not rerun | ✓ |
| Karp 1972 (NP-hardness) | Yes | ✓ Yes | ✓ |
| ACN08 (rank aggregation) | Yes | ✓ Yes | ✓ |

## 3. Attribution Accuracy

| Attribution | Claim in manuscript | Accuracy |
|------------|--------------------|---------
| LR-TA | "the local-ratio principle used in LR-TA is prior art" | ✓ CORRECT |
| WMSF | "Cavallaro-Cutello-derived engineered seed" | ✓ CORRECT |
| Weighted Eades adaptation | "local adaptation rather than the original authors' algorithm" | ✓ CORRECT |
| DRMacIver documentation claim | "deterministic and reports a local-optimality property" | Accurately describes documentation; actual `srand(time|pid)` behavior noted in audit |
| igraph Eades | "Eades-style heuristic...represents what a practitioner could call from a general-purpose graph library" | ✓ CORRECT |

## 4. Reused Code and Datasets

| Item | Attribution in manuscript | Adequate? |
|------|--------------------------|----------|
| graph-benchmarks repository instances | Cited as `\cite{graph_benchmarks_repo}` | ✓ Yes |
| LOLIB 2010 instances | Cited as `\cite{MRD12, lolib_library}` | ✓ Yes |
| DRMacIver binary (commit 16ff24a) | Cited with repo URL | ✓ Yes |
| python-igraph | Cited | ✓ Yes |
| HiGHS solver | Used in EXP8; should be cited | Check §5/§8 for HiGHS citation |
| WikiVote SNAP dataset | Cited as `\cite{LHK10WikiVote}` | ✓ Yes |

## 5. Contribution Differences from CC25

The manuscript explicitly states CC25 was not rerun and positions WMSF as a CC25-derived adaptation used as a seed. The claimed novelty is IPSNS. This is appropriate for an algorithm-engineering paper. The relationship between this work and CC25 is adequately described.

## 6. Salami-Slicing Concern (N-03)

The prior audit flagged potential overlap with arXiv:2412.16181. The current manuscript (COAP version) makes no reference to a prior arXiv version. If this work has been previously submitted elsewhere (CAIE, EJCO based on commit history), the COAP cover letter must disclose this. The submission history found in git commits:
- CAIE submissions (commits d496b8a, fd3c8f7)
- EJCO submissions (commits 9bc756c, 5c61925, 5e1fcc1, 581ee35)

**Action required:** The COAP submission must include disclosure of prior journal submissions (CAIE, EJCO) in the cover letter or related-work section per journal policy. This is a **Critical** issue if not addressed.

## 7. AI Disclosure

The declarations section states: "the author used AI-assisted tools, including ChatGPT, Codex, Claude, and Perplexity AI, to support literature exploration, organization of material, language editing, and coding assistance. The author reviewed and edited all outputs..."

This is appropriate and complete for COAP, which requires AI disclosure as part of Springer Nature policy.

## 8. Summary

Related work disclosure is comprehensive and accurate. The principal concerns are:
1. N-03 (arXiv/prior submission overlap) — requires author confirmation and cover letter disclosure
2. DRMacIver single-run limitation — should be added as one sentence in §5
3. HiGHS citation check — should verify HiGHS is cited in EXP8 description
