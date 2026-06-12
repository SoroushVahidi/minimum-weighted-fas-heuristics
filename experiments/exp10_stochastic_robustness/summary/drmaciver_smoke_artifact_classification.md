# DRMacIver Smoke Artifact Classification

**Date:** 2026-06-11T22:47:15Z

## Summary

- Artifacts examined: 9 raw JSON + 9 checkpoints
- All classified as smoke with **high** confidence: True

## Classification criteria

Each artifact matches the documented `--smoke` schedule:
- Instances: `stg`, `r20_60`, `s27` (diagnostic smoke trio)
- Run indices: 0, 1, 2 only (`n_reps=3` in smoke mode)
- Timestamps: 2026-06-11T17:59Z batch
- Git commit: 80b3144d5fdbbe250faed8a4fe671dde2da76c89
- Preflight `check_smoke_records()` explicitly lists these nine keys

## Per-artifact detail

### r20_60 run 0

- **Status:** ok
- **Confidence:** high
- **Evidence:** instance in documented smoke trio (stg,r20_60,s27); run_index 0..2 matches --smoke n_reps=3; matches run_drmaciver_repetitions.py --smoke schedule exactly; timestamp matches documented smoke-test window (2026-06-11T17:59Z); git_commit matches frozen EXP10 HEAD
- **SHA-256:** `a486b8e4cb2095473bae64d0c2417d4b439feee47181ccc0e957cb942dd91641`
- **Instance SHA-256:** `89214060ba2844884e5fd4d23b406387765ad803b20d0585f5f7c86a0ff89c65`
- **Original path:** `experiments/exp10_stochastic_robustness/raw/drmaciver/drmaciver_r20_60_run00.json`
- **Checkpoint:** `experiments/exp10_stochastic_robustness/checkpoints/drmaciver_r20_60_run00.done`

### r20_60 run 1

- **Status:** ok
- **Confidence:** high
- **Evidence:** instance in documented smoke trio (stg,r20_60,s27); run_index 0..2 matches --smoke n_reps=3; matches run_drmaciver_repetitions.py --smoke schedule exactly; timestamp matches documented smoke-test window (2026-06-11T17:59Z); git_commit matches frozen EXP10 HEAD
- **SHA-256:** `1277285f11c1473c6ef59e44310b851560ed8bd86f0cf79e1d21fc137ef4769a`
- **Instance SHA-256:** `89214060ba2844884e5fd4d23b406387765ad803b20d0585f5f7c86a0ff89c65`
- **Original path:** `experiments/exp10_stochastic_robustness/raw/drmaciver/drmaciver_r20_60_run01.json`
- **Checkpoint:** `experiments/exp10_stochastic_robustness/checkpoints/drmaciver_r20_60_run01.done`

### r20_60 run 2

- **Status:** ok
- **Confidence:** high
- **Evidence:** instance in documented smoke trio (stg,r20_60,s27); run_index 0..2 matches --smoke n_reps=3; matches run_drmaciver_repetitions.py --smoke schedule exactly; timestamp matches documented smoke-test window (2026-06-11T17:59Z); git_commit matches frozen EXP10 HEAD
- **SHA-256:** `1f6083135e1017f9fb7bdef755062f1fa6908b78fc5a259a550e1704d421916d`
- **Instance SHA-256:** `89214060ba2844884e5fd4d23b406387765ad803b20d0585f5f7c86a0ff89c65`
- **Original path:** `experiments/exp10_stochastic_robustness/raw/drmaciver/drmaciver_r20_60_run02.json`
- **Checkpoint:** `experiments/exp10_stochastic_robustness/checkpoints/drmaciver_r20_60_run02.done`

### s27 run 0

- **Status:** ok
- **Confidence:** high
- **Evidence:** instance in documented smoke trio (stg,r20_60,s27); run_index 0..2 matches --smoke n_reps=3; matches run_drmaciver_repetitions.py --smoke schedule exactly; timestamp matches documented smoke-test window (2026-06-11T17:59Z); git_commit matches frozen EXP10 HEAD
- **SHA-256:** `00cbe9dd654f51587b448316eb1baf381b310a9e1a00fe7bb7d5915a6c7d353b`
- **Instance SHA-256:** `6e13dd58a5a1c6b39b90f5ea7fc97045ec462fd6e17be1d17ce4dccb8419b953`
- **Original path:** `experiments/exp10_stochastic_robustness/raw/drmaciver/drmaciver_s27_run00.json`
- **Checkpoint:** `experiments/exp10_stochastic_robustness/checkpoints/drmaciver_s27_run00.done`

### s27 run 1

