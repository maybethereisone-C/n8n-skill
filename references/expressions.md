# n8n Expressions — Exhaustive Reference (v2.26)

> Sources: expression-reference/index.md, expression-reference/root.md, expression-reference/execdata.md,
> expression-reference/nodeinputdata.md, expression-reference/nodeoutputdata.md,
> expression-reference/workflowdata.md, expression-reference/prevnodedata.md,
> expression-reference/string.md, expression-reference/array.md, expression-reference/number.md,
> expression-reference/datetime.md, expression-reference/object.md, expression-reference/boolean.md,
> expression-reference/customdata.md, expression-reference/httpresponse.md, expression-reference/item.md,
> specific-data-types/luxon.md, specific-data-types/jmespath.md, expressions.md,
> expressions-for-transformation.md, transforming-data.md, data-filtering.md

---

## 1. Literal vs Expression — the `=` prefix rule

A node parameter is a **literal string** by default. Wrap with `{{ }}` inside a value prefixed by `=` to activate evaluation.

```jsonc
"channel": "#general"                         // literal — braces never evaluated
"text":    "=Order {{ $json.orderId }}"       // expression string — parts in {{ }} evaluated
"email":   "={{ $json.email }}"              // pure expression (whole value from braces)
```

Rules:
- Without the leading `=` the `{{ }}` is treated as raw text — **silent wrong value, no error**.
- Inside `{{ }}` write a single JS expression (no `;`, no `return`, no multi-line). Use Code node for statements.
- Multi-statement IIFE pattern for inline complex logic:
  ```js
  {{(()=>{ let a = DateTime.fromISO('2024-01-01'); let b = $now; return b.diff(a,'days').days })()}}
  ```

---

## 2. Built-in Variables

### 2.1 Current item — `$json` / `$binary` / `$input.item`

| Variable | Returns | Example |
|---|---|---|
| `$json` | Current item's JSON payload. Shorthand for `$input.item.json` | `{{ $json.email }}` |
| `$json.field` | Top-level field | `{{ $json.body.city }}` |
| `$json['field']` | Bracket notation (required when key has spaces/dots) | `{{ $json['order-id'] }}` |
| `$binary` | Current item's binary map. Shorthand for `$input.item.binary` | `{{ $binary.data.fileName }}` |
| `$input.item` | The item currently being processed | `{{ $input.item.json.id }}` |
| `$itemIndex` | 0-based index of the current item in the input batch | `{{ $itemIndex }}` |

Source: expression-reference/root.md, expression-reference/nodeinputdata.md

### 2.2 Current node's input — `$input`

| Method/Prop | Returns | Example |
|---|---|---|
| `$input.item` | Current item | `{{ $input.item.json.name }}` |
| `$input.first(branchIdx?, runIdx?)` | First input item | `{{ $input.first().json.id }}` |
| `$input.last(branchIdx?, runIdx?)` | Last input item | `{{ $input.last().json.id }}` |
| `$input.all(branchIdx?, runIdx?)` | Array of all input items | `{{ $input.all().length }}` |
| `$input.params` | This node's own configuration parameters | `{{ $input.params.operation }}` |

Source: expression-reference/nodeinputdata.md

### 2.3 Other node's output — `$()`

| Method/Prop | Returns | Example |
|---|---|---|
| `$("Name")` | NodeOutputData accessor | — |
| `$("Name").item` | Paired item (item-linked to current) | `{{ $("Webhook").item.json.body.id }}` |
| `$("Name").first(branchIdx?, runIdx?)` | First output item | `{{ $("HTTP").first().json.status }}` |
| `$("Name").last(branchIdx?, runIdx?)` | Last output item | `{{ $("DB").last().json.id }}` |
| `$("Name").all(branchIdx?, runIdx?)` | All output items | `{{ $("Loop").all().length }}` |
| `$("Name").itemMatching(idx)` | Item that produced current node's item at index | `{{ $("Set").itemMatching(0).json.x }}` |
| `$("Name").isExecuted` | `true` if node ran on this path | `{{ $("If").isExecuted }}` |
| `$("Name").params` | That node's configuration | `{{ $("HTTP Request").params.url }}` |

Source: expression-reference/nodeoutputdata.md

> `$("Name").item` uses item-linking; `$("Name").first()` / `.all()` ignore pairing. A node not on the current execution path throws — guard with `.isExecuted`.

### 2.4 Previous node — `$prevNode`

