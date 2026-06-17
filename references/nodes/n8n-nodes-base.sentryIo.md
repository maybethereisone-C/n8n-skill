# Sentry.io  (`n8n-nodes-base.sentryIo`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: sentryIoApi, sentryIoOAuth2Api, sentryIoServerApi
- resources: event, issue, organization, project, release, team
- operations: create, delete, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | accessToken |  |  |
| `resource` | Resource | options | event |  |  |
