# Dropcontact  (`n8n-nodes-base.dropcontact`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: dropcontactApi
- resources: contact
- operations: enrich, fetchRequest

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | contact | true |  |
| `operation` | Operation | options | enrich | true |  |
| `requestId` | Request ID | string |  | true | res=contact,op=fetchRequest |
| `email` | Email | string |  |  | res=contact,op=enrich |
| `simplify` | Simplify Output (Faster) | boolean | false |  | res=contact,op=enrich |
| `additionalFields` | Additional Fields | collection | {} |  | res=contact,op=enrich |
| `options` | Options | collection | en |  | res=contact,op=enrich |
