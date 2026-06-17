# AWS Transcribe  (`n8n-nodes-base.awsTranscribe`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: —
- resources: transcriptionJob
- operations: create, delete, get, getAll

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | transcriptionJob |  |  |
| `operation` | Operation | options | create |  |  |
| `transcriptionJobName` | Job Name | string |  |  | res=transcriptionJob,op=create,op=get,op=delete |
| `mediaFileUri` | Media File URI | string |  |  | res=transcriptionJob,op=create |
| `detectLanguage` | Detect Language | boolean | false |  | res=transcriptionJob,op=create |
| `languageCode` | Language | options | en-US |  | res=transcriptionJob,op=create |
| `options` | Options | collection | {} |  | op=create |
| `returnTranscript` | Return Transcript | boolean | true |  | res=transcriptionJob,op=get |
| `simple` | Simplify | boolean | true |  | res=transcriptionJob,op=get |
| `returnAll` | Return All | boolean | false |  | res=transcriptionJob,op=getAll |
| `limit` | Limit | number | 20 |  | res=transcriptionJob,op=getAll |
| `filters` | Filters | collection | {} |  | res=transcriptionJob,op=getAll |
