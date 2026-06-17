# Databricks  (`n8n-nodes-base.databricks`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: databricksApi, databricksOAuth2Api
- resources: databricksSql, files, genie, modelServing, unityCatalog, vectorSearch
- operations: createCatalog, createDirectory, createFunction, createIndex, createMessage, createTable, createVolume, deleteCatalog, deleteDirectory, deleteFile, deleteFunction, deleteTable, deleteVolume, downloadFile, executeMessageQuery, executeQuery, getCatalog, getFileInfo, getFunction, getIndex, getMessage, getQueryResults, getSpace, getTable, getVolume, listCatalogs, listDirectory, listFunctions, listIndexes, listTables, listVolumes, queryEndpoint, queryIndex, startConversation, updateCatalog, uploadFile

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | accessToken |  |  |
| `resource` | Resource | options | databricksSql |  |  |
