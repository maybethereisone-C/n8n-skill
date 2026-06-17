# Execute Sub-workflow Trigger — `n8n-nodes-base.executeWorkflowTrigger`
**Type** `n8n-nodes-base.executeWorkflowTrigger` · **typeVersion** 1 · **trigger**

**What:** Starts a workflow when called by an Execute Sub-workflow node or Call n8n Workflow Tool node — enables sub-workflow reuse and workflow decomposition.

**Credentials:** none.

**Resources / Operations:**
| Trigger type | What fires it |
|---|---|
| Internal call | Another workflow's Execute Sub-workflow node or `@n8n/n8n-nodes-langchain.toolWorkflow` node explicitly calls this workflow |

**Key params & gotchas:**
- Must be the **first (and only trigger) node** in the sub-workflow.
- Data passed from the calling workflow arrives as input items — the trigger emits those items directly downstream.
- In the calling workflow, the Execute Sub-workflow node must reference this workflow's ID or name.
- Sub-workflows run synchronously — the parent waits for the child to finish unless "Wait for Sub-Workflow" is disabled.
- If the sub-workflow errors, the error propagates back to the parent workflow.

**Minimal example:**
```
Parent workflow → [Execute Sub-workflow node: workflowId=42] → ...
Sub-workflow 42 → [Execute Sub-workflow Trigger] → [process items] → ...
```

**Source:** n8n-nodes-base.executeworkflowtrigger.md  [doc-verified]
