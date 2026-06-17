# Invoice Ninja Trigger — `n8n-nodes-base.invoiceNinjaTrigger`
**Type** `n8n-nodes-base.invoiceNinjaTrigger` · **typeVersion** 2 · **trigger**
**What:** Fires on Invoice Ninja business events (invoices, payments, clients, expenses, quotes, tasks, bank transactions) via webhook.
**Credentials:** `invoiceNinjaApi`

## Events (options)

| Resource | Events |
|---|---|
| client | created, updated, deleted |
| invoice | created, updated, deleted, paid, sent |
| payment | created, updated, deleted |
| quote | created, updated, deleted, approved |
| expense | created, updated, deleted |
| task | created, updated, deleted |
| bank_transaction | created, updated, deleted |

## Key params & gotchas
- `apiVersion` — `v4` (default) or `v5`; use v5 for Invoice Ninja v5+ instances.
- `event` — required options field; select the specific event.
- API-key auth only (no OAuth2 variant for this trigger).
- Companion app node: `n8n-nodes-base.invoiceNinja`.

**Source:** n8n-nodes-base.invoiceninjatrigger.md + schema  [doc-verified]
