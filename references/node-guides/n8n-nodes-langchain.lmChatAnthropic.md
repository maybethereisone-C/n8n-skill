# Anthropic Chat Model — `n8n-nodes-langchain.lmChatAnthropic`
**Type** `n8n-nodes-langchain.lmChatAnthropic` · **ai · sub-node**
**What:** Connects Anthropic Claude models to AI chains and agents.
**Credentials:** `anthropicApi`.

**Key params & gotchas:**
- **Model**: `Claude` or `Claude Instant` families. See [Anthropic model docs](https://docs.anthropic.com/claude/reference/selecting-a-model) for current model IDs — the UI list may not reflect the latest models; switch to Expression mode to enter a specific ID like `claude-opus-4-5`.
- **Options**:
  - `Maximum Number of Tokens`: Sets max completion length.
  - `Sampling Temperature`: Higher = more creative/varied; lower = deterministic. Use near 0 for structured output tasks.
  - `Top K`: Limits token choices at each step.
  - `Top P`: Nucleus sampling. Adjust either Temperature or Top P, not both.
- Most capable Claude models (Opus) are best for complex reasoning; Haiku/Sonnet for speed-sensitive agent tool calls.

**Source:** n8n-nodes-langchain.lmchatanthropic.md  [doc-verified]
