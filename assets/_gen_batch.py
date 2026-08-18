#!/usr/bin/env python3
"""Batch driver: calls shared gen_image.py for each 小黑 hand-drawn illustration.
Uses subprocess with argument lists (no shell escaping issues)."""
import subprocess, sys, os, json

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

# (project, idx, prompt)
JOBS = []

# 1. edu-analytic-geometry
JOBS.append(("edu-analytic-geometry", "01", prompt(
    "解析几何题变成能拖动滑块看的互动网页",
    "系统局部",
    "拖一根滑块，椭圆曲线和取值范围就活过来",
    "小黑站在画面中央，伸出细手推动一根横向滑块；左侧一张题面纸写着椭圆方程，右侧一块画板里一条椭圆曲线随滑块伸缩，画板上亮起一条横向范围条。",
    "小黑推滑块 / 题面纸与椭圆方程 / 画板里的椭圆曲线 / 亮起的范围条",
    "拖一拖 / 活的 / 范围条 / 范围",
    "Black for main line art and 小黑. Orange for the slider track and flow arrows. Red only for the key range bar highlight. Blue only for secondary state notes."
)))
JOBS.append(("edu-analytic-geometry", "02", prompt(
    "取值范围题能看见被教辅漏掉的端点",
    "概念隐喻",
    "小黑在画板上圈出端点，范围条亮起，端点不再漏算",
    "小黑举着一支画笔，在右侧画板上认真圈出一个发光的小圆点（端点），旁边一条横向范围条被橙色箭头点亮；左侧飘着一行小字标明这个端点。",
    "小黑执画笔 / 画板上的发光端点 / 被点亮的范围条 / 端点标注",
    "端点 / 别漏 / 算对了 / 范围",
    "Black for main line art and 小黑. Orange for the lit range bar and arrows. Red only for the key endpoint circle. Blue only for secondary notes."
)))

# 2. edu-chem-reaction
JOBS.append(("edu-chem-reaction", "01", prompt(
    "化学反应变成能转着看的3D断键成键动画",
    "系统局部",
    "小黑旋转3D分子模型，旧键断开新键连上",
    "小黑双手捧着一个三维球棍分子模型，正用手指拨动它旋转；几根棍子画成断开的橙色缺口，又有新棍在连接；左下角一个小计数器。",
    "小黑转3D球棍模型 / 断开的旧键(橙) / 连接的新键 / 原子守恒计数器",
    "断键 / 成键 / 转着看 / 守恒",
    "Black for main line art and 小黑. Orange for broken-bond gaps and flow arrows. Red only for the key conservation prompt. Blue only for secondary state."
)))
JOBS.append(("edu-chem-reaction", "02", prompt(
    "甲烷燃烧看得见原子守恒",
    "前后对比",
    "反应前后原子一个没少，计数器不掉数",
    "小黑用一根细棍指着一块小黑板，黑板左半边画着反应前的原子小团，右半边画着反应后的原子小团，中间一个等号；小黑另一手举着一个计数器显示数字不变；两侧原子数量上下对齐。",
    "小黑指黑板 / 左侧反应前原子团 / 右侧反应后原子团 / 守恒计数器",
    "没少 / 配平 / 前后一样",
    "Black for main line art and 小黑. Orange for flow arrows. Red only for the conservation highlight bar. Blue only for secondary notes."
)))

# 3. edu-chem-tutorial
JOBS.append(("edu-chem-tutorial", "01", prompt(
    "化学课变成能一步步播放的互动网页",
    "系统局部",
    "小黑按下一步，卡片一页页动起来",
    "小黑站在一块网页卡片前，伸出细手点一个下一步按钮；卡片上方有概览小卡，侧边一栏讲解要点，中间是一步动画示意；卡片像幻灯片正翻到下一页。",
    "小黑点下一步 / 概览卡片 / 侧边讲解栏 / 当前动画步",
    "下一步 / 一小节 / 带解说",
    "Black for main line art and 小黑. Orange for the playback flow arrows. Red only for the current key step. Blue only for secondary notes."
)))
JOBS.append(("edu-chem-tutorial", "02", prompt(
    "填好课程清单自动拼出课件网页",
    "方法分层",
    "数据驱动：把清单注入模板就自动生成网页",
    "小黑把一张写满步骤的清单纸塞进一个简易模板机器的投料口，机器另一头吐出一张带卡片和步骤的网页；中间用箭头连起清单与网页。",
    "小黑投清单 / 模板机器 / 吐出的网页 / 连接箭头",
    "填清单 / 自动拼 / 改着方便",
    "Black for main line art and 小黑. Orange for flow arrows. Red only for key parts. Blue only for secondary notes."
)))

