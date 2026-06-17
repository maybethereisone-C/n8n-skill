# Asana  (`n8n-nodes-base.asana`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: asanaApi, asanaOAuth2Api
- resources: project, subtask, task, taskComment, taskProject, taskTag, user
- operations: add, create, delete, get, getAll, move, remove, search, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | accessToken |  |  |
| `resource` | Resource | options | task |  |  |
| `operation` | Operation | options | create |  | res=subtask |
| `taskId` | Parent Task ID | string |  | true | res=subtask,op=create |
| `name` | Name | string |  | true | res=subtask,op=create |
| `otherProperties` | Additional Fields | collection | {} |  | res=subtask,op=create |
| `taskId` | Parent Task ID | string |  | true | res=subtask,op=getAll |
| `returnAll` | Return All | boolean | false |  | res=subtask,op=getAll |
| `limit` | Limit | number | 100 |  | res=subtask,op=getAll |
| `options` | Options | collection | {} |  | res=subtask,op=getAll |
| `operation` | Operation | options | create |  | res=task |
| `workspace` | Workspace Name or ID | options |  | true | res=task,op=create |
| `name` | Name | string |  | true | res=task,op=create |
| `id` | Task ID | string |  | true | res=task,op=delete |
| `id` | Task ID | string |  | true | res=task,op=get |
| `returnAll` | Return All | boolean | false |  | res=task,op=getAll |
| `limit` | Limit | number | 100 |  | res=task,op=getAll |
| `filters` | Filters | collection | {} |  | res=task,op=getAll |
| `id` | Task ID | string |  | true | res=task,op=move |
| `projectId` | Project Name or ID | options |  | true | res=task,op=move |
| `section` | Section Name or ID | options |  | true | res=task,op=move |
| `id` | Task ID | string |  | true | res=task,op=update |
| `workspace` | Workspace Name or ID | options |  | true | res=task,op=search |
| `searchTaskProperties` | Filters | collection | {} |  | res=task,op=search |
| `otherProperties` | Additional Fields | collection | {} |  | res=task,op=create,op=update |
| `operation` | Operation | options | add |  | res=taskComment |
| `id` | Task ID | string |  | true | res=taskComment,op=add |
| `isTextHtml` | Is Text HTML | boolean | false |  | res=taskComment,op=add |
| `text` | Text | string |  | true | res=taskComment,op=add |
| `additionalFields` | Additional Fields | collection | {} |  | res=taskComment,op=add |
| `id` | Comment ID | string |  | true | res=taskComment,op=remove |
| `operation` | Operation | options | add |  | res=taskProject |
| `id` | Task ID | string |  | true | res=taskProject,op=add |
| `project` | Project Name or ID | options |  | true | res=taskProject,op=add |
| `additionalFields` | Additional Fields | collection | {} |  | res=taskProject,op=add |
| `id` | Task ID | string |  | true | res=taskProject,op=remove |
| `project` | Project Name or ID | options |  | true | res=taskProject,op=remove |
| `operation` | Operation | options | add |  | res=taskTag |
| `id` | Task ID | string |  | true | res=taskTag,op=add |
| `tag` | Tags Name or ID | options |  | true | res=taskTag,op=add |
| `id` | Task ID | string |  | true | res=taskTag,op=remove |
| `tag` | Tags Name or ID | options |  | true | res=taskTag,op=remove |
| `operation` | Operation | options | get |  | res=user |
| `userId` | User ID | string |  | true | res=user,op=get |
| `workspace` | Workspace Name or ID | options |  | true | res=user,op=getAll |
| `operation` | Operation | options | get |  | res=project |
| `name` | Name | string |  | true | res=project,op=create |
| `workspace` | Workspace Name or ID | options |  | true | res=project,op=create |
| `team` | Team Name or ID | options |  |  | res=project,op=create |
| `additionalFields` | Additional Fields | collection | none |  | res=project,op=create |
| `id` | Project ID | string |  | true | res=project,op=delete |
| `id` | Project ID | string |  | true | res=project,op=get |
| `workspace` | Workspace Name or ID | options |  | true | res=project,op=getAll |
| `returnAll` | Return All | boolean | false |  | res=project,op=getAll |
| `limit` | Limit | number | 100 |  | res=project,op=getAll |
| `additionalFields` | Additional Fields | collection | {} |  | res=project,op=getAll |
| `workspace` | Workspace Name or ID | options |  | true | res=project,op=update |
| `id` | Project ID | string |  | true | res=project,op=update |
| `updateFields` | Update Fields | collection | none |  | res=project,op=update |
| `workspace` | Workspace Name or ID | options |  |  |  |
