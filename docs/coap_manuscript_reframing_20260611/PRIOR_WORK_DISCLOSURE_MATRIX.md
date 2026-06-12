# Prior Work Disclosure Matrix

**Audit date:** 2026-06-11

| Lineage item | Evidence in repo | Manuscript disclosure location | Cover letter | Status |
|--------------|------------------|-------------------------------|--------------|--------|
| **arXiv:2412.16181** (Vahidi & Koutis) | Public preprint; cited in predecessor bibs | §2.1 `\cite{VahidiKoutis2024arxiv}`; declarations; bib entry | Required paragraph | **Disclosed in manuscript** |
| **JOCO LR-TA predecessor** | Archived TeX in repo; code match noted | §2.1 narrative; `% AUTHOR-STATUS` comment | IDs/outcomes pending author | **Partial — no invented outcome** |
| **DAM IPSNS predecessor** | Archived TeX with `\journal{Discrete Applied Mathematics}` | §2.1 narrative; `% AUTHOR-STATUS` comment | IDs/outcomes pending author | **Partial — no invented outcome** |
| **CAIE package** | `submission_package/` folders | §2.1: preparation ≠ submission | Author confirmation required | **Neutral disclosure** |
| **EJCO package** | `submission_package/ejco_source/` | §2.1: preparation ≠ submission | Author confirmation required | **Neutral disclosure** |
| **Demetrescu–Finocchi 2003** | Verified bib `DF03` | LR-TA inheritance throughout §2, §4 | N/A | **Correct** |
| **Cavallaro–Cutello 2025 (SEKE)** | Verified bib `CC25`, DOI 10.18293/SEKE2025-049 | WMSF attribution §2, §4, §5, limitations | External provenance | **Correct** |
| **Cavallaro–Cutello–Pavone 2024 (JoCO)** | Springer record DOI 10.1007/s10878-024-01209-8 | Added `CCP24`; cited as WMSF lineage | Predecessor to CC25 | **Added in this pass** |
| **IPSNS (new in COAP)** | `src/mwfas/ipsns.py` + §4 | Primary contribution list, title, abstract | New integrated method | **Foregrounded** |

---

## Incremental COAP contribution (editor-visible summary)

Relative to arXiv VK and archived predecessors, the COAP manuscript adds:

1. IPSNS as primary integrated destroy-and-repair method with incumbent-protection analysis.
2. Unified dual-seed framework (LR-TA + WMSF-style seed + IPSNS).
3. Exact DP validation and time-capped HiGHS MIP validation.
4. Expanded sparse external baselines and LOLIB scope boundary.
5. Ablation, budget, plain local-search, holdout, application, and pending stochastic-robustness studies.
6. Supporting correctness properties and complexity (not headline theory).

---

## Explicit non-claims

- No statement that predecessors were rejected/withdrawn/transferred without documentary evidence.
- No claim that CAIE/EJCO packages were submitted merely because folders exist.
- No claim that all algorithms are new or that the submission is entirely independent of prior work.
