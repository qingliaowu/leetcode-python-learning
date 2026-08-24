# Behavioral Story Workbook

[FDE track](./README.md) | [Role map](./01_role_and_interview_map.md) | [Customer solutioning](./02_customer_discovery_and_solutioning.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## What Behavioral Interviews Test

Behavioral questions ask for evidence of judgment, ownership, communication, and
growth. They are not a break from technical evaluation.

For an FDE-style role, interviewers may care whether you can:

- operate when requirements are incomplete,
- earn trust with technical and non-technical stakeholders,
- make and explain a difficult tradeoff,
- deliver and operate real software,
- disagree without damaging collaboration,
- respond honestly when a project or decision fails,
- connect technical work to a user or customer outcome.

Use only real experiences. Change confidential names and details when needed,
but do not invent actions or results.

## STAR-L From Scratch

Use five parts:

| Part | Purpose | Typical Share of Answer |
| --- | --- | ---: |
| Situation | Give only context needed to understand the stakes. | 10-15% |
| Task | State your responsibility, goal, and constraints. | 10-15% |
| Action | Explain what **you** decided, did, and communicated. | 50-60% |
| Result | Give measured or observable consequences. | 10-15% |
| Learning | Explain what changed in your later judgment or process. | 10% |

Most weak answers spend too long on Situation and say too little about Action.

## Build a Six-Story Bank

One story can answer several prompts from different angles, but prepare enough
range that one project is not forced into every answer.

| Story Type | Evidence to Prepare |
| --- | --- |
| Ambiguous ownership | How you defined the problem, aligned people, and chose a first step |
| Customer or user impact | How you discovered the need and measured a changed outcome |
| Technical depth | A difficult design, implementation, debugging, or performance decision |
| Conflict or disagreement | How you understood interests, used evidence, and reached a decision |
| Failure or incident | Your contribution, immediate response, accountability, and prevention |
| Cross-functional delivery | How engineering, product, security, sales, or operations worked together |

Optional additional stories include mentoring, prioritization, ethical judgment,
cost reduction, and changing your mind after new evidence.

## Story Inventory

Fill this before writing polished answers:

| Project | Your Role | Customer/User | Hard Decision | Observable Result | Useful Prompts |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

Choose stories with meaningful decisions, not merely large project names.

## The Detailed Story Worksheet

### Situation

- When and where did this happen?
- Who was affected?
- Why did it matter?
- What was already true when you entered?

Limit this to two or three sentences.

### Task

- What outcome were you personally responsible for?
- What authority did you have?
- What deadline, risk, or constraint made it difficult?
- What would failure mean?

### Action

Prepare a sequence of decisions:

1. What did you learn first?
2. Which alternatives did you consider?
3. What did you personally recommend or implement?
4. How did you communicate it?
5. What resistance or surprise appeared?
6. How did you adapt?
7. How did you verify the work?

Use "I" for your own actions and "we" only for genuinely shared work.

### Result

Use the strongest truthful evidence available:

- before and after metric,
- time or cost avoided,
- users or workloads migrated,
- incident impact contained,
- deadline met or consciously changed,
- risk retired,
- customer decision enabled,
- qualitative feedback from a credible stakeholder.

If no number exists, say what was observed and how you know. Never manufacture a
percentage because quantified answers sound impressive.

### Learning

Avoid empty endings such as "communication is important."

Name a changed behavior:

```text
After that project, I added a written rollback owner and permission test to every
integration launch checklist. On the next migration, that exposed a missing
service account permission two days before cutover instead of during it.
```

## A Fictional Worked Example

The details below are invented to show structure. Replace them with your own
truthful experience.

### Prompt

"Tell me about a time you handled an ambiguous customer problem."

### Situation

An internal operations team reported that a new order integration was "too
unreliable" to expand. No shared definition of reliability existed, and the
vendor and application teams blamed each other.

### Task

I owned the technical investigation and a recommendation for whether to expand,
pause, or redesign the integration before the next regional launch.

### Action

I first converted "unreliable" into three observable states: requests rejected
before acceptance, accepted orders that never reached a terminal state, and
duplicate downstream orders. I added a correlation ID across the API, queue,
worker, and vendor call, then reconstructed one week of failures.

The data showed that most missing orders were accepted successfully but exhausted
fast retries during a vendor slowdown. Duplicate orders came from replaying those
messages without a downstream idempotency key. I proposed a two-part repair:
bounded delayed retries with a dead-letter review path, and a stable order key
enforced by our database and included in vendor requests.

I reviewed the failure model with operations in plain language, agreed on a
dashboard and manual recovery owner, and ran a failure-injection test with the
vendor team before enabling a small traffic canary.

### Result

The canary completed without lost or duplicated test orders during the agreed
observation period. Operations could see and replay terminal failures, and the
launch owner approved a staged expansion rather than the original all-at-once
cutover. Use your own measured figures here if you have them.

### Learning

I learned not to accept a broad reliability label as a diagnosable problem. I now
define workflow states, identifiers, and ownership before gathering incident
data, which makes cross-team debugging faster and less personal.

### Why This Structure Works

- The customer problem becomes measurable.
- Personal technical actions are visible.
- Communication and implementation both matter.
- The result is observable without invented revenue.
- The learning changes later behavior.

## Prepare the "Why This Role?" Answer

This is not a STAR story, but it still needs evidence.

Use:

```text
experience -> insight about your best work -> accurate role understanding -> fit
```

Example shape:

```text
While building [real project], I enjoyed both [specific engineering work] and
[specific user/customer responsibility]. I found that I am strongest when I can
move from an unclear operational need to a working system and explain the
tradeoffs to the people using it. From this role's description and my recruiter
conversation, its focus on [actual responsibility] offers more of that work. My
experience in [evidence] gives me a foundation, and I want to deepen [honest gap].
```

Avoid generic claims such as loving customers, loving challenges, or wanting to
work at a prestigious company.

## High-Value Follow-up Drill

After every story, answer these without notes:

1. What was the hardest decision?
2. Which option did you reject and why?
3. What did you personally do versus the team?
4. Who disagreed and what did you learn from them?
5. What data supported the decision?
6. What would you do differently now?
7. What happened after the immediate result?
8. How did this affect the customer or user?
9. What was the technical detail you simplified in the first answer?
10. Which confidential detail must remain generalized?

Interviewers often find the real signal in follow-ups, not the rehearsed opening.

## Failure Stories

A strong failure story does not secretly describe a perfect success.

Include:

- the decision, omission, or assumption you owned,
- the consequence,
- how you reduced immediate harm,
- how you communicated without hiding,
- the specific system or process change afterward,
- evidence that the learning persisted.

Do not blame a customer, teammate, or vague communication issue. Context matters,
but accountability must be visible.

## Conflict Stories

Conflict does not need shouting. A genuine technical disagreement is enough.

Explain:

1. The shared goal.
2. Each side's concern and evidence.
3. How you tested assumptions or clarified decision rights.
4. What decision was made.
5. How you supported execution even if your option was not chosen.

The goal is not to prove that you won. It is to show sound judgment and durable
collaboration.

## Communicate at Two Depths

Practice each story in:

- **90 seconds:** outcome, decision, personal action, result, learning.
- **4 minutes:** enough architecture and tradeoff detail for a technical follow-up.

If the listener is non-technical, translate mechanism into consequence:

```text
Technical: "We added idempotency and delayed retries."

Plain language: "A repeated delivery could no longer create a second order, and
temporary vendor failures waited before trying again instead of creating a
traffic spike."
```

## Assumptions and Boundaries

- Confirm how long the interviewer wants the answer to be.
- Protect confidential customer names, data, security details, and contracts.
- Distinguish facts you measured from estimates or team interpretation.
- Do not claim sole credit for shared work.
- Do claim your own decisions and implementation specifically.
- Say when the final business outcome was outside your observation window.

## Common Mistakes

- Giving a project history instead of answering the question.
- Spending two minutes on context and twenty seconds on action.
- Repeating "we" until personal contribution disappears.
- Inventing precise metrics or taking credit for another person's work.
- Describing technical actions with no user or customer consequence.
- Describing stakeholder management with no technical judgment.
- Choosing a failure that caused no real consequence.
- Ending without learning or evidence that behavior changed.
- Memorizing exact sentences until follow-up questions break the answer.

## Possible Interview Questions

| Prompt | What to Demonstrate |
| --- | --- |
| Tell me about an ambiguous problem. | Discovery, structure, ownership, and adaptation |
| Tell me about customer impact. | Outcome, empathy, technical contribution, and evidence |
| Tell me about a difficult technical decision. | Alternatives, constraints, depth, and tradeoffs |
| Tell me about disagreement. | Listening, evidence, decision process, and collaboration |
| Tell me about a failure. | Accountability, mitigation, learning, and prevention |
| Tell me about competing priorities. | Decision criteria, communication, and consequences |
| Explain something complex to a non-technical person. | Audience model, analogy, checks for understanding |
| Tell me when you changed your mind. | Intellectual honesty and evidence response |

## Behavioral Mock Scorecard

Give yourself one point for each:

- [ ] I answered the exact prompt in the first sentence.
- [ ] Situation and Task took less than one-third of the answer.
- [ ] My personal decisions and actions were unmistakable.
- [ ] I explained at least one considered alternative or tradeoff.
- [ ] Technical detail was accurate and matched the listener.
- [ ] Customer or user impact was explicit.
- [ ] Results were truthful, observable, and not exaggerated.
- [ ] Learning named a later behavior or process change.
- [ ] I handled three follow-ups without contradicting the opening.
- [ ] The answer fit the requested time and protected confidential information.

## Check Your Understanding

### Question 1: Repair a Weak Action Section

Why is this weak, and how should it change?

```text
We worked hard with several teams, improved the architecture, and communicated
often until the launch succeeded.
```

<details>
<summary>Show answer and explanation</summary>

It hides the candidate's role, decisions, technical actions, conflict, and
evidence. Replace it with truthful specifics such as:

```text
I mapped the three failure paths and found that our queue retry could repeat a
payment write. I proposed an operation ID with a database uniqueness constraint,
wrote the migration and replay test, and asked the payments owner to review the
failure contract. When operations raised concern about stuck requests, I added a
reconciliation report and named an owner before the canary.
```

This version shows personal analysis, implementation, collaboration, adaptation,
and verification. The exact content must come from the candidate's real story.

</details>

### Question 2: Build a Failure Answer Outline

You released a configuration change that caused a one-hour service degradation.
What should a strong STAR-L outline include?

<details>
<summary>Show answer and detailed explanation</summary>

**Situation:** Briefly state the service, affected users, and severity without
dramatic blame.

**Task:** State that you owned or approved the change and became responsible for
restoring safe service and explaining what happened.

**Action:** Describe how you detected impact, stopped or rolled back the change,
communicated status, preserved evidence, and verified recovery. Explain why the
change passed existing checks and the decision you made at the time. Name your
own omission directly.

**Result:** Give truthful duration, affected scope, recovery evidence, and any
customer communication. Do not hide harm behind later improvements.

**Learning:** Name a durable change such as typed configuration validation,
staged rollout, automated rollback threshold, peer review for high-risk fields,
or a runbook. Explain where you later used that change and what evidence shows it
worked.

The answer should show accountability and improved judgment, not perfection.

</details>
