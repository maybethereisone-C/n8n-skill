# Home Assistant  (`n8n-nodes-base.homeAssistant`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: homeAssistantApi
- resources: cameraProxy, config, event, history, log, service, state, template
- operations: call, check, create, get, getAll, getErroLogs, getLogbookEntries, getScreenshot, upsert

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | config |  |  |
