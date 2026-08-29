#!/usr/bin/env python3
"""skill-intros 静态站点构建器。

做三件事：
1. md → html：把每篇 <slug>.md 转成 <slug>.html
   —— 自动剔除「## 闲鱼接单文案」整段（该段只留在 markdown 源里，不进网页）
2. 重建 index.html：按分类输出卡片网格 + 更新篇数
3. 重写 pager：按 index.html 的扁平顺序，给每篇文章补 prev / next

新增 skill 时：把 slug 和分类写进下面的 NEW_SKILLS，跑一次即可。
已有文章的顺序从现有 index.html 解析，不会被打乱。

用法：
    python build_site.py            # 构建全站
    python build_site.py --dry-run  # 只看将要做什么，不写文件
"""
import re
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).parent.resolve()

# 新增 skill 在这里登记：slug -> 分类名。已存在的 slug 会被跳过（不重复插入）。
NEW_SKILLS = {
    "math-concept-film": "教育科普与数学类",
    "ecom-video-seedance-prompt": "电商与广告类",
    "glm-5.3-flash-vision-rag": "研究与智能体框架类",
    "glm-5.3-flash-vision-video-rag": "研究与智能体框架类",
    "glm-ecom-video-seedance-prompt": "电商与广告类",
    # amazon-skill 聚合包拆出的 9 个子技能（紧贴聚合篇之后分组）
    "amazon-analyse": "电商与广告类",
    "amazon-listing-builder": "电商与广告类",
    "category-selection": "电商与广告类",
    "keyword-research": "电商与广告类",
    "product-research": "电商与广告类",
    "review-analysis": "电商与广告类",
    "sellersprite-amazon-research": "电商与广告类",
    "sif-amazon-research": "电商与广告类",
    "xiyou-insight": "电商与广告类",
}

# 新增子技能希望紧贴在哪个已有 slug 之后（用于聚合包分组）；
# 不指定则追加到分类末尾。
AFTER = {
    "amazon-analyse": "amazon-skill",
    "amazon-listing-builder": "amazon-skill",
    "category-selection": "amazon-skill",
    "keyword-research": "amazon-skill",
    "product-research": "amazon-skill",
    "review-analysis": "amazon-skill",
    "sellersprite-amazon-research": "amazon-skill",
    "sif-amazon-research": "amazon-skill",
    "xiyou-insight": "amazon-skill",
}

# 从 markdown 正文里切掉这一节（含之后所有内容）
CUT_MARKER = "## 闲鱼接单文案"


def parse_index() -> tuple[list[tuple[str, list[str]]], dict[str, str]]:
    """解析现有 index.html，返回 [(分类, [slug...]), ...] 和 {slug: 短标题}。"""
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    cats: list[tuple[str, list[str]]] = []
    titles: dict[str, str] = {}

    sections = re.split(r'<section class="cat">', html)[1:]
    for sec in sections:
        m = re.search(r"<h2>([^<]+)</h2>", sec)
        if not m:
            continue
        cat = m.group(1)
        slugs: list[str] = []
        for card in re.findall(r'<a class="card" href="([^"]+\.html)"', sec):
            slugs.append(card[:-5])
        cats.append((cat, slugs))

    # 卡片里的短标题（用于 pager 文案）
    for slug, title in re.findall(
        r'<a class="card" href="([^"]+\.html)">.*?<h3>([^<]+)</h3>', html, re.S
    ):
        titles[slug[:-5]] = title
    return cats, titles


def add_new_skills(cats: list[tuple[str, list[str]]]) -> list[tuple[str, list[str]]]:
    """把 NEW_SKILLS 追加到对应分类（已存在的跳过），并按 AFTER 紧贴锚点重排。"""
    for slug, cat in NEW_SKILLS.items():
        for i, (c, slugs) in enumerate(cats):
            if c == cat:
                if slug not in slugs:
                    slugs.append(slug)
                    print(f"  + 新增卡片 {slug} → {cat}")
                break
        else:
            cats.append((cat, [slug]))
            print(f"  + 新建分类 {cat} → {slug}")
    # 按 AFTER 把子技能紧贴锚点之后（聚合包分组），组内顺序与 NEW_SKILLS 一致
    from collections import defaultdict

    groups: dict[str, list[str]] = defaultdict(list)
    for slug, anchor in AFTER.items():
        groups[anchor].append(slug)
    for anchor, group in groups.items():
        for _, slugs in cats:
            if anchor in slugs:
                ordered = [s for s in NEW_SKILLS if s in group]
                for s in ordered:
                    if s in slugs:
                        slugs.remove(s)
                j = slugs.index(anchor)
                for s in reversed(ordered):
                    slugs.insert(j + 1, s)
                break
    return cats


