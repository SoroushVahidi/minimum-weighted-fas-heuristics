#!/usr/bin/env python3
"""Build contact sheets from rendered PDF page PNGs."""

from __future__ import annotations

import math
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    Image = None


ROOT = Path(__file__).resolve().parents[1]
RENDER_DIR = ROOT / "notes" / "final_warning_pass" / "rendered_pages"
OUT_DIR = ROOT / "notes" / "final_warning_pass" / "contact_sheets"
REPORT = ROOT / "notes" / "final_warning_pass" / "contact_sheet_report.md"
PAGES_PER_SHEET = 6


def page_number(path: Path) -> int:
    stem = path.stem
    if "-" in stem:
        return int(stem.rsplit("-", 1)[-1])
    digits = "".join(ch for ch in stem if ch.isdigit())
    return int(digits) if digits else 0


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    pages = sorted(RENDER_DIR.glob("page-*.png"), key=page_number)
    if not pages:
        REPORT.write_text("# Contact Sheet Report\n\nNo rendered pages found.\n")
        print("No rendered pages found.")
        return

    if Image is None:
        REPORT.write_text(
            "# Contact Sheet Report\n\nPillow unavailable; contact sheets not built.\n"
        )
        print("Pillow unavailable.")
        return

    cols = 2
    rows = PAGES_PER_SHEET // cols
    thumb_w, thumb_h = 500, 700
    pad = 20
    label_h = 28
    sheet_w = cols * thumb_w + (cols + 1) * pad
    sheet_h = rows * (thumb_h + label_h) + (rows + 1) * pad

    sheets: list[Path] = []
    for sheet_idx, start in enumerate(range(0, len(pages), PAGES_PER_SHEET)):
        batch = pages[start : start + PAGES_PER_SHEET]
        sheet = Image.new("RGB", (sheet_w, sheet_h), "white")
        draw = ImageDraw.Draw(sheet)
        try:
            font = ImageFont.truetype("DejaVuSans.ttf", 18)
        except OSError:
            font = ImageFont.load_default()

        for i, page_path in enumerate(batch):
            row, col = divmod(i, cols)
            x = pad + col * (thumb_w + pad)
            y = pad + row * (thumb_h + label_h + pad)
            img = Image.open(page_path).convert("RGB")
            img.thumbnail((thumb_w, thumb_h))
            sheet.paste(img, (x, y))
            label = f"Page {page_number(page_path)}"
            draw.text((x, y + thumb_h + 4), label, fill="black", font=font)

        out = OUT_DIR / f"contact_sheet_{sheet_idx + 1:02d}.png"
        sheet.save(out)
        sheets.append(out)

    lines = [
        "# Contact Sheet Report",
        "",
        f"- rendered pages: {len(pages)}",
        f"- pages per sheet: {PAGES_PER_SHEET}",
        f"- contact sheets: {len(sheets)}",
        "",
        "## Sheets",
        "",
    ]
    for s in sheets:
        lines.append(f"- `{s.relative_to(ROOT.parent)}`")
    REPORT.write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
