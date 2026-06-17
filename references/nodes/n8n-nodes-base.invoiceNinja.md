# Invoice Ninja  (`n8n-nodes-base.invoiceNinja`)

- typeVersion (max): **2**  | group: output  | trigger: no
- credentials: invoiceNinjaApi
- resources: bank_transaction, client, expense, invoice, payment, quote, task
- operations: create, delete, email, get, getAll, matchPayment

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `apiVersion` | API Version | options | v4 |  |  |
| `resource` | Resource | options | client |  |  |
| `event` | Event | options |  | true |  |
