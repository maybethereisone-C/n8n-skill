# Trello Trigger  (`n8n-nodes-base.trelloTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: trelloApi, trelloOAuth1Api
- resources: attachment, board, boardMember, card, cardComment, checklist, label, list
- operations: add, addLabel, archive, completedCheckItems, create, createCheckItem, delete, deleteCheckItem, get, getAll, getCards, getCheckItem, invite, remove, removeLabel, update, updateCheckItem

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | apiKey |  |  |
| `id` | Model ID | string |  | true |  |
| `resource` | Resource | options | card |  |  |
