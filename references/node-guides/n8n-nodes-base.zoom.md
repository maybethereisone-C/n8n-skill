# Zoom — `n8n-nodes-base.zoom`
**Type** `n8n-nodes-base.zoom` · **typeVersion** 1 · **action**
**What:** Create, retrieve, update, and delete Zoom meetings.
**Credentials:** `zoomOAuth2Api` (OAuth2 via Zoom Marketplace app) or `zoomApi` (JWT — deprecated by Zoom as of 2023).

## Resources / Operations
| Resource | Operations |
|---|---|
| Meeting | Create, Delete, Get, Get All, Update |

## Key params & gotchas
- Zoom deprecated JWT apps in September 2023; use OAuth2 (Server-to-Server OAuth or user OAuth) for new integrations.
- **Get All** returns meetings for the authenticated user by default; to list another user's meetings, the app must have admin-level scopes.
- Meeting **type** parameter controls what is returned: `scheduled`, `live`, or `upcoming` — default is scheduled.
- This node supports use as an **AI tool** (can be called by AI Agent nodes).

**Source:** n8n-nodes-base.zoom.md  [doc-verified]
