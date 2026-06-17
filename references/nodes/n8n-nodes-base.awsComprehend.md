# AWS Comprehend  (`n8n-nodes-base.awsComprehend`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: —
- resources: text
- operations: detectDominantLanguage, detectEntities, detectSentiment

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | text |  |  |
| `operation` | Operation | options | detectDominantLanguage |  |  |
| `languageCode` | Language Code | options | en |  | res=text,op=detectSentiment,op=detectEntities |
| `text` | Text | string |  |  | res=text |
| `simple` | Simplify | boolean | true |  | res=text,op=detectDominantLanguage |
| `additionalFields` | Additional Fields | collection | {} |  | res=text,op=detectEntities |
