# KoboToolbox — `n8n-nodes-base.kobotoolbox`
**Type** `n8n-nodes-base.kobotoolbox` · **typeVersion** 1 · **action**
**What:** Access KoboToolbox survey forms, submissions, webhooks (hooks), and file attachments for humanitarian/field data collection workflows.
**Credentials:** `koboToolboxApi` (API token + server URL — koboToolbox.org or self-hosted).

## Resources / Operations
| Resource | Operations |
|---|---|
| File | Create, Delete, Get, Get Many |
| Form | Get, Get Many, Redeploy |
| Hook | Get, Get Many, Logs, Retry All, Retry One |
| Submission | Delete, Get, Get Many, Get Validation Status, Update Validation Status |

## Key params & gotchas
- **Submission→Get Many** supports MongoDB-style **Query** filter (e.g. `{"status":"success","_submission_time":{"$lt":"2021-11-01"}}`), **Sort**, and **Fields** to reduce payload.
- API hard limit: 30,000 records max regardless of Limit param; use **Start** offset + **Limit** for pagination.
- **Reformat** option on submission operations: restructures flat `Group/Question` keys into nested JSON, parses GeoJSON, splits multi-select into arrays, and converts numeric fields — requires **Multiselect Mask** and **Number Mask** wildcard patterns (e.g. `Crops_*`, `*_sqm`).
- **Hook→Retry** re-sends failed webhook deliveries — useful when downstream systems were temporarily down.
- **Form→Redeploy** republishes a form after schema changes — required for new questions to appear in submissions.
- Attachment download (File operations) returns binary data; large media files can be slow.

**Source:** n8n-nodes-base.kobotoolbox.md  [doc-verified]
