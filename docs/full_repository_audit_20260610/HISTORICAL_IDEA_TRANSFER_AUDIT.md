# Historical Repository Idea Transfer Audit

**Audit date:** 2026-06-10  
**Scope:** Predecessor repos per `docs/provenance/predecessor_project_manifest.md` and deferred historical notes.

## Ideas from predecessor / historical work

| Idea | Source | Current equivalent | Novelty vs current | Benefit | Cost | Risk | Priority |
|---|---|---|---|---|---|---|---|
| LR-TA topological add-back | Predecessor 1 (JOCO) | `src/mwfas/lrta.py` | **Integrated** | Core contribution | — | — | Done |
| IPSNS incumbent LNS | Predecessor 2 | `src/mwfas/ipsns.py` | **Integrated** | Core contribution | — | — | Done |
| WMSF seed pipeline | Predecessor 2 | `src/mwfas/wmsf.py` | **Integrated** | Strong seed | — | — | Done |
| Unified notebook prototype | Both predecessors | `notebooks/` | Superseded by `src/` | None | — | Confusion if used | Archive only |
| Interval/block refinement | Historical repos (not in manifest detail) | **Absent** | Potentially novel | Unknown on sparse graphs | High impl. cost | Distraction pre-submission | **Defer** |
| Genetic/memetic search | Historical | **Absent** | Low for current narrative | Maybe on dense | Very high | Off-scope | Defer |
| Persistent-edge learning | Historical | **Absent** | Unclear | Unknown | High | Engineering risk | Defer |
| Expanded seed portfolio | Historical | Dual seed only (WMSF+LR) | Moderate | Diminishing returns | Medium compute | More tuning | Post-holdout optional |
| Parallel SCC processing | Historical | Sequential SCC loops | Engineering | Speed on large graphs | Refactor + tests | Race bugs | Post-submission |
| Rocket-Crane variants | Historical | **Absent** | Unknown | Unknown | Unknown | Unknown | Defer |
| Permanent-edge scoring | Historical | SCC backward-weight scoring | Partially related | IPSNS already scores SCCs | — | Redundant | Low |
| Large-graph specializations | Historical | Budget curve + holdout on large ISCAS | Partial | May help s38417-class | Experiment time | Scope creep | After holdout |

## Recommended experiments (only if holdout completes early)

| Experiment | Stop rule |
|---|---|
| Expanded seed portfolio (3rd seed) | Stop if holdout shows no gain on holdout split |
| Parallel SCC (read-only scoring parallel) | Stop if speedup <2× on s38417 with bugs |
| sfas / igraph exact_ip baselines | **Do before submission** if time — strengthens baselines |

## Do not merge pre-submission

- Interval/block refinement code from historical repos (no provenance in current tree)
- Genetic/memetic layers (conflicts with COAP algorithm-engineering story)

## Predecessor repos for manual review

1. https://github.com/SoroushVahidi/weighted-minfas-local-ratio
2. https://github.com/SoroushVahidi/weighted-minfas-codes

Not cloned in this audit pass.
