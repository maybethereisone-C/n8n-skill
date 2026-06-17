# Execute Sub-workflow  (`n8n-nodes-base.executeWorkflow`)

- typeVersion (max): **1.3**  | group: transform  | trigger: no
- credentials: —
- operations: call_workflow

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `operation` | Operation | hidden | call_workflow |  |  |
| `outdatedVersionWarning` | This node is out of date. Please upgrade by removing it and adding a new one | notice |  |  |  |
| `source` | Source | options | database |  |  |
| `workflowId` | Workflow ID | string |  | true |  |
| `workflowPath` | Workflow Path | string |  | true |  |
| `workflowJson` | Workflow JSON | json | \n\n\n | true |  |
| `workflowUrl` | Workflow URL | string |  | true |  |
| `executeWorkflowNotice` | Any data you pass into this node will be output by the Execute Workflow Trigger. <a href="https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow/" target="_blank">More info</a> | notice |  |  |  |
| `workflowInputs` | Workflow Inputs | resourceMapper |  | true |  |
| `mode` | Mode | options | once |  |  |
| `options` | Options | collection | {} |  |  |
