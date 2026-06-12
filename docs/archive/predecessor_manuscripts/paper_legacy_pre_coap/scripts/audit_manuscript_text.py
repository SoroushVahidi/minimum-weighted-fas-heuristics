#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SECTIONS_DIR = ROOT / "sections"
TABLES_DIR = ROOT / "tables"
FIGURES_DIR = ROOT / "figures"
DECLARATIONS_DIR = ROOT / "declarations"
NOTES_DIR = ROOT / "notes"
REFERENCES = ROOT / "references.bib"
MAIN_ANON = ROOT / "main_anonymized.tex"
MAIN = ROOT / "main.tex"
HIGHLIGHTS = ROOT / "highlights.txt"
TITLE_PAGE = ROOT / "title_page.tex"

SECTION_FILES = sorted(SECTIONS_DIR.glob("*.tex"))
SHARED_TEX = [MAIN_ANON, *SECTION_FILES, *sorted(TABLES_DIR.glob("*.tex")), *sorted(FIGURES_DIR.glob("*.tex"))]
ALL_TEX = [MAIN, MAIN_ANON, TITLE_PAGE, *SECTION_FILES, *sorted(TABLES_DIR.glob("*.tex")), *sorted(FIGURES_DIR.glob("*.tex")), *sorted(DECLARATIONS_DIR.glob("*.tex"))]

WORD_RE = re.compile(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)?")
CITE_RE = re.compile(r"\\cite[a-zA-Z*]*\{([^}]+)\}")
BIB_KEY_RE = re.compile(r"@\s*\w+\s*\{\s*([^,\s]+)")

TODO_PATTERNS = ("TODO", "FIXME", "rejection-audit", "citation needed", "tbd", "TBD")
IDENTITY_TERMS = [
    "Soroush",
    "Vahidi",
    "NJIT",
    "New Jersey Institute of Technology",
    "SoroushVahidi",
    "github.com/SoroushVahidi",
    "sv96",
]
OVERCLAIM_TERMS = [
    "state-of-the-art",
    "universal",
    "guarantee",
    "guaranteed",
    "optimal",
    "dominates",
    "dominant",
]
REPORT_TERMS = [
    "repository",
    "commit",
    "tmux",
    "raw summary",
    "GitHub",
    "EXP1",
    "EXP2",
    "EXP3",
    "EXP4",
    "EXP5",
]


def read(path: Path) -> str:
    return path.read_text(errors="ignore") if path.exists() else ""


def strip_latex(text: str) -> str:
    text = re.sub(r"(?<!\\)%.*", " ", text)
    text = re.sub(r"\\begin\{[^}]*\}", " ", text)
    text = re.sub(r"\\end\{[^}]*\}", " ", text)
    text = re.sub(r"\\(label|ref|cite[a-zA-Z*]*|input|includegraphics|bibliographystyle|bibliography)\{[^}]*\}", " ", text)
    text = re.sub(r"\\[A-Za-z@]+(\[[^\]]*\])?(\{[^{}]*\})?", " ", text)
    text = text.replace("{", " ").replace("}", " ")
    return text


def word_count(text: str) -> int:
    return len(WORD_RE.findall(strip_latex(text)))


def find_lines(paths: list[Path], terms: list[str] | tuple[str, ...]) -> list[dict]:
    hits = []
    for path in paths:
        text = read(path)
        for lineno, line in enumerate(text.splitlines(), 1):
            lowered = line.lower()
            matched = [term for term in terms if term.lower() in lowered]
            if matched:
                hits.append(
                    {
                        "file": str(path.relative_to(ROOT)),
                        "line": lineno,
                        "matches": matched,
                        "text": line.strip(),
                    }
                )
    return hits


def extract_abstract(tex: str) -> str:
    match = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", tex, re.S)
    return match.group(1).strip() if match else ""


def section_counts() -> dict:
    counts = {"sections": 0, "subsections": 0, "subsubsections": 0}
    per_file = {}
    for path in SECTION_FILES:
        text = read(path)
        file_counts = {
            "sections": len(re.findall(r"\\section\{", text)),
            "subsections": len(re.findall(r"\\subsection\{", text)),
            "subsubsections": len(re.findall(r"\\subsubsection\{", text)),
        }
        per_file[path.name] = file_counts
        for key in counts:
            counts[key] += file_counts[key]
    return {"totals": counts, "per_file": per_file}


