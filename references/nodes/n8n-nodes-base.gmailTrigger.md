# Gmail Trigger  (`n8n-nodes-base.gmailTrigger`)

- typeVersion (max): **2.2**  | group: trigger  | trigger: yes
- credentials: googleApi
- resources: draft, label, message, messageLabel, thread
- operations: add, addLabels, create, delete, get, getAll, markAsRead, markAsUnread, remove, removeLabels, reply, send, trash, untrash

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | oAuth2 |  |  |
| `event` | Event | options | messageReceived |  |  |
| `simple` | Simplify | boolean | true |  |  |
| `maxResults` | Max Emails per Poll | number | 10 |  |  |
| `filters` | Filters | collection | {} |  |  |
| `options` | Options | collection | attachment_ |  |  |
| `resource` | Resource | options | draft |  |  |
| `sendTo` | To | string |  | true |  |
