# Zoom  (`n8n-nodes-base.zoom`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: zoomApi, zoomOAuth2Api
- resources: meeting, meetingRegistrant, webinar
- operations: create, delete, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | accessToken |  |  |
| `resource` | Resource | options | meeting |  |  |
