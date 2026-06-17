# RabbitMQ — `n8n-nodes-base.rabbitmq`
**Type** `n8n-nodes-base.rabbitmq` · **action**
**What:** Send messages to and delete messages from RabbitMQ queues/exchanges.
**Credentials:** `rabbitmq`

## Resources / Operations
| Operation |
|-----------|
| Delete From Queue (ack/remove a message) |
| Send a Message to RabbitMQ |

## Key params & gotchas
- Supports use as an AI tool node.
- Send requires specifying the queue or exchange name and routing key; message body can be a string or JSON.
- "Delete From Queue" acknowledges (acks) a message, removing it from the queue — ensure the message has been processed before acking.
- A companion trigger node (`n8n-nodes-base.rabbitmqTrigger`) consumes messages reactively; use this action node for publishing or manual ack patterns.
- Credentials require AMQP connection details (host, port, vhost, user, password); TLS supported.
- Messages can include custom headers via Additional Fields.

**Source:** n8n-nodes-base.rabbitmq.md  [doc-verified]
