# Google Chat  (`n8n-nodes-base.googleChat`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: googleApi, googleChatOAuth2Api
- resources: attachment, incomingWebhook, media, member, message, space
- operations: create, delete, download, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | serviceAccount |  |  |
| `resource` | Resource | options | message | true |  |
