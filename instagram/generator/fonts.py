"""Font loading for Pharus Lee carousel generator."""
import os
from PIL import ImageFont

_FONT_DIR = os.path.join(os.path.dirname(__file__), "fonts")
_WIN_FONTS = "C:/Windows/Fonts"

# Korean variable fonts (system)
NOTO_SANS_KR = os.path.join(_WIN_FONTS, "NotoSansKR-VF.ttf")
NOTO_SERIF_KR = os.path.join(_WIN_FONTS, "NotoSerifKR-VF.ttf")

# English fonts
CRIMSON_PRO = os.path.join(_FONT_DIR, "CrimsonPro-VF.ttf")
CRIMSON_PRO_IT = os.path.join(_FONT_DIR, "CrimsonPro-Italic-VF.ttf")
WORK_SANS = os.path.join(_FONT_DIR, "WorkSans-VF.ttf")
JURA = os.path.join(_FONT_DIR, "Jura-VF.ttf")
INSTRUMENT_SERIF_IT = os.path.join(_FONT_DIR, "InstrumentSerif-Italic.ttf")

LIGHT = 300
REGULAR = 400
MEDIUM = 500
SEMIBOLD = 600
BOLD = 700


def has_korean(text: str) -> bool:
    return any('\uac00' <= c <= '\ud7a3' for c in text)


def load_font(path: str, size: int, weight: int = None) -> ImageFont.FreeTypeFont:
    font = ImageFont.truetype(path, size)
    if weight is not None:
        try:
            axes = font.get_variation_axes()
            if axes:
                values = []
                for a in axes:
                    name = a['name'].decode() if isinstance(a['name'], bytes) else a['name']
                    if name == 'Weight':
                        clamped = max(a['minimum'], min(a['maximum'], weight))
                        values.append(clamped)
                    else:
                        values.append(a['default'])
                font.set_variation_by_axes(values)
        except Exception:
            pass
    return font


def title_kr(size=72):
    return load_font(NOTO_SERIF_KR, size, BOLD)

def title_en(size=64):
    return load_font(CRIMSON_PRO, size, BOLD)

def subtitle_it(size=36):
    return load_font(INSTRUMENT_SERIF_IT, size)

def body(lang, size=36):
    if lang == "KR":
        return load_font(NOTO_SANS_KR, size, REGULAR)
    return load_font(WORK_SANS, size, REGULAR)

def body_bold(lang, size=38):
    if lang == "KR":
        return load_font(NOTO_SANS_KR, size, BOLD)
    return load_font(WORK_SANS, size, BOLD)

def quote_font(lang, size=42):
    if lang == "KR":
        return load_font(NOTO_SERIF_KR, size, REGULAR)
    return load_font(CRIMSON_PRO_IT, size, REGULAR)

def label(size=28):
    return load_font(JURA, size, MEDIUM)
