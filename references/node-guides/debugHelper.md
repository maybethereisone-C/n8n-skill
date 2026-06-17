# Debug Helper — `n8n-nodes-base.debugHelper`

**Type** `n8n-nodes-base.debugHelper` · **typeVersion** 1 · **core**

**What:** Testing utility — throws errors, simulates OOM, or generates synthetic random datasets for workflow development and QA.

**Credentials:** None.

**Resources / Operations:**

| Category | What it does |
|----------|-------------|
| Do Nothing | Passes items through unchanged |
| Throw Error | Throws NodeApiError, NodeOperationError, or generic Error with a custom message |
| Out Of Memory | Allocates a specified memory size to simulate OOM |
| Generate Random Data | Generates N items of fake data (address, email, UUID, user data, coordinates, credit card, IPv4/IPv6, MAC, URL, nanoid, version) |

**Key params & gotchas:**
- **Generate Random Data → Seed**: set a fixed seed for reproducible fake data across runs — leave blank for truly random data each time.
- **Output as Single Array**: when on, all generated items are wrapped in one array field rather than emitted as separate items.
- **Nanoid**: requires specifying both alphabet and length.
- Use **Throw Error** to test error workflow handling and the Error Trigger node without needing a real failure condition.
- **Out Of Memory** is for stress-testing n8n resource limits — use with caution in production environments.

**Source:** n8n-nodes-base.debughelper.md  [doc-verified]
