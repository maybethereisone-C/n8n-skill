# Operating a Live n8n Instance — deploy & debug hard truths

Building correct workflow JSON is half the job. **Pushing it to a running instance and getting it to actually fire** is where production breaks silently. This page is the operational layer: the create→activate→trigger→inspect loop and the traps that make a valid workflow do nothing. Battle-tested against a live ad-ingestion pipeline.

Cross-refs (don't duplicate): REST surface → `rest-api.md`; MCP paths → `mcp-and-api.md`; webhook semantics → `webhooks.md`; execution inspection → `execution-debugging.md`; JSON shape → `workflow-schema.md`.

## The deploy → activate → trigger → inspect loop

The deterministic, UI-free cycle for shipping and debugging a workflow on a live instance:

```
1. create/update  → POST /api/v1/workflows         (or n8n-mcp n8n_create_workflow)
2. activate        → POST /api/v1/workflows/{id}/activate
3. trigger         → curl the production webhook URL, or wait for the schedule
4. inspect         → GET /api/v1/executions?workflowId={id}  then
                     GET /api/v1/executions/{execId}?includeData=true
5. patch + repeat  → update → re-activate (see "re-register" below) → re-trigger
```

Always inspect with `includeData=true` on failure — it returns **per-node** input/output, timing, error object, and which branch ran (`main[0]`=true, `main[1]`=false on an IF). That is the n8n equivalent of a stack trace; never guess from the top-level status.

## webhookId — the silent endpoint killer

A Webhook (or any webhook-based trigger) node **must carry a `webhookId` (a UUID) in its JSON**, or n8n accepts the workflow, shows it active, and **never registers the production endpoint** — every call to the URL 404s with no error anywhere.

```jsonc
{
  "parameters": { "httpMethod": "POST", "path": "my-hook", "responseMode": "onReceived" },
  "type": "n8n-nodes-base.webhook",
  "typeVersion": 2,
  "name": "Webhook",
  "webhookId": "f7c1e2a4-9b3d-4e21-8a6f-0c2d1e5b7a90",   // ← REQUIRED. Generate a UUID on create.
  "position": [0, 0]
}
```

Rule: when you author or import a workflow with a webhook node, generate and inject a `webhookId` if one is missing. (The bundled `validate-workflow.py` ship gate flags webhook nodes; treat a missing `webhookId` as a BLOCK before deploy.)

## Credentials are id-references resolved at deploy time

Workflow JSON never holds a secret — it holds a credential **id** that must already exist on the target instance:

```jsonc
"credentials": {
  "postgres": { "id": "$N8N_POSTGRES_CREDENTIAL_ID", "name": "DWH Postgres" }
}
```

The robust deploy pattern: keep credential ids (and any tokens used inside expressions) as `$ENV_VAR` placeholders in the committed JSON, and **substitute from the environment at deploy time** (`set -a; source .env; set +a`, then a templating pass) just before the create/update call. This keeps secrets and instance-specific ids out of git while letting the same JSON deploy to dev and prod.

Corollary (already in `workflow-schema.md`): if you do **not** have a real credential id, **omit the `credentials` block entirely**. A made-up/placeholder id that reaches the live instance breaks the n8n UI credential picker for that node.

## PUT /workflows accepts only four keys

`PUT /api/v1/workflows/{id}` (update) accepts **only** `{name, nodes, connections, settings}`. Sending back the full object you just GET'd — with read-only/UI keys like `active`, `id`, `tags`, `createdAt`, `pinData`, `versionId`, `meta`, `callerPolicy`, `availableInMCP` — returns **400**. Strip to the four allowed keys before PUT.

## Re-register after every edit: deactivate → activate

Updating a workflow does **not** re-register its triggers. After any `update` that touches a Webhook or Schedule Trigger, the live endpoint/cron still points at the old definition until you cycle it:

```
POST /api/v1/workflows/{id}/deactivate
POST /api/v1/workflows/{id}/activate
```

A single `activate` on an already-active workflow can silently no-op. The reliable move is deactivate→activate (what a `webhook-activate` helper does under the hood). Forget this and you debug "my fix didn't apply" when the fix deployed fine but the trigger never rebound.

## Two traps that look like build bugs but are deploy/runtime behavior

- **`respondToWebhook` nodes crash on manual trigger** ("No Webhook node found") because there's no live HTTP request to answer. For a fire-and-forget hook use `responseMode: "onReceived"` on the Webhook node and no Respond node. Full response-mode matrix → `webhooks.md`.
- **HTTP Request replaces the whole item.** The response body **overwrites every input field** on that item, and an **array response auto-expands** (2 input items → 110 output items breaks any positional reference downstream). To keep upstream fields, read them across nodes with `$('UpstreamNode').item.json.field` instead of assuming they survive the HTTP node. Detail → `node-guides/n8n-nodes-base.httpRequest.md`.

## Gateway / access note

A public n8n host sitting behind Cloudflare Access (or any SSO proxy) will reject API-key calls at the proxy, before n8n sees them — the API key alone is not enough. For CLI/MCP work, hit the instance on an internal/Tailscale URL that bypasses the proxy, or mint a service-token. (Project-specific, but a common production footgun.)
