# E2E Test  (`n8n-nodes-base.e2eTest`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: —
- operations: remoteOptions, resourceLocator, resourceMapper

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `operation` | Operation | options | remoteOptions |  |  |
| `fieldId` | Field ID | string |  |  |  |
| `remoteOptions` | Remote Options Name or ID | options | [] | true | op=remoteOptions |
| `rlc` | Resource Locator | resourceLocator |  | true | op=resourceLocator |
| `resourceMapper` | Resource Mapping Component | resourceMapper |  | true | op=resourceMapper |
| `otherField` | Other Non Important Field | string |  |  |  |
