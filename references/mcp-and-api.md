# MCP & API — Operating a Live n8n Instance

> Purpose: how Claude builds/edits/activates workflows on a real n8n instance (v2.26.0). Three distinct paths — don't conflate the two MCP servers.

## The three paths

| Path | What it is | Auth | Best for |
|---|---|---|---|
| **(a) Community `czlonkowski/n8n-mcp`** | 3rd-party MCP server. 1,851 nodes indexed. 8 doc/validate tools + ~19 `n8n_*` management tools (README says 13; source registers more — list live with `n8n_list_available_tools`). | Doc tools: none. Mgmt tools: `N8N_API_URL` + `N8N_API_KEY` (proxies the REST API). | Authoring with rich node docs, schema search, and workflow **validation** before you write to the instance. |
| **(b) Native built-in MCP** | 1st-party, shipped in every edition (Cloud/Enterprise/Community). Per-workflow "Make available in MCP" toggle. | Instance-native (enabled in n8n). | Letting a coding agent generate + self-validate + execute on the instance. **Generates TypeScript, not JSON.** |
| **(c) Public REST API `/api/v1`** | Direct HTTP. Stable, versioned. | Header `X-N8N-API-KEY`. | Scripting/CI, deterministic create/activate, when no MCP is wired. |

Pick: **(a)** for the best authoring loop (node knowledge + validation); **(b)** if the user prefers the native TS path and has a recent instance; **(c)** as the always-available primitive (both MCP paths and the CLI ultimately ride the REST API).

## (a) Community `czlonkowski/n8n-mcp`

**Discipline: call `tools_documentation()` first.** It returns topic guides — including `ai_agents_guide` — and the complete up-to-date tool surface for your session. Never rely on a cached list.

### Doc/validation tools (no instance needed)

| Tool | Purpose |
|---|---|
| `tools_documentation` | Start here. Returns topic guides (incl. `ai_agents_guide`) + complete live tool list. |
| `search_nodes` | FTS search across 1,851 nodes. |
| `get_node` | Node detail — see token ladder below. |
| `validate_node` | Validate a single node config. |
| `validate_workflow_connections` | Structural connection check (orphan nodes, bad index). |
| `validate_workflow_expressions` | Expression syntax validation (n8n `={{ }}` patterns). |
| `validate_workflow` | Full workflow: nodes + connections + expressions + AI Agent wiring. |
| `search_templates` | Search 2,352 templates. |
| `get_template` | Fetch a template by ID. |

**`get_node` modes/detail token ladder** (source: README.md §Configuration Phase):
- `detail: 'minimal'` — basic metadata only, ~200 tokens
- `detail: 'standard'` — essential properties + examples (default, ~1–2k tokens)
- `detail: 'full'` — complete information, ~3–8k tokens
- `mode: 'search_properties'` + `propertyQuery` — find a specific property by name
- `mode: 'docs'` — human-readable markdown documentation
- `mode: 'versions'` / `'compare'` / `'breaking'` / `'migrations'` — version history and migration guidance

### Management tools (need `N8N_API_URL` + `N8N_API_KEY`)

All 17 `n8n_*` tools registered in source (`src/mcp/tools-n8n-manager.ts`):

