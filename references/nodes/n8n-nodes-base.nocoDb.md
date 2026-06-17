# NocoDB  (`n8n-nodes-base.nocoDb`)

- typeVersion (max): **4**  | group: input  | trigger: no
- credentials: —
- resources: base, linkrow, row
- operations: count, create, delete, get, getAll, link, list, search, unlink, update, upload, upsert

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | nocoDb |  |  |
| `version` | API Version | options | 1 |  |  |
| `resource` | Resource | options | row |  |  |
| `operation` | Operation | options | get |  | res=row |
