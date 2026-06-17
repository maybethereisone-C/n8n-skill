# Kafka Trigger — `n8n-nodes-base.kafkaTrigger`
**Type** `n8n-nodes-base.kafkaTrigger` · **typeVersion** 1 · **trigger**
**What:** Consumes messages from one or more Kafka topics and fires the workflow for each message received.
**Credentials:** `kafkaApi` (broker list, SASL auth optional); optionally `schemaRegistry` for Confluent Schema Registry decode.
**Resources / Operations:**
| Trigger type | Notes |
|---|---|
| Topic subscription | Persistent consumer; one execution per message batch |

**Key params & gotchas:**
- **Topics** — comma-separated list of topic names.
- **Group ID** — consumer group; reusing the same group across workflows means only one consumes each partition.
- **Use Schema Registry** — enable when messages are Avro/Protobuf-encoded via a Confluent Schema Registry; requires a separate `schemaRegistry` credential.
- **Allow Topic Creation** — creates the topic if it doesn't exist; needs broker `auto.create.topics.enable`.
- **Session Timeout / Heartbeat Interval** — lower values detect failures faster but increase rebalances.
- Messages are committed after n8n processes them; if the workflow errors the offset may not advance — configure DLQ logic accordingly.
- Does **not** support manual poll interval; it is a long-running listener, not polling.

**Source:** n8n-nodes-base.kafkatrigger.md  [doc-verified]
