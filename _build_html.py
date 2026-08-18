#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把 skill-intros/ 下的 56 篇 .md 介绍，连同已生成的小黑手绘配图，
打包成同目录可直接打开/部署的静态 HTML：
  - index.html           分类导航首页
  - <项目名>.html        每篇 md 同名的 html
  - style.css            统一阅读样式
  - assets/<项目>/01.png 已生成的 112 张图，原地复用，不移动
图片路径做大小写不敏感匹配，便于后续部署到 Linux 服务器 / EdgeOne Pages。
"""
import os, re, html, io
import markdown

BASE = os.path.dirname(os.path.abspath(__file__))
README = os.path.join(BASE, "README.md")
ASSETS = os.path.join(BASE, "assets")

# ---------- 解析 README 的 7 大类结构 ----------
def parse_readme(path):
    cats = []          # [(clean_name, [(title, file, desc), ...]), ...]
    flat = []          # [(title, file, desc, cat_name), ...]
    cur = None
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            m = re.match(r"^##\s+(.+)$", line)
            if m:
                raw = m.group(1)
                # 去掉 "一、" 前缀 与 "（8 篇）" 后缀
                name = re.sub(r"^[一二三四五六七八九十]+、", "", raw)
                name = re.sub(r"\s*[（(]\d+\s*篇[）)]", "", name).strip()
                cur = (name, [])
                cats.append(cur)
                continue
            # 列表项: - [标题](file.md) — 说明
            m = re.match(r"^\s*-\s*\[([^\]]+)\]\(([^)]+\.md)\)\s*[—-]\s*(.+)$", line)
            if m and cur is not None:
                title, file, desc = m.group(1), m.group(2), m.group(3)
                base = os.path.splitext(os.path.basename(file))[0]
                cur[1].append((title, base, desc))
                flat.append((title, base, desc, cur[0]))
    return cats, flat

# ---------- assets 目录大小写不敏感匹配 ----------
_assets_cache = None
def find_asset_dir(base):
    global _assets_cache
    if _assets_cache is None:
        _assets_cache = {d.lower(): d for d in os.listdir(ASSETS)
                         if os.path.isdir(os.path.join(ASSETS, d))}
    return _assets_cache.get(base.lower())

def thumb_src(base):
    real = find_asset_dir(base)
    if not real:
        return None
    p = os.path.join(ASSETS, real, "01.png")
    return f"assets/{real}/01.png" if os.path.exists(p) else None

# ---------- markdown -> html ----------
MD = markdown.Markdown(extensions=["fenced_code", "tables", "sane_lists"])
def md_to_html(text):
    MD.reset()
    return MD.convert(text)

def split_title(body):
    lines = body.splitlines()
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines) and lines[i].startswith("# "):
        title = lines[i][2:].strip()
        rest = "\n".join(lines[i+1:])
        return title, rest
    return None, body

# ---------- 模板 ----------
PAGE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<article class="post">
  <nav class="crumbs"><a href="index.html">&larr; 全部项目</a> &middot; {cat}</nav>
  <header class="post-head"><h1>{title}</h1></header>
  <div class="content">
{body}
  </div>
  <footer class="pager">
    <span class="prev">{prev}</span>
    <span class="next">{next}</span>
  </footer>
  <p class="back"><a href="index.html">&larr; 返回目录</a></p>
</article>
</body>
</html>
"""

INDEX = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AI 技能项目集合 · 白话介绍</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="hero">
  <h1>AI 技能项目集合 &middot; 白话介绍</h1>
  <p class="sub">56 个项目的通俗介绍，每篇配「小黑手绘」插图。点开任意一篇，看看它能帮你解决什么问题。</p>
  <p class="meta">共 {n} 篇 &middot; {cats} 大分类</p>
</header>
<main class="cats">
{cards}
</main>
<footer class="foot">本地静态站点 &middot; 由 Markdown 自动生成 &middot; 图片沿用已生成的小黑手绘插图</footer>
</body>
</html>
"""

CARD = """  <section class="cat">
    <h2>{cat}</h2>
    <div class="grid">
{cards}
    </div>
  </section>
"""

ITEM = """      <a class="card" href="{file}.html">
        {img}
        <div class="card-body">
          <h3>{title}</h3>
          <p>{desc}</p>
        </div>
      </a>"""

# ---------- 主流程 ----------
def main():
    cats, flat = parse_readme(README)
    n = len(flat)
    print(f"解析到 {n} 篇文章 / {len(cats)} 个分类")

    # 单篇 html
    for idx, (title, base, desc, cat) in enumerate(flat):
        md_path = os.path.join(BASE, base + ".md")
        if not os.path.exists(md_path):
            print(f"  [跳过] 找不到 {md_path}")
            continue
        with open(md_path, encoding="utf-8") as f:
            raw = f.read()
        h1, body = split_title(raw)
        disp_title = h1 or title
        body_html = md_to_html(body)

        prev_html = next_html = ""
        if idx > 0:
            pt, pb, _, _ = flat[idx-1]
            prev_html = f'<a href="{pb}.html">&larr; {html.escape(pt)}</a>'
        if idx < n-1:
            nt, nb, _, _ = flat[idx+1]
            next_html = f'<a href="{nb}.html">{html.escape(nt)} &rarr;</a>'

        out = PAGE.format(title=html.escape(disp_title), cat=html.escape(cat),
                          body=body_html, prev=prev_html, next=next_html)
        with open(os.path.join(BASE, base + ".html"), "w", encoding="utf-8") as f:
            f.write(out)

    # 首页
    cards_blocks = []
    for cat_name, items in cats:
        item_html = ""
        for (title, base, desc) in items:
            ts = thumb_src(base)
            img = f'<img class="thumb" loading="lazy" src="{ts}" alt="{html.escape(title)}">' if ts else ""
            item_html += ITEM.format(file=base, img=img,
                                     title=html.escape(title), desc=html.escape(desc))
        cards_blocks.append(CARD.format(cat=html.escape(cat_name), cards=item_html))
    index_html = INDEX.format(n=n, cats=len(cats), cards="\n".join(cards_blocks))
    with open(os.path.join(BASE, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)

    print(f"生成完成：index.html + {n} 篇 .html")

if __name__ == "__main__":
    main()
