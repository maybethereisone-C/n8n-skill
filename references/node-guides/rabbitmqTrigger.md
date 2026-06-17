# RabbitMQ Trigger — `n8n-nodes-base.rabbitmqTrigger`
**Type** `n8n-nodes-base.rabbitmqTrigger` · **typeVersion** 1 · **trigger**
**What:** Consumes messages from a RabbitMQ queue and fires the workflow for each message.
**Credentials:** `rabbitmq` (host, port, vhost, username, password, TLS options).
**Resources / Operations:**
| Trigger type | Notes |
|---|---|
| Queue consumer | Persistent AMQP consumer; one execution per message |

**Key params & gotchas:**
- **Queue** — must pre-exist unless your user has permission to declare queues.
- **Options → Content is Binary** — enable for non-text payloads (images, serialized objects).
- **Options → JSON Parse Body** — auto-parses JSON message bodies into structured objects.
- **Options → Only Content** — strips AMQP envelope metadata and passes only the message body downstream.
- Messages are acknowledged **after** n8n processes the execution; if the workflow errors the message may be requeued (depends on broker nack/reject config).
- Use in conjunction with the RabbitMQ action node (for publishing) to build request-reply patterns.

**Source:** n8n-nodes-base.rabbitmqtrigger.md  [doc-verified]
