# AI 项目的一体化数据底座 —— ai-data-hub 介绍

一个给 AI 项目用的数据中心，覆盖数据摄取、加工、探索、检索四大环节，整合了 MongoDB、Postgres/Supabase、Chroma/Milvus、阿里云 OSS，外加 LangChain、多模态、RAG、爬虫和 FastAPI。

## 它能做什么

- Ingestion / Transform / Explore / Retrieve 全流程
- 整合关系库、文档库、向量库和对象存储
- 内置 RAG、爬虫和基础 Agent
- FastAPI 对外提供接口

## 怎么用

按模块配置数据库连接后启动 FastAPI 服务。

## 适合谁 & 边界

搭 AI 应用的后端开发者。组件较多，按需启用。

## 仓库

https://github.com/liangdabiao/AI_data_hub
