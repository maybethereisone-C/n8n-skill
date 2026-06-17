# Storyblok  (`n8n-nodes-base.storyblok`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: storyblokContentApi, storyblokManagementApi
- resources: story
- operations: create, delete, get, getAll, publish, unpublish

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `source` | Source | options | contentApi |  |  |
| `resource` | Resource | options | story |  |  |
