# Token Economics for AI Models

## Executive summary

Tokens are the accounting unit most LLM APIs use for **context limits, rate limits, and billing**: providers “tokenize” your text into model-specific pieces (often subwords plus whitespace/punctuation), then charge separately for **input tokens** (what you send) and **output tokens** (what the model generates). citeturn33search0turn33search4turn39view0turn38view0

Across major providers, a practical English rule of thumb is that **1 token ≈ ~4 characters** (and ~0.75 words), but this varies by vendor/tokenizer and by language (e.g., Anthropic notes ~3.5 English characters per token). citeturn33search0turn33search2turn34search0turn33search4

Token pricing is usually published in **USD per 1M tokens** (MTok) and differs by: model family, input vs output, long-context thresholds, and discounts such as **batch** (often ~50% cheaper) and **prompt/context caching** (cheaper cache reads; sometimes more expensive cache writes). citeturn8search24turn38view0turn39view0turn25search1turn32view0

“Tokens” are **not equivalent across vendors/models**: the same text can tokenize differently (different vocabularies/algorithms), providers may insert system/format tokens (often not billed), and long-context requests may move you onto higher unit prices. citeturn31view1turn33search20turn38view0turn39view0turn8search24

Real-world budgeting has two dominant spend patterns: (1) **flat subscriptions** (great for interactive use; token caps are usually not transparent), and (2) **API usage** (predictable per-unit economics; scales linearly with volume but can jump at long-context thresholds). Developer behavior evidence suggests many teams experience “bring your own AI” spend: a 2026 survey found **35%** of developers use leading AI tools through **personal accounts**, and **over 50%** use ChatGPT via personal accounts—signals that individuals often pay out-of-pocket even when companies have AI programs. citeturn36search0turn38view2

## Tokens and tokenization basics

A “token” is the smallest unit a model processes when reading or writing. Tokens can be whole words (“the”), subwords (“token” + “ization”), punctuation, or whitespace-attached fragments (many tokenizers include a leading space in the token). citeturn33search4turn33search0

### How tokens map to characters and words

Rules of thumb are helpful for estimation, not accounting:

- For many OpenAI model/tokenizer setups: **1 token ≈ 4 characters** and **100 tokens ≈ 75 words**, with examples like “1 paragraph ≈ 100 tokens.” citeturn33search0turn33search4  
- For Gemini models: **1 token ≈ 4 characters**, and **100 tokens ≈ ~60–80 English words**. citeturn33search2turn33search16  
- For Claude: a token “approximately represents **3.5 English characters**,” but varies by language/content. citeturn34search0  

A useful mental model is to treat tokens as **compressed text bytes**: OpenAI’s reference tokenizer implementation (BPE) notes that “on average… each token corresponds to about **4 bytes**,” which explains why token counts don’t match word counts and why different languages (or code) can tokenize less efficiently. citeturn33search3

### What tokenization is doing under the hood

Most LLM tokenizers are designed to balance **compression** (fewer tokens for the same text) with **generalization** (reusing common subword pieces like “ing”). citeturn33search3 Tokenization itself is an active research area; recent work on improving “characters per token” highlights that efficiency can shift materially with different tokenizer designs—one reason vendors’ token counts are not interchangeable. citeturn33academia40

## Converting tokens to dollars

This section provides a budgeting method and representative official prices. Prices below are **list prices** in **USD** unless a source explicitly indicates otherwise; enterprise contracts can differ. citeturn38view0turn39view0turn25search1turn8search24turn32view0

### Pricing units and the core formula

Most vendors quote:

- **Input price**: $ / 1M input tokens  
- **Output price**: $ / 1M output tokens  
- Sometimes: **cached input / cache reads**, **cache writes**, **batch pricing**, and **long-context tiers**. citeturn38view0turn39view0turn8search24  

A standard cost calculation (no caching, no batch) is:

\[
\text{Cost} =
\left(\frac{\text{InputTokens}}{10^6}\right)\cdot P_\text{in} +
\left(\frac{\text{OutputTokens}}{10^6}\right)\cdot P_\text{out}
\]

