# Google Gemini — `n8n-nodes-langchain.googlegemini`
**Type** `n8n-nodes-langchain.googlegemini` · **typeVersion** 1 · **action/ai**
**What:** Call Google Gemini models for text completions, audio/video/image/document analysis, image generation and editing, video generation, and RAG file search store management.
**Credentials:** `googleAIApi` (API key from Google AI Studio or Google Cloud).

## Resources / Operations
| Resource | Operations |
|---|---|
| Audio | Analyze Audio, Transcribe a Recording |
| Document | Analyze Document |
| File Search | Create Store, Delete Store, List Stores, Upload to Store |
| Image | Analyze Image, Generate an Image, Edit Image |
| Media File | Upload Media File |
| Text | Message a Model |
| Video | Analyze Video, Generate a Video, Download Video |

## Key params & gotchas
- **File Search Store** operations implement RAG — upload documents to a store, then reference the store ID in Text → Message a Model for grounded responses.
- **Generate a Video / Download Video** are two-step: Generate returns a URL (async generation), then Download fetches the binary. Use Download Video with the URL from the generation step.
- **Edit Image** accepts one or more images plus a text prompt describing the desired edits — multimodal editing.
- For LangChain sub-node use (as LLM for AI Agent), use `n8n-nodes-langchain.lmChatGoogleGemini` (embeddings) or the Gemini-specific LLM sub-node instead.
- Google AI Studio API key works for prototyping; production workloads should use Vertex AI credentials.

**Source:** n8n-nodes-langchain.googlegemini.md  [doc-verified]
