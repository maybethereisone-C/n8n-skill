# KoBoToolbox  (`n8n-nodes-base.koBoToolbox`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: koBoToolboxApi
- resources: file, form, hook, submission
- operations: create, delete, get, getAll, getLogs, getValidation, redeploy, retryAll, retryOne, setValidation

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | submission | true |  |
| `formId` | Form Name or ID | options |  | true |  |
| `triggerOn` | Trigger On | options | formSubmission | true |  |