Assumptions you must set (and should document) include: expected input/output ratio, whether you reuse prompts (caching helps), whether you can defer work (batch helps), and whether some requests exceed long-context thresholds. citeturn38view0turn39view0turn8search24  

### Representative official token prices across vendors

Official list pricing examples (selected representative “text” models for comparison):

- OpenAI: published per-model MTok rates for input, cached input, and output. citeturn8search24turn37search16  
- Anthropic: published MTok rates plus prompt caching multipliers, batch prices, and long-context tiers. citeturn38view0  
- Google Gemini API: published MTok rates, batch discount, context caching prices (including storage), and long-context breakpoints (<=200k vs >200k prompt sizes for some models). citeturn39view0  
- Microsoft Azure OpenAI: pricing is token-based and includes options such as pay-as-you-go and provisioned throughput units (PTUs), and describes batch discounts (50% discount for batch in the Azure pricing description). citeturn25search1turn25search2  
- Cohere: lists MTok prices for legacy and current Command family models and explains token billing at a high level. citeturn31view0turn31view1  
- xAI: lists per-million token prices for Grok-family models and notes separate pricing for large contexts. citeturn30view2  
- Mistral: publishes model prices (e.g., Medium 3 at $0.4/$2 per MTok; earlier family price updates like $2/$6 for Mistral Large). citeturn29view0turn29view1  
- AWS Bedrock: publishes per-model MTok prices and explicitly supports multiple service tiers; it also notes batch inference can be priced at **50% lower** than on-demand for select models. citeturn32view0turn26search5  

### Charts

![Representative per-1K token prices by vendor (input vs output)](sandbox:/mnt/data/per_1k_token_costs_by_vendor.png)

Figure notes: This chart converts official list prices from **$/1M tokens** to **$/1K tokens** (divide by 1000). The representative models used are: OpenAI gpt-5-mini; Anthropic Claude Haiku 4.5; Google Gemini 3.1 Flash‑Lite Preview; Microsoft Azure OpenAI GPT‑5.2 (Global); xAI grok‑4‑1‑fast‑reasoning; Cohere Command R (03‑2024); Mistral Medium 3; and AWS Bedrock’s Mistral Large 3 on-demand. citeturn8search24turn38view0turn39view0turn25search2turn30view2turn31view0turn29view0turn26search5  

![Cost scaling with volume under a fixed output ratio](sandbox:/mnt/data/cost_scaling_with_volume.png)

Figure notes: This shows linear scale-up of API spend when **output tokens = input/4** (a common-ish ratio for many summarization/assistant workloads, but not universal). Prices are taken from the same official pages as above for OpenAI gpt-5-mini, Anthropic Claude Sonnet 4.6, and Google Gemini 3.1 Flash‑Lite Preview. citeturn8search24turn38view0turn39view0  

### Worked example: “cost to process 1M tokens”

Because input and output have different prices, “1M tokens” must be defined. Below are three standard ways teams define it:

- **1M input tokens only** (e.g., embed/classify/long-context read-heavy tasks)  
- **1M output tokens only** (generation-heavy)  
- **1M total tokens as 750k input + 250k output** (a common budgeting convention when you need one number)

Representative results (USD):

| Provider (representative model) | 1M input | 1M output | 750k in + 250k out |
|---|---:|---:|---:|
| OpenAI gpt-5-mini | $0.25 | $2.00 | $0.6875 |
| Anthropic Claude Sonnet 4.6 | $3.00 | $15.00 | $6.00 |
| Google Gemini 3.1 Flash‑Lite Preview | $0.25 | $1.50 | $0.5625 |
| Microsoft Azure OpenAI GPT‑5.2 (Global) | $1.75 | $14.00 | $4.8125 |
| xAI grok‑4‑1‑fast‑reasoning | $0.20 | $0.50 | $0.275 |
| Cohere Command R (03‑2024) | $0.50 | $1.50 | $0.75 |
| Mistral Medium 3 | $0.40 | $2.00 | $0.80 |

