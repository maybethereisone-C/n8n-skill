# Mailcheck  (`n8n-nodes-base.mailcheck`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: mailcheckApi
- resources: email
- operations: check

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | email |  |  |
| `operation` | Operation | options | check |  | res=email |
| `email` | Email | string |  |  | res=email,op=check |
