# Google Translate  (`n8n-nodes-base.googleTranslate`)

- typeVersion (max): **2**  | group: input,output  | trigger: no
- credentials: googleApi, googleTranslateOAuth2Api
- resources: language
- operations: translate

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | serviceAccount |  |  |
| `resource` | Resource | options | language |  |  |
| `operation` | Operation | options | translate |  | res=language |
| `text` | Text | string |  | true | op=translate |
| `translateTo` | Translate To | options |  | true | op=translate |
