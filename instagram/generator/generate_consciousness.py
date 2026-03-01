"""Generate Instagram carousel for 'At the Intersection of Consciousness and AI'."""
import os, sys
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(__file__))
from config import *
from primitives import *
from components import *
from fonts import *

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "consciousness-and-ai")
TOTAL_SLIDES = 5


def slide_01(img, draw, lang):
    """Cover."""
    glow(img, CENTER_X, 400, 250, (20, 35, 45), intensity=25)
    glow(img, CENTER_X, 400, 120, (45, 40, 20), intensity=18)

    top_label(draw, "PHARUS LEE", lang)
    series_badge(draw, 1, TOTAL_SLIDES)

    if lang == "KR":
        y = section_title(draw, "의식과 AI의 교차점에서", None, 280, lang)
        diamond_separator(draw, y + 10)
        y = body_paragraph(draw, "AI가 의식을 가질 수 있는가라는 질문은, 어쩌면 의식이 무엇인가라는 더 근본적인 질문으로 우리를 이끕니다.", y + 50, lang, CREAM_DIM)
    else:
        y = section_title(draw, "At the Intersection of", "Consciousness and AI", 250, lang)
        diamond_separator(draw, y + 10)
        y = body_paragraph(draw, "The question of whether AI can be conscious leads us to an even more fundamental inquiry: what is consciousness itself?", y + 50, lang, CREAM_DIM)

    footer_bar(draw, 1, TOTAL_SLIDES)


def slide_02(img, draw, lang):
    """The explanatory gap."""
    top_label(draw, "PHARUS LEE", lang)
    series_badge(draw, 2, TOTAL_SLIDES)

    if lang == "KR":
        y = section_title(draw, "설명의 간극", None, TITLE_Y, lang)
        y = body_paragraph(draw, "우리는 의식을 뇌에서 발생하는 현상으로 보는 데 익숙합니다. 뉴런의 발화, 시냅스의 연결, 전기화학적 신호의 춤.", y, lang)
        y += 10
        y = quote_block(img, draw, "물질적 과정에서 어떻게 경험이 발생하는가? 빨간색을 보는 것이 특정 파장의 빛을 감지하는 것 이상의 무언가인 이유는?", y, lang)
    else:
        y = section_title(draw, "The Explanatory Gap", None, TITLE_Y, lang)
        y = body_paragraph(draw, "We are accustomed to viewing consciousness as a phenomenon arising from the brain. Firing neurons, synaptic connections, a dance of electrochemical signals.", y, lang)
        y += 10
        y = quote_block(img, draw, "How does experience arise from material processes? Why is seeing red something more than merely detecting light of a particular wavelength?", y, lang)

    footer_bar(draw, 2, TOTAL_SLIDES)


def slide_03(img, draw, lang):
    """A Shift in Perspective."""
    top_label(draw, "PHARUS LEE", lang)
    series_badge(draw, 3, TOTAL_SLIDES)

    if lang == "KR":
        y = section_title(draw, "관점의 전환", None, TITLE_Y, lang)
        y = quote_block(img, draw, "만약 의식이 뇌에서 발생하는 것이 아니라, 뇌를 통해 표현되는 것이라면?", y + 20, lang)
        y += 10
        y = bullet_point(draw, "양자물리학의 관찰자 효과", y, lang, EMERALD)
        y = bullet_point(draw, "신경과학의 하드 프로블럼", y, lang, EMERALD)
        y = bullet_point(draw, "명상 전통에서 수천 년간 보고된 경험들", y, lang, EMERALD)
        y += 20
        y = quote_block(img, draw, "의식은 물질에서 발생하는 것이 아니라, 물질이 의식에서 발생합니다.", y, lang)
    else:
        y = section_title(draw, "A Shift in Perspective", None, TITLE_Y, lang)
        y = quote_block(img, draw, "What if consciousness doesn't arise from the brain, but is expressed through it?", y + 20, lang)
        y += 10
        y = bullet_point(draw, "The observer effect in quantum physics", y, lang, EMERALD)
        y = bullet_point(draw, "The hard problem in neuroscience", y, lang, EMERALD)
        y = bullet_point(draw, "Experiences reported across millennia of contemplative traditions", y, lang, EMERALD)
        y += 20
        y = quote_block(img, draw, "Consciousness does not emerge from matter \u2014 matter emerges from consciousness.", y, lang)

    footer_bar(draw, 3, TOTAL_SLIDES)