# 4. edu-physics
JOBS.append(("edu-physics", "01", prompt(
    "物理过程变成能拖滑块看的2D网页",
    "系统局部",
    "拖时间滑块，小球沿抛物线飞，机械能守恒一直亮",
    "小黑站在中间推一根时间滑块；右侧画板上一个小球沿抛物线轨迹飞，速度箭头实时转向；画板一角亮着E恒定的提示；左侧是题面。",
    "小黑推时间滑块 / 抛物线轨迹 / 速度矢量箭头 / E恒定提示",
    "拖时间 / 抛物线 / E恒定",
    "Black for main line art, 小黑 and trajectory. Orange for the slider and flow arrows. Red only for the E-constant highlight bar. Blue only for secondary notes."
)))
JOBS.append(("edu-physics", "02", prompt(
    "平面物理多场景都能演",
    "概念隐喻",
    "小黑在二维画板上切换画出波、光、场",
    "小黑握笔在画板上画：一段上下传播的波形、一条折射的光线、一组电场线；三个小画面并排，用橙色箭头表示可切换。",
    "小黑执笔 / 波形 / 折射光线 / 电场线",
    "波 / 光 / 场",
    "Black for main line art, 小黑 and lines. Orange for switching arrows and light rays. Red only for key parts. Blue only for secondary notes."
)))

# 5. edu-physics-3d
JOBS.append(("edu-physics-3d", "01", prompt(
    "必须3D的物理变成能旋转的网页",
    "系统局部",
    "小黑旋转视角，亲手验证v、B、F三箭头互相垂直",
    "小黑双手转着一个透明三维坐标框，框里从同一点伸出三根箭头代表v、B、F；小黑歪头认真看，旁边画一个右手比划；箭头用虚线连出互相垂直的平面。",
    "小黑转3D坐标框 / v B F 三箭头 / 右手比划 / 垂直平面",
    "转着看 / v B F / 垂直",
    "Black for main line art, 小黑 and arrow lines. Orange for the rotation ring and flow. Red only for the key F arrow. Blue only for secondary notes."
)))
JOBS.append(("edu-physics-3d", "02", prompt(
    "立体空间关系转着看清",
    "概念隐喻",
    "小黑摆弄原子轨道、晶体格、刚体，从任意角度看",
    "小黑捧着一组立体的球与杆，轻轻转它；周围飘着几个可从不同角度看的立体小图，用橙色弧线表示可绕任意轴转。",
    "小黑转晶体格 / 轨道形状 / 任意角弧线 / 立体小图",
    "立体 / 任意角 / 看清",
    "Black for main line art and 小黑. Orange for rotation arcs. Red only for key parts. Blue only for secondary notes."
)))

# 6. edu-plane-geometry
JOBS.append(("edu-plane-geometry", "01", prompt(
    "平面几何变成能拖着玩的网页",
    "系统局部",
    "拖直角边，勾股定理恒等式一直为0",
    "小黑推一根滑块，右侧画板一个直角三角形跟着变形，直角处有标准直角记号，边长a、b、c标着；画板亮起a方加b方减c方恒等于0的恒等式条。",
    "小黑推滑块 / 直角三角形 / 直角记号 / 恒等式条",
    "拖一拖 / 恒为0 / 勾股",
    "Black for main line art, 小黑 and shapes. Orange for the slider and flow. Red only for the identity highlight bar. Blue only for secondary notes."
)))
JOBS.append(("edu-plane-geometry", "02", prompt(
    "用几何构造语法点出中点垂足，不用算坐标",
    "方法分层",
    "小黑用尺规直接点出中点、垂足等构造",
    "小黑拿一把小尺和圆规，在三角形上点出中点（小叉）和垂足（小直角），图形上标出等长标记；旁边一行小字：不用手算坐标。",
    "小黑执尺规 / 中点标记 / 垂足标记 / 等长标记",
    "中点 / 垂足 / 不用算",
    "Black for main line art, 小黑 and shapes. Orange for construction flow arrows. Red only for key parts. Blue only for secondary notes."
)))

# 7. edu-sci-viz
JOBS.append(("edu-sci-viz", "01", prompt(
    "科学概念变成单页互动实验",
    "前后对比",
    "小黑拖月球，地月日排成一线才出日全食",
    "小黑伸细手推着一个小月球沿弧线移动；远处画太阳、地球、月球三者，当月影投到地球上时，地球上出现一小块阴影；一条橙色轨迹连起三者。",
    "小黑推月球 / 太阳地球 / 投下的月影 / 排成线轨迹",
    "拖月球 / 排成线 / 日全食",
    "Black for main line art, 小黑 and celestial lines. Orange for the trajectory and flow. Red only for the total-eclipse highlight block. Blue only for secondary notes."
)))
JOBS.append(("edu-sci-viz", "02", prompt(
    "先直觉后定义的叙事科普",
    "方法分层",
    "小黑先玩实验台，再翻到正式定义和来源",
    "小黑左手拨一个实验台滑杆，右手翻一本手册；手册左页是能玩的模型，右页是正式定义，末尾一小行标着来源链接；用箭头表示先玩后学。",
    "小黑拨实验台 / 手册模型页 / 定义页 / 来源链接",
    "先玩 / 后定义 / 有来源",
    "Black for main line art and 小黑. Orange for the play-then-learn arrows. Red only for key parts. Blue only for secondary source notes."
)))

