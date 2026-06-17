# Message an n8n Agent  (`n8n-nodes-base.messageAnAgent`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `agentId` | Agent | resourceLocator |  | true |  |
| `message` | Message | string |  | true |  |
| `useStructuredOutput` | Require Specific Output Format | boolean | false |  |  |
| `outputSchema` | Output Schema | json |  |  |  |
| `structuredOutputNotice` | Structured output is enforced by the model provider. For best results across providers, mark every property as required. Some providers reject optional fields or advanced keywords (e.g. OpenAI and xAI), and a few do not support structured output at all (e.g. DeepSeek). | notice |  |  |  |
| `advanced` | Advanced | collection | {} |  |  |
