# Template Catalog (all source workflows analyzed)

> Auto-parsed from `/Users/tew/Desktop/intern/n8n_templates` (24 workflow JSONs). Shows trigger + every node type each uses. Bundled & cleaned subset lives in `templates/` (see templates/README.md). Regenerate: `python3 scripts/index-templates.py`.

## Business-domain taxonomy (Zie619/n8n-workflows)

`references/template-categories/` contains two JSON files sourced from Zie619/n8n-workflows (4,343 workflows, FTS search app at zie619.github.io/n8n-workflows):

- **`unique_categories.json`** — 16-category business-domain taxonomy used to classify all 2,057+ workflows in that corpus.
- **`search_categories.json`** — per-workflow category labels for browsing and filtering the bundled templates by domain.

Use these for "find me a template that does X in category Y" lookups before reaching for keyword search.

| Template | nodes | conns | trigger | node types used |
|---|---|---|---|---|
| `1) RAG Pipeline & Chatbot.json` | 12 | 9 | chatTrigger, googleDriveTrigger | agent, chatTrigger, documentDefaultDataLoader, embeddingsOpenAi, googleDrive, googleDriveTrigger, lmChatOpenRouter, stickyNote, textSplitterRecursiveCharacterTextSplitter, vectorStorePinecone |
| `10) Product Videos.json` | 24 | 13 | formTrigger | agent, convertToFile, formTrigger, gmail, googleDrive, httpRequest, if, lmChatOpenRouter, stickyNote, wait |
| `11) RAG Workflow vs RAG Agent.json` | 23 | 16 | gmailTrigger, manualTrigger | agent, aggregate, documentDefaultDataLoader, embeddingsOpenAi, filter, gmail, gmailTool, gmailTrigger, googleDrive, lmChatGoogleGemini, manualTrigger, openAi, stickyNote, textSplitterRecursiveCharacterTextSplitter, vectorStorePinecone |
| `12) Technical Analyst Agent vs Workflow.json` | 23 | 15 | executeWorkflowTrigger, telegramTrigger | agent, executeWorkflowTrigger, httpRequest, lmChatOpenAi, openAi, set, stickyNote, telegram, telegramTrigger, toolWorkflow |
| `13) First AI Agent.json` | 8 | 6 | chatTrigger | agent, chatTrigger, gmailTool, googleCalendarTool, googleSheetsTool, lmChatOpenRouter, memoryBufferWindow, stickyNote |
| `14) Supabase Postgres.json` | 15 | 10 | chatTrigger, manualTrigger | agent, chatTrigger, documentDefaultDataLoader, embeddingsOpenAi, googleDrive, lmChatOpenAi, manualTrigger, memoryPostgresChat, stickyNote, textSplitterRecursiveCharacterTextSplitter, vectorStoreSupabase |
| `15) Orchestrator Architecture.json` | 46 | 36 | telegramTrigger | agent, airtableTool, gmailTool, googleCalendarTool, lmChatGoogleGemini, lmChatOpenAi, lmChatOpenRouter, memoryBufferWindow, openAi, set, stickyNote, switch, telegram, telegramTrigger, toolCalculator, toolHttpRequest, toolThink, toolWorkflow |
| `16) Prompt Chaining.json` | 10 | 9 | chatTrigger | agent, chatTrigger, googleDocs, lmChatAnthropic, lmChatDeepSeek, lmChatGoogleGemini, lmChatOpenAi, stickyNote |
| `17) Routing.json` | 14 | 9 | gmailTrigger | agent, gmail, gmailTool, gmailTrigger, lmChatOpenAi, stickyNote, telegramTool, textClassifier |
| `18) Parallelization.json` | 13 | 10 | chatTrigger | agent, aggregate, chatTrigger, googleDocs, lmChatDeepSeek, lmChatOpenAi, merge, stickyNote |
| `19) Evaluator Optimizer.json` | 10 | 7 | chatTrigger | agent, chatTrigger, googleDocs, if, lmChatDeepSeek, lmChatOpenAi, set, stickyNote |
| `2) Customer Support Workflow.json` | 11 | 8 | gmailTrigger | agent, embeddingsOpenAi, gmail, gmailTrigger, lmChatOpenAi, lmChatOpenRouter, noOp, stickyNote, textClassifier, vectorStorePinecone |
| `20) HITL Example Flows.json` | 34 | 15 | telegramTrigger | agent, if, lmChatOpenRouter, set, stickyNote, telegram, telegramTrigger, textClassifier, toolHttpRequest, twitter |
| `21) Error Logger.json` | 5 | 1 | errorTrigger | errorTrigger, googleSheets, slack, stickyNote |
| `22) Dynamic Brain.json` | 43 | 21 | chatTrigger, manualTrigger, slackTrigger | agent, airtableTool, chatTrigger, documentDefaultDataLoader, embeddingsOpenAi, gmailTool, googleCalendarTool, googleDrive, googleSheets, lmChatOpenRouter, manualTrigger, slack, slackTrigger, stickyNote, textSplitterRecursiveCharacterTextSplitter, toolHttpRequest, vectorStoreSupabase |
| `23) Voice Email Agent.json` | 6 | 5 | — | agent, gmailTool, googleSheetsTool, lmChatOpenAi, respondToWebhook, webhook |
| `3) LinkedIn Workflow.json` | 7 | 5 | manualTrigger | agent, googleSheets, httpRequest, lmChatOpenRouter, manualTrigger, stickyNote |
| `4) Invoice Workflow.json` | 9 | 8 | googleDriveTrigger | extractFromFile, gmail, googleDrive, googleDriveTrigger, googleSheets, informationExtractor, lmChatGoogleGemini, noOp, openAi |
| `5) API Calls in n8n.json` | 12 | 4 | chatTrigger | agent, chatTrigger, httpRequest, httpRequestTool, lmChatOpenRouter, openWeatherMap, set, stickyNote |
| `6) Perplexity.json` | 4 | 2 | manualTrigger | httpRequest, manualTrigger, set, stickyNote |
| `7) Firecrawl Extract Template.json` | 9 | 6 | manualTrigger | httpRequest, if, manualTrigger, set, stickyNote, wait |
| `8) Apify.json` | 9 | 2 | — | httpRequest, stickyNote, wait |
| `9) OpenAI Image Gen.json` | 20 | 9 | formTrigger, manualTrigger | agent, convertToFile, formTrigger, gmail, httpRequest, linkedIn, lmChatOpenRouter, manualTrigger, stickyNote, toolHttpRequest |
| `AI-Mention-Tracker-Simple.json` | 5 | 4 | manualTrigger | googleSheets, httpRequest, manualTrigger, set |
