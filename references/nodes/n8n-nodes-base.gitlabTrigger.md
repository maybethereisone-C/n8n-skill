# GitLab Trigger  (`n8n-nodes-base.gitlabTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: gitlabApi, gitlabOAuth2Api
- resources: file, issue, release, repository, user
- operations: create, createComment, delete, edit, get, getAll, getIssues, getRepositories, list, lock, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | accessToken |  |  |
| `owner` | Repository Owner | string |  | true |  |
| `repository` | Repository Name | string |  | true |  |
| `events` | Events | multiOptions | [] | true |  |
| `resource` | Resource | options | issue |  |  |
| `operation` | Operation | options | create |  | res=issue |
| `operation` | Operation | options | getIssues |  | res=repository |
| `operation` | Operation | options | getRepositories |  | res=user |
| `operation` | Operation | options | create |  | res=release |
| `operation` | Operation | options | create |  | res=file |
| `repository` | Project Name | string |  | true | res=user,op=getRepositories |
| `title` | Title | string |  | true | res=issue,op=create |
| `body` | Body | string |  |  | res=issue,op=create |
| `due_date` | Due Date | dateTime |  |  | res=issue,op=create |
| `labels` | Labels | collection |  |  | res=issue,op=create |
| `assignee_ids` | Assignees | collection | 0 |  | res=issue,op=create |
| `issueNumber` | Issue Number | number | 0 | true | res=issue,op=createComment |
| `body` | Body | string |  |  | res=issue,op=createComment |
| `issueNumber` | Issue Number | number | 0 | true | res=issue,op=edit |
| `editFields` | Edit Fields | collection | {} |  | res=issue,op=edit |
| `issueNumber` | Issue Number | number | 0 | true | res=issue,op=get |
| `issueNumber` | Issue Number | number | 0 | true | res=issue,op=lock |
| `lockReason` | Lock Reason | options | resolved |  | res=issue,op=lock |
| `releaseTag` | Tag | string |  | true | res=release,op=create |
| `additionalFields` | Additional Fields | collection | {} |  | res=release,op=create |
| `projectId` | Project ID | string |  | true | res=release,op=delete,op=get |
| `tag_name` | Tag Name | string |  | true | res=release,op=delete,op=get |
| `projectId` | Project ID | string |  | true | res=release,op=getAll |
| `returnAll` | Return All | boolean | false |  | res=release,res=file,res=repository,op=getAll,op=list,op=getIssues |
| `limit` | Limit | number | 20 |  | res=release,res=file,res=repository,op=getAll,op=list,op=getIssues |
| `additionalFields` | Additional Fields | collection | released_at |  | res=release,op=getAll |
| `projectId` | Project ID | string |  | true | res=release,op=update |
| `tag_name` | Tag Name | string |  | true | res=release,op=update |
| `additionalFields` | Additional Fields | collection | {} |  | res=release,op=update |
| `getRepositoryIssuesFilters` | Filters | collection | {} |  | res=repository,op=getIssues |
| `filePath` | File Path | string |  |  | res=file,op=list |
| `page` | Page | number | 1 |  | res=file,op=list |
| `additionalParameters` | Additional Parameters | collection | {} |  | res=file,op=list |
| `asBinaryProperty` | As Binary Property | boolean | true |  | res=file,op=get |
| `binaryPropertyName` | Put Output File in Field | string | data | true | res=file,op=get |
| `additionalParameters` | Additional Parameters | collection | {} |  | res=file,op=get |
| `binaryData` | Binary File | boolean | false | true | res=file,op=create,op=edit |
| `fileContent` | File Content | string |  | true | res=file,op=create,op=edit |
| `binaryPropertyName` | Input Binary Field | string | data | true | res=file,op=create,op=edit |
| `commitMessage` | Commit Message | string |  | true | res=file,op=create,op=delete,op=edit |
| `branch` | Branch | string |  | true | res=file,op=create,op=delete,op=edit |
| `additionalParameters` | Additional Parameters | fixedCollection | {} |  | res=file,op=create,op=delete,op=edit |
