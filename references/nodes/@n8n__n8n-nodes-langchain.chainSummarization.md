# Summarization Chain  (`@n8n/n8n-nodes-langchain.chainSummarization`)

- typeVersion (max): **2.1**  | group: transform  | trigger: no
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `type` | Type | options | map_reduce |  |  |
| `options` | Options | collection | {} |  |  |
| `operationMode` | Data to Summarize | options | nodeInputJson |  |  |
| `chunkingMode` | Chunking Strategy | options | simple |  |  |
| `chunkSize` | Characters Per Chunk | number | 1000 |  |  |
| `chunkOverlap` | Chunk Overlap (Characters) | number | 200 |  |  |
