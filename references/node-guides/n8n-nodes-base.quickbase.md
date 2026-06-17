# Quick Base — `n8n-nodes-base.quickbase`
**Type** `n8n-nodes-base.quickbase` · **action**
**What:** CRUD operations on Quick Base (Quickbase) tables, records, reports, and files.
**Credentials:** `quickbaseApi`

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Field | Get All |
| File | Delete, Download |
| Record | Create, Delete, Get All, Update, Upsert |
| Report | Get, Run |

## Key params & gotchas
- Quick Base uses numeric field IDs (FIDs), not field names — use the Field → Get All operation to discover FIDs before constructing record payloads.
- Upsert merges on a specified key field (merge field ID); ensure it is set correctly or duplicate records will be created.
- Report → Run executes a saved Quickbase report and returns matching records; useful for complex filter logic defined in Quickbase UI.
- File Download returns binary data; pipe to Write Files or S3 node to persist.
- Quickbase API requires an **App token** scoped to the specific application and **User token** for auth.

**Source:** n8n-nodes-base.quickbase.md  [doc-verified]