These numbers come directly from each vendor’s published $/MTok, multiplied by the scenario’s MTok quantities. citeturn8search24turn38view0turn39view0turn25search2turn30view2turn31view0turn29view0  

## Why tokens are not equivalent across models and vendors

Even when two vendors both say “$X per 1M tokens,” the underlying “token” can differ in ways that change both **token counts** and **effective cost per character/word**.

### Different tokenizers mean different token counts

Tokenizers differ in vocabulary size, merge rules, training corpora, and special-token conventions. OpenAI’s reference tokenizer is BPE-based and reports ~4 bytes/token average; other providers use different systems and can achieve different compression efficiency on the same text. citeturn33search3turn33academia40

This matters most for:

- Non-English scripts (where tokenization efficiency can be worse or better than English rules of thumb). citeturn34search0turn33search0  
- Code, JSON, and punctuation-heavy text (often more tokens than “word count” suggests). citeturn33search3turn33search0  

### Providers may add invisible tokens, often not billed

Two important “gotchas” show up in official docs:

- Anthropic warns that token counts can include tokens “added automatically… for system optimizations,” and clarifies users are **not billed for system-added tokens**; billing reflects user content. citeturn33search20  
- Cohere distinguishes “tokens” vs “billed units”: there are situations where Cohere adds tokens under the hood (or produces special tokens), and those are **not charged** as billed tokens. citeturn31view1  

These design choices improve reliability/formatting but complicate “token-for-token” cost comparisons.

### “Long context” creates pricing discontinuities

Many vendors charge **higher unit prices** when prompt/context length crosses a threshold:

- Anthropic: for certain 1M-context configurations, requests exceeding **200K input tokens** can be charged at premium long-context rates. citeturn38view0  
- Google Gemini API: some models price prompts **<=200k vs >200k tokens** at different rates. citeturn39view0  
- OpenAI: published pricing includes distinct rates tied to long context thresholds (e.g., separate entries for certain context-length bands). citeturn8search24  

Budget implication: average cost per token can jump for a minority of “giant context” requests; that’s why many production systems implement chunking, retrieval, and caching.

### “Output tokens” can include thinking/reasoning tokens

Some vendors explicitly state that **output token charges include internal thinking tokens** (or similar). Google’s Gemini pricing calls out that output price includes “thinking tokens” for certain models. citeturn39view0 OpenAI similarly notes that “text output tokens include model reasoning tokens.” citeturn37search16turn8search24

That means two responses with the same visible text length might have different billed output tokens depending on how much “thinking” the model used.

### Pricing units aren’t always tokens

Within the broader “genAI pricing” space, some services bill per **character** or per **request** (and multimodal inputs can be converted into token-like units). For example, Google’s Vertex AI pricing guidance references the “~4 characters per text token” relationship and also includes non-token billing for some offerings. citeturn33search22turn27search18

Practical takeaway: treat “token” as a **provider-local meter**, not a universal unit like a kilowatt-hour.

## Typical token volumes and what small, medium, and large look like

This section defines sizing bands that are practical for forecasting. These are **heuristics**: actual usage depends on product design (RAG vs long prompts), guardrails, tool calls, language mix, and how much output you allow. citeturn33search0turn34search4turn38view0turn39view0

### A user-friendly way to reason about volume

Start from the “text unit” estimates:

- 1–2 sentences ≈ 30 tokens  
- 1 paragraph ≈ 100 tokens  
- 100 tokens ≈ 75 words citeturn33search0  

Then scale by “turns”:

- A short chat turn might be ~100 input + ~200 output = ~300 tokens  
- A code-assist turn that includes a stack trace or diff can be thousands of tokens  
- Agentic workflows can burn surprisingly large overhead: Anthropic notes tool definitions/results can sometimes consume **50,000+ tokens** before an agent even reads the user request. citeturn34search4  

### Suggested sizing bands

These bands are expressed as **total tokens per month** (input + output). If you budget separately, you can apply your expected output ratio.

