# OpenAI Chat Model  (`@n8n/n8n-nodes-langchain.lmChatOpenAi`)

- typeVersion (max): **1.3**  | group: transform  | trigger: no
- credentials: openAiApi

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `model` | Model | options | gpt-5-mini |  |  |
| `notice` | When using non-OpenAI models via "Base URL" override, not all models might be chat-compatible or support other features, like tools calling or JSON response format | notice |  |  |  |
| `responsesApiEnabled` | Use Responses API | boolean | true |  |  |
| `builtInTools` | Built-in Tools | collection | medium | true |  |
| `options` | Options | collection | https://api.openai.com/v1 |  |  |
