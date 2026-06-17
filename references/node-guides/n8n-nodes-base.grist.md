# Grist — `n8n-nodes-base.grist`
**Type** `n8n-nodes-base.grist` · **typeVersion** 1 · **action**
**What:** Read, create, update, and delete rows in Grist spreadsheet tables.
**Credentials:** `gristApi` (API key + server URL).

## Resources / Operations
| Resource | Operations |
|---|---|
| Row | Create, Delete, Read (Get All), Update |

## Key params & gotchas
- Update/Delete require the **Row ID** (integer). Two ways to get it: (1) add a formula column `$id` in Grist, or (2) use the Read operation which returns `id` in every row — reference with `{{ $("GristNode").item.json.id }}`.
- **Get All** supports column-level **Filter** option; filters are AND-joined across columns, OR-joined within a column's value list (comma-separated).
- **Doc ID** and **Table ID** are required for every operation — find them in the Grist URL (`/doc/<docId>/p/...`).
- The API limit is 30,000 returned records regardless of the Limit param.

**Source:** n8n-nodes-base.grist.md  [doc-verified]
