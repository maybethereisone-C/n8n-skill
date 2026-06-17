# Freshdesk  (`n8n-nodes-base.freshdesk`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: freshdeskApi
- resources: contact, ticket
- operations: create, delete, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | ticket | true |  |
| `operation` | Operation | options | create | true | res=ticket |
| `requester` | Requester Identification | options | requesterId | true | res=ticket,op=create |
| `requesterIdentificationValue` | Value | string |  | true | res=ticket,op=create |
| `status` | Status | options | pending | true | res=ticket,op=create |
| `priority` | Priority | options | low | true | res=ticket,op=create |
| `source` | Source | options | portal | true | res=ticket,op=create |
| `jsonParameters` | JSON Parameters | boolean | false |  | res=ticket,op=create |
| `options` | Options | collection | {} |  | res=ticket,op=create |
| `customFieldsUi` | Custom Fields | fixedCollection |  |  | res=ticket,op=create |
| `customFieldsJson` | Custom Fields | json |  |  | res=ticket,op=create |
| `ticketId` | Ticket ID | string |  | true | res=ticket,op=update |
| `updateFields` | Update Fields | collection | {} |  | res=ticket,op=update |
| `ticketId` | Ticket ID | string |  | true | res=ticket,op=get |
| `returnAll` | Return All | boolean | false |  | res=ticket,op=getAll |
| `limit` | Limit | number | 5 |  | res=ticket,op=getAll |
| `options` | Options | collection | {} |  | res=ticket,op=getAll |
| `ticketId` | Ticket ID | string |  | true | res=ticket,op=delete |
