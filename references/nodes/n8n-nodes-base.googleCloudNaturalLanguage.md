# Google Cloud Natural Language  (`n8n-nodes-base.googleCloudNaturalLanguage`)

- typeVersion (max): **1**  | group: input,output  | trigger: no
- credentials: googleCloudNaturalLanguageOAuth2Api
- resources: document
- operations: analyzeSentiment

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | document |  |  |
| `operation` | Operation | options | analyzeSentiment |  | res=document |
| `source` | Source | options | content | true | op=analyzeSentiment |
| `content` | Content | string |  | true | op=analyzeSentiment |
| `gcsContentUri` | Google Cloud Storage URI | string |  | true | op=analyzeSentiment |
| `options` | Options | collection | PLAIN_TEXT |  | op=analyzeSentiment |
