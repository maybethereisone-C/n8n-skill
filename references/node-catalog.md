# n8n Built-in Node Catalog (full per-node schemas)

> Source-extracted from n8n v2.26.0 (540 nodes: 436 core + 104 AI/LangChain). Each row links to a per-node schema in `nodes/` (resources, operations, full parameter list). Regenerate: `python3 scripts/extract-schemas.py`. Best-effort TS parse — for nested/imported props or exact typeVersion edge cases, confirm via n8n-mcp `get_node`. Prefer the dedicated node over `httpRequest` (node-selection.md).

## Core nodes (`n8n-nodes-base.*`)

| Node | type | maxVer | trig | #ops | #params | schema |
|---|---|---|---|---|---|---|
| Action Network | `n8n-nodes-base.actionNetwork` | 1 |  | 6 | 1 | [schema](nodes/n8n-nodes-base.actionNetwork.md) |
| ActiveCampaign | `n8n-nodes-base.activeCampaign` | 1 |  | 11 | 3 | [schema](nodes/n8n-nodes-base.activeCampaign.md) |
| ActiveCampaign Trigger | `n8n-nodes-base.activeCampaignTrigger` | 1 | ✓ | 11 | 3 | [schema](nodes/n8n-nodes-base.activeCampaignTrigger.md) |
| Acuity Scheduling Trigger | `n8n-nodes-base.acuitySchedulingTrigger` | 1 | ✓ | 0 | 3 | [schema](nodes/n8n-nodes-base.acuitySchedulingTrigger.md) |
| Adalo | `n8n-nodes-base.adalo` | 1 |  | 6 | 3 | [schema](nodes/n8n-nodes-base.adalo.md) |
| Affinity | `n8n-nodes-base.affinity` | 1 |  | 5 | 2 | [schema](nodes/n8n-nodes-base.affinity.md) |
| Affinity Trigger | `n8n-nodes-base.affinityTrigger` | 1 | ✓ | 5 | 2 | [schema](nodes/n8n-nodes-base.affinityTrigger.md) |
| Aggregate | `n8n-nodes-base.aggregate` | 1 |  | 0 | 7 | [schema](nodes/n8n-nodes-base.aggregate.md) |
| Agile CRM | `n8n-nodes-base.agileCrm` | 1 |  | 5 | 1 | [schema](nodes/n8n-nodes-base.agileCrm.md) |
| AI Transform | `n8n-nodes-base.aiTransform` | 1 |  | 0 | 1 | [schema](nodes/n8n-nodes-base.aiTransform.md) |
| Airtable | `n8n-nodes-base.airtable` | 2.2 |  | 12 | 25 | [schema](nodes/n8n-nodes-base.airtable.md) |
| Airtable Trigger | `n8n-nodes-base.airtableTrigger` | 2.2 | ✓ | 12 | 25 | [schema](nodes/n8n-nodes-base.airtableTrigger.md) |
| Airtop | `n8n-nodes-base.airtop` | 1.1 |  | 22 | 1 | [schema](nodes/n8n-nodes-base.airtop.md) |
| AMQP Sender | `n8n-nodes-base.amqp` | 1 |  | 0 | 5 | [schema](nodes/n8n-nodes-base.amqp.md) |
| AMQP Trigger | `n8n-nodes-base.amqpTrigger` | 1 | ✓ | 0 | 5 | [schema](nodes/n8n-nodes-base.amqpTrigger.md) |
| APITemplate.io | `n8n-nodes-base.apiTemplateIo` | 1 |  | 2 | 14 | [schema](nodes/n8n-nodes-base.apiTemplateIo.md) |
| Asana | `n8n-nodes-base.asana` | 1 |  | 9 | 60 | [schema](nodes/n8n-nodes-base.asana.md) |
| Asana Trigger | `n8n-nodes-base.asanaTrigger` | 1 | ✓ | 9 | 60 | [schema](nodes/n8n-nodes-base.asanaTrigger.md) |
| Autopilot | `n8n-nodes-base.autopilot` | 1 |  | 8 | 2 | [schema](nodes/n8n-nodes-base.autopilot.md) |
| Autopilot Trigger | `n8n-nodes-base.autopilotTrigger` | 1 | ✓ | 8 | 2 | [schema](nodes/n8n-nodes-base.autopilotTrigger.md) |
| AWS Certificate Manager | `n8n-nodes-base.awsCertificateManager` | 1 |  | 5 | 1 | [schema](nodes/n8n-nodes-base.awsCertificateManager.md) |
| AWS Cognito | `n8n-nodes-base.awsCognito` | 1 |  | 11 | 1 | [schema](nodes/n8n-nodes-base.awsCognito.md) |
| AWS Comprehend | `n8n-nodes-base.awsComprehend` | 1 |  | 3 | 6 | [schema](nodes/n8n-nodes-base.awsComprehend.md) |
| AWS DynamoDB | `n8n-nodes-base.awsDynamoDb` | 1 |  | 4 | 1 | [schema](nodes/n8n-nodes-base.awsDynamoDb.md) |
| AWS ELB | `n8n-nodes-base.awsElb` | 1 |  | 6 | 1 | [schema](nodes/n8n-nodes-base.awsElb.md) |
| AWS IAM | `n8n-nodes-base.awsIam` | 1 |  | 7 | 1 | [schema](nodes/n8n-nodes-base.awsIam.md) |
| AWS Lambda | `n8n-nodes-base.awsLambda` | 2 |  | 31 | 72 | [schema](nodes/n8n-nodes-base.awsLambda.md) |
| AWS Rekognition | `n8n-nodes-base.awsRekognition` | 1 |  | 1 | 8 | [schema](nodes/n8n-nodes-base.awsRekognition.md) |
| AWS SES | `n8n-nodes-base.awsSes` | 1 |  | 7 | 34 | [schema](nodes/n8n-nodes-base.awsSes.md) |
| AWS SNS | `n8n-nodes-base.awsSns` | 2 |  | 31 | 72 | [schema](nodes/n8n-nodes-base.awsSns.md) |
| AWS SNS Trigger | `n8n-nodes-base.awsSnsTrigger` | 2 | ✓ | 31 | 72 | [schema](nodes/n8n-nodes-base.awsSnsTrigger.md) |
| AWS SQS | `n8n-nodes-base.awsSqs` | 1 |  | 1 | 7 | [schema](nodes/n8n-nodes-base.awsSqs.md) |
| AWS Textract | `n8n-nodes-base.awsTextract` | 1 |  | 1 | 3 | [schema](nodes/n8n-nodes-base.awsTextract.md) |
| AWS Transcribe | `n8n-nodes-base.awsTranscribe` | 1 |  | 4 | 12 | [schema](nodes/n8n-nodes-base.awsTranscribe.md) |
| AwsS3 | `n8n-nodes-base.awsS3` | 2 |  | 7 | 1 | [schema](nodes/n8n-nodes-base.awsS3.md) |
| Azure Cosmos DB | `n8n-nodes-base.azureCosmosDb` | 2 |  | 7 | 1 | [schema](nodes/n8n-nodes-base.azureCosmosDb.md) |
| Azure Storage | `n8n-nodes-base.azureStorage` | 1 |  | 32 | 2 | [schema](nodes/n8n-nodes-base.azureStorage.md) |
| Bannerbear | `n8n-nodes-base.bannerbear` | 1 |  | 3 | 1 | [schema](nodes/n8n-nodes-base.bannerbear.md) |
| Baserow | `n8n-nodes-base.baserow` | 1.1 |  | 8 | 3 | [schema](nodes/n8n-nodes-base.baserow.md) |
| Beeminder | `n8n-nodes-base.beeminder` | 1 |  | 12 | 29 | [schema](nodes/n8n-nodes-base.beeminder.md) |
| Bitbucket Trigger | `n8n-nodes-base.bitbucketTrigger` | 1.1 | ✓ | 0 | 6 | [schema](nodes/n8n-nodes-base.bitbucketTrigger.md) |
| Bitly | `n8n-nodes-base.bitly` | 1 |  | 3 | 2 | [schema](nodes/n8n-nodes-base.bitly.md) |
| Bitwarden | `n8n-nodes-base.bitwarden` | 1 |  | 9 | 1 | [schema](nodes/n8n-nodes-base.bitwarden.md) |
| Box | `n8n-nodes-base.box` | 1 |  | 9 | 4 | [schema](nodes/n8n-nodes-base.box.md) |
| Box Trigger | `n8n-nodes-base.boxTrigger` | 1 | ✓ | 9 | 4 | [schema](nodes/n8n-nodes-base.boxTrigger.md) |
| Brandfetch | `n8n-nodes-base.Brandfetch` | 1 |  | 5 | 5 | [schema](nodes/n8n-nodes-base.Brandfetch.md) |
| Brevo | `n8n-nodes-base.sendInBlue` | 1 |  | 9 | 3 | [schema](nodes/n8n-nodes-base.sendInBlue.md) |
| Brevo Trigger | `n8n-nodes-base.sendInBlueApi` | 1 |  | 9 | 3 | [schema](nodes/n8n-nodes-base.sendInBlueApi.md) |
| Bubble | `n8n-nodes-base.bubble` | 1 |  | 5 | 1 | [schema](nodes/n8n-nodes-base.bubble.md) |
| Cal.com Trigger | `n8n-nodes-base.calTrigger` | 2 | ✓ | 0 | 3 | [schema](nodes/n8n-nodes-base.calTrigger.md) |
| Calendly Trigger | `n8n-nodes-base.calendlyTrigger` | 2 | ✓ | 0 | 3 | [schema](nodes/n8n-nodes-base.calendlyTrigger.md) |
| Chargebee | `n8n-nodes-base.chargebee` | 1 |  | 13 | 12 | [schema](nodes/n8n-nodes-base.chargebee.md) |
| Chargebee Trigger | `n8n-nodes-base.chargebeeTrigger` | 1 | ✓ | 13 | 12 | [schema](nodes/n8n-nodes-base.chargebeeTrigger.md) |
| Check Credential Status | `n8n-nodes-base.dynamicCredentialCheck` | 1 |  | 0 | 0 | [schema](nodes/n8n-nodes-base.dynamicCredentialCheck.md) |
| CircleCI | `n8n-nodes-base.circleCi` | 1 |  | 3 | 1 | [schema](nodes/n8n-nodes-base.circleCi.md) |
| Clearbit | `n8n-nodes-base.clearbit` | 1 |  | 2 | 1 | [schema](nodes/n8n-nodes-base.clearbit.md) |
| ClickUp | `n8n-nodes-base.clickUp` | 1 |  | 12 | 5 | [schema](nodes/n8n-nodes-base.clickUp.md) |
| ClickUp Trigger | `n8n-nodes-base.clickUpTrigger` | 1 | ✓ | 12 | 5 | [schema](nodes/n8n-nodes-base.clickUpTrigger.md) |
| Clockify | `n8n-nodes-base.clockify` | 1 |  | 5 | 4 | [schema](nodes/n8n-nodes-base.clockify.md) |
| Clockify Trigger | `n8n-nodes-base.clockifyTrigger` | 1 | ✓ | 5 | 4 | [schema](nodes/n8n-nodes-base.clockifyTrigger.md) |
| Cloudflare | `n8n-nodes-base.cloudflare` | 1 |  | 4 | 1 | [schema](nodes/n8n-nodes-base.cloudflare.md) |
| Cockpit | `n8n-nodes-base.cockpit` | 1 |  | 5 | 1 | [schema](nodes/n8n-nodes-base.cockpit.md) |
| Coda | `n8n-nodes-base.coda` | 1.1 |  | 14 | 1 | [schema](nodes/n8n-nodes-base.coda.md) |
| Code | `n8n-nodes-base.code` | 2 |  | 0 | 2 | [schema](nodes/n8n-nodes-base.code.md) |
| CoinGecko | `n8n-nodes-base.coinGecko` | 1 |  | 8 | 1 | [schema](nodes/n8n-nodes-base.coinGecko.md) |
| Compare Datasets | `n8n-nodes-base.compareDatasets` | 2.3 |  | 0 | 7 | [schema](nodes/n8n-nodes-base.compareDatasets.md) |
| Compression | `n8n-nodes-base.compression` | 1.1 |  | 2 | 8 | [schema](nodes/n8n-nodes-base.compression.md) |
| Contentful | `n8n-nodes-base.contentful` | 1 |  | 2 | 2 | [schema](nodes/n8n-nodes-base.contentful.md) |
| Convert to File | `n8n-nodes-base.convertToFile` | 1.1 |  | 10 | 1 | [schema](nodes/n8n-nodes-base.convertToFile.md) |
| Convert to/from binary data | `n8n-nodes-base.moveBinaryData` | 1.1 |  | 0 | 6 | [schema](nodes/n8n-nodes-base.moveBinaryData.md) |
| ConvertKit | `n8n-nodes-base.convertKit` | 1 |  | 7 | 7 | [schema](nodes/n8n-nodes-base.convertKit.md) |
| ConvertKit Trigger | `n8n-nodes-base.convertKitTrigger` | 1 | ✓ | 7 | 7 | [schema](nodes/n8n-nodes-base.convertKitTrigger.md) |
| Copper | `n8n-nodes-base.copper` | 1 |  | 5 | 2 | [schema](nodes/n8n-nodes-base.copper.md) |
| Copper Trigger | `n8n-nodes-base.copperTrigger` | 1 | ✓ | 5 | 2 | [schema](nodes/n8n-nodes-base.copperTrigger.md) |
| Cortex | `n8n-nodes-base.cortex` | 1 |  | 3 | 1 | [schema](nodes/n8n-nodes-base.cortex.md) |
| CrateDB | `n8n-nodes-base.crateDb` | 1 |  | 3 | 11 | [schema](nodes/n8n-nodes-base.crateDb.md) |
| Cron | `n8n-nodes-base.cron` | 1 |  | 0 | 2 | [schema](nodes/n8n-nodes-base.cron.md) |
| Crypto | `n8n-nodes-base.crypto` | 2 |  | 0 | 14 | [schema](nodes/n8n-nodes-base.crypto.md) |
| Currents | `n8n-nodes-base.currents` | 1 |  | 14 | 3 | [schema](nodes/n8n-nodes-base.currents.md) |
| Currents Trigger | `n8n-nodes-base.currentsTrigger` | 1 | ✓ | 14 | 3 | [schema](nodes/n8n-nodes-base.currentsTrigger.md) |
| Customer Datastore (n8n training) | `n8n-nodes-base.n8nTrainingCustomerDatastore` | 1 |  | 2 | 3 | [schema](nodes/n8n-nodes-base.n8nTrainingCustomerDatastore.md) |
| Customer Messenger (n8n training) | `n8n-nodes-base.n8nTrainingCustomerMessenger` | 1 |  | 0 | 2 | [schema](nodes/n8n-nodes-base.n8nTrainingCustomerMessenger.md) |
| Customer.io | `n8n-nodes-base.customerIo` | 1 |  | 9 | 2 | [schema](nodes/n8n-nodes-base.customerIo.md) |
| Customer.io Trigger | `n8n-nodes-base.customerIoTrigger` | 1 | ✓ | 9 | 2 | [schema](nodes/n8n-nodes-base.customerIoTrigger.md) |
| Data table | `n8n-nodes-base.dataTable` | 1.1 |  | 0 | 1 | [schema](nodes/n8n-nodes-base.dataTable.md) |
| Databricks | `n8n-nodes-base.databricks` | 1 |  | 36 | 2 | [schema](nodes/n8n-nodes-base.databricks.md) |
| Date & Time | `n8n-nodes-base.dateTime` | 2 |  | 9 | 10 | [schema](nodes/n8n-nodes-base.dateTime.md) |
| DebugHelper | `n8n-nodes-base.debugHelper` | 1 |  | 0 | 10 | [schema](nodes/n8n-nodes-base.debugHelper.md) |
| DeepL | `n8n-nodes-base.deepL` | 1 |  | 1 | 2 | [schema](nodes/n8n-nodes-base.deepL.md) |
| Demio | `n8n-nodes-base.demio` | 1 |  | 3 | 1 | [schema](nodes/n8n-nodes-base.demio.md) |
| DHL | `n8n-nodes-base.dhl` | 1 |  | 1 | 4 | [schema](nodes/n8n-nodes-base.dhl.md) |
| Discord | `n8n-nodes-base.discord` | 2 |  | 11 | 5 | [schema](nodes/n8n-nodes-base.discord.md) |
| Discourse | `n8n-nodes-base.discourse` | 1 |  | 7 | 1 | [schema](nodes/n8n-nodes-base.discourse.md) |
| Disqus | `n8n-nodes-base.disqus` | 1 |  | 4 | 16 | [schema](nodes/n8n-nodes-base.disqus.md) |
| Drift | `n8n-nodes-base.drift` | 1 |  | 5 | 2 | [schema](nodes/n8n-nodes-base.drift.md) |
| Dropbox | `n8n-nodes-base.dropbox` | 1 |  | 8 | 27 | [schema](nodes/n8n-nodes-base.dropbox.md) |
| Dropcontact | `n8n-nodes-base.dropcontact` | 1 |  | 2 | 7 | [schema](nodes/n8n-nodes-base.dropcontact.md) |
| E-goi | `n8n-nodes-base.egoi` | 1 |  | 4 | 14 | [schema](nodes/n8n-nodes-base.egoi.md) |
| E2E Test | `n8n-nodes-base.e2eTest` | 1 |  | 3 | 6 | [schema](nodes/n8n-nodes-base.e2eTest.md) |
| Edit Image | `n8n-nodes-base.editImage` | 1 |  | 8 | 4 | [schema](nodes/n8n-nodes-base.editImage.md) |
| Elastic Security | `n8n-nodes-base.elasticSecurity` | 1 |  | 8 | 1 | [schema](nodes/n8n-nodes-base.elasticSecurity.md) |
| Elasticsearch | `n8n-nodes-base.elasticsearch` | 1 |  | 5 | 1 | [schema](nodes/n8n-nodes-base.elasticsearch.md) |
| Email Trigger (IMAP) | `n8n-nodes-base.emailReadImap` | 2.1 |  | 0 | 6 | [schema](nodes/n8n-nodes-base.emailReadImap.md) |
| Emelia | `n8n-nodes-base.emelia` | 1 |  | 8 | 3 | [schema](nodes/n8n-nodes-base.emelia.md) |
| Emelia Trigger | `n8n-nodes-base.emeliaTrigger` | 1 | ✓ | 8 | 3 | [schema](nodes/n8n-nodes-base.emeliaTrigger.md) |
| ERPNext | `n8n-nodes-base.erpNext` | 1 |  | 5 | 1 | [schema](nodes/n8n-nodes-base.erpNext.md) |
| Error Trigger | `n8n-nodes-base.errorTrigger` | 1 | ✓ | 0 | 1 | [schema](nodes/n8n-nodes-base.errorTrigger.md) |
| Eventbrite Trigger | `n8n-nodes-base.eventbriteTrigger` | 1 | ✓ | 0 | 5 | [schema](nodes/n8n-nodes-base.eventbriteTrigger.md) |
| Execute Command | `n8n-nodes-base.executeCommand` | 1 |  | 0 | 2 | [schema](nodes/n8n-nodes-base.executeCommand.md) |
| Execute Sub-workflow | `n8n-nodes-base.executeWorkflow` | 1.3 |  | 1 | 11 | [schema](nodes/n8n-nodes-base.executeWorkflow.md) |
| Execute Workflow Trigger | `n8n-nodes-base.executeWorkflowTrigger` | 1.2 | ✓ | 0 | 6 | [schema](nodes/n8n-nodes-base.executeWorkflowTrigger.md) |
| Execution Data | `n8n-nodes-base.executionData` | 1.1 |  | 1 | 3 | [schema](nodes/n8n-nodes-base.executionData.md) |
| Extract from File | `n8n-nodes-base.extractFromFile` | 1.1 |  | 12 | 1 | [schema](nodes/n8n-nodes-base.extractFromFile.md) |
| Facebook Graph API | `n8n-nodes-base.facebookGraphApi` | 1 |  | 0 | 14 | [schema](nodes/n8n-nodes-base.facebookGraphApi.md) |
| Facebook Lead Ads Trigger | `n8n-nodes-base.facebookLeadAdsTrigger` | 1 | ✓ | 0 | 5 | [schema](nodes/n8n-nodes-base.facebookLeadAdsTrigger.md) |
| Facebook Trigger | `n8n-nodes-base.facebookTrigger` | 1 | ✓ | 0 | 14 | [schema](nodes/n8n-nodes-base.facebookTrigger.md) |
| Figma Trigger (Beta) | `n8n-nodes-base.figmaTrigger` | 1 | ✓ | 0 | 3 | [schema](nodes/n8n-nodes-base.figmaTrigger.md) |
| FileMaker | `n8n-nodes-base.filemaker` | 1 |  | 0 | 25 | [schema](nodes/n8n-nodes-base.filemaker.md) |
| Filter | `n8n-nodes-base.filter` | 2.3 |  | 18 | 4 | [schema](nodes/n8n-nodes-base.filter.md) |
| Flow | `n8n-nodes-base.flow` | 1 |  | 4 | 3 | [schema](nodes/n8n-nodes-base.flow.md) |
| Flow Trigger | `n8n-nodes-base.flowTrigger` | 1 | ✓ | 4 | 3 | [schema](nodes/n8n-nodes-base.flowTrigger.md) |
| Form.io Trigger | `n8n-nodes-base.formIoTrigger` | 1 | ✓ | 0 | 4 | [schema](nodes/n8n-nodes-base.formIoTrigger.md) |
| Formstack Trigger | `n8n-nodes-base.formstackTrigger` | 1 | ✓ | 0 | 3 | [schema](nodes/n8n-nodes-base.formstackTrigger.md) |
| Freshdesk | `n8n-nodes-base.freshdesk` | 1 |  | 5 | 18 | [schema](nodes/n8n-nodes-base.freshdesk.md) |
| Freshservice | `n8n-nodes-base.freshservice` | 1 |  | 5 | 1 | [schema](nodes/n8n-nodes-base.freshservice.md) |
| Freshworks CRM | `n8n-nodes-base.freshworksCrm` | 1 |  | 7 | 1 | [schema](nodes/n8n-nodes-base.freshworksCrm.md) |
| FTP | `n8n-nodes-base.ftp` | 1 |  | 5 | 18 | [schema](nodes/n8n-nodes-base.ftp.md) |
| Function | `n8n-nodes-base.function` | 1 |  | 0 | 2 | [schema](nodes/n8n-nodes-base.function.md) |
| Function Item | `n8n-nodes-base.functionItem` | 1 |  | 0 | 2 | [schema](nodes/n8n-nodes-base.functionItem.md) |
| GetResponse | `n8n-nodes-base.getResponse` | 1 |  | 5 | 5 | [schema](nodes/n8n-nodes-base.getResponse.md) |
| GetResponse Trigger | `n8n-nodes-base.getResponseTrigger` | 1 | ✓ | 5 | 5 | [schema](nodes/n8n-nodes-base.getResponseTrigger.md) |
| Ghost | `n8n-nodes-base.ghost` | 1 |  | 5 | 2 | [schema](nodes/n8n-nodes-base.ghost.md) |
| Git | `n8n-nodes-base.git` | 1.1 |  | 15 | 3 | [schema](nodes/n8n-nodes-base.git.md) |
| GitHub | `n8n-nodes-base.github` | 1.1 |  | 24 | 74 | [schema](nodes/n8n-nodes-base.github.md) |
| Github Trigger | `n8n-nodes-base.githubTrigger` | 1.1 | ✓ | 24 | 74 | [schema](nodes/n8n-nodes-base.githubTrigger.md) |
| GitLab | `n8n-nodes-base.gitlab` | 1 |  | 11 | 47 | [schema](nodes/n8n-nodes-base.gitlab.md) |
| GitLab Trigger | `n8n-nodes-base.gitlabTrigger` | 1 | ✓ | 11 | 47 | [schema](nodes/n8n-nodes-base.gitlabTrigger.md) |
| Gmail | `n8n-nodes-base.gmail` | 2.2 |  | 14 | 8 | [schema](nodes/n8n-nodes-base.gmail.md) |
| Gmail Trigger | `n8n-nodes-base.gmailTrigger` | 2.2 | ✓ | 14 | 8 | [schema](nodes/n8n-nodes-base.gmailTrigger.md) |
| Gong | `n8n-nodes-base.gong` | 1 |  | 2 | 2 | [schema](nodes/n8n-nodes-base.gong.md) |
| Google Ads | `n8n-nodes-base.googleAds` | 1 |  | 2 | 2 | [schema](nodes/n8n-nodes-base.googleAds.md) |
| Google Analytics | `n8n-nodes-base.googleAnalytics` | 2 |  | 7 | 1 | [schema](nodes/n8n-nodes-base.googleAnalytics.md) |
| Google BigQuery | `n8n-nodes-base.googleBigQuery` | 2.1 |  | 4 | 2 | [schema](nodes/n8n-nodes-base.googleBigQuery.md) |
| Google Books | `n8n-nodes-base.googleBooks` | 2 |  | 6 | 14 | [schema](nodes/n8n-nodes-base.googleBooks.md) |
| Google Business Profile | `n8n-nodes-base.googleBusinessProfile` | 1 |  | 6 | 4 | [schema](nodes/n8n-nodes-base.googleBusinessProfile.md) |
| Google Business Profile Trigger | `n8n-nodes-base.googleBusinessProfileTrigger` | 1 | ✓ | 6 | 4 | [schema](nodes/n8n-nodes-base.googleBusinessProfileTrigger.md) |
| Google Calendar | `n8n-nodes-base.googleCalendar` | 1.3 |  | 6 | 5 | [schema](nodes/n8n-nodes-base.googleCalendar.md) |
| Google Calendar Trigger | `n8n-nodes-base.googleCalendarTrigger` | 1.3 | ✓ | 6 | 5 | [schema](nodes/n8n-nodes-base.googleCalendarTrigger.md) |
| Google Chat | `n8n-nodes-base.googleChat` | 1 |  | 6 | 2 | [schema](nodes/n8n-nodes-base.googleChat.md) |
| Google Cloud Firestore | `n8n-nodes-base.googleFirebaseCloudFirestore` | 1.1 |  | 7 | 2 | [schema](nodes/n8n-nodes-base.googleFirebaseCloudFirestore.md) |
| Google Cloud Natural Language | `n8n-nodes-base.googleCloudNaturalLanguage` | 1 |  | 1 | 6 | [schema](nodes/n8n-nodes-base.googleCloudNaturalLanguage.md) |
| Google Cloud Realtime Database | `n8n-nodes-base.googleFirebaseRealtimeDatabase` | 1 |  | 5 | 4 | [schema](nodes/n8n-nodes-base.googleFirebaseRealtimeDatabase.md) |
| Google Cloud Storage | `n8n-nodes-base.googleCloudStorage` | 1.1 |  | 17 | 2 | [schema](nodes/n8n-nodes-base.googleCloudStorage.md) |
| Google Contacts | `n8n-nodes-base.googleContacts` | 1 |  | 5 | 1 | [schema](nodes/n8n-nodes-base.googleContacts.md) |
| Google Docs | `n8n-nodes-base.googleDocs` | 2 |  | 3 | 2 | [schema](nodes/n8n-nodes-base.googleDocs.md) |
| Google Drive | `n8n-nodes-base.googleDrive` | 3 |  | 18 | 39 | [schema](nodes/n8n-nodes-base.googleDrive.md) |
| Google Drive Trigger | `n8n-nodes-base.googleDriveTrigger` | 3 | ✓ | 18 | 39 | [schema](nodes/n8n-nodes-base.googleDriveTrigger.md) |
| Google Perspective | `n8n-nodes-base.googlePerspective` | 1 |  | 1 | 4 | [schema](nodes/n8n-nodes-base.googlePerspective.md) |
| Google Sheets | `n8n-nodes-base.googleSheets` | 4.7 |  | 11 | 26 | [schema](nodes/n8n-nodes-base.googleSheets.md) |
| Google Sheets Trigger | `n8n-nodes-base.googleSheetsTrigger` | 4.7 | ✓ | 11 | 26 | [schema](nodes/n8n-nodes-base.googleSheetsTrigger.md) |
| Google Slides | `n8n-nodes-base.googleSlides` | 2 |  | 5 | 13 | [schema](nodes/n8n-nodes-base.googleSlides.md) |
| Google Tasks | `n8n-nodes-base.googleTasks` | 1 |  | 5 | 1 | [schema](nodes/n8n-nodes-base.googleTasks.md) |
| Google Translate | `n8n-nodes-base.googleTranslate` | 2 |  | 1 | 5 | [schema](nodes/n8n-nodes-base.googleTranslate.md) |
| Google Workspace Admin | `n8n-nodes-base.gSuiteAdmin` | 1 |  | 8 | 1 | [schema](nodes/n8n-nodes-base.gSuiteAdmin.md) |
| Gotify | `n8n-nodes-base.gotify` | 1 |  | 3 | 8 | [schema](nodes/n8n-nodes-base.gotify.md) |
| GoToWebinar | `n8n-nodes-base.goToWebinar` | 1 |  | 7 | 1 | [schema](nodes/n8n-nodes-base.goToWebinar.md) |
| Grafana | `n8n-nodes-base.grafana` | 1 |  | 7 | 1 | [schema](nodes/n8n-nodes-base.grafana.md) |
| GraphQL | `n8n-nodes-base.graphql` | 1.1 |  | 0 | 11 | [schema](nodes/n8n-nodes-base.graphql.md) |
| Grist | `n8n-nodes-base.grist` | 1 |  | 4 | 0 | [schema](nodes/n8n-nodes-base.grist.md) |
| Gumroad Trigger | `n8n-nodes-base.gumroadTrigger` | 1 | ✓ | 0 | 2 | [schema](nodes/n8n-nodes-base.gumroadTrigger.md) |
| Hacker News | `n8n-nodes-base.hackerNews` | 1 |  | 2 | 10 | [schema](nodes/n8n-nodes-base.hackerNews.md) |
| HaloPSA | `n8n-nodes-base.haloPSA` | 1 |  | 5 | 1 | [schema](nodes/n8n-nodes-base.haloPSA.md) |
| Harvest | `n8n-nodes-base.harvest` | 1 |  | 11 | 3 | [schema](nodes/n8n-nodes-base.harvest.md) |
| Help Scout | `n8n-nodes-base.helpScout` | 1 |  | 6 | 2 | [schema](nodes/n8n-nodes-base.helpScout.md) |
| Help Scout Trigger | `n8n-nodes-base.helpScoutTrigger` | 1 | ✓ | 6 | 2 | [schema](nodes/n8n-nodes-base.helpScoutTrigger.md) |
| HighLevel | `n8n-nodes-base.highLevel` | 2 |  | 9 | 0 | [schema](nodes/n8n-nodes-base.highLevel.md) |
| Home Assistant | `n8n-nodes-base.homeAssistant` | 1 |  | 9 | 1 | [schema](nodes/n8n-nodes-base.homeAssistant.md) |
| HTML | `n8n-nodes-base.html` | 1.2 |  | 3 | 7 | [schema](nodes/n8n-nodes-base.html.md) |
| HTML Extract | `n8n-nodes-base.htmlExtract` | 1 |  | 0 | 4 | [schema](nodes/n8n-nodes-base.htmlExtract.md) |
| HTTP Request | `n8n-nodes-base.httpRequest` | 4.4 |  | 0 | 19 | [schema](nodes/n8n-nodes-base.httpRequest.md) |
| HubSpot | `n8n-nodes-base.hubspot` | 2.2 |  | 15 | 4 | [schema](nodes/n8n-nodes-base.hubspot.md) |
| HubSpot Trigger | `n8n-nodes-base.hubspotTrigger` | 2.2 | ✓ | 15 | 4 | [schema](nodes/n8n-nodes-base.hubspotTrigger.md) |
| Humantic AI | `n8n-nodes-base.humanticAi` | 1 |  | 3 | 1 | [schema](nodes/n8n-nodes-base.humanticAi.md) |
| Hunter | `n8n-nodes-base.hunter` | 1 |  | 3 | 10 | [schema](nodes/n8n-nodes-base.hunter.md) |
| iCalendar | `n8n-nodes-base.iCal` | 1 |  | 1 | 1 | [schema](nodes/n8n-nodes-base.iCal.md) |
| If | `n8n-nodes-base.if` | 2.3 |  | 18 | 4 | [schema](nodes/n8n-nodes-base.if.md) |
| Intercom | `n8n-nodes-base.intercom` | 1 |  | 6 | 1 | [schema](nodes/n8n-nodes-base.intercom.md) |
| Interval | `n8n-nodes-base.interval` | 1 |  | 0 | 3 | [schema](nodes/n8n-nodes-base.interval.md) |
| Invoice Ninja | `n8n-nodes-base.invoiceNinja` | 2 |  | 6 | 3 | [schema](nodes/n8n-nodes-base.invoiceNinja.md) |
| Invoice Ninja Trigger | `n8n-nodes-base.invoiceNinjaTrigger` | 2 | ✓ | 6 | 3 | [schema](nodes/n8n-nodes-base.invoiceNinjaTrigger.md) |
| Item Lists | `n8n-nodes-base.itemLists` | 3.1 |  | 7 | 22 | [schema](nodes/n8n-nodes-base.itemLists.md) |
| Iterable | `n8n-nodes-base.iterable` | 1 |  | 6 | 1 | [schema](nodes/n8n-nodes-base.iterable.md) |
| Jenkins | `n8n-nodes-base.jenkins` | 1 |  | 11 | 15 | [schema](nodes/n8n-nodes-base.jenkins.md) |
| Jina AI | `n8n-nodes-base.jinaAi` | 1 |  | 3 | 12 | [schema](nodes/n8n-nodes-base.jinaAi.md) |
| Jira Software | `n8n-nodes-base.jira` | 1.1 |  | 10 | 6 | [schema](nodes/n8n-nodes-base.jira.md) |
| Jira Trigger | `n8n-nodes-base.jiraTrigger` | 1.1 | ✓ | 10 | 6 | [schema](nodes/n8n-nodes-base.jiraTrigger.md) |
| Jotform Trigger | `n8n-nodes-base.jotFormTrigger` | 1 | ✓ | 0 | 3 | [schema](nodes/n8n-nodes-base.jotFormTrigger.md) |
| JWT | `n8n-nodes-base.jwt` | 1 |  | 3 | 7 | [schema](nodes/n8n-nodes-base.jwt.md) |
| Kafka | `n8n-nodes-base.kafka` | 1.3 |  | 0 | 15 | [schema](nodes/n8n-nodes-base.kafka.md) |
| Kafka Trigger | `n8n-nodes-base.kafkaTrigger` | 1.3 | ✓ | 0 | 15 | [schema](nodes/n8n-nodes-base.kafkaTrigger.md) |
| Keap | `n8n-nodes-base.keap` | 1 |  | 9 | 3 | [schema](nodes/n8n-nodes-base.keap.md) |
| Keap Trigger | `n8n-nodes-base.keapTrigger` | 1 | ✓ | 9 | 3 | [schema](nodes/n8n-nodes-base.keapTrigger.md) |
| KoBoToolbox | `n8n-nodes-base.koBoToolbox` | 1 |  | 10 | 3 | [schema](nodes/n8n-nodes-base.koBoToolbox.md) |
| KoBoToolbox Trigger | `n8n-nodes-base.koBoToolboxTrigger` | 1 | ✓ | 10 | 3 | [schema](nodes/n8n-nodes-base.koBoToolboxTrigger.md) |
| Ldap | `n8n-nodes-base.ldap` | 1 |  | 6 | 2 | [schema](nodes/n8n-nodes-base.ldap.md) |
| Lemlist | `n8n-nodes-base.lemlist` | 2 |  | 10 | 3 | [schema](nodes/n8n-nodes-base.lemlist.md) |
| Lemlist Trigger | `n8n-nodes-base.lemlistTrigger` | 2 | ✓ | 10 | 3 | [schema](nodes/n8n-nodes-base.lemlistTrigger.md) |
| Limit | `n8n-nodes-base.limit` | 1 |  | 0 | 2 | [schema](nodes/n8n-nodes-base.limit.md) |
| Line | `n8n-nodes-base.line` | 1 |  | 1 | 2 | [schema](nodes/n8n-nodes-base.line.md) |
| Linear | `n8n-nodes-base.linear` | 1.1 |  | 7 | 4 | [schema](nodes/n8n-nodes-base.linear.md) |
| Linear Trigger | `n8n-nodes-base.linearTrigger` | 1.1 | ✓ | 7 | 4 | [schema](nodes/n8n-nodes-base.linearTrigger.md) |
| LingvaNex | `n8n-nodes-base.lingvaNex` | 1 |  | 3 | 4 | [schema](nodes/n8n-nodes-base.lingvaNex.md) |
| LinkedIn | `n8n-nodes-base.linkedIn` | 1 |  | 1 | 2 | [schema](nodes/n8n-nodes-base.linkedIn.md) |
| Local File Trigger | `n8n-nodes-base.localFileTrigger` | 1 | ✓ | 0 | 4 | [schema](nodes/n8n-nodes-base.localFileTrigger.md) |
| LoneScale | `n8n-nodes-base.loneScale` | 1 |  | 2 | 13 | [schema](nodes/n8n-nodes-base.loneScale.md) |
| LoneScale Trigger | `n8n-nodes-base.loneScaleTrigger` | 1 | ✓ | 2 | 13 | [schema](nodes/n8n-nodes-base.loneScaleTrigger.md) |
| Magento 2 | `n8n-nodes-base.magento2` | 1 |  | 7 | 1 | [schema](nodes/n8n-nodes-base.magento2.md) |
| Mailcheck | `n8n-nodes-base.mailcheck` | 1 |  | 1 | 3 | [schema](nodes/n8n-nodes-base.mailcheck.md) |
| Mailchimp | `n8n-nodes-base.mailchimp` | 1 |  | 8 | 48 | [schema](nodes/n8n-nodes-base.mailchimp.md) |
| Mailchimp Trigger | `n8n-nodes-base.mailchimpTrigger` | 1 | ✓ | 8 | 48 | [schema](nodes/n8n-nodes-base.mailchimpTrigger.md) |
| MailerLite | `n8n-nodes-base.mailerLite` | 2 |  | 4 | 3 | [schema](nodes/n8n-nodes-base.mailerLite.md) |
| MailerLite Trigger | `n8n-nodes-base.mailerLiteTrigger` | 2 | ✓ | 4 | 3 | [schema](nodes/n8n-nodes-base.mailerLiteTrigger.md) |
| Mailgun | `n8n-nodes-base.mailgun` | 1 |  | 0 | 8 | [schema](nodes/n8n-nodes-base.mailgun.md) |
| Mailjet | `n8n-nodes-base.mailjet` | 1 |  | 2 | 2 | [schema](nodes/n8n-nodes-base.mailjet.md) |
| Mailjet Trigger | `n8n-nodes-base.mailjetTrigger` | 1 | ✓ | 2 | 2 | [schema](nodes/n8n-nodes-base.mailjetTrigger.md) |
| Mandrill | `n8n-nodes-base.mandrill` | 1 |  | 2 | 15 | [schema](nodes/n8n-nodes-base.mandrill.md) |
| Manual Trigger | `n8n-nodes-base.manualTrigger` | 1 | ✓ | 0 | 1 | [schema](nodes/n8n-nodes-base.manualTrigger.md) |
| Markdown | `n8n-nodes-base.markdown` | 1 |  | 0 | 5 | [schema](nodes/n8n-nodes-base.markdown.md) |
| Marketstack | `n8n-nodes-base.marketstack` | 1 |  | 2 | 1 | [schema](nodes/n8n-nodes-base.marketstack.md) |
| Matrix | `n8n-nodes-base.matrix` | 1 |  | 9 | 1 | [schema](nodes/n8n-nodes-base.matrix.md) |
| Mattermost | `n8n-nodes-base.mattermost` | 1 |  | 14 | 1 | [schema](nodes/n8n-nodes-base.mattermost.md) |
| Mautic | `n8n-nodes-base.mautic` | 1 |  | 11 | 4 | [schema](nodes/n8n-nodes-base.mautic.md) |
| Mautic Trigger | `n8n-nodes-base.mauticTrigger` | 1 | ✓ | 11 | 4 | [schema](nodes/n8n-nodes-base.mauticTrigger.md) |
| Medium | `n8n-nodes-base.medium` | 1 |  | 2 | 12 | [schema](nodes/n8n-nodes-base.medium.md) |
| Merge | `n8n-nodes-base.merge` | 4.2 |  | 0 | 11 | [schema](nodes/n8n-nodes-base.merge.md) |
| Message an n8n Agent | `n8n-nodes-base.messageAnAgent` | 1 |  | 0 | 6 | [schema](nodes/n8n-nodes-base.messageAnAgent.md) |
| MessageBird | `n8n-nodes-base.messageBird` | 1 |  | 2 | 7 | [schema](nodes/n8n-nodes-base.messageBird.md) |
| Metabase | `n8n-nodes-base.metabase` | 1 |  | 5 | 1 | [schema](nodes/n8n-nodes-base.metabase.md) |
| Microsoft Dynamics CRM | `n8n-nodes-base.microsoftDynamicsCrm` | 1 |  | 5 | 1 | [schema](nodes/n8n-nodes-base.microsoftDynamicsCrm.md) |
| Microsoft Entra ID | `n8n-nodes-base.microsoftEntra` | 1 |  | 11 | 1 | [schema](nodes/n8n-nodes-base.microsoftEntra.md) |
| Microsoft Excel 365 | `n8n-nodes-base.microsoftExcel` | 2.2 |  | 17 | 2 | [schema](nodes/n8n-nodes-base.microsoftExcel.md) |
| Microsoft Graph Security | `n8n-nodes-base.microsoftGraphSecurity` | 1 |  | 3 | 1 | [schema](nodes/n8n-nodes-base.microsoftGraphSecurity.md) |
| Microsoft OneDrive | `n8n-nodes-base.microsoftOneDrive` | 1.1 |  | 10 | 2 | [schema](nodes/n8n-nodes-base.microsoftOneDrive.md) |
| Microsoft OneDrive Trigger | `n8n-nodes-base.microsoftOneDriveTrigger` | 1.1 | ✓ | 10 | 2 | [schema](nodes/n8n-nodes-base.microsoftOneDriveTrigger.md) |
| Microsoft Outlook | `n8n-nodes-base.microsoftOutlook` | 2 |  | 12 | 2 | [schema](nodes/n8n-nodes-base.microsoftOutlook.md) |
| Microsoft Outlook Trigger | `n8n-nodes-base.microsoftOutlookTrigger` | 2 | ✓ | 12 | 2 | [schema](nodes/n8n-nodes-base.microsoftOutlookTrigger.md) |
| Microsoft SharePoint | `n8n-nodes-base.microsoftSharePoint` | 1 |  | 9 | 1 | [schema](nodes/n8n-nodes-base.microsoftSharePoint.md) |
| Microsoft SQL | `n8n-nodes-base.microsoftSql` | 1.1 |  | 4 | 10 | [schema](nodes/n8n-nodes-base.microsoftSql.md) |
| Microsoft Teams | `n8n-nodes-base.microsoftTeams` | 2 |  | 7 | 8 | [schema](nodes/n8n-nodes-base.microsoftTeams.md) |
| Microsoft Teams Trigger | `n8n-nodes-base.microsoftTeamsTrigger` | 2 | ✓ | 7 | 8 | [schema](nodes/n8n-nodes-base.microsoftTeamsTrigger.md) |
| Microsoft To Do | `n8n-nodes-base.microsoftToDo` | 1 |  | 5 | 1 | [schema](nodes/n8n-nodes-base.microsoftToDo.md) |
| Mindee | `n8n-nodes-base.mindee` | 3 |  | 1 | 5 | [schema](nodes/n8n-nodes-base.mindee.md) |
| MISP | `n8n-nodes-base.misp` | 1 |  | 12 | 1 | [schema](nodes/n8n-nodes-base.misp.md) |
| Mistral AI | `n8n-nodes-base.mistralAi` | 1 |  | 1 | 1 | [schema](nodes/n8n-nodes-base.mistralAi.md) |
| Mocean | `n8n-nodes-base.mocean` | 1 |  | 1 | 7 | [schema](nodes/n8n-nodes-base.mocean.md) |
| Monday.com | `n8n-nodes-base.mondayCom` | 1 |  | 10 | 2 | [schema](nodes/n8n-nodes-base.mondayCom.md) |
| MongoDB | `n8n-nodes-base.mongoDb` | 1.3 |  | 11 | 0 | [schema](nodes/n8n-nodes-base.mongoDb.md) |
| Monica CRM | `n8n-nodes-base.monicaCrm` | 1 |  | 7 | 1 | [schema](nodes/n8n-nodes-base.monicaCrm.md) |
| MQTT | `n8n-nodes-base.mqtt` | 1 |  | 0 | 5 | [schema](nodes/n8n-nodes-base.mqtt.md) |
| MQTT Trigger | `n8n-nodes-base.mqttTrigger` | 1 | ✓ | 0 | 5 | [schema](nodes/n8n-nodes-base.mqttTrigger.md) |
| MSG91 | `n8n-nodes-base.msg91` | 1 |  | 1 | 5 | [schema](nodes/n8n-nodes-base.msg91.md) |
| MySQL | `n8n-nodes-base.mySql` | 2.5 |  | 6 | 9 | [schema](nodes/n8n-nodes-base.mySql.md) |
| n8n | `n8n-nodes-base.n8n` | 1 |  | 10 | 1 | [schema](nodes/n8n-nodes-base.n8n.md) |
| n8n Form | `n8n-nodes-base.form` | 2.6 |  | 2 | 5 | [schema](nodes/n8n-nodes-base.form.md) |
| n8n Form Trigger | `n8n-nodes-base.formTrigger` | 2.6 | ✓ | 2 | 5 | [schema](nodes/n8n-nodes-base.formTrigger.md) |
| n8n Trigger | `n8n-nodes-base.n8nTrigger` | 1 | ✓ | 0 | 1 | [schema](nodes/n8n-nodes-base.n8nTrigger.md) |
| NASA | `n8n-nodes-base.nasa` | 1 |  | 2 | 34 | [schema](nodes/n8n-nodes-base.nasa.md) |
| Netlify | `n8n-nodes-base.netlify` | 1 |  | 5 | 5 | [schema](nodes/n8n-nodes-base.netlify.md) |
| Netlify Trigger | `n8n-nodes-base.netlifyTrigger` | 1 | ✓ | 5 | 5 | [schema](nodes/n8n-nodes-base.netlifyTrigger.md) |
| Netscaler ADC | `n8n-nodes-base.citrixAdc` | 1 |  | 5 | 1 | [schema](nodes/n8n-nodes-base.citrixAdc.md) |
| Nextcloud | `n8n-nodes-base.nextCloud` | 1 |  | 11 | 33 | [schema](nodes/n8n-nodes-base.nextCloud.md) |
| No Operation, do nothing | `n8n-nodes-base.noOp` | 1 |  | 0 | 0 | [schema](nodes/n8n-nodes-base.noOp.md) |
| NocoDB | `n8n-nodes-base.nocoDb` | 4 |  | 12 | 4 | [schema](nodes/n8n-nodes-base.nocoDb.md) |
| Notion | `n8n-nodes-base.notion` | 2.2 |  | 7 | 7 | [schema](nodes/n8n-nodes-base.notion.md) |
| Notion Trigger | `n8n-nodes-base.notionTrigger` | 2.2 | ✓ | 7 | 7 | [schema](nodes/n8n-nodes-base.notionTrigger.md) |
| Npm | `n8n-nodes-base.npm` | 1 |  | 5 | 1 | [schema](nodes/n8n-nodes-base.npm.md) |
| Odoo | `n8n-nodes-base.odoo` | 2 |  | 5 | 2 | [schema](nodes/n8n-nodes-base.odoo.md) |
| Okta | `n8n-nodes-base.okta` | 1 |  | 6 | 1 | [schema](nodes/n8n-nodes-base.okta.md) |
| One Simple API | `n8n-nodes-base.oneSimpleApi` | 1 |  | 10 | 27 | [schema](nodes/n8n-nodes-base.oneSimpleApi.md) |
| Onfleet | `n8n-nodes-base.onfleet` | 1 |  | 14 | 1 | [schema](nodes/n8n-nodes-base.onfleet.md) |
| Onfleet Trigger | `n8n-nodes-base.onfleetTrigger` | 1 | ✓ | 14 | 1 | [schema](nodes/n8n-nodes-base.onfleetTrigger.md) |
| OpenAI | `n8n-nodes-base.openAi` | 1.1 |  | 4 | 1 | [schema](nodes/n8n-nodes-base.openAi.md) |
| OpenThesaurus | `n8n-nodes-base.openThesaurus` | 1 |  | 1 | 3 | [schema](nodes/n8n-nodes-base.openThesaurus.md) |
| OpenWeatherMap | `n8n-nodes-base.openWeatherMap` | 1 |  | 2 | 9 | [schema](nodes/n8n-nodes-base.openWeatherMap.md) |
| Orbit | `n8n-nodes-base.orbit` | 1 |  | 7 | 2 | [schema](nodes/n8n-nodes-base.orbit.md) |
| Oura | `n8n-nodes-base.oura` | 1 |  | 4 | 1 | [schema](nodes/n8n-nodes-base.oura.md) |
| Paddle | `n8n-nodes-base.paddle` | 1 |  | 5 | 1 | [schema](nodes/n8n-nodes-base.paddle.md) |
| PagerDuty | `n8n-nodes-base.pagerDuty` | 1 |  | 4 | 2 | [schema](nodes/n8n-nodes-base.pagerDuty.md) |
| PayPal | `n8n-nodes-base.payPal` | 1 |  | 3 | 2 | [schema](nodes/n8n-nodes-base.payPal.md) |
| PayPal Trigger | `n8n-nodes-base.payPalTrigger` | 1 | ✓ | 3 | 2 | [schema](nodes/n8n-nodes-base.payPalTrigger.md) |
| Peekalink | `n8n-nodes-base.peekalink` | 1 |  | 2 | 2 | [schema](nodes/n8n-nodes-base.peekalink.md) |
| Perplexity | `n8n-nodes-base.perplexity` | 2 |  | 5 | 1 | [schema](nodes/n8n-nodes-base.perplexity.md) |
| Phantombuster | `n8n-nodes-base.phantombuster` | 1 |  | 5 | 1 | [schema](nodes/n8n-nodes-base.phantombuster.md) |
| Philips Hue | `n8n-nodes-base.philipsHue` | 1 |  | 4 | 1 | [schema](nodes/n8n-nodes-base.philipsHue.md) |
| Pipedrive | `n8n-nodes-base.pipedrive` | 2 |  | 10 | 100 | [schema](nodes/n8n-nodes-base.pipedrive.md) |
| Pipedrive Trigger | `n8n-nodes-base.pipedriveTrigger` | 2 | ✓ | 10 | 100 | [schema](nodes/n8n-nodes-base.pipedriveTrigger.md) |
| Plivo | `n8n-nodes-base.plivo` | 1 |  | 2 | 1 | [schema](nodes/n8n-nodes-base.plivo.md) |
| PostBin | `n8n-nodes-base.postBin` | 1 |  | 6 | 1 | [schema](nodes/n8n-nodes-base.postBin.md) |
| Postgres | `n8n-nodes-base.postgres` | 2.6 |  | 6 | 18 | [schema](nodes/n8n-nodes-base.postgres.md) |
| Postgres Trigger | `n8n-nodes-base.postgresTrigger` | 2.6 | ✓ | 6 | 18 | [schema](nodes/n8n-nodes-base.postgresTrigger.md) |
| PostHog | `n8n-nodes-base.postHog` | 1 |  | 3 | 1 | [schema](nodes/n8n-nodes-base.postHog.md) |
| Postmark Trigger | `n8n-nodes-base.postmarkTrigger` | 1 | ✓ | 0 | 3 | [schema](nodes/n8n-nodes-base.postmarkTrigger.md) |
| ProfitWell | `n8n-nodes-base.profitWell` | 1 |  | 2 | 1 | [schema](nodes/n8n-nodes-base.profitWell.md) |
| Pushbullet | `n8n-nodes-base.pushbullet` | 1 |  | 4 | 15 | [schema](nodes/n8n-nodes-base.pushbullet.md) |
| Pushcut | `n8n-nodes-base.pushcut` | 1 |  | 1 | 5 | [schema](nodes/n8n-nodes-base.pushcut.md) |
| Pushcut Trigger | `n8n-nodes-base.pushcutTrigger` | 1 | ✓ | 1 | 5 | [schema](nodes/n8n-nodes-base.pushcutTrigger.md) |
| Pushover | `n8n-nodes-base.pushover` | 1 |  | 1 | 8 | [schema](nodes/n8n-nodes-base.pushover.md) |
| QuestDB | `n8n-nodes-base.questDb` | 1 |  | 2 | 8 | [schema](nodes/n8n-nodes-base.questDb.md) |
| Quick Base | `n8n-nodes-base.quickbase` | 1 |  | 8 | 1 | [schema](nodes/n8n-nodes-base.quickbase.md) |
| QuickBooks Online | `n8n-nodes-base.quickbooks` | 1 |  | 8 | 1 | [schema](nodes/n8n-nodes-base.quickbooks.md) |
| QuickChart | `n8n-nodes-base.quickChart` | 1 |  | 0 | 8 | [schema](nodes/n8n-nodes-base.quickChart.md) |
| RabbitMQ | `n8n-nodes-base.rabbitmq` | 1.1 |  | 2 | 13 | [schema](nodes/n8n-nodes-base.rabbitmq.md) |
| RabbitMQ Trigger | `n8n-nodes-base.rabbitmqTrigger` | 1.1 | ✓ | 2 | 13 | [schema](nodes/n8n-nodes-base.rabbitmqTrigger.md) |
| Raindrop | `n8n-nodes-base.raindrop` | 1 |  | 5 | 1 | [schema](nodes/n8n-nodes-base.raindrop.md) |
| Read Binary File | `n8n-nodes-base.readBinaryFile` | 1 |  | 0 | 2 | [schema](nodes/n8n-nodes-base.readBinaryFile.md) |
| Read Binary Files | `n8n-nodes-base.readBinaryFiles` | 1 |  | 0 | 2 | [schema](nodes/n8n-nodes-base.readBinaryFiles.md) |
| Read PDF | `n8n-nodes-base.readPDF` | 1 |  | 0 | 3 | [schema](nodes/n8n-nodes-base.readPDF.md) |
| Read/Write Files from Disk | `n8n-nodes-base.readWriteFile` | 1.1 |  | 2 | 2 | [schema](nodes/n8n-nodes-base.readWriteFile.md) |
| Reddit | `n8n-nodes-base.reddit` | 1 |  | 6 | 1 | [schema](nodes/n8n-nodes-base.reddit.md) |
| Redis | `n8n-nodes-base.redis` | 1 |  | 10 | 27 | [schema](nodes/n8n-nodes-base.redis.md) |
| Redis Trigger | `n8n-nodes-base.redisTrigger` | 1 | ✓ | 10 | 27 | [schema](nodes/n8n-nodes-base.redisTrigger.md) |
| Remove Duplicates | `n8n-nodes-base.removeDuplicates` | 2 |  | 2 | 4 | [schema](nodes/n8n-nodes-base.removeDuplicates.md) |
| Rename Keys | `n8n-nodes-base.renameKeys` | 1 |  | 0 | 2 | [schema](nodes/n8n-nodes-base.renameKeys.md) |
| Respond to Webhook | `n8n-nodes-base.respondToWebhook` | 1.5 |  | 0 | 11 | [schema](nodes/n8n-nodes-base.respondToWebhook.md) |
| RocketChat | `n8n-nodes-base.rocketchat` | 1 |  | 1 | 8 | [schema](nodes/n8n-nodes-base.rocketchat.md) |
| RSS Feed Trigger | `n8n-nodes-base.rssFeedReadTrigger` | 1.2 | ✓ | 0 | 3 | [schema](nodes/n8n-nodes-base.rssFeedReadTrigger.md) |
| RSS Read | `n8n-nodes-base.rssFeedRead` | 1.2 |  | 0 | 3 | [schema](nodes/n8n-nodes-base.rssFeedRead.md) |
| Rundeck | `n8n-nodes-base.rundeck` | 1 |  | 2 | 6 | [schema](nodes/n8n-nodes-base.rundeck.md) |
| S3 | `n8n-nodes-base.s3` | 1 |  | 0 | 2 | [schema](nodes/n8n-nodes-base.s3.md) |
| Salesforce | `n8n-nodes-base.salesforce` | 1.1 |  | 18 | 4 | [schema](nodes/n8n-nodes-base.salesforce.md) |
| Salesforce Trigger | `n8n-nodes-base.salesforceTrigger` | 1.1 | ✓ | 18 | 4 | [schema](nodes/n8n-nodes-base.salesforceTrigger.md) |
| Salesmate | `n8n-nodes-base.salesmate` | 1 |  | 5 | 1 | [schema](nodes/n8n-nodes-base.salesmate.md) |
| Schedule Trigger | `n8n-nodes-base.scheduleTrigger` | 1.3 | ✓ | 0 | 2 | [schema](nodes/n8n-nodes-base.scheduleTrigger.md) |
| SeaTable | `n8n-nodes-base.seaTable` | 2 |  | 16 | 8 | [schema](nodes/n8n-nodes-base.seaTable.md) |
| SeaTable Trigger | `n8n-nodes-base.seaTableTrigger` | 2 | ✓ | 16 | 8 | [schema](nodes/n8n-nodes-base.seaTableTrigger.md) |
| SecurityScorecard | `n8n-nodes-base.securityScorecard` | 1 |  | 14 | 1 | [schema](nodes/n8n-nodes-base.securityScorecard.md) |
| Segment | `n8n-nodes-base.segment` | 1 |  | 4 | 1 | [schema](nodes/n8n-nodes-base.segment.md) |
| Send Email | `n8n-nodes-base.emailSend` | 2.1 |  | 1 | 11 | [schema](nodes/n8n-nodes-base.emailSend.md) |
| SendGrid | `n8n-nodes-base.sendGrid` | 1 |  | 7 | 1 | [schema](nodes/n8n-nodes-base.sendGrid.md) |
| Sendy | `n8n-nodes-base.sendy` | 1 |  | 6 | 1 | [schema](nodes/n8n-nodes-base.sendy.md) |
| Sentry.io | `n8n-nodes-base.sentryIo` | 1 |  | 5 | 2 | [schema](nodes/n8n-nodes-base.sentryIo.md) |
| ServiceNow | `n8n-nodes-base.serviceNow` | 1 |  | 6 | 2 | [schema](nodes/n8n-nodes-base.serviceNow.md) |
| Set | `n8n-nodes-base.set` | 3.4 |  | 0 | 11 | [schema](nodes/n8n-nodes-base.set.md) |
| seven | `n8n-nodes-base.sms77` | 1 |  | 1 | 8 | [schema](nodes/n8n-nodes-base.sms77.md) |
| Shopify | `n8n-nodes-base.shopify` | 1 |  | 5 | 4 | [schema](nodes/n8n-nodes-base.shopify.md) |
| Shopify Trigger | `n8n-nodes-base.shopifyTrigger` | 1 | ✓ | 5 | 4 | [schema](nodes/n8n-nodes-base.shopifyTrigger.md) |
| SIGNL4 | `n8n-nodes-base.signl4` | 1 |  | 2 | 5 | [schema](nodes/n8n-nodes-base.signl4.md) |
| Simulate | `n8n-nodes-base.simulate` | 1 |  | 0 | 2 | [schema](nodes/n8n-nodes-base.simulate.md) |
| Simulate Trigger | `n8n-nodes-base.simulateTrigger` | 1 | ✓ | 0 | 2 | [schema](nodes/n8n-nodes-base.simulateTrigger.md) |
| Slack | `n8n-nodes-base.slack` | 2.5 |  | 34 | 8 | [schema](nodes/n8n-nodes-base.slack.md) |
| Slack Trigger | `n8n-nodes-base.slackTrigger` | 2.5 | ✓ | 34 | 8 | [schema](nodes/n8n-nodes-base.slackTrigger.md) |
| Snowflake | `n8n-nodes-base.snowflake` | 1 |  | 3 | 8 | [schema](nodes/n8n-nodes-base.snowflake.md) |
| Sort | `n8n-nodes-base.sort` | 1 |  | 0 | 4 | [schema](nodes/n8n-nodes-base.sort.md) |
| Split In Batches | `n8n-nodes-base.splitInBatches` | 3 |  | 0 | 3 | [schema](nodes/n8n-nodes-base.splitInBatches.md) |
| Split Out | `n8n-nodes-base.splitOut` | 1 |  | 0 | 4 | [schema](nodes/n8n-nodes-base.splitOut.md) |
| Splunk | `n8n-nodes-base.splunk` | 2 |  | 11 | 1 | [schema](nodes/n8n-nodes-base.splunk.md) |
| Spotify | `n8n-nodes-base.spotify` | 1 |  | 23 | 15 | [schema](nodes/n8n-nodes-base.spotify.md) |
| Spreadsheet File | `n8n-nodes-base.spreadsheetFile` | 2 |  | 2 | 0 | [schema](nodes/n8n-nodes-base.spreadsheetFile.md) |
| SSE Trigger | `n8n-nodes-base.sseTrigger` | 1 | ✓ | 0 | 1 | [schema](nodes/n8n-nodes-base.sseTrigger.md) |
| SSH | `n8n-nodes-base.ssh` | 1 |  | 3 | 11 | [schema](nodes/n8n-nodes-base.ssh.md) |
| Stackby | `n8n-nodes-base.stackby` | 1 |  | 4 | 8 | [schema](nodes/n8n-nodes-base.stackby.md) |
| Sticky Note | `n8n-nodes-base.stickyNote` | 1 |  | 0 | 4 | [schema](nodes/n8n-nodes-base.stickyNote.md) |
| Stop and Error | `n8n-nodes-base.stopAndError` | 1 |  | 0 | 3 | [schema](nodes/n8n-nodes-base.stopAndError.md) |
| Storyblok | `n8n-nodes-base.storyblok` | 1 |  | 6 | 2 | [schema](nodes/n8n-nodes-base.storyblok.md) |
| Strapi | `n8n-nodes-base.strapi` | 1 |  | 5 | 2 | [schema](nodes/n8n-nodes-base.strapi.md) |
| Strava | `n8n-nodes-base.strava` | 1.1 |  | 9 | 5 | [schema](nodes/n8n-nodes-base.strava.md) |
| Strava Trigger | `n8n-nodes-base.stravaTrigger` | 1.1 | ✓ | 9 | 5 | [schema](nodes/n8n-nodes-base.stravaTrigger.md) |
| Stripe | `n8n-nodes-base.stripe` | 1 |  | 7 | 3 | [schema](nodes/n8n-nodes-base.stripe.md) |
| Stripe Trigger | `n8n-nodes-base.stripeTrigger` | 1 | ✓ | 7 | 3 | [schema](nodes/n8n-nodes-base.stripeTrigger.md) |
| Summarize | `n8n-nodes-base.summarize` | 1.1 |  | 0 | 3 | [schema](nodes/n8n-nodes-base.summarize.md) |
| Supabase | `n8n-nodes-base.supabase` | 1 |  | 5 | 3 | [schema](nodes/n8n-nodes-base.supabase.md) |
| SurveyMonkey Trigger | `n8n-nodes-base.surveyMonkeyTrigger` | 1 | ✓ | 0 | 8 | [schema](nodes/n8n-nodes-base.surveyMonkeyTrigger.md) |
| Switch | `n8n-nodes-base.switch` | 3.4 |  | 16 | 9 | [schema](nodes/n8n-nodes-base.switch.md) |
| SyncroMSP | `n8n-nodes-base.syncroMsp` | 1 |  | 6 | 1 | [schema](nodes/n8n-nodes-base.syncroMsp.md) |
| Table Name or ID | `n8n-nodes-base.seaTableApi` | 1 |  | 5 | 4 | [schema](nodes/n8n-nodes-base.seaTableApi.md) |
| Taiga | `n8n-nodes-base.taiga` | 1 |  | 5 | 4 | [schema](nodes/n8n-nodes-base.taiga.md) |
| Taiga Trigger | `n8n-nodes-base.taigaTrigger` | 1 | ✓ | 5 | 4 | [schema](nodes/n8n-nodes-base.taigaTrigger.md) |
| Tapfiliate | `n8n-nodes-base.tapfiliate` | 1 |  | 9 | 1 | [schema](nodes/n8n-nodes-base.tapfiliate.md) |
| Telegram | `n8n-nodes-base.telegram` | 1.3 |  | 23 | 51 | [schema](nodes/n8n-nodes-base.telegram.md) |
| Telegram Trigger | `n8n-nodes-base.telegramTrigger` | 1.3 | ✓ | 23 | 51 | [schema](nodes/n8n-nodes-base.telegramTrigger.md) |
| TheHive | `n8n-nodes-base.theHive` | 2 |  | 8 | 2 | [schema](nodes/n8n-nodes-base.theHive.md) |
| TheHive 5 Trigger | `n8n-nodes-base.theHiveProjectTrigger` | 1 | ✓ | 22 | 5 | [schema](nodes/n8n-nodes-base.theHiveProjectTrigger.md) |
| TheHive Trigger | `n8n-nodes-base.theHiveTrigger` | 2 | ✓ | 8 | 2 | [schema](nodes/n8n-nodes-base.theHiveTrigger.md) |
| TimescaleDB | `n8n-nodes-base.timescaleDb` | 1 |  | 3 | 11 | [schema](nodes/n8n-nodes-base.timescaleDb.md) |
| Todoist | `n8n-nodes-base.todoist` | 2.2 |  | 13 | 51 | [schema](nodes/n8n-nodes-base.todoist.md) |
| Toggl Trigger | `n8n-nodes-base.togglTrigger` | 1 | ✓ | 0 | 1 | [schema](nodes/n8n-nodes-base.togglTrigger.md) |
| TOTP | `n8n-nodes-base.totp` | 1 |  | 1 | 2 | [schema](nodes/n8n-nodes-base.totp.md) |
| Track Time Saved | `n8n-nodes-base.timeSaved` | 1 |  | 0 | 3 | [schema](nodes/n8n-nodes-base.timeSaved.md) |
| TravisCI | `n8n-nodes-base.travisCi` | 1 |  | 5 | 1 | [schema](nodes/n8n-nodes-base.travisCi.md) |
| Trello | `n8n-nodes-base.trello` | 1 |  | 17 | 3 | [schema](nodes/n8n-nodes-base.trello.md) |
| Trello Trigger | `n8n-nodes-base.trelloTrigger` | 1 | ✓ | 17 | 3 | [schema](nodes/n8n-nodes-base.trelloTrigger.md) |
| Twake | `n8n-nodes-base.twake` | 1 |  | 1 | 6 | [schema](nodes/n8n-nodes-base.twake.md) |
| Twilio | `n8n-nodes-base.twilio` | 1 |  | 2 | 12 | [schema](nodes/n8n-nodes-base.twilio.md) |
| Twilio Trigger | `n8n-nodes-base.twilioTrigger` | 1 | ✓ | 2 | 12 | [schema](nodes/n8n-nodes-base.twilioTrigger.md) |
| Twist | `n8n-nodes-base.twist` | 1 |  | 7 | 1 | [schema](nodes/n8n-nodes-base.twist.md) |
| Typeform Trigger | `n8n-nodes-base.typeformTrigger` | 1.1 | ✓ | 0 | 4 | [schema](nodes/n8n-nodes-base.typeformTrigger.md) |
| Unleashed Software | `n8n-nodes-base.unleashedSoftware` | 1 |  | 2 | 1 | [schema](nodes/n8n-nodes-base.unleashedSoftware.md) |
| Uplead | `n8n-nodes-base.uplead` | 1 |  | 1 | 1 | [schema](nodes/n8n-nodes-base.uplead.md) |
| uProc | `n8n-nodes-base.uproc` | 1 |  | 0 | 1 | [schema](nodes/n8n-nodes-base.uproc.md) |
| UptimeRobot | `n8n-nodes-base.uptimeRobot` | 1 |  | 6 | 2 | [schema](nodes/n8n-nodes-base.uptimeRobot.md) |
| urlscan.io | `n8n-nodes-base.urlScanIo` | 1 |  | 3 | 1 | [schema](nodes/n8n-nodes-base.urlScanIo.md) |
| Venafi TLS Protect Cloud | `n8n-nodes-base.venafiTlsProtectCloud` | 1 |  | 6 | 2 | [schema](nodes/n8n-nodes-base.venafiTlsProtectCloud.md) |
| Venafi TLS Protect Cloud Trigger | `n8n-nodes-base.venafiTlsProtectCloudTrigger` | 1 | ✓ | 6 | 2 | [schema](nodes/n8n-nodes-base.venafiTlsProtectCloudTrigger.md) |
| Venafi TLS Protect Datacenter | `n8n-nodes-base.venafiTlsProtectDatacenter` | 1 |  | 6 | 2 | [schema](nodes/n8n-nodes-base.venafiTlsProtectDatacenter.md) |
| Venafi TLS Protect Datacenter Trigger | `n8n-nodes-base.venafiTlsProtectDatacenterTrigger` | 1 | ✓ | 6 | 2 | [schema](nodes/n8n-nodes-base.venafiTlsProtectDatacenterTrigger.md) |
| Vero | `n8n-nodes-base.vero` | 1 |  | 8 | 1 | [schema](nodes/n8n-nodes-base.vero.md) |
| Vonage | `n8n-nodes-base.vonage` | 1 |  | 1 | 15 | [schema](nodes/n8n-nodes-base.vonage.md) |
| Wait | `n8n-nodes-base.wait` | 1.1 |  | 0 | 6 | [schema](nodes/n8n-nodes-base.wait.md) |
| Webex by Cisco | `n8n-nodes-base.ciscoWebex` | 1 |  | 6 | 3 | [schema](nodes/n8n-nodes-base.ciscoWebex.md) |
| Webex by Cisco Trigger | `n8n-nodes-base.ciscoWebexTrigger` | 1 | ✓ | 6 | 3 | [schema](nodes/n8n-nodes-base.ciscoWebexTrigger.md) |
| Webflow | `n8n-nodes-base.webflow` | 2 |  | 6 | 4 | [schema](nodes/n8n-nodes-base.webflow.md) |
| Webflow Trigger | `n8n-nodes-base.webflowTrigger` | 1 | ✓ | 5 | 4 | [schema](nodes/n8n-nodes-base.webflowTrigger.md) |
| Webhook | `n8n-nodes-base.webhook` | 2.1 |  | 0 | 6 | [schema](nodes/n8n-nodes-base.webhook.md) |
| Wekan | `n8n-nodes-base.wekan` | 1 |  | 5 | 1 | [schema](nodes/n8n-nodes-base.wekan.md) |
| WhatsApp Business Cloud | `n8n-nodes-base.whatsApp` | 1.1 |  | 5 | 4 | [schema](nodes/n8n-nodes-base.whatsApp.md) |
| WhatsApp Trigger | `n8n-nodes-base.whatsAppTrigger` | 1.1 | ✓ | 5 | 4 | [schema](nodes/n8n-nodes-base.whatsAppTrigger.md) |
| Wise | `n8n-nodes-base.wise` | 1 |  | 8 | 3 | [schema](nodes/n8n-nodes-base.wise.md) |
| Wise Trigger | `n8n-nodes-base.wiseTrigger` | 1 | ✓ | 8 | 3 | [schema](nodes/n8n-nodes-base.wiseTrigger.md) |
| WooCommerce | `n8n-nodes-base.wooCommerce` | 1 |  | 5 | 2 | [schema](nodes/n8n-nodes-base.wooCommerce.md) |
| WooCommerce Trigger | `n8n-nodes-base.wooCommerceTrigger` | 1 | ✓ | 5 | 2 | [schema](nodes/n8n-nodes-base.wooCommerceTrigger.md) |
| Wordpress | `n8n-nodes-base.wordpress` | 1 |  | 4 | 2 | [schema](nodes/n8n-nodes-base.wordpress.md) |
| Workable Trigger | `n8n-nodes-base.workableTrigger` | 1 | ✓ | 0 | 2 | [schema](nodes/n8n-nodes-base.workableTrigger.md) |
| Workflow Trigger | `n8n-nodes-base.workflowTrigger` | 1 | ✓ | 0 | 2 | [schema](nodes/n8n-nodes-base.workflowTrigger.md) |
| Write Binary File | `n8n-nodes-base.writeBinaryFile` | 1 |  | 0 | 3 | [schema](nodes/n8n-nodes-base.writeBinaryFile.md) |
| Wufoo Trigger | `n8n-nodes-base.wufooTrigger` | 1 | ✓ | 0 | 2 | [schema](nodes/n8n-nodes-base.wufooTrigger.md) |
| X (Formerly Twitter) | `n8n-nodes-base.twitter` | 2 |  | 7 | 1 | [schema](nodes/n8n-nodes-base.twitter.md) |
| Xero | `n8n-nodes-base.xero` | 1 |  | 4 | 1 | [schema](nodes/n8n-nodes-base.xero.md) |
| XML | `n8n-nodes-base.xml` | 1 |  | 0 | 4 | [schema](nodes/n8n-nodes-base.xml.md) |
| Yourls | `n8n-nodes-base.yourls` | 1 |  | 3 | 1 | [schema](nodes/n8n-nodes-base.yourls.md) |
| YouTube | `n8n-nodes-base.youTube` | 1 |  | 9 | 1 | [schema](nodes/n8n-nodes-base.youTube.md) |
| Zammad | `n8n-nodes-base.zammad` | 1 |  | 6 | 2 | [schema](nodes/n8n-nodes-base.zammad.md) |
| Zendesk | `n8n-nodes-base.zendesk` | 1 |  | 20 | 5 | [schema](nodes/n8n-nodes-base.zendesk.md) |
| Zendesk Trigger | `n8n-nodes-base.zendeskTrigger` | 1 | ✓ | 20 | 5 | [schema](nodes/n8n-nodes-base.zendeskTrigger.md) |
| Zoho CRM | `n8n-nodes-base.zohoCrm` | 1 |  | 7 | 1 | [schema](nodes/n8n-nodes-base.zohoCrm.md) |
| Zoom | `n8n-nodes-base.zoom` | 1 |  | 5 | 2 | [schema](nodes/n8n-nodes-base.zoom.md) |
| Zulip | `n8n-nodes-base.zulip` | 1 |  | 10 | 1 | [schema](nodes/n8n-nodes-base.zulip.md) |

