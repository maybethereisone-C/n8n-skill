# Odoo  (`n8n-nodes-base.odoo`)

- typeVersion (max): **2**  | group: transform  | trigger: no
- credentials: odooApi, odooApiKeyApi
- resources: activity, contact, custom, note, opportunity
- operations: create, delete, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | contact |  |  |
| `authentication` | Authentication | options | odooApiKeyApi |  |  |
