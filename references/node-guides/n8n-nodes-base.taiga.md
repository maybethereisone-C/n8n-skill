# Taiga — `n8n-nodes-base.taiga`
**Type** `n8n-nodes-base.taiga` · **typeVersion** 1 · **action**
**What:** Create, read, update, and delete issues in Taiga agile project management.
**Credentials:** `taigaApi`
**Resources / Operations:**
| Resource | Operations |
|---|---|
| Issue | Create, Delete, Get, Get All, Update |

**Key params & gotchas:**
- Requires a Project ID (numeric) — find it in the Taiga project URL or via the API.
- Issue type, status, and priority are referenced by ID, not name; look up IDs per project.
- Companion trigger node (`n8n-nodes-base.taigaTrigger`) available for webhook-based events.

**Source:** n8n-nodes-base.taiga.md  [doc-verified]
