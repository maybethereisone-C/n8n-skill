# Coda — `n8n-nodes-base.coda`
**Type** `n8n-nodes-base.coda` · **action**
**What:** Read/write Coda docs — tables, views, controls, formulas, and row-level button pushes.
**Credentials:** codaApi (API token).

## Resources / Operations
| Resource | Operations |
|---|---|
| Control | Get, Get All |
| Formula | Get, Get All |
| Table | Create/Insert Row, Delete Row(s), Get All Columns, Get All Rows, Get Column, Get Row, Push Button |
| View | Delete View Row, Get, Get All, Get All Columns, Get All Rows, Update Row, Push Button |

## Key params & gotchas
- **Table Insert Row** — column values are key-value pairs using the column name (not ID); name must match exactly.
- **Push Button** — triggers a button column for a specific row; the button must be configured to run a formula.
- Doc ID and Table/View ID are required and appear in the Coda URL (`d/<docId>/...`).
- Coda API rate limits apply per token; avoid tight polling loops without a Wait node.

**Source:** n8n-nodes-base.coda.md  [doc-verified]
