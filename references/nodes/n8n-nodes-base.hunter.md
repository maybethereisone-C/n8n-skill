# Hunter  (`n8n-nodes-base.hunter`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: hunterApi
- operations: domainSearch, emailFinder, emailVerifier

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `operation` | Operation | options | domainSearch |  |  |
| `domain` | Domain | string |  | true | op=domainSearch |
| `onlyEmails` | Only Emails | boolean | true |  | op=domainSearch |
| `returnAll` | Return All | boolean | false |  | op=domainSearch |
| `limit` | Limit | number | 100 |  | op=domainSearch |
| `filters` | Filters | collection | {} |  | op=domainSearch |
| `domain` | Domain | string |  | true | op=emailFinder |
| `firstname` | First Name | string |  | true | op=emailFinder |
| `lastname` | Last Name | string |  | true | op=emailFinder |
| `email` | Email | string |  | true | op=emailVerifier |
