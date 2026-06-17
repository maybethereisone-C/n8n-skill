# Workflow Retriever  (`@n8n/n8n-nodes-langchain.retrieverWorkflow`)

- typeVersion (max): **1.1**  | group: transform  | trigger: no
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `executeNotice` | The workflow will receive "query" as input and the output of the last node will be returned and converted to Documents | notice |  |  |  |
| `source` | Source | options | database |  |  |
| `workflowId` | Workflow ID | string |  | true |  |
| `workflowJson` | Workflow JSON | json | \n\n\n | true |  |
| `fields` | Workflow Values | fixedCollection | {} |  |  |
