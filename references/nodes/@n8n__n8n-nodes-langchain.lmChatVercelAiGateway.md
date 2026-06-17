# Vercel AI Gateway Chat Model  (`@n8n/n8n-nodes-langchain.lmChatVercelAiGateway`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: vercelAiGatewayApi

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `notice` | If using JSON response format, you must include word "json" in the prompt in your chain or agent. Also, make sure to select latest models released post November 2023. | notice |  |  |  |
| `model` | Model | options | openai/gpt-4o |  |  |
| `options` | Options | collection | text |  |  |
