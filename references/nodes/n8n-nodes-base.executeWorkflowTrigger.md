# Execute Workflow Trigger  (`n8n-nodes-base.executeWorkflowTrigger`)

- typeVersion (max): **1.2**  | group: trigger  | trigger: yes
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `events` | Events | hidden | worklfow_call |  |  |
| `notice` | When an ‘execute workflow’ node calls this workflow, the execution starts here. Any data passed into the 'execute workflow' node will be output by this node. | notice |  |  |  |
| `outdatedVersionWarning` | This node is out of date. Please upgrade by removing it and adding a new one | notice |  |  |  |
| `Define using fields below` | Input data mode | options |  |  |  |
| `name` | Workflow Input Schema | fixedCollection | {} | true |  |
| `returnOutput` | Items to Return | options | lastRunOnly |  |  |
