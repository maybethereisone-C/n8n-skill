# QuickChart — `n8n-nodes-base.quickchart`
**Type** `n8n-nodes-base.quickchart` · **action**
**What:** Generate chart images (bar, doughnut, line, pie, polar) via the QuickChart API without credentials.
**Credentials:** none (public API)

## Resources / Operations
| Operation |
|-----------|
| Create Bar Chart |
| Create Doughnut Chart |
| Create Line Chart |
| Create Pie Chart |
| Create Polar Chart |

## Key params & gotchas
- Supports use as an AI tool node.
- Returns a chart image (PNG/SVG URL or binary); pipe output to email, Slack, or file storage nodes.
- No credentials required for the public QuickChart.io endpoint; rate limits apply on free tier.
- Chart data and labels are configured in node parameters; complex chart.js config can be passed as JSON.
- For high-volume use, consider a self-hosted QuickChart instance.

**Source:** n8n-nodes-base.quickchart.md  [doc-verified]
