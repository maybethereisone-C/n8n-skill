# HTTP Request  (`n8n-nodes-base.httpRequest`)

- typeVersion (max): **4.4**  | group: output  | trigger: no
- credentials: oAuth1Api, oAuth2Api

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | none |  |  |
| `requestMethod` | Request Method | options | GET |  |  |
| `url` | URL | string |  | true |  |
| `allowUnauthorizedCerts` | Ignore SSL Issues (Insecure) | boolean | false |  |  |
| `responseFormat` | Response Format | options | json |  |  |
| `dataPropertyName` | Property Name | string | data | true |  |
| `jsonParameters` | JSON/RAW Parameters | boolean | false |  |  |
| `options` | Options | collection | json |  |  |
| `sendBinaryData` | Send Binary File | boolean | false |  |  |
| `binaryPropertyName` | Input Binary Field | string | data | true |  |
| `bodyParametersJson` | Body Parameters | json |  |  |  |
| `bodyParametersUi` | Body Parameters | fixedCollection | {} |  |  |
| `headerParametersJson` | Headers | json |  |  |  |
| `headerParametersUi` | Headers | fixedCollection | {} |  |  |
| `queryParametersJson` | Query Parameters | json |  |  |  |
| `queryParametersUi` | Query Parameters | fixedCollection | {} |  |  |
| `infoMessage` | You can view the raw requests this node makes in your browser's developer console | notice |  |  |  |
| `nodeCredentialType` | Credential Type | credentialsSelect |  | true |  |
| `genericAuthType` | Generic Auth Type | credentialsSelect |  | true |  |
