# GitHub Pages + HonKit 发布指南

更新时间：2026-06-01

## 推荐方案

本仓库推荐使用 `GitHub Pages + HonKit` 发布文档站。原因是当前知识库已经按 GitBook 风格维护了 `README.md` 和 `SUMMARY.md`，HonKit 可以直接复用这两个文件生成静态网站，不需要维护第二套导航。

## 工作方式

```text
README.md / SUMMARY.md / docs/**/*.md
  -> HonKit build
  -> _book/
  -> GitHub Pages
  -> https://yezhiyue.github.io/knowledge-base/
```

`.bookignore` 会阻止 `private/`、`.github/`、`scripts/`、`node_modules/` 等非公开内容被复制到 `_book/`。

## 本地预览

首次安装依赖：

```bash
npm ci
```

构建静态站：

```bash
npm run docs:build
```

本地预览：

```bash
npm run docs:serve
```

## GitHub Actions 流水线

仓库包含两个工作流：

| 文件 | 用途 |
| --- | --- |
| `.github/workflows/validate-docs.yml` | 校验 Markdown 链接、导航、GitBook/HonKit 入口文件和高置信度密钥 |
| `.github/workflows/pages.yml` | 安装 HonKit、构建 `_book/`、发布到 GitHub Pages |

`pages.yml` 在 PR 中只构建验证；仓库仍为 private 时也只构建验证。仓库改为 public 后，推送到 `main` 或手动触发 workflow 会发布到 GitHub Pages。

## GitHub 仓库设置

如果仓库使用 GitHub Free，并且希望用 GitHub Pages 免费公开访问，需要把仓库设为 public。

然后进入：

```text
Settings -> Pages -> Build and deployment -> Source
```

选择：

```text
GitHub Actions
```

发布成功后，站点地址通常是：

```text
https://yezhiyue.github.io/knowledge-base/
```

## 公开前的安全处理

当前私有仓库历史中曾经包含私人学习材料。把仓库设为 public 前，不能只删除当前文件，还需要确保 Git 历史中没有私人材料。

推荐做法：

1. 保留当前私有仓库作为工作副本。
2. 新建一个干净的 public 仓库，首次只推送公开安全的当前文件。
3. 或者在当前仓库中重写 Git 历史，删除 `private/internal-learning/` 和早期 `docs/00-inbox/` 原始材料后，再改为 public。

不要在未清理历史的情况下直接把当前仓库设为 public。

## 后续维护规则

- 新增公开页面时，同步更新 `SUMMARY.md`。
- 不把 `private/` 加入 `SUMMARY.md`。
- 不提交内部截图、内部原文、客户数据、账户 ID、预算、密钥。
- 每次推送后查看 GitHub Actions 是否通过。