def md_title(slug: str) -> str:
    """取 markdown 里的完整 H1 标题。"""
    raw = (ROOT / f"{slug}.md").read_text(encoding="utf-8")
    for line in raw.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError(f"{slug}.md 缺少 H1 标题")


def short_title(full: str) -> str:
    """去掉「—— xxx 介绍」后缀，得到卡片/pager 用的短标题。"""
    return re.sub(r"\s*——.*$", "", full).strip()


def md_to_body(slug: str) -> str:
    """markdown 正文 → html 片段（剔除闲鱼接单文案段）。"""
    raw = (ROOT / f"{slug}.md").read_text(encoding="utf-8")

    # 1. 去掉 H1（网页里由 <h1> 单独渲染）
    raw = re.sub(r"^# .*$\n?", "", raw, count=1, flags=re.M)

    # 2. 切掉闲鱼接单文案整段
    if CUT_MARKER in raw:
        raw = raw.split(CUT_MARKER)[0].rstrip()

    return markdown.markdown(raw, extensions=["tables", "sane_lists"])


def render_post(slug: str, cat: str, full: str, body: str,
                prev: tuple[str, str] | None, nxt: tuple[str, str] | None) -> str:
    prev_html = (
        f'<a href="{prev[0]}.html">&larr; {prev[1]}</a>' if prev else ""
    )
    next_html = (
        f'<a href="{nxt[0]}.html">{nxt[1]} &rarr;</a>' if nxt else ""
    )
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full}</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<article class="post">
  <nav class="crumbs"><a href="index.html">&larr; 全部文章</a> &middot; {cat}</nav>
  <header class="post-head"><h1>{full}</h1></header>
  <div class="content">
{body}
  </div>
  <footer class="pager">
    <span class="prev">{prev_html}</span>
    <span class="next">{next_html}</span>
  </footer>
  <p class="back"><a href="index.html">&larr; 返回目录</a></p>
</article>
</body>
</html>
"""


def render_index(cats: list[tuple[str, list[str]]], titles: dict[str, str]) -> str:
    total = sum(len(s) for _, s in cats)
    parts = [
        "<!DOCTYPE html>",
        '<html lang="zh-CN">',
        "<head>",
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        "<title>AI 技能项目集合 · 白话介绍</title>",
        '<link rel="stylesheet" href="style.css">',
        "</head>",
        "<body>",
        '<header class="hero">',
        "  <h1>AI 技能项目集合 · 白话介绍</h1>",
        '  <p class="sub">点开任意一篇，看看它能帮你解决什么问题。</p>',
        f'  <p class="meta">共 {total} 篇 &middot; {len(cats)} 个分类 &middot; '
        f'<a href="README.html">项目说明</a></p>',
        "</header>",
        '<main class="cats">',
    ]
    for cat, slugs in cats:
        parts.append('  <section class="cat">')
        parts.append(f"    <h2>{cat}</h2>")
        parts.append('    <div class="grid">')
        for slug in slugs:
            t = titles.get(slug, short_title(md_title(slug)))
            thumb = f"assets/{slug}/01.png"
            parts.append(f'      <a class="card" href="{slug}.html">')
            parts.append(
                f'        <img class="thumb" loading="lazy" src="{thumb}" '
                f'alt="{t}">'
            )
            parts.append('        <div class="card-body">')
            parts.append(f"          <h3>{t}</h3>")
            parts.append(f"          <p>{slug}</p>")
            parts.append("        </div>")
            parts.append("      </a>")
        parts.append("    </div>")
        parts.append("  </section>")
        parts.append("")
    parts += [
        "</main>",
        '<footer class="foot">本地静态站点 &middot; 由 Markdown 自动生成</footer>',
        "</body>",
        "</html>",
        "",
    ]
    return "\n".join(parts)


_CN = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]

README_INTRO = """# 项目集合 · 通俗易懂介绍索引

本目录收录了 `E:\\all-skill-t0` 这个 AI 技能项目集合中 **{n} 个项目** 的入门介绍，每篇都用大白话讲清楚"它能帮人解决什么问题、怎么用、谁适合用、以及它的边界在哪"。

> 说明：这批文章是面向"不懂技术的普通人"写的，刻意避免了术语堆砌。凡是"给做 AI 工具的人用的技能（skill）"，文中都明确标注了它不是双击打开的 App。

