#!/usr/bin/env bash
# Level D: documentation only — does NOT launch full reruns
cat <<'EOF'
=== Optional full experimental rerun (NOT executed automatically) ===

Prerequisites:
  - Clone graph-benchmarks: https://github.com/alidasdan/graph-benchmarks
  - Build DRMacIver/FAS: https://github.com/DRMacIver/Feedback-Arc-Set
  - pip install -r requirements.txt && pip install scipy matplotlib highspy python-igraph

Documented commands (run from full repository checkout, not OR1 artifact alone):

  # EXP1b core benchmark
  python3 scripts/run_ipsns.py --manifest <sparse_manifest>

  # EXP4 external baselines
  python3 experiments/exp4_external_baselines/run_exp4_benchmark.py

  # EXP10 (1860+1860 runs; ~hours)
  python3 experiments/exp10_stochastic_robustness/scripts/run_ipsns_repetitions.py
  python3 experiments/exp10_stochastic_robustness/scripts/run_drmaciver_repetitions.py
  python3 experiments/exp10_stochastic_robustness/scripts/wait_and_finalize_exp10.py --skip-wait

Estimated EXP10 production burden from logs: IPSNS ~298 s for 1860 runs;
DRMacIver phase several hours depending on instance mix.

OR1 includes committed summaries so full reruns are optional for manuscript verification.
EOF
