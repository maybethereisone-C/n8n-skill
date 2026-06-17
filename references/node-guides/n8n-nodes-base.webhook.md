# Webhook — `n8n-nodes-base.webhook`

**Type** `n8n-nodes-base.webhook` · **typeVersion** 2.1 · **trigger**

**What:** Exposes an HTTP endpoint that triggers the workflow when called; supports GET, POST, PUT, PATCH, DELETE, HEAD; handles auth, binary uploads, and response strategies.

**Credentials:** Optional auth credentials depending on `Authentication` setting (Basic Auth, Header Auth, JWT Auth).

**Resources / Operations:** Single trigger — receives any inbound HTTP request.

**Key params & gotchas:**

- **Test vs Production URLs** — n8n generates two distinct URLs. Test URL is active only when you click "Listen for test event" (120-second window) and shows data in the editor. Production URL is active only when the workflow is published (saved + activated); data does NOT appear in the editor.
- **Path** — defaults to a UUID. Use a readable slug for stable endpoints (e.g. `my-webhook`), but ensure uniqueness across workflows.
- **Allow Multiple HTTP Methods** — when ON, a `httpMethod` multi-select replaces the single method picker. Lets one node accept, e.g., both GET and POST.
- **Respond** options:
  - `Immediately` — webhook returns 200 before workflow finishes (fire-and-forget from caller's perspective).
  - `When Last Node Finishes` — blocks caller until entire workflow completes; returns last node output.
  - `Using 'Respond to Webhook' Node` — workflow controls the response explicitly via the Respond to Webhook node.
- **Authentication** — Header Auth and JWT require a credential; Basic Auth uses a credential with username/password. `None` means the endpoint is public.
- **Binary data** — incoming file uploads land in `binary.data` by default; use `Binary Property` option to rename.
- **Ignore Bots** — filters requests from web crawlers / link previewers that probe URLs.
- **IP Whitelist** — comma-separated allowlist; requests from other IPs receive 403.
- **Localhost development** — run n8n in tunnel mode (`--tunnel` flag) so external services can reach a local instance.
- **Streaming** — requires a streaming-capable downstream node (e.g. AI Agent with streaming enabled); the webhook node itself exposes `webhookStreamingNotice` when the workflow lacks a streaming node.

**Source:** n8n-nodes-base.webhook/index.md + workflow-development.md  [doc-verified]