| Prop | Returns | Example |
|---|---|---|
| `$prevNode.name` | Name of the node that sent the current item | `{{ $prevNode.name }}` |
| `$prevNode.outputIndex` | Output branch index it came from | `{{ $prevNode.outputIndex }}` |
| `$prevNode.runIndex` | Run index it came from | `{{ $prevNode.runIndex }}` |

Source: expression-reference/prevnodedata.md — always uses first input connector on multi-input nodes (e.g., Merge).

### 2.5 Execution metadata — `$execution` / `$exec`

> `$execution` and `$exec` refer to the same object. expression-reference/root.md and expression-reference/execdata.md use both aliases.

| Prop | Returns | Example |
|---|---|---|
| `$execution.id` | Current execution ID string | `{{ $execution.id }}` |
| `$execution.mode` | `"test"` / `"production"` / `"evaluation"` | `{{ $execution.mode }}` |
| `$execution.resumeUrl` | Webhook URL to resume a Wait node | `{{ $execution.resumeUrl }}` |
| `$execution.resumeFormUrl` | Form URL to resume a Wait node | `{{ $execution.resumeFormUrl }}` |
| `$execution.customData.get(key)` | Retrieve custom execution data | `{{ $execution.customData.get("orderId") }}` |
| `$execution.customData.set(key, val)` | Store custom execution data | `{{ $execution.customData.set("stage","paid") }}` |
| `$execution.customData.getAll()` | All custom key-value pairs | `{{ $execution.customData.getAll() }}` |
| `$execution.customData.setAll(obj)` | Set multiple custom pairs | — |

Source: expression-reference/execdata.md, expression-reference/customdata.md

### 2.6 Workflow metadata — `$workflow`

| Prop | Returns |
|---|---|
| `$workflow.id` | Workflow ID string |
| `$workflow.name` | Workflow name |
| `$workflow.active` | Boolean — whether workflow is active |

Source: expression-reference/workflowdata.md

### 2.7 Date/time — `$now` / `$today`

Both are Luxon `DateTime` objects. Source: expression-reference/root.md, specific-data-types/luxon.md

| Variable | Meaning |
|---|---|
| `$now` | Current instant (workflow timezone) |
| `$today` | Midnight of today in workflow timezone |

Common Luxon ops on `$now` / `$today`:

| Expression | Result |
|---|---|
| `$now.toISO()` | `2026-06-17T14:03:00.000+07:00` |
| `$now.toISODate()` | `2026-06-17` |
| `$now.toFormat('yyyy-LL-dd HH:mm')` | `2026-06-17 14:03` |
| `$now.plus({ days: 7 }).toISO()` | 7 days from now |
| `$now.minus({ hours: 2 }).toISO()` | 2 hours ago |
| `$now.startOf('month').toISODate()` | First of current month |
| `$now.endOf('month').toISODate()` | Last of current month |
| `$now.set({ hour: 9, minute: 0 }).toISO()` | Today at 09:00 |
| `$now.weekday` | 1=Mon … 7=Sun |
| `$now.weekNumber` | ISO week number |
| `$now.month` | 1–12 |
| `$now.year` | e.g. 2026 |
| `$now.hour` | 0–23 |
| `$now.diff($today, 'hours').hours` | Hours elapsed since midnight |
| `$now.diffTo(other, 'days')` | n8n wrapper for diff to another DateTime |
| `$now.diffToNow('minutes')` | Minutes between DateTime and now |
| `$now.toMillis()` | Unix ms |
| `$now.toSeconds()` | Unix seconds |
| `$now.toRelative()` | `"in 3 days"` |
| `$now.toLocal()` | Shift to local timezone |
| `$now.toUTC()` | Shift to UTC |
| `$now.setZone('Asia/Bangkok')` | Shift to named zone |
| `$now.setLocale('th').toLocaleString()` | Locale-formatted string |

Parse a string to DateTime:
```js
{{ DateTime.fromISO($json.createdAt) }}                    // ISO string
{{ DateTime.fromFormat($json.date, 'dd-MM-yyyy') }}        // custom format
{{ $json.createdAt.toDateTime() }}                         // n8n String method
{{ (1718600000000).toDateTime('ms') }}                     // epoch ms via Number method
```

Source: specific-data-types/luxon.md — avoid `new Date()`; it doesn't respect workflow timezone.

### 2.8 Variables and environment — `$vars` / `$env` / `$secrets`

