# Metabase — `n8n-nodes-base.metabase`
**Type** `n8n-nodes-base.metabase` · **typeVersion** 1 · **action**
**What:** Reads alerts, databases, metrics, and questions (saved queries) from a Metabase instance.
**Credentials:** `metabaseApi` (username + password + instance URL).

**Resources / Operations:**

| Resource | Operations |
|---|---|
| Alert | Get, Get All |
| Database | Add, Get All, Get Fields |
| Metric | Get, Get All |
| Question | Get, Get All, Result Data |

**Key params & gotchas:**
- **Question > Result Data** executes the saved question and returns its result set — this is the key operation for pulling data from Metabase into n8n for further processing.
- Credentials use username/password (session token auth); Metabase does not have a native API key for all endpoints (API keys were added in v47+ for some endpoints).
- Instance URL must be reachable from the n8n server; self-hosted Metabase behind a VPN requires network access.
- Database > Add adds a database connection to Metabase — use with caution as it modifies Metabase configuration.
- Result Data can return large payloads for complex questions; consider filtering the question in Metabase before pulling via n8n.

**Source:** n8n-nodes-base.metabase.md  [doc-verified]
