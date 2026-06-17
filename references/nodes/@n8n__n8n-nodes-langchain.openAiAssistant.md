# OpenAI Assistant  (`@n8n/n8n-nodes-langchain.openAiAssistant`)

- typeVersion (max): **1.1**  | group: transform  | trigger: no
- credentials: openAiApi

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `mode` | Operation | options | existing |  |  |
| `name` | Name | string |  | true |  |
| `instructions` | Instructions | string |  |  |  |
| `model` | Model | options | gpt-3.5-turbo-1106 | true |  |
| `assistantId` | Assistant | options |  | true |  |
| `text` | Text | string | ={{ $json.chat_input }} | true |  |
| `nativeTools` | OpenAI Tools | multiOptions | [] |  |  |
| `noticeTools` | Connect your own custom tools to this node on the canvas | notice |  |  |  |
| `options` | Options | collection | https://api.openai.com/v1 |  |  |
