# Artifact Design

## Structure (final)

```
online_resource_1/
├── README.md, LICENSE, CITATION.cff, MANIFEST.sha256
├── requirements.txt, requirements-dev.txt, pytest.ini
├── src/                    # mwfas implementation
├── tests/                  # 78-test gate
├── scripts/                # reproduce_*.sh + CLI runners
├── environment/            # versions and freeze
├── supplement/             # LaTeX + online_resource_1.pdf
├── results/exp1..exp10/    # committed summaries only
├── results/combined/       # manuscript tables
├── experiments/exp10/      # minimal smoke archive + scripts (for tests)
├── manifests/
└── provenance/
```

## Deviations from initial template

| Planned | Actual | Reason |
|---------|--------|--------|
| `code/src` + `code/tests` | `src/` + `tests/` at root | Tests resolve `REPO_ROOT = parents[2]` correctly |
| Bundle EXP10 raw JSON | Summaries only + smoke archive | 15 MB raw redundant with `run_level_results.csv` |
| Full checkpoints in OR1 | Empty checkpoints dir + 2 test skips | 3720 checkpoint files unnecessary for reproduction |

## Excluded

`.git`, virtualenvs, audit folders, manuscript PDFs, EXP10 production raw/checkpoints/logs, confidential correspondence, absolute paths (sanitized).
