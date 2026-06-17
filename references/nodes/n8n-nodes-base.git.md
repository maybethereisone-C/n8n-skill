# Git  (`n8n-nodes-base.git`)

- typeVersion (max): **1.1**  | group: transform  | trigger: no
- credentials: —
- operations: add, addConfig, clone, commit, fetch, listConfig, log, pull, push, pushTags, reflog, status, switchBranch, tag, userSetup

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | none |  | op=clone,op=push |
| `operation` | Operation | options | log |  |  |
| `repositoryPath` | Repository Path | string |  | true | op=clone |
