# Mautic  (`n8n-nodes-base.mautic`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: mauticApi, mauticOAuth2Api
- resources: campaignContact, company, companyContact, contact, contactSegment, segmentEmail
- operations: add, create, delete, editContactPoint, editDoNotContactList, get, getAll, remove, send, sendEmail, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | credentials |  |  |
| `resource` | Resource | options | contact |  |  |
| `events` | Event Names or IDs | multiOptions | [] | true |  |
| `eventsOrder` | Events Order | options | ASC |  |  |
