# EXP4 vs EXP10 Comparison

## Single-run EXP4 (manuscript Table paired sparse tests)

| Outcome | Count |
|---------|-------|
| IPSNS wins | 37 |
| Ties | 55 |
| DRMacIver wins | 1 (`r20_60`) |
| Mean relative excess | 21.61% |

## EXP10 median repeated-run (93 instances)

| Outcome | Count |
|---------|-------|
| IPSNS wins | 38 |
| Ties | 55 |
| DRMacIver wins | 0 |
| Mean relative excess | 21.60% |

## Interpretation

| Question | Answer |
|----------|--------|
| Does EXP10 confirm EXP4? | **Yes** — same directional advantage and ~21.6% mean excess |
| Does EXP10 strengthen? | **Yes** — median comparison removes the sole DR win |
| Does EXP10 weaken? | **No** |
| Does EXP10 contradict? | **No** |
| Was EXP4 representative? | **Mostly yes**; `r20_60` was an outlier favorable to DR under single run |
| Was one IPSNS seed adequate? | **Yes** — seed 0 matched best on all 93 instances |
| Was one DRMacIver run adequate? | **Often yes** (53/93 zero variance), but 40/93 show multi-value spread |

## `r20_60` detail

| Protocol | IPSNS BW | DR BW | Winner |
|----------|----------|-------|--------|
| EXP4 single run | 1688 | 1685 | DR |
| EXP10 median (20 reps) | 1688 | 1698 | IPSNS |
