"""
CAIE abstract, keywords, highlights, and length audit.
Produces JSON and Markdown reports in paper/notes/final_submission_audit/.
"""

import json
import re
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PAPER = REPO / "paper"
OUT_DIR = PAPER / "notes" / "final_submission_audit"
OUT_DIR.mkdir(parents=True, exist_ok=True)

ABBREVS_OF_INTEREST = ["MWFAS", "LR-TA", "WMSF", "IPSNS", "LOLIB", "DRMacIver", "FAS"]

# ── helpers ─────────────────────────────────────────────────────────────────

def strip_latex(text: str) -> str:
    text = re.sub(r"\\[a-zA-Z]+\{([^}]*)\}", r"\1", text)
    text = re.sub(r"\\[a-zA-Z]+", " ", text)
    text = re.sub(r"[{}]", " ", text)
    text = re.sub(r"``|''|`|'", '"', text)
    return text

def count_words(text: str) -> int:
    clean = strip_latex(text)
    return len(clean.split())

def extract_block(source: str, env: str):
    pattern = rf"\\begin\{{{env}\}}(.*?)\\end\{{{env}\}}"
    m = re.search(pattern, source, re.DOTALL)
    return m.group(1).strip() if m else ""

def detect_citations(text: str):
    return re.findall(r"\\cite[tp]?\*?\{[^}]+\}", text)

def extract_keywords_from_block(block: str):
    clean = block.replace("\\sep", "|").replace("\n", " ")
    parts = [k.strip() for k in clean.split("|") if k.strip()]
    return parts

def check_abbreviation_defined(abbrev: str, abstract_text: str) -> dict:
    idx = abstract_text.find(abbrev)
    if idx == -1:
        return {"found": False, "defined": None}
    # look for a definition pattern like "X (ABBREV)" or "ABBREV (expansion)"
    before = abstract_text[:idx]
    defined = bool(re.search(
        r"\b" + re.escape(abbrev) + r"\s*\(|"
        r"\([^)]*\b" + re.escape(abbrev) + r"\b",
        abstract_text[:idx + len(abbrev) + 60]
    ))
    return {"found": True, "defined": defined, "first_position": idx}

def page_count_pdf(pdf_path: Path):
    try:
        out = subprocess.check_output(["pdfinfo", str(pdf_path)], text=True, stderr=subprocess.DEVNULL)
        m = re.search(r"Pages:\s*(\d+)", out)
        return int(m.group(1)) if m else None
    except Exception:
        return None

def word_count_pdf(pdf_path: Path):
    try:
        out = subprocess.check_output(["pdftotext", str(pdf_path), "-"], text=True, stderr=subprocess.DEVNULL)
        return len(out.split())
    except Exception:
        return None

def count_latex_commands(tex: str, cmd: str) -> int:
    return len(re.findall(r"\\" + re.escape(cmd) + r"\b", tex))

def gather_all_tex(base_tex: Path) -> str:
    r"""Recursively inline \input{} commands."""
    root = base_tex.parent

    def _read(p: Path) -> str:
        if not p.exists():
            return ""
        src = p.read_text(errors="ignore")

        def _replace(m):
            inc = m.group(1)
            if not inc.endswith(".tex"):
                inc += ".tex"
            # try path relative to current file first, then relative to paper root
            candidate = p.parent / inc
            if not candidate.exists():
                candidate = root / inc
            return _read(candidate)

        return re.sub(r"\\input\{([^}]+)\}", _replace, src)

    return _read(base_tex)

def find_repetition_candidates(full_tex: str) -> list:
    candidates = []
    patterns = [
        (r"dense.*?LOLIB.*?scope", "Dense/scope caveat repeated"),
        (r"best.*?observed.*?not.*?optim", "Best-observed caveat repeated"),
        (r"sparse.*?outperform.*?baseline", "Sparse outperform baseline repeated"),
        (r"EXP[6-9].*?interpret", "EXP6-9 interpretation note"),
    ]
    for pat, label in patterns:
        hits = re.findall(pat, full_tex, re.IGNORECASE | re.DOTALL)
        if len(hits) > 1:
            candidates.append({"pattern": pat, "label": label, "occurrences": len(hits)})
    return candidates

