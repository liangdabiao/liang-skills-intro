# -*- coding: utf-8 -*-
"""闲鱼/淘宝服务商品图生成器（纯代码绘制，文案式图示，1080x1080）

每篇文章一张：主标题 + 前三项服务说明按各篇闲鱼文案定制，
顶栏 / 卖点胶囊 / 第 4 项 / 底部条为全店统一模板。
用法：python gen_xianyu_card.py   输出：assets/xianyu/<name>.png
"""
import os
from PIL import Image, ImageDraw, ImageFont

# ---------- 配色（沿用 skill-intros 视觉体系） ----------
INK       = (31, 35, 40)
MUTED     = (107, 114, 128)
ACCENT    = (232, 84, 63)
ACCENT_DK = (194, 52, 34)
HL        = (255, 214, 90)
BG        = (251, 251, 249)
CARD      = (255, 255, 255)
LINE      = (233, 233, 230)
BAND      = (243, 243, 240)

W = H = 1080
FONT_DIR = r"C:\Windows\Fonts"
OUT_DIR = os.path.join("assets", "xianyu")

# ---------- 全店统一模板 ----------
LABEL  = "AI 技能 SKILL 定制开发服务"
TITLE2 = "skill 软件开发"
PILLS  = ["现成作品可演示", "源码全交付", "支持二次开发"]
ITEM4  = ("skill源码交付", "SKILL.md + 提示词/脚本/模板 + 部署说明 + 使用演示")
FOOTER = "兼容 codex / workbuddy 等 agent · 装好即用 · 可先看演示再下单"
ITEM_TITLES = ["需求沟通梳理", "skill交付内容和格式", "项目功能/系统开发"]

