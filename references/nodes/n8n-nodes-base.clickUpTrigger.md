# ClickUp Trigger  (`n8n-nodes-base.clickUpTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: clickUpApi, clickUpOAuth2Api
- resources: checklist, checklistItem, comment, folder, goal, goalKeyResult, guest, list, spaceTag, task, taskDependency, taskList, taskTag, timeEntry, timeEntryTag
- operations: add, create, customFields, delete, get, getAll, member, remove, setCustomField, start, stop, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | accessToken |  |  |
| `team` | Team Name or ID | options |  | true |  |
| `events` | Events | multiOptions | [] | true |  |
| `filters` | Filters | collection | {} |  |  |
| `resource` | Resource | options | task |  |  |