| Variable | Meaning | Scope |
|---|---|---|
| `$vars.keyName` | n8n instance Variables (Settings → Variables) | All nodes |
| `$env.VAR_NAME` | OS environment variable (must be allow-listed) | All nodes |
| `$secrets.providerName.keyName` | External secrets vault value (never shown to user) | **Credential fields only** |

Source: expression-reference/root.md

### 2.9 Run/loop context

| Variable | Returns |
|---|---|
| `$runIndex` | Current run index of this node execution (starts at 0) |
| `$itemIndex` | 0-based index of item being processed |
| `$nodeVersion` | Version of current node (string) |
| `$parameter` | This node's own config parameters (same as `$input.params`) |
| `$pageCount` | Pages fetched — HTTP Request node only |

Source: expression-reference/root.md

### 2.10 HTTP request/response — `$request` / `$response`

Available only inside the HTTP Request node.

| Variable | Returns |
|---|---|
| `$request` | The outgoing request object |
| `$response.body` | Response body |
| `$response.headers` | Response headers |
| `$response.statusCode` | HTTP status code |
| `$response.statusMessage` | Status message |

Source: expression-reference/root.md, expression-reference/httpresponse.md

---

## 3. Built-in Functions

### 3.1 Conditional helpers

| Function | Signature | Example |
|---|---|---|
| `$if` | `$if(condition, valueIfTrue, valueIfFalse)` | `{{ $if($now.hour < 17, "day", "evening") }}` |
| `$ifEmpty` | `$ifEmpty(value, fallback)` | `{{ $ifEmpty($json.city, "Unknown") }}` |
| Ternary | `condition ? a : b` | `{{ $json.active ? "yes" : "no" }}` |

Empty for `$ifEmpty`: `""`, `[]`, `{}`, `null`, `undefined`. Source: expression-reference/root.md

### 3.2 Math helpers

| Function | Example |
|---|---|
| `$max(n1, n2, …)` | `{{ $max($json.a, $json.b, 100) }}` |
| `$min(n1, n2, …)` | `{{ $min($json.price, 99) }}` |

Source: expression-reference/root.md

### 3.3 JMESPath — `$jmespath`

```js
$jmespath(obj, expression)
```

Query complex nested JSON without chaining optional-chain operators. Returns `undefined` if the expression is invalid. Source: expression-reference/root.md, specific-data-types/jmespath.md

| Pattern | Expression | Result |
|---|---|---|
| All values of a key | `"[*].name"` | `["Bob","Fred"]` |
| Slice | `"[:2].name"` | First 2 names |
| Filter | `"[?age > \`20\`].name"` | Names where age > 20 |
| First filtered | `"[?age > \`20\`].name \| [0]"` | First match |
| Object projection | `"*.age"` | All ages from object values |
| Multiselect list | `"[].[first, last]"` | Array of `[first, last]` pairs |
| Nested filter | `"reservations[].guests[?requirements.room==\`double\`].name"` | Deep filter |
| Use on all() items | `$jmespath($("Code").all(), "[?json.name=='Lenovo'].json.category_id")` | Search across items |

> Note: n8n's `jmespath.js` parameter order is `(object, searchString)` — opposite of the JMESPath spec examples.

### 3.4 AI tool helper — `$fromAI`

```js
$fromAI(key, description?, type?, defaultValue?)
```

Lets an LLM fill in a node parameter value. **Only valid inside a Tool sub-node wired to an AI Agent node.** Throws "No execution data available" elsewhere.

| Param | Type | Notes |
|---|---|---|
| `key` | String | Letters, numbers, `_`, `-` only |
| `description` | String (opt) | Improves model accuracy |
| `type` | String (opt) | `string` / `number` / `boolean` / `json` / `date` / `datetime` |
| `defaultValue` | any (opt) | Fallback if model returns nothing |

Example: `{{ $fromAI('email', 'User email address', 'string') }}`

Source: expression-reference/root.md

---

## 4. String Methods

All callable on any string value via dot notation inside `{{ }}`. Source: expression-reference/string.md

