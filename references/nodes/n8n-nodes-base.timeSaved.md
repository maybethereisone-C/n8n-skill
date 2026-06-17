# Track Time Saved  (`n8n-nodes-base.timeSaved`)

- typeVersion (max): **1**  | group: organization  | trigger: no
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `notice` | For each run, time saved is the sum of all Time Saved nodes that execute. Use this when different execution paths or items save different amounts of time. | notice |  |  |  |
| `mode` | Calculation Mode | options | once |  |  |
| `minutesSaved` | Minutes Saved | number | 0 |  |  |
