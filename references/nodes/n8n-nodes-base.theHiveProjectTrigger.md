# TheHive 5 Trigger  (`n8n-nodes-base.theHiveProjectTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: theHiveProjectApi
- resources: alert, case, comment, log, observable, page, query, task
- operations: add, addAttachment, create, deleteAlert, deleteAttachment, deleteCase, deleteComment, deleteLog, deleteObservable, deletePage, deleteTask, executeAnalyzer, executeQuery, executeResponder, get, getAttachment, getTimeline, merge, promote, search, status, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `notice` | You must set up the webhook in TheHive — instructions <a href="https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.thehive5trigger/#configure-a-webhook-in-thehive" target="_blank">here</a> | notice |  |  |  |
| `events` | Events | multiOptions | [] | true |  |
| `filters` | Filters | fixedCollection | {} |  |  |
| `options` | Options | collection | {} |  |  |
| `resource` | Resource | options | alert | true |  |
