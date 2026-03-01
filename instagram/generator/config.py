"""Pharus Lee — Instagram carousel design system."""

# Canvas
W, H = 1080, 1350

# Colors — Charcoal + Antique Gold + Emerald
BG_DARK = (17, 18, 21)        # #111215  Charcoal black
BG_MID = (28, 30, 35)         # #1C1E23  Slightly lighter
GOLD = (201, 168, 76)         # #C9A84C  Antique gold
GOLD_LIGHT = (228, 206, 140)  # #E4CE8C  Light gold
CREAM = (232, 220, 200)       # #E8DCC8  Warm cream (body text)
CREAM_DIM = (170, 160, 145)   # #AAA091  Muted cream
EMERALD = (45, 139, 111)      # #2D8B6F  Emerald green
EMERALD_DARK = (30, 80, 60)   # #1E503C  Dark emerald (cards)

# Layout zones (y positions)
TOP_Y = 55
TITLE_Y = 140
CONTENT_Y = 300
FOOTER_Y = 1100
BOTTOM_Y = 1260

# Content margins
MARGIN_L = 80
MARGIN_R = 80
CONTENT_W = W - MARGIN_L - MARGIN_R  # 920px usable
CENTER_X = W // 2

# Font sizes (mobile-first: 1080px → ~375px on phone)
SIZE_TITLE = 72
SIZE_SUBTITLE = 40
SIZE_BODY = 36
SIZE_BODY_BOLD = 38
SIZE_LABEL = 28
SIZE_TAG = 26
SIZE_QUOTE = 42

# Weight constants for variable fonts
LIGHT = 300
REGULAR = 400
MEDIUM = 500
SEMIBOLD = 600
BOLD = 700
