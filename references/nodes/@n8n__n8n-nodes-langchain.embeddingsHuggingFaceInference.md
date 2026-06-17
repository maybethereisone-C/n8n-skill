# Embeddings Hugging Face Inference  (`@n8n/n8n-nodes-langchain.embeddingsHuggingFaceInference`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: huggingFaceApi

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `notice` | Each model is using different dimensional density for embeddings. Please make sure to use the same dimensionality for your vector store. The default model is using 768-dimensional embeddings. | notice |  |  |  |
| `modelName` | Model Name | string | sentence-transformers/distilbert-base-nli-mean-tokens |  |  |
| `options` | Options | collection | {} |  |  |
