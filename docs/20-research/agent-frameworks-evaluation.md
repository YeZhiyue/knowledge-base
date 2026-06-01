# Agent 框架调研：广告 Agent 场景初评

更新时间：2026-06-01

## 问题

哪些 Agent 框架适合 GEO / SEM 广告 Agent 场景，尤其是素材创建、投放、优化全链路？

## 短答案

首阶段建议采用“确定性工作流 + 可插拔 Agent 节点”的架构。广告链路有明确流程、预算风险、平台规则和人审要求，优先选择支持状态图、工具治理、可观测性、评测和人工确认的框架。

初步判断：

- 强流程编排和生产可控：优先看 LangGraph、OpenAI Agents SDK、Google ADK。
- Python 后端、结构化输出和强类型约束：重点看 Pydantic AI。
- 多 Agent 协作原型和业务自动化 demo：可看 CrewAI、AutoGen。
- 知识库 / RAG / 数据 Agent 深：可看 LlamaIndex Workflows。
- TypeScript 技术栈：可看 Mastra。

## 评价维度

| 维度 | 为什么重要 |
| --- | --- |
| 工作流可控性 | 广告投放有明确步骤和风险，不能完全黑盒自主执行 |
| 状态管理 | 素材、平台配置、投放指标、优化建议都需要跨步骤传递 |
| 工具接入 | 需要连接广告平台 API、素材库、报表、规则库、审核系统 |
| 人工确认 | 投放、预算、账户权限等动作必须有人审或可配置审批 |
| 结构化输出 | 投放配置、素材方案、诊断结论需要稳定 schema |
| 评测与回放 | 广告效果优化需要复盘每次 Agent 决策和输入输出 |
| 多模型适配 | 业务可能需要在成本、质量、延迟之间切换模型 |
| 部署与运维 | 要考虑服务化、队列、日志、权限、监控和灰度 |
| 团队学习成本 | 新团队要快速交付，框架不能过度复杂 |

## 候选框架初评

### OpenAI Agents SDK

官方入口：

- https://platform.openai.com/docs/guides/agents-sdk/
- https://openai.github.io/openai-agents-python/agents/
- https://openai.github.io/openai-agents-js/guides/agents/

适合点：

- 与 OpenAI 模型、工具调用、guardrails、handoffs 等能力结合紧。
- 适合快速搭建工具型 Agent 和多 Agent 协作原型。
- 对使用 OpenAI 生态的团队，上手和模型能力验证较快。

风险：

- 如果生产环境需要强多云模型适配或复杂状态图，可能还需要额外工作流层。
- 需要确认企业内可用模型、数据合规和部署约束。

广告 Agent 适配度：高。适合作为工具 Agent / Review Agent / 生成型 Agent 的基础。

### LangGraph

官方入口：

- https://langchain-ai.github.io/langgraph/

适合点：

- 强调状态图、可控流程、循环、分支和人机协同。
- 适合把广告链路拆成 Brief、Creative、Compliance、Launch、Analyst、Optimizer 等节点。
- 对“确定性流程 + 局部 Agent 推理”非常友好。

风险：

- 工程复杂度高于轻量 SDK。
- 需要团队对图状态、checkpoint、持久化和测试有清晰规范。

广告 Agent 适配度：很高。适合作为首阶段主编排层候选。

### Google ADK

官方入口：

- https://adk.dev/
- https://google.github.io/adk-docs/

适合点：

- 官方文档定位为灵活、模块化的 Agent 开发工具包。
- 与 Google 生态、Gemini、Google Cloud 部署链路可能更顺。
- 若目标平台强依赖 Google Ads / Google Cloud，值得重点验证。

风险：

- 需要确认团队云平台、模型生态和部署偏好。
- 若公司不是 Google 生态，集成收益可能下降。

广告 Agent 适配度：中高。若 GEO / SEM 首站包含 Google Ads，优先级提升。

### Microsoft AutoGen

官方入口：

- https://microsoft.github.io/autogen/

适合点：

- 多 Agent 对话、协作、工具调用和实验探索能力强。
- 适合复杂角色协作 demo，如策略 Agent、素材 Agent、分析 Agent 互相讨论。

风险：

- 对生产广告投放链路，仍需额外治理流程、状态和审批。
- 多 Agent 自由对话容易带来可解释性和稳定性问题。

广告 Agent 适配度：中。适合原型和研究，不建议首阶段作为唯一主框架。

### CrewAI

官方入口：

- https://docs.crewai.com/

适合点：

- 面向 agents、crews、flows 的业务自动化表达较直观。
- 适合快速搭建多角色协作型流程。

风险：

- 需要验证复杂状态管理、审计、评测和生产运维能力。
- 对严格预算/权限场景，需要额外工程保障。

广告 Agent 适配度：中。适合业务原型和自动化演示。

### Pydantic AI

官方入口：

- https://ai.pydantic.dev/
- https://pydantic.dev/docs/validation/dev/examples/pydantic_ai/

适合点：

- 强类型、结构化输出、校验能力与广告配置 schema 很匹配。
- Python 后端友好，适合把 Agent 输出收敛成稳定对象。

风险：

- 若需要复杂多 Agent 状态图，可能需要搭配工作流框架。

广告 Agent 适配度：高。适合作为结构化输出和工具 Agent 层。

### LlamaIndex Workflows / Agents

官方入口：

- https://docs.llamaindex.ai/en/stable/use_cases/agents/
- https://docs.llamaindex.ai/en/stable/understanding/agent/multi_agent/

适合点：

- 知识库、RAG、数据 Agent 能力成熟。
- 对广告规则库、素材资产库、历史案例库和指标解释库有价值。

风险：

- 作为主投放编排层前，需要验证工作流控制、审批和平台执行能力。

广告 Agent 适配度：中高。适合知识检索、素材/案例召回、指标解释。

### Mastra

官方入口：

- https://mastra.ai/
- https://mastra.ai/framework
- https://mastra.ai/agents

适合点：

- TypeScript Agent 框架，强调 agents、workflows、memory、tools、MCP 和多模型。
- 如果团队前后端或平台工具偏 TS，可能更易集成。

风险：

- 需要验证与现有后端、广告 API、部署体系的匹配度。

广告 Agent 适配度：中。TS 技术栈下值得验证。

## 初步推荐路线

### 路线 A：LangGraph 主编排 + Pydantic AI/结构化输出 + LlamaIndex 知识库

适合：广告链路强流程、强状态、强评测的生产方案。

### 路线 B：OpenAI Agents SDK 快速原型 + 工作流层补治理

适合：快速验证模型能力、工具调用和多 Agent 分工。

### 路线 C：Google ADK 优先

适合：强 Google Ads / Google Cloud / Gemini 生态约束。

## 下一步实验

1. 选一个真实但脱敏的 SEM brief，做素材生成 -> 合规检查 -> 投放配置草稿 -> 优化建议的最小闭环。
2. 用 LangGraph 和 OpenAI Agents SDK 各实现一次，比较代码复杂度、稳定性和可解释性。
3. 引入 Pydantic schema，验证 Agent 输出是否能稳定转成投放配置对象。
4. 建立 10 条评测样例，覆盖正常、违规、预算风险、平台参数缺失、指标异常等情况。

## 待确认

- 公司技术栈偏 Python、Java、Go 还是 TypeScript？
- 生产模型供应商和合规要求是什么？
- 投放动作是否允许 Agent 自动执行？
- 首批平台 API 和报表 API 是哪些？
