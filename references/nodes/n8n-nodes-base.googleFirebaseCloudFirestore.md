# Google Cloud Firestore  (`n8n-nodes-base.googleFirebaseCloudFirestore`)

- typeVersion (max): **1.1**  | group: input  | trigger: no
- credentials: googleApi, googleFirebaseCloudFirestoreOAuth2Api
- resources: collection, document
- operations: create, delete, get, getAll, query, update, upsert

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | googleFirebaseCloudFirestoreOAuth2Api |  |  |
| `resource` | Resource | options | document |  |  |
