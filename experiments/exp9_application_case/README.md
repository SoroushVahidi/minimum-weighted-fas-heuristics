# EXP9: Application Case Study — Wikipedia Adminship Vote Network

## Purpose

Address the CAIE venue-fit concern that the manuscript uses mainly abstract
graph-optimization benchmarks. This case study applies the MWFAS framework to
a real social-network dataset with a natural application framing.

## Dataset

**Wikipedia Adminship Vote Network (SNAP)**
- Source: J. Leskovec, D. Huttenlocher, J. Kleinberg. "Predicting Positive and
  Negative Links in Online Social Networks." Proc. WWW 2010.
- URL: https://snap.stanford.edu/data/wiki-Vote.html
- File: wiki-Vote.txt.gz (downloaded by prepare script)
- 7,115 nodes (Wikipedia users), 103,689 directed edges (vote events)
- Each edge u→v: user u cast a vote in support of user v's adminship candidacy

## Application framing

**Problem**: Find a hierarchical prestige ranking of Wikipedia users that
minimizes "reverse endorsements" — cases where a higher-ranked user endorsed a
lower-ranked one.

Under the MWFAS lens: each vote u→v is an arc; the backward weight of a
ranking counts the total weight of arcs that go from higher to lower rank. A
minimum-BW ordering extracts the best-fitting hierarchical structure from the
vote graph.

This is a real-world application of rank aggregation / social influence
ordering that connects directly to the paper's methodology.

## Conversion rule

1. Restrict to the top-N nodes by total vote degree (in + out) to form a
   manageable dense subgraph.  Default: top-50 nodes.  Smoke test: top-10.
2. For each ordered pair (u, v) in the top-N subset, count the total number of
   times u voted for v across all elections: w_uv = vote count.
3. Exclude zero-weight arcs; keep both directions if both > 0.
4. Save as DIMACS weighted arc file: `a u v w` per arc.
5. Node IDs are anonymized integer IDs (original SNAP integer IDs, no names).

## Algorithms to run

- LR-TA (ours)
- WMSF (ours)
- IPSNS (ours, default 400 iterations)
- DRMacIver/FAS (external)
- igraph approx_eades (external)
- Weighted Eades (adaptation)

## Expected runtime

- With top-50 nodes: all algorithms complete in seconds; IPSNS ≤ 5 minutes.
- Overnight run not expected; the experiment is designed to complete quickly.

## Anonymity / privacy notes

- The dataset uses integer node IDs from SNAP; no names or identifiable
  information is included.
- The SNAP dataset is publicly available and citable (Leskovec et al. 2010).
- No author-identifying data is used.
- Complies with CAIE double-anonymized review constraints.

## Monitoring tmux (if launched)

```bash
tmux attach -t mwfas_exp9_application   # attach to live session
# Ctrl-b then d to detach without stopping
tail -f experiments/exp9_application_case/logs/exp9_tmux.log
```

## Relation to prior experiments

EXP1b–EXP8 are NOT modified by this experiment.
Results go entirely under experiments/exp9_application_case/.

## Status

Setup: pending prepare script run.
