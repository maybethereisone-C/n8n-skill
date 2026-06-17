# OpenRouter Chat Model  (`@n8n/n8n-nodes-langchain.lmChatOpenRouter`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: openRouterApi

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `notice` | If using JSON response format, you must include word "json" in the prompt in your chain or agent. Also, make sure to select latest models released post November 2023. | notice |  |  |  |
| `model` | Model | options | openai/gpt-4.1-mini |  |  |
| `options` | Options | collection | text |  |  |
