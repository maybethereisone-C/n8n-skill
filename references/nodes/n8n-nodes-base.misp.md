# MISP  (`n8n-nodes-base.misp`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: mispApi
- resources: attribute, event, eventTag, feed, galaxy, noticelist, object, organisation, tag, user, warninglist
- operations: add, create, delete, disable, enable, get, getAll, publish, remove, search, unpublish, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | attribute |  |  |
