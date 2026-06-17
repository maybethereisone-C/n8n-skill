# ConvertKit Trigger  (`n8n-nodes-base.convertKitTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: convertKitApi
- resources: customField, form, sequence, tag, tagSubscriber
- operations: add, addSubscriber, create, delete, getAll, getSubscriptions, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `event` | Event | options |  | true |  |
| `formId` | Form Name or ID | options |  | true |  |
| `courseId` | Sequence Name or ID | options |  | true |  |
| `link` | Initiating Link | string |  | true |  |
| `productId` | Product ID | string |  | true |  |
| `tagId` | Tag Name or ID | options |  | true |  |
| `resource` | Resource | options | form |  |  |
