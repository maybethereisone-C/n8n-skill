# Zulip  (`n8n-nodes-base.zulip`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: zulipApi
- resources: message, stream, user
- operations: create, deactivate, delete, get, getAll, getSubscribed, sendPrivate, sendStream, update, updateFile

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | message |  |  |
