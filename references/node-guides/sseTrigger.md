# SSE Trigger — `n8n-nodes-base.sseTrigger`
**Type** `n8n-nodes-base.sseTrigger` · **trigger**

**What:** Starts a workflow when it receives a Server-Sent Event (SSE) from a specified URL over HTTP.

**Credentials:** none.

**Resources / Operations:** Trigger only.

**Key params & gotchas:**
- Single parameter: **URL** — the SSE endpoint to subscribe to.
- Uses HTTP long-polling (EventSource protocol); the connection persists until an event arrives.
- No authentication configuration in the node — if the SSE endpoint requires auth, it cannot be configured here directly.

**Source:** n8n-nodes-base.ssetrigger.md  [doc-verified]
