# 钛动科技 GEO / SEM 广告 Agent 知识库

[![GitHub Pages](https://github.com/YeZhiyue/knowledge-base/actions/workflows/pages.yml/badge.svg)](https://github.com/YeZhiyue/knowledge-base/actions/workflows/pages.yml)
[![Docs Validation](https://github.com/YeZhiyue/knowledge-base/actions/workflows/validate-docs.yml/badge.svg)](https://github.com/YeZhiyue/knowledge-base/actions/workflows/validate-docs.yml)

这个仓库用于沉淀未来去钛动科技做 GEO / SEM 广告 Agent 方向所需的业务、技术和工作流知识。当前目标不是做一个单点工具说明，而是逐步整理出一套可由 GitBook 阅读、可由 GitHub 版本化、可由 Codex Cloud 长期维护的知识库结构。

## 知识库目标

- 建立广告 Agent 的统一项目上下文。
- 梳理 GEO / SEM、素材创建、投放执行、效果优化的核心链路。
- 对 Agent 框架进行可追溯的选型调研。
- 设计可适配多广告平台的参考架构。
- 沉淀风控、审计、评测和人工确认方法。
- 准备入职前学习计划和入职后问题清单。

## 推荐阅读路径

1. 阅读 [广告 Agent 总览](docs/10-projects/taidong-ad-agent/ad-agent-overview.md)，先理解业务目标和知识库边界。
2. 阅读 [项目 Brief](docs/10-projects/taidong-ad-agent/brief.md)，确认当前事实、判断、假设和待确认问题。
3. 阅读 [GEO / SEM 基础](docs/20-research/geo-sem-basics.md)，补齐广告业务基础。
4. 阅读 [Agent 框架调研](docs/20-research/agent-frameworks-evaluation.md)，理解框架选型标准。
5. 阅读 [广告 Agent 参考架构](docs/20-research/ad-agent-reference-architecture.md)，把业务链路映射到系统模块。
6. 阅读 [素材创建、投放、优化工作流](docs/10-projects/taidong-ad-agent/creative-launch-optimization-workflow.md)，理解端到端工作流。
7. 阅读 [风控、审计与评测](docs/20-research/risk-audit-evaluation.md)，明确生产化边界。
8. 阅读 [入职前学习计划](docs/10-projects/taidong-ad-agent/pre-onboarding-learning-plan.md) 和 [公司学习地图](docs/10-projects/taidong-ad-agent/company-learning-map-clean-room.md)，安排后续行动。

## 核心模块

| 模块 | 说明 |
| --- | --- |
| 广告 Agent 总览 | 项目目标、核心链路、知识库边界和近期问题 |
| GEO / SEM 基础 | 搜索广告、生成式搜索、关键词、素材、转化和优化基础 |
| Agent 框架选型 | OpenAI Agents SDK、LangGraph、Google ADK、Pydantic AI 等候选方案 |
| 广告 Agent 架构 | 任务入口、流程编排、工具接入、状态管理、评测和审计 |
| 工作流 | 素材创建、投放配置、指标回收、诊断优化和复盘闭环 |
| 风控评测 | 预算、权限、合规、品牌安全、审计日志和回放样例 |
| 学习计划 | 入职前阶段计划、入职后访谈问题和持续维护方式 |

## 仓库结构

```text
README.md                 GitBook 首页
SUMMARY.md                GitBook 导航目录
.gitbook.yaml             GitBook Git Sync 解析配置
AGENTS.md                 Codex 维护规则
docs/
  10-projects/            项目上下文、学习计划、工作流、Backlog
  20-research/            框架、业务、架构、风控和评测调研
  30-decisions/           决策记录
  40-playbooks/           Codex Cloud 和发布维护流程
  90-templates/           调研和决策模板
  publishing/             GitBook 发布与同步说明
private/
  internal-learning/      仅私人学习使用的原始材料，不进入公开 GitBook 主导航
```

## GitHub Pages 发布方式

本仓库推荐使用 GitHub Pages 发布文档站：

- 使用 HonKit 直接读取 `README.md` 和 `SUMMARY.md`。
- 推送到 `main` 后由 GitHub Actions 构建 `_book/`。
- 构建产物通过 GitHub Pages 发布。
- 后续只需要维护 Markdown 内容和 `SUMMARY.md` 导航。

详细步骤见 [GitHub Pages + HonKit 发布指南](docs/publishing/github-pages-honkit.md)。

## GitBook 同步方式

本仓库仍保留 GitBook Git Sync 兼容配置：

- 仓库根目录放置 `README.md` 作为首页。
- 仓库根目录放置 `SUMMARY.md` 作为导航目录。
- 仓库根目录放置 `.gitbook.yaml`，显式声明 `root: ./`、`structure.readme` 和 `structure.summary`。
- 在 GitBook 中连接 GitHub 仓库时，Project directory 选择仓库根目录 `/`。

详细步骤见 [GitBook 发布与同步指南](docs/publishing/gitbook-setup.md)。

## Clean-Room 知识沉淀原则

涉及 ATA、语雀、公司内部会议、内部系统、内部试用、客户项目或未公开材料时，只允许保留个人抽象后的通用学习结论，不能复制内部原文。

必须遵守：

- 不复制 ATA、语雀、内部文档、内部群聊、内部系统页面的原文。
- 不上传内部截图、报表、接口文档、客户信息、账户信息、预算信息或真实投放数据。
- 不记录公司内部系统实现细节、权限配置、密钥、token、cookie、账号密码。
- 可以保留学习主题、问题清单、通用方法论、公开资料链接和个人复盘。
- 无法判断是否可公开的内容，归入 `private/internal-learning/` 并标注“仅私人学习使用”，不要加入 `SUMMARY.md`。

## Codex Cloud 维护方式

每次让 Codex Cloud 继续维护时，建议先读取：

1. `AGENTS.md`
2. `README.md`
3. `SUMMARY.md`
4. [项目 Brief](docs/10-projects/taidong-ad-agent/brief.md)
5. 与任务相关的 research、decision 或 playbook 文件

推荐任务提示词：

```text
请先阅读 AGENTS.md、README.md、SUMMARY.md 和 docs/10-projects/taidong-ad-agent/brief.md。
本次任务：<具体任务>。
要求：只新增或更新 docs/ 下合适位置的 Markdown，保持 GitBook 可读性；
涉及内部来源时遵守 Clean-Room 原则；
新增公开页面时同步更新 SUMMARY.md；
最后列出改动文件、判断依据、待确认问题和下一步建议。
```
