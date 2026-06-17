# Google Perspective  (`n8n-nodes-base.googlePerspective`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: googlePerspectiveOAuth2Api
- operations: analyzeComment

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `operation` | Operation | options | analyzeComment |  |  |
| `text` | Text | string |  | true | op=analyzeComment |
| `requestedAttributesUi` | Attributes to Analyze | fixedCollection | flirtation | true | op=analyzeComment |
| `options` | Options | collection | {} |  | op=analyzeComment |
