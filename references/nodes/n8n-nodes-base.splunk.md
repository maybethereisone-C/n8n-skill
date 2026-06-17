# Splunk  (`n8n-nodes-base.splunk`)

- typeVersion (max): **2**  | group: transform  | trigger: no
- credentials: splunkApi
- resources: alert, firedAlert, report, search, searchConfiguration, searchJob, searchResult, user
- operations: create, delete, deleteJob, deleteReport, deleteUser, get, getAll, getMetrics, getReport, getResult, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | searchJob |  |  |
