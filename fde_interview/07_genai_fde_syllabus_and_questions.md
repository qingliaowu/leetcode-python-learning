# GenAI FDE Supplemental Syllabus and System Design Questions

[FDE track](./README.md) | [Google Cloud prep notes](./06_google_cloud_genai_fde_prep.md) | [Role map](./01_role_and_interview_map.md) | [Customer discovery](./02_customer_discovery_and_solutioning.md) | [Cloud fundamentals](./03_cloud_architecture_fundamentals.md) | [AI engineering](../ai_engineering/README.md) | [System design](../system_design/README.md)

## Purpose

This note documents a supplemental GenAI Forward Deployed Engineer interview
prep syllabus. Use it beside the official prep guide notes, not as a replacement
for them.

The syllabus points to three preparation areas:

| Area | What It Tests |
| --- | --- |
| Coding | Clean Python, basic data structures, algorithm reasoning, OOP, edge cases, and debugging without execution help |
| AI systems and architecture | Production GenAI design, reliability, orchestration, data integration, observability, and enterprise constraints |
| Engineering consulting and execution | Ambiguity handling, stakeholder discovery, tradeoff communication, and adapting as requirements change |

The main theme is simple: demonstrate calm raw problem-solving. In both coding
and system design, the interviewer wants to hear how you reason before they see
the final answer.

## Coding Interview Setup

Expect a Python interview in a Google virtual interview platform. The platform
may provide basic syntax highlighting, but you should not depend on autocomplete,
code correction, an interactive compiler, or an AI assistant.

Prepare for the live environment by practicing with these constraints:

| Constraint | Practice Habit |
| --- | --- |
| No autocomplete | Write common Python patterns from memory |
| No compiler | Dry-run syntax, variable names, indentation, and returns |
| No code correction | Keep functions small enough to inspect manually |
| No AI assistant | Rehearse your own problem-solving narration |
| Limited time | Start with a correct simple solution, then optimize |

Do not rush to type. Spend the first few minutes clarifying the problem,
constraints, expected input shape, output shape, scale, and edge cases. A slow,
organized start is stronger than fast typing followed by a rewrite.

## Coding Interview Behavior

Use this order:

| Step | Interview Move |
| ---: | --- |
| 1 | Restate the problem in your own words |
| 2 | Ask clarifying questions about constraints and edge cases |
| 3 | Name the data structure or algorithm shape |
| 4 | Explain the baseline approach |
| 5 | Discuss time and space complexity |
| 6 | Write clean Python |
| 7 | Dry-run at least one normal case and one edge case |
| 8 | Optimize only after the simple version is correct |

Think out loud. Good narration sounds like this:

```text
I am choosing a dictionary because I need average O(1) lookup by key. I will
handle empty input before the loop, then update the map as I scan the list once.
The time complexity should be O(n), and the extra space is O(k), where k is the
number of distinct keys.
```

Avoid long silence, but also avoid narrating every keystroke. Explain decisions,
invariants, edge cases, and tradeoffs.

## Coding Syllabus

The coding interview evaluates clean, efficient, production-ready code.

| Competency | What to Review | How to Demonstrate It |
| --- | --- | --- |
| Core data structures | Lists, strings, dictionaries, sets, stacks, queues, heaps, intervals, simple graphs, and classes | Choose the structure from the operations you need, not from habit |
| Operational constraints | Lookup, insertion, deletion, ordering, duplicates, memory, and mutation | Explain why one structure is better under the prompt's constraints |
| Algorithm optimization | O(1), O(log n), O(n), O(n log n), O(n^2), and space tradeoffs | Identify the bottleneck and improve the actual expensive step |
| Robust implementation | Empty input, one item, duplicates, invalid values, large values, and tie behavior | Dry-run edge cases before the interviewer asks |
| OOP design | State, methods, invariants, encapsulation, and update order | Keep state transitions explicit and testable |

High-yield repo practice:

| Pattern | Lesson |
| --- | --- |
| Practical no-compiler drills | [High-priority practical coding questions](./08_high_priority_practical_coding_questions.md) |
| Hash map grouping | [49 Group Anagrams](../arrays_strings/0049_group_anagrams.md) |
| Frequency counting | [347 Top K Frequent Elements](../heaps/0347_top_k_frequent_elements.md) |
| Stack parsing | [394 Decode String](../stacks_queues/0394_decode_string.md) |
| Intervals | [56 Merge Intervals](../intervals_search/0056_merge_intervals.md) |
| Binary search | [704 Binary Search](../intervals_search/0704_binary_search.md) |
| Binary search on answer | [875 Koko Eating Bananas](../intervals_search/0875_koko_eating_bananas.md) |
| Graph dependencies | [207 Course Schedule](../trees_graphs/0207_course_schedule.md) |
| OOP cache | [146 LRU Cache](../design_data_structures/0146_lru_cache.md) |
| Time-indexed state | [981 Time Based Key-Value Store](../design_data_structures/0981_time_based_key_value_store.md) |

