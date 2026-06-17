# Alibaba Cloud Chat Model — `n8n-nodes-langchain.lmChatAlibabaCloud`
**Type** `n8n-nodes-langchain.lmChatAlibabaCloud` · **ai · sub-node**
**What:** Connects Alibaba Cloud conversational LLMs (Qwen family) to AI chains and agents.
**Credentials:** `alibabaCloudApi`.

**Key params & gotchas:**
- **Model**: Select from Alibaba Cloud Model Studio list. See [Alibaba Cloud Model Studio — Models](https://www.alibabacloud.com/help/en/model-studio/getting-started/models) for IDs.
- **Options**:
  - `Frequency Penalty` (default 0): Reduces verbatim repetition.
  - `Presence Penalty` (default 0): Encourages new topics.
  - `Sampling Temperature` (default 0.7): Lower = more deterministic; set near 0 for classification/extraction tasks.
  - `Top P` (default 1): Nucleus sampling — adjust either Temperature or Top P, not both.
  - `Maximum Number of Tokens` (default -1 = model limit): Cap output length.
  - `Response Format`: Text or structured formats.
  - `Timeout` (default 360000 ms): Raise for long-running completions.
  - `Max Retries` (default 2): Automatic retry on transient failures.

**Source:** n8n-nodes-langchain.lmchatalibabacloud.md  [doc-verified]
