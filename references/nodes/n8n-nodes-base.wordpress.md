# Wordpress  (`n8n-nodes-base.wordpress`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: wordpressApi, wordpressOAuth2Api
- resources: page, post, user
- operations: create, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authType` | Authentication | options | basicAuth |  |  |
| `resource` | Resource | options | post |  |  |
