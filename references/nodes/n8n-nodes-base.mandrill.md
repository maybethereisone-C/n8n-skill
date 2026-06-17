# Mandrill  (`n8n-nodes-base.mandrill`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: mandrillApi
- resources: message
- operations: sendHtml, sendTemplate

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | message |  |  |
| `operation` | Operation | options | sendTemplate |  | res=message |
| `template` | Template Name or ID | options |  | true | op=sendTemplate |
| `fromEmail` | From Email | string |  | true | op=sendHtml,op=sendTemplate |
| `toEmail` | To Email | string |  | true | op=sendHtml,op=sendTemplate |
| `jsonParameters` | JSON Parameters | boolean | false |  | op=sendHtml,op=sendTemplate |
| `options` | Options | collection | {} |  | op=sendHtml,op=sendTemplate |
| `mergeVarsJson` | Merge Vars | json |  |  |  |
| `mergeVarsUi` | Merge Vars | fixedCollection | {} |  |  |
| `metadataUi` | Metadata | fixedCollection | Name of the metadata key to add. |  |  |
| `metadataJson` | Metadata | json |  |  |  |
| `attachmentsJson` | Attachments | json |  |  |  |
| `attachmentsUi` | Attachments | fixedCollection | {} |  |  |
| `headersJson` | Headers | json |  |  |  |
| `headersUi` | Headers | fixedCollection | {} |  |  |
