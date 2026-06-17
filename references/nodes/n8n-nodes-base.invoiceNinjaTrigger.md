# Invoice Ninja Trigger  (`n8n-nodes-base.invoiceNinjaTrigger`)

- typeVersion (max): **2**  | group: trigger  | trigger: yes
- credentials: invoiceNinjaApi
- resources: bank_transaction, client, expense, invoice, payment, quote, task
- operations: create, delete, email, get, getAll, matchPayment

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `apiVersion` | API Version | options | v4 |  |  |
| `event` | Event | options |  | true |  |
| `resource` | Resource | options | client |  |  |
