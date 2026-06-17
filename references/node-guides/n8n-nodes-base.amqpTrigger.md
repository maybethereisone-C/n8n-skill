# AMQP Trigger — `n8n-nodes-base.amqpTrigger`
**Type** `n8n-nodes-base.amqpTrigger` · **typeVersion** 1 · **trigger**

**What:** Consumes messages from an AMQP 1.0 message broker (e.g., Azure Service Bus, ActiveMQ, RabbitMQ with AMQP 1.0 plugin).

**Credentials:** `amqp` (hostname, port, username, password, transport).

**Resources / Operations:**
| Trigger type | What fires it |
|---|---|
| Queue/topic subscription | Each message received on the configured queue or topic |

**Key params & gotchas:**
- Supports **AMQP 1.0 only** — not compatible with AMQP 0-9-1 (classic RabbitMQ default). Use the RabbitMQ Trigger node for 0-9-1.
- Messages are acknowledged on receipt; failed workflow executions do not nack/requeue automatically.
- Companion app node: `n8n-nodes-base.amqp` (sender).

**Source:** n8n-nodes-base.amqptrigger.md  [doc-verified]