# ---------- 每篇定制：(文件名, 主标题, 第1项说明, 第2项说明, 第3项说明) ----------
CARDS = [
    # 电商与广告类
    ("amazon-skill", "亚马逊运营AI技能",
     "明确运营痛点与数据来源，列清功能清单再动手",
     "选品 / Listing / 竞品 / 评论等具体报告和数据成果",
     "按你的类目定制功能模块，数据接口对接联调"),
    ("amazon-listing-alexa-optimizer", "亚马逊Listing AI导购优化",
     "品类 / 站点 / 优化目标确认，商品页素材齐全",
     "8 维体检报告 + 标题五点改前改后 + 7 天落地清单",
     "按品类定制评分维度与改写规则，可批量体检"),
    ("apiz", "AI模型聚合调用",
     "画图 / 视频 / 配音等模型能力与使用场景确认",
     "文生图 / 图生视频 / 语音克隆 / 字幕打轴等调用成果",
     "定制模型选型、参数模板与批量生成回收流程"),
    ("apiz-use", "电商AI作图/短视频/角色设计",
     "平台 / 内容类型 / 风格确认，备好产品图与文案",
     "主图套图 / 宣传图 / 带货视频 / 角色人设等生成成果",
     "定制提示词模板与样图确认批量流程，联调模型网关"),
    ("facebook-ads-analyzer", "Facebook广告数据分析",
     "投放规模 / 复盘周期 / 数据字段确认",
     "广告评分评级 + Top10 排名 + 三套预算方案报告",
     "定制评分权重、分组维度与报告模板"),
    ("fastmoss-rpa", "TikTok电商数据采集",
     "站点 / 榜单类型 / 筛选条件确认，登录 FastMoss",
     "商品 / 达人 / 店铺 / 广告等 7 类榜单 CSV + 分析报告",
     "定制抓取字段、多市场对比与定期采集"),
    ("sellersprite-rpa", "亚马逊卖家精灵数据采集",
     "模块（选品/关键词/ABA/竞品）与站点确认",
     "热销 ASIN / 关键词 / ABA 排行等 CSV + 对比报告",
     "定制抓取模块组合、多站点批量与定期采集"),
    ("sorftime-rpa", "Sorftime亚马逊数据采集",
     "榜单 / 反查板块与 14 个目标站点确认",
     "畅销榜 TOP100 / 品牌卖家榜 / 反查数据 + 中文报告",
     "定制板块组合、跨站批量与报告模板"),
    # amazon 子技能
    ("amazon-analyse", "亚马逊竞品穿透分析",
     "ASIN 清单与关注维度确认，Sorftime 账号可用",
     "价格 / 关键词 / 评论情感 / 战略建议等情报报告",
     "定制分析维度与报告模板，可扩展多站对比"),
    ("amazon-listing-builder", "亚马逊爆款Listing打造",
     "产品卖点 / 站点 / 新品或老 Listing 改造确认",
     "词库 + 问题库 + 证据库 + 标题五点多版草稿",
     "定制词库构建与生成规则，可扩展多语言版本"),
    ("category-selection", "亚马逊类目选品分析",
     "类目 / 站点 / 分析深度与对比数量确认",
     "五维评分 + 综合评级 + 25 个月趋势报告",
     "定制维度权重、多类目对比与站点扩展"),
    ("keyword-research", "亚马逊关键词调研词库",
     "产品 / ASIN / 广告目标确认，Sorftime 账号可用",
     "2000+ 关键词 8 维分类：报告 + CSV 词库 + 看板",
     "定制分类维度与词库结构，可批量 ASIN 反查"),
    ("product-research", "亚马逊选品调研分析",
     "品类 / 关键词 / 决策问题确认，Sorftime 账号可用",
     "数据看板 + VOC 痛点挖掘 + 壁垒评估与决策评分",
     "定制分析维度、评分模型与看板模板"),
    ("review-analysis", "亚马逊评论痛点分析",
     "分析对象与目的（改进/避雷/客服）确认",
     "差评聚类 + 痛点 Top3 + 客服话术模板报告",
     "定制痛点框架与话术风格，可多 ASIN 批量分析"),
    ("sellersprite-amazon-research", "卖家精灵全链路调研",
     "调研场景（市场/竞品/广告/流量）与常用工具确认",
     "43 个数据工具全链路调研成果与策略洞察",
     "定制命令组合、报告模板与机会识别规则"),
    ("sif-amazon-research", "亚马逊流量诊断与增长优化",
     "问题（流量下跌/上新验证）与 ASIN 确认，Sif 可用",
     "带证据链的根因诊断、决策与优先动作报告",
     "定制诊断场景、指标口径与报告模板"),
    ("xiyou-insight", "亚马逊竞品广告流量透视",
     "场景（盯广告/找流量缺口/建词库）与 ASIN 确认",
     "广告监控 / 流量缺口 / 竞品拆解 + 可视化看板",
     "定制监控指标、竞品清单与看板模板"),
    # 市场与选题调研类
    ("exa-company-research", "企业情报调研挖掘",
     "用途（合作摸底/找客户/竞品盘点）与目标确认",
     "公司档案 / 竞品清单 / 高管资料等情报报告",
     "定制信息维度、名单规模与报告模板"),
    ("exa-foreign-trade-research", "外贸目标国市场调研",
     "目标国家 / 产品领域 / 调研深度确认",
     "TOP20 玩家格局 + 对比矩阵 + 中国供应商进入建议",
     "定制玩家分类、验证渠道与报告章节"),
    ("market-insight", "用户洞察与需求分析",
     "产品方向 / 所处阶段 / 想要的产出确认",
     "用户画像 + 情绪洞察 + P0/P1/P2 机会清单",
     "定制画像维度、机会框架与创业路线图"),
    ("reddit-business-idea-validator", "海外生意点子验证",
     "生意点子与验证深度确认，Reddit 接口可用",
     "0–100 评分 + 痛点 / 竞品 / 机会验证报告",
     "定制分析维度、评分权重与报告模板"),
    ("xhs-business-validator", "小红书生意点子验证",
     "生意想法与模式（快速/完整）确认，TikHub 可用",
     "0–100 评分 + 关键痛点 + 热门笔记 Top3 报告",
     "定制分析维度、评分口径与报告模板"),
    ("XHS_Business_Idea_Validator", "小红书商业创意验证器",
     "创意点子与验证深度（轻量/深度）确认",
     "0–100 评分 + 痛点 / 方案 / 机会验证报告",
     "定制分析框架与报告样式，可改技能版"),
    ("simple-review-analyzer", "电商评论分析（VOC）",
     "评论来源 / 分析条数 / 关心问题确认",
     "22 维打标明细 + 洞察报告 + 可视化看板",
     "定制打标维度、画像框架与看板图表"),
    # 教育科普与数学类
    ("edu-analytic-geometry", "解析几何交互课件",
     "用途（课件/自学/教辅配图）与题目范围确认",
     "可拖滑块交互网页：分步推导 + 画板 + 范围条指示",
     "按教材定制布局与滑块参数，可批量生成"),
    ("edu-chem-reaction", "化学反应3D动画课件",
     "反应清单与教学重点（配平/守恒/机理）确认",
     "可旋转 3D 网页：断键成键动画 + 原子守恒计数器",
     "定制反应库、动画节奏与讲解文案"),
    ("edu-chem-tutorial", "化学互动微课课件",
     "课程主题 / 目标学段 / 步数规模确认",
     "5–15 步互动课程页：分步动画 + 概览卡 + 要点",
     "定制课程结构、动画场景与知识卡片"),
    ("edu-physics", "物理互动课件（2D）",
     "物理场景 / 典型参数 / 教学重点确认",
     "可拖滑块网页：轨迹波形 + 守恒定律指示",
     "定制场景库、参数范围与推导风格"),
    ("edu-physics-3d", "物理3D互动课件",
     "3D 场景 / 可调参数 / 观察重点确认",
     "可旋转缩放 3D 网页：立体画板 + 守恒指示",
     "定制 3D 对象类型、镜头视角与讲解文案"),
    ("edu-plane-geometry", "平面几何交互课件",
     "定理 / 题型（全等/相似/面积）与用途确认",
     "课本风画板网页：几何标注 + 恒等式指示",
     "定制构造类型、标注风格与题库"),
    ("edu-sci-viz", "科学互动科普页",
     "科普主题 / 目标读者 / 平台确认，主题真实可核验",
     "单文件互动页：叙事讲解 + 互动实验台 + 来源追溯",
     "定制叙事结构、视觉风格与实验台参数"),
    ("edu-solid-geometry", "立体几何3D课件",
     "题型（线面角/二面角/距离/体积）与用途确认",
     "可旋转 3D 网页：分步高亮 + 建系向量法推导",
     "定制题型库、模型类型与讲解节奏"),
    ("mathigon-skill", "Mathigon互动课程开发",
     "想新增 / 修改的课程内容与技术基础确认",
     "步骤化操作指引与规范文档（含中文课隐藏规则）",
     "定制内容文件、互动脚本与样式，本地预览联调"),
    ("stem-illustration", "科研教学STEM示意图",
     "学科 / 场景 / 风格 / 尺寸与用途确认",
     "视觉简报 + 期刊风示意图（整套风格统一）",
     "定制场景模板与风格变体，可批量成套出图"),
    # 视频与动画类
    ("geometry-math-proof-remotion", "数学证明动画视频",
     "证明主题 / 目标观众 / 时长确认，提供证明文档",
     "1080p 推导成片：描线动画 + 公式揭示 + 配音字幕",
     "定制章节结构、配色配音与系列模板"),
    ("hyperframes-video-spec-builder", "视频分镜脚本策划",
     "视频目的 / 受众 / 素材盘点与视觉风格选定",
     "镜头级规格脚本：分镜表 + 配乐字幕动效说明",
     "定制追问流程、视觉风格库与快速通道"),
    ("make-prompt-seedance2", "AI短视频提示词编写",
     "视频用途（带货/种草/广告）与产品图确认",
     "五大模块分镜提示词，可直接粘贴即梦 / 豆包",
     "定制路线写法、钩子结构与强制约束库"),
    ("paper-cutout-remotion", "剪纸分层动画视频",
     "故事 / 分镜 / 风格 / 时长确认",
     "四层剪纸风成片：遮挡立体感 + 配音字幕",
     "定制分层模板、中国风配色与配音方案"),
    ("podcast-shorts-remotion", "播客转竖屏短视频",
     "音频来源 / 时长 / 逐字稿与目标平台确认",
     "竖屏字幕视频：章节切分 + 进度条 + 关键词高亮",
     "定制章节策略、主题配色与字幕样式"),
    ("story-handdrawn-remotion", "手绘日记风故事视频",
     "故事文本 / 风格（治愈/童话/教学）与用途确认",
     "3:4 手绘动画：一句一拍三次揭示 + 配音字幕",
     "定制画面风格、节奏与英文教学闪卡模式"),
    ("story-handdrawn-video", "蜡笔风动画短视频",
     "故事文本 / 画风 / 时长确认",
     "9:16 会动蜡笔风短片：音画对齐 + 毛笔字幕",
     "定制画风锁定、场景拆分与英语教学卡"),
    ("talking-head-remotion", "口播视频工程模板",
     "口播素材 / 录屏需求 / 团队复用需求确认",
     "排布好的成片 + 可复用工程与公共素材库",
     "定制布局、动效与竖屏版本"),
    ("wechat-article-remotion", "公众号文章转视频",
     "文章链接 / 目标平台 / 配图保留要求确认",
     "Studio 风成片：原文图完整 + 配音高亮字幕",
     "定制场景模板、配色与配音方案"),
    # 写作与课程类
    ("liurun-bookwriter", "刘润式商业长文写作",
     "选题 / 目标读者 / 文体（评论/拆解/回应）确认",
     "完整长文稿：成稿结构 + 金句故事 + 12 项自检",
     "定制结构模板、禁用词表与自检规则"),
    ("luozhenyu-bookwriter", "罗振宇式启发文章写作",
     "选题 / 文体（60秒/长文/演讲稿）与篇幅确认",
     "启发式完稿：原创金句 + 人物故事 + 生活比方",
     "定制金句公式、故事库规则与自检标准"),
    ("course-site-skill", "笔记转课程网站",
     "笔记规模 / 课程定位 / 发布平台确认",
     "课程网站：课程化正文 + 每课测验 + 进度追踪",
     "定制全站配色 / logo / 标题与章节结构"),
    ("i18n-helper-skills", "网站多语言国际化（i18n）",
     "项目类型（纯网页/源码工程）与目标语言确认",
     "多语言站点目录或语言文件包 + 完成度报告",
     "定制提取规则、术语表与回填流程"),
    ("wechat-writer", "公众号写作+配图",
     "主题 / 读者 / 篇幅 / 是否联网配图确认",
     "完整文章稿：选题卡 + 三遍审校 + 统一风格配图",
     "定制写作风格、审校规则与配图风格"),
    ("ian-xiaohei-illustrations", "文章手绘配图（小黑）",
     "文章内容 / 配图数量 / 交付方式确认",
     "配图清单 + 16:9 小黑风格手绘成图（批量）",
     "定制视觉动作、标注风格与出图数量"),
    # 研究与智能体框架类
    ("deep-research-agent", "深度研究报告生成",
     "研究主题 / 范围 / 格式 / 来源要求确认",
     "报告文件夹：摘要 + 全文 + 引用验证 + 来源评级",
     "定制研究框架、评级标准与报告模板"),
    ("stock-deep-research", "股票公司尽调报告",
     "标的 / 投资风格 / 持有周期与关注点确认",
     "8 阶段尽调：交叉验证 + 看空场景 + 信号灯评级",
     "定制尽调阶段、指标口径与报告模板"),
    ("claude-agent-sdk", "Claude智能体应用开发",
     "应用形态（读代码助手/客服/多AI协作）确认",
     "能自主干活的智能体：流式交互 + 工具 + 会话",
     "定制工具集成、权限钩子与部署方案"),
    ("flue-framework", "TypeScript智能体框架",
     "智能体用途 / 模型 / 形态（常驻/工作流）确认",
     "能跑、能联网、能部署的智能体工程 + 上线说明",
     "定制自定义工具、子智能体编排与部署方案"),
    ("game-gameability", "游戏创意游戏性验证",
     "游戏概念 / 目标玩家 / 平台确认",
     "验证报告：核心动词 + 压力测试 + 好玩七维预检",
     "定制判定标准、测试维度与报告模板"),
    # 工具与杂项类
    ("brickMosaic", "照片转乐高拼搭图纸",
     "照片 / 格子尺寸 / 配色套装与抠背景需求确认",
     "预览图 + A4 拼搭说明书 + 零件采购清单",
     "按套装定制量化配色方案，可批量出图纸"),
    ("boardgame-io", "棋牌桌游网页游戏",
     "游戏规则 / 形态（双人/联网/人机）确认",
     "能玩的游戏：网页界面 + 规则逻辑 + 对战",
     "模板改造、界面主题与机器人策略"),
    ("tikhub-api-helper", "社媒数据接口调用",
     "平台与数据类型（资料/评论/热门）确认",
     "接口匹配说明 + 整理好的现成数据",
     "定制常用接口组合、批量采集与定期拉数"),
    ("geo-optimizer", "GEO生成式引擎优化",
     "品牌信息 / 官网网址 / 优化目标确认",
     "结构化标记 + AI 友好度评分 + 可见度对比报告",
     "定制检测维度、内容集群结构与问题库"),
    ("geo-content-optimizer", "网页AI引用诊断",
     "诊断网址 / 目标关键词 / 优化目标确认",
     "中文诊断报告：内容缺口清单 + 修改建议",
     "定制查询扩展与对比维度，改后可复测"),
    ("geolook", "GEO品牌优化一条龙",
     "官网 / 介绍材料 / 目标市场（国内/海外）确认",
     "三份客户交付文档 + llms.txt + 带验收工单",
     "定制体检维度、AI 平台名单与交付模板"),
    ("resume-matcher", "简历匹配分析与优化",
     "求职方向 / 岗位 JD / 想要的产出确认",
     "问题清单 + 修改蓝图 + 优化简历 + 可打印 PDF",
     "定制审计维度、匹配规则与简历模板"),
    ("sprite-gen", "游戏精灵图动画生成",
     "角色描述 / 动作类型 / 帧数要求确认",
     "排格精灵图 + 透明底动画 GIF + 逐帧预览页",
     "定制角色剧本、帧布局与动作库"),
    ("staticshield", "网页密码加密保护",
     "网页范围（单页/整站）与密码要求确认",
     "自解锁加密文件 + 强密码与使用说明",
     "定制解锁页样式与附加功能"),
    ("weekend-city-trip", "城市周末旅游攻略",
     "城市 / 时间窗口 / 版本（文字/地图/PDF）确认",
     "11 类信息攻略 + 可选交互地图与打印版",
     "定制信息类别、地图标注与报告模板"),
    ("pindou-pattern", "拼豆图纸生成",
     "图片 / 网格尺寸 / 品牌色号与白底处理确认",
     "带色号坐标施工图 + 物料清单（颗数/总量）",
     "定制色库与量化方案，可批量出图"),
]