| Tool | Purpose |
|---|---|
| `n8n_create_workflow` | Create workflow (lands inactive; activate separately). |
| `n8n_get_workflow` | Read workflow. Modes: `full` (draft+metadata), `details` (full+execution stats), `active` (published graph only — errors if no live version), `structure` (topology), `minimal` (~200 tokens). Token-cheap read for inspect/diff before editing. |
| `n8n_update_full_workflow` | Full replacement — requires complete `nodes[]` and `connections{}`. Use only when restructuring everything. |
| `n8n_update_partial_workflow` | Diff-based incremental edits — 6–22× cheaper than full rewrite. See diff-ops section below. |
| `n8n_delete_workflow` | Permanently delete a workflow (irreversible). |
| `n8n_list_workflows` | List workflows (id/name/active/tags). Supports `active`, `tags`, `projectId` filters + cursor pagination. |
| `n8n_validate_workflow` | Validate deployed workflow by ID (nodes + connections + expressions). |
| `n8n_autofix_workflow` | Auto-fix common issues: expression format, typeVersions, connection structure, webhook paths. Preview or apply. |
| `n8n_workflow_versions` | Version history + rollback + prune. Modes: `list`, `get`, `rollback`, `delete`, `prune`. |
| `n8n_deploy_template` | Deploy an n8n.io template by ID directly to the instance, then auto-fix expression format + typeVersions. Returns workflow ID + required credentials. |
| `n8n_test_workflow` | Trigger a workflow execution. Auto-detects trigger type (webhook / form / chat). Params: `waitForResponse`, `sessionId` (for chat continuity), `data`, `headers`, `timeout`. |
| `n8n_executions` | Execution CRUD. Actions: `get` (modes: `preview`/`summary`/`filtered`/`full`/`error`), `list`, `delete`. |
| `n8n_manage_credentials` | Credential CRUD. Actions: `list`, `get`, `create`, `update`, `delete`, `getSchema`. Use `getSchema` before `create`. |
| `n8n_manage_datatable` | Data table + row CRUD. Actions: `createTable`, `listTables`, `getTable`, `updateTable`, `deleteTable`, `getRows`, `insertRows`, `updateRows`, `upsertRows`, `deleteRows`. Schema is immutable after `createTable`. |
| `n8n_generate_workflow` | NL → workflow. Two-phase: (1) call with `description` → returns proposals; (2) call again with `deploy_id` to deploy chosen proposal, or `skip_cache=true` + `confirm_deploy=true` for a fresh generate-and-deploy. Source-only — not documented in README. |
| `n8n_audit_instance` | Security audit: n8n built-in categories (credentials/database/nodes/instance/filesystem) + custom deep scan (hardcoded secrets via 50+ regex patterns, unauthenticated webhooks, error handling gaps, data retention). |
| `n8n_health_check` | Instance health + API connectivity. Mode `diagnostic` includes env vars + tool status. |

List the live tool set at runtime: `n8n_list_available_tools` (or check `tools_documentation()`). The number registered depends on whether `N8N_API_URL`/`N8N_API_KEY` are set.

### Partial-update diff-ops (19 types)

Source: `src/services/workflow-diff-engine.ts` + `src/mcp/tools-n8n-manager.ts` (`n8n_update_partial_workflow`).

| Op type | Notes |
|---|---|
| `addNode` | Insert a new node. |
| `removeNode` | Remove a node by name or id. |
| `updateNode` | Replace a node's full config. |
| `patchNodeField` | **Cheapest** — patch one field in place (~144 chars vs full node rewrite). Params: `fieldPath` (dot-path, e.g. `"parameters.jsCode"`), `patches: [{find, replace}]`. Max 50 patches/op; 512KB field size limit. |
| `moveNode` | Reposition a node on the canvas. |
| `enableNode` | Re-enable a disabled node. |
| `disableNode` | Disable a node without removing it. |
| `addConnection` | Wire two nodes. |
| `removeConnection` | Remove a specific wire. |
| `rewireConnection` | Change source or target of an existing connection. |
| `updateSettings` | Update workflow-level settings object. |
| `updateName` | Rename the workflow. |
| `addTag` | Attach a tag by name or ID. |
| `removeTag` | Remove a tag. |
| `transferWorkflow` | Move workflow to another project (as a diff op — no separate REST call needed). |
| `activateWorkflow` | Publish/activate (as a diff op). |
| `deactivateWorkflow` | Unpublish/deactivate (as a diff op). |
| `cleanStaleConnections` | Remove connections that reference deleted or renamed nodes. |
| `replaceConnections` | Bulk-replace the entire connections object. |

**Smart connection params:** IF node uses `branch: "true"` / `"false"`; Switch node uses `case: N` (zero-indexed). Use semantic params — avoids output-index errors.

### Connect Claude Code to n8n-mcp

Two tiers — pick by whether you need to touch a live instance:

```bash
# Tier 1 — docs only: node knowledge + validation, NO instance/key needed
claude mcp add n8n-mcp -e MCP_MODE=stdio -e LOG_LEVEL=error \
  -e DISABLE_CONSOLE_OUTPUT=true -- npx n8n-mcp

# Tier 2 — full: adds the n8n_* tools that operate a live instance
claude mcp add n8n-mcp -e MCP_MODE=stdio -e LOG_LEVEL=error \
  -e DISABLE_CONSOLE_OUTPUT=true \
  -e N8N_API_URL=https://your-n8n.example.com -e N8N_API_KEY="$N8N_API_KEY" \
  -- npx n8n-mcp
```

