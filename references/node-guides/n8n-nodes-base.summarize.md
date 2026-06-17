# Summarize — `n8n-nodes-base.summarize`

**Type** `n8n-nodes-base.summarize` · **typeVersion** 1.1 · **core**

**What:** Aggregates multiple input items into summary rows — pivot-table style (sum, count, average, min, max, append, concatenate, count-unique).

**Credentials:** none.

**Resources / Operations:**

| Aggregation | Description |
|---|---|
| Append | Collect all values into an array |
| Average | Numeric mean |
| Concatenate | Join values with separator |
| Count | Total item count |
| Count Unique | Distinct values only |
| Max / Min | Numeric extremes |
| Sum | Numeric total |

**Key params & gotchas:**

- **Fields to Summarize** — one or more `{aggregation, field}` pairs. Multiple aggregations on the same input field are supported.
- **Fields to Split By** — comma-separated; produces one summary row per unique combination (GROUP BY). Leave blank for a single global aggregate.
- **Output Format** — `Each Split in a Separate Item` (default, one item per group) vs `All Splits in a Single Item` (nested object). The nested form is harder to use downstream.
- **Continue if Field Not Found** (option) — default OFF throws an error when a summarize field is missing from all items. Turn ON to return an empty item instead.
- **Disable Dot Notation** (option) — dot notation for nested fields (`order.total`) is ON by default; disable only if field names literally contain dots.
- **Ignore items without valid fields to group by** — items missing a split-by field are dropped (turned on) or cause an error (turned off, default).
- `Count` counts the number of input items processed, not distinct values — use `Count Unique` for deduplicated counts.

**Source:** n8n-nodes-base.summarize.md  [doc-verified]
