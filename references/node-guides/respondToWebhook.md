# Respond to Webhook — `n8n-nodes-base.respondToWebhook`
**Type** `n8n-nodes-base.respondToWebhook` · **core**

**What:** Sends a custom HTTP response to the caller of a Webhook trigger node.

**Credentials:** none.

**Resources / Operations:** Single operation — send webhook response.

**Key params & gotchas:**
- Requires the Webhook trigger node to have **Respond** set to `Using 'Respond to Webhook' node`.
- **Respond With** options: All Incoming Items, Binary File, First Incoming Item, JSON, JWT Token, No Data, Redirect (URL), Text (sends as `text/html`).
- Runs only once per execution using the **first incoming item** — use **All Incoming Items** (added 1.22.0) or Aggregate node to return multiple.
- **Options**: Response Code, Response Headers, Put Response in Field, Enable Streaming.
- **Enable Response Output Branch** (Settings tab) adds a second output carrying the actual response object sent.
- From n8n 1.103.0, HTML responses are automatically sandboxed in an `<iframe>` — relative URLs and auth headers won't work inside it; use absolute URLs and embed tokens in HTML instead.
- Second Respond to Webhook node in same execution is ignored. No webhook present → node is ignored.
- Workflow errors before this node → 500 response. Workflow finishes without hitting this node → 200 with standard message.

**Source:** n8n-nodes-base.respondtowebhook.md  [doc-verified]
