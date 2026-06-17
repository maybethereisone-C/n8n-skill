# Code Node Cookbook (v2.26.0)

> Task → smallest correct snippet. Doctrine: **dedicated node → expression → minimal Code.** Reach here only when nodes/expressions can't express the transform. Every snippet is minimal-but-complete (all-items mode JS unless noted). Sourced from `code/cookbook/*`, `code/builtin/*`, `code/ai-code.md`, plus standard JS idioms marked `[unverified]` where not in the docs.

**Default contract:** all-items Code returns `[{json:{...}}, ...]`; each-item returns `{json:{...}}`. Set `pairedItem: { item: i }` when output count differs from input so downstream `$node` refs and item-linking stay correct. See code-node.md for the full surface.

---

## Count items from the previous node
`cookbook/code-node/number-items-last-node.md` — also handles the "1 empty item" case n8n emits for no data.
```js
const items = $input.all();
const n = Object.keys(items[0].json).length === 0 ? 0 : items.length;
return [{ json: { results: n } }];
```
Prefer the **Summarize** node for counts/sums/averages over a dataset; use Code only for custom logic.

## Find a record in a second dataset (cross-node lookup)
`code/ai-code.md` (example 1). Read another node's items by name, match on a key.
```js
const target = $("Mock Slack").all()[0];
const email = target.json.email;
const match = $input.all().find(u => u.json.person && u.json.person.email === email);
return match ? [{ json: { notionId: match.json.id } }] : [];
```

## Pick / reshape fields per item
`code/ai-code.md` (reference-data example). Prefer the **Set / Edit Fields** node first; Code only for nested logic.
```js
return $input.all().map((item, i) => ({
  json: {
    firstName: item.json.personal_info.first_name,
    jobTitle: item.json.work_info.job_title,
  },
  pairedItem: { item: i },
}));
```

## Join all items into one string
`code/ai-code.md` (example 2). Many→one, so emit a single item.
```js
const names = $input.all().map(i => `"${i.json.username}"`);
return [{ json: { usernames: names.join(", ") } }];
```

## Aggregate / count by category + top-N
`code/ai-code.md` (example 3). Build a summary item.
```js
const items = $input.all();
const counts = {};
for (const it of items) {
  const type = it.json.property_type?.[0] ?? "Unknown";
  counts[type] = (counts[type] || 0) + 1;
}
const top5 = [...items].sort((a, b) => b.json.votes - a.json.votes).slice(0, 5);
return [{ json: { counts, top5: top5.map(i => i.json.name) } }];
```
For plain grouped counts/sums, the **Summarize** node (`Split Out`/`Aggregate`) is usually enough — skip Code.

## Group items by a key → one item per group  `[unverified — standard idiom]`
Dedicated alternative: **Aggregate** node ("Aggregate items into groups"). Use Code only when the group shape is custom.
```js
const groups = {};
for (const it of $input.all()) {
  const k = it.json.category;
  (groups[k] ||= []).push(it.json);
}
return Object.entries(groups).map(([category, rows]) => ({ json: { category, rows, count: rows.length } }));
```

## Deduplicate items by a field  `[unverified — standard idiom]`
Dedicated alternative: **Remove Duplicates** node. Use Code for composite keys.
```js
const seen = new Set();
return $input.all().filter(it => {
  const k = it.json.email;
  if (seen.has(k)) return false;
  seen.add(k);
  return true;
});
```

## Cross-run dedupe (remember keys between executions)
`cookbook/builtin/get-workflow-static-data.md`. Workflow must be **active** + trigger/webhook-run to persist.
```js
const store = $getWorkflowStaticData('global');
store.seen ||= [];
const fresh = $input.all().filter(it => !store.seen.includes(it.json.id));
store.seen.push(...fresh.map(it => it.json.id));
return fresh;
```

## One item per element of an array field (flatten / explode)  `[unverified — standard idiom]`
Dedicated alternative: **Split Out** node. Use Code only when each child needs extra shaping.
```js
return $input.all().flatMap((it, i) =>
  (it.json.tags ?? []).map(tag => ({ json: { id: it.json.id, tag }, pairedItem: { item: i } }))
);
```

## Merge two node outputs by a shared key (join)  `[unverified — standard idiom]`
Dedicated alternative: **Merge** node, "Combine → by matching fields". Use Code for non-trivial join logic.
```js
const left = $input.all();
const right = $("Orders").all();
const byId = new Map(right.map(o => [o.json.userId, o.json]));
return left.map((it, i) => ({
  json: { ...it.json, order: byId.get(it.json.id) ?? null },
  pairedItem: { item: i },
}));
```

## Flatten nested JSON to dotted keys  `[unverified — standard idiom]`
```js
const flatten = (obj, prefix = "") =>
  Object.entries(obj).reduce((acc, [k, v]) => {
    const key = prefix ? `${prefix}.${k}` : k;
    if (v && typeof v === "object" && !Array.isArray(v)) Object.assign(acc, flatten(v, key));
    else acc[key] = v;
    return acc;
  }, {});
return $input.all().map((it, i) => ({ json: flatten(it.json), pairedItem: { item: i } }));
```

