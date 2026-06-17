# SeaTable Trigger — `n8n-nodes-base.seaTableTrigger`
**Type** `n8n-nodes-base.seaTableTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires when rows are added or modified in a SeaTable collaborative database table (polling).
**Credentials:** `seatableApi` (API token + server URL).
**Resources / Operations:**
| Event | Notes |
|---|---|
| Row created | New row added to a table |
| Row updated | Existing row modified |

**Key params & gotchas:**
- **Polling** trigger — not a webhook; latency depends on n8n poll interval.
- Requires specifying the **Base** (workspace) and **Table** name.
- Self-hosted SeaTable: set the correct server URL in the credential.
- Deduplication uses row `_id` and `_mtime` fields stored between polls.

**Source:** n8n-nodes-base.seatabletrigger.md  [doc-verified]
