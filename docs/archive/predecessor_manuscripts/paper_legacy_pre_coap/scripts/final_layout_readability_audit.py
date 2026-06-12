#!/usr/bin/env python3
"""
Final layout/readability audit: compile log analysis + PDF text stats + pattern scan.
Outputs paper/notes/final_layout_readability_audit/{final_layout_audit.json,.md,main_anonymized_text.txt}
"""
from __future__ import annotations
import json
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAPER = ROOT / "paper"
OUT_DIR = PAPER / "notes" / "final_layout_readability_audit"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ── 1. Compile log analysis ─────────────────────────────────────────────────
log_path = PAPER / "final_layout_compile.log"
if not log_path.exists():
    log_path = PAPER / "final_layout_recompile.log"

log_text = log_path.read_text(errors="ignore") if log_path.exists() else ""
overfull = [l for l in log_text.splitlines() if "overfull" in l.lower()]
underfull = [l for l in log_text.splitlines() if "underfull" in l.lower()]
undef_refs = [l for l in log_text.splitlines()
              if "undefined" in l.lower() and "hyperref" not in l.lower()]
errors = [l for l in log_text.splitlines()
          if l.strip().startswith("!") or ("error" in l.lower() and "warning" not in l.lower())]

# ── 2. PDF text extraction ───────────────────────────────────────────────────
pdf_path = PAPER / "main_anonymized.pdf"
txt_path = OUT_DIR / "main_anonymized_text.txt"
if pdf_path.exists():
    subprocess.run(["pdftotext", str(pdf_path), str(txt_path)],
                   check=False, capture_output=True)
pdf_text = txt_path.read_text(errors="ignore") if txt_path.exists() else ""

# Page count from pdfinfo
pages = None
try:
    pi = subprocess.check_output(["pdfinfo", str(pdf_path)], text=True, stderr=subprocess.STDOUT)
    m = re.search(r"Pages:\s*(\d+)", pi)
    pages = int(m.group(1)) if m else None
except Exception:
    pass

total_words = len(pdf_text.split())

# ── 3. Section word counts (from source tex) ────────────────────────────────
sec_dir = PAPER / "sections"
section_words: dict[str, int] = {}
for tex in sorted(sec_dir.glob("*.tex")):
    t = tex.read_text(errors="ignore")
    section_words[tex.name] = len(t.split())

# ── 4. Float/structure counts ────────────────────────────────────────────────
all_tex_text = ""
for tex in sorted((PAPER / "sections").glob("*.tex")):
    all_tex_text += tex.read_text(errors="ignore") + "\n"
all_tex_text += (PAPER / "main_anonymized.tex").read_text(errors="ignore")

tables_count = all_tex_text.count(r"\begin{table}")
figures_count = all_tex_text.count(r"\begin{figure}")
algos_count = all_tex_text.count(r"\begin{algorithm}")

# Check for floats after \bibliography in PDF text (crude)
bib_idx = pdf_text.lower().find("references")
post_ref_text = pdf_text[bib_idx:] if bib_idx >= 0 else ""
post_ref_table = "Table" in post_ref_text[500:] if len(post_ref_text) > 500 else False
post_ref_figure = "Figure" in post_ref_text[500:] if len(post_ref_text) > 500 else False

# ── 5. Repeated phrase scan ──────────────────────────────────────────────────
defensive_phrases = [
    "scope boundary", "not a new approximation", "not a universal",
    "best observed", "dense", "limitation",
]
phrase_counts: dict[str, int] = {}
src_all = ""
for tex in sorted((PAPER / "sections").glob("*.tex")):
    src_all += tex.read_text(errors="ignore") + "\n"
for ph in defensive_phrases:
    phrase_counts[ph] = src_all.lower().count(ph.lower())

# ── 6. Identity / style scan ────────────────────────────────────────────────
identity_terms = [
    "Soroush", "Vahidi", "NJIT", "New Jersey Institute of Technology",
    "sv96@njit.edu", "sv96", "SoroushVahidi", "github.com/SoroushVahidi",
    "ORCID", "Koutis",
]
bad_style_terms = [
    "writing pass", "earlier audit", "audit concern", "prior manuscript",
    "manuscript should", "paper should", "repository report", "internal report",
]
files = [PAPER / "main_anonymized.tex"]
for d in ["sections", "tables", "figures", "algorithms"]:
    if (PAPER / d).exists():
        files += sorted((PAPER / d).glob("*.tex"))
