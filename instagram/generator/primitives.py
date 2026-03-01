"""Low-level drawing primitives for Pharus Lee carousel."""
import math, random
from PIL import Image, ImageDraw
from config import *


def new_slide():
    """Create a slide with dark forest gradient background."""
    img = Image.new("RGB", (W, H), BG_DARK)
    _gradient_bg(img)
    return img


def _gradient_bg(img):
    """3-stop vertical gradient: mid → dark → mid (subtle vignette)."""
    pixels = img.load()
    for y in range(H):
        # Ease through dark center
        t = y / H
        if t < 0.3:
            frac = t / 0.3
            c = _lerp_color(BG_MID, BG_DARK, frac)
        elif t < 0.7:
            c = BG_DARK
        else:
            frac = (t - 0.7) / 0.3
            c = _lerp_color(BG_DARK, BG_MID, frac)
        for x in range(W):
            pixels[x, y] = c


def _lerp_color(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def glow(img, cx, cy, radius, color, intensity=30):
    """Radial gradient glow overlay."""
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    for r in range(radius, 0, -2):
        alpha = int(intensity * (1 - r / radius) ** 2)
        alpha = min(255, max(0, alpha))
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(*color, alpha))
    img.paste(Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB"))


def gold_line(draw, y, width=1):
    """Full-width gold accent line."""
    draw.line([(MARGIN_L, y), (W - MARGIN_R, y)], fill=GOLD, width=width)


def diamond_separator(draw, y):
    """Diamond accent separator: ——— ◆ ———"""
    mid = CENTER_X
    line_len = 100
    draw.line([(mid - line_len - 15, y), (mid - 15, y)], fill=GOLD, width=1)
    draw.line([(mid + 15, y), (mid + line_len + 15, y)], fill=GOLD, width=1)
    # Diamond
    s = 6
    draw.polygon([(mid, y - s), (mid + s, y), (mid, y + s), (mid - s, y)], fill=GOLD)


def glass_card(img, draw, y, height, accent_color=EMERALD_DARK):
    """Semi-transparent card with colored left border."""
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    x1, x2 = MARGIN_L, W - MARGIN_R
    # Card background
    od.rounded_rectangle([x1, y, x2, y + height], radius=12,
                         fill=(30, 32, 38, 140))
    # Left accent stripe
    od.rounded_rectangle([x1, y, x1 + 5, y + height], radius=2,
                         fill=(*accent_color, 200))
    img.paste(Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB"))


def page_dots(draw, current, total):
    """Bottom navigation dots."""
    dot_y = BOTTOM_Y + 20
    spacing = 22
    total_w = (total - 1) * spacing
    start_x = (W - total_w) // 2
    for i in range(total):
        x = start_x + i * spacing
        if i == current - 1:
            draw.ellipse([x - 5, dot_y - 5, x + 5, dot_y + 5], fill=GOLD)
        else:
            draw.ellipse([x - 3, dot_y - 3, x + 3, dot_y + 3], outline=CREAM_DIM, width=1)


def wrap_text(text, font, max_width):
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
