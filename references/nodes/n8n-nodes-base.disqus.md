# Disqus  (`n8n-nodes-base.disqus`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: disqusApi
- resources: forum
- operations: get, getCategories, getPosts, getThreads

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | forum |  |  |
| `operation` | Operation | options | get |  | res=forum |
| `id` | Forum Name | string |  | true | res=forum,op=get |
| `additionalFields` | Additional Fields | collection | {} |  | res=forum,op=get |
| `id` | Forum Name | string |  | true | res=forum,op=getPosts |
| `returnAll` | Return All | boolean | false |  | res=forum,op=getPosts |
| `limit` | Limit | number | 100 |  | res=forum,op=getPosts |
| `additionalFields` | Additional Fields | collection | asc |  | res=forum,op=getPosts |
| `id` | Forum Name | string |  | true | res=forum,op=getCategories |
| `returnAll` | Return All | boolean | false |  | res=forum,op=getCategories |
| `limit` | Limit | number | 100 |  | res=forum,op=getCategories |
| `additionalFields` | Additional Fields | collection | asc |  | res=forum,op=getCategories |
| `id` | Forum Name | string |  | true | res=forum,op=getThreads |
| `returnAll` | Return All | boolean | false |  | res=forum,op=getThreads |
| `limit` | Limit | number | 100 |  | res=forum,op=getThreads |
| `additionalFields` | Additional Fields | collection | asc |  | res=forum,op=getThreads |
