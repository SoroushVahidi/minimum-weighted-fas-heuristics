# Running Process Audit
**Date:** 2026-06-11  
**Audit method:** Passive inspection only — no process signals, no tmux interaction

---

## 1. Active Processes (at audit time)

### EXP10 IPSNS Runner

| Field | Value |
|-------|-------|
| PID | 24482 |
| Process | `python3 experiments/exp10_stochastic_robustness/scripts/run_ipsns_repetitions.py` |
| Parent | PID 24477 (bash shell) |
| CPU use | ~100% (one core) |
| RAM | ~117 MB (reasonable for graph algorithm) |
| Start time | 2026-06-11 13:59 (UTC) |
| Working directory | `/home/soroush/minimum-weighted-fas-heuristics` |
| Log | `experiments/exp10_stochastic_robustness/logs/ipsns_full_run.log` |
| Progress at audit time | **1215/1860 IPSNS runs complete (65.3%)** |
| Current instance | `parker1986` (n=2795) |
| Checkpoint files | 1215 sentinel files in `experiments/exp10_stochastic_robustness/checkpoints/ipsns_*.done` |

**Note:** This process was launched by Claude Code as part of EXP10 execution. It is writing to the log file and creating checkpoint files. **No interaction was performed during this audit.**

### Other Relevant Processes

| PID | Process | Role |
|-----|---------|------|
| 1544 | unattended-upgrade-shutdown | System update daemon — does not compete for experiment CPU |
| 3904 | ubuntu-release-upgrader | Background system check — negligible CPU |

**No competing experiments observed.**

## 2. Holdout Experiment Status

**Status: COMPLETED**

Evidence:
- `logs/coap_ipsns_holdout/COMPLETED.ok` exists
- `logs/coap_ipsns_holdout/summary.json`: `"completed_runs": 1290, "expected_runs": 1290`
- No holdout process visible in `ps aux`

The holdout (COAP IPSNS sensitivity study, 1290 runs) completed before the current session and is no longer active.

## 3. Sensitivity Experiment Status

**Status: COMPLETED**

Evidence:
- `experiments/coap_ipsns_sensitivity/results/runs.jsonl` exists
- No active process for this experiment

## 4. EXP10 Current State Details

### IPSNS phase (active)

Progress at audit time:
- Instances completed: All of `bad`, `bad1-7`, `bigkey`, `complete2-9`, `daio_receiver`, `dene`, `dsip`, `ecc`, `example*`, `good`, `gr*`, `green*`, `grid`, `gr-paper`, `howard-min`, `mm30a`, `mm4a`, `mm9a`, `mm9b`, `mult16a`, `mult16b`, `mult32a`, partial `parker1986`
- Currently processing: `parker1986` (n=2795, ~6s per seed × 20 seeds ≈ 120s remaining for this instance)
- Remaining after parker1986: `phase_decoder`, `present`, `r1000`, `r20_60` (done-smoke), `rd_*`, `s*`, `sample`, `sbc`, `small`, `stg` (done-smoke), `trace` 

### DRMacIver phase (not yet started)

Will start after IPSNS completes. DRMacIver phase estimated ~1860 runs × ~2s = ~62 minutes, serialized.

### Postprocessing (not yet started)

`experiments/exp10_stochastic_robustness/scripts/postprocess.py` will run after both phases complete.

## 5. Resource Isolation

| Resource | Holdout | EXP10 IPSNS | Competition? |
|----------|---------|-------------|-------------|
| CPU | COMPLETED | Active (1 core) | No holdout; clean |
| RAM | COMPLETED | ~117 MB | No competition |
| I/O | COMPLETED | Sequential reads/writes | Clean |
| Disk | — | ~1215 JSON files × ~2KB = ~2.4 MB so far | No issue (601 GB free reported earlier) |

**EXP10 is isolated. No concurrent experiment interference.**

## 6. Process Integrity

The EXP10 runner was launched with background flag and redirected output to the log file. The checkpoint system ensures:
- If the process is killed (e.g., by timeout), all completed runs are preserved
- On restart, only incomplete runs are re-executed
- No data loss occurs from interruption

## 7. Runtime Measurement Validity

Since EXP10 is running as a single process on a machine with no competing experiment, runtime measurements are scientifically usable. The machine is described in the manuscript (Intel Core i7-12700K, 62 GiB RAM, Ubuntu 24.04, Python 3.12). The EXP10 runner records per-run runtime in each JSON record — independent of any timeout-based interaction.

## 8. Summary

| Experiment | Status | Active? | Usable results? |
|------------|--------|---------|-----------------|
| EXP1b core benchmark | COMPLETE | No | Yes |
| EXP2 ablation | COMPLETE | No | Yes |
| EXP3 exact validation | COMPLETE | No | Yes |
| EXP4 external baselines | COMPLETE | No | Yes |
| EXP5 LOLIB dense | COMPLETE | No | Yes |
| EXP6 budget curve | COMPLETE | No | Yes |
| EXP7 plain local search | COMPLETE | No | Yes |
| EXP8 MIP baseline | COMPLETE | No | Yes |
| EXP9 application case | COMPLETE | No | Yes |
| COAP holdout | COMPLETE | No | Yes |
| COAP sensitivity | COMPLETE | No | Yes |
| EXP10 stochastic robustness | IN PROGRESS | Yes (PID 24482) | Partial (IPSNS only, 65%) |
