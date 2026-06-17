# Gong — `n8n-nodes-base.gong`
**Type** `n8n-nodes-base.gong` · **typeVersion** 1 · **action**
**What:** Retrieves call recordings/metadata and user data from Gong revenue intelligence platform.
**Credentials:** `gongApi` (Access Key + Secret from Gong API settings).

**Resources / Operations:**

| Resource | Operations |
|---|---|
| Call | Get, Get Many |
| User | Get, Get Many |

**Key params & gotchas:**
- Call > Get Many returns paginated results; use cursor-based pagination — the node exposes a cursor field in additional fields.
- Gong API credentials are workspace-scoped; ensure the API key belongs to a user with the right data scope (calls may be restricted by workspace visibility settings).
- Call data includes transcripts only if transcription is enabled for the workspace and the call has been processed; newly completed calls may not be available immediately.

**Source:** n8n-nodes-base.gong.md  [doc-verified]