Focus on Medium-level questions. Complex hard puzzles are lower priority than
fluently solving practical strings, lists, dictionaries, and simple stateful
classes.

## AI Systems and Architecture Syllabus

The RRK interview tests whether you can design and implement GenAI solutions
that meet enterprise standards. Do not stop at "call an LLM." Design the system
around the model.

| Competency | What to Review | How to Demonstrate It |
| --- | --- | --- |
| System reliability | Fault tolerance, retries, idempotency, circuit breakers, workflow state, and fallback | Explain what happens when the model, retriever, database, or tool call fails |
| Non-deterministic behavior | LLM variability, evaluation, guardrails, refusals, and human review | Describe how the system remains predictable enough for production |
| Multi-step orchestration | Agents, tools, state machines, queues, compensation, and timeouts | Bound each step with ownership, validation, and recovery |
| Secure execution boundaries | Identity, authorization, secrets, audit, tenant isolation, and tool permissions | Prevent the model from becoming an uncontrolled actor |
| Data integration | Ingestion, parsing, normalization, metadata, freshness, and lineage | Show how data becomes usable context without losing source traceability |
| Storage paradigms | Relational stores, object storage, search indexes, vector indexes, caches, streams, and warehouses | Match each storage choice to access patterns and consistency needs |
| Retrieval mechanisms | Keyword search, embeddings, hybrid search, metadata filters, reranking, and citations | Connect retrieval quality to answer quality and trust |
| Observability | Metrics, logs, traces, quality dashboards, feedback, and alerts | Track both system health and AI output quality |
| Quality baselines | Golden sets, expert review, offline evals, online feedback, and regression tests | Compare each new version against a known baseline |

Production GenAI design has two layers:

```text
model behavior
    +
application controls, data boundaries, workflow state, evaluation, and operations
```

The second layer is what makes the first layer safe enough to use.

## Engineering Consulting and Execution Syllabus

As an FDE, you are expected to solve technical problems with strategic
stakeholders. That means your answer must discover the real problem, not simply
display technical knowledge.

| Competency | What to Practice | Strong Signal |
| --- | --- | --- |
| Navigating ambiguity | Turn broad prompts into users, outcomes, constraints, and success metrics | You ask questions that change the design |
| Business rule discovery | Identify policies, exceptions, approval paths, and ownership | You do not automate a rule you have not understood |
| Technical communication | Explain architecture choices in clear tradeoff language | You can go deep without losing the customer outcome |
| Dynamic adaptation | Incorporate new constraints while preserving structure | You revise the recommendation instead of defending the first idea |
| Execution planning | Proof, pilot, hardening, rollout, support, and measurement | You know how a demo becomes production |

Use this sentence when the prompt is broad:

```text
Before I design the system, I want to understand the workflow, users, current
baseline, constraints, and what evidence would make this worth shipping.
```

## System Design Answer Template

Use this structure for the system design questions below:

| Step | What to Cover |
| ---: | --- |
| 1 | Clarify customer, users, workflow, and success metric |
| 2 | Define functional requirements and out-of-scope items |
| 3 | Define scale, latency, availability, privacy, and cost assumptions |
| 4 | Choose the high-level architecture |
| 5 | Specify APIs, data model, and workflow states |
| 6 | Deep-dive on AI quality, retrieval, orchestration, or reliability |
| 7 | Explain security, tenant isolation, and compliance controls |
| 8 | Explain observability, evaluation, rollout, and failure handling |
| 9 | Discuss tradeoffs and changed assumptions |

For GenAI prompts, always include:

- who is allowed to see which data,
- where context comes from and how fresh it is,
- how the answer is evaluated or validated,
- what happens when confidence or evidence is insufficient,
- how cost and latency are bounded,
- who owns the final decision when the action is consequential.

## System Design Question Bank

Use these for timed 45-60 minute mocks. Spend the first five minutes only on
clarifying questions.

### 1. Internal Policy Assistant

Design an AI assistant that answers employee questions using internal policy
documents. Answers must include citations and respect document permissions.

Focus areas:

- permission-aware retrieval,
- document ingestion and freshness,
- answer grounding and refusal behavior,
- evaluation set and expert review,
- audit logs and privacy boundaries.

Follow-up constraints:

- documents change daily,
- some policies are region-specific,
- executives want answers in Slack and the intranet,
- legal requires every factual claim to be traceable.

### 2. Customer Support Copilot

Design a copilot that helps support agents draft responses to customer tickets.
Agents must approve every outbound response.

Focus areas:

