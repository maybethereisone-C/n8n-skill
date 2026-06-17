# Stackby — `n8n-nodes-base.stackby`
**Type** `n8n-nodes-base.stackby` · **typeVersion** 1 · **action**
**What:** Read, append, delete, and list records in Stackby spreadsheet-database tables.
**Credentials:** `stackbyApi`
**Resources / Operations:**
| Operation |
|---|
| Append |
| Delete |
| List |
| Read |

**Key params & gotchas:**
- Operations target a specific Stack and Table — both IDs must be provided.
- No dedicated Update operation; use Delete + Append to replace a record.

**Source:** n8n-nodes-base.stackby.md  [doc-verified]
