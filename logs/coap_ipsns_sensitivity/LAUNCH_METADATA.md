# COAP IPSNS Sensitivity — Launch Metadata

## Launch

| Field | Value |
|---|---|
| Launch timestamp (UTC) | 2026-06-10T19:00:59+local (session created Wed Jun 10 19:00:59 2026) |
| Hostname | see `hostname.txt` |
| Git commit | see `git_head.txt` |
| Working tree | see `git_status.txt` |
| Python | see `python_version.txt` |
| Environment | see `pip_freeze.txt` |
| CPU / memory | see `system_info.txt` |

## tmux session

| Field | Value |
|---|---|
| Session name | `coap_ipsns_sensitivity` |
| Attach | `tmux attach -t coap_ipsns_sensitivity` |
| Detach | `Ctrl-b d` (do not kill session) |
| List sessions | `tmux ls` |
| Capture output | `tmux capture-pane -pt coap_ipsns_sensitivity \| tail -n 80` |

## Command

```bash
cd /home/soroush/minimum-weighted-fas-heuristics
export PYTHONPATH=src
python3 -u scripts/run_coap_ipsns_sensitivity.py --resume --workers 4 \
  > logs/coap_ipsns_sensitivity/run_$(date +%Y%m%d_%H%M%S).log 2>&1
```

**Active log (this launch):** `logs/coap_ipsns_sensitivity/run_20260610_190059.log`

**Driver:** `scripts/run_coap_ipsns_sensitivity.py`

**Plan:** `experiments/coap_ipsns_sensitivity/config/sensitivity_plan.yaml`

## Process

| Field | Value |
|---|---|
| PID (initial) | 1486512 |
| Workers | 4 |
| `--resume` | enabled |

## Experiment design (reduced)

Full Cartesian product of `configs/sensitivity.yaml` would be **432 configs × 10 instances = 4320 runs** — excessive.

**Scientific reduction:** one-at-a-time (OAT) sensitivity around manuscript defaults on the EXP2 representative subset (10 instances):

- Baseline: `iters=400`, `topK=15`, `destroy_addback=0.30`, `destroy_remove=0.02`, `tol=1e-12`, `rng_seed=1`
- Vary one parameter at a time: `iters∈{100,200,600}`, `topK∈{5,10,20}`, `addback∈{0.15,0.25,0.35}`, `remove∈{0.01,0.05}`, `rng∈{2,3}`

| Metric | Value |
|---|---|
| Instances | 10 |
| Unique configs per instance | 14 |
| **Total planned runs** | **140** |
| Pilot runs (pre-launch) | 6 (bad1/bad2; resumed/skipped) |
| Pending at full launch | 134 |

## Pilot estimate (2026-06-10)

| Metric | Value |
|---|---|
| Pilot scope | 2 instances × 3 configs = 6 runs |
| Pilot wall time | ~0.6 s (tiny instances) |
| Pilot mean run time | ~0.045 s |
| Projected total CPU (rough) | ~1600 s (~27 min) single-thread; dominated by `r1000`/`grid` |
| Projected with 4 workers | ~7–15 min (observed `r1000` ~47 s/run at 400 iters) |
| Projected disk | ~7–10 MB checkpoints + JSONL + tmp rankings |
| Parallel safe? | **Yes** — unique checkpoint JSON + tmp CSV per run key |
| Recommended workers | **4** (20 cores, 62 GiB RAM; conservative) |

## Output paths

| Purpose | Path |
|---|---|
| Per-run checkpoints | `experiments/coap_ipsns_sensitivity/checkpoints/runs/<run_key>.json` |
| Success log (append) | `experiments/coap_ipsns_sensitivity/results/runs.jsonl` |
| Failure log (append) | `experiments/coap_ipsns_sensitivity/results/failures.jsonl` |
| Run manifest | `experiments/coap_ipsns_sensitivity/results/run_manifest.json` |
| tmux log | `logs/coap_ipsns_sensitivity/run_20260610_190059.log` |
| Completion marker | `logs/coap_ipsns_sensitivity/COMPLETED.ok` |
| Summary (on completion) | `logs/coap_ipsns_sensitivity/summary.json` |

## Safe restart

```bash
cd /home/soroush/minimum-weighted-fas-heuristics
export PYTHONPATH=src
python3 -u scripts/run_coap_ipsns_sensitivity.py --resume --workers 4 \
  >> logs/coap_ipsns_sensitivity/run_$(date +%Y%m%d_%H%M%S).log 2>&1
```

Or in tmux:

```bash
tmux new-session -d -s coap_ipsns_sensitivity
tmux send-keys -t coap_ipsns_sensitivity \
  'cd /home/soroush/minimum-weighted-fas-heuristics && export PYTHONPATH=src && python3 -u scripts/run_coap_ipsns_sensitivity.py --resume --workers 4 >> logs/coap_ipsns_sensitivity/run_$(date +%Y%m%d_%H%M%S).log 2>&1' C-m
```

Restart preserves valid checkpoints; reruns only missing/failed/invalid configurations.

## Post-completion workflow (do not update manuscript until complete)

1. Verify `logs/coap_ipsns_sensitivity/COMPLETED.ok`
2. Validate run counts in `summary.json`
3. Inspect `results/failures.jsonl`
4. Regenerate processed summaries from raw checkpoints
5. Run consistency checks
6. Then update tables/figures/prose/PDF

## Status (updated after launch)

| Metric | Value |
|---|---|
| **Status** | **COMPLETE** |
| Completion marker | `logs/coap_ipsns_sensitivity/COMPLETED.ok` |
| Expected runs | 140 |
| Completed runs | 140 |
| Skipped (resume from pilot) | 6 |
| Failed runs | 0 |
| Elapsed (driver wall clock) | ~220 s (~3.7 min) with 4 workers |
| Finished (UTC) | 2026-06-10T23:04:39Z |


```bash
tmux ls
tmux capture-pane -pt coap_ipsns_sensitivity | tail -n 80
tail -f logs/coap_ipsns_sensitivity/run_20260610_190059.log
ls experiments/coap_ipsns_sensitivity/checkpoints/runs/*.json | wc -l
wc -l experiments/coap_ipsns_sensitivity/results/runs.jsonl
```
