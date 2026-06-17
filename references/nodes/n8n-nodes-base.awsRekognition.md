# AWS Rekognition  (`n8n-nodes-base.awsRekognition`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: —
- resources: image
- operations: analyze

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | image |  |  |
| `operation` | Operation | options | analyze |  |  |
| `type` | Type | options | detectFaces |  | res=image,op=analyze |
| `binaryData` | Binary File | boolean | false | true | res=image,op=analyze |
| `binaryPropertyName` | Input Binary Field | string | data | true | res=image,op=analyze |
| `bucket` | Bucket | string |  | true | res=image,op=analyze |
| `name` | Name | string |  | true | res=image,op=analyze |
| `additionalFields` | Additional Fields | collection | {} |  | res=image,op=analyze |
