# Nextcloud  (`n8n-nodes-base.nextCloud`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: nextCloudApi, nextCloudOAuth2Api
- resources: file, folder, user
- operations: copy, create, delete, download, get, getAll, list, move, share, update, upload

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | accessToken |  |  |
| `resource` | Resource | options | file |  |  |
| `operation` | Operation | options | upload |  | res=file |
| `operation` | Operation | options | create |  | res=folder |
| `operation` | Operation | options | create |  | res=user |
| `path` | From Path | string |  | true | res=file,res=folder,op=copy |
| `toPath` | To Path | string |  | true | res=file,res=folder,op=copy |
| `path` | Delete Path | string |  | true | res=file,res=folder,op=delete |
| `path` | From Path | string |  | true | res=file,res=folder,op=move |
| `toPath` | To Path | string |  | true | res=file,res=folder,op=move |
| `path` | File Path | string |  | true | res=file,op=download |
| `binaryPropertyName` | Put Output File in Field | string | data | true | res=file,op=download |
| `path` | File Path | string |  | true | res=file,op=upload |
| `binaryDataUpload` | Binary File | boolean | false | true | res=file,op=upload |
| `fileContent` | File Content | string |  |  | res=file,op=upload |
| `binaryPropertyName` | Input Binary Field | string | data | true | res=file,op=upload |
| `path` | File Path | string |  | true | res=file,res=folder,op=share |
| `shareType` | Share Type | options | 0 |  | res=file,res=folder,op=share |
| `circleId` | Circle ID | string |  |  | res=file,res=folder,op=share |
| `email` | Email | string |  |  | res=file,res=folder,op=share |
| `groupId` | Group ID | string |  |  | res=file,res=folder,op=share |
| `user` | User | string |  |  | res=file,res=folder,op=share |
| `options` | Options | collection | {} |  | res=file,res=folder,op=share |
| `path` | Folder | string |  | true | res=folder,op=create |
| `path` | Folder Path | string |  |  | res=folder,op=list |
| `userId` | Username | string |  | true | res=user,op=create |
| `email` | Email | string |  | true | res=user,op=create |
| `additionalFields` | Additional Fields | collection | {} |  | res=user,op=create |
| `userId` | Username | string |  | true | res=user,op=delete,op=get,op=update |
| `returnAll` | Return All | boolean | false |  | res=user,op=getAll |
| `limit` | Limit | number | 50 |  | res=user,op=getAll |
| `options` | Options | collection | {} |  | res=user,op=getAll |
| `updateFields` | Update Fields | fixedCollection | email |  | res=user,op=update |
