# Environment and Dependency Audit

| Item | Value |
|------|-------|
| Minimum Python | 3.11 (CI matrix) |
| Tested Python | 3.12.3 |
| OS | Ubuntu 24.04 Linux |
| CPU | Intel Core i7-12700K |
| Direct deps | `requirements.txt`: numpy, pandas, networkx, pyyaml, tqdm |
| Dev deps | `requirements-dev.txt`: pytest>=8, pytest-cov>=5 |
| Freeze file | `online_resource_1/environment/dependency_lock_or_freeze.txt` |
| DRMacIver SHA-256 | `907b7abe96ff8fb54d8b70910eb3068744f765e72da5520f2c7aacf70ba996bd` |
| Git commit | `80b3144d5fdbbe250faed8a4fe671dde2da76c89` |

HiGHS and python-igraph are optional (EXP8/EXP4 external wrappers only).
