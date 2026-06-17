# S3  (`n8n-nodes-base.s3`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: —
- resources: bucket, file, folder

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `s3StandardNotice` | This node is for services that use the S3 standard, e.g. Minio or Digital Ocean Spaces. For AWS S3 use the 'AWS S3' node. | notice |  |  |  |
| `resource` | Resource | options | file |  |  |
