# Respond to Webhook  (`n8n-nodes-base.respondToWebhook`)

- typeVersion (max): **1.5**  | group: transform  | trigger: no
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `enableResponseOutput` | Enable Response Output Branch | boolean | false |  |  |
| `generalNotice` | Verify that the "Webhook" node\ | notice |  |  |  |
| `credentials` | Credentials | credentials |  |  |  |
| `webhookNotice` | When using expressions, note that this node will only run for the first item in the input data | notice |  |  |  |
| `redirectURL` | Redirect URL | string |  | true |  |
| `responseBody` | Response Body | json | {\n  "myField": "value"\n} |  |  |
| `payload` | Payload | json | {\n  "myField": "value"\n} |  |  |
| `responseDataSource` | Response Data Source | options | automatically |  |  |
| `inputFieldName` | Input Field Name | string | data | true |  |
| `contentTypeNotice` | To avoid unexpected behavior, add a "Content-Type" response header with the appropriate value | notice |  |  |  |
| `options` | Options | collection | {} |  |  |
