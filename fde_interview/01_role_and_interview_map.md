# FDE Role and Interview Map

[FDE track](./README.md) | [Enterprise AI adoption](./05_enterprise_ai_adoption.md) | [Repository home](../README.md) | [Study plans](../INTERVIEW_STUDY_PLANS.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## First, Treat the Title as Ambiguous

Forward Deployed Engineer can mean different things at different companies. One
role may spend most of its time building customer-specific production software.
Another may focus on prototypes, integrations, architecture, or technical
delivery leadership.

Before preparing, verify the actual job description and ask the recruiter:

1. What does a normal project look like from discovery through production?
2. How much time is spent coding, designing, working with customers, and traveling?
3. Which technical domains are tested?
4. Is coding algorithmic, practical, or both?
5. Is there a system design, domain knowledge, or customer scenario round?
6. What level of production ownership continues after launch?

This prevents preparing for a generic title instead of the real interview.

## The Durable Core of the Role

An FDE usually works at the intersection of four responsibilities:

```text
customer outcome
      +
software implementation
      +
production architecture
      +
clear technical communication
```

The difficult part is moving between them. You may explain a business constraint
to an engineer, explain a reliability tradeoff to a customer leader, then write
the integration or debugging code that proves the solution.

## FDE and Product SWE Emphasis

These are tendencies, not strict job boundaries.

| Dimension | Product SWE Often Emphasizes | FDE Often Adds More Emphasis On |
| --- | --- | --- |
| Problem source | Product roadmap and internal requirements | Ambiguous customer and field constraints |
| Discovery | Product/engineering collaboration | Direct customer questioning and synthesis |
| Implementation | Shared product code and platforms | Product code, integrations, prototypes, and deployment work |
| Architecture | General product scale and reliability | Customer environment, migration, security, adoption, and value |
| Communication | Engineering and product peers | Technical and non-technical customer stakeholders as well |
| Success | Product and engineering metrics | Product metrics plus customer adoption and business outcome |
| Reuse | Build for a broad product surface | Solve now while identifying what should become reusable product |

Neither role is inherently more or less technical. Read the specific position.

## A Practical Interview Map

An interview loop may contain some of these dimensions:

| Dimension | What You May Be Asked to Do | Evidence to Show |
| --- | --- | --- |
| Coding | Solve an algorithm or implement a practical transformation | Correct state, readable code, tests, complexity, communication |
| Technical debugging | Diagnose a failing API, pipeline, model, or deployment | Hypotheses, evidence order, safe mitigation, prevention |
| System design | Design a production service under scale and reliability constraints | Requirements, estimates, data flow, deep dives, failure recovery |
| Domain depth | Explain AI, data, cloud, security, or another role-specific area | Accurate concepts, tradeoffs, production consequences |
| Customer scenario | Advise a customer with incomplete requirements | Discovery, recommendation, phases, risks, measurable outcome |
| Enterprise AI adoption | Choose and deliver an AI-enabled business workflow | Baseline, use-case tradeoffs, architecture, evaluation, rollout, adoption, ownership, and value |
| Behavioral | Describe past ownership, conflict, failure, and impact | Truthful personal actions, judgment, reflection, results |

The loop and scoring vary. Use this map to identify preparation categories, not
to predict a particular company's process.

The enterprise AI adoption dimension may be presented as system design, an
ambiguous customer case, product sense, technical strategy, or an AI deep dive.
Practice the full version in
[Enterprise AI Adoption Design](./05_enterprise_ai_adoption.md).

## What Role-Related Knowledge Means

Role-related knowledge is the technical context needed to contribute to the
customer problem. For an AI platform role, it may include RAG, evaluation,
serving, data governance, and cost. For a data role, it may include ingestion,
warehousing, schemas, quality, and migration. For a security role, the domain is
different again.

A strong answer does more than name a service:

```text
Weak:   "Use a managed queue."

Strong: "The processor is slower and burstier than uploads, so I would place a
durable queue between them. At-least-once delivery means the worker needs an
idempotency key, bounded retries, and a dead-letter path."
```

The second answer connects a tool category to the requirement and its operating
consequences.

## Translate Real-World Framing Into Data Structures

FDE coding prompts may hide a familiar algorithm inside domain language.

| Domain Wording | Underlying Shape |
| --- | --- |
| Service dependencies must deploy in order | Directed graph and topological sort |
| Alert spreads from several affected regions | Multi-source BFS |
| Keep the busiest `k` customers | Frequency map and heap |
| Find a minimum safe capacity | Binary search on a monotonic answer |
| Merge time ranges from many sources | Sort and merge intervals |
| Resolve nested configuration variables | Graph traversal with cycle detection |
| Connect accounts as relationships arrive | Union-find |

Say the translation aloud before coding:

> I can model each service as a node and each dependency as a directed edge. The
> requested deployment order is a topological ordering, and a cycle means no
> valid order exists.

## Build an Evidence Matrix

Do not prepare only descriptions of skills. Prepare evidence.

| Skill | Evidence From Your Experience | Gap to Repair |
| --- | --- | --- |
| Coding under time pressure |  |  |
| Customer discovery |  |  |
| Production architecture |  |  |
| Debugging and incidents |  |  |
| AI or target domain depth |  |  |
| AI adoption and value measurement |  |  |
| Cross-functional delivery |  |  |
| Explaining technical tradeoffs |  |  |
| Handling failure and learning |  |  |

If one row has no truthful evidence, create a small project, volunteer for that
work, or prepare to explain adjacent experience honestly. Do not invent a story.

## Your 60-Second Introduction

Use four parts:

1. **Present:** what you build or own now.
2. **Evidence:** one example combining technical work and user or customer impact.
3. **Direction:** why you want more of that intersection.
4. **Fit:** why this specific role's actual work matches that direction.

Template:

```text
I am a [role] focused on [technical area]. In a recent project, I personally
[specific action], which helped [user/customer] achieve [measured or observable
result]. I learned that I do my best work when [engineering/customer insight].
This role interests me because its work on [specific responsibility from the job
description] combines that strength with [skill you can demonstrate].
```

Do not claim confidential customer details or invented numbers. A concrete
observable result is better than a fake percentage.

## A Preparation Priority Rule

For each confirmed interview dimension, rate yourself:

```text
0 = unfamiliar
1 = can explain after reading notes
2 = can perform with hints
3 = can perform independently
4 = can adapt under a changed requirement
```

Spend most preparation time on dimensions that are both confirmed in the loop
and currently scored `0-2`. Do not spend a week polishing your strongest topic
while avoiding the round most likely to fail.

## Assumptions to Say Aloud

In an FDE discussion, useful assumptions include:

- who owns the final decision,
- who uses and operates the solution,
- what production and compliance boundaries exist,
- whether the goal is a prototype, pilot, migration, or durable platform,
- which outcome and deadline define success,
- what is known versus what still requires discovery.

Labeling an assumption invites correction and demonstrates comfort with
ambiguity.

## Common Mistakes

- Assuming every FDE role has the same interview loop.
- Describing FDE as consulting without engineering ownership, or as SWE with
  easier coding.
- Preparing vendor product names without understanding architecture patterns.
- Solving the technical problem before confirming the customer outcome.
- Using only "we" in behavioral answers and hiding personal contribution.
- Giving a polished recommendation with no adoption plan or failure handling.
- Memorizing one architecture and forcing it onto every scenario.

## Possible Follow-up Questions

| Follow-up | Strong Answer Direction |
| --- | --- |
| Why FDE instead of product SWE? | Name the work intersection you have already enjoyed, then connect it to specific role responsibilities. |
| Are you comfortable with ambiguity? | Give a real example of how you reduced ambiguity through questions, experiments, and checkpoints. |
| How do you avoid one-off customer code? | Separate urgent customer needs from reusable capability; define ownership and a path to productization. |
| What if the customer asks for the wrong solution? | Understand the desired outcome, show evidence and tradeoffs, propose a safer experiment, and preserve the relationship. |
| How technical should an FDE be? | Match the actual role; demonstrate enough depth to build, debug, secure, and operate the proposed solution. |

## Test Your Understanding Aloud

Explain this in two minutes:

```text
An FDE is not defined only by a title. I would first verify the role's actual
coding, domain, customer, and production responsibilities. The transferable core
is turning ambiguous customer outcomes into working, operable software while
communicating across technical boundaries. My preparation should therefore map
each confirmed interview dimension to evidence and a scored practice gap.
```

## Check Your Understanding

### Question 1: Choose What to Study

A recruiter confirms four rounds: practical Python, AI system design, customer
scenario, and behavioral. You score yourself `3`, `1`, `1`, and `2`. Where should
most of the next week's time go?

<details>
<summary>Show answer and explanation</summary>

Prioritize AI system design and customer scenarios because both are confirmed
and currently weak. Keep shorter practical Python review so the existing strength
does not decay, and prepare behavioral stories to move from assisted to
independent performance.

A reasonable split might be 35% AI design, 30% customer scenarios, 20%
behavioral, and 15% Python. Exact percentages matter less than resisting the urge
to spend most time on the already comfortable coding round.

</details>

### Question 2: Extract the Hidden Algorithm

A customer has tasks with prerequisite task IDs and asks whether all tasks can
finish. What model and algorithm should you state before writing code?

<details>
<summary>Show answer and detailed explanation</summary>

Model each task as a directed graph node. A prerequisite relation is a directed
edge from prerequisite to dependent task. All tasks can finish exactly when the
graph has no directed cycle.

Use topological sort with indegree counts or DFS color states. With Kahn's
algorithm, queue every zero-indegree task, remove its outgoing edges, and count
processed tasks. If the count equals the task count, a full order exists.

**Complexity:** `O(V + E)` time and `O(V + E)` space for nodes and prerequisite
edges.

**Say aloud:** "The business wording describes dependency ordering, so I will
translate it into a directed graph before choosing the implementation."

</details>
