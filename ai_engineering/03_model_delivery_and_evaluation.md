# Model Delivery and Evaluation

[AI engineering guide](./README.md) | [LLM fundamentals](./01_llm_product_fundamentals.md) | [RAG systems](./02_rag_systems.md) | [System design](../system_design/README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## A Model File Is Not a Production System

A production model needs a controlled lifecycle:

```text
problem and metric definition
    -> versioned data and code
    -> training or model selection
    -> offline evaluation
    -> registry and approval
    -> deployment
    -> shadow or canary
    -> monitoring and feedback
    -> rollback, retraining, or retirement
```

Every arrow needs ownership, reproducibility, and failure behavior.

## 1. Choose the Serving Mode

| Mode | User Experience | Good Fit | Main Concern |
| --- | --- | --- | --- |
| Online synchronous | Caller waits for one response | Low-latency scoring and interactive generation | Tail latency, availability, admission control |
| Online asynchronous | Caller receives a job ID | Long generation or heavy processing | Durable state, queue, progress, retries, cancellation |
| Batch | Many records processed offline | Nightly scoring, backfills, large migrations | Throughput, reproducibility, partial retry, deadline |
| Streaming | Events scored continuously | Fraud, monitoring, personalization | Ordering, state, late events, sustained capacity |
| Edge or on-device | Model runs near data or user | Offline, privacy, very low network latency | Hardware limits, update control, model size |

Choose from workflow and SLO, not from model fashion.

## 2. Define a Latency Budget

For online inference:

```text
end-to-end latency
    = gateway and auth
    + feature or retrieval work
    + queue wait
    + preprocessing
    + model inference
    + postprocessing and policy
    + network return
```

If the user SLO is 500 ms, do not assign 500 ms to the model and hope every
other stage is free. Give each stage a budget and observe p50, p95, and p99.

For generated output, also measure time to first useful output and total
completion time.

## 3. Version the Complete Behavior

Record more than a model name:

- model artifact or provider version,
- training or selection code commit,
- training data snapshot and feature definitions,
- preprocessing and postprocessing version,
- prompt and tool schema version,
- embedding, reranker, and index version for RAG,
- policy and threshold version,
- runtime and relevant hardware configuration,
- evaluation dataset and result,
- approval and rollout state.

Without these, a team cannot explain why yesterday's request differs from
today's or reproduce an incident.

## 4. Use a Model Registry

A registry is a controlled catalog of immutable model versions and metadata.

Example states:

```text
CANDIDATE -> EVALUATED -> APPROVED -> CANARY -> PRODUCTION -> RETIRED
```

State transitions require evidence and authorization. A product alias such as
`standard` or `fraud-current` resolves to one immutable version, and each request
records the resolved version.

The registry does not replace source control, data versioning, or deployment
configuration. It links their identities.

## 5. Build Reproducible Pipelines

A pipeline may include:

1. Validate source data and schema.
2. Split or snapshot data without leakage.
3. Compute features or prepare examples.
4. Train, tune, or select a candidate.
5. Run quality, safety, latency, and cost evaluation.
6. Package the artifact and dependencies.
7. Register evidence and lineage.
8. Require approval for higher environments.
9. Deploy and run smoke tests.
10. Observe a controlled rollout.

Cache expensive deterministic stages by content and version where safe, but
never let a stale cache hide a changed input.

## 6. Prevent Training-Serving Skew

Skew means production computes inputs differently from training or evaluation.

Examples:

- training fills a missing age with the median; serving uses zero,
- training timestamps are UTC; serving parses local time,
- training has a category mapping serving does not know,
- evaluation uses full future information unavailable at prediction time,
- RAG evaluation uses a newer index than production.

Controls:

- shared versioned transformation code where practical,
- schema and range validation at both boundaries,
- feature definitions with point-in-time correctness,
- sample parity tests comparing offline and online results,
- lineage from one request back to its versions,
- canary comparisons on production-shaped inputs.

## 7. Design the Evaluation Set

A useful evaluation set represents the actual decision distribution, not only
easy examples.

Include:

- common cases by meaningful cohort,
- rare but high-impact cases,
- ambiguous and missing-data cases,
- recent failures and regressions,
- unsafe and adversarial cases,
- expected refusal or escalation,
- slices for language, region, device, customer, or other relevant groups.

Keep a stable regression set and a changing recent set. A stable set detects old
breakage; a recent set detects a world that has moved.

Protect a final holdout from repeated prompt or model tuning, or it becomes part
of the training process and overstates generalization.

## 8. Choose Metrics From Consequences

### Classification

Accuracy can hide costly errors. Ask what false positive and false negative mean.

Use:

- precision and recall,
- confusion matrix by class,
- threshold curves,
- calibration,
- business-weighted error cost,
- slice performance.

### Ranking and Retrieval

- recall at K,
- precision at K,
- ranking position,
- coverage and freshness,
- permission correctness.

### Generation

- task correctness,
- evidence support and citation validity,
- appropriate abstention,
- schema and instruction compliance,
- human preference or usefulness,
- policy and privacy violations.

Every quality metric needs latency, reliability, safety, and cost guardrails.

## 9. Automated and Human Evaluation

Deterministic checks are strongest for:

- schema validity,
- exact fields,
- citations pointing to retrieved sources,
- forbidden data patterns,
- code tests,
- latency and cost.

Human review is important for nuanced usefulness, completeness, tone, and domain
correctness. Give reviewers a rubric, examples, conflict process, and agreement
measurement.

Model-based graders can scale comparison, but calibrate them against trusted
human labels. Version the grader and prompt. Test whether it favors longer
answers, a particular style, or outputs from its own model family.

## 10. Release Strategies

### Offline Only

Necessary but insufficient. Saved data cannot reveal every production input,
latency, integration, or user behavior.

### Shadow

Copy eligible real requests to the candidate but do not show candidate output.

Good for latency, error, and quality comparison without direct user impact.
Still apply privacy, consent, retention, and cost controls.

### Canary

Send a small controlled share of real user requests to the candidate. Define:

- eligible cohort,
- traffic percentage,
- observation time,
- quality and safety gates,
- automatic and manual rollback,
- owner.

### A/B Experiment

Compare product outcomes between variants with deliberate experimental design.
A canary primarily reduces release risk; an A/B test estimates product impact.
They may use similar routing but answer different questions.

### Champion/Challenger

Keep the current production version as champion and evaluate challengers against
it continuously or on scheduled windows.

## 11. Rollback

Rollback is a designed operation, not a hopeful plan.

- Keep the prior model and compatible runtime available.
- Separate data migrations from irreversible deployment steps.
- Record which in-flight jobs stay pinned to which version.
- Preserve old prompt, feature, and index compatibility as needed.
- Test the rollback path.
- Define how outputs created by the bad version are identified and remediated.

For a harmful output regression, stop exposure first, then preserve evidence and
diagnose.

## 12. Monitor by Layer

| Layer | Signals |
| --- | --- |
| Product | Task completion, adoption, correction, escalation, business outcome |
| Quality | Labeled performance, claim support, retrieval, human feedback |
| Safety | Block, appeal, policy error, reviewed escape, unauthorized action |
| Data | Schema, missingness, ranges, category frequency, freshness, volume |
| Model | Score or output distribution, calibration, refusal, output length |
| Service | Requests, errors, queue age, latency, saturation, retries |
| Cost | Compute, tokens, storage, egress, cost per useful result |

Aggregate by model, prompt, index, policy, tenant, region, and meaningful cohort
without leaking sensitive content.

## 13. Understand Drift

### Data Drift

The distribution of inputs changes. Example: a support classifier sees a new
product category.

Data drift does not automatically mean quality fell, but it tells the team the
production population differs from its reference.

### Prediction Drift

Output score, class, refusal, length, or tool-choice distribution changes.

This may come from input change, model change, prompt change, or a bug.

### Concept Drift

The relationship between input and correct outcome changes. A fraud pattern that
used to be safe may become risky.

Concept drift requires fresh outcomes or labels to detect reliably.

### Performance Drift

Measured task quality worsens on newly labeled production data.

Do not diagnose all drift by retraining. First identify whether measurement,
schema, preprocessing, traffic, policy, application, infrastructure, or model
behavior changed.

## 14. Delayed Labels and Feedback

Some outcomes arrive seconds later; others arrive weeks later.

Store a prediction or generation event with:

- stable event ID,
- request and entity IDs under privacy policy,
- all behavior versions,
- prediction or output reference,
- timestamp,
- later outcome join key.

When labels arrive, join them without overwriting history. Track label delay and
selection bias: only reviewed, appealed, or clicked items may receive labels.

User thumbs alone are not ground truth. They are one signal.

## 15. Reliability and Capacity

### Online Capacity

```text
required concurrency = peak arrival rate * average service time
```

Add headroom and benchmark on representative input size. Autoscale on useful
signals such as queue age, concurrent requests, latency, accelerator utilization,
and memory, not only CPU.

### Failure Behavior

- timeout before retry,
- bounded retry with backoff and jitter,
- idempotency for side effects,
- fallback model or deterministic rule where safe,
- admission control and load shedding,
- circuit breaker for failing dependencies,
- durable async jobs for long work,
- dead-letter and reconciliation paths,
- honest user-visible status.

A fallback must be evaluated. An old or smaller model can fail differently and
may not satisfy current policy.

## 16. Cost Controls

Track:

```text
unit cost = feature/retrieval + model compute + validation + storage + network
```

Then divide by successful or useful outcomes, not only request count.

Controls:

- right-size model and hardware,
- batch compatible offline work,
- cap input and output,
- cache authorized stable computation,
- avoid repeated preprocessing,
- route by task difficulty,
- reserve budgets before expensive async work,
- detect loops and retry storms,
- archive or delete old artifacts and outputs,
- stop a rollout on cost regression even when quality improves slightly.

## 17. Security, Privacy, and Governance

- Approve data purpose and retention before using production examples.
- Minimize personal and confidential data in training and evaluation.
- Enforce tenant and row/document access outside the model.
- Track source consent, license, deletion, and lineage.
- Protect model artifacts, prompts, features, and evaluation sets.
- Audit privileged access and deployment approval.
- Threat-model poisoning, extraction, prompt injection, unsafe tools, and supply chain.
- Define whether customer data can improve shared models; default assumptions are
  not a contract.
- Ensure deletion reaches training candidates, indexes, caches, and logs according
  to policy.

## 18. Incident Response

When quality suddenly degrades:

1. Confirm the metric and user impact.
2. Identify versions and timeline.
3. Stop harmful automation, pause rollout, or roll back if needed.
4. Preserve request IDs, inputs under policy, outputs, features, and dependency state.
5. Segment by version, cohort, region, and time.
6. Test measurement, schema, preprocessing, data, application, model, and infrastructure hypotheses.
7. Repair the proven cause and canary it.
8. Backfill or remediate affected outputs where required.
9. Add the missing guardrail and assign ownership.
10. Document the incident and verify prevention later.

Changing three components at once destroys evidence.

## Correctness Invariants

1. Every served result identifies the full behavior version that produced it.
2. Only evaluated and approved immutable versions receive production traffic.
3. A stale worker or deployment cannot publish after its rollout or lease is revoked.
4. Rollback restores a known compatible behavior, not only an old model file.
5. Evaluation results identify dataset and all compared versions.
6. Customer data use follows its tenant, consent, purpose, and retention policy.
7. Side-effecting retries use stable operation identity.

## Edge Cases

- New model quality improves overall but harms one important cohort.
- Offline score improves while latency doubles.
- Shadow traffic contains data not approved for the candidate environment.
- Rollback model cannot read a newly changed feature schema.
- Labels arrive only for cases users appeal.
- Autoscaling adds replicas slower than the traffic spike.
- A fallback model violates a newer safety policy.
- Prompt or index changes without changing the model alias.
- Model succeeds but postprocessing corrupts output.
- Monitoring pipeline fails while serving remains healthy.

## Common Mistakes

- Versioning only the model artifact.
- Using one average metric and ignoring slices and consequences.
- Calling shadow output an A/B test result.
- Deploying directly to all traffic after offline evaluation.
- Monitoring input drift without obtaining outcome labels.
- Automatically retraining and deploying from a drift alert with no approval gate.
- Building rollback without testing compatibility.
- Measuring cost per call when most calls are unusable.
- Logging sensitive model inputs by default.

## Possible Follow-up Questions

| Follow-up | Strong Answer Direction |
| --- | --- |
| Online or batch? | Match action deadline and workflow; batch maximizes throughput when users do not wait. |
| What triggers retraining? | Proven performance need, data sufficiency, and a pipeline with evaluation and approval, not drift alone. |
| How do you compare two LLMs? | Versioned representative set, calibrated human and automated rubrics, product metrics, and safety/latency/cost guardrails. |
| How do you rollback a prompt change? | Version and route prompt/config independently while recording the complete behavior bundle. |
| How do you monitor without immediate labels? | Input/output distributions and proxies for early warning, then join delayed labels for actual quality. |

## Interview Explanation

> I deliver a model as a versioned behavior bundle: data, transformations, model,
> prompt, index, policy, runtime, and evaluation. A registry controls approval. I
> validate offline, shadow eligible traffic, canary with explicit quality,
> safety, latency, reliability, and cost gates, and keep a tested rollback. In
> production I monitor user outcome plus data, model, service, and cost layers,
> join delayed labels, and diagnose measurement or pipeline failures before
> assuming retraining is the answer.

## Check Your Understanding

### Question 1: Drift Alert

Input drift crosses a threshold, but no labeled quality metric has changed yet.
Should the system automatically retrain and deploy?

<details>
<summary>Show answer and explanation</summary>

No. Treat drift as an investigation signal. Verify the monitoring pipeline,
identify changed features and cohorts, understand whether the change is expected,
and obtain representative outcomes or labels. A harmless seasonal shift may not
need retraining; a schema bug needs repair, not retraining.

If retraining is justified, the candidate must still pass versioned quality,
safety, latency, and cost evaluation and a controlled rollout.

</details>

### Question 2: Safe Model Release Plan

Outline a release for a new support-ticket classifier.

<details>
<summary>Show answer and detailed explanation</summary>

1. Freeze a candidate artifact with code, data, feature, threshold, and runtime
   versions.
2. Evaluate on a stable regression set, recent set, rare high-impact categories,
   and relevant customer slices.
3. Compare confusion and business-weighted error, calibration, latency, service
   errors, and cost against production.
4. Register evidence and receive required approval.
5. Shadow production-shaped eligible traffic and compare distributions and
   delayed labels without affecting routing.
6. Canary a small low-risk cohort with a fallback and rollback threshold.
7. Expand gradually while observing category-level quality, queue or endpoint
   saturation, user correction, and unit cost.
8. Keep the prior compatible bundle available and record version per decision.
9. After full rollout, continue a holdback or scheduled champion/challenger
   evaluation where appropriate.
10. Document result, ownership, and any affected examples added to regression.

An overall accuracy gain does not justify release if one critical category or
customer cohort regresses beyond its guardrail.

</details>
