"""사진 위에 글자를 얹어 1200x630 썸네일을 만든다.
사용: python tools/make_thumb.py 사진.jpg "제목" "부제" assets/og-출력.png
"""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageOps
src, title, sub, out = sys.argv[1:5]
W, H = 1200, 630
img = ImageOps.fit(Image.open(src).convert("RGB"), (W, H), Image.LANCZOS)
ov = Image.new("RGBA", (W, H))
d = ImageDraw.Draw(ov)
for y in range(H):  # 아래로 갈수록 어두워지는 그라데이션
    a = int(215 * max(0, (y - H * 0.18) / (H * 0.82)) ** 1.2)
    d.line([(0, y), (W, y)], fill=(8, 10, 16, a))
img = Image.alpha_composite(img.convert("RGBA"), ov)
d = ImageDraw.Draw(img)
B, R = "C:/Windows/Fonts/malgunbd.ttf", "C:/Windows/Fonts/malgun.ttf"
d.ellipse([70, 60, 106, 96], fill=(229, 35, 58))
d.text((120, 56), "우리 블로그", font=ImageFont.truetype(B, 34), fill="white")
f = ImageFont.truetype(B, 70)
lines, cur = [], ""
for w in title.split():  # 단어 단위 줄바꿈
    t = (cur + " " + w).strip()
    if cur and d.textlength(t, font=f) > W - 140:
        lines.append(cur); cur = w
    else:
        cur = t
lines.append(cur)
y = H - 70 - 44 - len(lines) * 88
for ln in lines:
    d.text((70, y), ln, font=f, fill="white"); y += 88
d.rounded_rectangle([70, y + 6, 190, y + 14], radius=4, fill=(255, 122, 89))
d.text((70, y + 28), sub, font=ImageFont.truetype(R, 30), fill=(235, 235, 235))
img.convert("RGB").save(out, optimize=True)