- user workflow integration,
- retrieval from tickets, knowledge base, and customer records,
- human-in-the-loop approval,
- draft quality metrics,
- safe rollout from pilot to production.

Follow-up constraints:

- 2,000 agents handle 40,000 tickets per day,
- p95 draft latency must stay under five seconds,
- wrong refund advice creates financial risk,
- product documentation is incomplete.

### 3. Enterprise Document Ingestion Pipeline

Design a pipeline that ingests PDFs, web pages, spreadsheets, and internal wiki
pages for GenAI retrieval.

Focus areas:

- parsing and normalization,
- chunking strategy,
- metadata and lineage,
- indexing for keyword and vector retrieval,
- retries, dead-letter queues, and reprocessing.

Follow-up constraints:

- source permissions must be preserved,
- duplicate documents are common,
- documents can be deleted under retention policy,
- re-indexing must not take the assistant offline.

### 4. Multi-Tenant GenAI Platform

Design a platform that lets enterprise customers build GenAI apps on shared
infrastructure while keeping each tenant isolated.

Focus areas:

- tenant isolation,
- quotas and fair scheduling,
- model and prompt versioning,
- per-tenant data stores or metadata filters,
- billing and cost attribution.

Follow-up constraints:

- one tenant sends 100 times more traffic than others,
- premium customers require stronger SLOs,
- tenants need custom tools and private data connectors,
- the platform must support regional data residency.

### 5. AI Evaluation and Regression Service

Design a service that evaluates prompts, retrieval, and model versions before
they are released to production.

Focus areas:

- golden datasets,
- offline and online evaluation,
- human review,
- safety and quality metrics,
- release gates and rollback.

Follow-up constraints:

- labels are expensive,
- model outputs are non-deterministic,
- business teams want fast prompt iteration,
- bad releases must be detected within one hour.

### 6. Tool-Using Agent With Approval

Design an AI agent that can look up customer information, draft a recommendation,
and create a support case action only after human approval.

Focus areas:

- secure tool execution,
- scoped permissions,
- state machine orchestration,
- approval workflow,
- idempotency and audit.

Follow-up constraints:

- tool APIs are slow and sometimes fail,
- the same request may be retried,
- managers need an approval history,
- certain actions require two-person approval.

### 7. Slow Website Troubleshooting System

Design an observability and troubleshooting approach for a website that a
marketing manager reports as slow.

Focus areas:

- symptom clarification,
- client, CDN, network, app, database, and dependency metrics,
- tracing and release correlation,
- safe mitigation,
- prevention and runbooks.

Follow-up constraints:

- only users in one region are affected,
- the issue began after a deployment,
- CDN hit rate dropped sharply,
- database latency looks normal.

### 8. Personalized Product Recommendation Assistant

Design a GenAI assistant that recommends products to customers based on catalog
data, user behavior, and policy constraints.

Focus areas:

- structured and unstructured data integration,
- ranking and explanation,
- privacy and consent,
- cache strategy,
- A/B testing and business metrics.

Follow-up constraints:

- recommendations must avoid restricted products,
- product availability changes every few minutes,
- users can request explanations,
- the assistant must not reveal sensitive profile attributes.

### 9. Meeting Notes to CRM Updates

Design a system that summarizes sales calls and proposes CRM updates for account
executives to review.

Focus areas:

- audio or transcript ingestion,
- entity extraction,
- proposed structured updates,
- human review and correction,
- audit and rollback.

Follow-up constraints:

- transcripts contain confidential customer information,
- salespeople use different terminology,
- CRM writes must be idempotent,
- managers want adoption and accuracy metrics.

### 10. Codebase Onboarding Assistant

Design an assistant that helps new engineers understand a large internal
codebase and answer questions with source references.

Focus areas:

- repository indexing,
- code-aware retrieval,
- permission boundaries,
- answer citations,
- freshness after commits.

Follow-up constraints:

- repositories are very large,
- access differs by team,
- answers must distinguish fact from inference,
- stale architecture explanations are dangerous.

### 11. AI Incident Triage Assistant

Design an assistant that helps on-call engineers triage production incidents
using logs, metrics, traces, deploy history, and runbooks.

Focus areas:

- observability data integration,
- time-windowed retrieval,
- hypothesis generation,
- safe recommendations,
- escalation and audit.

Follow-up constraints:

- incident data is noisy,
- recommendations must not execute production changes automatically,
- p95 response time matters during outages,
- the assistant should learn from resolved incidents.

### 12. Contract Review Assistant

Design a GenAI workflow that helps legal teams review vendor contracts and flag
risky clauses.

Focus areas:

- document parsing,
- clause extraction,
- policy retrieval,
- risk classification,
- human approval and audit.

Follow-up constraints:

- contracts contain highly sensitive data,
- policy changes must apply to future reviews,
- false negatives are more costly than false positives,
- reviewers need explanations and source snippets.

