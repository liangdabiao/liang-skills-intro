"""Fill/validate the 代码仓库 line in every skill-intro markdown.

Usage:
  python repo_links.py fetch     # refresh the GitHub repo list cache for liangdabiao
  python repo_links.py fill      # insert links for articles whose file name matches a repo
  python repo_links.py check     # HTTP-probe every inserted link

Matching is exact on the normalized file name only; articles without a same-named
repo are left untouched (sub-skill folders inside aggregate repos are maintained in
SUBSKILL below, all verified to return HTTP 200).
"""
import glob
import io
import json
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

TOOLS = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.dirname(TOOLS)
CACHE = os.path.join(TOOLS, "repos_all.json")
OWNER = "liangdabiao"
SKIP = {"ALL-MERGED.md", "MISSING-DOCS.md", "README.md"}

# 文章名 -> 聚合仓库内的子技能目录（默认分支已逐个校验）
SUBSKILL = {
    "amazon-analyse": "amazon-sorftime-research-MCP-skill/tree/main/SKILLS/skills/amazon-analyse",
    "amazon-listing-builder": "amazon-sorftime-research-MCP-skill/tree/main/SKILLS/skills/amazon-listing-builder",
    "category-selection": "amazon-sorftime-research-MCP-skill/tree/main/SKILLS/skills/category-selection",
    "keyword-research": "amazon-sorftime-research-MCP-skill/tree/main/SKILLS/skills/keyword-research",
    "product-research": "amazon-sorftime-research-MCP-skill/tree/main/SKILLS/skills/product-research",
    "review-analysis": "amazon-sorftime-research-MCP-skill/tree/main/SKILLS/skills/review-analysis",
    "sellersprite-amazon-research": "amazon-sorftime-research-MCP-skill/tree/main/SKILLS/skills/sellersprite-amazon-research",
    "xiyou-insight": "amazon-sorftime-research-MCP-skill/tree/main/SKILLS/skills/xiyou-insight",
    "apiz-use": "apiz-skill/tree/main/skills/apiz-use",
    "brightdata-research": "Bright-Data-MCP-Claude-Skill-deep-research",
    "deep-research-agent": "deep-research-agent-skill",
    "exa-company-research": "exa-research-mcp-skill/tree/main/skills/company-research",
    "exa-foreign-trade-research": "exa-research-mcp-skill/tree/main/skills/foreign-trade-research",
    "geo-optimizer": "GEO-Content-Optimizer-Skill/tree/main/skills/geo-optimizer",
    "hyperframes-video-spec-builder": "hyperframes-fix/tree/main/skill/video-spec-builder",
    "tikhub-api-helper": "claudesdk-tikhub-chat/tree/main/.claude/skills/tikhub-api-helper",
    "luozhenyu-bookwriter": "liurun-bookwriter-skills/tree/main/SKILLS/skills/luozhenyu-bookwriter",
    "resume-matcher": "resume-matcher-skill",
}
for s in ("edu-analytic-geometry", "edu-chem-reaction", "edu-chem-tutorial", "edu-physics-3d",
          "edu-physics", "edu-plane-geometry", "edu-sci-viz", "edu-solid-geometry"):
    SUBSKILL[s] = f"edulab/tree/master/skills/{s}"

LINK = re.compile(r"^代码仓库：(\S+)\s*$", re.M)


def norm(s):
    return re.sub(r"[\s_\-\.\+]+", "", s.lower())


def load_repos():
    return json.load(open(CACHE, encoding="utf-8"))


def status(url):
    r = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}",
                        "--ssl-no-revoke", "-m", "25", "-L", url],
                       capture_output=True, text=True, errors="replace")
    return r.stdout.strip()


def set_link(path, url):
    lines = io.open(path, encoding="utf-8").read().split("\n")
    lines = [l for l in lines if not l.startswith("代码仓库：")]
    out = []
    for i, l in enumerate(lines):
        if l == "" and i > 0 and lines[i - 1] == "":
            continue
        out.append(l)
    if url:
        for i, l in enumerate(out):
            if l.startswith("# "):
                out.insert(i + 1, "")
                out.insert(i + 2, f"代码仓库：{url}")
                break
    io.open(path, "w", encoding="utf-8").write("\n".join(out))


def fetch():
    repos, page = [], 1
    while True:
        p = subprocess.run(["curl", "-s", "--ssl-no-revoke", "-m", "60",
                            f"https://api.github.com/users/{OWNER}/repos?per_page=100&page={page}&type=owner"],
                           stdout=subprocess.PIPE)
        batch = json.loads(p.stdout.decode("utf-8", "replace"))
        if not isinstance(batch, list) or not batch:
            break
        repos += [{"name": r["name"], "url": r["html_url"], "stars": r["stargazers_count"],
                   "desc": r["description"] or ""} for r in batch]
        if len(batch) < 100:
            break
        page += 1
    json.dump(repos, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("repos:", len(repos))


def fill():
    by_name = {}
    for r in load_repos():
        by_name.setdefault(norm(r["name"]), []).append(r)
    added = 0
    for path in sorted(glob.glob(os.path.join(DOCS, "*.md"))):
        fn = os.path.basename(path)
        if fn in SKIP:
            continue
        slug = fn[:-3]
        txt = io.open(path, encoding="utf-8", errors="replace").read()
        m = LINK.search(txt)
        if m:
            continue
        url = f"https://github.com/{OWNER}/{SUBSKILL[slug]}" if slug in SUBSKILL else None
        if not url:
            cands = by_name.get(norm(slug), [])
            url = max(cands, key=lambda r: r["stars"])["url"] if cands else None
        if url and status(url) == "200":
            set_link(path, url)
            print(f"补 {fn} <- {url}")
            added += 1
    print(f"新增 {added}")


def check():
    bad = []
    total = 0
    for path in sorted(glob.glob(os.path.join(DOCS, "*.md"))):
        m = LINK.search(io.open(path, encoding="utf-8", errors="replace").read())
        if not m:
            continue
        total += 1
        if status(m.group(1)) != "200":
            bad.append((os.path.basename(path), m.group(1)))
    print("检查", total, "失败", len(bad))
    for b in bad:
        print(*b)


if __name__ == "__main__":
    {"fetch": fetch, "fill": fill, "check": check}[sys.argv[1] if len(sys.argv) > 1 else "fill"]()
