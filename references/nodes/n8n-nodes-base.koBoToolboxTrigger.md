# KoBoToolbox Trigger  (`n8n-nodes-base.koBoToolboxTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: koBoToolboxApi
- resources: file, form, hook, submission
- operations: create, delete, get, getAll, getLogs, getValidation, redeploy, retryAll, retryOne, setValidation

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `formId` | Form Name or ID | options |  | true |  |
| `triggerOn` | Trigger On | options | formSubmission | true |  |
| `resource` | Resource | options | submission | true |  |