# 8. edu-solid-geometry
JOBS.append(("edu-solid-geometry", "01", prompt(
    "立体几何角和距离变成可旋转3D",
    "系统局部",
    "小黑旋转正四棱锥，对应棱和底面被高亮",
    "小黑双手转着一个正四棱锥3D模型；模型上一条棱和底面被高亮圈出，旁边一个镜头框对准它；左侧飘着分步解析小卡。",
    "小黑转四棱锥 / 高亮棱与底面 / 镜头对准框 / 分步小卡",
    "转着看 / 高亮 / 对得上",
    "Black for main line art, 小黑 and model lines. Orange for rotation and highlight. Red only for key highlight. Blue only for secondary notes."
)))
JOBS.append(("edu-solid-geometry", "02", prompt(
    "建系向量法求解立体几何",
    "方法分层",
    "小黑建坐标系标法向量，答案和图形对得上",
    "小黑在一块立体图形上画一个三维坐标系，标出法向量箭头，旁边写一个小答案；箭头从图形指向答案，表示同源一致。",
    "小黑建坐标系 / 法向量箭头 / 小答案 / 一致连线",
    "建系 / 向量法 / 答案",
    "Black for main line art, 小黑 and coordinate lines. Orange for vector arrows. Red only for the key answer. Blue only for secondary notes."
)))

# 9. mathigon-skill
JOBS.append(("mathigon-skill", "01", prompt(
    "给Mathigon加一节互动课的操作手册",
    "方法分层",
    "一门课等于一串步骤，content.md与functions.ts靠名字对应",
    "小黑在一张content.md纸上写下一串带标记的步骤，另一张functions.ts纸上写对应函数；两张纸用同名的链条连起来，表示一一对应。",
    "小黑写content.md / 步骤标记 / functions.ts脚本 / 同名链条",
    "写步骤 / 配脚本 / 名字对上",
    "Black for main line art, 小黑 and paper lines. Orange for the matching-chain arrows. Red only for key parts. Blue only for secondary notes."
)))
JOBS.append(("mathigon-skill", "02", prompt(
    "改Mathigon中文课本的隐藏规则",
    "概念隐喻",
    "每个小节必须写英文段落标识，否则后面打不开",
    "小黑在一份文档的小节处补写一个英文段落标识；旁边一扇章节门原本锁着，补上标识后门打开；用红色叉表示没写会打不开。",
    "小黑补英文标识 / 锁着的章节门 / 打开的门 / 红色叉",
    "英文标识 / 别忘了 / 能打开",
    "Black for main line art and 小黑. Orange for the opening arrow. Red only for the cannot-open warning cross. Blue only for secondary notes."
)))

# 10. stem-illustration
JOBS.append(("stem-illustration", "01", prompt(
    "让AI画出准确的STEM示意图",
    "方法分层",
    "给需求后先出视觉简报(中文说明+英文Prompt)，确认后生图",
    "小黑把一张画图需求纸折成一份视觉简报，简报上分两栏写着中文说明和英文Prompt，右下角一个确认勾；箭头从需求流向简报再流向出图。",
    "小黑出简报 / 需求纸 / 中文说明栏 / 英文Prompt栏加确认勾",
    "先简报 / 准 / 确认",
    "Black for main line art and 小黑. Orange for flow arrows. Red only for the confirmation key. Blue only for secondary notes."
)))
JOBS.append(("stem-illustration", "02", prompt(
    "不让AI画错STEM图的科学铁律",
    "系统局部",
    "小黑检查箭头方向、术语标准、禁止虚构",
    "小黑拿放大镜盯一张示意图，核对箭头方向是否正确、术语有没有写错；旁边一个红叉划掉虚构通路，一个色板表示统一风格。",
    "小黑拿放大镜 / 箭头方向核对 / 术语表 / 红叉禁止虚构",
    "别画反 / 别编 / 统一",
    "Black for main line art and 小黑. Orange for the checking arrow. Red only for the no-fabrication cross. Blue only for secondary term notes."
)))

def main():
    results = []
    for project, idx, pr in JOBS:
        out = os.path.join(OUT_BASE, project, idx + ".png")
        args = [PY, GEN, "--prompt", pr, "--out", out]
        try:
            cp = subprocess.run(args, capture_output=True, text=True, timeout=200)
            ok = (cp.returncode == 0) and ("OK:" in cp.stdout)
            line = f"[{project}/{idx}] ok={ok} rc={cp.returncode} out={cp.stdout.strip()[-80:]} err={cp.stderr.strip()[:80]}"
        except Exception as e:
            ok = False
            line = f"[{project}/{idx}] EXCEPTION {e}"
        print(line, flush=True)
        results.append({"project": project, "idx": idx, "ok": ok, "line": line})
    # summary
    failed = [r for r in results if not r["ok"]]
    print("\n=== SUMMARY ===")
    print(f"total={len(results)} ok={len(results)-len(failed)} failed={len(failed)}")
    for r in failed:
        print("FAILED:", r["project"], r["idx"], r["line"])
    with open("E:/all-skill-t0/skill-intros/assets/_batch_result.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
