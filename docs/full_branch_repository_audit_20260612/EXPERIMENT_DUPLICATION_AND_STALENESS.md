# Experiment Duplication and Staleness Audit

## Duplication matrix

| Pair | Relationship | Action |
|---|---|---|
| EXP1 vs EXP1b | **Supersession** (seed mode) | Retain EXP1 with README archived warning; cite EXP1b only |
| EXP4 vs EXP10 | EXP10 is stochastic repeat on EXP4 subset | Not duplicate; complementary |
| EXP6 vs EXP7 | Same 20-instance subset | Different question (budget vs plain LS); both valid |
| coap_ipsns_sensitivity vs EXP2 | Same 10 instances | Sensitivity is parameter OAT; distinct purpose |
| `combined/` digest vs LaTeX tables | Digest subset of experiments | Digest stale for EXP6–11 |
| OR1 `results/exp*` vs `experiments/*/summary` | Mirrored summaries | Intentional OR1 bundle copy |

## Stale or misleading artifacts

| Item | Issue | Severity | Recommendation |
|---|---|---|---|
| `experiments/exp1_core_benchmark/` | Legacy seed; README should warn | Low | Keep with ARCHIVED label |
| `experiment_progress.json` NONFINAL | Misleading status field | Low | Update script when convenient |
| `experiments/combined/` | Digest covers EXP1b–5 only | Low | Regenerate or add README date |
| EXP5 README historical "in progress" | May contradict complete summary | Low | Verify README vs summary |
| EXP11 README "12 instances" vs aggregate 6 | Doc inconsistency | Low | Align README to aggregate.json |
| EXP10 raw + checkpoints (local) | Large disk use; gitignored | Info | Archive externally if needed; not in git |
| EXP10 smoke_archive/ | Quarantined preflight | Info | Correctly excluded from production counts |

## Abandoned / exploratory without warning?

| Item | Assessment |
|---|---|
| `experiments/seedfix_full_wmsf/` | Diagnostic only; report clarifies non-manuscript |
| `paper/` tree | Legacy; not wired to COAP build |
| `submission_package/` | EJCO; should not be used for COAP |

No **abandoned result is cited in the COAP manuscript** without scope qualification.

## Checkpoint necessity post-completion

| Experiment | Keep checkpoints? |
|---|---|
| EXP10 | Optional local archive; summaries sufficient for paper |
| coap_ipsns_sensitivity | Committed; useful for sensitivity audit trail |
| coap_ipsns_holdout | Needed until summary generated |

## Machine paths in results

Spot-check: committed summaries under `experiments/*/summary/` use relative paths or instance names. OR1 validation scans for `/home/soroush` — passes after cache cleanup.

## Verdict

Duplication is **mostly intentional** (OR1 mirror, subset studies). Staleness items are **documentation/metadata** level, not scientific integrity issues.
