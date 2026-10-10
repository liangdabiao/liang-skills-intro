# 缺失文档清单 · 待补充（60 篇）

> ✅ **2026-10-10 已全部补齐**：下方 60 个项目的 md + html 均已生成（粗粒度），站点共 **138 篇 / 7 个分类**。本文件保留作为清单与映射记录。

---

## 已有 78 篇文档 → GitHub 仓库映射

### A. 同名 / 规则匹配到 star>10 仓库（42 篇；严格去重统计口径为 41，因 reddit 两个大小写仓库归一化时碰撞）
make-prompt-seedance2、seedance2-storyboard→Seedance2-Storyboard-Generator、ecom-details-image、ecom-video-seedance-prompt、fastmoss-rpa→fastmoss-rpa-skills、liurun-bookwriter→liurun-bookwriter-skills、whiteboard-explainer、claude-data-analysis、amazon-listing-alexa-optimizer、sorftime-rpa→sorftime-rpa-skills、sellersprite-rpa→sellersprite-rpa-skills、xhs-business-validator→xhs-business-validator-skill、Reddit_Business_Idea_Validator、XHS_Business_Idea_Validator、amazon-skill→Amazon-Skills-Liang、story-handdrawn-remotion、story-handdrawn-video、geo-content-optimizer→GEO-Content-Optimizer-Skill、paper-cutout-remotion、deepseek-v4-flash-vision-rag、exa-company-research→exa-research-mcp-skill、math-concept-film、pindou-pattern→perler-beads-skill、reddit-business-idea-validator、weekend-city-trip、market-insight→market-insight-claude-skill、stem-illustration→stem-illustration-skill、tikhub-api-helper→tikhub_api_skill、course-site-skill、facebook-ads-analyzer、sprite-gen→302Sprite、glm-5.3-flash-vision-rag、podcast-shorts-remotion、apiz→apiz-skill、deepseek-v4-flash-vision-video-rag、flue-framework→flue-framework-skill、directing-xiaohei-videos、boardgame-io→boardgame-io-skill、simple-review-analyzer、sif-amazon-research、brightdata-research→Bright-Data-MCP-Claude-Skill-deep-research、i18n-helper-skills。

### B. 同名但仓库 star ≤ 10（6 篇）
brickMosaic（6）、deep-research-agent→deep-research-agent-skill（4）、geometry-math-proof-remotion（4）、resume-matcher→resume-matcher-skill（2，另有 163 star 的 resume-matcher-agent-cn 中文版）、stock-deep-research→stock-deep-research-skill（5）、wechat-article-remotion（5）。

### C. 大仓子技能 / 变体，无独立同名仓库（11 篇）
- 亚马逊聚合包子技能（归属 Amazon-Skills-Liang 大仓）：amazon-analyse、amazon-listing-builder、category-selection、keyword-research、product-research、review-analysis、sellersprite-amazon-research、xiyou-insight
- 变体篇：apiz-use→apiz-skill、exa-foreign-trade-research→exa-research-mcp-skill、glm-5.3-flash-vision-video-rag→glm-5.3-flash-vision-rag

### D. 未找到对应独立仓库（20 篇，多为本地方法论/教学技能）
claude-agent-sdk（上游官方 anthropics/claude-agent-sdk）、edu-analytic-geometry、edu-chem-reaction、edu-chem-tutorial、edu-physics、edu-physics-3d、edu-plane-geometry、edu-sci-viz、edu-solid-geometry、game-gameability、geo-optimizer、geolook、glm-ecom-video-seedance-prompt、hyperframes-video-spec-builder、ian-xiaohei-illustrations、luozhenyu-bookwriter、mathigon-skill、staticshield、talking-head-remotion、wechat-writer。
> 如这些项目在 GitHub 上有仓库但名字不同，告知仓库名即可补链。

---

