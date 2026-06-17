# Gumroad Trigger  (`n8n-nodes-base.gumroadTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: gumroadApi, gumroadOAuth2Api
- resources: cancellation, dispute, dispute_won, refund, sale

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | accessToken |  |  |
| `resource` | Resource | options |  | true |  |
