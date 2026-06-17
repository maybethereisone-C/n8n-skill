# Zoho CRM — `n8n-nodes-base.zohocrm`
**Type** `n8n-nodes-base.zohocrm` · **typeVersion** 1 · **action**
**What:** Full CRUD plus upsert across Zoho CRM records: accounts, contacts, deals, invoices, leads, products, purchase orders, quotes, sales orders, and vendors.
**Credentials:** `zohoCrmOAuth2Api` (OAuth2; data center region must match the Zoho account region).

## Resources / Operations
| Resource | Operations |
|---|---|
| Account | Create, Upsert, Delete, Get, Get All, Update |
| Contact | Create, Upsert, Delete, Get, Get All, Update |
| Deal | Create, Upsert, Delete, Get, Get All, Update |
| Invoice | Create, Upsert, Delete, Get, Get All, Update |
| Lead | Create, Upsert, Delete, Get, Get All, Get Fields, Update |
| Product | Create, Upsert, Delete, Get, Get All, Update |
| Purchase Order | Create, Upsert, Delete, Get, Get All, Update |
| Quote | Create, Upsert, Delete, Get, Get All, Update |
| Sales Order | Create, Upsert, Delete, Get, Get All, Update |
| Vendor | Create, Upsert, Delete, Get, Get All, Update |

## Key params & gotchas
- **Upsert** requires a duplicate-check field (e.g., `Email`) configured in Zoho CRM's duplicate-check settings; otherwise it may create duplicate records.
- **Lead → Get Fields** returns the list of available field names, useful for dynamic field mapping.
- OAuth2 scopes must include the relevant module scopes (e.g., `ZohoCRM.modules.accounts.ALL`).
- Zoho data centers differ by region (`.com`, `.eu`, `.in`, etc.) — the OAuth2 credential must point to the correct data center or authentication will fail.
- This node supports use as an **AI tool** (can be called by AI Agent nodes).

**Source:** n8n-nodes-base.zohocrm.md  [doc-verified]
