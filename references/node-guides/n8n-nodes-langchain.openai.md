# OpenAI — `n8n-nodes-langchain.openAi`
**Type** `n8n-nodes-langchain.openAi` · **typeVersion** 1 (V1) / **2** (V2, n8n ≥1.117.0) · **action/ai**
**What:** Full OpenAI integration — text completions (Chat API + Responses API), image generation/analysis/editing, audio TTS/transcription/translation, file management, video generation, conversation management, and (V1 only) Assistant CRUD.
**Credentials:** `openAiApi` (OpenAI API key).

## Resources / Operations

### Text
| Operation | API Used | Notes |
|---|---|---|
| Generate a Chat Completion | Chat Completions API | Multi-turn, tool connectors supported |
| Generate a Model Response | Responses API (V2+) | Supports built-in tools: Web Search, MCP Servers, File Search, Code Interpreter |
| Classify Text for Violations | Moderation API | Returns `flagged`, `categories`, `category_scores` |

### Image
| Operation | Notes |
|---|---|
| Analyze Image | URL(s) or binary file(s); `detail` controls token usage |
| Generate an Image | DALL-E 2 / DALL-E 3; quality, resolution, style options |
| Edit an Image | DALL-E 2 + gpt-image-1; up to 16 images, mask support; compression/format for gpt-image-1 |

### Audio
| Operation | Notes |
|---|---|
| Generate Audio | TTS-1 / TTS-1-HD; 6 output formats; max 4096 chars |
| Transcribe a Recording | Whisper-1; max 25 MB; specify ISO-639-1 language for better accuracy |
| Translate a Recording | Whisper-1; translates to English only; max 25 MB |

### File
| Operation | Notes |
|---|---|
| Upload a File | Max 512 MB or 2M tokens; purpose: Assistants or Fine-Tune |
| List Files | Filter by purpose |
| Delete a File | By ID or dropdown |

### Video (V2+)
| Operation | Notes |
|---|---|
| Generate a Video | Sora-2 / Sora-2-Pro; up to 25s; optional image reference; `waitTimeout` defaults to 300s |

### Conversation (V2+)
| Operation | Notes |
|---|---|
| Create a Conversation | Up to 16 metadata key-value pairs |
| Get a Conversation | By conversation ID |
| Update a Conversation | Update metadata |
| Remove a Conversation | By conversation ID |

### Assistant (V1 only — deprecated in V2)
- Create, Delete, List, Message, Update an Assistant (uses Assistants API, deprecated by OpenAI)

## Key params & gotchas
- **V2 (n8n ≥1.117.0) removes Assistant operations** in favor of Responses API Conversations; upgrade path is documented by OpenAI.
- **Generate a Model Response** supports `conversationId` OR `previousResponseId` for stateful context — not both simultaneously.
- **Reasoning** parameter (V2 Responses API) controls effort level and can return a reasoning summary for debugging.
- **Background mode** (V2) enables long-running async responses; combine with Conversation ID to retrieve results.
- **JSON output**: "Output Content as JSON" on Chat Completion requires GPT-4 Turbo or GPT-3.5-turbo ≥ gpt-3.5-turbo-1106.
- Tool connectors: Chat Completion and Generate a Model Response support n8n sub-node tools, making this node a cluster root node.
- **Don't set both Temperature and Top P** — OpenAI recommends adjusting only one.
- Transcription/Translation max file size is 25 MB — pre-compress large audio files.
- Rate limits: use exponential backoff; see n8n's [Handling rate limits](/integrations/builtin/rate-limits.md).

**Source:** n8n-nodes-langchain.openai/index.md + sub-pages  [doc-verified]
