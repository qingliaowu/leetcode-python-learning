# Enterprise AI Adoption Design for FDE Interviews

[FDE track](./README.md) | [Customer discovery](./02_customer_discovery_and_solutioning.md) | [Cloud fundamentals](./03_cloud_architecture_fundamentals.md) | [AI engineering](../ai_engineering/README.md) | [RAG troubleshooting](../ai_engineering/04_rag_accuracy_latency_playbook.md) | [System design](../system_design/README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## What This Interview Question Asks

An interviewer may give you a broad prompt such as:

```text
A large enterprise wants to adopt AI to improve customer support. Design the
solution and explain how you would take it from idea to production.
```

The weak interpretation is:

```text
Choose a model and draw an API call.
```

The useful interpretation is:

```text
Find a valuable workflow, prove that AI improves it safely, build the surrounding
production system, help people adopt it, and create an operating loop that keeps
the result useful.
```

This belongs in FDE preparation because current role descriptions emphasize the
whole path from discovery and technical scoping through system design, production
rollout, adoption, measurable workflow impact, and evaluation feedback. See this
[official FDE role example](https://openai.com/careers/forward-deployed-engineer-%28fde%29-seattle-seattle/).

Role descriptions differ by company, but the durable interview skill is the
same: connect engineering decisions to a real customer outcome.

## The Central Idea

An AI demo proves that a model can produce an output.

Enterprise adoption proves much more:

```text
the right users
    -> use a safe and reliable workflow
    -> often enough
    -> to improve a measured business outcome
    -> at an acceptable total cost and risk
```

If any arrow is missing, the model may be impressive while the adoption fails.

## Beginner Vocabulary

| Term | Plain-English Meaning |
| --- | --- |
| Use case | One specific job a specific user needs to complete |
| Workflow | The actual sequence of people, software, data, and decisions used to do the job |
| Baseline | How the workflow performs before the proposed change |
| Guardrail | A result that must not become unacceptable while another metric improves |
| Evaluation set | Saved representative examples used to compare system versions |
| Proof of value | A small test that asks whether the idea can create useful business improvement |
| Pilot | Limited real use with selected users, support, measurements, and an end date |
| Adoption | Eligible users repeatedly use the workflow because it helps them |
| Human in the loop | A person reviews or approves before a consequential action occurs |
| RAG | Retrieve relevant evidence, then ask a model to answer using that evidence |
| Tenant | One customer organization whose users and data share an account boundary |
| System of record | The authoritative application or database where the final business state is stored |
| Idempotency | Retrying the same request has the same logical effect as doing it once |
| p50/p95 latency | Half of requests finish within p50; ninety-five percent finish within p95 |
| Shadow mode | The system runs on copied work, but users or business processes do not rely on its output |
| Canary | A small controlled group receives a new version before wider rollout |
| Kill criterion | Evidence that tells the team to stop, narrow, or redesign the effort |
| Unit economics | Cost and benefit for one useful business result, not only one model request |
| Change management | Training, communication, support, incentives, and process changes that help people use a new workflow |

## How to Study This Capstone

Do not memorize the page or read all of it in one sitting.

1. **First pass:** Read Sections 1-4, the concise summary, and the scorecard.
   Practice choosing a workflow and defining success.
2. **Second pass:** Read the support case through delivery phases. Draw the
   architecture with no more than ten boxes.
3. **Third pass:** Study reliability, model changes, ownership, observability,
   testing, and follow-ups.
4. **Interview practice:** Choose one practice case, set a 45-minute timer, and
   reveal the detailed answers only after finishing your own outline.

The goal is to remember the order of decisions, not every example sentence.

## A 45-Minute FDE Design Plan

| Time | What to Do | What the Interviewer Should Hear |
| ---: | --- | --- |
| 0-7 minutes | Discover the customer, workflow, outcome, baseline, and constraints | A confirmed problem statement, not a technology guess |
| 7-12 minutes | Compare candidate use cases and choose the first slice | Why this use case creates value with manageable risk |
| 12-17 minutes | Define users, requirements, metrics, and assumptions | Business target, quality target, guardrails, scale, and scope |
| 17-27 minutes | Draw the workflow and high-level architecture | Identity, data, model, application, human decision, and system of record |
| 27-34 minutes | Deep-dive on evaluation, security, reliability, and cost | How the team knows it works and what happens when it does not |
| 34-40 minutes | Explain proof, pilot, rollout, training, and ownership | How a prototype becomes an adopted production capability |
| 40-45 minutes | Handle a changed assumption and summarize | Tradeoffs, open risks, next decision, and expected value |

Do not force every section into exactly these minutes. The table keeps you from
spending 35 minutes on architecture and leaving no time for adoption.

## 1. Start With the Business Problem

Ask what work is painful before asking which AI technique to use.

### Questions for the Executive Sponsor

- Which business outcome needs to change?
- What is its current baseline, target, and deadline?
- Why is this important now?
- Which cost, quality, risk, or growth metric must not regress?
- What evidence would justify more investment?

### Questions for the End User

- Walk me through one real case from beginning to end.
- Where do you wait, search, copy, classify, decide, or redo work?
- Which errors are annoying, and which are dangerous?
- Which output would you trust only with evidence or approval?
- What would make you ignore the new tool?

### Questions for Engineering, Data, and Operations

- Which systems and APIs hold the source data and final record?
- How fresh, complete, and permissioned is the data?
- What traffic, latency, availability, and recovery needs exist?
- Who will deploy, monitor, support, and improve the system?
- Which integration or migration cannot change in the first phase?

### Questions for Security, Privacy, and Legal

- Which data may the application and model process?
- Where may data be stored or sent?
- What retention, deletion, residency, audit, or contractual rules apply?
- Which user or tenant boundaries must be preserved?
- Which decisions require a person, an explanation, or an appeal path?

Then restate the problem:

```text
Support agents currently search several approved sources and manually draft
answers. This increases handle time and inconsistent guidance. The first goal is
to help one agent group produce cited drafts faster, while agents keep final
control and permission leakage remains unacceptable.
```

Ask the interviewer whether that understanding is correct.

## 2. Choose the First Use Case

An enterprise may suggest ten AI ideas. Do not build a generic platform before
one workflow proves value.

Compare each candidate on four dimensions:

| Dimension | Strong Signal | Warning Signal |
| --- | --- | --- |
| Business value | Frequent work, costly delay, measurable error, or meaningful growth | Interesting demo with no owner or baseline |
| Technical feasibility | Accessible representative data, testable outputs, workable integration | Missing data, no labels, or an unknown system boundary |
| Risk | Reversible assistance, human review, clear fallback | Irreversible high-impact action with uncertain quality |
| Adoption readiness | Named users, workflow owner, available training and feedback | The buyer likes it but users have no reason to change |

Do not turn this into fake precision with a complicated score. Use evidence to
explain why one candidate should be first.

### Example Portfolio

| Candidate | Value | Feasibility | Risk | Adoption | First Decision |
| --- | --- | --- | --- | --- | --- |
| Support answer drafts with citations | High and measurable | Approved articles and cases exist | Medium; agent reviews | Fits current support console | Good first proof |
| Automatic refund approval | High | Policy data exists | High financial side effect | Requires policy and audit redesign | Keep out of first phase |
| Executive meeting summaries | Moderate | Easy input access | Low to medium privacy risk | Easy, but outcome may be weak | Useful experiment, not first value case |
| Fully autonomous support agent | Potentially high | Many unresolved edge cases | High customer and brand risk | Major workflow change | Too broad for first slice |

### Say the Recommendation Aloud

```text
I would begin with cited response drafts for one support queue. It is frequent,
measurable, and fits the existing agent workflow. A human remains responsible for
sending the answer, so we can learn before adding actions. I would defer automatic
refunds until the evidence, policy engine, audit, and approval controls are proven.
```

## 3. Decide Whether AI Belongs

AI is one possible component, not the default answer.

| Task | Start With | Why |
| --- | --- | --- |
| Exact eligibility or price rule | Normal code or rules engine | The result must be deterministic and auditable |
| Known record lookup | Database query or search | Generation adds no value to an exact lookup |
| Changing private knowledge in natural language | Search or RAG | Current evidence can be retrieved at request time |
| Classify a case into stable categories | Rules baseline, then classifier if needed | Compare against a simple measurable approach |
| Summarize or draft from supplied evidence | Language model with validation | The task allows language variation but needs grounding |
| Forecast numeric demand | Statistical or machine-learning forecast | A text generator is not the natural core model |
| Take an external action | Tool behind application policy and approval | Free-form model output must not directly control side effects |

### The Autonomy Ladder

Increase autonomy only when evidence and controls justify it:

```text
Level 0: observe and measure the current workflow
Level 1: retrieve or summarize for a user
Level 2: recommend or draft; user decides
Level 3: execute a reversible action after confirmation
Level 4: execute bounded actions automatically with monitoring and rollback
```

The highest level is not the goal. The correct level matches the consequence of
an error, quality evidence, reversibility, and customer policy.

## 4. Define Success Before Architecture

Use a metric tree so a good model score cannot hide a failed product.

| Layer | Example Measures |
| --- | --- |
| Business outcome | Handle time, first-contact resolution, backlog age, conversion, loss, or processing cost |
| User outcome | Time to useful result, repeated use, accepted draft, correction burden, and satisfaction |
| AI quality | Correctness, evidence support, completeness, classification quality, and appropriate refusal |
| Safety and policy | Unauthorized data, harmful output, forbidden action, appeal, and reviewed escape |
| Reliability | Availability, p50/p95 latency, timeout, queue age, and dependency failure |
| Economics | Cost per accepted draft, resolved case, approved invoice, or other useful outcome |

### Leading and Lagging Measures

- A **leading measure** appears quickly, such as draft acceptance or time saved in
  a task observation.
- A **lagging measure** may take weeks, such as renewal, loss reduction, or
  customer satisfaction.

Use both. Do not promise a long-term business result from a two-week model test.

### Example Launch Statement

```text
For the first support queue, the pilot should reduce median draft preparation
time without lowering expert-rated correctness or first-contact resolution.
Every factual claim must map to an authorized source, and agents must approve all
outbound messages. We will agree on numeric thresholds after measuring the
baseline during discovery.
```

## 5. Detailed Case: Enterprise Support Copilot

### Scenario

A global software company has 2,000 support agents. They handle about 40,000
tickets per day. Agents search several knowledge systems, inspect customer data,
and draft responses in a case-management application. Leadership asks for an AI
copilot to improve efficiency and answer consistency.

### Working Assumptions to Say Aloud

These are interview assumptions, not discovered facts:

- Start with 200 agents in one product queue.
- Each pilot agent handles about 20 eligible tickets per day.
- Approved knowledge changes daily.
- Customer account data has tenant and role restrictions.
- The first release drafts responses but never sends them automatically.
- Agents can edit, reject, or escalate every draft.
- The existing case system remains the final system of record.
- The target region and retention period must be confirmed with security.
- English is the first language; multilingual behavior is later scope.

State which assumptions would change the design most: autonomous actions,
regulated data, inaccessible source permissions, or no reliable baseline.

### In Scope

- Authenticate the agent and read the current case.
- Retrieve authorized product and account evidence.
- Produce a cited draft or an honest fallback.
- Let the agent edit, accept, reject, or escalate.
- Save the final human-approved response in the existing case system.
- Record privacy-safe evaluation, adoption, reliability, and cost events.

### Out of Scope for the First Phase

- Sending a response without human approval
- Approving refunds or changing customer entitlements
- Every product, language, region, and support channel
- Training a shared model on customer content without explicit agreement
- Replacing the case-management system

Narrow scope is a delivery decision, not lack of ambition.

## 6. High-Level Architecture

```text
approved knowledge sources                 enterprise identity
          |                                        |
          v                                        v
versioned ingestion -> permissioned index    API gateway + policy
          |                                        |
          +-------------------+--------------------+
                              v
agent support console -> copilot workflow service
                              |
                 +------------+-------------+
                 |                          |
                 v                          v
       authorized retrieval          case/account APIs
                 |                          |
                 +------------+-------------+
                              v
                    prompt/context builder
                              |
                              v
                  model gateway and router
                              |
                              v
             output validation + citation checks
                              |
                              v
                 draft shown to support agent
                              |
                      approve/edit/reject
                              |
                              v
                existing case system of record

Every stage -> audit, metrics, traces, feedback, and evaluation records
```

The model is surrounded by identity, policy, data access, validation, human
control, durable records, and measurement. That surrounding system is most of
the enterprise design.

## 7. Explain the Request Flow

1. The support console sends the case ID and the agent's authenticated session.
2. The gateway derives organization, role, and policy from verified identity.
3. The workflow service reads only case fields authorized for that agent.
4. Retrieval searches approved sources using the same tenant and role filters.
5. The context builder includes the task contract, case facts, and traceable
   evidence within a size limit.
6. The model gateway chooses an approved model version and enforces timeout,
   rate, region, and budget policy.
7. Validators check output shape, citations, policy, and forbidden content.
8. The user sees a draft, evidence, and a clear fallback when confidence or
   support is insufficient.
9. The agent edits, accepts, rejects, or escalates.
10. Only the approved application path writes the final response to the case.
11. The system records versions, evidence IDs, outcome, latency, and cost under
    the agreed privacy and retention policy.

### Core Invariant

Say this clearly:

```text
No model output becomes a customer-visible response or business side effect
unless the application applies current authorization and the required human or
policy approval.
```

## 8. Simple API and Durable Records

One possible API contract:

```text
POST /v1/cases/{case_id}/drafts
Idempotency-Key: <client-generated-key>

request:
  requested_language
  optional_agent_note

response:
  draft_id
  status
  draft_text
  citations
  fallback_reason
  model_release
```

Do not accept a tenant or agent ID from an untrusted request field as proof of
identity. Derive it from the authenticated session.

Useful durable records:

| Record | Why It Exists |
| --- | --- |
| Use-case definition | Owner, users, baseline, target, guardrails, scope, and phase |
| Draft run | Case reference, versions, authorized evidence IDs, status, latency, and cost |
| Human outcome | Accepted, edited, rejected, escalated, and reason |
| Evaluation case | Versioned input, expected behavior, risk tags, and trusted labels |
| Release | Model, prompt, retrieval, policy, application, and index versions deployed together |
| Audit event | Who accessed, approved, changed, or released a controlled resource |
| Incident | Impact, timeline, containment, owner, repair, and prevention |

Store sensitive text only when needed and permitted. IDs and aggregates may be
enough for some product measurements.

## 9. Data and Enterprise Boundaries

### Data Inventory

For every source, record:

- owner and approved purpose,
- data classes and sensitive fields,
- user and tenant permissions,
- freshness and quality expectations,
- region and retention,
- deletion process,
- whether it may appear in prompts, logs, evaluation, or training.

### Access Rules

- Derive tenant and user identity from trusted authentication.
- Enforce row, document, and tool authorization before data enters context.
- Partition indexes, caches, storage, keys, or deployments when customer policy
  requires stronger isolation.
- Test forbidden access, guessed IDs, stale membership, revoked access, and
  cross-tenant cache behavior.
- Keep service accounts narrowly scoped and audit privileged access.

### Model Provider Boundary

Confirm rather than assume:

- where requests are processed,
- whether inputs or outputs are retained,
- whether customer data can improve shared models,
- which personnel can access data,
- encryption and key options,
- incident, deletion, and subcontractor terms,
- available region, capacity, and service commitments.

Architecture must match the actual agreement, not a marketing summary.

## 10. Evaluation Before and After Launch

### Build the Evaluation Set

Use representative historical work with permission and expert review:

- common cases,
- rare but important cases,
- incomplete and conflicting evidence,
- unanswerable requests,
- sensitive data and permission boundaries,
- prompt injection and malicious content,
- new products, languages, and user cohorts,
- known failures from the current workflow.

Label what a good result means. For a draft, the rubric may include correctness,
evidence support, completeness, tone, safe escalation, and edit effort.

### Separate System Layers

| Symptom | Investigate First |
| --- | --- |
| Correct article never retrieved | Parsing, metadata, permissions, query, index, freshness |
| Correct evidence retrieved but draft is wrong | Context construction, model, prompt, conflicting evidence |
| Draft is good but agent rewrites it | Tone, workflow fit, missing case fields, trust, or user incentives |
| Offline quality is good but handle time does not improve | Latency, copy steps, ineligible cases, measurement, or adoption |
| Overall score is good but one group fails | Segment data, permissions, language, product, or risk cohort |

For a full production diagnosis process, use the
[RAG Accuracy and Latency Troubleshooting Playbook](../ai_engineering/04_rag_accuracy_latency_playbook.md).
It separates source, parsing, retrieval, ranking, context, generation, queue,
and service-time failures before choosing a fix.

### Release Sequence

```text
offline evaluation
    -> expert review
    -> shadow on recent traffic
    -> internal users
    -> small agent canary
    -> measured pilot
    -> gradual expansion
```

Every arrow needs entry criteria, monitoring, an owner, and rollback behavior.

## 11. Adoption Is Part of the Design

Low use is not automatically user resistance. Diagnose the workflow.

### Before the Pilot

- Observe real users instead of relying only on management descriptions.
- Include respected agents and operations owners in workflow design.
- Explain what the tool does, does not do, and how feedback is used.
- Put the capability inside the current console when possible.
- Train with real scenarios, including rejection and escalation.
- Publish support, incident, and data-use contacts.

### During the Pilot

- Hold short office hours and inspect repeated friction.
- Collect reason codes for edits, rejections, and escalations.
- Measure eligible exposure, use, repeat use, and useful outcomes separately.
- Protect users from pressure to accept a bad suggestion for an adoption target.
- Share repairs and known limits so feedback feels consequential.

### After the Pilot

- Assign product, data, security, content, and operational owners.
- Update standard procedures and training.
- Keep a feedback and evaluation cadence.
- Expand one cohort or capability at a time.
- Retire the tool if it creates no defensible value.

Adoption cannot be fixed only by adding a banner or mandating clicks.

## 12. Delivery Phases and Decision Gates

| Phase | Main Question | Work | Exit Gate |
| --- | --- | --- | --- |
| Discover | Is this a real, measurable problem? | Observe workflow, baseline, data, stakeholders, constraints | Confirmed owner, use case, baseline plan, and risk boundary |
| Prove | Can the approach work on representative examples? | Baselines, thin integration, evaluation set, expert review | Beats agreed baseline with acceptable guardrails |
| Pilot | Does it help real users in their workflow? | Limited production use, training, support, online measurement | Useful outcome and repeat adoption without guardrail failure |
| Harden | Can the enterprise operate it safely? | Identity, audit, SLOs, runbooks, rollback, capacity, cost, deletion | Security and operational acceptance with named owners |
| Scale | Does value continue across more scope? | Cohorts, domains, languages, regions, optimization | Each expansion independently meets value and risk gates |

### Kill or Redesign Criteria

- No measurable workflow problem or accountable owner
- Data cannot be used lawfully or safely for the proposed purpose
- The simple baseline performs as well with lower cost and risk
- Representative quality remains below the minimum after bounded experiments
- Users gain no workflow benefit despite repaired integration and training
- Unit economics do not support the outcome
- The customer cannot own the required run state

Stopping a weak use case protects time for a stronger one.

## 13. Capacity and Cost Aloud

For the 200-agent pilot:

```text
eligible drafts/day
    = 200 agents * 20 tickets
    = 4,000 drafts/day

average requests/second
    = 4,000 / 86,400
    = about 0.05 requests/second

20x peak
    = about 1 request/second

if average end-to-end time is 4 seconds:
required active request concurrency
    = 1 request/second * 4 seconds
    = about 4, before headroom
```

Average traffic looks tiny, but peak concurrency, model quotas, long outputs,
retries, ingestion bursts, and regional limits still matter.

### Benefit Example

Suppose observation shows that an accepted draft saves two minutes:

```text
maximum measured time released/day
    = 4,000 eligible tickets * 2 minutes
    = 8,000 minutes
    = about 133 hours/day
```

This is not automatically cash savings. Adjust for acceptance rate, work shifted
elsewhere, demand, staffing model, and whether released time improves backlog,
quality, or capacity.

### Cost Example

If a complete draft workflow costs an assumed `$0.03` per request:

```text
model and workflow variable cost/day
    = 4,000 * $0.03
    = $120/day
```

Then include integration, data work, evaluation, security review, infrastructure,
support, training, and ongoing ownership.

Use this decision model:

```text
verified outcome value
    - model and infrastructure cost
    - delivery and operating cost
    - change-management cost
    - expected risk cost
    = defensible net value
```

Never invent the customer's labor rate or claim that every saved minute becomes
budget reduction. State the missing input and show where it belongs.

## 14. Reliability and Fallbacks

| Failure | User-Safe Behavior | System Response |
| --- | --- | --- |
| Model timeout | Keep manual workflow available | Bound timeout, avoid retry storm, alert by dependency and release |
| Retrieval unavailable | Show approved search links or manual path | Isolate failure, reconcile index, do not invent an answer |
| Weak or conflicting evidence | Abstain or ask for review | Record reason and route to content owner |
| Case API unavailable | Do not draft from stale guessed facts | Return clear status and retry only safe reads |
| Output validation fails | Hide invalid draft | One bounded repair or safe fallback |
| Permission cannot be confirmed | Reveal nothing | Fail closed and investigate identity mapping |
| New release regresses | Return to last approved release | Stop canary, preserve evidence, roll back all coupled versions |
| Feedback store fails | Do not block core manual support | Buffer safely or degrade measurement with an alert |

The manual workflow is often the first fallback. Test whether it still works
after users become dependent on the copilot.

## 15. Model and Vendor Changes

Treat a model change like a product and policy change, not a library patch.

Version together:

- model and provider,
- system and task prompts,
- retrieval and index,
- tool definitions,
- validation and safety policy,
- application behavior,
- evaluation set and release decision.

Compare candidate versions on quality, safety, latency, reliability, capacity,
and cost. Shadow, canary, and roll back. A stronger average score does not justify
a regression in a critical cohort.

### Build, Buy, or Combine

| Option | Strength | Cost or Risk | Good First Fit |
| --- | --- | --- | --- |
| Configure an existing enterprise product | Fast adoption path and common controls | Less workflow control and vendor coupling | Standard workflow with limited differentiation |
| Build an application on a managed model API | Fast model access with custom workflow | Provider boundary, variable cost, and application ownership | Differentiated workflow with acceptable provider terms |
| Host or manage a model | Greater placement and runtime control | Infrastructure, capacity, upgrades, and specialist burden | Hard boundary or economics that justify operations |
| Hybrid | Route tasks to different products or models | More evaluation and operational complexity | Distinct risk, latency, or cost tiers with proven need |

Preserve portable business data, evaluation sets, and application interfaces where
the migration value exceeds the extra work.

## 16. Operating Model

A production system needs named owners:

| Responsibility | Example Owner |
| --- | --- |
| Business outcome and scope | Support operations leader |
| User workflow and roadmap | Product owner |
| Application and integrations | Engineering team |
| Source quality and freshness | Knowledge/content owners |
| Evaluation labels and review | Domain experts plus AI/product team |
| Identity, privacy, and policy | Security, privacy, legal, and governance partners |
| Reliability and incidents | Service owner and on-call team |
| Training and adoption | Operations enablement and team leads |
| Cost and vendor management | Product, engineering, finance, and procurement |

An FDE should make ownership visible early. The forward-deployed team cannot be
the permanent answer to every incident and content update.

## 17. Observability Dashboard

Organize signals by the question they answer:

| Question | Signals |
| --- | --- |
| Is the business improving? | Handle time, resolution, backlog, customer outcome |
| Are users receiving and using it? | Eligible cases, exposure, use, repeat use, accept/edit/reject |
| Is the result good? | Expert score, citation support, correction, escalation, abstention |
| Is it safe and authorized? | Permission tests, blocked output, reviewed escape, forbidden action |
| Is the service healthy? | Traffic, errors, p50/p95 latency, saturation, timeouts, dependency health |
| Is the data current? | Source age, ingestion lag, failed documents, permission-sync lag |
| Is cost controlled? | Tokens, retrieval, model, storage, retries, cost per accepted draft |

Segment by organization, queue, product, language, release, model, and meaningful
risk cohort without exposing sensitive content in metrics.

## 18. Test the Whole Adoption

### Technical Tests

- Normal, missing, conflicting, stale, and malicious evidence
- Allowed and forbidden users, roles, tenants, cases, and documents
- Model timeout, quota exhaustion, bad schema, and provider outage
- Duplicate request and idempotency behavior
- Source update, permission revocation, and deletion
- Release rollback and fallback availability
- Peak traffic, large cases, long context, and cost budget

### Workflow Tests

- A new agent completes a real task after training.
- An expert rejects a plausible but unsupported draft.
- A user can find citations and understand a fallback.
- The manual process still works during an outage.
- An operations lead can diagnose a failure from the runbook.
- A content owner can repair stale knowledge.
- A security reviewer can reconstruct access and release history.

### Measurement Tests

- Eligible cases are counted consistently before and after launch.
- Treatment and comparison groups represent similar work.
- Saved time is observed, not based only on user guesses.
- Quality and safety labels are blinded when practical.
- Adoption does not reward accepting incorrect drafts.
- Delayed outcomes join to the correct release and case.

## 19. Edge Cases to Raise

- The executive sponsor wants AI, but no workflow owner has committed time.
- The most valuable use case has no usable data or evaluation labels.
- A pilot uses clean examples that omit real permission and integration failures.
- One region prohibits the assumed data flow.
- Acquired business units use different identities, taxonomies, and languages.
- Model quality improves while user edit time grows.
- Agents accept drafts quickly because of workload pressure, not correctness.
- The vendor changes model behavior without the application changing.
- A source owner deletes content that remains in an index or evaluation set.
- Savings in one team create more review work in another.
- The pilot succeeds, but no team can operate the production service.
- A general platform request hides several unrelated use cases and risk levels.

## 20. Common Mistakes

- Starting with a chatbot instead of a workflow and outcome.
- Treating every enterprise AI problem as RAG or an LLM problem.
- Choosing the largest model before defining an evaluation set.
- Reporting model accuracy without business, adoption, safety, or cost measures.
- Calling a demo a pilot when it has no real users or decision gate.
- Drawing architecture without identity, permissions, system of record, or human action.
- Assuming users will adopt a separate tool because the output looks impressive.
- Promising ROI before measuring the baseline and realized workflow effect.
- Scaling to many departments before one use case has an owner and runbook.
- Treating human review as free, instant, and perfectly consistent.
- Hiding uncertainty instead of proposing a reversible experiment.

## 21. Possible Follow-up Questions

| Follow-up | Strong Answer Direction |
| --- | --- |
| The CEO wants full automation in three months. | Separate the desired outcome from autonomy, use the autonomy ladder, quantify error consequence, and propose evidence gates for each added action. |
| Security forbids data leaving one region. | Revisit provider and hosting options, minimize data, redesign placement, and state the cost and operational tradeoff. |
| Offline accuracy is high but users do not return. | Inspect eligibility, latency, workflow placement, edit burden, trust, training, incentives, and whether the chosen task creates value. |
| There is no labeled evaluation set. | Start with a baseline sample, domain-expert rubric, historical outcomes, and active collection during shadow mode. |
| The model provider doubles price. | Measure cost per useful outcome, route easier work, reduce context, compare providers or hosting, and preserve rollback and quality gates. |
| The customer wants one platform for every department. | Establish shared controls and interfaces, but prove separate use cases with separate owners, metrics, data, and risk tiers. |
| A new model is better but slower. | Compare against task-specific quality, latency, cost, and safety thresholds; route or retain the old version when the tradeoff differs by cohort. |
| The pilot saves time but quality falls slightly. | Treat the quality metric as a guardrail, quantify consequence, repair the cause, and do not average away a critical regression. |

## 22. A Concise Interview Summary

```text
I would begin by identifying one frequent workflow with a measurable baseline,
an accountable owner, usable data, and manageable error consequences. For the
support case, I would start with cited drafts inside the existing agent console,
not autonomous responses. Identity and permission filters apply before data
reaches the model, application policy controls every side effect, and the agent
keeps final approval.

I would compare against current search and drafting using a representative
evaluation set, then move through shadow, canary, and a time-boxed pilot. Launch
requires business improvement, quality and privacy guardrails, repeat adoption,
acceptable cost, tested fallback, and named operational owners. Expansion is a
new evidence decision, not an automatic reward for a good demo.
```

## 23. Enterprise AI Adoption Scorecard

Give yourself one point for each item:

- [ ] Identified the user, buyer, workflow owner, operator, and risk approver.
- [ ] Restated a measurable business problem with a baseline plan and guardrail.
- [ ] Compared candidate use cases and recommended a narrow first slice.
- [ ] Explained why AI is useful and why a simpler baseline is insufficient.
- [ ] Chose an autonomy level that matches error consequence and reversibility.
- [ ] Drew identity, data, model, application, human decision, and system of record.
- [ ] Defined offline, online, adoption, safety, reliability, and cost measures.
- [ ] Proposed discovery, proof, pilot, hardening, and scale gates.
- [ ] Covered failure, fallback, tenant isolation, change management, and ownership.
- [ ] Handled a changed assumption and ended with value, risk, and the next decision.

Score interpretation:

| Score | Meaning | Next Practice |
| ---: | --- | --- |
| 0-3 | The answer is mostly a technology proposal | Repeat only discovery, use-case choice, and metrics |
| 4-6 | The design has useful pieces but misses an end-to-end adoption story | Add rollout, ownership, failure, and value gates |
| 7-8 | Interview-ready structure with a few weak deep dives | Change one risk, region, scale, or autonomy assumption |
| 9-10 | Strong integrated answer | Re-run with a different business workflow and less preparation time |

## Practice Cases

Before revealing the formal answers below, outline these cases with the same
structure:

1. Accounts payable wants AI to extract invoices and resolve exceptions.
2. Sales wants faster, safer responses to enterprise requests for proposal
   (RFPs).
3. Manufacturing wants technicians to diagnose equipment from maintenance notes.
4. Legal wants contract review assistance across several regions.

For each, name the user, business measure, simple baseline, AI task, human action,
data boundary, first pilot, guardrail, and kill criterion.

## Check Your Understanding

### Question 1: Accounts Payable Exception Triage

An enterprise receives 100,000 invoices per month. Staff manually inspect failed
invoices, find the cause, and route each exception. Design a first AI adoption
phase. Explain the business outcome, scope, architecture, evaluation, rollout,
edge cases, and complexity or capacity assumptions aloud.

<details>
<summary>Show answer and detailed explanation</summary>

**Customer and outcome:** The direct users are accounts-payable specialists.
Finance leadership owns cycle time, late fees, duplicate payment, and operating
cost. Procurement, security, audit, legal, vendors, and the ERP team also matter.
Measure current exception rate, median resolution time, queue age, routing error,
duplicate payment, and manual touches. The goal is faster correct routing without
increasing payment or privacy risk.

**First scope:** Start with one business unit and two frequent, low-ambiguity
exception classes, such as missing purchase-order match and invalid vendor field.
The system extracts fields, retrieves related records, recommends a reason and
next queue, and shows evidence. A specialist approves or corrects it. Do not let
the first version release payments, create vendors, or change bank details.

**Why AI:** Deterministic validation should still handle exact totals, required
fields, duplicate IDs, and policy rules. Document extraction or classification
may help with varied invoice layouts and free-text exceptions. The workflow
should combine rules and AI rather than ask a language model to reproduce exact
accounting policy.

**Architecture:** Invoice intake stores the original immutable file and event.
Malware and format checks run before parsing. A versioned extractor produces
fields with source coordinates. The workflow service reads authorized data from
the enterprise resource planning (ERP) system, purchase orders, receipts, and
vendor records. Rules compute exact mismatches. A model may classify ambiguous
reason text and draft an explanation. Validation checks schema and policy. The
specialist reviews in the existing queue, and only the ERP integration writes an
approved route. Every stage records versions, evidence, human outcome, and audit
events.

**Data and security:** Separate business units or tenants as required. Restrict
vendor bank and tax data, derive user access from enterprise identity, encrypt
files, define retention and deletion, and prevent invoice text from entering
unapproved logs or shared training. Changes to vendor bank details need a
separate strongly controlled process.

**Evaluation:** Build a time-split set of historical exceptions with expert
labels: use older cases while developing, then test on untouched newer cases.
Include new vendors, scans, multiple languages, duplicate invoices,
handwritten notes, missing purchase orders, conflicting records, and malicious
document content. Measure field accuracy, how often a recommended route is
correct, how many cases of each type are found, evidence correctness, safe
abstention, review time, and serious-error rate. Compare with current rules and
manual routing.

**Rollout:** Replay historical data, run shadow mode on current exceptions, let a
small specialist group review recommendations, then canary one business unit.
Train users on evidence, correction, and escalation. Expansion requires faster
resolution, acceptable correction burden, no guardrail failure, stable cost, and
named ERP, model, security, and operations owners.

**Capacity:** `100,000 / 30` is about `3,333` invoices per day. If 20% become
exceptions, that is about `667` exceptions per day on average. State a peak
factor and document size assumption before sizing workers. Parsing can be
asynchronous behind a durable queue. Interactive review reads should have a
separate latency target from document processing.

**Edge cases:** A duplicate arrives with a changed file name, the purchase order
changes after extraction, one invoice covers several orders, confidence is high
but evidence conflicts, an ERP write times out after succeeding, or the model is
unavailable. Use stable invoice identity, versioned reads, idempotent writes,
reconciliation, and a manual queue.

**Kill criterion:** Stop or narrow the use case if the rules baseline performs as
well, specialist review time does not fall, serious routing errors exceed the
guardrail, required data cannot be used safely, or no team can own production.

</details>

### Question 2: Strong Model, Weak Adoption

A support copilot scores well on the offline evaluation set. During a six-week
pilot, only 12% of eligible agents use it twice, accepted drafts do not reduce
handle time, and leadership wants to roll it out globally because model accuracy
is 92%. What do you say and do?

<details>
<summary>Show answer and detailed explanation</summary>

Do not recommend global rollout from the model score. The pilot has not yet
shown production adoption or workflow impact, and `92%` is incomplete without
the rubric, class balance, segments, error severity, and baseline.

**Validate measurement first:** Confirm which cases were eligible, whether users
actually saw the feature, how repeat use was calculated, and whether handle time
is comparable across case difficulty and agent experience. Check telemetry loss,
pilot selection, seasonality, and whether accepted drafts include large edits.

**Observe the workflow:** Sit with agents and trace several eligible cases. Look
for a separate login, slow response, missing case context, weak citations,
unhelpful tone, extra copy/paste, poor keyboard flow, or a suggestion that arrives
after the agent has already finished. Ask why users ignored, edited, rejected, or
escalated, without treating non-use as disobedience.

**Segment the result:** Compare queue, product, language, tenure, case type,
latency, source coverage, and release. The system may help new agents on one
product while slowing experts elsewhere. One average hides the useful slice.

**Recheck the use case:** A good model may be solving the wrong task. Agents may
need faster evidence retrieval rather than a complete draft, or the selected
cases may already be easy. Compare a search-only baseline and measure edit or
verification burden, not just output correctness.

**Repair with a bounded experiment:** Choose the strongest cohort, fix the top
workflow barriers, improve training and support, and run another time-boxed pilot
with predefined adoption, handle-time, quality, and safety gates. Preserve a
comparison group where practical. Do not hide the weak result by changing the
metric after seeing it.

**Communicate upward:** Say that offline quality is necessary but not sufficient.
Global rollout would multiply support, cost, and risk before proving value. Give
leadership a decision date, the evidence still missing, the focused repair plan,
and explicit outcomes for expand, narrow, redesign, or stop.

**Possible conclusion:** If repeated workflow repairs still produce no useful
outcome, stop this feature and redirect the reusable identity, evaluation, and
model-gateway pieces to a better use case. Adoption is an outcome to earn, not a
number to force.

</details>

## Final Reminder

The strongest FDE answer is not the architecture with the most AI. It is the
smallest credible path from a real business problem to an adopted, measurable,
secure, operable result.