**Individuals**
- Small: **< 1M tokens/month** (light daily Q&A, short summaries). This corresponds to roughly “a few hundred” short turns per day using the OpenAI rule-of-thumb conversions. citeturn33search0  
- Medium: **1M–50M tokens/month** (daily coding help + frequent doc/paste analysis; occasional long contexts). citeturn34search4turn33search0  
- Large: **50M–500M tokens/month** (power users running local agents, heavy code review, long transcripts, or multiple projects). citeturn34search4turn38view0  

**Startups (API-backed product)**
- Small: **50M–1B tokens/month** (early traction; a few thousand–tens of thousands of requests/day at ~1k tokens each). citeturn33search0turn39view0  
- Medium: **1B–10B tokens/month** (meaningful customer base, RAG + tool calls, A/B testing models). citeturn38view0turn39view0  
- Large: **10B–100B tokens/month** (high-traffic assistant/search/coding product or multi-tenant enterprise tooling). citeturn39view0turn38view0  

**Enterprises**
- Small: **10B–100B tokens/month** (a department-scale deployment, or a few high-volume workflows). citeturn34search7turn36search0  
- Medium: **100B–1T tokens/month** (company-wide copilots + customer support + document processing). citeturn36search0turn34search4  
- Large: **> 1T tokens/month** (platform-scale deployments, multiple business units, ubiquitous assistants). citeturn34search7turn39view0turn38view0  

### Anchoring examples from official implementation guides

- Anthropic content moderation guide gives a “social media at scale” example: **1B posts/month**, ~100 characters/post, estimated **28.6B input tokens** and **1.5B output tokens** under stated assumptions—an enterprise-scale token footprint. citeturn34search7  
- Anthropic legal summarization guide estimates **86M input tokens** for 1,000 long agreements (300M characters total), showing how large corpora translate into tens of millions of tokens even before generation. citeturn34search3  
- Microsoft documentation for an Azure content understanding scenario explicitly works through token costs (e.g., 1,000 pages leading to ~1.1M input tokens under stated assumptions), illustrating “department-scale” workloads that are still meaningful but not massive. citeturn2search0  

## Spending scenarios and budgeting guidance

This section provides estimates (with transparent assumptions) and separates **subscriptions** from **API usage**. All API estimates use official list prices and assume USD; subscription pricing may vary by region and may include taxes depending on how it’s presented. citeturn37search13turn37search7turn37search26turn37search4turn38view2

### Subscriptions

Subscriptions are best understood as paying for **interactive access under “reasonable use” policies**, rather than a predictable cost-per-token. For example:

- ChatGPT Plus was announced at **$20/month**. citeturn37search4  
- Claude Pro is stated as **$20/month (US)** (with local currency variations and potential tax differences by region). citeturn37search13  
- Google One AI Premium (Gemini Advanced access) was launched at **$19.99/month** in Google’s own product blog announcement. citeturn37search26  
- Google’s higher-end Gemini subscription offerings can be much higher (e.g., Google AI Ultra shown as **$249.99/month** on the subscriptions page). citeturn37search6  
- Microsoft bundles consumer AI access into Microsoft 365 plans and advertises **$19.99/month** for a plan that “includes Copilot for subscription owner.” citeturn37search7  
- For dev tooling adjacent to LLM usage, GitHub Copilot lists **$10/month** for Copilot Pro (personal) and higher tiers. citeturn35search8  

Budget implication: subscriptions are often cost-effective for **human-in-the-loop** work, but are harder to map to tokens unless the service publishes explicit caps (many do not, or caps change dynamically). citeturn38view2turn37search13  

### API usage

API spend is more forecastable. Below are illustrative monthly and annual costs under four archetypes, using the earlier representative model prices. (Assumption: token counts are already known or estimated; caching/batch discounts are not applied unless stated.)

**Individual hobbyist** (2M input + 1M output per month)  
- Rough range across representative models: about **$0.90/month** (xAI grok fast) to **$21/month** (Claude Sonnet 4.6). citeturn30view2turn38view0  