- **Status:** ok
- **Confidence:** high
- **Evidence:** instance in documented smoke trio (stg,r20_60,s27); run_index 0..2 matches --smoke n_reps=3; matches run_drmaciver_repetitions.py --smoke schedule exactly; timestamp matches documented smoke-test window (2026-06-11T17:59Z); git_commit matches frozen EXP10 HEAD
- **SHA-256:** `4a2473ac01548bddf129f30228ee02912fa9fae9c05cb059998e01f4d5392161`
- **Instance SHA-256:** `6e13dd58a5a1c6b39b90f5ea7fc97045ec462fd6e17be1d17ce4dccb8419b953`
- **Original path:** `experiments/exp10_stochastic_robustness/raw/drmaciver/drmaciver_s27_run01.json`
- **Checkpoint:** `experiments/exp10_stochastic_robustness/checkpoints/drmaciver_s27_run01.done`

### s27 run 2

- **Status:** ok
- **Confidence:** high
- **Evidence:** instance in documented smoke trio (stg,r20_60,s27); run_index 0..2 matches --smoke n_reps=3; matches run_drmaciver_repetitions.py --smoke schedule exactly; timestamp matches documented smoke-test window (2026-06-11T17:59Z); git_commit matches frozen EXP10 HEAD
- **SHA-256:** `26f2a4f07457110213c95c6eb6a9f7fe302594d6f4ad7ab807f542292a4bcda3`
- **Instance SHA-256:** `6e13dd58a5a1c6b39b90f5ea7fc97045ec462fd6e17be1d17ce4dccb8419b953`
- **Original path:** `experiments/exp10_stochastic_robustness/raw/drmaciver/drmaciver_s27_run02.json`
- **Checkpoint:** `experiments/exp10_stochastic_robustness/checkpoints/drmaciver_s27_run02.done`

### stg run 0

- **Status:** ok
- **Confidence:** high
- **Evidence:** instance in documented smoke trio (stg,r20_60,s27); run_index 0..2 matches --smoke n_reps=3; matches run_drmaciver_repetitions.py --smoke schedule exactly; timestamp matches documented smoke-test window (2026-06-11T17:59Z); git_commit matches frozen EXP10 HEAD
- **SHA-256:** `c1710078f522a1a0b8d237655a5bdcb7309658d41b665196abe9bfd1113812ae`
- **Instance SHA-256:** `03f7f9ab6d2b8c03d6430f900e3d3a2da27c7123bd2d1b6bc4bba97d7dca53dc`
- **Original path:** `experiments/exp10_stochastic_robustness/raw/drmaciver/drmaciver_stg_run00.json`
- **Checkpoint:** `experiments/exp10_stochastic_robustness/checkpoints/drmaciver_stg_run00.done`

### stg run 1

- **Status:** ok
- **Confidence:** high
- **Evidence:** instance in documented smoke trio (stg,r20_60,s27); run_index 0..2 matches --smoke n_reps=3; matches run_drmaciver_repetitions.py --smoke schedule exactly; timestamp matches documented smoke-test window (2026-06-11T17:59Z); git_commit matches frozen EXP10 HEAD
- **SHA-256:** `0ca287d1951b81a7c245a8a671a1afcb6421f80c4bf47f6309b9c7451713128b`
- **Instance SHA-256:** `03f7f9ab6d2b8c03d6430f900e3d3a2da27c7123bd2d1b6bc4bba97d7dca53dc`
- **Original path:** `experiments/exp10_stochastic_robustness/raw/drmaciver/drmaciver_stg_run01.json`
- **Checkpoint:** `experiments/exp10_stochastic_robustness/checkpoints/drmaciver_stg_run01.done`

### stg run 2

- **Status:** ok
- **Confidence:** high
- **Evidence:** instance in documented smoke trio (stg,r20_60,s27); run_index 0..2 matches --smoke n_reps=3; matches run_drmaciver_repetitions.py --smoke schedule exactly; timestamp matches documented smoke-test window (2026-06-11T17:59Z); git_commit matches frozen EXP10 HEAD
- **SHA-256:** `8e80bd0401a2884f24dcb0a23cf93a11d98100c7936fc947ce0ea7f801f5024e`
- **Instance SHA-256:** `03f7f9ab6d2b8c03d6430f900e3d3a2da27c7123bd2d1b6bc4bba97d7dca53dc`
- **Original path:** `experiments/exp10_stochastic_robustness/raw/drmaciver/drmaciver_stg_run02.json`
- **Checkpoint:** `experiments/exp10_stochastic_robustness/checkpoints/drmaciver_stg_run02.done`
