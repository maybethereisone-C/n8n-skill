# ActiveCampaign  (`n8n-nodes-base.activeCampaign`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: activeCampaignApi
- resources: account, accountContact, connection, contact, contactList, contactTag, deal, ecommerceCustomer, ecommerceOrder, ecommerceOrderProducts, list, tag
- operations: add, create, createNote, delete, get, getAll, getByOrderId, getByProductId, remove, update, updateNote

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | contact |  |  |
| `events` | Event Names or IDs | multiOptions | [] |  |  |
| `sources` | Source | multiOptions | [] |  |  |
