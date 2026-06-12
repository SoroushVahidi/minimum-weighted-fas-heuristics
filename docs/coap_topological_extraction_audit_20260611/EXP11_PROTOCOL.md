# EXP11 protocol (frozen)

**Name:** Topological-extraction sensitivity  
**HEAD:** `80b3144d5fdbbe250faed8a4fe671dde2da76c89`

## Input

LR-TA final active DAG per instance (reconstructed, not stored).

## Rules

1. `current_min_id` — repository default (Kahn, min-heap vertex id)
2. `max_id` — Kahn, max-heap vertex id
3. `weighted_net` — Kahn, priority by active weighted out−in degree
4. `insertion_refine` — one-pass single-vertex insertion respecting active precedence

## Metrics

- \(\mathrm{bw}(\pi)\)
- \(w(F)-\mathrm{bw}(\pi)\)
- Relative improvement vs current with \(\varepsilon=10^{-9}\)

## Exclusions

Negative-weight instances (peterson1/2) reported but excluded from nonnegative headline.
