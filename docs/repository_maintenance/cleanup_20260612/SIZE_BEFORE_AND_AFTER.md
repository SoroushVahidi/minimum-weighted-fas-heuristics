# Size Before and After

| Metric | Before (6c04ff1) | After cleanup |
|---|---|---|
| Tracked files (`git ls-files`) | 6336 | see post-commit count |
| Working tree size | ~333 MB | ~334 MB |
| Top-level `submission_package/` | present | removed (archived) |
| Top-level `paper/` | present | removed (archived) |

Large ignored trees (EXP10 raw, checkpoints) unchanged by policy. No aggressive checkpoint deletion.
