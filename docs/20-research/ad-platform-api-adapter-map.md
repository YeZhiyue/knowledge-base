# 多广告平台 API 适配地图

更新时间：2026-06-01

## 问题

广告 Agent 如果要适配多个广告平台，哪些概念应该抽象成统一能力，哪些平台差异必须保留？

## 短答案

首阶段不要试图设计一个“完全统一”的广告平台模型。更稳妥的方式是抽象稳定的业务层对象，例如 Campaign、Ad Group / Ad Set、Creative、Keyword / Targeting、Budget、Report、Conversion，再通过平台适配器保留各平台差异。

Agent 只应面向统一的业务 schema 生成草案；真实平台执行由 adapter 负责转换、校验、降级和审计。

## 官方资料入口

| 平台 | 官方资料 |
| --- | --- |
| Google Ads | [Google Ads API 概览](https://developers.google.com/google-ads/api/docs/start)、[Account budgets](https://developers.google.com/google-ads/api/docs/billing/account-budgets)、[Reporting](https://developers.google.com/google-ads/api/docs/reporting/overview) |
| Meta | [Marketing API](https://developers.facebook.com/docs/marketing-apis/)、[Campaign API](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign/) |
| TikTok for Business | [TikTok Business API](https://business-api.tiktok.com/portal/docs)、[Campaign](https://business-api.tiktok.com/portal/docs?id=1739318962329602) |
| Microsoft Advertising | [Microsoft Advertising API](https://learn.microsoft.com/en-us/advertising/guides/)、[Campaign Management Service](https://learn.microsoft.com/en-us/advertising/campaign-management-service/campaign-management-service) |

## 统一抽象层

| 抽象对象 | 说明 | 平台差异 |
| --- | --- | --- |
| Account | 广告账户或客户账户 | 账户层级、权限、币种、时区、结算方式不同 |
| Campaign | 投放目标、预算、周期、平台级策略 | 目标类型、预算位置、状态枚举、出价策略差异很大 |
| Ad Group / Ad Set | 人群、关键词、版位、素材组合的中间层 | Google / Microsoft 偏 ad group；Meta / TikTok 偏 ad set / ad group |
| Creative / Ad | 标题、正文、图片、视频、落地页、CTA | 素材规格、审核规则、动态创意能力不同 |
| Keyword / Targeting | 搜索词、兴趣、行为、人群、地域、设备 | 搜索广告和信息流广告差异最大，不能强行统一 |
| Budget / Bid | 预算、出价、消耗节奏 | 日预算 / 总预算、竞价策略、上限控制不同 |
| Conversion | 转化事件、回传、归因窗口 | Pixel、SDK、离线回传、增强转化等机制不同 |
| Report | 指标、维度、时间粒度、归因口径 | 指标命名和归因口径不能直接横向比较 |

## Adapter 分层建议

```text
Agent 输出业务草案
  -> Unified Ads Schema
  -> Platform Adapter
  -> Platform Validation
  -> Draft / Preview / Human Approval
  -> Platform API Execution
  -> Audit Log
```

### Unified Ads Schema

用于收敛 Agent 输出，不直接等同任何平台 API。

建议字段：

- `objective`：投放目标。
- `platform`：目标平台。
- `account_ref`：账户引用，不记录真实账户 ID。
- `campaign`：投放计划草案。
- `groups`：广告组或 ad set 草案。
- `creatives`：素材草案。
- `targeting`：关键词、人群、地域、设备等约束。
- `budget`：预算草案和风险等级。
- `tracking`：转化追踪需求。
- `approval_required`：是否需要人工确认。
- `risk_notes`：预算、合规、账户、品牌风险。

### Platform Adapter

职责：

- 把统一 schema 转成平台 API 需要的字段。
- 补齐平台默认值或阻断缺失字段。
- 把平台错误码转成业务可读问题。
- 记录转换前后的字段映射。
- 支持只生成草稿，不直接执行。

### Platform Validation

执行前必须检查：

- 必填字段是否完整。
- 预算和出价是否超过安全阈值。
- 素材格式是否符合平台要求。
- 文案是否触发通用合规风险。
- 目标平台是否允许当前自动化动作。
- 是否需要人工审批。

## Agent 适配策略

### 推荐做法

- Agent 只生成平台无关的业务草案和明确的平台偏好。
- Adapter 做字段转换、枚举映射、错误处理和降级。
- 每个平台保留独立测试样例，避免统一抽象掩盖平台差异。
- 报表分析先做平台内诊断，再做跨平台归一化对比。
- 高风险动作只允许草稿模式或人工确认后执行。

### 不推荐做法

- 让 Agent 直接拼平台 API payload。
- 用一个表结构强行覆盖所有平台细节。
- 把不同平台的指标直接做横向比较。
- 把账户、预算、客户或真实报表数据写入知识库。
- 一开始就追求全平台自动执行。

## 首批实验建议

1. 选择 Google Ads 或 Microsoft Advertising 作为搜索广告实验平台，验证关键词、广告组、创意、报表诊断链路。
2. 选择 Meta 或 TikTok 作为信息流实验平台，验证素材、受众、版位、视频创意和投放目标差异。
3. 用同一个脱敏 brief 输出两个平台草案，对比统一 schema 是否足够表达平台差异。
4. 只生成草案和人审摘要，不接入真实账户执行。

## 待确认问题

- 首批平台到底是搜索广告、信息流广告，还是两者同时覆盖？
- 公司内部是否已有平台 adapter 或统一投放模型？
- 是否支持草稿模式、预览模式或沙箱账户？
- 报表 API 的延迟、归因口径和指标命名是否已经统一？
- 哪些平台动作允许 Agent 自动执行，哪些只能输出建议？
