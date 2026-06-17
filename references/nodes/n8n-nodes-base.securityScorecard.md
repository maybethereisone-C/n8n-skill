# SecurityScorecard  (`n8n-nodes-base.securityScorecard`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: securityScorecardApi
- resources: company, industry, invite, portfolio, portfolioCompany, report
- operations: add, create, delete, download, generate, getAll, getFactor, getFactorHistorical, getHistoricalScore, getScore, getScorePlan, getScorecard, remove, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | company | true |  |
