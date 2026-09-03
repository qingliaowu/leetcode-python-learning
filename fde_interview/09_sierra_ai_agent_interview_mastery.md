# Sierra AI Agent Interview Mastery Plan

[FDE track](./README.md) | [High-priority coding drills](./08_high_priority_practical_coding_questions.md) | [Supplemental syllabus](./07_genai_fde_syllabus_and_questions.md) | [Enterprise AI adoption](./05_enterprise_ai_adoption.md) | [AI engineering](../ai_engineering/README.md) | [System design](../system_design/README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## Purpose

This is the Sierra-specific mastery plan. It turns the shared Sierra interview
strategy into a repeatable study track.

Use it when the target role is Sierra Software Engineer, Agent, Agent Engineer,
Forward Deployed Infrastructure Engineer, or another customer-facing AI agent
role.

## Sources Checked

- [Shared ChatGPT Sierra strategy](https://chatgpt.com/share/6a992f64-3270-83ee-ba8d-8cc47f8b6738)
- [Sierra: The AI-native interview](https://sierra.ai/blog/the-ai-native-interview)
- [Sierra careers](https://sierra.ai/careers)
- [Sierra: The challenge with rolling your own agent](https://sierra.ai/blog/the-challenge-with-rolling-your-own-agent)
- [Sierra: Voice AI is only as good as what it hears](https://sierra.ai/blog/voice-ai-is-only-as-good-as-what-it-hears)
- [Sierra: Context engineering](https://sierra.ai/blog/context-engineering-the-key-to-great-agents)
- [Sierra: tau-voice benchmark](https://sierra.ai/blog/tau-voice-benchmarking-real-time-voice-agents-on-real-world-tasks)

As of the checked sources, Sierra publicly describes an AI-native onsite with
`Plan`, `Build`, and `Review`, and says its phone screen moved toward system
design. However, real loops can vary by role, country, timing, and recruiter
guidance. If your recruiter confirms a no-AI live coding round, follow that
constraint exactly.

## Mastery Target

The goal is not to memorize one old question. The goal is to become reliable at
this loop:

```text
ambiguous product or coding prompt
    -> clarify the real requirement
    -> build the smallest correct version
    -> handle follow-up requirements without breaking the design
    -> find edge cases before the interviewer does
    -> explain production risks, tests, and customer impact
```

Before the interview, you should be able to:

- solve practical Python prompts without autocomplete, compiler help, or AI,
- handle incremental requirements in the final 10-15 minutes,
- design a production customer-service AI agent,
- explain voice-agent latency, transcription, turn-taking, and evaluation,
- use AI tools thoughtfully when the format explicitly allows them,
- review your own code and explain what you verified yourself,
- turn a bug or weak round into a clear learning story.

## Priority Allocation

Use this split when time is limited:

| Area | Time | Why It Matters |
| --- | ---: | --- |
| Practical coding and debugging | 35% | You need clean Python, edge-case discipline, and follow-up resilience |
| System design | 25% | Sierra emphasizes production systems, scaling, tradeoffs, and path to production |
| AI agent and voice architecture | 20% | The company builds customer-facing conversational agents, including voice |
| Product thinking and AI-native build | 15% | The onsite may test scoping, product judgment, pivoting, and review quality |
| Behavioral and values | 5% | You still need concise stories showing ownership, judgment, and customer impact |

Do not spend most of this track on LeetCode Hard. Your highest return is
practical implementation plus production reasoning.

## Daily Mastery Loop

Every practice block should include all five steps:

```text
Example -> Edge cases -> Implementation -> Manual trace -> Tests
```

After writing code, pause for 30-60 seconds and check:

- empty input,
- single item,
- duplicate values,
- missing keys,
- malformed input,
- boundary values,
- unexpected API response,
- repeated request or retry,
- sorted versus unsorted input,
- follow-up requirement that changes output shape.

This pause is part of the performance, not an optional cleanup.

## High-Priority Coding Drills

First, master the three short practical drills:

| Order | Drill | Why First |
| ---: | --- | --- |
| 1 | [Filter Duplicates](./08_high_priority_practical_coding_questions.md#1-filter-duplicates) | Set membership and stable output order |
| 2 | [Count Word Frequencies](./08_high_priority_practical_coding_questions.md#2-count-word-frequencies) | Dictionary counting and deterministic sorted output |
| 3 | [Merge Person Data](./08_high_priority_practical_coding_questions.md#3-merge-person-data) | Parsing, grouping, merging, and output formatting |

Then practice these Sierra-style prompts. Each should be solved in parts so you
train incremental requirement handling.

| Priority | Prompt | Core Skills | Follow-up Pressure |
| --- | --- | --- | --- |
| High | Accept-Language parser | String parsing, sorting by preference, fallback | Wildcards, malformed weights, supported-language matching |
| High | API client with retry | Exceptions, timeout, retryable errors, clean loops | 429, 5xx, jitter, max retries, idempotency |
| High | Nested JSON flatten | Recursion or stack, path building, type checks | Lists, nulls, custom separators, max depth |
| High | Connected components | Graph construction, BFS or DFS, visited set | Disconnected nodes, cycles, large input |
| High | Dependency graph | Topological sort, cycle detection | Multiple valid orders, missing dependency, partial deploy |
| Medium | Tree traversal | DFS or BFS, state per node | Filtering, path output, early stop |
| Medium | Log parser | String parsing, dictionaries, time windows | Invalid rows, grouping, top-k errors |
| Medium | Rate limiter | State design, time windows, fairness | Per-user quotas, cleanup, burst behavior |
| Medium | Pagination client | Loops, API boundaries, deduplication | Retry pages, stop tokens, partial failure |
| Medium | LRU or TTL cache | OOP state, dictionary, order or expiry | Updates, eviction, time injection, stale entries |

For every prompt, write four parts:

```text
Part 1: simplest correct behavior
Part 2: validation or malformed input
Part 3: scale, retry, ordering, or performance requirement
Part 4: production concern and tests
```

## Coding Explanation Template

Use this in live coding:

```text
I will first solve the smallest version. The main state is [state]. The invariant
is [what remains true after each loop]. This gives [time] time and [space]
space. After coding, I will dry-run the sample and then check [edge cases].
```

For retry/API prompts, add:

```text
Before retrying a write, I would ask whether the operation is idempotent or
whether an idempotency key is available. Retrying a POST blindly can duplicate a
side effect.
```

## System Design Master Prompt

Master this one first:

```text
Design a customer-service AI agent for a large enterprise. It supports chat and
voice, answers customer questions, calls enterprise tools, escalates to humans
when needed, and must be safe enough for production.
```

A strong high-level flow:

```text
customer
    -> chat or voice channel
    -> ASR for voice
    -> conversation session and state store
    -> agent orchestrator
    -> context selection and retrieval
    -> LLM or model router
    -> policy and tool permission layer
    -> CRM, billing, order, or ticketing APIs
    -> response validation
    -> TTS for voice
    -> logs, traces, evaluation, and human handoff
```

Cover these topics without waiting to be asked:

- conversation state,
- authentication,
- PII handling,
- tool permissions,
- retrieval and context freshness,
- hallucination prevention,
- retries and idempotency,
- human handoff,
- latency budget,
- observability,
- offline and online evaluation,
- auditability,
- prompt and model versioning,
- model fallback,
- cost and concurrency.

## Voice Agent Deep Dive

Voice is a strong differentiator. Prepare to explain that voice-agent quality is
not just LLM reasoning.

| Layer | What to Discuss |
| --- | --- |
| ASR | Transcription accuracy, names, accents, noise, domain vocabulary, language switching |
| Turn-taking | Barge-in, silence detection, interruptions, backchannels, endpointing |
| Context | Account data, expected names, journey state, policy, glossary, previous turns |
| Agent reasoning | Intent, policy, tool choice, refusal, escalation, recovery |
| Tool calls | Latency, authorization, retries, idempotency, external failures |
| TTS | Naturalness, pronunciation, brand voice, language support |
| Evaluation | Task success, utterance errors, escalation rate, latency, user satisfaction |

Useful sentence:

```text
For a production voice agent, I would measure ASR accuracy, end-to-end latency,
turn-taking quality, tool latency, task completion, escalation quality, and
conversation-level safety separately. A charming call is not enough if the
underlying task fails.
```

## Context Engineering Deep Dive

Sierra's public writing emphasizes that agents need the right context at the
right moment. Use this architecture language:

```text
small starting context
    -> detect intent, state, and conditions
    -> unlock only relevant journeys, tools, policies, knowledge, memory, and
       glossary
    -> execute bounded actions through permissioned tools
    -> log decision state and evaluate the result
```

Context blocks to mention:

- journey,
- tool,
- rule or policy,
- workflow,
- knowledge,
- memory,
- glossary,
- response phrasing.

Tradeoff:

```text
Too little context causes missing facts. Too much context increases latency,
cost, distraction, and hallucination risk. The design should progressively
disclose relevant context based on conversation state.
```

## Plan-Build-Review Rehearsal

If the format allows AI coding tools, your skill is not typing all code by hand.
Your skill is directing the build and judging the result.

### Plan

Choose a small product in your domain:

```text
Enterprise multilingual voice customer-service agent
```

Define:

- user and business problem,
- success metric,
- MVP scope,
- out-of-scope items,
- data model,
- agent flow,
- tool API contract,
- test cases,
- production risks.

### Build

Build only the useful core:

```text
customer message
    -> classify intent
    -> retrieve or select context
    -> call mocked enterprise API
    -> return response
    -> escalate when confidence or policy fails
```

Skip heavy boilerplate unless it is the product. It is acceptable to cut scope if
the cut is thoughtful and visible.

### Review

Prepare to answer:

- Why this data model?
- Why this abstraction?
- What breaks at 100x scale?
- What would change for production?
- What did AI generate?
- What did you verify yourself?
- What would you test next?
- Where are the security risks?
- What would you instrument first?
- How would you roll this out to one customer?

## Behavioral Stories to Prepare

Prepare six two-minute stories:

| Story | Signal |
| --- | --- |
| Ambiguous customer need to production system | Discovery, ownership, delivery |
| Production incident or debugging | Evidence-first troubleshooting |
| Saying no or narrowing scope | Judgment and customer trust |
| Improving AI quality with evaluation | Production agent maturity |
| Cutting scope to meet a deadline | Prioritization and communication |
| Your bug and prevention loop | Humility, root cause, process repair |

Use this structure:

```text
situation -> constraint -> action I personally took -> result -> lesson
```

If discussing a recent coding miss, convert it cleanly:

```text
bug -> root cause -> missing test -> process change -> how I now catch it
```

## Seven-Day Sierra Plan

Use this if the interview is soon:

| Day | Focus | Required Output |
| ---: | --- | --- |
| 1 | Practical parsing and dictionaries | Solve the three high-priority practical drills without running code |
| 2 | Nested structures and graphs | Solve nested JSON flatten and connected components |
| 3 | API client | Implement retry, backoff, timeout, pagination, and idempotency discussion |
| 4 | System design | Mock the customer-service AI agent design for 45 minutes |
| 5 | Voice architecture | Mock a multilingual voice agent with ASR, TTS, latency, and eval |
| 6 | Plan-Build-Review | Build a two-hour mini project and write review notes |
| 7 | Full rehearsal | Coding, system design, product review, and two behavioral stories |

## Scorecard

| Skill | 0 | 2 | 4 |
| --- | --- | --- | --- |
| Practical coding | Cannot finish simple version | Works with hints but misses edge cases | Solves, traces, tests, and handles follow-up |
| Debugging | Guesses cause | Finds symptom but not root cause | Uses evidence, reproduces, fixes, prevents |
| System design | Names components | Draws flow but misses production risks | Covers state, tools, security, eval, cost, rollout |
| Voice architecture | Says ASR and TTS | Mentions latency and transcription | Explains turn-taking, context, recovery, and metrics |
| Product judgment | Builds too much or too little | Reasonable MVP but weak metric | Clear scope, metric, tradeoffs, and customer impact |
| Review quality | Says it works | Explains some choices | Critiques data model, tests, risks, and AI usage |
| Behavioral | Generic story | Specific but not tied to role | Shows builder judgment and learning loop |

Mastery target: score `3` or `4` in every row on two separate days.

## Final Readiness Gate

You are ready when you can:

- solve `Merge Person Data` from scratch in 35 minutes,
- implement an API retry loop and explain idempotency,
- flatten nested JSON and explain recursion versus stack,
- run BFS or DFS without losing the visited invariant,
- design the customer-service AI agent in 45 minutes,
- deep-dive voice evaluation without vague model talk,
- explain context engineering as progressive disclosure,
- complete one Plan-Build-Review mini project,
- name the security and privacy risks in your own project,
- tell six concise stories without hiding behind "we".

## Check Your Understanding

Try each question before opening its answer. Say the answer aloud in interview
style.

### Question 1: Choose the First Repair

You solved Parts 1 and 2 of a practical coding prompt, but Part 3 added a
follow-up requirement and your code became inconsistent. What should you repair
first in your practice process?

<details>
<summary>Show answer and explanation</summary>

Repair the incremental-change loop. Before editing code for a follow-up, restate
the new requirement, identify which invariant changes, update the smallest
affected state, and re-run the original example plus the new follow-up example.
Do not patch randomly. The practice habit is:

```text
new requirement -> affected state -> invariant -> minimal edit -> old tests ->
new tests
```

This directly targets the failure mode where later requirements break earlier
behavior.

</details>

### Question 2: Design the Voice Agent Deep Dive

In a Sierra-style system design answer, why is it not enough to say "use ASR,
LLM, and TTS" for a voice agent?

<details>
<summary>Show answer and explanation</summary>

That names the pipeline but not the production design. A strong answer explains
how the system handles transcription errors, noisy audio, accents, names,
language switching, barge-in, turn-taking, tool latency, authentication, PII,
human escalation, evaluation, model fallback, and observability. The interviewer
needs evidence that the candidate can operate a real customer-facing agent, not
only connect three model APIs.

</details>
