# n8n Item Data & Binary Contract (v2.26)

> Purpose: the in-depth item data contract — the array-of-`{json,binary,pairedItem}` shape, `pairedItem` lineage (why "Can't get data for expression" fires and how to fix it), automatic item linking, binary modes (memory vs filesystem), referencing other nodes' items, and `itemMatching`. Pairs with workflow-schema.md (runtime contract summary) and execution-model.md.

## The item array

All data passed between nodes is an **array of objects**. Each object wraps its payload under `json` (and optionally `binary`) (data/data-structure.md):

```json
[
  { "json": { "apple": "beets", "carrot": { "dill": 1 } } },
  { "json": { "apple": "kale",  "carrot": { "dill": 2 } } }
]
```

- A node processes **each item individually**, applying its operation per item (data/data-structure.md). `{{ $json.apple }}` is the *current* item's value as the node iterates.
- **Skipping `json` / array wrapping:** from 0.166.0+, the **Code/Function nodes** auto-add a missing `json` key and auto-wrap a bare object in an array. This is **only** for those nodes — when building your own node you must return data with the `json` key yourself (data/data-structure.md).
- Nested objects are allowed under `json` and render as nested columns in the INPUT table (data/data-structure.md).

## `pairedItem` lineage (item linking)

Each output item carries metadata linking it back to the **input item(s)** that produced it. This forms a thread you can walk backward to reach any earlier node's matching item (data-item-linking/index.md, item-linking-concepts.md).

### n8n's automatic linking (item-linking-concepts.md)

| Input → Output shape | What n8n does automatically |
|---|---|
| 1 in → 1 out | Output links to that input. |
| 1 in → many out | All outputs link to that single input. |
| many in → many out, same count | Links **in order**: out-1↔in-1, out-2↔in-2, … |
| many in, **reordered / some removed** (items kept) | n8n adds correct linking automatically. |
| **counts differ**, or **brand-new items created** | n8n **cannot** link automatically. |

When n8n can't auto-link and the node doesn't supply linking, n8n raises an item-linking error.

### The lineage shape

In the Code node you express linkage with `pairedItem`, indexing into `$input.all()`:

```js
// 1:1 transform — preserve lineage explicitly
return $input.all().map((item, i) => ({
  json: { name: item.json.name.toUpperCase() },
  pairedItem: { item: i }
}));
```

`pairedItem: { item: i }` says "this output came from input index `i`". For simple maps you can rely on auto-pairing; once you reorder/merge/create items, set it yourself.

## "Can't get data for expression" — diagnosis & fix

`.item` (e.g. `$('Some Node').item`) walks the lineage thread back to the matching item in a previous node. It **fails** in exactly two cases (item-linking-errors.md):

| Error | Cause | Fix |
|---|---|---|
| **Info for expression missing from previous node** | A node in the chain returned **no pairing info** — broke the thread. Typically a Code node that didn't set `pairedItem`, or a custom/community node that doesn't emit linking. | In Code nodes, return `pairedItem`/which input produced each output. For community nodes, the node author must add linking. Or avoid `.item`. |
| **Multiple matching items for expression** | The thread points to **>1 item** in the previous node, so n8n can't pick one. Happens after Merge / Summarize / Aggregate (many items → one). | Use `.first()`, `.last()`, or `.all()[index]` instead of `.item`; **or** reference a different node holding the same info without the many-to-one collapse. |

Avoidance vs root-cause (item-linking-errors.md): you can sidestep `.item` with `.first()` / `.last()` / `.all()[index]` (you must know the item's position), or fix the lineage at its source.

## Referencing other nodes' items

You can reference **any previous node**, not just the immediate one (item-linking-errors.md). Common accessors:

| Expression | Returns |
|---|---|
| `$('Node Name').item` | The lineage-matched item for the current item. Throws on broken / ambiguous thread (above). |
| `$('Node Name').first()` | First output item of that node. |
| `$('Node Name').last()` | Last output item. |
| `$('Node Name').all()` | All output items (array); index with `.all()[i]`. |
| `$json` | Current item's `json` in the *current* node. |

`.first()/.last()/.all()[i]` are position-based and **don't** rely on the lineage thread — that's why they're the recommended escape hatch when `.item` fails.

## `itemMatching` in the Code node

To resolve a *specific* earlier node's item linked to the current input item by **input index**, use `("<node-name>").itemMatching(currentNodeInputIndex)` (data-mapping/itemmatching.md). Use this when an intermediate node stripped fields you need to restore from a node further back:

```js
// Restore email from an upstream node after a Set node dropped it
for (let i = 0; i < $input.all().length; i++) {
  $input.all()[i].json.restoreEmail =
    $('Customer Datastore (n8n training)').itemMatching(i).json.email;
}
return $input.all();
```

```python
# Python equivalent (underscore-prefixed builtins)
for i, item in enumerate(_input.all()):
    _input.all()[i].json.restoreEmail = \
        _('Customer Datastore (n8n training)').itemMatching(i).json.email
return _input.all()
```

`itemMatching(i)` follows the lineage thread from input item `i` to the named node — it works precisely *because* the intervening nodes preserved pairing (data-mapping/itemmatching.md).

## Binary data

Binary (files, images, documents) lives under the item's `binary` key, keyed by a **property name** (default `data`) (data/data-structure.md):

```json
{
  "json": { "fileName": "example.png" },
  "binary": {
    "apple-picture": {
      "data": "....",            // Base64-encoded payload — required
      "mimeType": "image/png",   // best practice — optional
      "fileExtension": "png",    // best practice — optional
      "fileName": "example.png"  // best practice — optional
    }
  }
}
```

Only `data` (the Base64 content) is required; `mimeType` / `fileExtension` / `fileName` are best-practice optionals (data/data-structure.md).

### Binary modes (self-hosting)

How a self-hosted instance **stores** binary data is configured via the binary-data environment variables (data/specific-data-types/binary-data.md). Two modes:

| Mode | Where the bytes live | When to use |
|---|---|---|
| **memory** (default) | In-process, inside the execution payload. | Small files, simple/single-instance setups. |
| **filesystem** | On disk; the item's `binary.<key>.data` holds a **reference**, not the Base64. | Larger files / scaling — avoids bloating execution data in memory. |

The mode is set by the binary-data env vars (storage mode + storage path); filesystem mode is the recommended path for scaling (binary-data.md references the scaling guide). [unverified: the exact env var names — e.g. `N8N_DEFAULT_BINARY_DATA_MODE`, `N8N_BINARY_DATA_STORAGE_PATH` — are not spelled out in the read doc; it links to hosting/configuration/environment-variables/binary-data.md. Confirm names there before quoting.]

### Working with binary

- Dedicated nodes (binary-data.md): **Convert to File** (data→file), **Extract From File** (file→JSON), **Read/Write Files from Disk** (disk I/O). XML/HTML have their own nodes; Compression/Edit Image/FTP for common tasks; **Local File Trigger** to fire on file changes.
- In the **Code node** you can manipulate binary directly (e.g. get the binary data buffer) (binary-data.md).
- **Security:** reading/writing binary files has security implications — disable it instance-wide with the `NODES_EXCLUDE` env var if not needed (binary-data.md).

## Pinning vs the live data contract

Pinned data (`pinData`, keyed by node NAME → array of `{json}` items) substitutes a node's output during **development** executions only — it is **not available in production** and edited pinned data is dev-only too (data/data-pinning.md). You can only pin nodes with a **single main output** (error outputs don't count). See execution-model.md for the manual-vs-production split. Don't ship a workflow whose correctness depends on pinned data.
