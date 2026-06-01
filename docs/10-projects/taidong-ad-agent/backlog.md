# 钛动科技广告 Agent Backlog

更新时间：2026-06-01

## 使用方式

每个任务都应该能直接复制给 Codex Cloud 执行。任务结束后，把结论同步回 `docs/`，并标注事实、判断、假设、待确认问题。

## P0：入场前必须完成

### T1. 盘点广告 Agent 目标场景

目标：把 GEO / SEM 的业务链路拆到可执行粒度。

建议提示词：

```text
请阅读 README.md、AGENTS.md、docs/10-projects/taidong-ad-agent/brief.md，补充 docs/10-projects/taidong-ad-agent/scenario-map.md。要求拆解 GEO/SEM 广告 Agent 的用户、输入、输出、工具、风险点、人工确认点和衡量指标。区分事实、判断、假设、待确认问题。
```

### T2. Agent 框架第一轮调研

目标：比较 OpenAI Agents SDK、LangGraph、Google ADK、AutoGen、CrewAI、Pydantic AI、LlamaIndex Workflows、Mastra。

建议提示词：

```text
请基于官方文档核验 docs/20-research/agent-frameworks-evaluation.md，补充每个框架的核心能力、适合场景、生产化风险、广告 Agent 适配度和来源链接。不要使用二手文章替代官方资料。
```

### T3. 内部试用问题清单

目标：形成入职后访谈和系统盘点问题。

建议提示词：

```text
请基于 docs/10-projects/taidong-ad-agent/brief.md 生成 docs/10-projects/taidong-ad-agent/internal-trial-questions.md，列出入职后需要向产品、算法、投放运营、平台工程分别确认的问题。
```

## P1：形成方案雏形

### T4. 广告 Agent 参考架构

输出：`docs/20-research/ad-agent-reference-architecture.md`

关注点：

- 任务编排
- 工具接入
- 记忆与知识库
- 素材资产库
- 规则与合规
- 评测与回放
- 权限与审计

### T5. 素材创建链路设计

输出：`docs/10-projects/taidong-ad-agent/creative-agent-design.md`

关注点：

- 输入 brief
- 卖点抽取
- 平台规则
- 多版本生成
- 人审与打标
- 效果回流

### T6. 投放优化链路设计

输出：`docs/10-projects/taidong-ad-agent/optimization-agent-design.md`

关注点：

- 指标体系
- 异常诊断
- 策略建议
- 平台执行
- 预算风险控制

## P2：持续沉淀

- 建立广告平台 API 资料索引。
- 建立广告指标词典。
- 建立素材生成 SOP 和评测样例集。
- 建立 Agent 失败案例库。
- 建立面向团队沟通的术语表。
