# Google Cloud Storage  (`n8n-nodes-base.googleCloudStorage`)

- typeVersion (max): **1.1**  | group: transform  | trigger: no
- credentials: googleApi, googleCloudStorageOAuth2Api
- resources: bucket, object
- operations: AES256, authenticatedRead, bucketOwnerFullControl, bucketOwnerRead, create, delete, full, get, getAll, json, media, noAcl, private, projectPrivate, publicRead, publicReadWrite, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | oAuth2 |  |  |
| `resource` | Resource | options | bucket |  |  |
