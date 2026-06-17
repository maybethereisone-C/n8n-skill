# In Memory Vector Store Insert  (`@n8n/n8n-nodes-langchain.vectorStoreInMemoryInsert`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `notice` | The embbded data are stored in the server memory, so they will be lost when the server is restarted. Additionally, if the amount of data is too large, it may cause the server to crash due to insufficient memory. | notice |  |  |  |
| `clearStore` | Clear Store | boolean | false |  |  |
| `memoryKey` | Memory Key | string | vector_store_key |  |  |
