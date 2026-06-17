# Discord  (`n8n-nodes-base.discord`)

- typeVersion (max): **2**  | group: output  | trigger: no
- credentials: discordBotApi, discordOAuth2Api, discordWebhookApi
- resources: channel, member, message
- operations: create, deleteChannel, deleteMessage, get, getAll, react, roleAdd, roleRemove, send, sendLegacy, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `webhookUri` | Webhook URL | string |  | true |  |
| `text` | Content | string |  |  |  |
| `options` | Additional Fields | collection | {} |  |  |
| `authentication` | Connection Type | options | botToken |  |  |
| `resource` | Resource | options | channel |  |  |
