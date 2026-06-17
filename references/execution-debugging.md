# n8n Executions — Debugging & Operations Reference

> Source files: `docs/workflows/executions/index.md`,
> `docs/workflows/executions/all-executions.md`,
> `docs/workflows/executions/single-workflow-executions.md`,
> `docs/workflows/executions/manual-partial-and-production-executions.md`,
> `docs/workflows/executions/debug.md`,
> `docs/workflows/executions/dirty-nodes.md`,
> `docs/workflows/executions/custom-executions-data.md`,
> `docs/workflows/executions/execution-data-redaction.md`,
> `docs/api/authentication.md` (execution scopes)

---

## Execution types

| Type | Triggered by | Counts toward quota | Pinned data used |
|---|---|---|---|
| **Production** | Active workflow + trigger event (webhook, schedule, polling) | Yes | No |
| **Manual** | "Execute Workflow" button in editor | No | Yes |
| **Partial** | "Execute step" on a specific node | No | Yes |

Key distinctions:
- Production executions do **not** show live data in the editor. View them in the **Executions** tab.
- Manual executions mirror production logic as closely as possible; they still require a trigger node.
- Only production executions count toward paid plan quotas, regardless of the instance environment (dev or prod).

---

## Execution lists

### All executions

**Overview page → Executions tab** — shows all executions you have access to across all workflows.

If projects are enabled, each project also has an **Executions** tab scoped to that project's workflows.

Filter fields:
- **Workflows** — all or a specific workflow name
- **Status** — Failed / Running / Success / Waiting
- **Execution start** — time range
- **Saved custom data** — key + value (see Custom Execution Data below)

### Single-workflow executions

Open a workflow → **Executions** tab. Same filter options minus the workflow selector.

**Note:** Deleting a workflow also deletes its execution history — executions for deleted workflows are not recoverable.

---

## Retry a failed execution

From either the all-executions list or the single-workflow executions list:

1. Locate the failed execution.
2. Select **Retry execution** (three-dot menu or Refresh icon).
3. Choose retry mode (options injected via `_snippets/workflows/executions/retry-options.md` — refer to UI for current options; typically "Retry with original data" or "Retry with current workflow").

Via REST API:
```bash
curl -X POST "$BASE/executions/{id}/retry" -H "X-N8N-API-KEY: $N8N_API_KEY"
# Requires scope: execution:retry
```

Via n8n CLI:
```bash
n8n-cli execution retry <id>
```

---

## Debug in editor

> Feature availability: n8n Cloud + registered Community plans.

Load a past execution's data into the current canvas to reproduce and fix failures:

1. Workflow → **Executions** tab.
2. Select the execution.
   - Failed executions: **Debug in editor**
   - Successful executions: **Copy to editor**
3. n8n copies the execution data into the canvas and **pins** the data at the first node.

With pinned data loaded:
- Edit the workflow nodes that failed.
- Re-execute with `Execute step` from the failing node (partial execution).
- Remove pins before going back to production.

---

## Manual vs partial executions

### Full manual execution

Click **Execute Workflow** at the bottom of the canvas. Runs the entire workflow from the trigger. Uses any pinned data in place of live node execution.

### Partial execution

**Click a node → Execute step.** Runs that node plus all upstream nodes needed to supply its input. Skips nodes marked as disabled.

Common errors:

| Error | Cause | Fix |
|---|---|---|
| "The destination node is not connected to any trigger" | No trigger node in the chain | Add a Manual Trigger node |
| "Please execute the whole workflow…(Existing execution data is too large)" | Workflow has too many branches for the partial-execution message size | Add a Limit node to constrain output while testing |

---

## Dirty nodes

A **dirty node** has stale output — its previous result is unreliable because something upstream or about the node itself changed. Indicated by a **yellow border** and a **yellow triangle** (replacing the green tick).

### What marks a node dirty

- Inserting or deleting a node → first downstream node becomes dirty
- Modifying a node's parameters → that node becomes dirty
- Adding a connection → destination node becomes dirty
- Deactivating a node → first downstream node becomes dirty
- Unpinning a node → the unpinned node becomes dirty
- Modifying pinned data → the node after the pinned node becomes dirty
- Any of the above inside a loop → also marks the first node of the loop dirty

Sub-node changes (add / edit / disconnect / activate / deactivate a sub-node) mark the parent chain dirty up to the root.

### Resolving dirty nodes

Re-execute the node (or any downstream node) to clear dirty status:
- **Execute Workflow** (full run) — clears all dirty nodes
- **Execute step** on the dirty node or any successor — clears from that point forward

---

## Pin data (for debugging)

Pin data freezes a node's output for manual executions:
- Pinned nodes are not re-executed; their frozen output flows into downstream nodes.
- Production executions **ignore all pinned data** — pins are dev-only.
- Load a past execution via **Debug in editor** / **Copy to editor** to auto-pin first-node data.
- Unpin before activating for production.

Access in Code node:
```js
// Pinned data at a node is still $json — no special access needed
```

---

## Custom execution data

