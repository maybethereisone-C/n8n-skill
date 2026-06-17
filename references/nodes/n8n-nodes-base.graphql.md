# GraphQL  (`n8n-nodes-base.graphql`)

- typeVersion (max): **1.1**  | group: input  | trigger: no
- credentials: oAuth1Api, oAuth2Api

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | none |  |  |
| `requestMethod` | HTTP Request Method | options | POST |  |  |
| `endpoint` | Endpoint | string |  | true |  |
| `allowUnauthorizedCerts` | Ignore SSL Issues (Insecure) | boolean | false |  |  |
| `requestFormat` | Request Format | options | graphql | true |  |
| `query` | Query | string |  | true |  |
| `variables` | Variables | json |  |  |  |
| `operationName` | Operation Name | string |  |  |  |
| `responseFormat` | Response Format | options | json |  |  |
| `dataPropertyName` | Response Data Property Name | string | data | true |  |
| `headerParametersUi` | Headers | fixedCollection | {} |  |  |
