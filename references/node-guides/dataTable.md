# Data Table — `n8n-nodes-base.dataTable`

**Type** `n8n-nodes-base.dataTable` · **typeVersion** 1 · **core**

**What:** Built-in n8n key-value data store (structured tables with typed columns). Manage tables and rows without an external database.

**Credentials:** None (internal n8n storage).

**Resources / Operations:**

| Resource | Operations |
|----------|-----------|
| Table | Create, Delete, List, Update (rename) |
| Row | Delete, Get, If Row Exists, If Row Does Not Exist, Insert, Update, Upsert |

**Key params & gotchas:**

**Table operations:**
- **Create → Reuse Existing Tables**: prevents errors when a workflow re-runs and the table already exists.
- **List → Filter by Name**: case-insensitive substring match on table name.
- Column types: Boolean, Date, Number, String — set at create time; schema is fixed after creation.

**Row operations:**
- **Conditions**: all row operations (Get, Delete, Update, Upsert) filter by conditions (Equals, Not Equals, GT, GTE, LT, LTE, Is Empty, Is Not Empty). Combine with **Must Match: Any / All**.
- **Mapping Column Mode**: "Map Each Column Manually" for mismatched field names; "Map Automatically" requires incoming field names to exactly match column names.
- **Insert → Optimize Bulk**: suppresses returned data for bulk inserts — up to 5× faster, but you get no confirmation rows back.
- **Upsert**: updates matching rows; inserts a new row if none match — ideal for sync workflows.
- **Dry Run** (Delete, Update, Upsert): simulates the operation and returns affected rows without modifying data — use for testing conditions.
- **If Row Exists / If Row Does Not Exist**: pass-through gates — output the input item unchanged if condition met, otherwise output nothing. Use for conditional branching without an IF node.
- **Get → Return All / Limit + Order By**: always add an order and limit in production to prevent unbounded reads.

**Source:** n8n-nodes-base.datatable/rows.md + n8n-nodes-base.datatable/tables.md  [doc-verified]