Attach up to 10 key/value string pairs to an execution for filtering and auditing.

### Set (Code node or Execution Data node)

```js
// Set one key
$execution.customData.set("orderId", "12345");

// Set all at once (overwrites entire object)
$execution.customData.setAll({ "orderId": "12345", "region": "eu-west" });
```

Python equivalent uses `_execution` prefix.

Limits:
- Keys: max 50 characters
- Values: max 255 characters
- Max 10 pairs per execution
- Values must be strings

### Read during execution

```js
const all = $execution.customData.getAll();
const val = $execution.customData.get("orderId");
```

### Filter by custom data

In the Executions list → **Filters → Saved custom data** → enter key + value.

Note: Custom execution data filtering availability depends on your plan and settings.

---

## REST API — execution operations

```bash
H="X-N8N-API-KEY: $N8N_API_KEY"
BASE="https://your-instance/api/v1"

# List executions (recent failures for a workflow)
curl "$BASE/executions?workflowId={id}&status=error&limit=20" -H "$H"

# List with full node data included
curl "$BASE/executions?includeData=true&limit=10" -H "$H"

# Get single execution (full data)
curl "$BASE/executions/{id}" -H "$H"

# Retry a failed execution
curl -X POST "$BASE/executions/{id}/retry" -H "$H"

# Stop a running execution
curl -X POST "$BASE/executions/{id}/stop" -H "$H"

# Delete an execution
curl -X DELETE "$BASE/executions/{id}" -H "$H"
```

Status filter values: `error` / `success` / `waiting` / `running`.

Required scopes: `execution:list`, `execution:read`, `execution:retry`, `execution:stop`, `execution:delete`.

---

## n8n CLI — execution operations

```bash
n8n-cli execution list                          # all recent executions
n8n-cli execution list --status=error --limit=10
n8n-cli execution list --workflow-id=<id>
n8n-cli execution get <id>
n8n-cli execution retry <id>
n8n-cli execution stop <id>
n8n-cli execution delete <id>
```

---

## Execution data redaction (Enterprise)

> Available: Enterprise Self-hosted + Enterprise Cloud. Per-workflow: v2.16.0+. Instance-wide enforcement: v2.26.0+.

Redaction hides node input/output data in execution viewers while preserving metadata (status, timing, node names, error type).

### Per-workflow settings

**Workflow → (three-dots) → Settings**:
- `Redact production execution data` — Default: Do not redact / Redact
- `Redact manual execution data` — Default: Do not redact / Redact

Required scopes: `workflow:enableRedaction` / `workflow:disableRedaction`.

### Instance-level enforcement

**Settings → Security → Data redaction**. Sets a floor; workflow settings cannot go below it.

| Enforcement scope | What is enforced |
|---|---|
| Production executions | Redact all production executions instance-wide; manual executions follow per-workflow settings |
| Manual and production executions | Redact all executions on every workflow |

Enforcement applies **at read time** — existing executions are redacted when viewed, not retroactively on disk.

New workflows created while enforcement is active default to the enforced scope. Existing workflow settings are preserved but overridden at read time.

### What gets redacted

- All `item.json` data replaced with empty object `{}`
- All `item.binary` (files, images) removed
- Error messages reduced to error type + HTTP status code only
- Fields declared `sensitiveOutputFields` by node authors — always redacted, reveal denied even for privileged users

### Revealing redacted data

Requires `execution:reveal` scope (instance owners and admins have it by default):

1. Open execution viewer.
2. Click **Reveal data** → confirm in dialog.
3. Data visible for that execution in current session.

Reveal is denied for executions that used **dynamic credentials** (regardless of permission).

### Redaction limits

- `console.log` in Code nodes is NOT redacted (appears in editor Logs panel / stdout)
- Data flowing between nodes is not restricted during execution
- Webhook response bodies are raw (not redacted)
- No field-level granularity — applies to entire node payload (except declared `sensitiveOutputFields`)
- Stored DB data is unchanged; redaction is applied at API-serve time
- Instance enforcement is NOT exported via source control

### Audit events

| Event | Trigger |
|---|---|
| `n8n.audit.execution.data.revealed` | User reveals redacted data |
| `n8n.audit.execution.data.reveal_failure` | Reveal attempt denied |
| `n8n.audit.redaction-enforcement.updated` | Instance enforcement policy changed |

---

## Execution save settings

What gets saved is controlled per workflow in **Workflow Settings**:
- Save successful production executions: yes / no
- Save failed executions: yes / no
- Save manual executions: yes / no

Filtering executions in the list only shows executions that were saved per these settings. Lower retention settings reduce DB load but limit debug visibility.

---

## Quick debug workflow

1. Check **Executions** tab — filter by `status=error`
2. Select failed execution → **Debug in editor** (loads + pins data)
3. Identify the failing node (red border in canvas)
4. Fix node parameters
5. **Execute step** from the failing node to re-run with pinned input
6. Confirm output is correct
7. Clear pins, re-test with a full manual run
8. Activate workflow for production
