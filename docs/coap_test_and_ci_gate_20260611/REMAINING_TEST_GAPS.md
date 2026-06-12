# Remaining Test Gaps

## Before COAP submission (recommended)

1. Expand IPSNS coverage for `wmsf_seed_mode="legacy"` and accepted/rejected move accounting under crafted graphs.
2. Add explicit CLI invalid-input error-message tests (`FileNotFoundError` / nonzero exit).
3. Run GitHub Actions workflow remotely once and record badge/status in OR1.
4. Port remaining EXP10 script tests (`test_launcher_schedule`, `test_preflight_passed`) into pytest if still needed post-finalize.
5. Add holdout/sensitivity manifest schema validation tests (read-only on committed summaries).

## May defer to revision

1. Hypothesis-based random testing (not added; deterministic seeded tests used instead).
2. `baselines.py` coverage (DRMacIver wrapper not in unit gate).
3. Full manuscript table-regeneration integration test.
4. Performance/regression timing thresholds.
5. Negative-weight pipeline tests beyond parser contract.

## Not testable without author action

1. Online Resource 1 packaging end-to-end download-and-rerun script.
2. Full EXP10 repeated-run median integration (awaiting manuscript text, not code defect).