| Method | Description | Example |
|---|---|---|
| `.toUpperCase()` | ALL CAPS | `{{ $json.name.toUpperCase() }}` |
| `.toLowerCase()` | all lower | `{{ $json.name.toLowerCase() }}` |
| `.toTitleCase()` | Title Case (short words excluded) | `{{ $json.title.toTitleCase() }}` |
| `.toSentenceCase()` | First letter of each sentence capitalized | `{{ $json.body.toSentenceCase() }}` |
| `.toSnakeCase()` | `snake_case` | `{{ $json.label.toSnakeCase() }}` |
| `.trim()` | Remove leading/trailing whitespace | `{{ $json.input.trim() }}` |
| `.includes(s, start?)` | Boolean — contains `s` (case-sensitive) | `{{ $json.text.includes("error") }}` |
| `.startsWith(s, start?)` | Boolean | `{{ $json.url.startsWith("https") }}` |
| `.indexOf(s, start?)` | First position or -1 | `{{ $json.str.indexOf("@") }}` |
| `.replace(pattern, replacement)` | Replace first occurrence | `{{ $json.s.replace("foo","bar") }}` |
| `.replaceAll(pattern, replacement)` | Replace all occurrences | `{{ $json.s.replaceAll(" ","_") }}` |
| `.replaceSpecialChars()` | Replace non-ASCII with closest ASCII | `{{ $json.name.replaceSpecialChars() }}` |
| `.split(sep?, limit?)` | String → array | `{{ $json.csv.split(",") }}` |
| `.slice(start, end?)` | Substring by index | `{{ $json.code.slice(0, 3) }}` |
| `.substring(start, end?)` | Substring by index | `{{ $json.s.substring(2, 5) }}` |
| `.match(regexp)` | First match or all (with `g` flag) | `{{ $json.text.match(/\d+/g) }}` |
| `.search(regexp)` | Index of first regex match or -1 | `{{ $json.s.search(/\d/) }}` |
| `.concat(s1, s2?, …)` | Join strings | `{{ $json.first.concat(" ", $json.last) }}` |
| `.length` | Character count | `{{ $json.name.length }}` |
| `.isEmpty()` | `true` if `""` or `null` | `{{ $json.field.isEmpty() }}` |
| `.isNotEmpty()` | `true` if has ≥1 char | — |
| `.isEmail()` | Validate email | `{{ $json.address.isEmail() }}` |
| `.isUrl()` | Validate URL | `{{ $json.link.isUrl() }}` |
| `.isDomain()` | Validate domain | — |
| `.isNumeric()` | `true` if string represents a number | — |
| `.extractEmail()` | First email found, else `undefined` | `{{ $json.body.extractEmail() }}` |
| `.extractUrl()` | First URL found (must start with `http`) | `{{ $json.body.extractUrl() }}` |
| `.extractDomain()` | Domain from URL/email | `{{ $json.link.extractDomain() }}` |
| `.extractUrlPath()` | Path after domain | `{{ $json.url.extractUrlPath() }}` |
| `.toDateTime()` | Parse to Luxon DateTime (ISO/RFC2822/SQL/ms epoch) | `{{ $json.createdAt.toDateTime() }}` |
| `.toNumber()` | String → number | `{{ $json.qty.toNumber() }}` |
| `.toBoolean()` | `"false"/"0"/"no"` → `false`, else `true` (case-insensitive) | — |
| `.toJsonString()` | Escape and wrap in quotes (like `JSON.stringify`) | — |
| `.parseJson()` | JSON string → object/value | `{{ $json.payload.parseJson().id }}` |
| `.hash(algo?)` | Hash string (default md5) | `{{ $json.secret.hash("sha256") }}` |
| `.base64Encode()` | → base64 | `{{ $json.text.base64Encode() }}` |
| `.base64Decode()` | base64 → plain text | `{{ $json.encoded.base64Decode() }}` |
| `.urlEncode(allChars?)` | Percent-encode for URL | `{{ $json.query.urlEncode() }}` |
| `.urlDecode(allChars?)` | Decode `%XX` sequences | — |
| `.removeMarkdown()` | Strip Markdown and HTML tags | `{{ $json.md.removeMarkdown() }}` |
| `.removeTags()` | Strip HTML/XML tags | — |
| `.quote(mark?)` | Wrap in quotes, escape internal quotes | — |

---

## 5. Array Methods

Source: expression-reference/array.md

