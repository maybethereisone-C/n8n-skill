# Mautic Trigger  (`n8n-nodes-base.mauticTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: mauticApi, mauticOAuth2Api
- resources: campaignContact, company, companyContact, contact, contactSegment, segmentEmail
- operations: add, create, delete, editContactPoint, editDoNotContactList, get, getAll, remove, send, sendEmail, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | credentials |  |  |
| `events` | Event Names or IDs | multiOptions | [] | true |  |
| `eventsOrder` | Events Order | options | ASC |  |  |
| `resource` | Resource | options | contact |  |  |
