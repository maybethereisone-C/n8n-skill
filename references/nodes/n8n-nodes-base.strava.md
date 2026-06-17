# Strava  (`n8n-nodes-base.strava`)

- typeVersion (max): **1.1**  | group: input  | trigger: no
- credentials: stravaOAuth2Api
- resources: activity
- operations: create, get, getAll, getComments, getKudos, getLaps, getStreams, getZones, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | activity |  |  |
| `object` | Object | options | * |  |  |
| `event` | Event | options | * |  |  |
| `resolveData` | Resolve Data | boolean | true |  |  |
| `options` | Options | collection | {} |  |  |
