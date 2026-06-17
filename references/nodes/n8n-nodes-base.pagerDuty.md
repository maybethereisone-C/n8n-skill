# PagerDuty  (`n8n-nodes-base.pagerDuty`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: pagerDutyApi, pagerDutyOAuth2Api
- resources: incident, incidentNote, logEntry, user
- operations: create, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | apiToken |  |  |
| `resource` | Resource | options | incident |  |  |
