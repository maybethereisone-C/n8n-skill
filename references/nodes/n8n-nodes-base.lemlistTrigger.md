# Lemlist Trigger  (`n8n-nodes-base.lemlistTrigger`)

- typeVersion (max): **2**  | group: trigger  | trigger: yes
- credentials: lemlistApi
- resources: activity, campaign, enrich, lead, team, unsubscribe
- operations: add, create, delete, enrichLead, enrichPerson, get, getAll, getCredits, getStats, unsubscribe

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `event` | Event | options |  | true |  |
| `options` | Options | collection | {} |  |  |
| `resource` | Resource | options | activity |  |  |
