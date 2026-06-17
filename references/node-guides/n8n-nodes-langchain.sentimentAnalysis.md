# Sentiment Analysis — `n8n-nodes-langchain.sentimentAnalysis`
**Type** `n8n-nodes-langchain.sentimentAnalysis` · **ai**
**What:** Classifies input text into configurable sentiment categories using a connected LLM.
**Credentials:** None (LLM sub-node provides credentials).

**Key params & gotchas:**
- **Text to Analyze**: Expression referencing the input field (default expects `text`; change for chat triggers to `{{ $json.chatInput }}`).
- **Sentiment Categories** (option): Comma-separated list; defaults to `Positive, Neutral, Negative`. Customisable (e.g. `Very Positive, Positive, Neutral, Negative, Very Negative`).
- **Include Detailed Results** (option): Adds strength + confidence scores — these are LLM estimates, not calibrated probabilities.
- **System Prompt Template** (option): Uses `{categories}` placeholder; must keep it or categories won't be injected.
- **Enable Auto-Fixing** (option): Re-sends schema parse errors to the LLM to self-correct; adds latency.
- **Critical**: Set model temperature to 0 or near-0 for consistent, deterministic output. High temperature causes category drift across runs.
- Node outputs one branch per category + an "Other" branch if no match.

**Source:** n8n-nodes-langchain.sentimentanalysis.md  [doc-verified]