## AI / LangChain nodes (`@n8n/n8n-nodes-langchain.*`)

| Node | type | maxVer | trig | #ops | #params | schema |
|---|---|---|---|---|---|---|
| AI Agent | `@n8n/n8n-nodes-langchain.agent` | 3.1 |  | 0 | 6 | [schema](nodes/@n8n__n8n-nodes-langchain.agent.md) |
| AI Agent Tool | `@n8n/n8n-nodes-langchain.agentTool` | 3.1 |  | 0 | 6 | [schema](nodes/@n8n__n8n-nodes-langchain.agentTool.md) |
| Alibaba Cloud Chat Model | `@n8n/n8n-nodes-langchain.lmChatAlibabaCloud` | 1 |  | 0 | 3 | [schema](nodes/@n8n__n8n-nodes-langchain.lmChatAlibabaCloud.md) |
| Anthropic Chat Model | `@n8n/n8n-nodes-langchain.lmChatAnthropic` | 1.5 |  | 0 | 2 | [schema](nodes/@n8n__n8n-nodes-langchain.lmChatAnthropic.md) |
| Auto-fixing Output Parser | `@n8n/n8n-nodes-langchain.outputParserAutofixing` | 1 |  | 0 | 2 | [schema](nodes/@n8n__n8n-nodes-langchain.outputParserAutofixing.md) |
| AWS Bedrock Chat Model | `@n8n/n8n-nodes-langchain.lmChatAwsBedrock` | 1.1 |  | 0 | 3 | [schema](nodes/@n8n__n8n-nodes-langchain.lmChatAwsBedrock.md) |
| Azure OpenAI Chat Model | `@n8n/n8n-nodes-langchain.lmChatAzureOpenAi` | 1 |  | 0 | 0 | [schema](nodes/@n8n__n8n-nodes-langchain.lmChatAzureOpenAi.md) |
| Basic LLM Chain | `@n8n/n8n-nodes-langchain.chainLlm` | 1.9 |  | 0 | 0 | [schema](nodes/@n8n__n8n-nodes-langchain.chainLlm.md) |
| Binary Input Loader | `@n8n/n8n-nodes-langchain.documentBinaryInputLoader` | 1 |  | 0 | 7 | [schema](nodes/@n8n__n8n-nodes-langchain.documentBinaryInputLoader.md) |
| Calculator | `@n8n/n8n-nodes-langchain.toolCalculator` | 1 |  | 0 | 0 | [schema](nodes/@n8n__n8n-nodes-langchain.toolCalculator.md) |
| Call n8n Sub-Workflow Tool | `@n8n/n8n-nodes-langchain.toolWorkflow` | 2.2 |  | 0 | 11 | [schema](nodes/@n8n__n8n-nodes-langchain.toolWorkflow.md) |
| Character Text Splitter | `@n8n/n8n-nodes-langchain.textSplitterCharacterTextSplitter` | 1 |  | 0 | 3 | [schema](nodes/@n8n__n8n-nodes-langchain.textSplitterCharacterTextSplitter.md) |
| Chat | `@n8n/n8n-nodes-langchain.chat` | 1.4 |  | 1 | 16 | [schema](nodes/@n8n__n8n-nodes-langchain.chat.md) |
| Chat Memory Manager | `@n8n/n8n-nodes-langchain.memoryManager` | 1.1 |  | 0 | 7 | [schema](nodes/@n8n__n8n-nodes-langchain.memoryManager.md) |
| Chat Messages Retriever | `@n8n/n8n-nodes-langchain.memoryChatRetriever` | 1 |  | 0 | 2 | [schema](nodes/@n8n__n8n-nodes-langchain.memoryChatRetriever.md) |
| Chat Trigger | `@n8n/n8n-nodes-langchain.chatTrigger` | 1.4 | ✓ | 1 | 16 | [schema](nodes/@n8n__n8n-nodes-langchain.chatTrigger.md) |
| Code Tool | `@n8n/n8n-nodes-langchain.toolCode` | 1.3 |  | 0 | 7 | [schema](nodes/@n8n__n8n-nodes-langchain.toolCode.md) |
| Cohere Chat Model | `@n8n/n8n-nodes-langchain.lmChatCohere` | 1 |  | 0 | 2 | [schema](nodes/@n8n__n8n-nodes-langchain.lmChatCohere.md) |
| Cohere Model | `@n8n/n8n-nodes-langchain.lmCohere` | 1 |  | 0 | 1 | [schema](nodes/@n8n__n8n-nodes-langchain.lmCohere.md) |
| Contextual Compression Retriever | `@n8n/n8n-nodes-langchain.retrieverContextualCompression` | 1 |  | 0 | 0 | [schema](nodes/@n8n__n8n-nodes-langchain.retrieverContextualCompression.md) |
| Data to Summarize | `@n8n/n8n-nodes-langchain.operationMode` | 2.1 |  | 0 | 5 | [schema](nodes/@n8n__n8n-nodes-langchain.operationMode.md) |
| DeepSeek Chat Model | `@n8n/n8n-nodes-langchain.lmChatDeepSeek` | 1 |  | 0 | 3 | [schema](nodes/@n8n__n8n-nodes-langchain.lmChatDeepSeek.md) |
| Default Data Loader | `@n8n/n8n-nodes-langchain.documentDefaultDataLoader` | 1.1 |  | 0 | 9 | [schema](nodes/@n8n__n8n-nodes-langchain.documentDefaultDataLoader.md) |
| Embeddings AWS Bedrock | `@n8n/n8n-nodes-langchain.embeddingsAwsBedrock` | 1 |  | 0 | 1 | [schema](nodes/@n8n__n8n-nodes-langchain.embeddingsAwsBedrock.md) |
| Embeddings Azure OpenAI | `@n8n/n8n-nodes-langchain.embeddingsAzureOpenAi` | 1 |  | 0 | 2 | [schema](nodes/@n8n__n8n-nodes-langchain.embeddingsAzureOpenAi.md) |
| Embeddings Cohere | `@n8n/n8n-nodes-langchain.embeddingsCohere` | 1 |  | 0 | 2 | [schema](nodes/@n8n__n8n-nodes-langchain.embeddingsCohere.md) |
| Embeddings Google Gemini | `@n8n/n8n-nodes-langchain.embeddingsGoogleGemini` | 1 |  | 0 | 2 | [schema](nodes/@n8n__n8n-nodes-langchain.embeddingsGoogleGemini.md) |
| Embeddings Google Vertex | `@n8n/n8n-nodes-langchain.embeddingsGoogleVertex` | 1 |  | 0 | 3 | [schema](nodes/@n8n__n8n-nodes-langchain.embeddingsGoogleVertex.md) |
| Embeddings Hugging Face Inference | `@n8n/n8n-nodes-langchain.embeddingsHuggingFaceInference` | 1 |  | 0 | 3 | [schema](nodes/@n8n__n8n-nodes-langchain.embeddingsHuggingFaceInference.md) |
| Embeddings Lemonade | `@n8n/n8n-nodes-langchain.embeddingsLemonade` | 1 |  | 0 | 0 | [schema](nodes/@n8n__n8n-nodes-langchain.embeddingsLemonade.md) |
| Embeddings Mistral Cloud | `@n8n/n8n-nodes-langchain.embeddingsMistralCloud` | 1 |  | 0 | 2 | [schema](nodes/@n8n__n8n-nodes-langchain.embeddingsMistralCloud.md) |
| Embeddings Ollama | `@n8n/n8n-nodes-langchain.embeddingsOllama` | 1 |  | 0 | 0 | [schema](nodes/@n8n__n8n-nodes-langchain.embeddingsOllama.md) |
| Embeddings OpenAI | `@n8n/n8n-nodes-langchain.embeddingsOpenAi` | 1.2 |  | 0 | 1 | [schema](nodes/@n8n__n8n-nodes-langchain.embeddingsOpenAi.md) |
| Embeddings Oracle Database | `@n8n/n8n-nodes-langchain.embeddingsOracleDb` | 1 |  | 0 | 0 | [schema](nodes/@n8n__n8n-nodes-langchain.embeddingsOracleDb.md) |
| GitHub Document Loader | `@n8n/n8n-nodes-langchain.documentGithubLoader` | 1.1 |  | 0 | 4 | [schema](nodes/@n8n__n8n-nodes-langchain.documentGithubLoader.md) |
| Google Vertex Chat Model | `@n8n/n8n-nodes-langchain.lmChatGoogleVertex` | 1 |  | 0 | 2 | [schema](nodes/@n8n__n8n-nodes-langchain.lmChatGoogleVertex.md) |
| Groq Chat Model | `@n8n/n8n-nodes-langchain.lmChatGroq` | 1 |  | 0 | 2 | [schema](nodes/@n8n__n8n-nodes-langchain.lmChatGroq.md) |
| Guardrails | `@n8n/n8n-nodes-langchain.guardrails` | 3.4 |  | 2 | 0 | [schema](nodes/@n8n__n8n-nodes-langchain.guardrails.md) |
| HTTP Request Tool | `@n8n/n8n-nodes-langchain.toolHttpRequest` | 1.1 |  | 0 | 16 | [schema](nodes/@n8n__n8n-nodes-langchain.toolHttpRequest.md) |
| Hugging Face Inference Model | `@n8n/n8n-nodes-langchain.lmOpenHuggingFaceInference` | 1 |  | 0 | 2 | [schema](nodes/@n8n__n8n-nodes-langchain.lmOpenHuggingFaceInference.md) |
| In Memory Vector Store Insert | `@n8n/n8n-nodes-langchain.vectorStoreInMemoryInsert` | 1 |  | 0 | 3 | [schema](nodes/@n8n__n8n-nodes-langchain.vectorStoreInMemoryInsert.md) |
| In Memory Vector Store Load | `@n8n/n8n-nodes-langchain.vectorStoreInMemoryLoad` | 1 |  | 0 | 1 | [schema](nodes/@n8n__n8n-nodes-langchain.vectorStoreInMemoryLoad.md) |
| Information Extractor | `@n8n/n8n-nodes-langchain.informationExtractor` | 1.2 |  | 0 | 4 | [schema](nodes/@n8n__n8n-nodes-langchain.informationExtractor.md) |
| Item List Output Parser | `@n8n/n8n-nodes-langchain.outputParserItemList` | 1 |  | 0 | 1 | [schema](nodes/@n8n__n8n-nodes-langchain.outputParserItemList.md) |
| JSON Input Loader | `@n8n/n8n-nodes-langchain.documentJsonInputLoader` | 1 |  | 0 | 2 | [schema](nodes/@n8n__n8n-nodes-langchain.documentJsonInputLoader.md) |
| LangChain Code | `@n8n/n8n-nodes-langchain.code` | 1 |  | 0 | 4 | [schema](nodes/@n8n__n8n-nodes-langchain.code.md) |
| Lemonade Chat Model | `@n8n/n8n-nodes-langchain.lmChatLemonade` | 1 |  | 0 | 0 | [schema](nodes/@n8n__n8n-nodes-langchain.lmChatLemonade.md) |
| Lemonade Model | `@n8n/n8n-nodes-langchain.lmLemonade` | 1 |  | 0 | 0 | [schema](nodes/@n8n__n8n-nodes-langchain.lmLemonade.md) |
| Manual Chat Trigger | `@n8n/n8n-nodes-langchain.manualChatTrigger` | 1.1 | ✓ | 0 | 2 | [schema](nodes/@n8n__n8n-nodes-langchain.manualChatTrigger.md) |
| MCP Client | `@n8n/n8n-nodes-langchain.mcpClient` | 1.1 |  | 0 | 8 | [schema](nodes/@n8n__n8n-nodes-langchain.mcpClient.md) |
| MCP Client Tool | `@n8n/n8n-nodes-langchain.mcpClientTool` | 1.3 |  | 0 | 8 | [schema](nodes/@n8n__n8n-nodes-langchain.mcpClientTool.md) |
| MCP Registry Client (internal) | `@n8n/n8n-nodes-langchain.mcpRegistryClientTool` | 1 |  | 0 | 6 | [schema](nodes/@n8n__n8n-nodes-langchain.mcpRegistryClientTool.md) |
| MCP Server Trigger | `@n8n/n8n-nodes-langchain.mcpTrigger` | 2 | ✓ | 0 | 2 | [schema](nodes/@n8n__n8n-nodes-langchain.mcpTrigger.md) |
| Microsoft Agent 365 Trigger | `@n8n/n8n-nodes-langchain.microsoftAgent365Trigger` | 1.1 | ✓ | 0 | 10 | [schema](nodes/@n8n__n8n-nodes-langchain.microsoftAgent365Trigger.md) |
| MiniMax Chat Model | `@n8n/n8n-nodes-langchain.lmChatMinimax` | 1 |  | 0 | 2 | [schema](nodes/@n8n__n8n-nodes-langchain.lmChatMinimax.md) |
| Mistral Cloud Chat Model | `@n8n/n8n-nodes-langchain.lmChatMistralCloud` | 1 |  | 0 | 2 | [schema](nodes/@n8n__n8n-nodes-langchain.lmChatMistralCloud.md) |
| Model | `@n8n/n8n-nodes-langchain.type` | 1 |  | 0 | 2 | [schema](nodes/@n8n__n8n-nodes-langchain.type.md) |
| Model Selector | `@n8n/n8n-nodes-langchain.modelSelector` | 2 |  | 0 | 1 | [schema](nodes/@n8n__n8n-nodes-langchain.modelSelector.md) |
| MongoDB Chat Memory | `@n8n/n8n-nodes-langchain.memoryMongoDbChat` | 1.1 |  | 0 | 2 | [schema](nodes/@n8n__n8n-nodes-langchain.memoryMongoDbChat.md) |
| Moonshot Kimi Chat Model | `@n8n/n8n-nodes-langchain.lmChatMoonshot` | 1.1 |  | 0 | 3 | [schema](nodes/@n8n__n8n-nodes-langchain.lmChatMoonshot.md) |
| Motorhead | `@n8n/n8n-nodes-langchain.memoryMotorhead` | 1.4 |  | 0 | 2 | [schema](nodes/@n8n__n8n-nodes-langchain.memoryMotorhead.md) |
| MultiQuery Retriever | `@n8n/n8n-nodes-langchain.retrieverMultiQuery` | 1 |  | 0 | 1 | [schema](nodes/@n8n__n8n-nodes-langchain.retrieverMultiQuery.md) |
| NVIDIA Nemotron Chat Model | `@n8n/n8n-nodes-langchain.lmChatNvidia` | 1 |  | 0 | 3 | [schema](nodes/@n8n__n8n-nodes-langchain.lmChatNvidia.md) |
| NVIDIA Nemotron Embeddings | `@n8n/n8n-nodes-langchain.embeddingsNvidia` | 1 |  | 0 | 2 | [schema](nodes/@n8n__n8n-nodes-langchain.embeddingsNvidia.md) |
| Ollama Chat Model | `@n8n/n8n-nodes-langchain.lmChatOllama` | 1 |  | 0 | 0 | [schema](nodes/@n8n__n8n-nodes-langchain.lmChatOllama.md) |
| Ollama Model | `@n8n/n8n-nodes-langchain.lmOllama` | 1 |  | 0 | 0 | [schema](nodes/@n8n__n8n-nodes-langchain.lmOllama.md) |
| OpenAI | `@n8n/n8n-nodes-langchain.openAi` | 2.3 |  | 16 | 1 | [schema](nodes/@n8n__n8n-nodes-langchain.openAi.md) |
| OpenAI Assistant | `@n8n/n8n-nodes-langchain.openAiAssistant` | 1.1 |  | 0 | 9 | [schema](nodes/@n8n__n8n-nodes-langchain.openAiAssistant.md) |
| OpenAI Chat Model | `@n8n/n8n-nodes-langchain.lmChatOpenAi` | 1.3 |  | 0 | 5 | [schema](nodes/@n8n__n8n-nodes-langchain.lmChatOpenAi.md) |
| OpenAI Model | `@n8n/n8n-nodes-langchain.lmOpenAi` | 1 |  | 0 | 4 | [schema](nodes/@n8n__n8n-nodes-langchain.lmOpenAi.md) |
| OpenRouter Chat Model | `@n8n/n8n-nodes-langchain.lmChatOpenRouter` | 1 |  | 0 | 3 | [schema](nodes/@n8n__n8n-nodes-langchain.lmChatOpenRouter.md) |
| Pinecone: Insert | `@n8n/n8n-nodes-langchain.vectorStorePineconeInsert` | 1 |  | 0 | 3 | [schema](nodes/@n8n__n8n-nodes-langchain.vectorStorePineconeInsert.md) |
| Pinecone: Load | `@n8n/n8n-nodes-langchain.vectorStorePineconeLoad` | 1 |  | 0 | 2 | [schema](nodes/@n8n__n8n-nodes-langchain.vectorStorePineconeLoad.md) |
| Postgres Chat Memory | `@n8n/n8n-nodes-langchain.memoryPostgresChat` | 1.4 |  | 0 | 1 | [schema](nodes/@n8n__n8n-nodes-langchain.memoryPostgresChat.md) |
| Question and Answer Chain | `@n8n/n8n-nodes-langchain.chainRetrievalQa` | 1.7 |  | 0 | 3 | [schema](nodes/@n8n__n8n-nodes-langchain.chainRetrievalQa.md) |
| Recursive Character Text Splitter | `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter` | 1 |  | 0 | 3 | [schema](nodes/@n8n__n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter.md) |
| Redis Chat Memory | `@n8n/n8n-nodes-langchain.memoryRedisChat` | 1.6 |  | 0 | 2 | [schema](nodes/@n8n__n8n-nodes-langchain.memoryRedisChat.md) |
| Require Specific Output Format | `@n8n/n8n-nodes-langchain.hasOutputParser` | 2.2 |  | 0 | 5 | [schema](nodes/@n8n__n8n-nodes-langchain.hasOutputParser.md) |
| Reranker Cohere | `@n8n/n8n-nodes-langchain.rerankerCohere` | 1 |  | 0 | 2 | [schema](nodes/@n8n__n8n-nodes-langchain.rerankerCohere.md) |
| SearXNG | `@n8n/n8n-nodes-langchain.toolSearXng` | 1 |  | 0 | 1 | [schema](nodes/@n8n__n8n-nodes-langchain.toolSearXng.md) |
| Sentiment Analysis | `@n8n/n8n-nodes-langchain.sentimentAnalysis` | 1.1 |  | 0 | 3 | [schema](nodes/@n8n__n8n-nodes-langchain.sentimentAnalysis.md) |
| SerpApi (Google Search) | `@n8n/n8n-nodes-langchain.toolSerpApi` | 1 |  | 0 | 2 | [schema](nodes/@n8n__n8n-nodes-langchain.toolSerpApi.md) |
| Simple Memory | `@n8n/n8n-nodes-langchain.memoryBufferWindow` | 1.4 |  | 0 | 2 | [schema](nodes/@n8n__n8n-nodes-langchain.memoryBufferWindow.md) |
| Structured Output Parser | `@n8n/n8n-nodes-langchain.outputParserStructured` | 1.3 |  | 0 | 4 | [schema](nodes/@n8n__n8n-nodes-langchain.outputParserStructured.md) |
| Summarization Chain | `@n8n/n8n-nodes-langchain.chainSummarization` | 2.1 |  | 0 | 6 | [schema](nodes/@n8n__n8n-nodes-langchain.chainSummarization.md) |
| Supabase: Insert | `@n8n/n8n-nodes-langchain.vectorStoreSupabaseInsert` | 1 |  | 0 | 3 | [schema](nodes/@n8n__n8n-nodes-langchain.vectorStoreSupabaseInsert.md) |
| Supabase: Load | `@n8n/n8n-nodes-langchain.vectorStoreSupabaseLoad` | 1 |  | 0 | 2 | [schema](nodes/@n8n__n8n-nodes-langchain.vectorStoreSupabaseLoad.md) |
| Text Classifier | `@n8n/n8n-nodes-langchain.textClassifier` | 1.1 |  | 0 | 3 | [schema](nodes/@n8n__n8n-nodes-langchain.textClassifier.md) |
| Think Tool | `@n8n/n8n-nodes-langchain.toolThink` | 1.1 |  | 0 | 1 | [schema](nodes/@n8n__n8n-nodes-langchain.toolThink.md) |
| Tip: Get a feel for agents with our quick <a href="https://docs.n8n.io/advanced-ai/intro-tutorial/" target="_blank">tutorial</a> or see an <a href="/templates/1954" target="_blank">example</a> of how this node works | `@n8n/n8n-nodes-langchain.mySql` | 1.9 |  | 0 | 4 | [schema](nodes/@n8n__n8n-nodes-langchain.mySql.md) |
| Tip: Get a feel for agents with our quick <a href="https://docs.n8n.io/advanced-ai/intro-tutorial/" target="_blank">tutorial</a> or see an <a href="/workflows/templates/1954" target="_blank">example</a> of how this node works | `@n8n/n8n-nodes-langchain.aiAgentStarterCallout` | 2.2 |  | 0 | 5 | [schema](nodes/@n8n__n8n-nodes-langchain.aiAgentStarterCallout.md) |
| Token Splitter | `@n8n/n8n-nodes-langchain.textSplitterTokenSplitter` | 1 |  | 0 | 2 | [schema](nodes/@n8n__n8n-nodes-langchain.textSplitterTokenSplitter.md) |
| Tool Executor | `@n8n/n8n-nodes-langchain.toolExecutor` | 1 |  | 0 | 3 | [schema](nodes/@n8n__n8n-nodes-langchain.toolExecutor.md) |
| Vector Store Question Answer Tool | `@n8n/n8n-nodes-langchain.toolVectorStore` | 1.1 |  | 0 | 3 | [schema](nodes/@n8n__n8n-nodes-langchain.toolVectorStore.md) |
| Vector Store Retriever | `@n8n/n8n-nodes-langchain.retrieverVectorStore` | 1 |  | 0 | 1 | [schema](nodes/@n8n__n8n-nodes-langchain.retrieverVectorStore.md) |
| Vercel AI Gateway Chat Model | `@n8n/n8n-nodes-langchain.lmChatVercelAiGateway` | 1 |  | 0 | 3 | [schema](nodes/@n8n__n8n-nodes-langchain.lmChatVercelAiGateway.md) |
| Wikipedia | `@n8n/n8n-nodes-langchain.toolWikipedia` | 1 |  | 0 | 0 | [schema](nodes/@n8n__n8n-nodes-langchain.toolWikipedia.md) |
| Wolfram|Alpha | `@n8n/n8n-nodes-langchain.toolWolframAlpha` | 1 |  | 0 | 0 | [schema](nodes/@n8n__n8n-nodes-langchain.toolWolframAlpha.md) |
| Workflow Retriever | `@n8n/n8n-nodes-langchain.retrieverWorkflow` | 1.1 |  | 0 | 5 | [schema](nodes/@n8n__n8n-nodes-langchain.retrieverWorkflow.md) |
| xAI Grok Chat Model | `@n8n/n8n-nodes-langchain.lmChatXAiGrok` | 1 |  | 0 | 3 | [schema](nodes/@n8n__n8n-nodes-langchain.lmChatXAiGrok.md) |
| Xata | `@n8n/n8n-nodes-langchain.memoryXata` | 1.5 |  | 0 | 1 | [schema](nodes/@n8n__n8n-nodes-langchain.memoryXata.md) |
| Zep | `@n8n/n8n-nodes-langchain.memoryZep` | 1.4 |  | 0 | 3 | [schema](nodes/@n8n__n8n-nodes-langchain.memoryZep.md) |
| Zep Vector Store: Insert | `@n8n/n8n-nodes-langchain.vectorStoreZepInsert` | 1 |  | 0 | 4 | [schema](nodes/@n8n__n8n-nodes-langchain.vectorStoreZepInsert.md) |
| Zep Vector Store: Load | `@n8n/n8n-nodes-langchain.vectorStoreZepLoad` | 1 |  | 0 | 3 | [schema](nodes/@n8n__n8n-nodes-langchain.vectorStoreZepLoad.md) |
