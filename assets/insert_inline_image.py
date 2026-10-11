#!/usr/bin/env python3
"""给指定文档在「第一段正文之后」插入一张正文插图（复用 01.png）。

同时处理 .md 与 .html 两端，保持与老文档一致的写法：
    md   : ![配图：<alt>](assets/<slug>/01.png)
    html : <p><img alt="配图：<alt>" src="assets/<slug>/01.png" /></p>

用法：
    python insert_inline_image.py --slugs assets/_covers_1.json assets/_covers_2.json
    python insert_inline_image.py --slug a --slug b   # 精确指定
"""
import argparse, glob, json, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(ROOT)  # 脚本在 assets/ 下，项目根是上一层


def collect_slugs(files):
    out = []
    for f in files:
        for j in json.load(open(f, encoding="utf-8")):
            out.append(j["slug"])
    return out


def short_alt(md_title):
    """从 H1 标题里取一个简短的 alt 文案。"""
    t = md_title.strip()
    t = re.sub(r"^#\s*", "", t)
    # 去掉 “—— xxx 介绍” 之类的后缀
    t = re.split(r"\s*——\s*", t)[0]
    t = re.split(r"[?？!！。]", t)[0]
    return t.strip()[:30] or "正文配图"


def md_title_of(slug):
    p = os.path.join(ROOT, f"{slug}.md")
    if not os.path.exists(p):
        return ""
    with open(p, encoding="utf-8") as f:
        for line in f:
            if line.startswith("# "):
                return line
    return ""


def is_body_para(line):
    s = line.strip()
    if not s:
        return False
    if s.startswith("#") or s.startswith("---") or s.startswith(">") or s.startswith("!"):
        return False
    if s.startswith("代码仓库") or s.startswith("仓库") or s.startswith("```"):
        return False
    if s.startswith("http://") or s.startswith("https://"):
        return False
    return len(s) > 30


def patch_md(slug, alt):
    p = os.path.join(ROOT, f"{slug}.md")
    if not os.path.exists(p):
        return "no-md"
    txt = open(p, encoding="utf-8").read()
    if f"assets/{slug}/01.png" in txt:
        return "skip"

    lines = txt.split("\n")
    out, done = [], False
    for i, ln in enumerate(lines):
        out.append(ln)
        if not done and is_body_para(ln):
            out.append("")
            out.append(f"![配图：{alt}](assets/{slug}/01.png)")
            done = True
    if not done:
        return "no-anchor"
    open(p, "w", encoding="utf-8").write("\n".join(out))
    return "ok"


def patch_html(slug, alt):
    p = os.path.join(ROOT, f"{slug}.html")
    if not os.path.exists(p):
        return "no-html"
    txt = open(p, encoding="utf-8").read()
    if f"assets/{slug}/01.png" in txt:
        return "skip"

    lines = txt.split("\n")
    out, done = [], False
    for ln in lines:
        out.append(ln)
        if not done and ln.strip().startswith("<p>") and "<img" not in ln \
                and len(ln.strip()) > 40 and "<strong>" not in ln:
            out.append(f'<p><img alt="配图：{alt}" src="assets/{slug}/01.png" /></p>')
            done = True
    if not done:
        return "no-anchor"
    open(p, "w", encoding="utf-8").write("\n".join(out))
    return "ok"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", action="append", default=[])
    ap.add_argument("--covers", nargs="*", default=None)
    a = ap.parse_args()

    if a.slug:
        slugs = a.slug
    else:
        files = a.covers or sorted(glob.glob(os.path.join(ROOT, "assets", "_covers_*.json")))
        slugs = collect_slugs(files)

    print(f"[insert] {len(slugs)} slugs", flush=True)
    tally = {}
    problems = []
    for s in slugs:
        alt = short_alt(md_title_of(s) or s)
        r1 = patch_md(s, alt)
        r2 = patch_html(s, alt)
        key = f"md={r1} html={r2}"
        tally[key] = tally.get(key, 0) + 1
        if "ok" not in (r1, r2):
            problems.append((s, r1, r2))
        print(f"[{key}] {s}", flush=True)

    print("\n[summ]")
    for k, v in sorted(tally.items()):
        print(f"  {k}: {v}")
    if problems:
        print("[problems]")
        for s, r1, r2 in problems:
            print(f"  {s}: md={r1} html={r2}")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
