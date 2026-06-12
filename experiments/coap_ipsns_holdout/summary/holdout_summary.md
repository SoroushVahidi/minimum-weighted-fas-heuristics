# COAP IPSNS Holdout Study

- Status: **COMPLETE** (1290/1290 runs in `results/runs.jsonl`)
- Incumbent violations vs best seed: **0**
- Tuning instances: 18; Holdout instances: 25
- Configs: iters_10, iters_400, iters_50, iters_50_addback25, iters_50_topk5, seed_only

See `paper_coap/notes/COAP_DEFAULT_SELECTION_DECISION.md` for selection rules.
Manuscript uses holdout-supported **engineering defaults** (400 iterations, topK=15), not universal optimality.
