# Kafka — `n8n-nodes-base.kafka`
**Type** `n8n-nodes-base.kafka` · **typeVersion** 1 · **action**
**What:** Publish messages to Apache Kafka topics.
**Credentials:** `kafka` (brokers + optional SASL/SSL config) + optional `schemaRegistry` for Confluent Schema Registry encoding.

## Resources / Operations
| Resource | Operations |
|---|---|
| (flat) | Send Message |

## Key params & gotchas
- **Send Message** requires a **Topic** and **Message** (string or JSON). Use the **Headers** option to attach Kafka record headers.
- **Use Schema Registry**: enable to encode messages with Avro/Protobuf via an authenticated Confluent Schema Registry — requires a separate `schemaRegistry` credential (Confluent Cloud or self-hosted).
- For **consuming** messages (trigger), use the Kafka Trigger node (`n8n-nodes-base.kafkaTrigger`).
- Broker addresses must be reachable from the n8n instance; for Confluent Cloud use the bootstrap server format `pkc-xxxx.region.confluent.cloud:9092`.
- Message value can be any string; serialize objects to JSON with `{{ JSON.stringify($json) }}` before passing.

**Source:** n8n-nodes-base.kafka.md  [doc-verified]
