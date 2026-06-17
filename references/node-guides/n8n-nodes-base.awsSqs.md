# AWS SQS — `n8n-nodes-base.awsSqs`
**Type** `n8n-nodes-base.awsSqs` · **action**
**What:** Send messages to AWS SQS queues (standard and FIFO).
**Credentials:** AWS credential (access key + secret, with SQS permissions).

## Resources / Operations
- Send a message to a queue

## Key params & gotchas
- Single operation: send. Queue URL is required (not queue name).
- For **FIFO queues**, `MessageGroupId` is mandatory — without it the request fails. `MessageDeduplicationId` is required if content-based deduplication is disabled on the queue.
- Message body is the JSON of the current item by default.
- Delay seconds (0–900) can be set per message to defer delivery.
- IAM permissions: `sqs:SendMessage` on the target queue ARN.
- For consuming (polling) messages, use the HTTP Request node with ReceiveMessage API or AWS triggers.

**Source:** n8n-nodes-base.awssqs.md  [doc-verified]
