# Mailchimp Trigger  (`n8n-nodes-base.mailchimpTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: mailchimpApi, mailchimpOAuth2Api
- resources: campaign, listGroup, member, memberTag
- operations: create, delete, get, getAll, replicate, resend, send, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | apiKey |  |  |
| `list` | List Name or ID | options |  | true |  |
| `events` | Events | multiOptions | [] | true |  |
| `sources` | Sources | multiOptions | [] | true |  |
| `resource` | Resource | options | member | true |  |
| `operation` | Operation | options | create | true | res=member |
| `operation` | Operation | options | create | true | res=memberTag |
| `operation` | Operation | options | getAll | true | res=listGroup |
| `operation` | Operation | options | getAll | true | res=campaign |
| `list` | List Name or ID | options |  | true | res=member,op=create |
| `email` | Email | string |  | true | res=member,op=create |
| `status` | Status | options |  | true | res=member,op=create |
| `jsonParameters` | JSON Parameters | boolean | false |  | res=member,op=create |
| `options` | Options | collection | {} |  | res=member,op=create |
| `locationFieldsUi` | Location | fixedCollection | {} | true | res=member,op=create |
| `mergeFieldsUi` | Merge Fields | fixedCollection | {} | true | res=member,op=create |
| `mergeFieldsJson` | Merge Fields | json |  |  | res=member,op=create |
| `locationJson` | Location | json |  |  | res=member,op=create |
| `groupsUi` | Interest Groups | fixedCollection | {} |  | res=member,op=create |
| `groupJson` | Interest Groups | json |  |  | res=member,op=create |
| `list` | List Name or ID | options |  | true | res=member,op=delete |
| `email` | Email | string |  | true | res=member,op=delete |
| `list` | List Name or ID | options |  | true | res=member,op=get |
| `email` | Email | string |  | true | res=member,op=get |
| `options` | Options | collection | {} |  | res=member,op=get |
| `list` | List Name or ID | options |  | true | res=member,op=getAll |
| `returnAll` | Return All | boolean | false |  | res=member,op=getAll |
| `limit` | Limit | number | 500 |  | res=member,op=getAll |
| `options` | Options | collection | {} |  | res=member,op=getAll |
| `list` | List Name or ID | options |  | true | res=member,op=update |
| `email` | Email | string |  | true | res=member,op=update |
| `jsonParameters` | JSON Parameters | boolean | false |  | res=member,op=update |
| `updateFields` | Update Fields | collection | {} | true | res=member,op=update |
| `mergeFieldsJson` | Merge Fields | json |  |  | res=member,op=update |
| `locationJson` | Location | json |  |  | res=member,op=update |
| `groupJson` | Interest Groups | json |  |  | res=member,op=update |
| `list` | List Name or ID | options |  | true | res=memberTag,op=create,op=delete |
| `email` | Email | string |  | true | res=memberTag,op=create,op=delete |
| `tags` | Tags | string | [] |  | res=memberTag,op=create,op=delete |
| `options` | Options | collection | {} |  | res=memberTag,op=create,op=delete |
| `list` | List Name or ID | options |  | true | res=listGroup,op=getAll |
| `groupCategory` | Group Category Name or ID | options |  | true | res=listGroup,op=getAll |
| `returnAll` | Return All | boolean | false |  | res=listGroup,op=getAll |
| `limit` | Limit | number | 500 |  | res=listGroup,op=getAll |
| `returnAll` | Return All | boolean | false |  | res=campaign,op=getAll |
| `limit` | Limit | number | 10 |  | res=campaign,op=getAll |
| `options` | Options | collection | {} |  | res=campaign,op=getAll |
| `campaignId` | Campaign ID | string |  | true | res=campaign,op=send,op=get,op=delete,op=replicate,op=resend |
