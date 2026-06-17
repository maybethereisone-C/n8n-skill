# Supabase  (`n8n-nodes-base.supabase`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: supabaseApi
- resources: row
- operations: create, delete, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `useCustomSchema` | Use Custom Schema | boolean | false |  |  |
| `schema` | Schema | string | public |  |  |
| `resource` | Resource | options | row |  |  |
