# Bubble — `n8n-nodes-base.bubble`
**Type** `n8n-nodes-base.bubble` · **action**
**What:** Create, read, update, and delete objects (records) in Bubble no-code app databases.
**Credentials:** Bubble API key credential (app name + API key + environment).

## Resources / Operations
| Resource | Operations |
|---|---|
| Object | Create, Delete, Get, Get All, Update |

## Key params & gotchas
- **Type name** corresponds to a Bubble data type (table) — must match exactly as defined in your Bubble app.
- **Environment** in the credential selects between development and live — ensure the correct environment is set.
- "Get All" uses Bubble's Data API pagination; use **Return All** or set **Limit** and **Cursor** for large datasets.
- Bubble field names in API calls use the field's API name (set in Data tab → field settings), which may differ from the display name.
- Bubble API must be enabled in Settings → API → Enable Data API and the specific type must have API access enabled.

**Source:** n8n-nodes-base.bubble.md  [doc-verified]
