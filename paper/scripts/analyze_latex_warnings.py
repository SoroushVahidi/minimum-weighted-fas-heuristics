#!/usr/bin/env python3
"""Parse LaTeX compile logs and classify warnings by severity."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


OVERFULL_RE = re.compile(
    r"Overfull \\hbox \(([\d.]+)pt too wide\) in paragraph at lines (\d+)--(\d+)"
)
UNDERFULL_RE = re.compile(
    r"Underfull \\hbox \(badness (\d+)\) in paragraph at lines (\d+)--(\d+)"
)
UNDEF_REF_RE = re.compile(r"LaTeX Warning: Reference `([^']+)' on page \d+ undefined")
UNDEF_CITE_RE = re.compile(r"LaTeX Warning: Citation `([^']+)' on page \d+ undefined")
MISSING_FILE_RE = re.compile(r"LaTeX Warning: File `([^']+)' not found")
RERUN_RE = re.compile(r"LaTeX Warning: .*Rerun")
FLOAT_RE = re.compile(r"LaTeX Warning: (Float|Label\(s\) may have changed)")
ERROR_RE = re.compile(r"^! (.+)")
FILE_LINE_RE = re.compile(r"^([^:]+):(\d+):")
LATEXMK_WARN_RE = re.compile(
    r"^warning:\s+([^:]+):(\d+):\s*(.+)$"
)
BIB_WARN_RE = re.compile(
    r"(Overfull|Underfull) \\hbox.*(?:bibliography|references\.bib|\.bbl)",
    re.IGNORECASE,
)

LOW_PACKAGE_PATTERNS = (
    "algorithm.sty",
    "inputenc",
    "fontenc",
    "rerunfilecheck",
)


def classify_overfull(pt: float) -> str:
    if pt > 2.0:
        return "high"
    return "low"


def classify_underfull(badness: int) -> str:
    if badness >= 5000:
        return "medium"
    if badness >= 2000:
        return "medium"
    return "low"


def parse_log(text: str, log_path: Path) -> dict:
    lines = text.splitlines()
    warnings: list[dict] = []
    errors: list[dict] = []
    current_file = str(log_path.name)

    for i, line in enumerate(lines):
        stripped = line.strip()
        lm = LATEXMK_WARN_RE.match(stripped)
        if lm:
            current_file = lm.group(1)
            payload = lm.group(3)
            if "Invalid UTF-8" in payload or payload.strip() == "":
                warnings.append(
                    {
                        "type": "package_warning",
                        "severity": "low",
                        "file": current_file,
                        "log_line": i + 1,
                        "message": payload.strip() or "algorithm.sty UTF-8 warning",
                    }
                )
                continue
            line = payload

        m = FILE_LINE_RE.match(stripped)
        if m and not stripped.startswith("!") and not lm:
            current_file = m.group(1)

        em = ERROR_RE.match(stripped)
        if em:
            errors.append(
                {
                    "type": "error",
                    "severity": "critical",
                    "message": em.group(1),
                    "file": current_file,
                    "log_line": i + 1,
                }
            )

        for m in UNDEF_REF_RE.finditer(line):
            warnings.append(
                {
                    "type": "undefined_reference",
                    "severity": "critical",
                    "target": m.group(1),
                    "file": current_file,
                    "log_line": i + 1,
                    "message": line.strip(),
                }
            )

        for m in UNDEF_CITE_RE.finditer(line):
            warnings.append(
                {
                    "type": "undefined_citation",
                    "severity": "critical",
                    "target": m.group(1),
                    "file": current_file,
                    "log_line": i + 1,
                    "message": line.strip(),
                }
            )

        for m in MISSING_FILE_RE.finditer(line):
            warnings.append(
                {
                    "type": "missing_file",
                    "severity": "critical",
                    "target": m.group(1),
                    "file": current_file,
                    "log_line": i + 1,
                    "message": line.strip(),
                }
            )

        if RERUN_RE.search(line):
            warnings.append(
                {
                    "type": "rerun",
                    "severity": "medium",
                    "file": current_file,
                    "log_line": i + 1,
                    "message": line.strip(),
                }
            )

        if FLOAT_RE.search(line):
            warnings.append(
                {
                    "type": "float",
                    "severity": "medium",
                    "file": current_file,
                    "log_line": i + 1,
                    "message": line.strip(),
                }
            )

        m = OVERFULL_RE.search(line)
        if m:
            pt = float(m.group(1))
            warnings.append(
                {
                    "type": "overfull_hbox",
                    "severity": classify_overfull(pt),
                    "pt": pt,
                    "line_start": int(m.group(2)),
                    "line_end": int(m.group(3)),
                    "file": current_file,
                    "log_line": i + 1,
                    "message": line.strip(),
                }
            )

        m = UNDERFULL_RE.search(line)
        if m:
            badness = int(m.group(1))
            warnings.append(
                {
                    "type": "underfull_hbox",
                    "severity": classify_underfull(badness),
                    "badness": badness,
                    "line_start": int(m.group(2)),
                    "line_end": int(m.group(3)),
                    "file": current_file,
                    "log_line": i + 1,
                    "message": line.strip(),
                }
            )

        if "LaTeX Warning:" in line and not any(
            pat in line
            for pat in (
                "Reference",
                "Citation",
                "not found",
                "Rerun",
                "Float",
                "Label(s)",
            )
        ):
            sev = "low"
            if any(p in line for p in LOW_PACKAGE_PATTERNS):
                sev = "low"
            elif "Overfull" in line or "Underfull" in line:
                pass
            else:
                warnings.append(
                    {
                        "type": "package_warning",
                        "severity": sev,
                        "file": current_file,
                        "log_line": i + 1,
                        "message": line.strip(),
                    }
                )

        if BIB_WARN_RE.search(line):
            warnings[-1]["severity"] = "medium" if warnings else None

    return {"errors": errors, "warnings": warnings}


def dedupe_warnings(warnings: list[dict]) -> list[dict]:
    """Keep the last occurrence from multi-pass latexmk logs."""
    keyed: dict[tuple, dict] = {}
    order: list[tuple] = []
    for w in warnings:
        key = (
            w.get("type"),
            w.get("file"),
            w.get("line_start"),
            w.get("line_end"),
            w.get("pt"),
            w.get("badness"),
            w.get("target"),
        )
        if key not in keyed:
            order.append(key)
        keyed[key] = w
    return [keyed[k] for k in order]


def summarize(parsed: dict) -> dict:
    warnings = dedupe_warnings(parsed["warnings"])
    errors = parsed["errors"]
    by_severity = Counter()
    by_type = Counter()
    for w in warnings:
        by_severity[w["severity"]] += 1
        by_type[w["type"]] += 1
    for _ in errors:
        by_severity["critical"] += 1
        by_type["error"] += 1

    overfull = [w for w in warnings if w["type"] == "overfull_hbox"]
    underfull = [w for w in warnings if w["type"] == "underfull_hbox"]
    high_overfull = [w for w in overfull if w.get("pt", 0) > 2.0]

    source_ranges = Counter()
    for w in warnings:
        if "line_start" in w:
            source_ranges[f"{w['file']}:{w['line_start']}-{w['line_end']}"] += 1

    return {
        "counts": {
            "critical": by_severity["critical"],
            "high": by_severity["high"],
            "medium": by_severity["medium"],
            "low": by_severity["low"],
            "overfull": len(overfull),
            "underfull": len(underfull),
            "overfull_gt_2pt": len(high_overfull),
            "warning_lines": len(warnings) + len(errors),
            "errors": len(errors),
        },
        "by_type": dict(by_type),
        "top_source_ranges": source_ranges.most_common(25),
        "warnings": sorted(
            warnings + errors,
            key=lambda w: (
                {"critical": 0, "high": 1, "medium": 2, "low": 3}.get(
                    w["severity"], 4
                ),
                -w.get("pt", 0),
                -w.get("badness", 0),
                w.get("file", ""),
            ),
        ),
    }


def write_reports(summary: dict, prefix: Path) -> None:
    prefix.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "counts": summary["counts"],
        "by_type": summary["by_type"],
        "top_source_ranges": summary["top_source_ranges"],
        "warnings": summary["warnings"],
    }
    prefix.with_suffix(".json").write_text(json.dumps(payload, indent=2))

    lines = [
        "# LaTeX Warning Analysis",
        "",
        "## Counts by severity",
        "",
        f"- critical: {summary['counts']['critical']}",
        f"- high: {summary['counts']['high']}",
        f"- medium: {summary['counts']['medium']}",
        f"- low: {summary['counts']['low']}",
        "",
        "## Counts by warning type",
        "",
        f"- overfull hbox: {summary['counts']['overfull']}",
        f"- overfull hbox >2pt: {summary['counts']['overfull_gt_2pt']}",
        f"- underfull hbox: {summary['counts']['underfull']}",
        f"- total warning lines: {summary['counts']['warning_lines']}",
        f"- errors: {summary['counts']['errors']}",
        "",
        "## Top repeated source ranges",
        "",
    ]
    for src, count in summary["top_source_ranges"]:
        lines.append(f"- `{src}`: {count}")
    lines.extend(["", "## Warnings sorted by severity", ""])
    lines.append("| Severity | Type | File | Lines | Detail |")
    lines.append("|---|---|---|---|---|")
    for w in summary["warnings"][:120]:
        line_rng = ""
        if "line_start" in w:
            line_rng = f"{w['line_start']}-{w['line_end']}"
        detail = w.get("message", "")[:100]
        if w.get("pt") is not None:
            detail = f"{w['pt']}pt too wide"
        if w.get("badness") is not None:
            detail = f"badness {w['badness']}"
        lines.append(
            f"| {w['severity']} | {w['type']} | {w.get('file','')} | {line_rng} | {detail} |"
        )
    prefix.with_suffix(".md").write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Primary log file")
    parser.add_argument("--output-prefix", required=True)
    parser.add_argument(
        "--extra",
        action="append",
        default=[],
        help="Additional log files to merge",
    )
    args = parser.parse_args()

    paper_dir = Path(__file__).resolve().parents[1]
    logs = [paper_dir / args.input]
    logs.extend(paper_dir / p for p in args.extra)
    if (paper_dir / "main_anonymized.log").exists():
        extra = paper_dir / "main_anonymized.log"
        if extra not in logs:
            logs.append(extra)

    merged = {"errors": [], "warnings": []}
    for log in logs:
        if not log.exists():
            continue
        parsed = parse_log(log.read_text(errors="ignore"), log)
        merged["errors"].extend(parsed["errors"])
        merged["warnings"].extend(parsed["warnings"])

    summary = summarize(merged)
    write_reports(summary, Path(args.output_prefix))


if __name__ == "__main__":
    main()