| Method | Description | Example |
|---|---|---|
| `.length` | Element count | `{{ $json.items.length }}` |
| `.first()` | First element | `{{ $json.items.first() }}` |
| `.last()` | Last element | `{{ $json.items.last() }}` |
| `.isEmpty()` | `true` if empty or null | `{{ $json.tags.isEmpty() }}` |
| `.isNotEmpty()` | `true` if ≥1 element | — |
| `.includes(elem, start?)` | Boolean — element present | `{{ $json.ids.includes(42) }}` |
| `.indexOf(elem, start?)` | Position or -1 | — |
| `.filter(fn)` | Keep elements matching condition | `{{ $json.items.filter(x => x.active) }}` |
| `.find(fn)` | First matching element (or `undefined`) | `{{ $json.items.find(x => x.id === 5) }}` |
| `.map(fn)` | Transform each element | `{{ $json.items.map(x => x.id) }}` |
| `.reduce(fn, init)` | Accumulate to single value | `{{ $json.nums.reduce((acc,n) => acc+n, 0) }}` |
| `.sort(fn?)` | Sort (no arg = alphabetical; provide comparator for numbers/objects) | `{{ $json.names.sort() }}` |
| `.reverse()` | Reverse order | `{{ $json.items.reverse() }}` |
| `.join(sep?)` | Array → string | `{{ $json.tags.join(", ") }}` |
| `.slice(start, end)` | Sub-array | `{{ $json.items.slice(0, 5) }}` |
| `.append(e1, e2?, …)` | Add elements, returns new array | `{{ $json.ids.append(99) }}` |
| `.concat(arr2, …)` | Join arrays | `{{ $json.a.concat($json.b) }}` |
| `.union(otherArray)` | Concatenate + deduplicate | — |
| `.unique()` | Remove duplicate primitives | `{{ $json.tags.unique() }}` |
| `.removeDuplicates(keys?)` | Remove duplicates (objects by key) | `{{ $json.orders.removeDuplicates("id") }}` |
| `.compact()` | Remove `null`, `""`, `undefined` | `{{ $json.list.compact() }}` |
| `.chunk(n)` | Split into sub-arrays of size `n` | `{{ $json.ids.chunk(10) }}` |
| `.pluck(field, …)` | Extract field(s) from array of objects | `{{ $json.users.pluck("email") }}` |
| `.smartJoin(keyField, valField)` | Array of `{key,val}` objects → single object | `{{ $json.pairs.smartJoin("k","v") }}` |
| `.renameKeys(from, to, …)` | Rename keys in each object | `{{ $json.rows.renameKeys("Id","id") }}` |
| `.difference(other)` | Elements in base not in other | `{{ $json.a.difference($json.b) }}` |
| `.intersection(other)` | Elements in both arrays | `{{ $json.a.intersection($json.b) }}` |
| `.sum()` | Sum of numbers (throws on non-number) | `{{ $json.prices.sum() }}` |
| `.average()` | Mean (throws on non-number) | `{{ $json.scores.average() }}` |
| `.min()` | Smallest number | `{{ $json.vals.min() }}` |
| `.max()` | Largest number | `{{ $json.vals.max() }}` |
| `.randomItem()` | Random element | `{{ $json.options.randomItem() }}` |
| `.toSpliced(start, del, e1…)` | Non-mutating splice | — |
| `.toJsonString()` | → JSON string | `{{ $json.items.toJsonString() }}` |
| `.toString()` | → comma-joined string | — |

---

## 6. Number Methods

Source: expression-reference/number.md

| Method | Description | Example |
|---|---|---|
| `.round(places?)` | Round to nearest (or N decimals) | `{{ $json.price.round(2) }}` |
| `.ceil()` | Round up | `{{ $json.val.ceil() }}` |
| `.floor()` | Round down | `{{ $json.val.floor() }}` |
| `.abs()` | Absolute value | `{{ $json.delta.abs() }}` |
| `.isEven()` | Boolean (throws on non-integer) | — |
| `.isOdd()` | Boolean (throws on non-integer) | — |
| `.isInteger()` | Boolean | — |
| `.isEmpty()` | Always `false`; `true` only for `null` | — |
| `.toBoolean()` | `0` → `false`, else `true` | — |
| `.toString(radix?)` | Number → string | `{{ (255).toString(16) }}` // "ff" |
| `.toLocaleString(locale?, opts?)` | Localised number string | `{{ $json.amount.toLocaleString('th-TH') }}` |
| `.format(locale?, opts?)` | `Intl.NumberFormat` wrapper | `{{ $json.price.format('en-US', {style:'currency',currency:'USD'}) }}` |
| `.toDateTime(format?)` | Epoch → Luxon DateTime (default: ms) | `{{ $json.ts.toDateTime() }}` |

---

## 7. Object Methods

Source: expression-reference/object.md

