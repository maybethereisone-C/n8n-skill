# Google Vertex Chat Model — `n8n-nodes-langchain.lmChatGoogleVertex`
**Type** `n8n-nodes-langchain.lmChatGoogleVertex` · **typeVersion** 1 · **ai**
**What:** Sub-node that provides Google Vertex AI Gemini chat models for AI Agents and chains, authenticated via a GCP Service Account.
**Credentials:** `googleApi` (Service Account)
**Resources / Operations:** No discrete operations — exposes a chat LLM connection point.
**Key params & gotchas:**
- **Project ID**: GCP project; loaded dynamically but can be typed manually.
- **Model Name**: Not a dropdown — typed string (e.g. `gemini-1.5-flash-001`). Check [Google's model list](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models) for exact IDs.
- **Thinking Budget**: Unique to Vertex thinking models. `0` = disable thinking, `-1` = dynamic, empty = auto. Affects cost significantly.
- **Safety Settings**: Same adjustable harm-category filters as Gemini AI API.
- Requires Service Account credential (not API key) — distinct from the Google AI (Gemini) credential.
**Source:** n8n-nodes-langchain.lmchatgooglevertex.md  [doc-verified]
