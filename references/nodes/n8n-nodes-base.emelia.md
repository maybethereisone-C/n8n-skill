# Emelia  (`n8n-nodes-base.emelia`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: emeliaApi
- resources: campaign, contactList
- operations: add, addContact, create, duplicate, get, getAll, pause, start

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | campaign | true |  |
| `campaignId` | Campaign Name or ID | options |  | true |  |
| `events` | Events | multiOptions | [] | true |  |