| Method | Description | Example |
|---|---|---|
| `.keys()` | Array of field names | `{{ $json.meta.keys() }}` |
| `.values()` | Array of field values | `{{ $json.meta.values() }}` |
| `.hasField(name)` | Boolean — top-level key exists (case-sensitive) | `{{ $json.data.hasField("email") }}` |
| `.isEmpty()` | `true` if no keys or `null` | — |
| `.isNotEmpty()` | `true` if ≥1 key | — |
| `.compact()` | Remove `null` and `""` fields | `{{ $json.row.compact() }}` |
| `.merge(other)` | Merge; base wins on key conflict | `{{ $json.defaults.merge($json.overrides) }}` |
| `.removeField(key)` | Remove one field | `{{ $json.user.removeField("password") }}` |
| `.removeFieldsContaining(val)` | Remove fields whose string value contains `val` | — |
| `.keepFieldsContaining(val)` | Keep only fields whose value contains `val` | — |
| `.toJsonString()` | → JSON string | — |
| `.urlEncode()` | → `key=val&key2=val2` (top-level only) | `{{ $json.params.urlEncode() }}` |

---

## 8. DateTime Methods (Luxon object)

Source: expression-reference/datetime.md. These are available on any Luxon `DateTime` (including `$now`, `$today`, and values from `.toDateTime()`).

**Properties (read-only):**

| Prop | Returns |
|---|---|
| `.year` | e.g. 2026 |
| `.month` | 1–12 |
| `.day` | 1–31 |
| `.hour` | 0–23 |
| `.minute` | 0–59 |
| `.second` | 0–59 |
| `.millisecond` | 0–999 |
| `.weekday` | 1=Mon … 7=Sun |
| `.weekNumber` | 1–52ish |
| `.quarter` | 1–4 |
| `.monthLong` | `"October"` |
| `.monthShort` | `"Oct"` |
| `.weekdayLong` | `"Wednesday"` |
| `.weekdayShort` | `"Wed"` |
| `.locale` | e.g. `"en-GB"` |
| `.zone` | Time zone name |
| `.isInDST` | Boolean |

**Methods:**

| Method | Description | Example |
|---|---|---|
| `.plus(n, unit?)` | Add duration | `$now.plus({ days: 7 })` |
| `.minus(n, unit?)` | Subtract duration | `$now.minus({ months: 1 })` |
| `.set(values)` | Override specific units | `$now.set({ hour: 0, minute: 0 })` |
| `.startOf(unit)` | Round down to start of unit | `$now.startOf('week')` |
| `.endOf(unit)` | Round up to end of unit | `$now.endOf('month')` |
| `.toISO(opts?)` | ISO 8601 string | `$now.toISO()` |
| `.toISODate()` | `YYYY-MM-DD` [unverified — Luxon method not in n8n docs] | `$now.toISODate()` |
| `.toFormat(fmt)` | Custom format string | `$now.toFormat('yyyy-LL-dd')` |
| `.toLocaleString(fmtOpts?)` | Locale-aware string | `$now.toLocaleString({month:'long',day:'numeric'})` |
| `.toMillis()` | Unix ms | `$now.toMillis()` |
| `.toSeconds()` | Unix seconds | `$now.toSeconds()` |
| `.toString()` | ISO-like string | — |
| `.toRelative(opts?)` | `"in 3 days"` | `$now.toRelative()` |
| `.toLocal()` | Convert to workflow local tz | — |
| `.toUTC(offset?, opts?)` | Convert to UTC | `$now.toUTC()` |
| `.setZone(zone, opts?)` | Convert to named tz | `$now.setZone('Asia/Bangkok')` |
| `.setLocale(locale)` | Set locale for formatting | `$now.setLocale('th')` |
| `.diff(other, unit)` | Duration between two DateTimes | `$now.diff($today, 'hours').hours` |
| `.diffTo(other, unit)` | n8n alias for diff | — |
| `.diffToNow(unit)` | Duration from DateTime to now | — |
| `.equals(other)` | Strict equality (same instant + tz) | — |
| `.hasSame(other, unit)` | Same unit value (ignores tz) | — |
| `.isBetween(d1, d2)` | Boolean | — |
| `.extract(unit?)` | Extract unit as number | — |
| `.format(fmt)` | Same as `toFormat()` | — |

Luxon format tokens: `yyyy` year, `LL` 2-digit month, `dd` day, `HH` 24h hour, `mm` minutes, `ss` seconds. Full table: moment.github.io/luxon/#/formatting

