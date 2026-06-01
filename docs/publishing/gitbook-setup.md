# GitBook 发布与同步指南

更新时间：2026-06-01

> 当前推荐发布路径已调整为 [GitHub Pages + HonKit](github-pages-honkit.md)。本页保留用于兼容 GitBook Git Sync。

## 当前仓库状态

本仓库已经按 GitBook Git Sync 的常见结构准备：

- `README.md`：GitBook 首页。
- `SUMMARY.md`：GitBook 左侧导航。
- `.gitbook.yaml`：显式声明仓库根目录、首页和目录文件。

当前 `.gitbook.yaml`：

```yaml
root: ./

structure:
  readme: README.md
  summary: SUMMARY.md
```

GitBook 官方文档说明，Git Sync 可以通过仓库根目录的 `.gitbook.yaml` 配置 `root`、`structure.readme` 和 `structure.summary`；如果仓库根目录存在 `README.md` 和 `SUMMARY.md`，GitBook 会使用它们作为首页和目录。

官方参考：

- https://gitbook.com/docs/getting-started/git-sync/content-configuration
- https://gitbook.com/docs/getting-started/git-sync
- https://gitbook.com/docs/getting-started/git-sync/monorepos

## 在 GitBook 连接 GitHub 仓库

1. 打开 GitBook，创建或进入目标 Space。
2. 进入 Git Sync 或 Integrations。
3. 选择 GitHub，并授权 GitBook GitHub App 访问 `YeZhiyue/knowledge-base`。
4. 选择仓库：`YeZhiyue/knowledge-base`。
5. 选择分支：`main`。
6. Project directory 选择仓库根目录 `/`。
7. 启用同步后，确认首页来自 `README.md`，左侧导航来自 `SUMMARY.md`。

## 同步 README.md / SUMMARY.md

- 首页内容只在 GitHub 仓库中维护 `README.md`。
- 导航内容只在 GitHub 仓库中维护 `SUMMARY.md`。
- 不要在 GitBook UI 中直接新建或修改 README 页面，避免和 GitHub 产生重复页面或同步冲突。
- 每新增一个公开页面，都要同步更新 `SUMMARY.md`。

## GitHub Actions 校验流水线

仓库已增加 `.github/workflows/validate-docs.yml`，每次 PR、推送到 `main` 或手动触发时会执行：

- 检查 `README.md`、`SUMMARY.md`、`.gitbook.yaml` 是否存在。
- 检查 `.gitbook.yaml` 是否声明 GitBook 首页和目录。
- 检查 `SUMMARY.md` 中的文件是否存在。
- 检查 `SUMMARY.md` 是否误引用 `private/` 私人学习材料。
- 检查 Markdown 相对链接是否可跳转。
- 检查公开文档中是否出现高置信度密钥格式。

GitBook Git Sync 连接完成后，`main` 分支每次更新会由 GitBook 自己同步。本仓库当前不再维护 GitBook API 发布流水线，默认发布路径为 GitHub Pages。

## 避免上传敏感内容

同步前必须人工检查：

- 是否包含 ATA、语雀、内部文档原文。
- 是否包含内部截图、客户名称、账户 ID、预算、真实报表、合同内容。
- 是否包含 API key、token、cookie、账号密码。
- 是否包含未公开接口、数据库结构、系统实现细节。
- 是否把仅私人学习材料加入了 `SUMMARY.md`。

可以用命令辅助检查，但不能替代人工判断：

```bash
rg -n "(api[_-]?key|token|secret|password|cookie|客户|预算|账户ID|ATA|语雀)" README.md SUMMARY.md docs private
```

## 后续让 Codex Cloud 继续维护

推荐提示词：

```text
请先阅读 AGENTS.md、README.md、SUMMARY.md 和 docs/10-projects/taidong-ad-agent/brief.md。
本次任务：<具体任务>。
要求：
1. 保持 GitBook 可读结构。
2. 新增公开页面时同步更新 SUMMARY.md。
3. 涉及内部来源时遵守 Clean-Room 原则。
4. 不写入密钥、客户数据、内部系统截图、内部文档原文。
5. 最后列出改动文件、验证结果、待确认问题和下一步建议。
```
