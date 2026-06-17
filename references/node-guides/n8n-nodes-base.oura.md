# Oura — `n8n-nodes-base.oura`
**Type** `n8n-nodes-base.oura` · **action**
**What:** Read personal health data (profile, activity, readiness, sleep) from the Oura Ring API.
**Credentials:** `ouraApi`

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Profile | Get the user's personal information |
| Summary | Get activity summary |
| Summary | Get readiness summary |
| Summary | Get sleep summary |

## Key params & gotchas
- All Summary operations are read-only; date range filtering is expected via query parameters on the underlying API but may require Additional Fields or expressions.
- Oura uses OAuth2 — credentials must be authorized before use.
- Sleep/readiness data has ~24 h lag; don't expect real-time values.

**Source:** n8n-nodes-base.oura.md  [doc-verified]
