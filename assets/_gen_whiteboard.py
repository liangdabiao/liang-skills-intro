#!/usr/bin/env python3
"""whiteboard-explainer 2 张小黑手绘配图（复用 gen_image.py + 统一 Visual DNA）"""
import subprocess, sys

PY = "C:/Users/49707/.workbuddy/binaries/python/versions/3.13.12/python.exe"
GEN = "E:/all-skill-t0/skill-intros/assets/gen_image.py"
OUT_BASE = "E:/all-skill-t0/skill-intros/assets"

VISUAL_DNA = (
    "Visual DNA: Pure white background. Minimalist black hand-drawn line art. "
    "Slightly wobbly pen lines. Lots of empty white space. Sparse red/orange/blue "
    "handwritten Chinese annotations. Clean absurd product-sketch feeling. No gradients, "
    "shadows, paper texture, complex background, commercial vector style, PPT infographic, "
    "cute mascot, children's illustration, realistic UI."
)
XH = (
    "Recurring IP character required: 小黑, a small solid-black absurd creature with white "
    "dot eyes, tiny thin legs, blank serious expression, slightly uneven hand-drawn body "
    "shape. 小黑 must perform the core conceptual action, not decorate the scene. Serious, "
    "deadpan, slightly bizarre, not cute."
)
CONSTRAINTS = (
    "Constraints: One image explains only one core structure. Main subject 40%-60%. "
    "Preserve at least 35% blank white space. At most 5-8 short Chinese labels. No title "
    "in top-left corner. Not a formal diagram. Invent a fresh visual metaphor. Clear but "
    "not instructional, interesting but not childish, strange but clean."
)

def prompt(theme, structure, idea, composition, elements, labels, coloruse):
    return (
        "Generate one standalone 16:9 horizontal Chinese article illustration.\n"
        + VISUAL_DNA + "\n" + XH + "\n"
        f"Theme: {theme}\n"
        f"Structure type: {structure}\n"
        f"Core idea: {idea}\n"
        f"Composition: {composition}\n"
        f"Suggested elements: {elements}\n"
        f"Chinese handwritten labels: {labels}\n"
        f"Color use: {coloruse}\n"
        + CONSTRAINTS + "\n"
    )

JOBS = [
    ("whiteboard-explainer", "01", prompt(
        "讲稿自动变成讲到哪画到哪的白板手绘动画",
        "系统局部",
        "小黑边讲边画，笔画跟着语音长出来",
        "小黑站在一块大白板前，手持一支马克笔正在画一个太阳，笔尖伸出一根橙色电线连到旁边一个老式麦克风；白板上已画好的月亮和箭头是完成的黑色线稿，正在画的太阳只有半圈；麦克风上贴一行小字标注语音进度。",
        "小黑执笔画白板 / 半完成的太阳 / 已完成的月亮线稿 / 连着麦克风的电线 / 语音进度小字",
        "讲到哪 / 画到哪 / 正在画 / 音画同步",
        "Black for main line art and 小黑. Orange for the voice wire and in-progress stroke. Red only for the key sync label. Blue only for secondary notes."
    )),
    ("whiteboard-explainer", "02", prompt(
        "本地渲染零成本还能秒级重渲白板动画",
        "前后对比",
        "改一句稿子，一秒重出整片",
        "画面左半边一台冒着热气的旧云服务器，上面贴着付费账单小票，一叠钞票压在下面；右半边小黑家里的一台小方盒电脑，屏幕上显示一段白板动画波形，小黑按着旁边一个红色重渲按钮，白板图立刻重新长出来；中间一个大箭头从左指向右。",
        "左侧付费云服务器+账单 / 右侧小黑的本地方盒电脑 / 红色重渲按钮 / 中央指向右的大箭头",
        "零成本 / 秒级 / 重渲 / 本地跑",
        "Black for main line art and 小黑. Orange for the center flow arrow. Red only for the re-render button and bill. Blue only for secondary notes."
    )),
]

fail = 0
for project, idx, p in JOBS:
    out = f"{OUT_BASE}/{project}/{idx}.png"
    print(f"== {project} {idx} ->", out, flush=True)
    r = subprocess.run([PY, GEN, "--prompt", p, "--out", out])
    if r.returncode != 0:
        fail += 1
        print(f"[FAIL] {project} {idx}", flush=True)
sys.exit(1 if fail else 0)
