"""Reusable UI components for Pharus Lee carousel slides."""
from PIL import ImageDraw
from config import *
from primitives import *
from fonts import *


def top_label(draw, text, lang):
    """Top-left label (e.g. 'PHARUS LEE' or essay category)."""
    f = label(SIZE_TAG)
    draw.text((MARGIN_L, TOP_Y), text.upper(), fill=GOLD, font=f)


def series_badge(draw, page, total):
    """Top-right page badge: 01 / 05."""
    text = f"{page:02d} / {total:02d}"
    f = label(SIZE_TAG)
    bbox = f.getbbox(text)
    tw = bbox[2] - bbox[0]
    draw.text((W - MARGIN_R - tw, TOP_Y), text, fill=GOLD, font=f)


def section_title(draw, title, subtitle, y, lang):
    """Centered section title with optional subtitle. Returns next y."""
    if lang == "KR":
        f_title = title_kr(SIZE_TITLE)
    else:
        f_title = title_en(SIZE_TITLE)

    lines = wrap_text(title, f_title, CONTENT_W)
    for line in lines:
        bbox = f_title.getbbox(line)
        tw = bbox[2] - bbox[0]
        draw.text(((W - tw) // 2, y), line, fill=GOLD_LIGHT, font=f_title)
        y += bbox[3] - bbox[1] + 12

    if subtitle:
        y += 8
        # Use italic for EN, serif for KR (InstrumentSerif has no Korean glyphs)
        if has_korean(subtitle):
            f_sub = title_kr(SIZE_SUBTITLE)
        else:
            f_sub = subtitle_it(SIZE_SUBTITLE)
        bbox = f_sub.getbbox(subtitle)
        tw = bbox[2] - bbox[0]
        draw.text(((W - tw) // 2, y), subtitle, fill=CREAM_DIM, font=f_sub)
        y += bbox[3] - bbox[1] + 12

    return y + 20


def body_paragraph(draw, text, y, lang, color=CREAM, max_w=None):
    """Wrapped body text block. Returns next y."""
    f = body(lang, SIZE_BODY)
    mw = max_w or CONTENT_W
    lines = wrap_text(text, f, mw)
    for line in lines:
        draw.text((MARGIN_L, y), line, fill=color, font=f)
        y += SIZE_BODY + 14
    return y + 10


def quote_block(img, draw, text, y, lang):
    """Stylized quote with emerald card + gold diamond. Returns next y."""
    f = quote_font(lang, SIZE_QUOTE)
    lines = wrap_text(text, f, CONTENT_W - 60)
    block_h = len(lines) * (SIZE_QUOTE + 14) + 50

    glass_card(img, draw, y, block_h, accent_color=EMERALD)

    qy = y + 25
    for line in lines:
        draw.text((MARGIN_L + 30, qy), line, fill=GOLD_LIGHT, font=f)
        qy += SIZE_QUOTE + 14

    return y + block_h + 20


def bullet_point(draw, text, y, lang, dot_color=EMERALD):
    """Single bullet with colored dot. Returns next y."""
    f = body(lang, SIZE_BODY)
    # Dot
    draw.ellipse([MARGIN_L, y + 14, MARGIN_L + 10, y + 24], fill=dot_color)
    # Text
    lines = wrap_text(text, f, CONTENT_W - 30)
    for line in lines:
        draw.text((MARGIN_L + 30, y), line, fill=CREAM, font=f)
        y += SIZE_BODY + 12
    return y + 8


def numbered_item(draw, num, title, desc, y, lang, accent=GOLD):
    """Numbered circle + title + description. Returns next y."""
    # Number circle
    r = 20
    cx, cy = MARGIN_L + r, y + r
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=accent, width=2)
    nf = label(SIZE_LABEL)
    nt = str(num)
    nb = nf.getbbox(nt)
    nw = nb[2] - nb[0]
    draw.text((cx - nw // 2, cy - 14), nt, fill=accent, font=nf)

    # Title
    tx = MARGIN_L + 55
    f_bold = body_bold(lang, SIZE_BODY_BOLD)
    draw.text((tx, y), title, fill=GOLD_LIGHT, font=f_bold)
    y += SIZE_BODY_BOLD + 8

    # Description
    f = body(lang, SIZE_BODY)
    lines = wrap_text(desc, f, CONTENT_W - 55)
    for line in lines:
        draw.text((tx, y), line, fill=CREAM_DIM, font=f)
        y += SIZE_BODY + 10
    return y + 16


def footer_bar(draw, page, total, handle="@pharuslee"):
    """Bottom bar: page dots + handle."""
    page_dots(draw, page, total)
    f = label(SIZE_TAG - 2)
    bbox = f.getbbox(handle)
    tw = bbox[2] - bbox[0]
    draw.text(((W - tw) // 2, BOTTOM_Y + 50), handle, fill=CREAM_DIM, font=f)