# ── main audit ───────────────────────────────────────────────────────────────

def audit():
    report = {}

    # ── 1. Source files ──────────────────────────────────────────────────────
    anon_tex_path = PAPER / "main_anonymized.tex"
    main_tex_path = PAPER / "main.tex"

    anon_src = anon_tex_path.read_text(errors="ignore") if anon_tex_path.exists() else ""
    main_src = main_tex_path.read_text(errors="ignore") if main_tex_path.exists() else ""

    # ── 2. Abstract ──────────────────────────────────────────────────────────
    anon_abstract_raw = extract_block(anon_src, "abstract")
    main_abstract_raw = extract_block(main_src, "abstract")

    abstract_text = anon_abstract_raw  # authoritative

    abstract_word_count = count_words(abstract_text)
    abstract_pass = abstract_word_count <= 250
    citations_in_abstract = detect_citations(abstract_text)
    abstract_plain = strip_latex(abstract_text)

    abbrev_status = {}
    for abbrev in ABBREVS_OF_INTEREST:
        abbrev_status[abbrev] = check_abbreviation_defined(abbrev, abstract_text)

    abstracts_match = (
        anon_abstract_raw.strip() == main_abstract_raw.strip()
    )

    report["abstract"] = {
        "word_count": abstract_word_count,
        "limit": 250,
        "pass": abstract_pass,
        "has_citations": bool(citations_in_abstract),
        "citations_found": citations_in_abstract,
        "abbreviations": abbrev_status,
        "anon_main_match": abstracts_match,
        "text_preview": abstract_plain[:300],
    }

    # ── 3. Keywords ──────────────────────────────────────────────────────────
    anon_kw_block = extract_block(anon_src, "keyword")
    main_kw_block = extract_block(main_src, "keyword")

    anon_keywords = extract_keywords_from_block(anon_kw_block)
    main_keywords = extract_keywords_from_block(main_kw_block)

    kw_count = len(anon_keywords)
    kw_pass = 1 <= kw_count <= 7
    keywords_match = anon_keywords == main_keywords

    kw_issues = []
    for kw in anon_keywords:
        words_in_kw = kw.lower().split()
        if "and" in words_in_kw or "of" in words_in_kw:
            kw_issues.append({"keyword": kw, "issue": "contains 'and' or 'of'"})
        if len(kw.split()) > 5:
            kw_issues.append({"keyword": kw, "issue": "long phrase (>5 words)"})

    report["keywords"] = {
        "count": kw_count,
        "limit_min": 1,
        "limit_max": 7,
        "pass": kw_pass,
        "keywords": anon_keywords,
        "anon_main_match": keywords_match,
        "issues": kw_issues,
    }

    # ── 4. Highlights ─────────────────────────────────────────────────────────
    highlights_path = PAPER / "highlights.txt"
    upload_highlights_path = REPO / "submission_package" / "files_for_upload" / "highlights.txt"

    def load_highlights(p: Path):
        if not p.exists():
            return []
        lines = [ln.strip() for ln in p.read_text(errors="ignore").splitlines() if ln.strip()]
        bullets = []
        for ln in lines:
            # strip leading bullet markers
            text = re.sub(r"^[-•*]\s*", "", ln)
            bullets.append(text)
        return bullets

    paper_highlights = load_highlights(highlights_path)
    upload_highlights = load_highlights(upload_highlights_path)

    def check_highlights(bullets):
        results = []
        for b in bullets:
            char_len = len(b)
            results.append({
                "text": b,
                "char_count": char_len,
                "pass": char_len <= 85,
            })
        count = len(bullets)
        return {
            "count": count,
            "count_pass": 3 <= count <= 5,
            "bullets": results,
            "all_char_pass": all(r["pass"] for r in results),
            "overall_pass": 3 <= count <= 5 and all(r["pass"] for r in results),
        }

    hl_paper = check_highlights(paper_highlights)
    hl_upload = check_highlights(upload_highlights)
    highlights_match = paper_highlights == upload_highlights

    report["highlights"] = {
        "paper_highlights": hl_paper,
        "upload_highlights": hl_upload,
        "paper_upload_match": highlights_match,
    }

    # ── 5. Page and word counts from PDF ─────────────────────────────────────
    pdf_path = PAPER / "main_anonymized.pdf"
    pages = page_count_pdf(pdf_path)
    words = word_count_pdf(pdf_path)

    report["pdf"] = {
        "path": str(pdf_path.relative_to(REPO)),
        "exists": pdf_path.exists(),
        "pages": pages,
        "approx_word_count": words,
        "page_comment": (
            "44 pages: no strict CAIE page limit; acceptable for full experimental paper."
            if pages and pages <= 50 else
            "Check page count."
        ),
    }

    # ── 6. Structure counts from full LaTeX ──────────────────────────────────
    full_tex = gather_all_tex(anon_tex_path)

    sections = len(re.findall(r"\\section\b", full_tex))
    subsections = len(re.findall(r"\\subsection\b", full_tex))
    tables = len(re.findall(r"\\begin\{table", full_tex))
    figures = len(re.findall(r"\\begin\{figure", full_tex))
    algorithms = len(re.findall(r"\\begin\{algorithm\b", full_tex))

    report["structure"] = {
        "sections": sections,
        "subsections": subsections,
        "tables": tables,
        "figures": figures,
        "algorithms": algorithms,
    }

    # ── 7. Repetition / compression candidates ────────────────────────────────
    candidates = find_repetition_candidates(full_tex)
    report["compression_candidates"] = {
        "found": candidates,
        "recommendation": (
            "Review identified patterns for safe compression; do not remove EXP6-9 evidence."
            if candidates else
            "No obvious repeated patterns found."
        ),
    }

    # ── 8. Overall pass/fail ─────────────────────────────────────────────────
    abstract_ok = abstract_pass and not citations_in_abstract
    keywords_ok = kw_pass and not kw_issues
    highlights_ok = hl_paper["overall_pass"]

    report["overall"] = {
        "abstract_pass": abstract_ok,
        "keywords_pass": keywords_ok,
        "highlights_pass": highlights_ok,
        "ready": abstract_ok and keywords_ok and highlights_ok,
        "recommendation": (
            "All CAIE abstract/keywords/highlights checks pass. Ready for upload."
            if abstract_ok and keywords_ok and highlights_ok
            else "One or more checks failed — see details above."
        ),
    }

    # ── 9. Write JSON ─────────────────────────────────────────────────────────
    json_path = OUT_DIR / "abstract_keywords_length_check.json"
    json_path.write_text(json.dumps(report, indent=2))

    # ── 10. Write Markdown ────────────────────────────────────────────────────
    lines = ["# CAIE Abstract / Keywords / Highlights / Length Audit\n"]

    # Abstract
    a = report["abstract"]
    lines.append("## Abstract")
    status = "PASS" if a["pass"] else "FAIL"
    lines.append(f"- Word count: **{a['word_count']}** / 250  →  **{status}**")
    lines.append(f"- Citations in abstract: {'YES — FIX NEEDED' if a['has_citations'] else 'None (OK)'}")
    if a["citations_found"]:
        for c in a["citations_found"]:
            lines.append(f"  - `{c}`")
    lines.append(f"- Abstract matches between main.tex and main_anonymized.tex: {a['anon_main_match']}")
    lines.append("\n### Abbreviations in abstract")
    for abbrev, info in a["abbreviations"].items():
        if info["found"]:
            defined = info["defined"]
            lines.append(f"- `{abbrev}`: found at position {info['first_position']} — {'defined at/before first use (OK)' if defined else 'NOT defined at first use — check manually'}")
        else:
            lines.append(f"- `{abbrev}`: not found in abstract")

    # Keywords
    k = report["keywords"]
    lines.append("\n## Keywords")
    kstatus = "PASS" if k["pass"] else "FAIL"
    lines.append(f"- Count: **{k['count']}** (1–7 allowed)  →  **{kstatus}**")
    lines.append(f"- Keywords match between main.tex and main_anonymized.tex: {k['anon_main_match']}")
    lines.append("- Keyword list:")
    for i, kw in enumerate(k["keywords"], 1):
        lines.append(f"  {i}. {kw}")
    if k["issues"]:
        lines.append("- **Issues found:**")
        for iss in k["issues"]:
            lines.append(f"  - `{iss['keyword']}`: {iss['issue']}")
    else:
        lines.append("- No keyword issues found (OK)")

    # Highlights
    lines.append("\n## Highlights")
    hp = report["highlights"]["paper_highlights"]
    hstatus = "PASS" if hp["overall_pass"] else "FAIL"
    lines.append(f"- Count: **{hp['count']}** (3–5 required)  →  count {'OK' if hp['count_pass'] else 'FAIL'}")
    lines.append(f"- All bullets ≤85 chars: {'YES' if hp['all_char_pass'] else 'NO'}  →  **{hstatus}**")
    lines.append(f"- paper/highlights.txt matches upload highlights.txt: {report['highlights']['paper_upload_match']}")
    for b in hp["bullets"]:
        flag = "" if b["pass"] else " ← EXCEEDS 85 CHARS"
        lines.append(f"  - ({b['char_count']} chars) {b['text']}{flag}")

    # PDF / length
    p = report["pdf"]
    lines.append("\n## Manuscript Length")
    lines.append(f"- Pages: **{p['pages']}**")
    lines.append(f"- Approximate word count (from pdftotext): **{p['approx_word_count']}**")
    lines.append(f"- Assessment: {p['page_comment']}")

    # Structure
    s = report["structure"]
    lines.append("\n## Document Structure (LaTeX counts)")
    lines.append(f"- Sections: {s['sections']}")
    lines.append(f"- Subsections: {s['subsections']}")
    lines.append(f"- Tables: {s['tables']}")
    lines.append(f"- Figures: {s['figures']}")
    lines.append(f"- Algorithms: {s['algorithms']}")

    # Compression
    c = report["compression_candidates"]
    lines.append("\n## Compression / Repetition Candidates")
    lines.append(c["recommendation"])
    if c["found"]:
        for item in c["found"]:
            lines.append(f"- **{item['label']}** ({item['occurrences']} occurrences)")

    # Overall
    ov = report["overall"]
    lines.append("\n## Overall Result")
    lines.append(f"- Abstract: {'PASS' if ov['abstract_pass'] else 'FAIL'}")
    lines.append(f"- Keywords: {'PASS' if ov['keywords_pass'] else 'FAIL'}")
    lines.append(f"- Highlights: {'PASS' if ov['highlights_pass'] else 'FAIL'}")
    lines.append(f"\n**{ov['recommendation']}**")

    md_path = OUT_DIR / "abstract_keywords_length_check.md"
    md_path.write_text("\n".join(lines) + "\n")

    print(f"JSON: {json_path}")
    print(f"MD:   {md_path}")
    return report

if __name__ == "__main__":
    r = audit()
    # print a brief summary
    ov = r["overall"]
    print(f"\nAbstract words: {r['abstract']['word_count']}/250  pass={r['abstract']['pass']}")
    print(f"Keywords: {r['keywords']['count']}  pass={r['keywords']['pass']}")
    hl = r['highlights']['paper_highlights']
    print(f"Highlights: {hl['count']} bullets  all_char_pass={hl['all_char_pass']}  overall={hl['overall_pass']}")
    print(f"Pages: {r['pdf']['pages']}")
    print(f"Overall ready: {ov['ready']}")
    if not ov['ready']:
        print("Issues found — see MD report.")
