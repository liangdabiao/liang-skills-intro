#!/usr/bin/env python3
"""4 个新 skill 的 8 张小黑手绘配图（复用 gen_image.py + 统一 Visual DNA）"""
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
    # 1. brightdata-research
    ("brightdata-research", "01", prompt(
        "AI 带反爬盾抓取全网数据做调研",
        "系统局部",
        "小黑举盾破墙，网页数据变表格",
        "小黑站在一堵贴着禁止符号的高墙前，左手举着一面画有锁形图案的圆盾，右手正从墙上的破洞里抽出一卷长长的纸带；纸带从墙内延伸到右侧，末端自动折成一叠整齐的小表格；墙头上探出一个机器人探头的简笔线稿。",
        "小黑举盾 / 贴禁止符号的高墙 / 穿墙的纸带 / 折好的表格 / 墙头机器人探头",
        "反爬 / 破墙 / 抓数据 / 变表格",
        "Black for main line art and 小黑. Orange for the data paper stream. Red only for the wall prohibition mark. Blue only for the robot probe."
    )),
    ("brightdata-research", "02", prompt(
        "散落网页被聚合成一份市场报告",
        "前后对比",
        "碎片信息进去，结论报告出来",
        "画面左半边散落着七八张皱巴巴的小网页卡片，上面是乱线一样的文字；一个大箭头指向右半边；右侧小黑戴着一副小眼镜，双手捧着一份装订整齐的报告册，封面画着一个小饼图；小黑表情认真满足。",
        "左侧散乱网页卡 / 中央大箭头 / 小黑捧报告册 / 封面小饼图",
        "散的 / 归拢 / 结论 / 报告",
        "Black for main line art and 小黑. Orange for the center arrow. Red only for the report cover chart. Blue only for scattered page notes."
    )),
    # 2. claude-data-analysis
    ("claude-data-analysis", "01", prompt(
        "一堆CSV经过七模块流水线变成结论报告",
        "方法分层",
        "数据流水线：脏数据进去，结论出来",
        "画面左侧堆着一小山杂乱的CSV文件纸堆，一台传送带从纸堆伸向右侧；传送带上依次排着七个画有小图标的工作站牌子；传送带末端小黑接住一份亮着的结论卡片，卡片上画着上升折线；小黑脚下是流水线开关。",
        "左侧CSV纸堆 / 传送带七个工位 / 小黑接结论卡 / 上升折线 / 脚下开关",
        "脏数据 / 七道工序 / 出结论",
        "Black for main line art and 小黑. Orange for the conveyor belt. Red only for the rising line on the conclusion card. Blue only for station icons."
    )),
    ("claude-data-analysis", "02", prompt(
        "老板追问所以结论是什么呢",
        "概念隐喻",
        "三张图不算分析，结论才算",
        "小黑站在一块小白板前，白板上贴着三张图表卡片；一个巨大的手指从画面上方伸下来指着小黑，手指旁一个大问号；小黑一手举起一张写着结论二字的发光卡片回应；地上散着揉皱的草稿纸团。",
        "巨大下指的手指 / 大问号 / 小黑举结论卡 / 白板上的图表 / 地上纸团",
        "所以呢 / 结论在这 / 别再画图了",
        "Black for main line art and 小黑. Orange for the question mark. Red only for the glowing conclusion card. Blue only for chart notes."
    )),
    # 3. ecom-details-image
    ("ecom-details-image", "01", prompt(
        "一张产品图变全套电商素材",
        "前后对比",
        "单图进，主图详情页社媒图全出",
        "画面左侧小黑双手举起一张小小的产品照片（一个简单的水杯）；中间一台画着魔法阵的复印机正在运转；右侧扇形展开五六张不同比例的成品图卡（白底主图、场景图、长图详情、手机海报），像扑克牌一样排开。",
        "小黑举产品照 / 魔法复印机 / 扇形展开的多规格图卡",
        "一张图 / 全套素材 / 主图详情社媒",
        "Black for main line art and 小黑. Orange for the machine magic circle. Red only for the hero image card highlight. Blue only for size labels."
    )),
    ("ecom-details-image", "02", prompt(
        "多张图锁在同一套视觉风格里",
        "概念隐喻",
        "Style Lock：色板字体光线一起锁死",
        "小黑拿着一把大挂锁，锁梁穿过并排三张图卡的顶边，把三张图串在一起；每张图卡角落画着相同的色板条和字体样本；小黑另一手把钥匙插进锁眼；图卡内容各不相同但风格一致。",
        "小黑持大挂锁 / 锁住的三张图卡 / 角落同款色板 / 插入的钥匙",
        "风格锁死 / 色板一致 / 字体一致",
        "Black for main line art and 小黑. Orange for the lock body. Red only for the palette strip highlight. Blue only for font sample notes."
    )),
    # 4. seedance2-storyboard
    ("seedance2-storyboard", "01", prompt(
        "小说变成多集分镜脚本流水线",
        "系统局部",
        "一本书进去，分镜表一集集出来",
        "画面左侧一本翻开的书立在传送带起点；传送带向右穿过一台贴着AI标签的小机器；末端输出一排编号的分镜卡片（画着小格子画面和小字时间轴），像多米诺一样立着；小黑蹲在末端数卡片，手里拿着编号最大的最后一张。",
        "翻开的小说 / AI小机器 / 编号分镜卡排列 / 小黑数卡片 / 时间轴小字",
        "小说进 / 分镜出 / E01到E05",
        "Black for main line art and 小黑. Orange for the conveyor and machine label. Red only for the last episode number. Blue only for timeline notes."
    )),
    ("seedance2-storyboard", "02", prompt(
        "编号素材让每集角色长相一致",
        "概念隐喻",
        "编号资产库：同一角色反复调用",
        "小黑站在一个卡片架前，架子上插着三排带编号的卡片：一排角色（同一小人形象三张）、一排场景（同座小山三张）、一排道具（同一把刀三张）；小黑正抽出一张角色卡，卡上的小人与旁边分镜格里的小人一模一样。",
        "卡片架三排编号卡 / 同一角色三张 / 小黑抽卡 / 分镜格里相同小人",
        "C01角色 / 每集一样 / 资产库",
        "Black for main line art and 小黑. Orange for card numbering. Red only for the drawn character card. Blue only for scene and prop row labels."
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
