# AWS SES  (`n8n-nodes-base.awsSes`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: —
- resources: customVerificationEmail, email, template
- operations: create, delete, get, getAll, send, sendTemplate, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | email |  |  |
| `operation` | Operation | options | create |  | res=customVerificationEmail |
| `fromEmailAddress` | From Email | string |  | true | res=customVerificationEmail,op=create |
| `templateName` | Template Name | string |  |  | res=customVerificationEmail,op=create |
| `templateContent` | Template Content | string |  |  | res=customVerificationEmail,op=create |
| `templateSubject` | Template Subject | string |  | true | res=customVerificationEmail,op=create |
| `successRedirectionURL` | Success Redirection URL | string |  | true | res=customVerificationEmail,op=create |
| `failureRedirectionURL` | Failure Redirection URL | string |  | true | res=customVerificationEmail,op=create |
| `email` | Email | string |  | true | res=customVerificationEmail,op=send |
| `templateName` | Template Name | string |  | true | res=customVerificationEmail,op=send |
| `additionalFields` | Additional Fields | collection | {} |  | res=customVerificationEmail,op=send |
| `templateName` | Template Name | string |  |  | res=customVerificationEmail,op=update,op=delete,op=get |
| `updateFields` | Update Fields | collection | {} |  | res=customVerificationEmail,op=update |
| `returnAll` | Return All | boolean | false |  | res=customVerificationEmail,op=getAll |
| `limit` | Limit | number | 20 |  | res=customVerificationEmail,op=getAll |
| `operation` | Operation | options | send |  | res=email |
| `isBodyHtml` | Is Body HTML | boolean | false |  | res=email,op=send |
| `subject` | Subject | string |  | true | res=email,op=send |
| `body` | Body | string |  | true | res=email,op=send |
| `fromEmail` | From Email | string |  | true | res=email,op=send |
| `toAddresses` | To Addresses | string | [] |  | res=email,op=send |
| `templateName` | Template Name or ID | options |  |  | res=email,op=sendTemplate |
| `fromEmail` | From Email | string |  | true | res=email,op=sendTemplate |
| `toAddresses` | To Addresses | string | [] |  | res=email,op=sendTemplate |
| `templateDataUi` | Template Data | fixedCollection | {} |  | res=email,op=sendTemplate |
| `additionalFields` | Additional Fields | collection | {} |  | res=email,op=send,op=sendTemplate |
| `operation` | Operation | options | create |  | res=template |
| `templateName` | Template Name | string |  | true | res=template,op=update,op=create,op=get,op=delete |
| `subjectPart` | Subject Part | string |  |  | res=template,op=create |
| `htmlPart` | Html Part | string |  |  | res=template,op=create |
| `additionalFields` | Additional Fields | collection | {} |  | res=template,op=create |
| `updateFields` | Update Fields | collection | {} |  | res=template,op=update |
| `returnAll` | Return All | boolean | false |  | res=template,op=getAll |
| `limit` | Limit | number | 20 |  | res=template,op=getAll |
