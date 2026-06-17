# Embeddings Google Vertex  (`@n8n/n8n-nodes-langchain.embeddingsGoogleVertex`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: googleApi

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `notice` | Each model is using different dimensional density for embeddings. Please make sure to use the same dimensionality for your vector store. The default model is using 768-dimensional embeddings. You can find available models <a href="https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/text-embeddings-api">here</a>. | notice |  |  |  |
| `projectId` | Project ID | resourceLocator |  | true |  |
| `modelName` | Model Name | string | text-embedding-005 |  |  |
