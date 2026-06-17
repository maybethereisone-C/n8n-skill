# Zoho CRM  (`n8n-nodes-base.zohoCrm`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: zohoOAuth2Api
- resources: account, contact, deal, invoice, lead, product, purchaseOrder, quote, salesOrder, vendor
- operations: create, delete, get, getAll, getFields, update, upsert

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | account |  |  |
