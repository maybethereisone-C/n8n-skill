# n8n Webhooks — Complete Reference

> Source files: `docs/integrations/builtin/core-nodes/n8n-nodes-base.webhook/index.md`,
> `…/workflow-development.md`, `…/common-issues.md`,
> `docs/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook.md`,
> `docs/integrations/builtin/core-nodes/n8n-nodes-base.wait.md`

---

## URL types: test vs production

| | Test URL | Production URL |
|---|---|---|
| **How to activate** | Click **Listen for test event** in node panel | Publish the workflow |
| **Active duration** | 120 seconds | Until workflow is unpublished |
| **Data visible in editor** | Yes | No (view via Executions tab) |
| **Tunnel required on localhost** | Yes (`n8n start --tunnel`) | No |
| **Use case** | Development, debugging | Live traffic |

URL format (self-hosted):
- Test: `<HOST>:<PORT>/webhook-test/<path>`
- Production: `<HOST>:<PORT>/webhook/<path>`

Cloud: same paths under `<instance>.app.n8n.cloud/…`.

**Cloudflare timeout (n8n Cloud):** Webhooks that do not respond within 100 seconds receive a 524 error. For long-running workflows: configure an immediate-response webhook + a separate status-poll webhook.

**One webhook per path + method combination.** Registering a duplicate path/method raises a conflict error. Either change the path/method or unpublish the conflicting workflow.

---

## Webhook node parameters

### HTTP Method

Accepted values: `DELETE`, `GET`, `HEAD`, `PATCH`, `POST`, `PUT`.

Enable multiple methods per node: **Settings → Allow Multiple HTTP Methods**. Each method gets its own output branch.

Maximum payload: **16 MB** (self-hosted override: env var `N8N_PAYLOAD_SIZE_MAX`).

### Path

Default: randomly generated UUID path.

Custom paths support route parameters:

```
/:variable
/path/:variable
/:variable/path
/:variable1/path/:variable2
/:variable1/:variable2
```

Route params are available in the workflow as `$json.params.variable`.

### Authentication

| Method | Description |
|---|---|
| None | Open webhook — no auth required |
| Basic auth | Username + password via `Webhook` credential |
| Header auth | Custom header name + value via `Webhook` credential |
| JWT auth | JWT verification via `Webhook` credential |

Credential type: `webhookAuth`. Configure in **Credentials → Webhook**.

### Respond (responseMode)

Controls when and how the webhook replies to the caller:

| Mode | API value | Behavior |
|---|---|---|
| **Immediately** | `onReceived` | Returns `{ message: "Workflow got started." }` plus configured response code at once. Workflow continues asynchronously. |
| **When Last Node Finishes** | `lastNode` | Holds the HTTP connection open; returns last node's output when workflow completes. |
| **Using 'Respond to Webhook' Node** | `responseNode` | Delegates response control to a downstream Respond to Webhook node. |
| **Streaming response** | `streaming` | Real-time streaming back to caller (requires nodes with streaming support, e.g. AI Agent node). |

### Response Code

Configurable HTTP status code for success response. Default: 200. Supports custom codes.

Not applicable when **Respond = Using 'Respond to Webhook' Node** (response code set in that node instead).

### Response Data (when Respond = When Last Node Finishes)

| Option | Returns |
|---|---|
| All Entries | Array of all last-node output items |
| First Entry JSON | JSON object of first item |
| First Entry Binary | Binary file of first item |
| No Response Body | Empty body with status code |

---

## Webhook node options

| Option | Applies when | Description |
|---|---|---|
| Allowed Origins (CORS) | Any | Comma-separated list of allowed cross-origin domains. Default `*`. |
| Binary Property | POST / PATCH / PUT | Name of binary property to write received file data to. Enable to receive binary uploads. |
| Ignore Bots | Any | Drop requests from crawlers and link previewers. |
| IP(s) Whitelist | Any | Comma-separated allowed IPs. Requests from other IPs → 403. |
| No Response Body | Respond = Immediately | Send status code with no body. |
| Raw Body | Any | Receive body as raw string (JSON, XML, etc.) without parsing. |
| Response Content-Type | Respond = Last Node, Data = First Entry JSON | Set `Content-Type` header on response. |
| Response Data | Respond = Immediately | Custom response body string. |
| Response Headers | Any | Extra headers on the webhook response. |
| Property Name | Respond = Last Node + First Entry JSON | Return a specific JSON key's value instead of the full object. |

---

## Accessing webhook data in the workflow

```js
// Request body (JSON)
$json.body.fieldName

// Query string params
$json.query.paramName

// Route params (custom path /:variable)
$json.params.variable

// Headers
$json.headers['content-type']

// Raw body (when Raw Body option enabled)
$json.body    // string, not parsed object
```

**$json.body gotcha:** when `Raw Body` is off (default), n8n parses the body and the result is in `$json.body` as a nested object. When `Raw Body` is on, `$json.body` is the raw string. For binary uploads, use the `Binary Property` option — the file lands on `$binary.<propertyName>`.

