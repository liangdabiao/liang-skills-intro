# 28 个 AI 研究员并行干活的股票尽调系统 —— claude-code-stock-deep-research-agent 介绍

正经机构研究一只股票要拆成基本面、行业、竞品、风险等好多块。这个项目把这套流程做成 Claude Code 里的 skill：8 个尽调阶段、28 个并行研究智能体，自动上网搜资料、交叉验证，最后给你一份多空平衡的研报。

## 它能做什么

- 8 阶段股票投资尽调框架，流程完整
- 28 个智能体并行研究，速度快
- 自动调用 WebSearch / WebFetch 取证
- 强制多空平衡、明确标注风险

## 怎么用

在 Claude Code 里输入斜杠命令，如 `/stock-research AAPL, I want a quick overview`。

## 适合谁 & 边界

适合个人投资者和想学习 Deep Research 的开发者。结论仅供参考，需自己再核一遍。

## 仓库

https://github.com/liangdabiao/Claude-Code-Stock-Deep-Research-Agent
