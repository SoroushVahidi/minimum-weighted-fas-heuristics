# Documentation and Audit Directory Audit

**Scope:** All `docs/*` directories  
**HEAD:** `6c04ff1`

## Inventory

| Directory | Date (suffix) | Files (approx.) | Purpose | Superseded? | Still useful? |
|---|---|---|---|---|---|
| `provenance/` | — | few | Predecessor manifest | No | Yes — lineage |
| `full_repository_audit_20260610/` | 2026-06-10 | large | Pre-COAP-finalization repo audit | Partially | Historical baseline |
| `final_branch_audit_20260611/` | 2026-06-11 | medium | Branch/canonical map pre-final push | Partially | EJCO stale warnings still valid |
| `coap_manuscript_reframing_20260611/` | 2026-06-11 | medium | COAP migration | Yes | Reference |
| `coap_online_resource_1_20260611/` | 2026-06-11 | medium | OR1 initial build | Yes | Superseded by finalization |
| `coap_online_resource_finalization_20260611/` | 2026-06-11 | 25+ | OR1 freeze + validation | **Authoritative for OR1** | Yes — checksums, gates |
| `coap_exp10_manuscript_integration_20260611/` | 2026-06-11 | medium | EXP10 integration | Yes | Traceability |
| `coap_topological_extraction_audit_20260611/` | 2026-06-11 | medium | EXP11 / topo extraction | Yes | Technical reference |
| `coap_test_and_ci_gate_20260611/` | 2026-06-11 | small | CI gate | Yes | Reference |
| `coap_rejection_history_and_revision_plan_20260611/` | 2026-06-11 | unknown | Editorial strategy | Internal | **Do not publish** — verify contents before public repo |
| `coap_cover_letter_and_upload_20260612/` | 2026-06-12 | 20+ | Portal package | **Authoritative for EM metadata** | Yes — update abstract note |
| `final_coap_adversarial_audit_20260612/` | 2026-06-12 | 26+ | Pre-submission adversarial audit | Current for submission | **Primary submission QA** |
| `full_branch_repository_audit_20260612/` | 2026-06-12 | this audit | Full repo reconciliation | **New canonical inventory** | Yes |

## Source-of-truth hierarchy

For conflicting claims, prefer in order:

1. **Git HEAD** canonical source (`src/`, `paper_coap/main.tex`, `experiments/*/summary/`)
2. `docs/final_coap_adversarial_audit_20260612/` — submission readiness
3. `docs/coap_online_resource_finalization_20260611/` — OR1 checksums
4. `docs/coap_cover_letter_and_upload_20260612/` — portal text (except abstract: use `main.tex`)
5. Older audits — historical only

## Issues

| Issue | Severity |
|---|---|
| No single `docs/README.md` index | Low |
| `EDITORIAL_MANAGER_COPY_READY_TEXT.md` stale abstract | Medium for portal paste |
| Multiple overlapping audit dirs | Low — expected for staged QA |
| `coap_rejection_history_*` may be sensitive | Medium — keep private |

## Recommendations (future)

1. Add `docs/INDEX.md` pointing to authoritative audits.
2. Update copy-ready text abstract to 238 words.
3. Do not delete old audits without archiving — they document decision trail.

## Verdict

Documentation corpus is **extensive and appropriate** for a submission-grade research repo. Not misleading if readers use the hierarchy above.
