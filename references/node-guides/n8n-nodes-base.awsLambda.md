# AWS Lambda — `n8n-nodes-base.awsLambda`
**Type** `n8n-nodes-base.awsLambda` · **action**
**What:** Invoke AWS Lambda functions synchronously from an n8n workflow.
**Credentials:** AWS credential (access key + secret, with Lambda invoke permissions).

## Resources / Operations
- Invoke a function

## Key params & gotchas
- **Invocation type** defaults to synchronous (RequestResponse) — the node waits for the function response. Async (Event) invocation is not exposed; use HTTP Request for that.
- The input payload is the current item's JSON, serialized and sent as the Lambda event body.
- Response from Lambda is parsed and output as JSON. If the Lambda returns a string, it's wrapped in a `body` field.
- **Function name** can be a name, ARN, or partial ARN. Aliases and versions are supported (e.g. `myFunction:PROD`).
- IAM permissions: `lambda:InvokeFunction` on the target function ARN.
- Timeout: n8n's HTTP timeout applies — for long-running functions consider async invocation + polling.

**Source:** n8n-nodes-base.awslambda.md  [doc-verified]
