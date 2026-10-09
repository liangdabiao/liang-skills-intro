#!/usr/bin/env python3
"""directing-xiaohei-videos 2 张小黑手绘配图（复用 gen_image.py + 统一 Visual DNA）"""
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
    ("directing-xiaohei-videos", "01", prompt(
        "AI 导演指挥小黑在白画布上拍短视频",
        "系统局部",
        "一个导演喇叭指挥小黑演完整条片子",
        "画面左上角伸出一个大喇叭（带小旗），喇叭口对准下方一块立着的白色大画板；小黑正站在画板上表演——双手捧着一只摔裂的碗，水滴从裂缝漏出；画板旁立一块小场记板；远处一条胶片带从画板边缘延伸出去卷成卷。",
        "导演大喇叭 / 立式白画板 / 捧裂碗的小黑 / 场记板 / 卷起的胶片",
        "第3场 / 开拍 / 漏了 / 过",
        "Black for main line art and 小黑. Orange for the megaphone and film strip. Red only for the leaking water highlight. Blue only for the clapperboard notes."
    )),
    ("directing-xiaohei-videos", "02", prompt(
        "一篇文章变成一条带旁白字幕的成片",
        "前后对比",
        "左边一页文章，右边一条完整片子",
        "画面左侧一页写满字的纸竖着放；一个大箭头指向右侧；右侧一部竖着的手机屏幕里，小黑正在跑动，屏幕下方一条字幕条亮着，旁边一个音符符号和一条声波线；小黑在屏幕里比在纸上的文字更有生命力。",
        "左侧文章纸页 / 中央大箭头 / 手机竖屏里的小黑 / 字幕条 / 声波音符",
        "文章进 / 成片出 / 0元",
        "Black for main line art and 小黑. Orange for the center arrow. Red only for the zero-cost stamp. Blue only for subtitle bar notes."
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
