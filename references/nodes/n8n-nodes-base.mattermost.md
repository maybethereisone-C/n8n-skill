# Mattermost  (`n8n-nodes-base.mattermost`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: mattermostApi
- resources: channel, message, reaction, user
- operations: addUser, create, deactive, delete, getAll, getByEmail, getById, invite, members, post, postEphemeral, restore, search, statistics

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | message |  |  |
