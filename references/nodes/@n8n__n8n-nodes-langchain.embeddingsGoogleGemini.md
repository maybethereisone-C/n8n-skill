# Embeddings Google Gemini  (`@n8n/n8n-nodes-langchain.embeddingsGoogleGemini`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: googlePalmApi

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `notice` | Each model is using different dimensional density for embeddings. Please make sure to use the same dimensionality for your vector store. The default model is using 768-dimensional embeddings. | notice |  |  |  |
| `modelName` | Model | options | models/gemini-embedding-001 |  |  |
