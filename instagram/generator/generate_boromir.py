"""Generate Instagram carousel for 'The Boromir Syndrome' essay."""
import os, sys
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(__file__))
from config import *
from primitives import *
from components import *
from fonts import *

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "boromir-syndrome")
TOTAL_SLIDES = 5


def slide_01(img, draw, lang):
    """Cover — Title + hook quote."""
    glow(img, CENTER_X, 400, 250, (40, 35, 20), intensity=25)
    glow(img, CENTER_X, 400, 120, (50, 42, 15), intensity=20)

    top_label(draw, "PHARUS LEE", lang)
    series_badge(draw, 1, TOTAL_SLIDES)

    if lang == "KR":
        y = section_title(draw, "보로미르 신드롬", "AI 시대의 절대반지", 250, lang)
    else:
        y = section_title(draw, "The Boromir Syndrome", "The One Ring of the AI Age", 250, lang)

    diamond_separator(draw, y + 20)

    if lang == "KR":
        quote = "\"이것은 선물입니다. 모르도르의 적에게 주어진 선물이란 말입니다.\""
    else:
        quote = "\"It is a gift. A gift to the foes of Mordor.\""
    quote_block(img, draw, quote, y + 60, lang)

    if lang == "KR":
        body_paragraph(draw, "절대반지를 사용해 곤도르를 지키겠다던 보로미르의 논리가, 2026년 펜타곤의 AI 정책에서 그대로 반복되고 있습니다.", 900, lang, CREAM_DIM)
    else:
        body_paragraph(draw, "Boromir's logic for wielding the One Ring to save Gondor is being repeated, almost word for word, in the Pentagon's 2026 AI policy.", 900, lang, CREAM_DIM)

    footer_bar(draw, 1, TOTAL_SLIDES)


def slide_02(img, draw, lang):
    """The Pentagon's Logic — parallel between Boromir and Pentagon."""
    top_label(draw, "PHARUS LEE", lang)
    series_badge(draw, 2, TOTAL_SLIDES)

    if lang == "KR":
        y = section_title(draw, "펜타곤의 논리", None, TITLE_Y, lang)
        y = body_paragraph(draw, "2026년 2월, 미국 국방장관 피트 헤그세스는 앤트로픽 CEO에게 최후통첩을 보냈습니다.", y, lang)
        y = quote_block(img, draw, "금요일 오후 5시 1분까지 모든 안전 장치를 해제하라. 그렇지 않으면 공급망 위험 기업으로 지정하겠다.", y, lang)
        y = body_paragraph(draw, "보로미르가 절대반지를 사용하자고 했듯, 펜타곤은 AI의 모든 안전 장치를 해제하자고 합니다.", y, lang, CREAM_DIM)
    else:
        y = section_title(draw, "The Pentagon's Logic", None, TITLE_Y, lang)
        y = body_paragraph(draw, "In February 2026, Defense Secretary Pete Hegseth delivered an ultimatum to Anthropic's CEO.", y, lang)
        y = quote_block(img, draw, "Remove all safety guardrails by 5:01 PM Friday, or be designated a supply chain risk.", y, lang)
        y = body_paragraph(draw, "Where Boromir proposed to wield the Ring, the Pentagon proposes to remove all guardrails from AI. Same logic, same conviction, same danger.", y, lang, CREAM_DIM)

    footer_bar(draw, 2, TOTAL_SLIDES)


def slide_03(img, draw, lang):
    """What the Ring Corrupts — the core insight."""
    top_label(draw, "PHARUS LEE", lang)
    series_badge(draw, 3, TOTAL_SLIDES)

    if lang == "KR":
        y = section_title(draw, "반지가 부패시키는 것", None, TITLE_Y, lang)
        y = body_paragraph(draw, "보로미르는 선한 사람입니다. 곤도르를 사랑하고 백성을 지키려 합니다.", y, lang)
        y = quote_block(img, draw, "절대반지의 진짜 위험은 악한 자를 유혹하는 것이 아니라, 선한 자의 선한 의도를 통해 작동한다는 것입니다.", y, lang)
        y = body_paragraph(draw, "대량 감시 기술도 마찬가지입니다. 테러리스트를 찾겠다는 목적으로 시작하지만, 도구가 존재하면 사용 범위는 끊임없이 확장됩니다.", y, lang, CREAM_DIM)
    else:
        y = section_title(draw, "What the Ring Corrupts", None, TITLE_Y, lang)
        y = body_paragraph(draw, "Boromir is a good man. He loves Gondor and wants to protect his people. There is no selfishness in his motives.", y, lang)
        y = quote_block(img, draw, "The true danger of the One Ring is not that it tempts the wicked, but that it operates through the good intentions of the virtuous.", y, lang)
        y = body_paragraph(draw, "Mass surveillance works the same way. It begins with finding terrorists, but once the tool exists, its scope expands relentlessly.", y, lang, CREAM_DIM)

    footer_bar(draw, 3, TOTAL_SLIDES)


