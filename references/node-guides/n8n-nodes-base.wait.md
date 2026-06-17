# Wait — `n8n-nodes-base.wait`

**Type** `n8n-nodes-base.wait` · **typeVersion** 1.1 · **core**

**What:** Pauses workflow execution and offloads state to the database until a resume condition is met (time, webhook call, or form submission).

**Credentials:** none (optional per-auth-type credential for webhook auth).

**Resources / Operations:**

| Resume Mode | Description |
|---|---|
| After Time Interval | Resumes after N seconds/minutes/hours/days |
| At Specified Time | Resumes at a specific datetime |
| On Webhook Call | Resumes when `$execution.resumeUrl` is called |
| On Form Submitted | Resumes when a generated form is submitted |

**Key params & gotchas:**

- **Resume URL variable** — for `On Webhook Call`, the unique URL is available as `$execution.resumeUrl` at runtime. You must send it somewhere (email, Slack, etc.) *before* this node executes, because it is generated per-execution.
- **Webhook Suffix** — when a workflow has multiple Wait nodes in webhook mode, give each a unique suffix. The suffix is NOT automatically appended to `$execution.resumeUrl`; you must concatenate it manually before forwarding the URL.
- **Limit Wait Time** — safety escape hatch on webhook/form modes; auto-resumes after an interval or at a wall-clock time if the expected callback never arrives.
- **Sub-65-second waits** — time-interval waits under 65 s do NOT offload to the database; the process holds in memory. For longer pauses, offloading occurs and the instance must be running when the time elapses.
- **Timezone** — Wait always uses n8n server time. Workflow timezone settings are ignored.
- **Authentication** (webhook mode) — supports Basic Auth, Header Auth, JWT Auth, or None. Credentials must already exist.
- **Partial executions** — each partial re-run generates a new `$execution.resumeUrl`; ensure the node that forwards the URL is in the same execution as the Wait node.

**Minimal example (webhook resume):**

Send the resume URL in a prior step:
```
$execution.resumeUrl
```
Then a downstream system POSTs to that URL to unblock the workflow.

**Source:** n8n-nodes-base.wait.md  [doc-verified]
