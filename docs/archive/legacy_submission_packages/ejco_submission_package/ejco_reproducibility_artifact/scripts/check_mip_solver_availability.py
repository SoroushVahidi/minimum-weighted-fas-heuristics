"""
Check MIP/exact solver availability for EXP8.
Writes reports to experiments/exp8_medium_mip_baseline/config/
"""
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
OUT = BASE / "experiments/exp8_medium_mip_baseline/config"
OUT.mkdir(parents=True, exist_ok=True)

report = {}

# scipy / HiGHS (preferred)
try:
    import scipy
    report["scipy_version"] = scipy.__version__
    try:
        from scipy.optimize import milp, LinearConstraint, Bounds
        report["scipy_milp"] = True
        report["scipy_milp_backend"] = "HiGHS (via scipy)"
    except ImportError:
        report["scipy_milp"] = False
except ImportError:
    report["scipy_version"] = None
    report["scipy_milp"] = False

# standalone highspy
try:
    import highspy
    report["highspy"] = True
except ImportError:
    report["highspy"] = False

# pulp
try:
    import pulp
    report["pulp"] = pulp.__version__
except ImportError:
    report["pulp"] = None

# ortools
try:
    from ortools.linear_solver import pywraplp
    report["ortools"] = True
except ImportError:
    report["ortools"] = None

# gurobipy
try:
    import gurobipy
    v = gurobipy.gurobi.version()
    report["gurobipy"] = f"{v[0]}.{v[1]}.{v[2]}"
except Exception:
    report["gurobipy"] = None

# python-mip
try:
    import mip
    report["python_mip"] = mip.__version__
except ImportError:
    report["python_mip"] = None

# Determine recommended solver
if report.get("scipy_milp"):
    report["recommended_solver"] = "scipy.optimize.milp (HiGHS)"
    report["solver_available"] = True
elif report.get("pulp"):
    report["recommended_solver"] = "pulp"
    report["solver_available"] = True
elif report.get("ortools"):
    report["recommended_solver"] = "ortools"
    report["solver_available"] = True
elif report.get("gurobipy"):
    report["recommended_solver"] = "gurobipy"
    report["solver_available"] = True
elif report.get("python_mip"):
    report["recommended_solver"] = "python-mip"
    report["solver_available"] = True
else:
    report["recommended_solver"] = None
    report["solver_available"] = False

# Existing exact scripts
exact_scripts = list(BASE.glob("src/**/*exact*")) + list(BASE.glob("scripts/**/*exact*"))
report["existing_exact_scripts"] = [str(p.relative_to(BASE)) for p in exact_scripts]

# Write JSON
(OUT / "solver_availability.json").write_text(json.dumps(report, indent=2))

# Write markdown summary
md = f"""# EXP8 MIP Solver Availability

| Solver | Available | Version/Note |
|---|---|---|
| scipy.optimize.milp (HiGHS) | {'Yes' if report.get('scipy_milp') else 'No'} | {report.get('scipy_version','—')} |
| highspy | {'Yes' if report.get('highspy') else 'No'} | — |
| pulp | {'Yes' if report.get('pulp') else 'No'} | {report.get('pulp') or '—'} |
| ortools | {'Yes' if report.get('ortools') else 'No'} | — |
| gurobipy | {'Yes' if report.get('gurobipy') else 'No'} | {report.get('gurobipy') or '—'} |
| python-mip | {'Yes' if report.get('python_mip') else 'No'} | {report.get('python_mip') or '—'} |

**Recommended solver:** {report.get('recommended_solver') or 'NONE — no usable MIP solver found'}

**Solver available for EXP8:** {'YES' if report.get('solver_available') else 'NO'}
"""
(OUT / "solver_availability.md").write_text(md)

print(json.dumps(report, indent=2))
if not report["solver_available"]:
    print("\nERROR: No usable MIP solver found. EXP8 cannot proceed.", file=sys.stderr)
    sys.exit(1)
else:
    print(f"\nUsing: {report['recommended_solver']}")
