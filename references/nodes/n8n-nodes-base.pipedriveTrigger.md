# Pipedrive Trigger  (`n8n-nodes-base.pipedriveTrigger`)

- typeVersion (max): **2**  | group: trigger  | trigger: yes
- credentials: pipedriveApi, pipedriveOAuth2Api
- resources: activity, deal, dealActivity, dealProduct, file, lead, note, organization, person, product
- operations: add, create, delete, download, duplicate, get, getAll, remove, search, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | apiToken |  |  |
| `incomingAuthentication` | Incoming Authentication | options | none |  |  |
| `action` | Action | options | * |  |  |
| `entity` | Entity | options | * |  |  |
| `object` | Object | options | * |  |  |
| `resource` | Resource | options | deal |  |  |
| `operation` | Operation | options | create |  | res=activity |
| `operation` | Operation | options | create |  | res=deal |
| `operation` | Operation | options | getAll |  | res=dealActivity |
| `operation` | Operation | options | add |  | res=dealProduct |
| `operation` | Operation | options | create |  | res=file |
| `operation` | Operation | options | create |  | res=lead |
| `operation` | Operation | options | create |  | res=note |
| `operation` | Operation | options | create |  | res=organization |
| `operation` | Operation | options | create |  | res=person |
| `operation` | Operation | options | getAll |  | res=product |
| `subject` | Subject | string |  | true | res=activity,op=create |
| `done` | Done | options | 0 |  | res=activity,op=create |
| `type` | Type | string |  | true | res=activity,op=create |
| `additionalFields` | Additional Fields | collection | {} |  | res=activity,op=create |
| `activityId` | Activity ID | number | 0 | true | res=activity,op=delete |
| `activityId` | Activity ID | number | 0 | true | res=activity,op=get |
| `activityId` | Activity ID | number | 0 | true | res=activity,op=update |
| `updateFields` | Update Fields | collection | {} |  | res=activity,op=update |
| `title` | Title | string |  | true | res=deal,op=create |
| `associateWith` | Associate With | options | organization | true | res=deal,op=create |
| `org_id` | Organization ID | number | 0 | true | res=deal,op=create |
| `person_id` | Person ID | number | 0 |  | res=deal,op=create |
| `additionalFields` | Additional Fields | collection | USD |  | res=deal,op=create |
| `dealId` | Deal ID | number | 0 | true | res=deal,op=delete |
| `dealId` | Deal ID | number | 0 | true | res=deal,op=duplicate |
| `dealId` | Deal ID | number | 0 | true | res=deal,op=get |
| `dealId` | Deal ID | number | 0 | true | res=deal,op=update |
| `updateFields` | Update Fields | collection | USD |  | res=deal,op=update |
| `dealId` | Deal Name or ID | options |  | true | res=dealProduct,op=add |
| `productId` | Product Name or ID | options |  | true | res=dealProduct,op=add |
| `item_price` | Item Price | number | 0.0 | true | res=dealProduct,op=add |
| `quantity` | Quantity | number | 1 | true | res=dealProduct,op=add |
| `additionalFields` | Additional Fields | collection | {} |  | res=dealProduct,op=add |
| `dealId` | Deal Name or ID | options |  | true | res=dealProduct,op=update |
| `productAttachmentId` | Product Attachment Name or ID | options |  | true | res=dealProduct,op=update |
| `updateFields` | Update Fields | collection | {} |  | res=dealProduct,op=update |
| `dealId` | Deal Name or ID | options |  | true | res=dealProduct,op=remove |
| `productAttachmentId` | Product Attachment Name or ID | options |  | true | res=dealProduct,op=remove |
| `dealId` | Deal Name or ID | options |  | true | res=dealProduct,op=getAll |
| `term` | Term | string |  | true | res=deal,op=search |
| `exactMatch` | Exact Match | boolean | false |  | res=deal,op=search |
| `returnAll` | Return All | boolean | false |  | op=search |
| `limit` | Limit | number | 100 |  | op=search |
| `additionalFields` | Additional Fields | collection | {} |  | res=deal,op=search |
| `binaryPropertyName` | Input Binary Field | string | data | true | res=file,op=create |
| `additionalFields` | Additional Fields | collection | {} |  | res=file,op=create |
| `fileId` | File ID | number | 0 | true | res=file,op=delete |
| `fileId` | File ID | number | 0 | true | res=file,op=download |
| `binaryPropertyName` | Put Output File in Field | string | data | true | res=file,op=download |
| `fileId` | File ID | number | 0 | true | res=file,op=get |
| `fileId` | File ID | number | 0 | true | res=file,op=update |
| `updateFields` | Update Fields | collection | {} |  | res=file,op=update |
| `title` | Title | string |  | true | res=lead,op=create |
| `associateWith` | Associate With | options | organization | true | res=lead,op=create |
| `organization_id` | Organization ID | number | 0 | true | res=lead,op=create |
| `person_id` | Person ID | number | 0 | true | res=lead,op=create |
| `additionalFields` | Additional Fields | collection | {} |  | res=lead,op=create |
| `leadId` | Lead ID | string |  | true | res=lead,op=delete |
| `leadId` | Lead ID | string |  | true | res=lead,op=get |
| `leadId` | Lead ID | string |  | true | res=lead,op=update |
| `updateFields` | Update Fields | collection | {} |  | res=lead,op=update |
| `content` | Content | string |  | true | res=note,op=create |
| `additionalFields` | Additional Fields | collection | {} |  | res=note,op=create,op=getAll |
| `noteId` | Note ID | number | 0 | true | res=note,op=delete |
| `noteId` | Note ID | number | 0 | true | res=note,op=get |
| `noteId` | Note ID | number | 0 | true | res=note,op=update |
| `updateFields` | Update Fields | collection | {} |  | res=note,op=update |
| `name` | Name | string |  | true | res=organization,op=create |
| `additionalFields` | Additional Fields | collection | {} |  | res=organization,op=create |
| `organizationId` | Organization ID | number | 0 | true | res=organization,op=delete |
| `organizationId` | Organization ID | number | 0 | true | res=organization,op=get |
| `term` | Term | string |  | true | res=organization,op=search |
| `additionalFields` | Additional Fields | collection | {} |  | res=organization,op=search |
| `organizationId` | Organization ID | number |  | true | res=organization,op=update |
| `updateFields` | Update Fields | collection | {} |  | res=organization,op=update |
| `name` | Name | string |  | true | res=person,op=create |
| `additionalFields` | Additional Fields | collection | {} |  | res=person,op=create |
| `personId` | Person ID | number | 0 | true | res=person,op=delete |
| `personId` | Person ID | number | 0 | true | res=person,op=get |
| `personId` | Person ID | number | 0 | true | res=person,op=update |
| `updateFields` | Update Fields | collection | {} |  | res=person,op=update |
| `resolveProperties` | Resolve Properties | boolean | false |  | res=activity,res=deal,res=organization,res=person,res=product,op=get |
| `encodeProperties` | Encode Properties | boolean | false |  | res=activity,res=deal,res=organization,res=person,res=product,op=update |
| `returnAll` | Return All | boolean | false |  | op=getAll |
| `limit` | Limit | number | 100 |  | op=getAll |
| `dealId` | Deal Name or ID | options |  | true | res=dealActivity,op=getAll |
| `additionalFields` | Additional Fields | collection | {} |  | res=dealActivity,op=getAll |
| `filters` | Filters | collection | all |  | res=lead,op=getAll |
| `filters` | Filters | collection | {} |  | res=organization,op=getAll |
| `additionalFields` | Additional Fields | collection | {} |  | res=person,op=getAll |
| `term` | Term | string |  | true | res=person,op=search |
| `additionalFields` | Additional Fields | collection | {} |  | res=person,op=search |
| `additionalFields` | Additional Fields | collection | {} |  | res=activity,op=getAll |
| `filters` | Filters | collection | {} |  | res=deal,op=getAll |
