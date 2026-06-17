# Call n8n Workflow Tool — `@n8n/n8n-nodes-langchain.toolWorkflow`

**Type** `@n8n/n8n-nodes-langchain.toolWorkflow` · **typeVersion** 2 · **ai**

**What:** AI tool sub-node that lets an agent invoke another n8n workflow and receive its output as tool results.

**Credentials:** None (uses internal n8n workflow execution).

**Resources / Operations:**

| Parameter | Options |
|-----------|---------|
| Source | Database (by list or ID) / Define Below (inline JSON) |
| Workflow Inputs | Fixed values, expressions, or `$fromAI()` for AI-driven input |

**Key params & gotchas:**
- **Description** field is critical — it tells the agent *when* to call this tool. Write it as an imperative: `"Call this tool to look up customer orders. Input: customer email as a string."`.
- When using **Database** source, click **Refresh** after selecting the sub-workflow to pull in its declared input schema.
- `$fromAI()` lets you mix AI-generated values with static values in a single field — select the AI button on a field to auto-populate the expression, then customize.
- Sub-workflow must start with a **Workflow Input Trigger** node configured with the expected schema.
- Sub-node — connect to AI Agent's Tools input.

**Minimal example:**
```
Description: "Call to get weather for a city. Input: city name."
Source: Database → select "GetWeather" workflow
Workflow Inputs: city = $fromAI("city", "The city name")
```

**Source:** n8n-nodes-langchain.toolworkflow.md  [doc-verified]