def parse_citations() -> dict:
    tex = "\n".join(read(path) for path in ALL_TEX if path.exists())
    cited = set()
    for match in CITE_RE.finditer(tex):
        for key in match.group(1).split(","):
            key = key.strip()
            if key:
                cited.add(key)
    keys = set(BIB_KEY_RE.findall(read(REFERENCES)))
    missing = sorted(cited - keys)
    return {
        "used_count": len(cited),
        "used_keys": sorted(cited),
        "bib_count": len(keys),
        "missing_keys": missing,
    }


def parse_highlights() -> list[dict]:
    bullets = []
    for raw in read(HIGHLIGHTS).splitlines():
        line = raw.strip()
        if not line:
            continue
        clean = line.lstrip("-• ").rstrip()
        bullets.append({"text": clean, "chars": len(clean)})
    return bullets


def main() -> None:
    section_word_counts = {path.stem: word_count(read(path)) for path in SECTION_FILES}
    abstract = extract_abstract(read(MAIN_ANON))
    abstract_words = word_count(abstract)
    total_section_words = sum(section_word_counts.values())
    highlights = parse_highlights()
    counts = section_counts()
    todo_hits = find_lines([MAIN, MAIN_ANON, TITLE_PAGE, *SECTION_FILES, *sorted(TABLES_DIR.glob("*.tex")), *sorted(FIGURES_DIR.glob("*.tex")), *sorted(DECLARATIONS_DIR.glob("*.tex"))], TODO_PATTERNS)
    identity_hits = find_lines(SHARED_TEX, IDENTITY_TERMS)
    overclaim_hits = find_lines(SHARED_TEX, OVERCLAIM_TERMS)
    report_hits = find_lines(SHARED_TEX, REPORT_TERMS)
    citations = parse_citations()

    data = {
        "total_section_words": total_section_words,
        "section_word_counts": section_word_counts,
        "abstract_words": abstract_words,
        "abstract_ok": abstract_words <= 250,
        "section_counts": counts["totals"],
        "section_counts_per_file": counts["per_file"],
        "todos": todo_hits,
        "identity_hits": identity_hits,
        "overclaim_hits": overclaim_hits,
        "report_language_hits": report_hits,
        "highlights": highlights,
        "highlights_ok": 3 <= len(highlights) <= 5 and all(item["chars"] <= 85 for item in highlights),
        "citations": citations,
    }

    json_path = NOTES_DIR / "full_manuscript_audit.json"
    md_path = NOTES_DIR / "full_manuscript_audit.md"
    json_path.write_text(json.dumps(data, indent=2) + "\n")

    md_lines = [
        "# Full Manuscript Audit",
        "",
        "## Word counts",
        "",
        f"- Total section words: {total_section_words}",
        f"- Abstract words: {abstract_words} ({'OK' if abstract_words <= 250 else 'Too long'})",
        "",
        "### Per-section words",
        "",
    ]
    for name, count in section_word_counts.items():
        md_lines.append(f"- `{name}.tex`: {count}")

    md_lines += [
        "",
        "## Section structure",
        "",
        f"- Main sections: {counts['totals']['sections']}",
        f"- Subsections: {counts['totals']['subsections']}",
        f"- Subsubsections: {counts['totals']['subsubsections']}",
        "",
        "## Highlights",
        "",
        f"- Count: {len(highlights)} ({'OK' if 3 <= len(highlights) <= 5 else 'Check required'})",
    ]
    for item in highlights:
        status = "OK" if item["chars"] <= 85 else "Too long"
        md_lines.append(f"- {item['chars']} chars ({status}): {item['text']}")

    md_lines += [
        "",
        "## Citation sanity",
        "",
        f"- Citation keys used: {citations['used_count']}",
        f"- Missing citation keys: {len(citations['missing_keys'])}",
    ]
    if citations["missing_keys"]:
        for key in citations["missing_keys"]:
            md_lines.append(f"  - `{key}`")

    def add_hits(title: str, hits: list[dict]) -> None:
        md_lines.extend(["", f"## {title}", ""])
        if not hits:
            md_lines.append("- None")
            return
        for hit in hits:
            md_lines.append(f"- [{hit['file']}]({ROOT / hit['file']}:{hit['line']}): `{hit['text']}`")

    add_hits("TODOs", todo_hits)
    add_hits("Identity Leaks In Anonymized Or Shared Files", identity_hits)
    add_hits("Overclaiming Phrases", overclaim_hits)
    add_hits("Repository Or Report Language", report_hits)

    md_path.write_text("\n".join(md_lines) + "\n")


if __name__ == "__main__":
    main()
