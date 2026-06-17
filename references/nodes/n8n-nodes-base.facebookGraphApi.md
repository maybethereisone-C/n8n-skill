# Facebook Graph API  (`n8n-nodes-base.facebookGraphApi`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: facebookGraphApi, facebookGraphApiOAuth2Api, facebookGraphAppApi, facebookGraphAppOAuth2Api

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authType` | Authentication | options | accessToken |  |  |
| `hostUrl` | Host URL | options | graph.facebook.com | true |  |
| `httpRequestMethod` | HTTP Request Method | options | GET | true |  |
| `graphApiVersion` | Graph API Version | options |  | true |  |
| `node` | Node | string |  | true |  |
| `edge` | Edge | string |  |  |  |
| `allowUnauthorizedCerts` | Ignore SSL Issues (Insecure) | boolean | false |  |  |
| `sendBinaryData` | Send Binary File | boolean | false | true |  |
| `binaryPropertyName` | Input Binary Field | string |  |  |  |
| `options` | Options | collection | {} |  |  |
| `appId` | APP ID | string |  | true |  |
| `whatsappBusinessAccountNotice` | To watch Whatsapp business account events use the Whatsapp trigger node | notice |  |  |  |
| `object` | Object | options | user | true |  |
| `fields` | Field Names or IDs | multiOptions | [] |  |  |
