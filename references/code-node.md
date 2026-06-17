# n8n Code Node & AI Code Tool (v2.26.0)

> Purpose: the exact return contracts for the regular Code node (JS + Python) and the AI Code Tool — two DIFFERENT contracts LLMs routinely confuse — plus when to use Code at all vs a dedicated node.

## Doctrine: write the simplest fully-correct code

Write **200 lines that do the job, never 1000**. The decision order is always:

1. **Dedicated node** — validated, typed, versioned, self-documenting (`Set`, `Filter`, `Aggregate`, `Merge`, `HTTP Request`…). See the table at the bottom.
2. **Expression** (`{{ }}`) — for single-value compute, dates, string ops. See expressions.md.
3. **Minimal Code** — only when 1 and 2 can't express the transform.

Every Code snippet should be minimal-but-complete: correct, runnable, no padding, no speculative branches. If a dedicated node covers 80% of the task, use it and let Code handle only the remaining 20%. Reach for Code as glue, not as a platform.

## Regular Code node — `n8n-nodes-base.code`

A general-purpose scripting node placed inline in a workflow. JavaScript or Python (Pyodide). Two run modes.

### Run modes

| Mode | When it runs | Available helpers | Return |
|------|--------------|-------------------|--------|
| **Run Once for All Items** (default) | Once per node execution, sees the whole batch. | `$input.all()`, `$items()` | Array of items: `[{json:{...}}, ...]` |
| **Run Once for Each Item** | Once per incoming item. | `$input.item`, `$json` (current item) | One item: `{ json: {...} }` (n8n wraps it) |

Set via `parameters.mode`: `"runOnceForAllItems"` or `"runOnceForEachItem"`. Language via `parameters.language`: `"javaScript"` or `"python"`.

### JavaScript — return format `[{json:{}}]`

```js
// Run Once for All Items
const items = $input.all();              // [{ json, binary, pairedItem }, ...]

const out = items.map((item, i) => ({
  json: {
    id: item.json.id,
    upper: (item.json.name ?? '').toUpperCase(),
  },
  pairedItem: { item: i },               // preserve lineage for downstream $node refs
}));

return out;                              // MUST be an array of {json:{...}} objects
```

```js
// Run Once for Each Item
const name = $json.name ?? '';
return { json: { name, length: name.length } };   // single item; auto-wrapped
```

Available in JS Code node (`builtin/n8n-metadata.md`, `builtin/jmespath.md`):
- Items: `$input.all()`, `$input.first()`, `$input.last()`, `$input.item` (each-item mode), `$json`, `$binary`.
- Other nodes: `$("Name")`, `$("Name").all(branchIndex?, runIndex?)`, `$("Name").item`, `$("Name").first()`, `$("Name").last()`, `$("Name").isExecuted`, `$node["Name"].json`, `$items("Name")`. `.all(1, 0)` = output index 1 (e.g. IF "false"), run 0 (`cookbook/builtin/all.md`).
- Date/data: `$now`, `$today` (Luxon), `$jmespath(obj, "expr")`.
- Metadata: `$workflow.{id,name,active}`, `$execution.{id,mode,resumeUrl,customData}`, `$vars`, `$env`, `$runIndex` (0-based count of current-node runs), `$nodeVersion`, `$prevNode.{name,outputIndex,runIndex}`.
  - `$prevNode.name` = node the current input came from; on a **Merge** node `$prevNode` always reports input connector 0.
  - NOT in Code node (expressions only): `$itemIndex`, `$secrets`, `$version`.
- `$execution.customData` (Code node only) — per-execution KV store, surfaced in execution search/filtering:
  ```js
  $execution.customData.set("key", "value");
  $execution.customData.setAll({ k1: "v1", k2: "v2" });
  const all = $execution.customData.getAll();
  const one = $execution.customData.get("key");
  ```
- `this.helpers` — `this.helpers.httpRequest(opts)`, `this.helpers.returnJsonArray(...)`, `this.helpers.prepareBinaryData(buffer, fileName?, mimeType?)`, `await this.helpers.getBinaryDataBuffer(itemIndex, propName)`.
- Built-in: `JSON`, `Math`, `Date`, Promises (return a promise and it resolves), `console.log` (see below).

