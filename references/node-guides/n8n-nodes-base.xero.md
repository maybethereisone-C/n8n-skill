# Xero — `n8n-nodes-base.xero`
**Type** `n8n-nodes-base.xero` · **typeVersion** 1 · **action**
**What:** Create and manage contacts and invoices in Xero accounting software.
**Credentials:** `xeroOAuth2Api` (OAuth2; scope must include `accounting.contacts` and `accounting.transactions`).

## Resources / Operations
| Resource | Operations |
|---|---|
| Contact | Create, Get, Get All, Update |
| Invoice | Create, Get, Get All, Update |

## Key params & gotchas
- OAuth2 tokens expire; ensure token refresh is configured or re-authenticate when workflows fail with 401.
- Invoice status transitions are constrained by Xero's state machine: a `DRAFT` invoice must move to `SUBMITTED` before payment can be applied.
- Get All contacts/invoices returns up to 100 records per page by default; use pagination options for large datasets.
- Xero API limits: 60 API calls per minute and 5,000 per day per tenant.

**Source:** n8n-nodes-base.xero.md  [doc-verified]
