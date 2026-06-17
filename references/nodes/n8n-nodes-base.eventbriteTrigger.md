# Eventbrite Trigger  (`n8n-nodes-base.eventbriteTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: eventbriteApi, eventbriteOAuth2Api

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | privateKey |  |  |
| `organization` | Organization Name or ID | options |  | true |  |
| `event` | Event Name or ID | options |  | true |  |
| `actions` | Actions | multiOptions | [] | true |  |
| `resolveData` | Resolve Data | boolean | true |  |  |