files.append(PAPER / "references.bib")

source_identity: dict[str, list] = {}
source_style: dict[str, list] = {}
for p in files:
    if not p.exists():
        continue
    txt = p.read_text(errors="ignore")
    ih = [t for t in identity_terms if t.lower() in txt.lower()]
    sh = [t for t in bad_style_terms if t.lower() in txt.lower()]
    if ih:
        source_identity[str(p)] = ih
    if sh:
        source_style[str(p)] = sh

pdf_identity = [t for t in identity_terms if t.lower() in pdf_text.lower()]
pdf_placeholders = [t for t in ["TODO", "FIXME", "??", "[Editor Name]",
                                 "[Corresponding Author Contact]"]
                    if t.lower() in pdf_text.lower()]

# ── 7. Assemble report ───────────────────────────────────────────────────────
report = {
    "pages": pages,
    "total_pdf_words": total_words,
    "section_source_words": section_words,
    "tables": tables_count,
    "figures": figures_count,
    "algorithms": algos_count,
    "overfull_count": len(overfull),
    "underfull_count": len(underfull),
    "undefined_ref_count": len(undef_refs),
    "error_count": len(errors),
    "overfull_lines": overfull[:20],
    "underfull_summary": list(dict.fromkeys(underfull))[:20],
    "post_reference_table": post_ref_table,
    "post_reference_figure": post_ref_figure,
    "defensive_phrase_counts": phrase_counts,
    "source_identity_hits": source_identity,
    "source_style_hits": source_style,
    "pdf_identity_hits": pdf_identity,
    "pdf_placeholder_hits": pdf_placeholders,
}
(OUT_DIR / "final_layout_audit.json").write_text(json.dumps(report, indent=2))

# ── 8. Markdown summary ──────────────────────────────────────────────────────
md_lines = [
    "# Final Layout/Readability Audit",
    "",
    f"## Page count: {pages}",
    f"## Total PDF words (approx): {total_words:,}",
    "",
    "## Section word counts (source TeX)",
    "| Section file | Words |",
    "|---|---:|",
]
for f, w in section_words.items():
    md_lines.append(f"| {f} | {w:,} |")

md_lines += [
    "",
    "## Float counts",
    f"- Tables: {tables_count}",
    f"- Figures: {figures_count}",
    f"- Algorithms: {algos_count}",
    "",
    "## Compile warnings",
    f"- Overfull \\\\hbox: **{len(overfull)}**",
    f"- Underfull \\\\hbox: {len(underfull)}",
    f"- Undefined refs: {len(undef_refs)}",
    f"- Errors: {len(errors)}",
]
if overfull:
    md_lines += ["", "### Overfull lines"] + overfull[:10]
if undef_refs:
    md_lines += ["", "### Undefined refs"] + undef_refs[:10]

md_lines += [
    "",
    "## Post-reference floats",
    f"- Table after References: {post_ref_table}",
    f"- Figure after References: {post_ref_figure}",
    "",
    "## Repeated/defensive phrase counts (source TeX)",
    "| Phrase | Count |",
    "|---|---:|",
]
for ph, cnt in sorted(phrase_counts.items(), key=lambda x: -x[1]):
    flag = " ⚠" if cnt > 8 else ""
    md_lines.append(f"| {ph} | {cnt}{flag} |")

md_lines += [
    "",
    "## Anonymization/style scan",
    f"- Source identity hits: {source_identity or 'none'}",
    f"- Source style hits: {source_style or 'none'}",
    f"- PDF identity hits: {pdf_identity or 'none'}",
    f"- PDF placeholders: {pdf_placeholders or 'none'}",
    "",
    "## Verdict",
]
issues = []
if len(overfull) > 0:
    issues.append(f"{len(overfull)} overfull hboxes")
if undef_refs:
    issues.append(f"{len(undef_refs)} undefined refs")
if post_ref_table or post_ref_figure:
    issues.append("floats appear after References")
if source_identity or pdf_identity:
    issues.append("identity terms found")
if phrase_counts.get("dense", 0) > 15:
    issues.append(f"'dense' used {phrase_counts['dense']}× — check for repetition")

if issues:
    md_lines.append("**Issues found:** " + "; ".join(issues))
else:
    md_lines.append("**No blocking layout issues. Underfull hboxes only (cosmetic).**")

(OUT_DIR / "final_layout_audit.md").write_text("\n".join(md_lines) + "\n")
print("\n".join(md_lines))
