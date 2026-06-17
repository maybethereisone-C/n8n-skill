# SecurityScorecard — `n8n-nodes-base.securityscorecard`
**Type** `n8n-nodes-base.securityscorecard` · **action**
**What:** Access SecurityScorecard risk ratings — company scores, industry benchmarks, portfolio management, invites, and report generation.
**Credentials:** `securityScorecardApi`

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Company | Get factor scores & issue counts, Get historical factor scores, Get historical scores, Get info & scorecard summary, Get score improvement plan |
| Industry | Get Factor Scores, Get Historical Factor Scores, Get Score |
| Invite | Create invite for a company/user |
| Portfolio | Create, Delete, Get All, Update |
| Portfolio Company | Add company, Get All, Remove company |
| Report | Download generated report, Generate report, Get list of recent reports |

## Key params & gotchas
- Company domain (e.g., `example.com`) is the primary identifier — not company name.
- Report generation is async; call "Generate report" then poll or use "Get list of recently generated reports" before downloading.
- Portfolio operations require a portfolio ID; create one first if none exist.
- Industry scores use predefined industry slugs (e.g., `technology`, `healthcare`).
- API key must have appropriate permissions for portfolio and report operations.

**Source:** n8n-nodes-base.securityscorecard.md  [doc-verified]
