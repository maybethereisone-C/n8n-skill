# Gotify — `n8n-nodes-base.gotify`
**Type** `n8n-nodes-base.gotify` · **typeVersion** 1 · **action**
**What:** Sends push notifications and manages messages on a self-hosted Gotify server.
**Credentials:** `gotifyApi` (App Token + Server URL — Gotify is self-hosted only).

**Resources / Operations:**

| Resource | Operations |
|---|---|
| Message | Create, Delete, Get All |

**Key params & gotchas:**
- **Create** sends a push notification to all clients subscribed to the app whose token is used.
- The App Token scopes access to a single Gotify application — each Gotify app has its own token.
- Message priority is 1–10; clients may filter by priority. Default is 5.
- Get All and Delete require an **Admin/Client Token**, not an App Token; mixing them causes 403 errors.
- Server URL must be reachable from the n8n instance; for self-hosted n8n behind a firewall, both n8n and Gotify must be on the same network or internet-exposed.

**Source:** n8n-nodes-base.gotify.md  [doc-verified]
