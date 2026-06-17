# Microsoft OneDrive Trigger  (`n8n-nodes-base.microsoftOneDriveTrigger`)

- typeVersion (max): **1.1**  | group: trigger  | trigger: yes
- credentials: microsoftOAuth2Api, microsoftOneDriveOAuth2Api
- resources: file, folder
- operations: copy, create, delete, download, get, getChildren, rename, search, share, upload

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | microsoftOneDriveOAuth2Api |  |  |
| `resource` | Resource | options | file |  |  |
