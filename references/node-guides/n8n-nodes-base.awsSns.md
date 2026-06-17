# AWS SNS — `n8n-nodes-base.awsSns`
**Type** `n8n-nodes-base.awsSns` · **action**
**What:** Publish messages to AWS SNS topics (fan-out to SQS, Lambda, HTTP endpoints, email, SMS).
**Credentials:** AWS credential (access key + secret, with SNS permissions).

## Resources / Operations
- Publish a message to a topic

## Key params & gotchas
- Single operation: publish. Topic ARN is required.
- Message attributes can be added for filtering by SNS filter policies on subscriptions.
- For SMS direct send (without topic), use the HTTP Request node with SNS Publish API directly.
- IAM permissions: `sns:Publish` on the target topic ARN.
- n8n provides a separate SNS Trigger node for receiving SNS notifications via webhook.

**Source:** n8n-nodes-base.awssns.md  [doc-verified]
