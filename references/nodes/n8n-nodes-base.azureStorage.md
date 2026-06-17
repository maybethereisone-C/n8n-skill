# Azure Storage  (`n8n-nodes-base.azureStorage`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: azureStorageOAuth2Api, azureStorageSharedKeyApi
- resources: blob, container
- operations: ={{ $value }}, ={{ $value.join(",") || undefined }}, Absolute, AppendBlob, Archive, BlockBlob, Cold, Cool, Hot, NeverExpire, PageBlob, binary, copy, create, delete, deleted, deletedwithversions, directories, files, get, getAll, immutabilitypolicy, legalhold, locked, metadata, permissions, snapshots, tags, uncommittedblobs, unlocked, url, versions

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | sharedKey |  |  |
| `resource` | Resource | options | container |  |  |
