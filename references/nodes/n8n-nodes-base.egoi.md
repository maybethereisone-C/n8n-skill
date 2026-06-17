# E-goi  (`n8n-nodes-base.egoi`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: egoiApi
- resources: contact
- operations: create, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | contact | true |  |
| `operation` | Operation | options | create | true |  |
| `list` | List Name or ID | options |  |  | op=getAll,op=create,op=update,op=get |
| `email` | Email | string |  |  | op=create |
| `contactId` | Contact ID | string |  |  | res=contact,op=update |
| `resolveData` | Resolve Data | boolean | true |  | op=create,op=update |
| `additionalFields` | Additional Fields | collection | {} |  | res=contact,op=create |
| `updateFields` | Update Fields | collection | {} |  | op=update |
| `by` | By | options | id |  | res=contact,op=get |
| `contactId` | Contact ID | string |  |  | res=contact,op=get |
| `email` | Email | string |  |  | res=contact,op=get |
| `returnAll` | Return All | boolean | false |  | res=contact,op=getAll |
| `limit` | Limit | number | 100 |  | res=contact,op=getAll |
| `simple` | Simplify | boolean | true |  | res=contact,op=get,op=getAll |