def slide_04(img, draw, lang):
    """Faramir's Choice — the alternative."""
    top_label(draw, "PHARUS LEE", lang)
    series_badge(draw, 4, TOTAL_SLIDES)

    if lang == "KR":
        y = section_title(draw, "파라미르의 선택", None, TITLE_Y, lang)
        y = quote_block(img, draw, "\"길에 버려진 것을 주워도 가져가지 않겠소.\"", y + 20, lang)
        y = body_paragraph(draw, "파라미르가 반지를 거부한 것은 위협이 실재하지 않아서가 아닙니다.", y, lang)
        y = body_paragraph(draw, "그 힘을 사용하는 것 자체가, 지키려는 것을 파괴하는 길이라는 것을 이해했기 때문입니다.", y, lang, CREAM_DIM)
        y += 20
        y = numbered_item(draw, 1, "대규모 영장 없는 감시 거부", "미국 시민에 대한 무차별 감시", y, lang, EMERALD)
        y = numbered_item(draw, 2, "완전 자율 무기 거부", "인간의 개입 없는 표적 선택과 교전", y, lang, EMERALD)
    else:
        y = section_title(draw, "Faramir's Choice", None, TITLE_Y, lang)
        y = quote_block(img, draw, "\"I would not take this thing, if it lay by the highway.\"", y + 20, lang)
        y = body_paragraph(draw, "Faramir's refusal is not because the threat is unreal.", y, lang)
        y = body_paragraph(draw, "It is because he understands that wielding such power is itself the path to destroying what you seek to protect.", y, lang, CREAM_DIM)
        y += 20
        y = numbered_item(draw, 1, "No mass warrantless surveillance", "Of American citizens without due process", y, lang, EMERALD)
        y = numbered_item(draw, 2, "No fully autonomous weapons", "That select and engage targets without human oversight", y, lang, EMERALD)

    footer_bar(draw, 4, TOTAL_SLIDES)


def slide_05(img, draw, lang):
    """Closing question — will we be Boromir or Faramir?"""
    glow(img, CENTER_X, 500, 200, (40, 35, 20), intensity=20)

    top_label(draw, "PHARUS LEE", lang)
    series_badge(draw, 5, TOTAL_SLIDES)

    if lang == "KR":
        y = section_title(draw, "보로미르 신드롬", None, TITLE_Y + 40, lang)
        diamond_separator(draw, y + 10)
        y += 50
        y = bullet_point(draw, "위협이 실재하기 때문에 더욱 설득력 있는 유혹", y, lang, GOLD)
        y = bullet_point(draw, "위협의 실재성이 수단의 위험성을 정당화한다는 믿음", y, lang, GOLD)
        y = bullet_point(draw, "그 힘을 \"통제\"할 수 있다는 자기 확신", y, lang, GOLD)
        y += 20
        y = quote_block(img, draw, "반지를 사용하는 순간, 당신은 이미 사우론이 원하는 게임을 하고 있는 것이니까요.", y, lang)
        y += 10
        f_title = title_kr(SIZE_SUBTITLE) if lang == "KR" else title_en(SIZE_SUBTITLE)
        closing = "AI라는 절대반지 앞에서\n우리는 보로미르가 될 것인가,\n파라미르가 될 것인가." if lang == "KR" else "Before the One Ring of AI,\nwill we be Boromir,\nor will we be Faramir?"
        for line in closing.split("\n"):
            bbox = f_title.getbbox(line)
            tw = bbox[2] - bbox[0]
            draw.text(((W - tw) // 2, y), line, fill=GOLD, font=f_title)
            y += SIZE_SUBTITLE + 14
    else:
        y = section_title(draw, "The Boromir Syndrome", None, TITLE_Y + 40, lang)
        diamond_separator(draw, y + 10)
        y += 50
        y = bullet_point(draw, "A temptation made more persuasive by the reality of the threat", y, lang, GOLD)
        y = bullet_point(draw, "The belief that the reality of a threat justifies the danger of the means", y, lang, GOLD)
        y = bullet_point(draw, "The self-assurance that this power can be \"controlled\"", y, lang, GOLD)
        y += 20
        y = quote_block(img, draw, "The moment you use the Ring, you are already playing the game Sauron wants you to play.", y, lang)
        y += 10
        f_title = title_en(SIZE_SUBTITLE)
        closing = "Before the One Ring of AI,\nwill we be Boromir,\nor will we be Faramir?"
        for line in closing.split("\n"):
            bbox = f_title.getbbox(line)
            tw = bbox[2] - bbox[0]
            draw.text(((W - tw) // 2, y), line, fill=GOLD, font=f_title)
            y += SIZE_SUBTITLE + 14

    footer_bar(draw, 5, TOTAL_SLIDES)


# --- Generation ---

SLIDES = [
    (1, "cover", slide_01),
    (2, "pentagon", slide_02),
    (3, "corruption", slide_03),
    (4, "faramir", slide_04),
    (5, "closing", slide_05),
]


def generate():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for lang in ["KR", "EN"]:
        for page, slug, fn in SLIDES:
            img = new_slide()
            draw = ImageDraw.Draw(img)
            fn(img, draw, lang)
            fname = f"boromir_{lang}_{page:02d}_{slug}.png"
            path = os.path.join(OUTPUT_DIR, fname)
            img.save(path, "PNG", optimize=True)
            print(f"  {fname}")
    print(f"\nDone! {len(SLIDES) * 2} images → {OUTPUT_DIR}")


if __name__ == "__main__":
    generate()