> **配图状态**：全部 {n} 篇文章均已配齐「小黑手绘」风格插图（共 {imgs} 张），图片存放在 `assets/<项目名>/01.png`、`02.png`，严格遵循 `ian-xiaohei-illustrations` 技能的视觉 DNA（纯白背景、黑色手绘线稿、小黑 IP 作为动作主体、少量红/橙/蓝批注）。

> **完整分类索引**：见 [index.html](index.html)。本文件是该索引的文本镜像，由 `build_site.py` 自动同步生成，请勿手改目录部分。

---
"""


def _count_images() -> int:
    return sum(1 for p in (ROOT / "assets").rglob("*.png") if "_raw" not in p.parts)


def render_readme_md(cats: list[tuple[str, list[str]]], titles: dict[str, str]) -> str:
    """生成与 index.html 一致的文本镜像 README.md（保留 curated 顶部说明）。"""
    n = sum(len(s) for _, s in cats)
    imgs = _count_images()
    lines = [README_INTRO.format(n=n, imgs=imgs)]
    for i, (cat, slugs) in enumerate(cats, 1):
        cn = _CN[i] if i < len(_CN) else str(i)
        lines.append(f"## {cn}、{cat}（{len(slugs)} 篇）")
        lines.append("")
        for slug in slugs:
            t = titles.get(slug, short_title(md_title(slug)))
            lines.append(f"- [{t}]({slug}.md) — {slug}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_readme_html() -> str:
    """从 README.md 生成独立的 README.html 页面（剔除 H1，由页面标题渲染）。"""
    raw = (ROOT / "README.md").read_text(encoding="utf-8")
    raw = re.sub(r"^# .*$\n?", "", raw, count=1, flags=re.M)
    body = markdown.markdown(raw, extensions=["tables", "sane_lists"])
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>项目说明 · AI 技能集合白话介绍</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<article class="post">
  <nav class="crumbs"><a href="index.html">&larr; 全部文章</a> &middot; 项目说明</nav>
  <header class="post-head"><h1>项目集合 · 通俗易懂介绍索引</h1></header>
  <div class="content">
{body}
  </div>
  <p class="back"><a href="index.html">&larr; 返回目录</a></p>
</article>
</body>
</html>
"""


def main() -> None:
    dry = "--dry-run" in sys.argv

    cats, titles = parse_index()
    print(f"[1/3] 解析现有 index.html：{len(cats)} 个分类")
    cats = add_new_skills(cats)

    # 扁平顺序（pager 依据）
    order: list[str] = [s for _, slugs in cats for s in slugs]
    print(f"[2/3] 扁平顺序共 {len(order)} 篇，生成 HTML...")

    missing = [s for s in order if not (ROOT / f"{s}.md").exists()]
    if missing:
        print(f"  ⚠️ 以下 slug 缺 markdown，已跳过：{missing}")
    order = [s for s in order if s not in missing]

    # pager 会引用前后文章的标题，必须先全量解析，不能边遍历边补
    for slug in order:
        titles.setdefault(slug, short_title(md_title(slug)))

    for i, slug in enumerate(order):
        cat = next(c for c, slugs in cats if slug in slugs)
        full = md_title(slug)
        body = md_to_body(slug)
        prev = (order[i - 1], titles[order[i - 1]]) if i > 0 else None
        nxt = (order[i + 1], titles[order[i + 1]]) if i < len(order) - 1 else None
        html = render_post(slug, cat, full, body, prev, nxt)
        if not dry:
            (ROOT / f"{slug}.html").write_text(html, encoding="utf-8")
        print(f"  {'[dry] ' if dry else ''}{slug}.html ({cat})")

    print("[3/3] 重建 index.html...")
    idx = render_index(cats, titles)
    if not dry:
        (ROOT / "index.html").write_text(idx, encoding="utf-8")
    print(f"完成：共 {len(order)} 篇 / {len(cats)} 个分类" + ("（dry-run，未写文件）" if dry else ""))

    print("[4/4] 同步 README.md / README.html...")
    readme_md = render_readme_md(cats, titles)
    if not dry:
        (ROOT / "README.md").write_text(readme_md, encoding="utf-8")
        (ROOT / "README.html").write_text(render_readme_html(), encoding="utf-8")
    print(f"   README.md（{len(order)} 篇镜像） + README.html" + ("（dry-run，未写文件）" if dry else ""))


if __name__ == "__main__":
    main()
