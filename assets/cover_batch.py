#!/usr/bin/env python3
"""批量为缺失封面的文档生成小黑手绘风封面图（apiz CLI，最低质量档省钱）。

用法：
    python cover_batch.py --jobs assets/_covers_2.json --quality low --workers 3
    python cover_batch.py                      # 汇总 assets/_covers_*.json

输出：assets/<slug>/01.png （16:9，PNG，匹配 build_site.py 的引用规则）
已存在 01.png 的默认跳过；若只有 01.jpg 则先转成 PNG。
"""
import argparse, glob, json, os, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor
from PIL import Image

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


def build_prompt(j):
    return (
        "Generate one standalone 16:9 horizontal Chinese article illustration.\n"
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


def load_jobs(base):
    jobs = {}
    for f in sorted(glob.glob(os.path.join(base, "_covers_*.json"))):
        for j in json.load(open(f, encoding="utf-8")):
            jobs[j["slug"]] = j
    return jobs


def png_ok(path):
    if not os.path.exists(path):
        return False
    try:
        Image.open(path).verify()
        return os.path.getsize(path) > 20000
    except Exception:
        return False


def to_png(src, dst):
    im = Image.open(src).convert("RGB")
    im.save(dst, "PNG", optimize=True)
    return im.size


def gen_one(job, base, quality, force, retries=3):
    slug = job["slug"]
    png = os.path.join(base, slug, "01.png")
    jpg = os.path.join(base, slug, "01.jpg")

    if png_ok(png) and not force:
        return ("SKIP", slug, "already ok")
    os.makedirs(os.path.dirname(png), exist_ok=True)
    if os.path.exists(jpg) and not force:
        try:
            sz = to_png(jpg, png)
            os.remove(jpg)
            return ("CONV", slug, str(sz))
        except Exception:
            pass

    last = None
    for attempt in range(1, retries + 1):
        try:
            r = subprocess.run(
                ["apiz", "generate", build_prompt(job),
                 "--model", "apiz/gpt-image-2.5-flare",
                 "--aspect-ratio", "16:9",
                 "--params", json.dumps({"quality": quality}),
                 "--wait", "--wait-timeout", "10m", "--json"],
                capture_output=True, text=True, timeout=900,
            )
            if r.returncode != 0:
                raise RuntimeError((r.stderr or r.stdout or "").strip()[:250])
            body = json.loads(r.stdout)
            url = body["result"]["images"][0]["url"]
            price = body.get("price")
            tmp = jpg + ".dl"
            d = subprocess.run(["curl", "-sk", "-m", "120", "-o", tmp, url],
                               capture_output=True, text=True, timeout=180)
            if d.returncode != 0:
                raise RuntimeError("download failed: " + d.stderr[:200])
            sz = to_png(tmp, png)
            os.remove(tmp)
            if os.path.exists(jpg):
                os.remove(jpg)
            return ("OK", slug, f"{sz} price={price}")
        except Exception as e:
            last = e
            if attempt < retries:
                time.sleep(5 * attempt)
    return ("FAIL", slug, str(last)[:250])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", default=None, help="单个 jobs json；省略则汇总 assets/_covers_*.json")
    ap.add_argument("--base", default="assets")
    ap.add_argument("--quality", default="low")
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()

    if a.jobs:
        jobs = json.load(open(a.jobs, encoding="utf-8"))
    else:
        jobs = list(load_jobs(a.base).values())

    print(f"[batch] {len(jobs)} jobs, quality={a.quality}, workers={a.workers}", flush=True)
    tally = {"OK": 0, "SKIP": 0, "CONV": 0, "FAIL": 0}
    fails = []

    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        futs = [(ex.submit(gen_one, j, a.base, a.quality, a.force), j["slug"]) for j in jobs]
        for fut, slug in futs:
            try:
                status, s, info = fut.result()
            except Exception as e:
                status, s, info = "FAIL", slug, f"exc {e}"
            tally[status] = tally.get(status, 0) + 1
            print(f"[{status}] {s} -> {info}", flush=True)
            if status == "FAIL":
                fails.append(s)

    print(f"\n[summ] OK={tally['OK']} CONV={tally['CONV']} SKIP={tally['SKIP']} FAIL={tally['FAIL']}", flush=True)
    if fails:
        print("[failed] " + " ".join(fails), flush=True)
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
