# Adalo — `n8n-nodes-base.adalo`
**Type** `n8n-nodes-base.adalo` · **action**
**What:** Read and write records in Adalo no-code app databases via the Adalo API.
**Credentials:** Adalo API key credential.

## Resources / Operations
| Resource | Operations |
|---|---|
| Collection | Create, Delete, Get, Get Many, Update |

## Key params & gotchas
- **App ID** and **Collection ID** are both required — find them in your Adalo app URL and the External Collections settings panel.
- Field names must match your Adalo collection schema exactly (case-sensitive).
- Adalo's External Collections API uses REST; all fields are passed as JSON body. Unknown fields are silently ignored.
- "Get Many" returns all records by default; no server-side filtering — filter downstream with an n8n Filter node.

**Source:** n8n-nodes-base.adalo.md  [doc-verified]
