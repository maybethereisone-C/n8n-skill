# AWS SNS Trigger  (`n8n-nodes-base.awsSnsTrigger`)

- typeVersion (max): **2**  | group: trigger  | trigger: yes
- credentials: —
- resources: bucket, certificate, customVerificationEmail, email, file, folder, group, image, item, listenerCertificate, loadBalancer, template, text, transcriptionJob, user, userPool
- operations: ={{ { "addedToGroup": true } }}, ={{ { "deleted": true } }}, ={{ { "removedFromGroup": true } }}, ={{ { "updated": true } }}, add, addToGroup, analyze, analyzeExpense, copy, create, delete, detectDominantLanguage, detectEntities, detectSentiment, download, get, getAll, getMany, getMetadata, invoke, publish, remove, removeFromGroup, renew, search, send, sendMessage, sendTemplate, update, upload, upsert

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `topic` | Topic | resourceLocator |  | true |  |
| `operation` | Operation | options | invoke |  |  |
| `function` | Function Name or ID | options |  | true | op=invoke |
| `qualifier` | Qualifier | string | $LATEST | true | op=invoke |
| `invocationType` | Invocation Type | options | RequestResponse |  | op=invoke |
| `payload` | JSON Input | string |  |  | op=invoke |
| `name` | Name | string |  | true | op=create |
| `options` | Options | collection | {} |  | op=create |
| `topic` | Topic | resourceLocator |  | true | op=publish,op=delete |
| `subject` | Subject | string |  | true | op=publish |
| `message` | Message | string |  | true | op=publish |
| `resource` | Resource | options | file |  |  |
| `queue` | Queue Name or ID | options |  | true | op=sendMessage |
| `queueType` | Queue Type | options | standard |  |  |
| `sendInputData` | Send Input Data | boolean | true |  |  |
| `message` | Message | string |  | true | op=sendMessage |
| `messageGroupId` | Message Group ID | string |  | true |  |
| `options` | Options | collection | {} |  | op=sendMessage |
| `binaryPropertyName` | Input Data Field Name | string | data | true | op=analyzeExpense |
| `simple` | Simplify | boolean | true |  | op=analyzeExpense |
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
| `languageCode` | Language Code | options | en |  | res=text,op=detectSentiment,op=detectEntities |
| `text` | Text | string |  |  | res=text |
| `simple` | Simplify | boolean | true |  | res=text,op=detectDominantLanguage |
| `additionalFields` | Additional Fields | collection | {} |  | res=text,op=detectEntities |
| `type` | Type | options | detectFaces |  | res=image,op=analyze |
| `binaryData` | Binary File | boolean | false | true | res=image,op=analyze |
| `binaryPropertyName` | Input Binary Field | string | data | true | res=image,op=analyze |
| `bucket` | Bucket | string |  | true | res=image,op=analyze |
| `name` | Name | string |  | true | res=image,op=analyze |
| `additionalFields` | Additional Fields | collection | {} |  | res=image,op=analyze |
| `transcriptionJobName` | Job Name | string |  |  | res=transcriptionJob,op=create,op=get,op=delete |
| `mediaFileUri` | Media File URI | string |  |  | res=transcriptionJob,op=create |
| `detectLanguage` | Detect Language | boolean | false |  | res=transcriptionJob,op=create |
| `languageCode` | Language | options | en-US |  | res=transcriptionJob,op=create |
| `returnTranscript` | Return Transcript | boolean | true |  | res=transcriptionJob,op=get |
| `simple` | Simplify | boolean | true |  | res=transcriptionJob,op=get |
| `returnAll` | Return All | boolean | false |  | res=transcriptionJob,op=getAll |
| `limit` | Limit | number | 20 |  | res=transcriptionJob,op=getAll |
| `filters` | Filters | collection | {} |  | res=transcriptionJob,op=getAll |