`N8N_API_URL` + `N8N_API_KEY` are the gate: omit → only doc/validation tools register; add → the `n8n_*` management tools appear. Key comes from **Settings → n8n API**. Project-scoped alternative: same `command`/`args`/`env` under `mcpServers` in a `.mcp.json` at the repo root (commit it for the team; keep the key in an env var, not inline). Credit: server by Romuald Członkowski (aiadvisors.pl).

**nodeType format gotcha (critical):** search/validate tools take the **short** form, workflow JSON takes the **full** form.
```
search_nodes / validate_node / get_node   →  nodes-base.slack
workflow JSON  "type":                     →  n8n-nodes-base.slack
```
Get this wrong and the node won't resolve. Validation profiles: `minimal` / `runtime` / `ai-friendly` / `strict`.

## (b) Native built-in MCP

- Maintained by n8n. Clients: Claude Code, Cursor, Windsurf, Claude Desktop, ChatGPT, etc.
- **Version gates:** run-existing-workflows = base; **build/edit = v2.13+**; create+update shipped v2.14.0 (beta); v2.18.4+ recommended. v2.26.0 is comfortably above all gates. Public Preview — tool names/params are **moving fast; re-verify against docs.n8n.io**.
- **Generates TypeScript, not raw JSON.** n8n's rationale: the model must produce code that type-checks + compiles before touching the instance → "more reliable than direct JSON generation" (vendor claim, not a benchmark).
- **Autonomous loop:** generate → validate → fix-and-revalidate → execute (with generated test data) → read-error-and-fix. n8n recommends coding agents over chat clients for this.

This is a **different server** from (a). (a) is a community Node-knowledge + management layer; (b) is n8n's own in-instance server that speaks TS. Don't mix their tool names.

## (c) REST API quickstart

Create the key in the UI: **Settings → n8n API** (set Label + Expiration). Base path: self-hosted `<HOST>:<PORT>/api/v1/...`; Cloud `<instance>.app.n8n.cloud/api/v1/...`.

```bash
# Auth header on every call
H="X-N8N-API-KEY: $N8N_API_KEY"
BASE="https://your-instance/api/v1"

# Create a workflow (POST ignores `active` — it lands inactive/unpublished)
curl -s -X POST "$BASE/workflows" -H "$H" -H "Content-Type: application/json" \
  -d @workflow.json            # body: { name, nodes, connections, settings }

# Activate (publish) — separate call, by id
curl -s -X POST "$BASE/workflows/{id}/activate" -H "$H"

# Other resources: GET/PATCH/DELETE /workflows/{id}, /executions, /credentials, /tags
# Transfer to project: PUT /workflows/{id}/transfer  { "destinationProjectId": "..." }
#                      PUT /credentials/{id}/transfer { "destinationProjectId": "..." }
```

Notes:
- **Create does not activate.** `active` in the POST body is ignored; you must call **`POST /api/v1/workflows/{id}/activate`**. (n8n 2.0 renamed active/inactive → Publish/Unpublish; terminology varies across docs.)
- **Workflow JSON uses the full `n8n-nodes-base.*` type** (same gotcha as MCP). Pin `typeVersion` to the catalog `maxVer`.
- **Use `/api/v1/`, not internal `/rest/`.** `/rest/` is the Editor UI's API — OEM/embed-only and "subject to change." `/api/v1/` is the stable public surface.
- **n8n CLI** wraps this same public API and is tuned for coding agents (Claude Code, Cursor) — a convenient alternative to raw curl.
- **Full reference** → [rest-api.md](rest-api.md): all endpoint groups, scopes table, pagination, Server CLI, n8n CLI command surface.

## Recommended flow

1. **Author + validate with (a)**: `search_nodes` → `get_node` (confirm ops + typeVersion) → assemble JSON → `validate_workflow` → `n8n_autofix_workflow`.
2. **Write to instance** via (a) `n8n_create_workflow`, or (c) `POST /workflows` if no MCP.
3. **Activate** via `POST /api/v1/workflows/{id}/activate`.
4. Or, if the user is on native MCP (b), let its TS generate→validate→execute loop drive the whole thing.
