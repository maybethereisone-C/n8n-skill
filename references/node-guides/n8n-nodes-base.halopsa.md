# HaloPSA — `n8n-nodes-base.halopsa`
**Type** `n8n-nodes-base.halopsa` · **typeVersion** 1 · **action**
**What:** Manage HaloPSA clients, sites, tickets, and users (MSP PSA platform).
**Credentials:** `haloPsaApi` (OAuth2 client credentials — Tenant URL + Client ID + Secret).

## Resources / Operations
| Resource | Operations |
|---|---|
| Client | Create, Delete, Get, Get All, Update |
| Site | Create, Delete, Get, Get All, Update |
| Ticket | Create, Delete, Get, Get All, Update |
| User | Create, Delete, Get, Get All, Update |

## Key params & gotchas
- HaloPSA uses OAuth2 **client credentials** flow (not user login) — the credential requires a dedicated API application configured in HaloPSA settings.
- **Ticket** creation requires at minimum a `summary` and a valid `tickettype_id`; look up ticket type IDs via the HaloPSA UI or API before automating.
- **Site** is a child of **Client** — always link a site to a client when creating.
- Get All operations support pagination; use **Return All** or set **Limit** + **Page** manually.

**Source:** n8n-nodes-base.halopsa.md  [doc-verified]
