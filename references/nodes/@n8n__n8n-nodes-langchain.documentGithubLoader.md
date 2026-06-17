# GitHub Document Loader  (`@n8n/n8n-nodes-langchain.documentGithubLoader`)

- typeVersion (max): **1.1**  | group: transform  | trigger: no
- credentials: githubApi

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `repository` | Repository Link | string |  |  |  |
| `branch` | Branch | string | main |  |  |
| `textSplittingMode` | Text Splitting | options | simple | true |  |
| `additionalOptions` | Options | collection | {} |  |  |
