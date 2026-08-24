# Customer Discovery and Solutioning

[FDE track](./README.md) | [Role map](./01_role_and_interview_map.md) | [AI engineering](../ai_engineering/README.md) | [System design](../system_design/README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## What a Customer Scenario Tests

A customer scenario is not a trivia question with one hidden product answer. It
tests whether you can:

- discover the actual outcome before designing,
- separate facts from assumptions,
- translate business language into technical requirements,
- compare options and make a recommendation,
- plan adoption rather than only draw the final architecture,
- identify risks, measurements, and operating ownership,
- explain the same decision at different technical depths.

The fastest way to weaken an answer is to name a database, model, or cloud
service before knowing what problem it must solve.

## The COSTAR Framework

Use **COSTAR** to keep the conversation organized:

| Letter | Meaning | Question |
| --- | --- | --- |
| C | Customer and stakeholders | Who uses, buys, approves, secures, and operates this? |
| O | Outcome and measurement | What must improve, by how much, and by when? |
| S | Starting state and constraints | What exists today, what failed, and what cannot change? |
| T | Technical options and tradeoffs | Which approaches fit, and what does each cost or risk? |
| A | Adoption and delivery plan | What is the smallest proof, and how does it reach production safely? |
| R | Risks and run state | What can fail, how will we detect it, and who responds? |

COSTAR is not a speech you recite. It is a checklist that prevents a missing
customer, metric, constraint, or production plan.

## A 40-Minute Scenario Plan

| Time | Work |
| ---: | --- |
| 0-7 minutes | Ask discovery questions and restate the core problem. |
| 7-12 minutes | Prioritize requirements, constraints, and success metrics. |
| 12-22 minutes | Compare two or three technical options and recommend one. |
| 22-30 minutes | Draw the workflow and explain security, data, and operations. |
| 30-35 minutes | Propose proof, hardening, and rollout phases. |
| 35-40 minutes | Test risks, handle objections, and summarize value. |

An interviewer may interrupt or change the scenario. Treat that as new customer
information, not as damage to a memorized answer.

## C: Customer and Stakeholders

"The customer" is rarely one person.

| Stakeholder | What They May Care About |
| --- | --- |
| End user | Accuracy, speed, workflow fit, and trust |
| Executive sponsor | Business outcome, deadline, budget, and adoption |
| Engineering team | Integration, maintainability, testing, and ownership |
| Security or legal | Access, data use, retention, audit, and compliance |
| Operations team | Monitoring, incidents, capacity, and support burden |
| Procurement or finance | Contract, unit cost, forecast, and vendor risk |

Ask who has decision authority and who will operate the result after the launch
team leaves. A technically elegant system with no owner is not production-ready.

## O: Outcome and Measurement

Turn a feature request into an outcome.

```text
Feature request: "We need an AI support assistant."

Possible outcomes:
- reduce median time to a correct support answer,
- increase first-contact resolution without increasing unsafe responses,
- help new agents find approved procedures,
- make answer sources auditable.
```

Ask for a baseline and guardrails:

- What happens today?
- Which users and workflow are affected?
- What is the current time, error, cost, or conversion baseline?
- What minimum improvement would justify rollout?
- Which safety, privacy, or quality metric must not regress?
- When must evidence be available?

Do not invent a target. If none is known, propose measuring the baseline during
the proof phase and agreeing on a launch threshold.

## S: Starting State and Constraints

Discover before replacing.

### Current State

- Existing applications, APIs, data stores, models, and vendors
- Current workflow and manual workarounds
- Data location, format, quality, ownership, and update frequency
- Team skills, on-call ownership, deployment process, and testing maturity
- Previous attempts and why they were rejected or failed

### Constraints

- Latency and throughput
- Budget and unit economics
- Deadline and available team
- Security, privacy, legal, residency, and retention
- Availability and recovery objectives
- Integration and migration limits
- Explainability, citations, or human approval
- Vendor, open-source, or on-premises requirements

### Restate the Problem

Use a sentence that connects cause to impact:

```text
My current understanding is that support agents search five changing policy
repositories manually, which delays answers and creates inconsistent guidance.
The first goal is a cited internal assistant for one policy domain, with access
controls preserved and no autonomous customer response.
```

Ask whether that summary is correct before designing.

## T: Technical Options and Tradeoffs

Present real choices, not one recommendation disguised as certainty.

For each option, compare:

| Dimension | Questions |
| --- | --- |
| Fit | Does it meet the required outcome and constraints? |
| Delivery | How quickly can the team prove and ship it? |
| Quality | What errors does it reduce or introduce? |
| Operations | Who monitors, upgrades, and supports it? |
| Security | Where does data flow and who can access it? |
| Cost | What are fixed, variable, migration, and staffing costs? |
| Reversibility | Can the customer change direction without a rewrite? |

### Recommendation Shape

```text
I considered A and B. I recommend A for the first production slice because it
meets [requirements] with lower [risk/time/cost]. Its limitation is [specific
limit]. I would move toward B when [measurable trigger], and I would preserve that
path now by [interface or data decision].
```

This is more credible than calling one option "best."

## A: Adoption and Delivery

A customer buys an outcome, not a diagram. Explain how people reach it.

### Phase 1: Prove

- One narrow user group and use case
- Representative data, including hard and unsafe examples
- Baseline comparison
- Human review and frequent feedback
- Short time box and explicit stop/go criteria

### Phase 2: Harden

- Identity, authorization, privacy, and audit
- Automated evaluation and regression tests
- Durable workflows, retries, backups, and incident paths
- Cost and capacity limits
- Documentation, training, support, and ownership

### Phase 3: Scale

- More users, data domains, regions, and integrations
- Gradual rollout and rollback
- Performance and unit-cost optimization
- Reusable platform pieces extracted from proven needs

Name the decision gate between phases. A pilot should answer a question, not run
forever as an unofficial production system.

## R: Risks and Run State

For every major risk, state four things:

```text
risk -> prevention -> detection -> response owner
```

Example:

```text
Risk: the assistant cites an outdated policy.
Prevention: ingest only approved repositories and store version metadata.
Detection: evaluate freshness and log source versions in every answer.
Response: suppress the stale domain, re-index, and notify the content owner.
```

Useful risk groups include data quality, security, model behavior, integration,
availability, cost, adoption, and organizational ownership.

## Detailed Example: Internal Document Assistant

### Scenario

An enterprise asks for an AI assistant that answers employee questions from
internal policies.

### Discovery

Ask:

- Which employees and policy domains are first?
- Are answers advisory, or can they trigger a business action?
- Must every answer cite an approved source?
- How often do documents change, and who approves them?
- Do document permissions differ by user or group?
- Which languages and file types exist?
- What latency is acceptable?
- Can data leave the customer's region or network boundary?
- What is the current answer-time and escalation baseline?

### Working Assumptions

- Internal employees only
- One policy domain for the proof
- Answers require citations
- Documents change weekly
- Existing identity groups must control retrieval
- A human remains responsible for sensitive decisions
- The first success metric is faster correct answer discovery, with unsupported
  answer rate as a guardrail

### Options

| Option | Strength | Limitation |
| --- | --- | --- |
| Better keyword search | Fastest and easiest to audit | Weak on paraphrases and answer synthesis |
| Retrieval plus an LLM | Handles natural questions and changing documents with citations | Requires retrieval and answer evaluation, access filtering, and model controls |
| Fine-tune a model on policies | May improve stable style or behavior | Poor fit for frequently changing facts; harder deletion and freshness story |

Recommend retrieval-augmented generation for the proof, while keeping keyword
search as a baseline and fallback. The reason is frequent content change and the
need to show sources, not fashion.

### High-Level Workflow

```text
approved document source
    -> parse and normalize
    -> split into traceable chunks
    -> attach access and version metadata
    -> create searchable representations
    -> index

employee question
    -> authenticate user
    -> retrieve only authorized chunks
    -> rerank and build bounded context
    -> generate answer with citations
    -> validate output and policy
    -> show answer or safe fallback
    -> collect outcome feedback
```

Read [RAG Systems](../ai_engineering/02_rag_systems.md) for the full design.

### Proof Plan

1. Select one approved policy set and 100-300 representative questions.
2. Label expected source documents and whether each question is answerable.
3. Measure current search time and correctness on a sample.
4. Build retrieval first and inspect misses before adding generation.
5. Add cited generation with a refusal when evidence is insufficient.
6. Run expert review, permission tests, and adversarial prompt tests.
7. Pilot with a small employee group and compare against the baseline.

### Launch Gates

- Retrieval finds the approved source for an agreed share of answerable questions.
- Unsupported claims stay below the agreed guardrail.
- Permission tests show no cross-group source access.
- Latency and cost meet the expected usage envelope.
- Content, operations, security, and support owners accept their runbooks.
- Users demonstrate repeated adoption in the real workflow.

### Risks

| Risk | Control |
| --- | --- |
| Unsupported answer | Require evidence, evaluate claims, and fall back when context is weak. |
| Permission leakage | Filter during retrieval from verified identity, not only after generation. |
| Stale policy | Version sources, process change events, and monitor index freshness. |
| Prompt injection in documents | Treat retrieved text as untrusted data, isolate instructions, and restrict tools. |
| Low adoption | Design with agents, measure workflow use, and repair sources or UX before scaling. |
| Cost growth | Cap context, cache authorized stable work, budget by tenant, and monitor cost per useful answer. |

### Executive Summary

```text
I recommend a narrow, cited internal assistant for one policy domain. We will
preserve existing access controls, compare it against current search, and require
human responsibility for sensitive decisions. The proof tests retrieval quality,
unsupported claims, latency, cost, and actual agent time saved. Only after those
gates pass will we harden operations and expand domains.
```

## Handle Customer Objections

Use this sequence:

1. Confirm the concern.
2. Ask what evidence or constraint drives it.
3. State where you agree.
4. Compare consequences with data or a small experiment.
5. Propose a reversible next step.

Example:

```text
Customer: "We must fine-tune immediately because RAG is too simple."

Response: "I hear that you need high domain accuracy, not a demo. Before choosing
the adaptation method, can we separate missing knowledge from wrong behavior?
Your policies change weekly and require citations, which favors retrieval for
facts. I propose a two-week retrieval baseline with a labeled evaluation set. If
retrieval finds the right evidence but generation still fails your style or task
requirements, that gives us evidence for targeted fine-tuning."
```

Do not win an argument and lose the customer. Make the next decision evidence-based.

## Complexity and Capacity Aloud

Customer scenarios still need numbers. State simple assumptions:

```text
10,000 users * 4 questions/day = 40,000 questions/day
40,000 / 86,400 = about 0.5 average questions/second
10x peak = about 5 questions/second
```

Then estimate document volume, index size, model concurrency, latency budget, and
unit cost. Exact values can change; explicit arithmetic lets the customer correct
them.

## Edge Cases to Raise

- The requested success metric has no baseline.
- The buyer and end user want different outcomes.
- A pilot uses clean sample data unlike production data.
- Security review starts after the architecture is already fixed.
- The customer lacks a team to own the system.
- A deadline makes the full target impossible.
- Data cannot legally or technically move where the proposal assumes.
- A model performs well offline but users do not adopt it.
- The cheaper option creates unacceptable operational burden.
- One enterprise group must never retrieve another group's data.

## Common Mistakes

- Asking many questions without synthesizing an understanding.
- Assuming the customer's requested technology is the actual goal.
- Giving three options but refusing to recommend one.
- Proposing a pilot with no baseline, evaluator, or exit criteria.
- Treating security, migration, support, and adoption as post-launch details.
- Inventing savings or accuracy numbers.
- Ending on architecture instead of outcome and next decision.

## Possible Follow-up Questions

| Follow-up | Strong Answer Direction |
| --- | --- |
| The customer demands launch in two weeks. | Reduce scope, preserve safety gates, identify what cannot be promised, and define a reversible proof. |
| Budget is cut in half. | Revisit the outcome, reduce candidate approaches and usage, choose lower-cost tiers, and protect critical guardrails. |
| Security rejects the data flow. | Understand the prohibited boundary, redesign placement or data minimization, and do not bypass the control. |
| The pilot is accurate but unused. | Observe workflow friction, interview users, inspect latency and trust, and treat adoption as a product failure to diagnose. |
| An executive wants a precise ROI before a baseline exists. | State what is unknown and propose a short measurement phase with a decision model. |

## Scenario Mock Scorecard

Give yourself one point for each:

- [ ] Identified users, buyer, approver, operator, and affected workflow.
- [ ] Defined outcome, baseline, target, deadline, and guardrails.
- [ ] Discovered current state, prior attempts, data, team, and constraints.
- [ ] Restated the core problem and received confirmation.
- [ ] Compared at least two viable options with specific tradeoffs.
- [ ] Recommended one option and named its limit and migration trigger.
- [ ] Proposed proof, hardening, and scale phases with decision gates.
- [ ] Covered security, operations, cost, adoption, and ownership.
- [ ] Tested failures and handled one objection without becoming defensive.
- [ ] Ended with measurable value, open questions, and the next decision.

## Check Your Understanding

### Question 1: A Model Suddenly Performs Worse

A customer's production classifier was healthy last week, but business users now
report poor results. How do you structure the response?

<details>
<summary>Show answer and detailed explanation</summary>

**Customer and outcome:** Identify affected users and business actions. Ask which
metric worsened: prediction quality, latency, availability, or cost. Establish
severity and whether unsafe decisions require immediate rollback or human review.

**Starting state:** Build a timeline. Check model version, application deployment,
feature code, upstream schemas, traffic mix, thresholds, infrastructure, and
label availability. Compare healthy and unhealthy requests.

**Hypothesis order:**

1. Measurement or reporting changed.
2. Input schema or preprocessing changed.
3. Production data distribution shifted.
4. Model or threshold changed.
5. Serving dependency or resource behavior changed.
6. The relationship between inputs and correct outcomes changed.

**Immediate action:** Stop harmful automation, roll back a known bad release, or
route to a safe fallback according to impact. Preserve evidence before changing
everything.

**Diagnosis:** Segment metrics by model, feature version, customer cohort, region,
and time. Validate raw inputs and preprocessing parity. Compare input and
prediction distributions with the training and recent healthy windows. Obtain
fresh labels where possible.

**Repair and prevention:** Fix the proven cause, canary the repair, and add the
missing schema, drift, quality, or deployment guardrail. Record ownership and an
incident review.

The strong answer does not jump directly to retraining. Retraining cannot repair
a broken schema, incorrect metric, or overloaded endpoint.

</details>

### Question 2: Real-Time Fraud Decisions

A payment company wants an ML system to block fraudulent transactions in real
time. Use COSTAR to produce an answer outline.

<details>
<summary>Show answer and detailed explanation</summary>

**C - Customer:** Cardholders, merchants, fraud analysts, risk leadership,
security, compliance, and the team operating decisions.

**O - Outcome:** Reduce fraud loss while controlling false declines and decision
latency. Baseline current rules, fraud capture, false-positive rate, manual review
load, and customer complaints. Define which metric is the hard guardrail.

**S - Starting state:** Ask about transaction volume and peak, labels and delay,
existing rules, available features at decision time, regions, explanation needs,
and action options such as approve, challenge, review, or decline.

**T - Options:** Keep rules as a baseline; add a supervised risk score when labels
are sufficient; use anomaly signals for emerging patterns; combine them in a
decision policy. Recommend shadow scoring before automatic blocking. A complex
model is not useful if its features cannot be served inside the latency budget.

**A - Adoption:** Replay historical data, run shadow traffic, calibrate thresholds,
canary one low-risk cohort, keep manual review and rollback, then expand. Train
analysts and capture review outcomes as labels.

**R - Risks:** False declines, adversarial adaptation, delayed or biased labels,
feature outages, drift, duplicate transactions, privacy, and unbounded review
queues. Monitor segmented precision/recall, expected loss, latency, feature
freshness, drift, appeal outcomes, and cost.

**Architecture outline:** Event intake -> validated online features -> rules and
model score -> policy decision -> durable audit event. Training uses versioned
historical data and the same feature definitions. A registry, shadow/canary
deployment, fallback rules, and monitoring connect training to serving.

**Complexity and scale:** State transactions per second, latency budget, feature
lookup count, model service capacity, and review queue size before choosing
infrastructure.

</details>
