# Google Cloud GenAI FDE Prep Notes

[FDE track](./README.md) | [Role map](./01_role_and_interview_map.md) | [Customer discovery](./02_customer_discovery_and_solutioning.md) | [Cloud fundamentals](./03_cloud_architecture_fundamentals.md) | [AI engineering](../ai_engineering/README.md) | [System design](../system_design/README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## Source Checked

This note documents `/Users/qingliaowu/Downloads/system-design.pdf`.

The PDF metadata title is `GenAI Forward Deployed Engineer (FDE) Prep Doc -
Updated 4/15/2026 (Download as PDF)`. It is a five-page Google Cloud interview
preparation guide. The rendered pages are readable and organized into:

1. cover and table of contents,
2. role overview and interview process,
3. role-related knowledge topics,
4. coding interview topics,
5. additional resources.

The document is preparation guidance, not an exhaustive syllabus. Use it to
prioritize practice, then rehearse with timed mocks.

## Role Signal

The role is described as an embedded builder for customer GenAI deployments.
The important signal is that this is not only architecture advice. The candidate
is expected to help turn frontier AI products into production reality inside
customer environments.

Prepare evidence that you can:

- move from ambiguous customer needs to a concrete technical plan,
- code, debug, and ship customer-facing or customer-specific solutions,
- handle integration, data readiness, and state-management blockers,
- reason about enterprise production quality instead of demo-only success,
- communicate lessons learned to customers and internal product teams,
- stay effective when the work is novel, unclear, or changing.

Connect every technical answer back to customer value. In this role, a strong
design is one the customer can actually operate, trust, and adopt.

## Interview Process

The PDF describes this flow:

| Stage | What Happens | Preparation Focus |
| --- | --- | --- |
| Initial call | Recruiter explains the role and learns about your experience | Clarify interview format, expected language, and role-specific priorities |
| Interview preparation | Review the guide and additional resources | Build a focused plan for RRK, coding, GenAI, cloud, and system design |
| Virtual interviews | Two virtual interviews, with possible interviewer shadowing | Expect one RRK interview and one coding interview |
| RRK | Role Related Knowledge, 60 minutes | Discovery, architecture, GenAI, cloud, troubleshooting, security, scale, cost |
| Coding | Coding, 60 minutes | Python, OOP, clear requirements, algorithm explanation, test cases |
| Final review | Calibrated review of interview feedback | No action except staying responsive to the recruiter |

## RRK Interview Map

The RRK interview moves from high-level discovery into deeper architecture. The
PDF names these core evaluation areas:

| Area | What to Be Ready to Show | Repo Practice |
| --- | --- | --- |
| AI/ML engineering | Integrate models into a working application, not just call an API | [LLM fundamentals](../ai_engineering/01_llm_product_fundamentals.md), [RAG systems](../ai_engineering/02_rag_systems.md) |
| Operational excellence | Reliability, resilience, monitoring, performance, and recovery | [Cloud fundamentals](./03_cloud_architecture_fundamentals.md), [foundational patterns](../system_design/foundational_patterns.md) |
| Security, privacy, compliance | Protect sensitive customer or internal data | [enterprise AI adoption](./05_enterprise_ai_adoption.md) |
| Scalability | Explain what changes between internal scale and public scale | [system design guide](../system_design/README.md) |
| Performance and cost | Balance latency, throughput, resource usage, and unit economics | [cloud cost and capacity](./03_cloud_architecture_fundamentals.md#8-cost-and-capacity) |

Do not treat these as separate trivia categories. A realistic answer often
touches all of them at once.

## GenAI Concepts to Review

For this role, GenAI knowledge should be practical and production-oriented.
Prepare to discuss:

- where an LLM belongs in an application workflow,
- when RAG is better than fine-tuning,
- how prompts, retrieval, tools, and validation interact,
- how to evaluate model outputs before and after launch,
- how to troubleshoot poor answers, high latency, cost spikes, and regressions,
- how to serve models with versioning, fallback, monitoring, and rollout gates,
- how GenAI changes a customer's workflow, not only the UI.

A useful sentence shape:

```text
I would first define the workflow and success metric, then decide whether the
model should retrieve, draft, classify, summarize, or call a tool. After that I
would design the surrounding controls: permissions, evaluation, logging,
fallback, cost limits, and rollout.
```

## Application Development

The PDF expects comfort with designing, building, testing, deploying, and
explaining the value of a demo to a customer.

For practice, prepare one demo story using this structure:

| Part | What to Say |
| --- | --- |
| User | Who used the demo and what job they needed to complete |
| Workflow | What happened before and after your application existed |
| Technical core | The API, data model, integration, or model workflow you built |
| Reliability | How you handled errors, retries, invalid input, and observability |
| Customer value | What became faster, safer, cheaper, or clearer |
| Next step | What would be needed before production rollout |

Avoid describing only the stack. The interviewer needs to hear judgment.

## Consulting and Discovery

Interviewers want to know how you uncover stakeholder needs and make
recommendations. Use the [COSTAR framework](./02_customer_discovery_and_solutioning.md#the-costar-framework):

| Letter | Interview Move |
| --- | --- |
| C | Identify users, buyer, operator, security owner, and decision-maker |
| O | Ask what outcome must improve and how it is measured |
| S | Understand current systems, data, constraints, and failed attempts |
| T | Compare options with explicit tradeoffs |
| A | Propose proof, hardening, rollout, training, and ownership |
| R | Name risks, detection, prevention, and response owner |

The key habit: ask enough questions to make the design relevant, then move into
a recommendation once the problem is clear enough.

## Cloud Technology

The PDF says the interviews are not GCP-specific, but recommends familiarity
with relevant Google Cloud product names and value proposition.

Prepare in two layers:

1. Explain the cloud category without a product name.
2. Then map the category to the provider the interviewer wants to discuss.

Examples:

| Requirement | Category to Explain First |
| --- | --- |
| Expose an HTTP application safely | Load balancer, API gateway, identity, WAF, TLS |
| Run stateless application code | Managed containers or serverless request service |
| Process slow or bursty work | Durable queue and worker fleet |
| Store uploaded files | Object storage with lifecycle, encryption, and signed access |
| Search private documents | Search or vector index with metadata filters and permission checks |
| Observe production behavior | Metrics, logs, traces, business events, alerts |
| Control cost | Quotas, budgets, autoscaling, batching, model choice, caching |

Use [Cloud Architecture Fundamentals](./03_cloud_architecture_fundamentals.md)
as the base map.

## Troubleshooting Pattern

The PDF highlights structured troubleshooting for distributed systems, network,
and web scenarios. A sample prompt is:

```text
Your marketing manager says the new company website is slow. What would you do?
```

Use this order:

1. Clarify the symptom: who is affected, when it started, which pages, which
   regions, and what "slow" means.
2. Check scope: all users or one segment, web only or API too, new release or
   traffic spike.
3. Find evidence: client timings, CDN/cache hit rate, load balancer metrics,
   server latency, database latency, error rate, third-party calls, deploys.
4. Split the path: browser, network, edge, app server, data store, downstream
   dependency.
5. Mitigate safely: rollback, disable expensive feature, raise cache TTL, shed
   noncritical work, or route around a failing dependency.
6. Prevent recurrence: add SLOs, alerts, dashboards, load tests, canaries, and
   runbooks.

Say what you would measure before guessing the cause.

## System Design Pattern

The PDF frames system design as a broad real-world engineering problem with
constraints, simplicity, robustness, and tradeoffs. Use this interview order:

| Step | What to Do |
| ---: | --- |
| 1 | Clarify the customer, users, and success outcome |
| 2 | Define functional and nonfunctional requirements |
| 3 | Estimate scale, traffic, storage, latency, availability, and cost |
| 4 | Sketch the simplest architecture that meets the requirements |
| 5 | Define APIs, data model, workflow states, and ownership boundaries |
| 6 | Deep-dive on GenAI, data, security, reliability, or scale |
| 7 | Discuss failure modes, observability, and operational response |
| 8 | Explain tradeoffs and what would change under different assumptions |

For GenAI system design, always include:

- identity and authorization before retrieval or tool use,
- data freshness and permission-aware indexing,
- model versioning and evaluation sets,
- human review for consequential actions,
- refusal or fallback behavior when evidence is insufficient,
- cost controls by tenant, user, or workflow.

## Coding Interview Map

The PDF describes a LeetCode or HackerRank-style interview, using a virtual
interview platform with formatting and syntax highlighting. You should expect
Python, object-oriented programming, and roughly 30-50 lines of code. The PDF
also says you should not rely on pseudocode unless the interviewer specifically
asks for it.

Use this flow:

1. Ask clarifying questions and define requirements.
2. Translate the prompt into a data structure or algorithm.
3. State a simple correct approach before optimizing.
4. Write runnable-looking Python with clean names and small helpers.
5. Walk through edge cases and complexity.
6. Add tests manually, since the platform may not run your code.
7. Find and fix bugs aloud.

High-yield practice from this repo:

| Skill | Practice |
| --- | --- |
| Hash maps and grouping | [49 Group Anagrams](../arrays_strings/0049_group_anagrams.md) |
| Heaps and top-k | [347 Top K Frequent Elements](../heaps/0347_top_k_frequent_elements.md) |
| Intervals | [56 Merge Intervals](../intervals_search/0056_merge_intervals.md) |
| Binary search on answer | [875 Koko Eating Bananas](../intervals_search/0875_koko_eating_bananas.md) |
| Graph prerequisites | [207 Course Schedule](../trees_graphs/0207_course_schedule.md) |
| OOP state and invariants | [146 LRU Cache](../design_data_structures/0146_lru_cache.md) |
| Time-indexed state | [981 Time Based Key-Value Store](../design_data_structures/0981_time_based_key_value_store.md) |

When a coding prompt sounds practical or product-shaped, first translate it:

```text
users and events -> maps, sets, heaps, queues, graphs, intervals, or state machines
```

## One-Week Prep Plan

| Day | Focus | Output |
| ---: | --- | --- |
| 1 | Read the PDF, role map, and customer discovery notes | 60-second role intro and evidence matrix |
| 2 | GenAI fundamentals and RAG | One AI workflow design with evaluation and fallback |
| 3 | Cloud architecture and system design patterns | One 45-minute system design mock |
| 4 | Troubleshooting | One slow-website incident walkthrough and runbook |
| 5 | Coding fluency | Two Python problems, including one OOP or stateful design |
| 6 | Customer scenario | One COSTAR mock with recommendation and rollout phases |
| 7 | Mixed rehearsal | RRK mock, coding mock, and behavioral story review |

Record each mock in the [progress tracker](../PROGRESS_TRACKER.md). Write the
weakest observable behavior and the next practice action.

## Additional Resources From the PDF

The PDF includes these embedded resource links:

- [Life in App Engine Production](http://www.youtube.com/watch?v=rgQm1KEIIuc)
- [Prepare for Your Google Interview: Systems Design](https://youtu.be/Gg318hR5JY0)
- [Prepare for Your Google Interview: Coding](https://www.youtube.com/watch?v=XKu_SEDAykw&t=4s)
- [Google Cloud Blog](https://cloud.google.com/blog/)
- [Why Google Cloud](https://cloud.google.com/why-google-cloud)
- [Google Cloud AI products](https://cloud.google.com/products/ai)
- [Google Cloud Next](https://cloud.withgoogle.com/next/25)
- [About Google](https://about.google/)
- [The Google Story](https://about.google/our-story/)
- [Life at Google](https://www.youtube.com/user/lifeatgoogle)
- [Google Developers](https://developers.google.com/)
- [Google Open Source Projects](https://opensource.google/projects)

## Final Self-Check

Before the interview, you should be able to say yes to each item:

- I can explain why this role is both customer-facing and deeply technical.
- I have one story about building or debugging an application for real users.
- I can design a GenAI workflow with identity, data, model, evaluation,
  reliability, and cost controls.
- I can troubleshoot a slow web application using evidence instead of guesses.
- I can map cloud requirements to provider-neutral categories and GCP examples.
- I can write 30-50 lines of clear Python under time pressure.
- I can discuss tradeoffs without pretending there is one perfect architecture.

## Check Your Understanding

Try each question before opening its answer. Say the approach, tradeoffs, and
one concrete example aloud.

### Question 1: Explain the Role Signal

Why is a GenAI FDE answer weaker if it only names cloud products and model APIs?

<details>
<summary>Show answer and explanation</summary>

A GenAI FDE is expected to bridge customer needs and production reality. A
strong answer must show the workflow, stakeholders, data boundaries, integration
work, reliability, evaluation, rollout, and measurable customer value. Product
names may be useful after the design is clear, but they do not prove that the
candidate can discover the problem, build the solution, debug blockers, or help
the customer adopt it.

</details>

### Question 2: Prepare a Coding Round

In the described coding interview, why should you ask clarifying questions and
dry-run tests even if the problem looks simple?

<details>
<summary>Show answer and explanation</summary>

The environment may not provide autocomplete, code correction, or a compiler, so
the interviewer needs to see your reasoning and your ability to catch mistakes
manually. Clarifying questions prevent solving the wrong problem. Dry-running
normal and edge cases exposes missing returns, incorrect update order, duplicate
handling, empty input behavior, and complexity issues before you claim the code
is complete.

</details>
