# Beeminder  (`n8n-nodes-base.beeminder`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: beeminderApi, beeminderOAuth2Api
- resources: charge, datapoint, goal, user
- operations: cancelStepDown, create, createAll, delete, get, getAll, getArchived, refresh, shortCircuit, stepDown, uncle, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | apiToken |  |  |
| `resource` | Resource | options | datapoint | true |  |
| `operation` | Operation | options | create | true | res=charge |
| `operation` | Operation | options | create | true | res=datapoint |
| `operation` | Operation | options | get | true | res=goal |
| `operation` | Operation | options | get | true | res=user |
| `goalName` | Goal Name or ID | options |  | true | res=datapoint |
| `goalName` | Goal Name or ID | options |  | true | res=goal,op=uncle |
| `goalName` | Goal Name or ID | options |  | true | res=goal,op=get,op=update,op=refresh,op=shortCircuit,op=stepDown |
| `amount` | Amount | number | 0 | true | res=charge,op=create |
| `datapoints` | Datapoints | json | [] | true | res=datapoint,op=createAll |
| `slug` | Goal Slug | string |  | true | res=goal,op=create |
| `title` | Goal Title | string |  | true | res=goal,op=create |
| `goal_type` | Goal Type | options | hustler | true | res=goal,op=create |
| `gunits` | Goal Units | string |  | true | res=goal,op=create |
| `returnAll` | Return All | boolean | false |  | res=datapoint,op=getAll |
| `limit` | Limit | number | 30 |  | res=datapoint,op=getAll |
| `value` | Value | number | 1 | true | res=datapoint,op=create |
| `datapointId` | Datapoint ID | string |  | true | res=datapoint,op=update,op=delete,op=get |
| `additionalFields` | Additional Fields | collection | {} |  | res=datapoint,op=create |
| `additionalFields` | Additional Fields | collection | {} |  | res=charge,op=create |
| `additionalFields` | Additional Fields | collection | manual |  | res=goal,op=create |
| `updateFields` | Update Fields | collection | {} |  | res=goal,op=update |
| `additionalFields` | Additional Fields | collection | {} |  | res=goal,op=get |
| `additionalFields` | Additional Fields | collection | {} |  | res=user,op=get |
| `additionalFields` | Additional Fields | collection | {} |  | res=goal,op=getAll |
| `additionalFields` | Additional Fields | collection | {} |  | res=goal,op=getArchived |
| `options` | Options | collection | id |  | res=datapoint,op=getAll |
| `updateFields` | Update Fields | collection | {} |  | res=datapoint,op=update |