**Modules / `require()` rules** (`_snippets/.../code-node.md`):
- **n8n Cloud (JS):** no external npm. Exactly two modules are pre-provided: `crypto` (Node builtin) and `moment` (npm). Nothing else.
- **Self-hosted (JS):** import builtin + external npm only after allow-listing via `NODE_FUNCTION_ALLOW_BUILTIN` / `NODE_FUNCTION_ALLOW_EXTERNAL` (see Enable modules in Code node guide). Unlisted `require()` throws.
- **No filesystem, no direct HTTP** from Code. Use the **Read/Write File From Disk** node and the **HTTP Request** node instead (`this.helpers.httpRequest` is the only in-Code HTTP path, and only where helpers are available).

**Return wrapping.** From 0.166.0+ the node auto-wraps a bare object and auto-adds a missing `json` key — but be explicit: always return `[{json:{...}}]` (all-items) or `{json:{...}}` (each-item).

**`console.log` / debug surface** (`cookbook/code-node/console-log.md`): `console.log(x)` (JS) and `print(x)` (Python) write to the **browser console**, not the execution log panel. Use for debugging while editing. If output shows `[object Object]`, the value is an object — log a field or `JSON.stringify(x)`.

### Python — native runner (v2 default), return format

In **n8n v2 the Python runner is native** (task runners, stable since 1.111.0), not Pyodide. Pyodide is a legacy feature that **v2 no longer supports** (`_snippets/.../code-node.md`). Variables are prefixed with `_`.

```python
# Run Once for All Items
out = []
for item in _items:                       # native: _items, bracket access only
    out.append({
        "json": {
            "id": item["json"]["id"],
            "upper": str(item["json"].get("name", "")).upper(),
        }
    })
return out                                # list of dicts each with a "json" key
```

```python
# Run Once for Each Item
name = _item["json"].get("name", "")      # native: _item, the current item
return { "json": { "name": name, "length": len(name) } }
```

Native Python specifics (`_snippets/.../code-node.md`, `builtin/n8n-metadata.md`):
- **Only `_items` (all-items) and `_item` (per-item) are supported.** No other n8n built-ins — no `_input`, `_json`, `_now`, `_vars`, `_env`, `_getWorkflowStaticData`, `_jmespath`, `_("Node")`. If you need those, write the node in **JavaScript**.
- **Bracket access only:** `item["json"]["field"]`. Dot access (`item.json.field`) is Pyodide-only and is **not legal** in native Python.
- Return Python dicts/lists; same `{"json": {...}}` wrapping rule.
- **Cloud:** no library imports at all (stdlib or third-party). **Self-hosted:** stdlib + third-party only if the `n8nio/runners` image bundles and allow-lists them (task-runners config); insecure built-ins denied by default.
- Prefer JS unless Python is specifically needed — JS exposes the full built-in surface; native Python deliberately does not.

The Pyodide-era `_("<node>").all()` returns `JsProxy` objects needing `.to_py()` — this applies only to legacy Pyodide instances, not v2 native (`cookbook/builtin/all.md`, `cookbook/code-node/console-log.md`).

## AI Code Tool — `@n8n/n8n-nodes-langchain.toolCode`

A **tool sub-node** wired into an AI Agent via an `ai_tool` connection. The agent (LLM) calls it during reasoning. This is a fundamentally different contract from the regular Code node.

```js
// AI Code Tool — JavaScript
// 'query' / '_query' holds the input the agent passes in (name is FIXED, not renameable).
const input = query;                 // a string the LLM decided to send

const result = { tempC: 22, city: input };

return JSON.stringify(result);       // MUST return a STRING (stringify structured data)
```

- Input arrives as `query` (JS) / `_query` (Python) — you cannot rename it.
- Output MUST be a **string**. For structured data, `JSON.stringify(...)`; the agent reads the string.
- **`$fromAI()` is NOT supported here** — it throws "No execution data available". (`$fromAI()` belongs in other tool sub-nodes whose parameters the agent fills, not in tool *code*.)
- Returning an array/object (the regular-Code contract) is wrong here and will misbehave.

## Side-by-side: Code node vs AI Code Tool

| Aspect | Code node (`n8n-nodes-base.code`) | AI Code Tool (`@n8n/n8n-nodes-langchain.toolCode`) |
|--------|-----------------------------------|----------------------------------------------------|
| Role | Inline step in the main data flow | Tool the AI Agent invokes during reasoning |
| Connection | `main` → `main` | `ai_tool` → AI Agent |
| Input access | `$input.all()` / `$input.item` / `$json` | `query` (JS) / `_query` (Python), name FIXED |
| Return type | **Array** `[{json:{...}}]` (or `{json:{...}}` each-item) | **String** (use `JSON.stringify` for structures) |
| `$json`, `$node`, `$input` | available | not the data model — use `query` |
| `$fromAI()` | not applicable | **NOT supported — throws** |
| Run modes | runOnceForAllItems / runOnceForEachItem | n/a (invoked per tool call) |
| Auto json-wrap | yes (0.166.0+) | no — you return a raw string |