### 13. Invoice Exception Automation

Design a system that detects invoice exceptions, summarizes the reason, and
routes the invoice to the correct approver.

Focus areas:

- structured ERP data and unstructured invoice files,
- deterministic rules versus AI classification,
- workflow state,
- idempotent routing,
- exception metrics.

Follow-up constraints:

- duplicate invoices are common,
- approval rules vary by region,
- the AI must not approve payment by itself,
- finance wants cost savings measured against a baseline.

### 14. Knowledge Base Freshness Monitor

Design a system that detects stale or conflicting knowledge base articles used
by a customer-facing AI assistant.

Focus areas:

- content versioning,
- conflict detection,
- ownership routing,
- evaluation impact,
- suppression or fallback rules.

Follow-up constraints:

- multiple teams own articles,
- stale content caused a customer escalation,
- updates need review before publication,
- the assistant must avoid citing suppressed documents.

### 15. GenAI Cost Control Layer

Design a cost control layer for a GenAI platform used by many internal teams.

Focus areas:

- budgets and quotas,
- model routing,
- caching,
- request admission,
- cost attribution and alerts.

Follow-up constraints:

- one team accidentally creates a runaway batch job,
- leadership wants cost per useful outcome,
- some workflows are more latency-sensitive than others,
- teams need visibility without seeing each other's data.

### 16. Secure Data Connector Framework

Design a framework for connecting enterprise data sources such as Drive, Jira,
Slack, databases, and internal APIs to GenAI applications.

Focus areas:

- connector authentication,
- incremental sync,
- permission mapping,
- secret management,
- connector health and retries.

Follow-up constraints:

- external APIs have rate limits,
- credentials expire,
- permissions change frequently,
- customers need to disable a connector quickly.

### 17. AI-Powered Search Migration

Design a migration from existing keyword search to hybrid search with keyword,
embedding, metadata filtering, and reranking.

Focus areas:

- baseline search quality,
- dual-write or dual-index strategy,
- ranking evaluation,
- latency and cost,
- rollback.

Follow-up constraints:

- customers depend on exact-match behavior,
- embedding models may change,
- the index contains private tenant data,
- search traffic has sharp weekday peaks.

### 18. Production Demo to Pilot

Design the path from a promising GenAI demo to a production pilot for one
enterprise customer.

Focus areas:

- proof criteria,
- hardening checklist,
- identity and data controls,
- deployment ownership,
- pilot measurement and exit criteria.

Follow-up constraints:

- the demo used manually curated data,
- the customer wants production in four weeks,
- the security team has not approved data movement,
- users are skeptical because a previous tool failed.

## How to Review an Answer

After each mock, score yourself from 0 to 4:

| Score | Meaning |
| ---: | --- |
| 0 | I could not start without hints |
| 1 | I named pieces but missed the workflow or customer outcome |
| 2 | I produced a basic architecture but missed important risks |
| 3 | I covered requirements, architecture, tradeoffs, security, and operations |
| 4 | I adapted well when constraints changed and explained production rollout |

Record one specific weakness:

```text
Weak note: "My design was messy."
Useful note: "I chose vector search before asking whether source permissions
must be enforced per user."
```

Then choose the next drill:

| Weakness | Next Drill |
| --- | --- |
| Asked few clarifying questions | Spend five minutes writing only discovery questions |
| Jumped to products too soon | Redesign using provider-neutral categories |
| Forgot security | Trace one request and mark auth, data, and audit at every step |
| Forgot observability | Add product, quality, reliability, safety, and cost metrics |
| Got lost in AI details | Restate the user workflow and business outcome |
| Gave no tradeoffs | Compare two options and name the migration trigger |

## Check Your Understanding

Try each question before opening its answer. Focus on the first decision you
would make in a live interview.

### Question 1: Choose the First Design Question

If you have only one day to practice system design for a GenAI FDE interview,
which question from the bank should you do first and why?

<details>
<summary>Show answer and explanation</summary>

Start with either `Customer Support Copilot` or `Internal Policy Assistant`.
Both force the core GenAI FDE skills: stakeholder discovery, permission-aware
retrieval, human review, evaluation, rollout, observability, and customer value.
They are better first mocks than a narrow infrastructure prompt because they
combine AI architecture with consulting and execution.

</details>

### Question 2: Repair a Weak Mock

During a mock, you immediately chose vector search before asking about
permissions, document freshness, or success metrics. What should your repair
drill be?

<details>
<summary>Show answer and explanation</summary>

Redo the first five minutes of the mock using only discovery questions. Ask who
uses the system, what outcome must improve, which data sources exist, how
permissions work, how fresh answers must be, what baseline exists, and what
failure would block rollout. Then recommend retrieval only after the requirements
make it necessary.

</details>
