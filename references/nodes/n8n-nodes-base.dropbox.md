# Dropbox  (`n8n-nodes-base.dropbox`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: dropboxApi, dropboxOAuth2Api
- resources: file, folder, search
- operations: copy, create, delete, download, list, move, query, upload

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | accessToken |  |  |
| `resource` | Resource | options | file |  |  |
| `operation` | Operation | options | upload |  | res=file |
| `operation` | Operation | options | create |  | res=folder |
| `operation` | Operation | options | query |  | res=search |
| `path` | From Path | string |  | true | res=file,res=folder,op=copy |
| `toPath` | To Path | string |  | true | res=file,res=folder,op=copy |
| `path` | Delete Path | string |  | true | res=file,res=folder,op=delete |
| `path` | From Path | string |  | true | res=file,res=folder,op=move |
| `toPath` | To Path | string |  | true | res=file,res=folder,op=move |
| `path` | File Path | string |  | true | res=file,op=download |
| `binaryPropertyName` | Put Output File in Field | string | data | true | res=file,op=download |
| `path` | File Path | string |  | true | res=file,op=upload |
| `binaryData` | Binary File | boolean | false |  | res=file,op=upload |
| `fileContent` | File Content | string |  |  | res=file,op=upload |
| `binaryPropertyName` | Input Binary Field | string | data | true | res=file,op=upload |
| `query` | Query | string |  | true | res=search,op=query |
| `fileStatus` | File Status | options | active |  | res=search,op=query |
| `returnAll` | Return All | boolean | false |  | res=search,op=query |
| `limit` | Limit | number | 100 |  | res=search,op=query |
| `simple` | Simplify | boolean | true |  | res=search,op=query |
| `filters` | Filters | collection | {} |  | res=search,op=query |
| `path` | Folder | string |  | true | res=folder,op=create |
| `path` | Folder Path | string |  |  | res=folder,op=list |
| `returnAll` | Return All | boolean | false |  | res=folder,op=list |
| `limit` | Limit | number | 100 |  | res=folder,op=list |
| `filters` | Filters | collection | {} |  | res=folder,op=list |