Memory aid: **Code node returns items (array of `{json}`); AI Code Tool returns a string.** Never return an array from the AI Code Tool; never return a bare string from the Code node.

## Production gotchas

**Reading loop data after Split In Batches loses all but the last iteration.** After a `Loop Over Items` (`splitInBatches`) loop, `$('NodeInsideLoop').all()` returns **only the final iteration's items** — earlier batches are silently dropped (no error). To aggregate across all iterations, accumulate in workflow static data:

```js
// inside the loop body, each iteration:
const store = $getWorkflowStaticData('global');
store.acc = (store.acc || []).concat($input.all().map(i => i.json));
return $input.all();
// after the loop: a Code node reads store.acc (the full set)
```

Reset `store.acc = []` in a Set/Code node *before* the loop starts so a re-run doesn't compound. Native Python Code nodes don't expose `$getWorkflowStaticData` — do the accumulation in a JS Code node.

**Currency / float equality.** `if (a !== b)` fires on float noise (`0.1 + 0.2 !== 0.3`). Compare integer cents: `Math.round(a * 100) !== Math.round(b * 100)`.

## `$getWorkflowStaticData(type)` — full semantics

Persistent KV storage that lives **with the workflow** between executions (`cookbook/builtin/get-workflow-static-data.md`). Use it for small state: last-seen timestamp, dedupe cursor, RSS/DB watermark.

```js
const g = $getWorkflowStaticData('global');   // shared by every node in the workflow
const n = $getWorkflowStaticData('node');      // private to THIS node only

const last = g.lastRun;            // read
g.lastRun = Date.now();            // write — persisted on successful completion
delete g.lastRun;                  // delete
```

Rules:
- Two scopes: `'global'` (all nodes share) and `'node'` (only the setting node can read it back).
- n8n diffs the object after the run and **persists only if it changed** and the **execution succeeded**.
- **Does not persist during manual/test runs.** The workflow must be **active** and triggered by a trigger or webhook for writes to save.
- Keep it small; mutate the returned object in place (don't reassign the whole handle).
- Flagged experimental and **unreliable under high-frequency executions** — don't treat it as a database.
- For data you set/read within a single execution (not across runs), prefer `$execution.customData` instead (`code/variables.md`).

## Binary data — get/set the buffer

Binary file payloads ride on `item.binary.<propName>` (default prop name is `data`); the actual bytes are fetched via a helper, not read off the item (`cookbook/code-node/get-binary-data-buffer.md`).

```js
// READ: get the Buffer for an item's binary property (JS only — not in Python)
const buf = await this.helpers.getBinaryDataBuffer(0, 'data');   // (itemIndex, binaryPropertyName)
// ...operate on buf: hash, parse CSV, rewrite headers, etc.

// WRITE: turn a Buffer back into an n8n binary property
const binary = await this.helpers.prepareBinaryData(buf, 'out.csv', 'text/csv');
return [{ json: {}, binary: { data: binary } }];
```

- Always use `getBinaryDataBuffer()` — never reach into `items[0].binary.data.data` directly.
- `getBinaryDataBuffer()` is **not available in Python**; do binary work in a JS Code node.
- `getBinaryDataBuffer` is `async` — `await` it.

## When to use Code vs a dedicated node

Prefer a dedicated node — it is validated, typed, versioned, and self-documenting. Reach for Code only as glue.

| Need | Use this, not Code |
|------|--------------------|
| Set/rename/compute fields | **Set / Edit Fields** (`n8n-nodes-base.set`) |
| Filter items by condition | **Filter** / **IF** |
| Branch on a value | **Switch** / **IF** |
| Call an HTTP API | **HTTP Request** |
| Merge/split/aggregate items | **Merge**, **Split Out**, **Aggregate**, **Item Lists** |
| Loop in batches | **Loop Over Items (Split in Batches)** |
| Date math, simple string ops | **expressions** (`{{ }}`) inline — see expressions.md |

Use the **Code node** for: multi-step transforms expressions can't express, custom aggregation/reshaping, calling `this.helpers.httpRequest` in a loop with custom logic, or generating items programmatically. Keep it small; if a dedicated node covers 80% of it, use the dedicated node and let Code handle only the remainder.
