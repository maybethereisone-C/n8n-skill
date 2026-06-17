# Hacker News  (`n8n-nodes-base.hackerNews`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: —
- resources: all, article, user
- operations: get, getAll

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | article |  |  |
| `operation` | Operation | options | getAll |  | res=all |
| `operation` | Operation | options | get |  | res=article |
| `operation` | Operation | options | get |  | res=user |
| `articleId` | Article ID | string |  | true | res=article,op=get |
| `username` | Username | string |  | true | res=user,op=get |
| `returnAll` | Return All | boolean | false |  | res=all,op=getAll |
| `limit` | Limit | number | 100 |  | res=all,op=getAll |
| `additionalFields` | Additional Fields | collection | {} |  | res=article,op=get |
| `additionalFields` | Additional Fields | collection | {} |  | res=all,op=getAll |
