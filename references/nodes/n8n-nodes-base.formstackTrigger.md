# Formstack Trigger  (`n8n-nodes-base.formstackTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: formstackApi, formstackOAuth2Api

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | accessToken |  |  |
| `formId` | Form Name or ID | options |  | true |  |
| `simple` | Simplify | boolean | true |  |  |
