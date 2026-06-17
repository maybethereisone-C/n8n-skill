# Jina AI  (`n8n-nodes-base.jinaAi`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: jinaAiApi
- resources: reader, research
- operations: deepResearch, read, search

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | reader |  |  |
| `operation` | Operation | options | read |  | res=reader |
| `operation` | Operation | options | deepResearch |  | res=research |
| `url` | URL | string |  | true | res=reader,op=read |
| `simplify` | Simplify | boolean | true |  | res=reader,op=read |
| `options` | Options | collection | {} |  | res=reader,op=read |
| `searchQuery` | Search Query | string |  | true | res=reader,op=search |
| `simplify` | Simplify | boolean | true |  | res=reader,op=search |
| `options` | Options | collection | {} |  | res=reader,op=search |
| `researchQuery` | Research Query | string |  | true | res=research,op=deepResearch |
| `simplify` | Simplify | boolean | true |  | res=research,op=deepResearch |
| `options` | Options | collection | {} |  | res=research,op=deepResearch |
