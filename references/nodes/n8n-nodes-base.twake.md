# Twake  (`n8n-nodes-base.twake`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: twakeCloudApi, twakeServerApi
- resources: message
- operations: send

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `twakeVersion` | Twake Version | options | cloud |  |  |
| `resource` | Resource | options | message |  |  |
| `operation` | Operation | options | send |  | res=message |
| `channelId` | Channel Name or ID | options |  |  | op=send |
| `content` | Content | string |  | true | op=send |
| `additionalFields` | Additional Fields | collection | {} |  | op=send |
