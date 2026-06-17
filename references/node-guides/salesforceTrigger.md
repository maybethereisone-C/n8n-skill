# Salesforce Trigger — `n8n-nodes-base.salesforceTrigger`
**Type** `n8n-nodes-base.salesforceTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires when Salesforce CRM objects are created or updated (polling via Salesforce API).
**Credentials:** `salesforceOAuth2Api` (OAuth2 — connected app in Salesforce).
**Resources / Operations:**
| Object | Events |
|---|---|
| Account | Created / Updated |
| Attachment | Created / Updated |
| Case | Created / Updated |
| Contact | Created / Updated |
| Custom Object | Created / Updated |
| Lead | Created / Updated |
| Opportunity | Created / Updated |
| Task | Created / Updated |
| User | Created / Updated |

**Key params & gotchas:**
- **Polling** trigger — uses Salesforce SOQL queries with `LastModifiedDate` filter; not a streaming push. Latency = poll interval.
- For **Custom Object**: enter the API name (e.g. `My_Object__c`) in the **Custom Object** field.
- Deduplication is based on record ID + `LastModifiedDate` stored between polls.
- The connected app in Salesforce must have the correct OAuth scopes (`api`, `refresh_token`).
- Salesforce API governor limits apply — high-volume tables with frequent updates can exhaust per-org API call limits.

**Source:** n8n-nodes-base.salesforcetrigger.md  [doc-verified]
