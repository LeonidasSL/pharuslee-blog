"""Generate OG images (1200x630) for Pharus Lee blog posts.

Reuses the carousel design system (colors, fonts, primitives).
Output: public/og/default.png, public/og/{lang}/{slug}.png
"""
import os, sys

# Add generator dir to path so we can import config/fonts/primitives
sys.path.insert(0, os.path.dirname(__file__))

from PIL import Image, ImageDraw
from config import BG_DARK, BG_MID, GOLD, GOLD_LIGHT, CREAM, CREAM_DIM
from fonts import load_font, has_korean, NOTO_SERIF_KR, CRIMSON_PRO, JURA, BOLD, MEDIUM, REGULAR, SEMIBOLD
from primitives import _lerp_color

# OG image dimensions
OG_W, OG_H = 1200, 630

# Output directory (relative to project root)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT_DIR = os.path.join(PROJECT_ROOT, "public", "og")


def _og_background():
    """Dark gradient background matching brand style."""
    img = Image.new("RGB", (OG_W, OG_H), BG_DARK)
    pixels = img.load()
    for y in range(OG_H):
        t = y / OG_H
        if t < 0.3:
            c = _lerp_color(BG_MID, BG_DARK, t / 0.3)
        elif t < 0.7:
            c = BG_DARK
        else:
            c = _lerp_color(BG_DARK, BG_MID, (t - 0.7) / 0.3)
        for x in range(OG_W):
            pixels[x, y] = c
    return img


def _diamond(draw, cx, cy, size=8):
    """Gold diamond shape."""
    draw.polygon(
        [(cx, cy - size), (cx + size, cy), (cx, cy + size), (cx - size, cy)],
        fill=GOLD,
    )


def _gold_line(draw, y, x1, x2):
    draw.line([(x1, y), (x2, y)], fill=GOLD, width=1)


def _wrap_text(text, font, max_width):
    """Word-wrap text to fit within max_width pixels."""
    words = text.split()
    lines, current = [], ""
    for word in words:
        test = f"{current} {word}".strip()
        bbox = font.getbbox(test)
        if bbox[2] - bbox[0] > max_width and current:
            lines.append(current)
            current = word
        else:
            current = test
    if current:
        lines.append(current)
    return lines


def generate_default():
    """Brand OG image: charcoal bg + PHARUS LEE gold + diamond + tagline."""
    img = _og_background()
    draw = ImageDraw.Draw(img)
    cx = OG_W // 2

    # Brand name
    brand_font = load_font(JURA, 72, MEDIUM)
    text = "PHARUS LEE"
    bbox = brand_font.getbbox(text)
    tw = bbox[2] - bbox[0]
    draw.text((cx - tw // 2, 200), text, fill=GOLD, font=brand_font)

    # Diamond separator
    _gold_line(draw, 300, cx - 120, cx - 20)
    _diamond(draw, cx, 300)
    _gold_line(draw, 300, cx + 20, cx + 120)

    # Tagline
    tagline_font = load_font(CRIMSON_PRO, 30, REGULAR)
    tagline = "Consciousness · Spirituality · Technology"
    bbox = tagline_font.getbbox(tagline)
    tw = bbox[2] - bbox[0]
    draw.text((cx - tw // 2, 340), tagline, fill=CREAM_DIM, font=tagline_font)

    # Bottom accent line
    _gold_line(draw, 530, 100, OG_W - 100)

    # URL
    url_font = load_font(JURA, 22, MEDIUM)
    url_text = "pharuslee.com"
    bbox = url_font.getbbox(url_text)
    tw = bbox[2] - bbox[0]
    draw.text((cx - tw // 2, 555), url_text, fill=CREAM_DIM, font=url_font)

    path = os.path.join(OUT_DIR, "default.png")
    img.save(path, "PNG")
    print(f"  OK{path}")


def generate_post(title: str, lang: str, slug: str):
    """Post OG image: title centered on brand background."""
    img = _og_background()
    draw = ImageDraw.Draw(img)
    cx = OG_W // 2
    margin = 100
    max_w = OG_W - margin * 2

    # Choose font based on language
    is_kr = has_korean(title)
    if is_kr:
        title_font = load_font(NOTO_SERIF_KR, 56, BOLD)
    else:
        title_font = load_font(CRIMSON_PRO, 60, BOLD)

    # Wrap title
    lines = _wrap_text(title, title_font, max_w)
    line_h = 75 if is_kr else 80
    total_h = len(lines) * line_h

    # Center vertically (slightly above center for visual balance)
    start_y = (OG_H - total_h) // 2 - 30

    for i, line in enumerate(lines):
        bbox = title_font.getbbox(line)
        tw = bbox[2] - bbox[0]
        draw.text((cx - tw // 2, start_y + i * line_h), line, fill=CREAM, font=title_font)

    # Diamond separator below title
    sep_y = start_y + total_h + 30
    _gold_line(draw, sep_y, cx - 80, cx - 15)
    _diamond(draw, cx, sep_y, size=6)
    _gold_line(draw, sep_y, cx + 15, cx + 80)

    # Author name below separator
    author_font = load_font(JURA, 26, MEDIUM)
    author = "PHARUS LEE"
    bbox = author_font.getbbox(author)
    tw = bbox[2] - bbox[0]
    draw.text((cx - tw // 2, sep_y + 25), author, fill=GOLD, font=author_font)

    # Top accent line
    _gold_line(draw, 40, 100, OG_W - 100)

    # Bottom accent line + URL
    _gold_line(draw, 545, 100, OG_W - 100)
    url_font = load_font(JURA, 20, MEDIUM)
    url_text = "pharuslee.com"
    bbox = url_font.getbbox(url_text)
    tw = bbox[2] - bbox[0]
    draw.text((cx - tw // 2, 565), url_text, fill=CREAM_DIM, font=url_font)

    # Save
    lang_dir = os.path.join(OUT_DIR, lang)
    os.makedirs(lang_dir, exist_ok=True)
    path = os.path.join(lang_dir, f"{slug}.png")
    img.save(path, "PNG")
    print(f"  OK{path}")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    print("Generating OG images...")

    generate_default()

    # Blog posts: (title, lang, slug)
    posts = [
        ("보로미르 신드롬: AI 시대의 절대반지", "ko", "boromir-syndrome"),
        ("The Boromir Syndrome: The One Ring of the AI Age", "en", "boromir-syndrome"),
        ("의식과 AI의 교차점에서", "ko", "consciousness-and-ai"),
        ("At the Intersection of Consciousness and AI", "en", "consciousness-and-ai"),
    ]

    for title, lang, slug in posts:
        generate_post(title, lang, slug)

    print(f"\nDone! {len(posts) + 1} images generated in {OUT_DIR}")


if __name__ == "__main__":
    main()
