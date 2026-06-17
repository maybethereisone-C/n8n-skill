# Webex by Cisco  (`n8n-nodes-base.ciscoWebex`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: ciscoWebexOAuth2Api
- resources: all, attachmentAction, meeting, meetingTranscript, membership, message, recording, room, telephonyCall
- operations: create, delete, download, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | message |  |  |
| `resolveData` | Resolve Data | boolean | true |  | res=attachmentAction |
| `filters` | Filters | collection | {} |  |  |
