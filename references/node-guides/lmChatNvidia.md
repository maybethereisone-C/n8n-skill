# NVIDIA Nemotron Chat Model — `n8n-nodes-langchain.lmChatNvidia`
**Type** `n8n-nodes-langchain.lmChatNvidia` · **typeVersion** 1 · **ai**
**What:** Sub-node that provides NVIDIA Nemotron models (cloud via build.nvidia.com or self-hosted NIM) for AI Agents and chains.
**Credentials:** `nvidiaNimApi`
**Resources / Operations:** No discrete operations — exposes a chat LLM connection point.
**Key params & gotchas:**
- **Model**: Dynamically loaded from the endpoint in credentials; falls back to a curated static list if the endpoint is unreachable.
- Supports both `build.nvidia.com` (cloud) and self-hosted **NVIDIA Inference Microservices (NIM)** — credential endpoint controls which.
- **Response Format JSON**: When using JSON mode, the word `json` must appear in the prompt (OpenAI spec requirement; NVIDIA API is OpenAI-compatible).
- **Max Tokens `-1`**: Uses model default — safe for most cases.
**Source:** n8n-nodes-langchain.lmchatnvidia.md  [doc-verified]
