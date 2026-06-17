# SurveyMonkey Trigger  (`n8n-nodes-base.surveyMonkeyTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: surveyMonkeyApi, surveyMonkeyOAuth2Api

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | accessToken |  |  |
| `objectType` | Type | options |  | true |  |
| `event` | Event | options |  | true |  |
| `surveyIds` | Survey Names or IDs | multiOptions | [] | true |  |
| `surveyId` | Survey Name or ID | options | [] | true |  |
| `collectorIds` | Collector Names or IDs | multiOptions | [] | true |  |
| `resolveData` | Resolve Data | boolean | true |  |  |
| `onlyAnswers` | Only Answers | boolean | true |  |  |
