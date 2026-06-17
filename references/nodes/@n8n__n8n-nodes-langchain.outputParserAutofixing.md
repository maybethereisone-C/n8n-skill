# Auto-fixing Output Parser  (`@n8n/n8n-nodes-langchain.outputParserAutofixing`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `info` | This node wraps another output parser. If the first one fails it calls an LLM to fix the format | notice |  |  |  |
| `options` | Options | collection | {} |  |  |