**Individual power user** (100M input + 30M output per month)  
- Rough range: **$35/month** (xAI grok fast) to **$750/month** (Claude Sonnet 4.6), before discounts like batch/caching. citeturn30view2turn38view0turn39view0  

**Startup product** (1B input + 0.3B output per month)  
- Rough range: **$350/month** (xAI grok fast) to **$7,500/month** (Claude Sonnet 4.6). citeturn30view2turn38view0  

**Large enterprise** (50B input + 10B output per month)  
- Rough range: **$15K/month** (xAI grok fast) to **$300K/month** (Claude Sonnet 4.6), before discounts/committed capacity. citeturn30view2turn38view0  

These ranges are intentionally wide because model selection dominates cost; many orgs run **routing** (cheap model for most requests, premium model for hard cases) and lean on batch + caching. citeturn39view0turn38view0turn32view0  

### Discounts and cost-optimization primitives that change the curve

Common vendor mechanisms visible in official docs include:

- **Batch**: Google’s Gemini API explicitly advertises “Batch API (50% cost reduction)” for paid tier, and publishes separate batch pricing tables. citeturn39view0  
- **Prompt/context caching**:  
  - Anthropic publishes cache write and cache hit prices (e.g., cache hits at a fraction of base input) and separate multipliers. citeturn38view0turn34search22  
  - Google publishes “context caching price” and an hourly storage price per million cached tokens. citeturn39view0  
  - OpenAI publishes “cached input” prices for multiple models and notes that output includes reasoning tokens. citeturn8search24turn37search16  
- **Reserved/committed throughput**: Azure OpenAI describes Provisioned Throughput Units (PTUs) with reservations and positions it as a predictability and cost-control option; AWS Bedrock offers multiple tiers and also offers provisioned throughput constructs across providers. citeturn25search1turn32view0  

### Mermaid flowchart: how cost typically scales with volume

```mermaid
flowchart TD
  A[Define workload] --> B[Estimate token volume: input + output]
  B --> C{Mostly interactive human use?}
  C -->|Yes| D[Consider per-seat subscription\n(limits often policy-based)]
  C -->|No / mixed| E[Use API pay-as-you-go\n(track tokens by feature, team, tenant)]
  E --> F{Reuse the same long prompt/context?}
  F -->|Yes| G[Add caching\n(cache hits cheaper; writes may cost more)]
  F -->|No| H[Optimize prompts + retrieval\navoid unnecessary long context]
  E --> I{Can requests run asynchronously?}
  I -->|Yes| J[Use batch processing\n(often ~50% cheaper)]
  I -->|No| K[Route requests:\nsmall model default, large model fallback]
  E --> L{Sustained high volume?}
  L -->|Yes| M[Consider committed capacity / provisioned throughput\nand negotiate volume discounts]
  L -->|No| N[Keep on-demand + monitor anomalies]
```

### Do developers spend personal money

Evidence indicates that personal spend is common, especially when governance lags adoption:

- The 2026 Sonar “State of Code Developer Survey” reports a “personal account problem”: **35%** of developers access top AI tools through personal accounts, with **over 50%** using ChatGPT through personal accounts; it frames this as a “bring your own AI (BYOAI) culture.” citeturn36search0  
- Stack Overflow survey reporting shows AI tool usage is widespread among developers (e.g., 2024: “76% … are using or planning to use AI tools,” and 2025 shows broad adoption trends), which increases the likelihood of unmanaged, personally expensed usage when enterprise provisioning is incomplete. citeturn35search10turn35search0  

## Vendor pricing and pricing-model comparison

This table summarizes how major providers meter tokens and structure discounts. When a detail is not publicly specified on an official page, it is explicitly marked.

