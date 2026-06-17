# Emelia Trigger  (`n8n-nodes-base.emeliaTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: emeliaApi
- resources: campaign, contactList
- operations: add, addContact, create, duplicate, get, getAll, pause, start

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `campaignId` | Campaign Name or ID | options |  | true |  |
| `events` | Events | multiOptions | [] | true |  |
| `resource` | Resource | options | campaign | true |  |
