# Unleashed Software — `n8n-nodes-base.unleashedsoftware`
**Type** `n8n-nodes-base.unleashedsoftware` · **typeVersion** 1 · **action**
**What:** Read sales orders and stock-on-hand data from Unleashed Software (inventory management).
**Credentials:** `unleashedSoftwareApi` (API ID + API Key from Unleashed account settings).
**Resources / Operations:**
| Resource | Operation |
|----------|-----------|
| Sales Order | Get All |
| Stock On Hand | Get (single), Get All |

**Key params & gotchas:** Read-only integration — no create/update/delete. Pagination uses Unleashed's page-based API; "Get All" handles it automatically.
**Source:** n8n-nodes-base.unleashedsoftware.md  [doc-verified]
