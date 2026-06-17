# AMQP Sender — `n8n-nodes-base.amqp`
**Type** `n8n-nodes-base.amqp` · **action**
**What:** Send messages to an AMQP 1.0 message broker (Azure Service Bus, ActiveMQ, RabbitMQ with AMQP 1.0 plugin, etc.).
**Credentials:** AMQP credential (host, port, username, password, transport).

## Resources / Operations
- Send message

## Key params & gotchas
- Supports **AMQP 1.0 only** — not AMQP 0-9-1 (the RabbitMQ default). Use the RabbitMQ node for AMQP 0-9-1.
- Message body is serialized from the input item's JSON.
- For Azure Service Bus, set transport to `tls` and include the SAS token in the credential.
- n8n provides a separate AMQP Trigger node for consuming messages.

**Source:** n8n-nodes-base.amqp.md  [doc-verified]
