# ActiveCampaign Trigger  (`n8n-nodes-base.activeCampaignTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: activeCampaignApi
- resources: account, accountContact, connection, contact, contactList, contactTag, deal, ecommerceCustomer, ecommerceOrder, ecommerceOrderProducts, list, tag
- operations: add, create, createNote, delete, get, getAll, getByOrderId, getByProductId, remove, update, updateNote

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `events` | Event Names or IDs | multiOptions | [] |  |  |
| `sources` | Source | multiOptions | [] |  |  |
| `resource` | Resource | options | contact |  |  |
