# Notion Trigger  (`n8n-nodes-base.notionTrigger`)

- typeVersion (max): **2.2**  | group: trigger  | trigger: yes
- credentials: notionApi, notionOAuth2Api
- resources: block, database, databasePage, page, user
- operations: append, archive, create, get, getAll, search, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | apiKey |  |  |
| `event` | Event | options | pageAddedToDatabase | true |  |
| `notionNotice` | In Notion, make sure to <a href="https://www.notion.com/help/add-and-manage-connections-with-the-api" target="_blank">add your connection</a> to the pages you want to access. | notice |  |  |  |
| `databaseId` | Database | resourceLocator |  | true |  |
| `simple` | Simplify | boolean | true |  |  |
| `resource` | Resource | options | page |  |  |
| `Credentials` | Credentials | credentials |  |  |  |
