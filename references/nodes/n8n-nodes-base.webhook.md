# Webhook  (`n8n-nodes-base.webhook`)

- typeVersion (max): **2.1**  | group: trigger  | trigger: no
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `multipleMethods` | Allow Multiple HTTP Methods | boolean | false |  |  |
| `httpMethod` | HTTP Methods | multiOptions |  |  |  |
| `path` | Path | string |  |  |  |
| `webhookNotice` | Insert a \ | notice |  |  |  |
| `webhookStreamingNotice` | Insert a node that supports streaming (e.g. \ | notice |  |  |  |
| `contentTypeNotice` | If you are sending back a response, add a "Content-Type" response header with the appropriate value to avoid unexpected behavior | notice |  |  |  |