## Pivot rows → columns  `[unverified — standard idiom]`
Rows `{date, metric, value}` → one item per date with each metric as a column.
```js
const out = {};
for (const it of $input.all()) {
  const { date, metric, value } = it.json;
  (out[date] ||= { date })[metric] = value;
}
return Object.values(out).map(json => ({ json }));
```

## Query nested JSON with JMESPath
`builtin/jmespath.md`. JS only (`$jmespath`); native Python has no `_jmespath`.
```js
const data = $input.first().json;
return [{ json: { emails: $jmespath(data, "users[?active].email") } }];
```

## Date bucketing (group by day/month)  `[unverified — Luxon via $now/$today]`
`$now`/`$today` are Luxon `DateTime`. Parse arbitrary strings with `DateTime.fromISO`.
```js
const { DateTime } = require('luxon'); // available in expressions context; on Cloud use moment if luxon require fails
const buckets = {};
for (const it of $input.all()) {
  const day = DateTime.fromISO(it.json.createdAt).toFormat('yyyy-MM-dd');
  buckets[day] = (buckets[day] || 0) + 1;
}
return Object.entries(buckets).map(([day, count]) => ({ json: { day, count } }));
```
For simple date formatting prefer an **expression** (`{{ $json.createdAt.toDateTime().toFormat('yyyy-MM') }}`), not Code.

## Build N items programmatically
```js
return Array.from({ length: 10 }, (_, i) => ({ json: { index: i, label: `row-${i}` } }));
```

## Number / index items (add a running counter)
`cookbook/code-node/number-items-last-node.md` pattern, generalized.
```js
return $input.all().map((it, i) => ({ json: { ...it.json, rowNumber: i + 1 }, pairedItem: { item: i } }));
```

## Sort items
```js
return $input.all().sort((a, b) => b.json.votes - a.json.votes);
```

## Filter items by condition
Dedicated alternative: **Filter** node — use it unless the predicate is complex.
```js
return $input.all().filter(it => it.json.age >= 18);
```

## Paginate an API inside Code (loop until exhausted)
Prefer the **HTTP Request** node's built-in **Pagination** option (`cookbook/http-node/pagination.md`): Response-Contains-Next-URL (`{{ $response.body["next-page"] }}`) or Update-a-Parameter with `{{ $pageCount + 1 }}`. Drop to Code only for irregular pagination. `this.helpers.httpRequest` is the only in-Code HTTP path.
```js
const out = [];
let url = "https://api.example.com/items?page=1";
while (url) {
  const res = await this.helpers.httpRequest({ url, json: true });
  out.push(...res.data);
  url = res.next_url ?? null;        // stop when API stops giving a next URL
}
return out.map(json => ({ json }));
```

## HTTP request per item (enrich each row)
Dedicated alternative: an **HTTP Request** node downstream runs once per item automatically. Use Code only to batch/shape custom calls.
```js
const out = [];
for (const it of $input.all()) {
  const res = await this.helpers.httpRequest({ url: `https://api.example.com/u/${it.json.id}`, json: true });
  out.push({ json: { ...it.json, profile: res } });
}
return out;
```

## Read a binary file's bytes (hash / parse / rewrite)
`cookbook/code-node/get-binary-data-buffer.md`. JS only — `getBinaryDataBuffer` is unavailable in Python.
```js
const crypto = require('crypto');                 // crypto is provided on Cloud
const buf = await this.helpers.getBinaryDataBuffer(0, 'data'); // (itemIndex, propName)
const sha = crypto.createHash('sha256').update(buf).digest('hex');
return [{ json: { sha256: sha } }];
```

## Write a Buffer back as a binary property
`code-node.md` (binary section). Pair with `prepareBinaryData`.
```js
const buf = Buffer.from("col1,col2\n1,2\n", "utf8");
const data = await this.helpers.prepareBinaryData(buf, 'out.csv', 'text/csv');
return [{ json: {}, binary: { data } }];
```

## Tag items with a custom execution value (searchable)
`cookbook/builtin/execution.md`. Per-execution metadata, not cross-run state.
```js
$execution.customData.set("source", $json.channel);
return $input.all();
```

## Debug: inspect a value
`cookbook/code-node/console-log.md`. Writes to the **browser console**, not the run log.
```js
console.log(JSON.stringify($input.first().json, null, 2)); // avoid bare object → "[object Object]"
return $input.all();
```

## Read a specific branch/run of an upstream node
`cookbook/builtin/all.md`. `.all(branchIndex, runIndex)` — e.g. the "false" output (index 1) of an IF node, first run.
```js
const falseBranch = $("IF").all(1, 0);
return falseBranch;
```

## Native-Python variant (when JS isn't an option)
v2 native Python exposes **only** `_items` / `_item`, **bracket access only**, no other built-ins (`_snippets/.../code-node.md`). Pick fields:
```python
out = []
for item in _items:
    out.append({"json": {
        "name": item["json"].get("name", ""),
        "len": len(item["json"].get("name", "")),
    }})
return out
```
If you need `$()`, `$now`, static data, JMESPath, or binary buffers, write the node in **JavaScript** — native Python doesn't expose them.
