# AI Agent Tool  (`@n8n/n8n-nodes-langchain.agentTool`)

- typeVersion (max): **3.1**  | group: transform  | trigger: no
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `aiAgentStarterCallout` | Tip: Get a feel for agents with our quick <a href="https://docs.n8n.io/advanced-ai/intro-tutorial/" target="_blank">tutorial</a> or see an <a href="/templates/1954" target="_blank">example</a> of how this node works | callout |  |  |  |
| `deprecated` | This node is using Agent that has been deprecated. Please switch to using 'Tools Agent' instead. | notice |  |  |  |
| `notice` | For more reliable structured output parsing, consider using the Tools agent | notice |  |  |  |
| `hasOutputParser` | Require Specific Output Format | boolean | false |  |  |
| `needsFallback` | Enable Fallback Model | boolean | false |  |  |
| `fallbackNotice` | Connect an additional language model on the canvas to use it as a fallback if the main model fails | notice |  |  |  |
