# NocoDB — `n8n-nodes-base.nocoDb`
**Type** `n8n-nodes-base.nocoDb` · **typeVersion** 2 · **action**
**What:** CRUD operations on NocoDB tables (open-source Airtable alternative backed by SQL databases).
**Credentials:** NocoDB API token (`nocoDb`) — base URL + API token.
**Resources / Operations:**
| Resource | Operations |
|---|---|
| Row | Create, Delete, Get, Get Many, Update |

**Key params & gotchas:**
- NocoDB is self-hostable; the credential requires your instance URL (e.g., `https://nocodb.example.com`).
- Requires Table ID (not name) — find it in the NocoDB UI URL or via API.
- "Get Many" supports filtering and sorting via NocoDB's query syntax.
- Can be used as an AI tool node.

**Source:** n8n-nodes-base.nocodb.md  [doc-verified]
