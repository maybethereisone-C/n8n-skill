# LoneScale  (`n8n-nodes-base.loneScale`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: loneScaleApi
- resources: item, list
- operations: add, create

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | list | true |  |
| `operation` | Operation | options | create |  | res=list |
| `operation` | Operation | options | add |  | res=item |
| `type` | Type | options | PEOPLE | true | res=item |
| `list` | List Name or ID | options |  | true | res=item |
| `first_name` | First Name | string |  | true | res=item,op=add |
| `last_name` | Last Name | string |  | true | res=item,op=add |
| `company_name` | Company Name | string |  |  | res=item,op=add |
| `peopleAdditionalFields` | Additional Fields | collection | {} |  | res=item,op=add |
| `companyAdditionalFields` | Additional Fields | collection | {} |  | res=item,op=add |
| `name` | Name | string |  | true | res=list,op=create |
| `type` | Type | options | COMPANY | true | res=list,op=create |
| `workflow` | Workflow Name | options |  | true |  |
