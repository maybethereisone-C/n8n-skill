# Todoist  (`n8n-nodes-base.todoist`)

- typeVersion (max): **2.2**  | group: output  | trigger: no
- credentials: todoistApi, todoistOAuth2Api
- resources: comment, label, project, reminder, section, task
- operations: archive, close, create, delete, get, getAll, getCollaborators, move, quickAdd, reopen, sync, unarchive, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | apiKey |  |  |
| `resource` | Resource | options | task | true |  |
| `operation` | Operation | options | create | true | res=task |
| `taskId` | Task ID | string |  | true | res=task,op=delete,op=close,op=get,op=reopen,op=update |
| `project` | Project Name or ID | resourceLocator |  | true | res=task,op=create,op=move,op=sync |
| `section` | Section Name or ID | options |  |  | res=task,op=move |
| `labels` | Label Names or IDs | multiOptions | [] |  | res=task,op=create |
| `content` | Content | string |  | true | res=task,op=create |
| `commands` | Sync Commands | string | [] |  | res=task,op=sync |
| `options` | Additional Fields | collection | {} |  | res=task,op=create |
| `returnAll` | Return All | boolean | false |  | res=task,op=getAll |
| `limit` | Limit | number | 50 |  | res=task,op=getAll |
| `filters` | Filters | collection | {} |  | res=task,op=getAll |
| `updateFields` | Update Fields | collection | {} |  | res=task,op=update |
| `operation` | Operation | options | create | true | res=project |
| `operation` | Operation | options | create | true | res=section |
| `operation` | Operation | options | create | true | res=comment |
| `operation` | Operation | options | create | true | res=label |
| `operation` | Operation | options | create | true | res=reminder |
| `project` | Project Name or ID | resourceLocator |  | true | res=task,op=create,op=move |
| `options` | Additional Fields | collection | {} |  | res=task,op=move |
| `text` | Text | string |  | true | res=task,op=quickAdd |
| `options` | Additional Fields | collection | {} |  | res=task,op=quickAdd |
| `projectId` | Project ID | string |  | true | res=project,op=archive,op=delete,op=get,op=getCollaborators,op=unarchive |
| `name` | Name | string |  | true | res=project,op=create |
| `projectOptions` | Additional Fields | collection | {} |  | res=project,op=create |
| `projectUpdateFields` | Update Fields | collection | {} |  | res=project,op=update |
| `sectionId` | Section ID | string |  | true | res=section,op=delete,op=get,op=update |
| `sectionProject` | Project Name or ID | resourceLocator |  | true | res=section,op=create |
| `sectionName` | Name | string |  | true | res=section,op=create |
| `sectionOptions` | Additional Fields | collection | {} |  | res=section,op=create |
| `sectionUpdateFields` | Update Fields | collection | {} |  | res=section,op=update |
| `sectionFilters` | Filters | collection | {} |  | res=section,op=getAll |
| `commentId` | Comment ID | string |  | true | res=comment,op=delete,op=get,op=update |
| `commentTaskId` | Task ID | string |  | true | res=comment,op=create |
| `commentContent` | Content | string |  | true | res=comment,op=create |
| `commentUpdateFields` | Update Fields | collection | {} |  | res=comment,op=update |
| `commentFilters` | Filters | collection | {} |  | res=comment,op=getAll |
| `labelId` | Label ID | string |  | true | res=label,op=delete,op=get,op=update |
| `labelName` | Name | string |  | true | res=label,op=create |
| `labelOptions` | Additional Fields | collection | {} |  | res=label,op=create |
| `labelUpdateFields` | Update Fields | collection | {} |  | res=label,op=update |
| `reminderId` | Reminder ID | string |  | true | res=reminder,op=delete,op=update |
| `itemId` | Task ID | string |  | true | res=reminder,op=create |
| `dueDateType` | Due Date Type | options | natural_language | true | res=reminder,op=create |
| `natural_language_representation` | Natural Language Representation | string |  | true | res=reminder,op=create |
| `date` | Date | string |  | true | res=reminder,op=create |
| `datetime` | Date Time | dateTime |  | true | res=reminder,op=create |
| `timezone` | Timezone | string |  | true | res=reminder,op=create |
| `reminderOptions` | Additional Fields | collection | absolute |  | res=reminder,op=create |
| `reminderUpdateFields` | Update Fields | collection | {} |  | res=reminder,op=update |
