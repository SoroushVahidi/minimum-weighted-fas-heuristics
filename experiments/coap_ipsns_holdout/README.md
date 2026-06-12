# COAP IPSNS Holdout Study (Stage 2)

**Status:** COMPLETE (1290/1290 runs in `results/runs.jsonl`)

**Purpose:** Confirm IPSNS parameter defaults on disjoint tuning (18 instances) and holdout (25 instances) splits after stage-1 OAT screening (`experiments/coap_ipsns_sensitivity/`).

**Canonical summaries:**

- `summary/holdout_aggregate.json`
- `summary/holdout_summary.md`
- `logs/coap_ipsns_holdout/COMPLETED.ok` (repo root)

**Design:** `config/holdout_plan.yaml`, `paper_coap/notes/COAP_DEFAULT_SELECTION_DECISION.md`

**Manuscript use:** Holdout-supported engineering defaults (not universal optimality). Raw paths in `runs.jsonl` reference local benchmark install paths.
