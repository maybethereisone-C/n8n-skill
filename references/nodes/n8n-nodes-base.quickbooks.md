# QuickBooks Online  (`n8n-nodes-base.quickbooks`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: quickBooksOAuth2Api
- resources: bill, customer, employee, estimate, invoice, item, payment, purchase, transaction, vendor
- operations: create, delete, get, getAll, getReport, send, update, void

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | customer |  |  |
