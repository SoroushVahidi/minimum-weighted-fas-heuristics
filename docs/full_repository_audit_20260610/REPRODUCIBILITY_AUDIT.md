# Reproducibility Artifact Audit

**Audit date:** 2026-06-10

## Current artifacts

| Artifact | Path | Venue | Status |
|---|---|---|---|
| EJCO reproducibility tree | `submission_package/ejco_reproducibility_artifact/` | EJCO | Committed; **stale branding** |
| EJCO reproducibility ZIP | `submission_package/ejco_reproducibility_artifact.zip` | EJCO | Committed |
| EJCO source ZIP | `submission_package/ejco_source.zip` | EJCO | Committed |
| Anonymous artifact staging | `submission_package/anonymous_artifact/` | Review | Partial; gitignored zips |
| COAP ESM_1.zip | — | COAP | **Not built** |

## Match to active COAP manuscript

| Field | EJCO artifact | COAP manuscript | Match? |
|---|---|---|---|
| Title | Same title string | Same | Yes |
| Journal metadata | EJCO | COAP | **No** |
| Formal analysis section | Absent in ejco_source | Present in `paper_coap/` | **No** |
| Core code (`src/mwfas/`) | SHA match to live | Live HEAD | **Yes** (7 modules) |
| EXP6–9 summaries | README claims included | Manuscript cites | Likely yes in tree |
| COAP sensitivity/holdout | **Absent** | Notes only | **No** |
| Parameter study results | N/A | Stage-1 in Git; holdout untracked | Partial |
| Environment pins | `requirements.txt` only (5 packages) | Underspecified | **Weak** |
| Dataset paths | External + converted LOLIB | Same | Partial |
| Absolute path leaks | Possible in configs | Tracked CSVs have `/home/soroush/...` | **Risk** |
| Anonymization | EJCO anonymous artifact | COAP author-visible | Different policies |

## README issues (`ejco_reproducibility_artifact/README.md`)

- States "EJCO manuscript" — must rebrand for COAP ESM
- Says "public repository after acceptance" — update for COAP data availability
- `REPRODUCE.md` may not cover COAP experiments

## What must change for `ESM_1.zip`

1. Rebrand metadata (COAP, Online Resource 1, citation text in manuscript)
2. Include `paper_coap`-aligned experiment summaries (EXP1–9)
3. Add COAP sensitivity canonical CSV (`coap_ipsns_sensitivity/summary/`)
4. Add holdout results **after completion**
5. Pin Python + key dependency versions (numpy, pandas, networkx, scipy for MIP)
6. Replace absolute paths with relative instructions or bundled instance lists
7. Include licenses for LOLIB/SNAP converted data
8. Remove EJCO/CAIE wording and author-anonymization artifacts
9. Document external baseline clone steps (DRMacIver, igraph version)
10. Provide checksum manifest for committed summary CSVs

## Reproduction scope (realistic)

| Scope | Feasible? |
|---|---|
| Inspect committed summaries → manuscript tables | **Yes** |
| Rerun single instance via CLI | **Yes** (needs external graphs) |
| Full EXP1b + EXP4 rerun | **Yes** (hours; external tools) |
| Full holdout rerun | **Yes** (after design frozen) |
| Bit-exact reproduction across machines | **Unlikely** (float order, no lock file) |

## Identity / privacy

EJCO anonymous artifact excludes author info by design. COAP ESM may be author-visible — confirm portal policy before reusing anonymous packaging.