| Vendor | API unit price model | Notable published modifiers | Subscription / seat pricing signals | Committed-use / enterprise notes |
|---|---|---|---|---|
| OpenAI | $/MTok input, cached input, output (varies by model) citeturn8search24 | Cached input rates; output tokens include reasoning tokens citeturn37search16turn8search24 | ChatGPT Plus announced $20/month (consumer); other plans published on pricing page but may be regionally presented citeturn37search4turn38view2 | Enterprise pricing via sales for some plans; API list prices are public citeturn38view2turn8search24 |
| Anthropic | $/MTok base input and output by model; explicit cache write/hit pricing citeturn38view0 | Batch prices; long-context tiering; prompt caching multipliers citeturn38view0turn34search22 | Claude Pro is $20/month (US) per support docs; higher tiers exist but not always fully enumerated on one static page citeturn37search13turn38view0 | Notes on regional endpoint premiums on some third-party platforms; enterprise via sales citeturn38view0 |
| Google | Gemini API: $/MTok input/output; batch + context caching + storage price; long-context breakpoints (<=200k vs >200k) citeturn39view0 | Batch “50% cost reduction”; context caching; grounding billed per search query after free quota citeturn39view0 | Google One AI Premium launched at $19.99/month (Gemini Advanced); higher “Ultra” plan shown at $249.99/month citeturn37search26turn37search6 | “Enterprise” is positioned via Vertex AI and explicitly mentions volume-based discounts citeturn39view0 |
| Microsoft | Azure OpenAI is token-based (input/output) with deployment scopes (global/data zone/regional); PTUs described for predictable costs; batch discount described citeturn25search1turn25search2 | PTUs; batch (50% discount mentioned in Azure pricing text); regionality options citeturn25search1turn25search2 | Microsoft 365 Premium plan includes Copilot for $19.99/month (consumer bundle) citeturn37search7 | Enterprise and government purchasing programs; pricing varies by region and deployment type citeturn25search1turn25search2 |
| xAI | $/MTok input/output by model family; separate large-context pricing noted citeturn30view2 | Large context charged at higher input/output rates per page notes citeturn30view2 | Consumer subscription pricing not analyzed here (not consistently published as “per token”) | Enterprise positioning via API + sales contact on site citeturn30view2 |
| Cohere | $/MTok input/output by model family (published on pricing page); trial vs production keys citeturn31view0turn31view1 | Distinguishes billed tokens vs generic tokens; some tokens not billed citeturn31view1 | Subscription vs API varies; main customer path is API keys (trial free, production paid) citeturn31view0 | Enterprise deployments exist; some pricing may be negotiated citeturn31view0 |
| Mistral AI | Public model prices in announcements (e.g., Medium 3 at $0.4/$2 per MTok; other family price updates) citeturn29view0turn29view1 | Emphasizes reduced prices and a free API tier in announcements; partner platform pricing referenced citeturn29view1 | Consumer “Le Chat” plans exist (API pricing tab appears dynamic on pricing page; not fully captured as static text) citeturn28view0turn29view1 | Enterprise deployments via contact; model can be deployed on multiple clouds citeturn29view0 |
| Amazon Web Services | Bedrock publishes per-model MTok prices and multiple tiers (Standard/Flex/Priority/Reserved) citeturn32view0 | Batch inference at 50% lower price for select models; tier premiums/discounts described citeturn32view0turn26search5 | Not a single “assistant subscription” model; it’s a cloud service meter | Reserved/provisioned throughput and enterprise purchasing are core to AWS pricing citeturn32view0 |

### Key budgeting takeaways from the comparison

Output tokens are often several times more expensive than input tokens (clear in most official tables), so controlling maximum output length and using structured responses are first-order levers. citeturn38view0turn39view0turn8search24

The biggest practical drivers of spend variance are: (a) model choice (often >10× spread), (b) output/input ratio, (c) long-context tier thresholds, and (d) whether you can exploit batch + caching. citeturn38view0turn39view0turn32view0turn8search24

Finally, “shadow AI” and personal accounts are not just governance issues—they can become real fragmentation in cost attribution and procurement. The Sonar survey’s personal-account findings are a concrete indicator that organizations should expect mixed funding sources unless they implement sanctioned tooling and reimbursements clearly. citeturn36search0