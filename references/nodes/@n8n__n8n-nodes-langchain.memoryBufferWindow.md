# Simple Memory  (`@n8n/n8n-nodes-langchain.memoryBufferWindow`)

- typeVersion (max): **1.4**  | group: transform  | trigger: no
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `scalingNotice` | This node stores memory locally in the n8n instance. It is not compatible with Queue Mode or Multi-Main setups, as memory will not be shared across workers. For production use with scaling, consider using an external memory store such as Redis, Postgres, or another persistent memory node. | notice |  |  |  |
| `sessionKey` | Session Key | string | chat_history |  |  |
