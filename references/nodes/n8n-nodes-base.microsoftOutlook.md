# Microsoft Outlook  (`n8n-nodes-base.microsoftOutlook`)

- typeVersion (max): **2**  | group: transform  | trigger: no
- credentials: microsoftOutlookOAuth2Api
- resources: calendar, contact, draft, event, folder, folderMessage, message, messageAttachment
- operations: add, create, delete, download, get, getAll, getChildren, getMime, move, reply, send, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `event` | Trigger On | options | messageReceived |  |  |
| `resource` | Resource | options | message |  |  |