> 统计口径：对照 GitHub [liangdabiao](https://github.com/liangdabiao) 全部 **767** 个仓库（含 fork），剔除 fork 后，只保留 **star 数 > 10** 的自有项目，共 **102** 个；其中本地已写介绍 **42** 个，**缺失 60 个**。
> 数据截止：2026-10-10。
>
> 优先级说明：**P0 = star ≥ 100**（最该补，20 篇）｜**P1 = star 30–99**（19 篇）｜**P2 = star 11–29**（21 篇）。
> 写作规范沿用现有 78 篇：大白话、面向非技术读者、每篇配「小黑手绘」风格插图 2 张（`assets/<项目名>/01.png`、`02.png`）。

---

## P0 · 高优先（star ≥ 100，20 篇）

| # | 仓库 | star | 建议文档名 | 一句话说明 |
|---|------|-----|-----------|-----------|
| 1 | [amazon-sorftime-research-MCP-skill](https://github.com/liangdabiao/amazon-sorftime-research-MCP-skill) | 957 | amazon-sorftime-research-MCP-skill.md | 亚马逊选品全家桶：Listing 穿透报告 + 全品类/关键词/差评/市场调研，整合 Sorftime、西柚、Sif、卖家精灵 MCP 的 skill 工具集 |
| 2 | [easy_investment_Agent_crewai](https://github.com/liangdabiao/easy_investment_Agent_crewai) | 659 | easy-investment-agent-crewai.md | 基于 AKShare + CrewAI 的 A 股智能分析平台，4 个 AI 角色分工，覆盖行情/财务/资金流/情绪 |
| 3 | [Claude-Code-Stock-Deep-Research-Agent](https://github.com/liangdabiao/Claude-Code-Stock-Deep-Research-Agent) | 374 | claude-code-stock-deep-research-agent.md | 8 阶段股票尽调框架、28 个并行研究智能体，输入 `/stock-research AAPL` 即出研报 |
| 4 | [Fashion-AI](https://github.com/liangdabiao/Fashion-AI) | 336 | fashion-ai.md | 电商 AI 生图流水线：新品平铺图 → 自动检索相似爆款、分析风格 → 生成模特宣传图 |
| 5 | [langgraph_multi-agent-rag-customer-support](https://github.com/liangdabiao/langgraph_multi-agent-rag-customer-support) | 333 | langgraph-multi-agent-rag-customer-support.md | LangChain + LangGraph 多智能体客服：机酒租车预订问答，并对接 WooCommerce 商城查商品/订单 |
| 6 | [perler-beads-ai](https://github.com/liangdabiao/perler-beads-ai) | 326 | perler-beads-ai.md | AI 优化版拼豆图纸生成网站（基于 Zippland/perler-beads），一键出图，配套小程序 |
| 7 | [claude-data-analysis-ultra-main](https://github.com/liangdabiao/claude-data-analysis-ultra-main) | 290 | claude-data-analysis-ultra-main.md | 小白一键互联网/电商数据分析：拉新、留存、促活、转化、A/B test、用户分析 |
| 8 | [Claude-Code-Deep-Research-main](https://github.com/liangdabiao/Claude-Code-Deep-Research-main) | 290 | claude-code-deep-research-main.md | 用 Claude Code 一步步实现 Deep Research 的教程版 skill（简化版为 deep-research-agent-skill） |
| 9 | [hyperframes-fix](https://github.com/liangdabiao/hyperframes-fix) | 237 | hyperframes-fix.md | HyperFrames 国内适配增强：流畅中文语音 + 中文短视频样式，丢一篇文章即可一键出横竖版视频 |
| 10 | [crewai_stock_analysis_system](https://github.com/liangdabiao/crewai_stock_analysis_system) | 182 | crewai-stock-analysis-system.md | CrewAI 股票分析系统：批量分析、实时监控、智能预警，带 Web 管理界面 |
| 11 | [AI-generated-English-podcast-videos](https://github.com/liangdabiao/AI-generated-English-podcast-videos) | 175 | ai-generated-english-podcast-videos.md | 一键生成英文教育短视频：双人对话 + 语音讲解 + 单词配图，可下载发抖音 |
| 12 | [Business_Idea_Validator](https://github.com/liangdabiao/Business_Idea_Validator) | 165 | business-idea-validator.md | 带 Web 界面的商业创意验证器：自动抓取网络讨论、识别痛点与竞品、打分出报告 |
| 13 | [resume-matcher-agent-cn](https://github.com/liangdabiao/resume-matcher-agent-cn) | 163 | resume-matcher-agent-cn.md | "HR 批评"简历智能体中文版：模拟招聘筛选算法，展示关键词匹配与筛选结论 |
| 14 | [autogen-financial-analysis](https://github.com/liangdabiao/autogen-financial-analysis) | 162 | autogen-financial-analysis.md | 基于微软 AutoGen 的企业级金融分析系统：VaR、压力测试、蒙特卡洛、量化选股 |
| 15 | [SeekMoney-ai](https://github.com/liangdabiao/SeekMoney-ai) | 159 | seekmoney-ai.md | 全视频社媒找商机：抖音/小红书/TikTok/B站/视频号/YouTube 采集 + 语义聚类 + 痛点评分 |
| 16 | [llm-wiki](https://github.com/liangdabiao/llm-wiki) | 156 | llm-wiki.md | 按 Karpathy 方法论用 AI 维护个人知识库，多源素材自动整理为 wiki，Quartz 发布并提供 API |
| 17 | [smy-seedance-storyboard](https://github.com/liangdabiao/smy-seedance-storyboard) | 137 | smy-seedance-storyboard.md | 上美影风（大闹天宫/九色鹿复古手绘）短剧文档生成器：故事进，出图出视频文档出 |
| 18 | [LLM-Agent-Resume](https://github.com/liangdabiao/LLM-Agent-Resume) | 127 | llm-agent-resume.md | 从 0 到 1 的 LLM 简历筛选系统：上传简历 + JD → 解析、检索、评分、排序、报告 |
| 19 | [Godogen](https://github.com/liangdabiao/Godogen) | 126 | godogen.md | 用 Claude Code 生成完整 Godot 4 项目的技能：架构/美术/代码/截图自检全自动（二开 htdt/godogen） |
| 20 | [video-clone-lite](https://github.com/liangdabiao/video-clone-lite) | 108 | video-clone-lite.md | 轻量视频复刻：给一条视频，自动换商品/换效果产出同结构新片，过程可控可改 |

## P1 · 中优先（star 30–99，19 篇）

| # | 仓库 | star | 建议文档名 | 一句话说明 |
|---|------|-----|-----------|-----------|
| 21 | [easy-amazon-voc](https://github.com/liangdabiao/easy-amazon-voc) | 77 | easy-amazon-voc.md | 上传 Easy Scraper 爬取的评论 CSV，AI 多维分析出用户画像，下载带分析结果的 CSV |
| 22 | [skill-ten-prompt-generator](https://github.com/liangdabiao/skill-ten-prompt-generator) | 72 | skill-ten-prompt-generator.md | 10 个场景化提示词专家 + 自动路由，基于 Claude Code Agent Skills 的提示词生成系统 |
| 23 | [wordpress_kefu_ai_agent](https://github.com/liangdabiao/wordpress_kefu_ai_agent) | 68 | wordpress-kefu-ai-agent.md | 不用 coze/dify 的 WordPress 自适应智能客服，2 个文件即可部署 |
| 24 | [lark-workflow-feishu-cli](https://github.com/liangdabiao/lark-workflow-feishu-cli) | 68 | lark-workflow-feishu-cli.md | 飞书 AI 效率系统：20 大工作流 Skill，基于 lark-cli 的个人效率基础设施 |
| 25 | [investment_Agent_langgraph_crewai](https://github.com/liangdabiao/investment_Agent_langgraph_crewai) | 59 | investment-agent-langgraph-crewai.md | 基于 CrewAI 的 A 股智能投研系统，多智能体协作决策（教育研究用途） |
| 26 | [ai-make-face-meme](https://github.com/liangdabiao/ai-make-face-meme) | 59 | ai-make-face-meme.md | NanoMotion：Next.js 应用，上传图片经 apiz.ai（nano-banana-2）并行生成 12 帧定格动画并导出 GIF |
| 27 | [ecom-details-image-ui](https://github.com/liangdabiao/ecom-details-image-ui) | 58 | ecom-details-image-ui.md | ecom-details-image 的 Web 版：一句中文 30 秒出电商图，基于 EdgeOne Makers 免费额度 |
| 28 | [fetch-everything](https://github.com/liangdabiao/fetch-everything) | 48 | fetch-everything.md | Claude Code/openclaw 技能合集：网页抓取、文档提取、电商数据、云端部署，强化中文平台 |
| 29 | [social_research_agent](https://github.com/liangdabiao/social_research_agent) | 44 | social-research-agent.md | "微舆"：社媒（TikHub）+ Web Search 两个 skill 合体的深度调研智能体 |
| 30 | [claudesdk-amazon-skills-chat](https://github.com/liangdabiao/claudesdk-amazon-skills-chat) | 42 | claudesdk-amazon-skills-chat.md | Claude Agent SDK 版亚马逊卖家助手，集成 54 个技能，对话完成选品/Listing/PPC 全链路 |
| 31 | [Multimodal-RAG](https://github.com/liangdabiao/Multimodal-RAG) | 41 | multimodal-rag.md | 不做文本提取/OCR 的多模态 RAG：PDF 页面直接视觉编码，完整保留表格图表排版批注 |
| 32 | [SKILL-kefu](https://github.com/liangdabiao/SKILL-kefu) | 39 | skill-kefu.md | LangChain/LangGraph 完整智能客服方案：记忆、RAG、情绪、工单、多 Agent、MCP 11 章合集 |
| 33 | [llm-wiki-claude-agent-sdk-agentic-rag](https://github.com/liangdabiao/llm-wiki-claude-agent-sdk-agentic-rag) | 39 | llm-wiki-claude-agent-sdk-agentic-rag.md | llm-wiki + Claude Agent SDK 组成的 agentic RAG：AI 当"知识编译器" |
| 34 | [simple_claude_deep_research_agent](https://github.com/liangdabiao/simple_claude_deep_research_agent) | 37 | simple-claude-deep-research-agent.md | Claude Code 简化版多智能体研究系统：主导代理 + 并行研究子代理 + 引用代理 |
| 35 | [perlerBeadsApplet](https://github.com/liangdabiao/perlerBeadsApplet) | 35 | perler-beads-applet.md | Taro + Vue3 拼豆像素画小程序：编辑、作品管理、图片导入、图纸导出（二开 noir017） |
| 36 | [Geogebra-WebChat](https://github.com/liangdabiao/Geogebra-WebChat) | 35 | geogebra-webchat.md | 聊天 + AI + GeoGebra 画图的极简 Web 应用，一句话搞定数学几何绘图 |
| 37 | [claudesdk-skill](https://github.com/liangdabiao/claudesdk-skill) | 35 | claudesdk-skill.md | Claude Agent SDK 能力实验：AI 读 SDK 文档自主构建 TikHub 社媒对话 Webapp |
| 38 | [deep_search_write](https://github.com/liangdabiao/deep_search_write) | 32 | deep-search-write.md | 写作 Agent + 知识库 Agent 双智能体，产出图文并茂的公众号/小红书/博客帖子 |
| 39 | [claudesdk-seedance-chat](https://github.com/liangdabiao/claudesdk-seedance-chat) | 30 | claudesdk-seedance-chat.md | Claude Agent SDK 版 Seedance 2.0 视频脚本/分镜创作 Web 应用 |

## P2 · 常规补充（star 11–29，21 篇）

| # | 仓库 | star | 建议文档名 | 一句话说明 |
|---|------|-----|-----------|-----------|
| 40 | [wecomcli_crm](https://github.com/liangdabiao/wecomcli_crm) | 28 | wecomcli-crm.md | 基于 wecom-cli 的企业微信 Agent 工作台：AI 驱动 CRM、消息、会议日程 |
| 41 | [dsh-plugin-developer-skill](https://github.com/liangdabiao/dsh-plugin-developer-skill) | 26 | dsh-plugin-developer-skill.md | DeepSeek Harness 插件开发 Skill：从 0 到 1 开发构建测试 dsh 插件，附天气插件实例 |
| 42 | [product-motion-gif](https://github.com/liangdabiao/product-motion-gif) | 26 | product-motion-gif.md | GPT-Image 2.5 一次出多格帧图合成产品动图 GIF，面向不会设计软件的人 |
| 43 | [HSTECH_2026_AI_SUMMARY](https://github.com/liangdabiao/HSTECH_2026_AI_SUMMARY) | 26 | hstech-2026-ai-summary.md | 用股票尽调 Agent 对恒生科技成分股做的 2026 全面分析报告 |
| 44 | [claudesdk-ecom-image-chat](https://github.com/liangdabiao/claudesdk-ecom-image-chat) | 23 | claudesdk-ecom-image-chat.md | Claude Agent SDK 版电商视觉 Web 应用：25 个场景模板 + GPT-Image-2 直接出图 |
| 45 | [AI_data_hub](https://github.com/liangdabiao/AI_data_hub) | 20 | ai-data-hub.md | AI 项目数据中心：Mongo/PG/向量库 + 多模态 + OSS + RAG + 爬虫 + FastAPI 一体化 |
| 46 | [liangdabiao.github.io](https://github.com/liangdabiao/liangdabiao.github.io) | 17 | liangdabiao-github-io.md | Agent 技术教学站：百炼、LangGraph、Claude/OpenAI Agent SDK、DeepAgents、EdgeOne 等课程 |
| 47 | [ai-investor](https://github.com/liangdabiao/ai-investor) | 17 | ai-investor.md | 基于 OpenAI Agents SDK 的用户需求洞察分析师，三段式框架 10 分钟出洞察 |
| 48 | [claudesdk-financial-chart-chat](https://github.com/liangdabiao/claudesdk-financial-chart-chat) | 16 | claudesdk-financial-chart-chat.md | Claude Agent SDK 财经图表助手：自然语言查 A 股数据出 6 种专业图表 |
| 49 | [dingtalk-cli-workflow](https://github.com/liangdabiao/dingtalk-cli-workflow) | 15 | dingtalk-cli-workflow.md | 钉钉 AI 效率系统：10 大工作流 Skill，飞书版的钉钉迁移 |
| 50 | [claudesdk-market-insight-chat](https://github.com/liangdabiao/claudesdk-market-insight-chat) | 15 | claudesdk-market-insight-chat.md | Claude Agent SDK 版用户洞察平台：三段式框架（画像→情绪→机会） |
| 51 | [do-deepagents-skill](https://github.com/liangdabiao/do-deepagents-skill) | 14 | do-deepagents-skill.md | LangChain DeepAgents 框架指导 Skill：多步推理、多工具、长会话的深度智能体 |
| 52 | [monica-crm-claude-skill](https://github.com/liangdabiao/monica-crm-claude-skill) | 13 | monica-crm-claude-skill.md | "聊天就是 CRM"：在 Claude Code/openclaw 里边聊边系统管理客户信息 |
| 53 | [claudesdk-exa-chat](https://github.com/liangdabiao/claudesdk-exa-chat) | 13 | claudesdk-exa-chat.md | Claude Agent SDK + Exa 的 AI 搜索研究平台：企业/外贸/竞品多维调研 |
| 54 | [claudesdk-amazon-chat](https://github.com/liangdabiao/claudesdk-amazon-chat) | 12 | claudesdk-amazon-chat.md | 亚马逊竞品 Listing 全维度穿透分析：文案、评论情感、关键词、市场动态出报告 |
| 55 | [langgraph-runtime-skill-agent](https://github.com/liangdabiao/langgraph-runtime-skill-agent) | 12 | langgraph-runtime-skill-agent.md | 把本地 Agent Skill 包成 HTTP/SSE API 服务，模型编排 + 脚本确定性执行 |
| 56 | [simple_ai_toolset](https://github.com/liangdabiao/simple_ai_toolset) | 12 | simple-ai-toolset.md | 面向后端程序员的类 Coze 基础框架：FastAPI、搜索、RPA、Agent、Mongo、多模态 |
| 57 | [ecom-details-image-plugin](https://github.com/liangdabiao/ecom-details-image-plugin) | 12 | ecom-details-image-plugin.md | ecom-details-image 的 dsh 插件版：在 DeepSeek Harness 里写合规电商 Prompt 并真实出图 |
| 58 | [lego-cinematic-remix](https://github.com/liangdabiao/lego-cinematic-remix) | 12 | lego-cinematic-remix.md | 乐高积木小镇 + 积木小人演戏 + 电影镜头的动画制片 Skill |
| 59 | [Simple-Agentic-Stack](https://github.com/liangdabiao/Simple-Agentic-Stack) | 11 | simple-agentic-stack.md | MCP + Skill 驱动的 Agent 编排：Skill 是程序、MCP 是库、LLM 是语言 |
| 60 | [lark-crm-feishu-cli](https://github.com/liangdabiao/lark-crm-feishu-cli) | 11 | lark-crm-feishu-cli.md | 基于飞书 CLI 的轻量 CRM Skill：多维表格封装成自然语言对话管理 |

---

## 主题分布速览

| 主题 | 数量 | 包含项目 |
|------|-----|---------|
| 电商 / 亚马逊 | 8 | #1 #4 #21 #27 #30 #44 #54 #57 |
| 金融投资 / A 股 | 7 | #2 #3 #10 #14 #25 #43 #48 |
| 智能客服 | 3 | #5 #23 #32 |
| 视频 / 动画 / 短剧 | 8 | #9 #11 #17 #20 #26 #39 #42 #58 |
| 商业验证 / 市场调研 | 6 | #12 #15 #29 #47 #50 #53 |
| 深度研究 / 数据分析 | 3 | #7 #8 #34 |
| 知识库 / RAG | 3 | #16 #31 #33 |
| 简历 / 招聘 | 2 | #13 #18 |
| Agent 框架与工程 | 13 | #19 #22 #28 #36 #37 #38 #41 #45 #51 #52 #55 #56 #59 |
| 拼豆 / 小程序 | 2 | #6 #35 |
| 办公效率（飞书/钉钉/企微） | 4 | #24 #40 #49 #60 |
| 教学站点 | 1 | #46 |

## 建议补充顺序

1. **先补 P0 的 20 篇**：其中 #1、#2、#3 是 300 star 以上的招牌项目，应最先补。
2. **再按主题打包补 P1**：建议同主题一次写齐（如金融 7 篇、电商 8 篇），便于在 index.html 中整组上架。
3. **P2 按需补充**：多为 P0/P1 项目的 SDK 版本或插件版本，可在主项目文档中互相引用，避免重复解释。
4. 每补一篇后，记得运行 [build_site.py](build_site.py) 同步 [README.md](README.md) 与 [index.html](index.html)，并更新文档总数（现有 78 → 最终 138）。
