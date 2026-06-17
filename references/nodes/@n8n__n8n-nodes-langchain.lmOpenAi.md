# OpenAI Model  (`@n8n/n8n-nodes-langchain.lmOpenAi`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: openAiApi

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `deprecated` | This node is using OpenAI completions which are now deprecated. Please use the OpenAI Chat Model node instead. | notice |  |  |  |
| `model` | Model | resourceLocator |  | true |  |
| `notice` | When using non OpenAI models via Base URL override, not all models might be chat-compatible or support other features, like tools calling or JSON response format. | notice |  |  |  |
| `options` | Options | collection | https://api.openai.com/v1 |  |  |
