# Codex Cloud 工作流

更新时间：2026-06-01

## 目标

让 Codex Cloud 每次进入 `YeZhiyue/knowledge-base` 仓库时，都能快速理解项目上下文、执行明确任务，并把结果沉淀回仓库。

## 每次任务的推荐输入

```text
请先阅读 AGENTS.md、README.md 和 docs/10-projects/taidong-ad-agent/brief.md。
本次任务：<写清楚要完成的内容>。
要求：输出或更新 docs/ 下合适文件，区分事实、判断、假设、待确认问题。若涉及调研，请优先使用官方资料并保留来源链接。最后总结改动文件和下一步建议。
```

## 标准执行步骤

1. 读取上下文
   - `AGENTS.md`
   - `README.md`
   - `SUMMARY.md`
   - 项目 brief
   - 相关 backlog / research / decision 文件

2. 判断任务类型
   - 可公开的原始信息整理：写入合适的 `docs/` 页面
   - 私人或内部来源材料：写入 `private/internal-learning/`，并标注仅私人学习使用
   - 项目上下文更新：写入 `10-projects`
   - 技术/业务调研：写入 `20-research`
   - 关键路线选择：写入 `30-decisions`
   - 可复用流程：写入 `40-playbooks`
   - 模板：写入 `90-templates`

3. 输出文档
   - 使用 Markdown。
   - 标注日期。
   - 区分事实、判断、假设、待确认问题。
   - 调研结论必须写适用条件。

4. 自检
   - README 链接是否指向真实文件。
   - SUMMARY 是否包含新增公开页面。
   - 有没有泄露密钥、账号、客户数据或内部敏感材料。
   - 私人学习材料是否没有进入 GitBook 主导航。
   - 是否留下下一步可执行任务。

5. 汇报
   - 改了哪些文件。
   - 沉淀了什么结构或结论。
   - 还有哪些不确定。
   - 下一步推荐做什么。

## 适合 Codex Cloud 的任务粒度

### 好任务

- “补充 Agent 框架调研，要求引用官方文档并按评价维度打分。”
- “基于 brief 生成广告 Agent 参考架构。”
- “把会议纪要整理成 facts / judgments / assumptions / open questions。”
- “把某个技术选择写成 decision record。”

### 不好任务

- “把所有东西都研究一下。”
- “帮我看看这个项目。”
- “直接做完广告 Agent。”

## 安全边界

不要写入：

- API key、token、cookie、账号密码。
- 客户名称、真实投放预算、账户 ID、合同内容。
- 未脱敏的内部截图或报表。
- 任何无法公开给仓库协作者看的内容。

涉及 ATA、语雀、公司内部系统或内部试用材料时，只保留抽象后的学习方向、问题清单和通用方法论；原文、截图、接口、客户和账户信息不得进入 GitBook 公开导航。

## 当前推荐的下一轮云端任务

```text
请基于官方文档核验 docs/20-research/agent-frameworks-evaluation.md，并补充一个评分表。评分维度包括工作流可控性、状态管理、工具接入、人工确认、结构化输出、评测回放、多模型适配、部署运维、团队学习成本。最后给出首阶段推荐方案。
```
