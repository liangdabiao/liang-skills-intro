# 把本地 Skill 一键变成 HTTP API —— langgraph-runtime-skill-agent 介绍

基于 langgraph-runtime 加 Skill 的 agent，把本地 Agent Skill 包装成 HTTP API 服务。用户发 SSE 请求，agent 自动选择技能、读取 SKILL.md、调用脚本或搜索网页，再流式返回结果。

## 它能做什么

- 本地 Skill 自动包装成 HTTP/SSE API
- 模型负责判断和编排
- 脚本负责确定性执行
- 流式返回，方便接前端

## 怎么用

把 Skill 放入目录，启动 runtime 后发请求。

## 适合谁 & 边界

想把技能产品化的开发者。适合流程清晰的任务。

## 仓库

https://github.com/liangdabiao/langgraph-runtime-skill-agent
