# ProfitWell — `n8n-nodes-base.profitwell`
**Type** `n8n-nodes-base.profitwell` · **action**
**What:** Retrieve ProfitWell account settings and daily financial metrics (MRR, churn, etc.).
**Credentials:** `profitWellApi`

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Company | Get account settings |
| Metric | Get financial metrics broken down by day (current or last month) |

## Key params & gotchas
- Metric retrieval is scoped to either the current month or the previous month — no arbitrary date range.
- Metrics are aggregated daily; ideal for reporting/alerting workflows triggered on a schedule.
- ProfitWell has since rebranded/merged into Paddle; verify API availability for your account.

**Source:** n8n-nodes-base.profitwell.md  [doc-verified]
