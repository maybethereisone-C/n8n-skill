# Webex by Cisco Trigger  (`n8n-nodes-base.ciscoWebexTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: ciscoWebexOAuth2Api
- resources: all, attachmentAction, meeting, meetingTranscript, membership, message, recording, room, telephonyCall
- operations: create, delete, download, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | meeting | true |  |
| `resolveData` | Resolve Data | boolean | true |  | res=attachmentAction |
| `filters` | Filters | collection | {} |  |  |
