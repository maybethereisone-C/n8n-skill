# Typeform Trigger  (`n8n-nodes-base.typeformTrigger`)

- typeVersion (max): **1.1**  | group: trigger  | trigger: yes
- credentials: typeformApi, typeformOAuth2Api

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | accessToken |  |  |
| `formId` | Form Name or ID | options |  | true |  |
| `simplifyAnswers` | Simplify Answers | boolean | true |  |  |
| `onlyAnswers` | Only Answers | boolean | true |  |  |
