# Strava Trigger  (`n8n-nodes-base.stravaTrigger`)

- typeVersion (max): **1.1**  | group: trigger  | trigger: yes
- credentials: stravaOAuth2Api
- resources: activity
- operations: create, get, getAll, getComments, getKudos, getLaps, getStreams, getZones, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `object` | Object | options | * |  |  |
| `event` | Event | options | * |  |  |
| `resolveData` | Resolve Data | boolean | true |  |  |
| `options` | Options | collection | {} |  |  |
| `resource` | Resource | options | activity |  |  |
