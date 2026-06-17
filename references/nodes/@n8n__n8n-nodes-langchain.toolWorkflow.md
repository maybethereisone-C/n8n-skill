# Call n8n Sub-Workflow Tool  (`@n8n/n8n-nodes-langchain.toolWorkflow`)

- typeVersion (max): **2.2**  | group: transform  | trigger: no
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `noticeTemplateExample` | See an example of a workflow to suggest meeting slots using AI <a href="/templates/1953" target="_blank">here</a>. | notice |  |  |  |
| `name` | Name | string |  |  |  |
| `description` | Description | string |  |  |  |
| `executeNotice` | This tool will call the workflow you define below, and look in the last node for the response. The workflow needs to start with an Execute Workflow trigger | notice |  |  |  |
| `source` | Source | options | database |  |  |
| `workflowId` | Workflow ID | string |  | true |  |
| `workflowJson` | Workflow JSON | json | \n\n\n\n\n\n\n\n\n | true |  |
| `responsePropertyName` | Field to Return | string | response | true |  |
| `fields` | Extra Workflow Inputs | fixedCollection | {} |  |  |
| `specifyInputSchema` | Specify Input Schema | boolean | false |  |  |
| `workflowInputs` | Workflow Inputs | resourceMapper |  | true |  |
