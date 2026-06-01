# 0001 知识库运作方式

状态：accepted

日期：2026-06-01

## 背景

未来需要使用 Codex Cloud 持续跟进钛动科技相关的广告 Agent 项目。为了让每次云端任务都能继承上下文，需要先建立稳定的知识沉淀结构，而不是把信息散落在聊天记录里。

## 决策

采用轻量但可持续的 Markdown 知识库结构：

```text
docs/
  10-projects/     项目上下文和执行计划
  20-research/     调研记录
  30-decisions/    决策记录
  40-playbooks/    可复用工作流
  90-templates/    模板
private/
  internal-learning/ 仅私人学习使用的原始材料
```

## 原则

- 可公开的原始信息先保留来源和日期，再整理为 `docs/` 中的项目或调研页面。
- 私人或内部来源材料进入 `private/internal-learning/`，不加入 GitBook 主导航。
- 项目结论进入 `10-projects`。
- 调研进入 `20-research`，优先引用官方来源。
- 关键选择进入 `30-decisions`。
- 可重复执行的方法进入 `40-playbooks`。
- 每次任务结束必须留下下一步任务建议。

## 备选方案

### 方案 A：只用 README

优点：简单。

缺点：随着信息增加会迅速混乱，不利于 Codex 读取局部上下文。

### 方案 B：完整知识库系统 / Notion 数据库

优点：查询和管理能力强。

缺点：初期维护成本高，和 Codex Cloud 的代码仓库工作流不如 Markdown 自然。

### 方案 C：当前 Markdown 目录结构

优点：轻量、可版本化、适合 Codex Cloud 读写、便于 Review。

缺点：需要坚持命名和归档纪律。

## 后果

- Codex Cloud 每次任务可以先读 `AGENTS.md`、`README.md` 和项目 brief。
- Git 历史天然记录知识演进。
- 后续可以逐步接入脚本、索引或静态站点，而不影响已有内容。

## 后续动作

- 保持 README 的快速入口更新。
- 每轮调研产生 research note。
- 每个关键技术路线产生 decision record。
