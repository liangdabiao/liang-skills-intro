#!/usr/bin/env python3
"""从 _covers_*.json 读取并打印某个 slug 的完整生图提示词。

用法:
    python cover_prompt.py <slug> [--prefix R1A]
"""
import argparse, json, os, glob

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


def load(base="assets"):
    jobs = {}
    for f in glob.glob(os.path.join(base, "_covers_*.json")):
        for j in json.load(open(f, encoding="utf-8")):
            jobs[j["slug"]] = j
    return jobs


def build(j, prefix=""):
    head = (prefix + ". ") if prefix else ""
    return (
        head + "Generate one standalone 16:9 horizontal Chinese article illustration.\n"
        + VISUAL_DNA + "\n" + XH + "\n"
        + f"Theme: {j['theme']}\n"
        + f"Structure type: {j['structure']}\n"
        + f"Core idea: {j['idea']}\n"
        + f"Composition: {j['composition']}\n"
        + f"Suggested elements: {j['elements']}\n"
        + f"Chinese handwritten labels: {j['labels']}\n"
        + f"Color use: {j['color']}\n"
        + CONSTRAINTS + "\n"
    )


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--prefix", default="")
    a = ap.parse_args()
    jobs = load()
    if a.slug not in jobs:
        raise SystemExit(f"slug not found: {a.slug}\navailable: {sorted(jobs)}")
    print(build(jobs[a.slug], a.prefix))