---

## 9. Boolean Methods

Source: expression-reference/boolean.md

| Method | Returns |
|---|---|
| `.toNumber()` | `true` → 1, `false` → 0 |
| `.toString()` | `"true"` / `"false"` |
| `.isEmpty()` | Always `false` (except `null` → `true`) |

---

## 10. BinaryFile Properties

Source: expression-reference/binaryfile.md, accessible via `$binary.keyName.*`

| Prop | Returns |
|---|---|
| `.fileName` | Filename including extension |
| `.fileExtension` | Extension only (e.g. `txt`) |
| `.fileSize` | Size as string |
| `.fileType` | Type string (e.g. `image`) |
| `.mimeType` | MIME type (e.g. `image/jpeg`) |
| `.id` | Unique file ID |
| `.directory` | Directory path (not set for DB storage) |

---

## 11. Transformation Cookbook

### Dates

```js
// Parse ISO string from upstream node
{{ DateTime.fromISO($json.startDate).toFormat('dd/MM/yyyy') }}

// Add 30 days to a timestamp field
{{ $json.expiresAt.toDateTime().plus({ days: 30 }).toISO() }}

// Days between two ISO strings
{{ DateTime.fromISO($json.endDate).diff(DateTime.fromISO($json.startDate), 'days').days }}

// Format current date for a filename
{{ $now.toFormat('yyyyLLdd_HHmm') }}

// Is today before a deadline?
{{ $now < DateTime.fromISO($json.deadline) ? "on time" : "overdue" }}

// First day of last month
{{ $now.minus({ months: 1 }).startOf('month').toISO() }}
```

### Strings

```js
// Sanitize to snake_case key
{{ $json.label.toSnakeCase() }}

// Build email subject from fields
{{ "Order #" + $json.orderId + " — " + $json.status.toUpperCase() }}

// Extract domain from user email
{{ $json.email.extractDomain() }}

// Strip HTML from a rich-text field
{{ $json.description.removeTags() }}

// Hash a value for deduplication
{{ $json.email.hash("sha256") }}

// Parse nested JSON string
{{ $json.metadata.parseJson().userId }}
```

### Arrays

```js
// Collect all IDs from previous node's items
{{ $("Get Records").all().map(item => item.json.id) }}

// Sum a numeric field across items
{{ $("Orders").all().map(i => i.json.total).sum() }}

// Filter active users
{{ $json.users.filter(u => u.active).pluck("email") }}

// Deduplicate tags
{{ $json.tags.unique() }}

// First 3 items
{{ $json.items.slice(0, 3) }}

// Join array to string
{{ $json.roles.join(", ") }}

// Group-by simulation: pluck + smartJoin
{{ $json.settings.smartJoin("key", "value") }}
```

### Objects

```js
// Remove sensitive fields before logging
{{ $json.user.removeField("password").removeField("token") }}

// Merge defaults with incoming data
{{ { defaultLang: "en", timezone: "UTC" }.merge($json.prefs) }}

// Build query string from object
{{ $json.filters.urlEncode() }}

// Check a field exists before using it
{{ $json.meta.hasField("source") ? $json.meta.source : "direct" }}
```

---

## 12. Common Mistakes

| Mistake | Wrong | Correct |
|---|---|---|
| Missing `=` prefix | `"{{ $json.id }}"` | `"={{ $json.id }}"` |
| Webhook body nesting | `$json.name` | `$json.body.name` |
| Referencing unrun node | `$("IfNode").first().json.x` (on false branch) | Guard: `$("IfNode").isExecuted ? … : fallback` |
| Unguarded null chain | `$json.user.address.city` | `$json.user?.address?.city ?? ""` |
| Using statements in `{{ }}` | `{{ let x = 1; x + 1 }}` | Use IIFE or Code node |
| Mutating with `push` / `splice` | `$json.arr.push(1)` | `$json.arr.append(1)` |
| `new Date()` ignores tz | `new Date()` | `$now` or `DateTime.now()` |
| `$fromAI` outside AI tool | Use in Code node | Only valid in Tool sub-node wired to AI Agent |
| `$secrets` in non-credential field | `{{ $secrets.vault.key }}` in node param | Only available in credential fields |
| String `format()` (Moment) | `$now.format('YYYY-MM-DD')` | `$now.toFormat('yyyy-LL-dd')` (Luxon) |
