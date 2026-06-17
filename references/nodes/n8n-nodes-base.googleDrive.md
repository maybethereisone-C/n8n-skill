# Google Drive  (`n8n-nodes-base.googleDrive`)

- typeVersion (max): **3**  | group: input  | trigger: no
- credentials: googleApi, googleDriveOAuth2Api
- resources: drive, file, fileFolder, folder
- operations: contains, copy, create, createFromText, delete, deleteDrive, deleteFile, deleteFolder, download, get, is, isNot, list, move, search, share, update, upload

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Credential Type | options | oAuth2 |  |  |
| `triggerOn` | Trigger On | options |  | true |  |
| `fileToWatch` | File | resourceLocator |  | true |  |
| `event` | Watch For | options | fileUpdated | true |  |
| `folderToWatch` | Folder | resourceLocator |  | true |  |
| `asas` | Changes within subfolders won't trigger this node | notice |  |  |  |
| `driveToWatch` | Drive To Watch | options | root | true |  |
| `options` | Options | collection | all |  |  |
| `resource` | Resource | options | file |  |  |
| `operation` | Operation | options | upload |  | res=file |
| `operation` | Operation | options | create |  | res=folder |
| `fileId` | File | resourceLocator |  | true | res=file,op=download,op=copy,op=update,op=delete,op=share |
| `fileId` | Folder | resourceLocator |  | true | res=folder,op=delete,op=share |
| `binaryPropertyName` | Put Output File in Field | string | data | true | res=file,op=download |
| `options` | Options | collection | application/vnd.openxmlformats-officedocument.wordprocessingml.document |  | res=file,op=download |
| `useQueryString` | Use Query String | boolean | false |  | res=file,op=list |
| `queryString` | Query String | string |  |  | res=file,op=list |
| `limit` | Limit | number | 50 |  | res=file,op=list |
| `queryFilters` | Filters | fixedCollection | contains |  | res=file,op=list |
| `permissionsUi` | Permissions | fixedCollection | {} |  | res=file,res=folder,op=share |
| `binaryData` | Binary File | boolean | false |  | res=file,op=upload |
| `fileContent` | File Content | string |  |  | res=file,op=upload |
| `binaryPropertyName` | Input Binary Field | string | data | true | res=file,op=upload |
| `updateFields` | Update Fields | collection | {} |  | res=file,op=update |
| `options` | Options | collection | {} |  | res=file,op=update |
| `name` | File Name | string |  | true | res=file,op=upload |
| `resolveData` | Resolve Data | boolean | false |  | res=file,op=upload |
| `parents` | Parents | string | [] |  | res=file,op=upload |
| `name` | Folder | string |  | true | res=folder,op=create |
| `operation` | Operation | options | create |  | res=drive |
| `driveId` | Drive | resourceLocator |  | true | res=drive,op=delete,op=get,op=update |
| `name` | Name | string |  |  | res=drive,op=create |
| `options` | Options | collection | {} |  | res=drive,op=create |
| `options` | Options | collection | {} |  | res=drive,op=get |
| `returnAll` | Return All | boolean | false |  | res=drive,op=list |
| `limit` | Limit | number | 100 |  | res=drive,op=list |
| `options` | Options | collection | {} |  | res=drive,op=list |
| `options` | Update Fields | collection | {} |  | res=drive,op=update |
| `options` | Options | collection | {} |  | res=file,op=upload |
