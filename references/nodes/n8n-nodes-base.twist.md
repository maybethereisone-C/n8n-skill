# Twist  (`n8n-nodes-base.twist`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: twistOAuth2Api
- resources: channel, comment, messageConversation, thread
- operations: archive, create, delete, get, getAll, unarchive, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | messageConversation |  |  |
