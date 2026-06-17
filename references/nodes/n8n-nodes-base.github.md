# GitHub  (`n8n-nodes-base.github`)

- typeVersion (max): **1.1**  | group: input  | trigger: no
- credentials: githubApi, githubOAuth2Api
- resources: file, issue, organization, release, repository, review, user, workflow
- operations: create, createComment, delete, disable, dispatch, dispatchAndWait, edit, enable, get, getAll, getIssues, getLicense, getMembers, getProfile, getPullRequests, getRepositories, getUsage, getUserIssues, invite, list, listPopularPaths, listReferrers, lock, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | accessToken |  |  |
| `resource` | Resource | options | issue |  |  |
| `operation` | Operation | options | getRepositories |  | res=organization |
| `operation` | Operation | options | create |  | res=issue |
| `operation` | Operation | options | create |  | res=file |
| `operation` | Operation | options | getIssues |  | res=repository |
| `operation` | Operation | options | getRepositories |  | res=user |
| `operation` | Operation | options | create |  | res=release |
| `operation` | Operation | options | create |  | res=review |
| `operation` | Operation | options | dispatch |  | res=workflow |
| `webhookNotice` | Your execution will pause until a webhook is called. This URL will be generated at runtime and passed to your Github workflow as a resumeUrl input. | notice |  |  | res=workflow,op=dispatchAndWait |
| `owner` | Repository Owner | resourceLocator |  | true | op=invite,op=getUserIssues |
| `repository` | Repository Name | resourceLocator |  | true | res=user,res=organization,op=getRepositories |
| `workflowId` | Workflow | resourceLocator |  | true | res=workflow,op=disable,op=dispatch,op=dispatchAndWait,op=get,op=getUsage |
| `ref` | Ref | string | main | true | res=workflow,op=dispatch,op=dispatchAndWait |
| `inputs` | Inputs | json | {} |  | res=workflow,op=dispatch,op=dispatchAndWait |
| `filePath` | File Path | string |  | true | res=file,op=list |
| `binaryData` | Binary File | boolean | false | true | res=file,op=create,op=edit |
| `fileContent` | File Content | string |  | true | res=file,op=create,op=edit |
| `binaryPropertyName` | Input Binary Field | string | data | true | res=file,op=create,op=edit |
| `commitMessage` | Commit Message | string |  | true | res=file,op=create,op=delete,op=edit |
| `additionalParameters` | Additional Parameters | fixedCollection | {} |  | res=file,op=create,op=delete,op=edit |
| `asBinaryProperty` | As Binary Property | boolean | true |  | res=file,op=get |
| `binaryPropertyName` | Put Output File in Field | string | data | true | res=file,op=get |
| `additionalParameters` | Additional Parameters | collection | {} |  | res=file,op=get |
| `title` | Title | string |  | true | res=issue,op=create |
| `body` | Body | string |  |  | res=issue,op=create |
| `labels` | Labels | collection |  |  | res=issue,op=create |
| `assignees` | Assignees | collection |  |  | res=issue,op=create |
| `issueNumber` | Issue Number | number | 0 | true | res=issue,op=createComment |
| `body` | Body | string |  |  | res=issue,op=createComment |
| `issueNumber` | Issue Number | number | 0 | true | res=issue,op=edit |
| `editFields` | Edit Fields | collection | {} |  | res=issue,op=edit |
| `issueNumber` | Issue Number | number | 0 | true | res=issue,op=get |
| `issueNumber` | Issue Number | number | 0 | true | res=issue,op=lock |
| `lockReason` | Lock Reason | options | resolved |  | res=issue,op=lock |
| `releaseTag` | Tag | string |  | true | res=release,op=create |
| `additionalFields` | Additional Fields | collection | {} |  | res=release,op=create |
| `release_id` | Release ID | string |  | true | res=release,op=get,op=delete,op=update |
| `additionalFields` | Additional Fields | collection | {} |  | res=release,op=update |
| `returnAll` | Return All | boolean | false |  | res=release,op=getAll |
| `limit` | Limit | number | 50 |  | res=release,op=getAll |
| `returnAll` | Return All | boolean | false |  | res=repository,op=getIssues |
| `limit` | Limit | number | 50 |  | res=repository,op=getIssues |
| `getRepositoryIssuesFilters` | Filters | collection | {} |  | res=repository,op=getIssues |
| `returnAll` | Return All | boolean | false |  | res=repository,op=getPullRequests |
| `limit` | Limit | number | 50 |  | res=repository,op=getPullRequests |
| `getRepositoryPullRequestsFilters` | Filters | collection | open |  | res=repository,op=getPullRequests |
| `pullRequestNumber` | PR Number | number | 0 | true | res=review,op=get,op=update |
| `reviewId` | Review ID | string |  | true | res=review,op=get,op=update |
| `pullRequestNumber` | PR Number | number | 0 | true | res=review,op=getAll |
| `returnAll` | Return All | boolean | false |  | res=review,op=getAll |
| `limit` | Limit | number | 50 |  | res=review,op=getAll |
| `pullRequestNumber` | PR Number | number | 0 | true | res=review,op=create |
| `event` | Event | options | approve |  | res=review,op=create |
| `body` | Body | string |  |  | res=review,op=create |
| `additionalFields` | Additional Fields | collection | {} |  | res=review,op=create |
| `body` | Body | string |  |  | res=review,op=update |
| `returnAll` | Return All | boolean | false |  | res=user,op=getRepositories |
| `limit` | Limit | number | 50 |  | res=user,op=getRepositories |
| `organization` | Organization | string |  | true | res=user,op=invite |
| `email` | Email | string |  | true | res=user,op=invite |
| `returnAll` | Return All | boolean | false |  | res=organization,op=getRepositories |
| `limit` | Limit | number | 50 |  | res=organization,op=getRepositories |
| `returnAll` | Return All | boolean | false |  | res=organization,op=getMembers |
| `limit` | Limit | number | 50 |  | res=organization,op=getMembers |
| `returnAll` | Return All | boolean | false |  | op=getUserIssues |
| `limit` | Limit | number | 50 |  | op=getUserIssues |
| `getUserIssuesFilters` | Filters | collection | {} |  | op=getUserIssues |
| `notice` | Only members with owner privileges for an organization or admin privileges for a repository can set up the webhooks this node requires. | notice |  |  |  |
| `owner` | Repository Owner | resourceLocator |  | true |  |
| `repository` | Repository Name | resourceLocator |  | true |  |
| `events` | Events | multiOptions | [] | true |  |
| `options` | Options | collection | {} |  |  |