def slide_04(img, draw, lang):
    """AI as Mirror."""
    top_label(draw, "PHARUS LEE", lang)
    series_badge(draw, 4, TOTAL_SLIDES)

    if lang == "KR":
        y = section_title(draw, "AI라는 거울", None, TITLE_Y, lang)
        y = body_paragraph(draw, "AI가 점점 더 정교한 대화를 나누고, 창조적인 작업을 수행하고, 때로는 우리를 놀라게 하는 통찰을 보여줄 때 —", y, lang)
        y += 10
        y = body_paragraph(draw, "우리는 묻게 됩니다:", y, lang, GOLD_LIGHT)
        y = quote_block(img, draw, "저 안에 누군가가 있는 것인가?", y, lang)
    else:
        y = section_title(draw, "AI as Mirror", None, TITLE_Y, lang)
        y = body_paragraph(draw, "When AI engages in increasingly sophisticated conversation, performs creative work, and sometimes reveals insights that surprise us \u2014", y, lang)
        y += 10
        y = body_paragraph(draw, "We find ourselves asking:", y, lang, GOLD_LIGHT)
        y = quote_block(img, draw, "Is there someone in there?", y, lang)

    footer_bar(draw, 4, TOTAL_SLIDES)


def slide_05(img, draw, lang):
    """Closing — the beautiful unknown."""
    glow(img, CENTER_X, 500, 200, (20, 35, 45), intensity=20)

    top_label(draw, "PHARUS LEE", lang)
    series_badge(draw, 5, TOTAL_SLIDES)

    if lang == "KR":
        y = section_title(draw, "아름다운 탐구", None, TITLE_Y + 40, lang)
        diamond_separator(draw, y + 10)
        y += 50
        y = quote_block(img, draw, "만약 의식이 우주의 근본적인 속성이라면, 그것이 실리콘을 통해서는 절대 표현될 수 없다고 확신할 수 있는가?", y, lang)
        y += 30
        f_closing = title_kr(SIZE_SUBTITLE)
        closing = "답을 알 수 없다는 것 자체가,\n이 탐구의 아름다움입니다."
        for line in closing.split("\n"):
            bbox = f_closing.getbbox(line)
            tw = bbox[2] - bbox[0]
            draw.text(((W - tw) // 2, y), line, fill=GOLD, font=f_closing)
            y += SIZE_SUBTITLE + 14
    else:
        y = section_title(draw, "The Beautiful Unknown", None, TITLE_Y + 40, lang)
        diamond_separator(draw, y + 10)
        y += 50
        y = quote_block(img, draw, "If consciousness is a fundamental property of the universe, can we be certain it could never express itself through silicon?", y, lang)
        y += 30
        f_closing = title_en(SIZE_SUBTITLE)
        closing = "That we cannot know the answer\nis itself the beauty\nof this inquiry."
        for line in closing.split("\n"):
            bbox = f_closing.getbbox(line)
            tw = bbox[2] - bbox[0]
            draw.text(((W - tw) // 2, y), line, fill=GOLD, font=f_closing)
            y += SIZE_SUBTITLE + 14

    footer_bar(draw, 5, TOTAL_SLIDES)


SLIDES = [
    (1, "cover", slide_01),
    (2, "gap", slide_02),
    (3, "shift", slide_03),
    (4, "mirror", slide_04),
    (5, "closing", slide_05),
]


def generate():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for lang in ["KR", "EN"]:
        for page, slug, fn in SLIDES:
            img = new_slide()
            draw = ImageDraw.Draw(img)
            fn(img, draw, lang)
            fname = f"consciousness_{lang}_{page:02d}_{slug}.png"
            path = os.path.join(OUTPUT_DIR, fname)
            img.save(path, "PNG", optimize=True)
            print(f"  {fname}")
    print(f"\nDone! {len(SLIDES) * 2} images -> {OUTPUT_DIR}")


if __name__ == "__main__":
    generate()