---

## Respond to Webhook node

Used when the Webhook node is set to **Respond = Using 'Respond to Webhook' Node**. Placed anywhere downstream (executes once, using the first incoming item).

### Respond With options

| Option | Description |
|---|---|
| All Incoming Items | Array of all input items as JSON |
| Binary File | Binary file from **Response Data Source** field |
| First Incoming Item | JSON of first input item |
| JSON | Custom JSON from **Response Body** expression |
| JWT Token | Signs and returns a JWT |
| No Data | Empty body |
| Redirect | HTTP redirect to **Redirect URL** |
| Text | Text/HTML string from **Response Body** (sends `Content-Type: text/html` by default) |

### Options

| Option | Description |
|---|---|
| Response Code | HTTP status code to return |
| Response Headers | Additional headers |
| Put Response in Field | Wraps All/First Incoming Items in a named field |
| Enable Streaming | Use with Streaming response mode |

### Workflow behavior rules

- Workflow ends without hitting Respond to Webhook node → 200 + standard message
- Workflow errors before Respond to Webhook node → 500 + error message
- Second Respond to Webhook node executes → ignored (first one wins)
- Respond to Webhook node executes with no webhook in scope → ignored

### Secondary output branch

Enable in **Settings → Enable Response Output Branch**. Adds a second output containing the response object sent to the webhook (in addition to the default input-data passthrough output).

### HTML responses and iframe sandboxing (v1.103.0+)

n8n wraps HTML responses in `<iframe>` tags for security:
- JavaScript cannot access the top-level window or local storage
- Basic auth headers unavailable in sandboxed iframe — embed short-lived token in HTML instead
- Relative URLs (`<form action="/">`) break — use absolute URLs

---

## Waiting webhooks — the Wait node

The Wait node pauses execution and offloads state to the database. Resumes when a condition is met.

### Resume modes

| Mode | Description |
|---|---|
| After Time Interval | Fixed delay (seconds / minutes / hours / days). For waits < 65s, state is not offloaded to DB. |
| At Specified Time | Resumes at a specific datetime. Uses n8n server time regardless of workflow timezone. |
| On Webhook Call | Resumes when an HTTP call is made to `$execution.resumeUrl` |
| On Form Submitted | Resumes when a form is submitted |

### On Webhook Call — resume URL

```js
// Available as a variable during execution
$execution.resumeUrl
```

- URL is **generated at runtime** and is **unique per execution**
- Send this URL to a third party (email, Slack, external service) so they can resume the workflow
- Multiple Wait nodes in one workflow: each resumes sequentially as the URL is called
- `Webhook Suffix` option appends a suffix to distinguish multiple Wait nodes — note: `$execution.resumeUrl` does NOT include the suffix automatically; append it manually before sending

**Auth options for the resume URL:** None / Basic Auth / Header Auth / JWT Auth (same as Webhook node auth).

**Respond options when resumed:** Immediately / When Last Node Finishes / Using 'Respond to Webhook' Node.

**Limit Wait Time:** optional timeout after which execution auto-resumes even if no webhook call arrives.

**Partial execution gotcha:** partial executions change the `$execution.resumeUrl`. Ensure the node that sends this URL runs in the same execution as the Wait node.

---

## Webhook security checklist

- [ ] Use **Header Auth** or **JWT Auth** for any webhook that receives sensitive data
- [ ] Set **IP(s) Whitelist** when the caller's IP is known and static
- [ ] Enable **Ignore Bots** to drop crawler traffic
- [ ] Use **HTTPS** — n8n Cloud is HTTPS by default; self-hosted requires a reverse proxy with TLS
- [ ] For Cloud: design long-running flows to respond immediately (Respond = Immediately) and poll separately — Cloudflare 100s timeout applies
- [ ] One path+method per workflow — no silent overwrites; conflicts raise an error
- [ ] If behind a reverse proxy, set `N8N_PROXY_HOPS` to the hop count so IP whitelisting works correctly

---

## Common patterns

### Webhook as a synchronous API endpoint

```
Webhook (Respond = When Last Node Finishes)
  → processing nodes
  → last node output returned to caller
```

### Async webhook with custom response

```
Webhook (Respond = Using 'Respond to Webhook' Node)
  → processing nodes
  → Respond to Webhook (Respond With = JSON, custom body)
  → (optional) more nodes that run after the response is sent
```

### Human-in-the-loop / approval flow

```
Webhook trigger → ... → Wait node (On Webhook Call)
  → send $execution.resumeUrl to approver (email / Slack)
  → approver calls URL → workflow resumes
```

### Binary file upload

1. Set HTTP Method = `POST`
2. Enable option **Binary Property** = `data` (or any name)
3. Access file: `$binary.data` in downstream nodes (e.g. Read Binary File, Move Binary Data)