def F(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def spaced(s, n=1):
    return (" " * n).join(list(s))


def fit_font(draw, text, bold, size, max_w, min_size):
    """超宽自动缩字号，返回可用字体"""
    f = F("msyhbd.ttc" if bold else "msyh.ttc", size)
    while draw.textlength(text, font=f) > max_w and size > min_size:
        size -= 2
        f = F("msyhbd.ttc" if bold else "msyh.ttc", size)
    return f


def gen_card(name, title1, d1, d2, d3):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    tw = lambda s, f: d.textlength(s, font=f)

    f_label = F("msyhbd.ttc", 32)
    f_title = fit_font(d, title1, True, 72, 920, 48)
    f_t2    = F("msyhbd.ttc", 72)
    f_pill  = F("msyhbd.ttc", 29)
    f_sec   = F("msyhbd.ttc", 38)
    f_num   = F("msyhbd.ttc", 30)
    f_it    = F("msyhbd.ttc", 36)

    # 顶部色带
    d.rectangle([0, 0, W, 124], fill=ACCENT)
    label = spaced(LABEL, 2)
    d.text(((W - tw(label, f_label)) / 2, 46), label, font=f_label, fill=(255, 255, 255))

    # 主标题两行，第二行加荧光笔底衬
    y = 162
    d.text(((W - tw(title1, f_title)) / 2, y + (72 - f_title.size)), title1,
           font=f_title, fill=INK)
    y += 104
    x2 = (W - tw(TITLE2, f_t2)) / 2
    d.rounded_rectangle([x2 - 20, y + 54, x2 + tw(TITLE2, f_t2) + 20, y + 110],
                        radius=14, fill=HL)
    d.text((x2, y), TITLE2, font=f_t2, fill=ACCENT_DK)

    # 卖点胶囊
    py, ph, gap = 398, 52, 18
    widths = [tw(p, f_pill) + 44 for p in PILLS]
    total = sum(widths) + gap * (len(PILLS) - 1)
    x = (W - total) / 2
    for p, w in zip(PILLS, widths):
        d.rounded_rectangle([x, py, x + w, py + ph], radius=ph // 2,
                            outline=ACCENT, width=2)
        d.text((x + 22, py + 9), p, font=f_pill, fill=ACCENT)
        x += w + gap

    # 小节标题
    sy = 502
    d.rectangle([64, sy + 2, 78, sy + 44], fill=ACCENT)
    d.text((96, sy), "服务内容", font=f_sec, fill=INK)
    d.line([110 + tw("服务内容", f_sec), sy + 24, W - 64, sy + 24], fill=LINE, width=2)

    # 四张服务项卡片
    descs = [d1, d2, d3, ITEM4[1]]
    cy, ch, cgap = 572, 98, 14
    for i, (t, desc) in enumerate(zip(ITEM_TITLES + [ITEM4[0]], descs), 1):
        d.rounded_rectangle([64, cy, W - 64, cy + ch], radius=16,
                            fill=CARD, outline=LINE, width=1)
        ccx, ccy = 122, cy + ch // 2
        d.ellipse([ccx - 26, ccy - 26, ccx + 26, ccy + 26], fill=ACCENT)
        num = str(i)
        d.text((ccx - tw(num, f_num) / 2, ccy - 22), num, font=f_num, fill=(255, 255, 255))
        d.text((172, cy + 14), t, font=f_it, fill=INK)
        f_id = fit_font(d, desc, False, 26, 800, 20)
        d.text((172, cy + 60), desc, font=f_id, fill=MUTED)
        cy += ch + cgap

    # 底部信息条
    by = H - 66
    d.rectangle([0, by, W, H], fill=BAND)
    d.line([0, by, W, by], fill=LINE, width=1)
    f_foot = fit_font(d, FOOTER, False, 25, 960, 20)
    d.text(((W - tw(FOOTER, f_foot)) / 2, by + 19), FOOTER, font=f_foot, fill=MUTED)

    out = os.path.join(OUT_DIR, name + ".png")
    img.save(out, "PNG")
    return out


if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    for c in CARDS:
        print("saved:", gen_card(*c))
    print("total:", len(CARDS))
