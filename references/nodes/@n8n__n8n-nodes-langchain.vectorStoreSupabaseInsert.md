# Supabase: Insert  (`@n8n/n8n-nodes-langchain.vectorStoreSupabaseInsert`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: supabaseApi

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `setupNotice` | Please refer to the <a href="https://supabase.com/docs/guides/ai/langchain" target="_blank">Supabase documentation</a> for more information on how to setup your database as a Vector Store. | notice |  |  |  |
| `queryName` | Query Name | string | match_documents | true |  |
| `notice` | Specify the document to load in the document loader sub-node | notice |  |  |  |
