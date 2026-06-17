# Chat Memory Manager  (`@n8n/n8n-nodes-langchain.memoryManager`)

- typeVersion (max): **1.1**  | group: transform  | trigger: no
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `mode` | Operation Mode | options | load |  |  |
| `insertMode` | Insert Mode | options | insert |  |  |
| `deleteMode` | Delete Mode | options | lastN |  |  |
| `messages` | Chat Messages | fixedCollection | system | true |  |
| `lastMessagesCount` | Messages Count | number | 2 |  |  |
| `simplifyOutput` | Simplify Output | boolean | true |  |  |
| `options` | Options | collection | {} |  |  |
