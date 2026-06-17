# TheHive  (`n8n-nodes-base.theHive`)

- typeVersion (max): **2**  | group: transform  | trigger: no
- credentials: theHiveApi
- resources: alert, case, log, observable, task
- operations: Cancel, Completed, InProgress, Waiting, create, executeResponder, get, getAll

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | alert | true |  |
| `notice` | You must set up the webhook in TheHive — instructions <a href="https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.thehivetrigger/#configure-a-webhook-in-thehive" target="_blank">here</a> | notice |  |  |  |
