# RAG Accuracy and Latency Troubleshooting Playbook

[AI engineering guide](./README.md) | [RAG systems](./02_rag_systems.md) | [Model delivery and evaluation](./03_model_delivery_and_evaluation.md) | [Enterprise AI adoption](../fde_interview/05_enterprise_ai_adoption.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## What This Lesson Solves

A RAG application can fail in two visible ways:

```text
the answer is wrong
the answer is too slow
```

Those symptoms do not identify the broken component. A wrong answer might come
from a missing document, a bad permission filter, weak ranking, lost context, or
generation. A slow answer might come from a queue, query rewriting, retrieval,
reranking, long context, long output, validation, or retries.

The central rule is:

```text
measure the pipeline -> locate the failing stage -> make one targeted change
-> test quality, latency, security, freshness, and cost together
```

Do not start by swapping the language model. First prove which layer failed.

## Beginner Vocabulary

| Term | Plain-English Meaning |
| --- | --- |
| Candidate | A chunk found before final ranking |
| Recall at K | How often the needed evidence appears somewhere in the first K results |
| Precision at K | How much of the first K results is actually relevant |
| Reranker | A second model or rule that puts the most useful candidates first |
| Grounded answer | An answer whose claims are supported by supplied evidence |
| Abstention | A safe response that says evidence is insufficient |
| Latency | Time from receiving a request until work completes |
| Time to first token | Time until the user first sees generated output |
| Tail latency | Slow-request behavior, commonly measured at p95 or p99 |
| p95 | Ninety-five percent of requests finish at or below this time |
| Queue time | Time waiting for a worker or model slot |
| Service time | Time a component actively spends doing the work |
| Latency budget | Maximum time allocated to each stage before the total deadline |
| Golden set | Saved, reviewed examples with expected evidence and answer behavior |
| Cohort | A useful group such as language, tenant, document type, or question type |
| Regression | A previously working behavior that a new version breaks |
| SLO | A measurable operating target such as p95 latency below 2.5 seconds |

## How to Use This Playbook

Use three passes:

1. **Learn:** Read the failure layers and latency stages once.
2. **Practice:** Take one bad query and complete the trace worksheet without
   changing the system.
3. **Interview:** Explain the decision tree, one quality metric, one latency
   budget, one tradeoff, and one rollback plan aloud.

This lesson uses an internal support assistant as a running example. It searches
approved company documents and drafts cited answers for support agents. The
same process applies to legal research, sales enablement, technical support,
enterprise search, and other evidence-based assistants.

## 1. Define Correct and Fast Before Tuning

There is no useful instruction named "make RAG accurate." Define the contract.

Ask:

1. Who is the user, and what decision follows the answer?
2. Which sources are authoritative and current?
3. Must every claim have a citation?
4. What should happen when evidence is absent or conflicting?
5. Which tenants, groups, languages, and document types matter?
6. What is the p50, p95, and p99 deadline?
7. Does the deadline mean first visible output or complete output?
8. What availability, freshness, privacy, and cost limits apply?

### Example Contract

These values are illustrative, not universal requirements:

| Area | Example Target |
| --- | --- |
| User outcome | Agent gets a usable cited draft faster than manual search |
| Retrieval | Needed evidence appears in top 20 for at least 90% of reviewed answerable questions |
| Answer | At least 85% of reviewed drafts are correct, complete enough, and supported |
| Abstention | At least 95% of unanswerable tests avoid inventing an answer |
| Permission safety | Zero unauthorized chunks, citations, or cache hits |
| Freshness | Approved updates searchable within 10 minutes |
| Responsiveness | p95 first token at or below 1.5 seconds |
| Completion | p95 complete answer at or below 2.5 seconds |
| Reliability | At least 99.9% of valid requests return an answer or explicit fallback |
| Cost | Cost per accepted draft stays below the agreed business limit |

A target should identify its dataset, population, time window, and owner. For
example, "90% recall" is incomplete unless everyone knows the questions, K,
source labels, and evaluation version.

## 2. Accuracy Is a Chain, Not One Score

Treat accuracy as six connected checks:

| Layer | The Question to Ask | Typical Evidence |
| --- | --- | --- |
| Source | Does the approved, current document exist? | Source catalog and active version |
| Parsing | Did the useful words, table headers, and structure survive ingestion? | Parsed document and chunk preview |
| Retrieval | Did the needed passage enter the candidate set? | Recall at K and retrieved chunk IDs |
| Ranking | Did useful evidence rank high enough to reach context? | Rank, reranker score, and precision at K |
| Context | Did the final prompt retain all required evidence clearly? | Exact rendered model input |
| Generation | Did the model use evidence, cite it, and abstain correctly? | Answer, claims, citations, and grader labels |

Product usefulness is a seventh check. A factually correct answer can still be
too late, too verbose, hard to verify, or disconnected from the user's work.

### The Accuracy Decision Tree

For one failed question, inspect in this order:

```text
1. Is the expected source approved, current, authorized, and available?
   no  -> repair source lifecycle, permissions, or freshness
   yes
    |
2. Did parsing preserve the expected passage?
   no  -> repair parser, OCR, tables, or chunk construction
   yes
    |
3. Is the expected passage in the retrieval candidates?
   no  -> repair candidate recall
   yes
    |
4. Did it rank into the final context?
   no  -> repair ranking, deduplication, or context selection
   yes
    |
5. Is the exact final context complete and understandable?
   no  -> repair trimming, ordering, headers, or conflict handling
   yes
    |
6. Is the answer supported, complete, cited, and appropriately cautious?
   no  -> repair generation contract, model choice, or validation
   yes -> investigate product presentation or the original label
```

Stop at the first failed step. Later stages cannot recover evidence that an
earlier stage removed.

## 3. Make Every Query Traceable

A single end-to-end timer is not enough. Record one trace across the complete
query path:

```text
request
    -> identity and policy
    -> query planning
    -> embedding
    -> keyword and vector candidates
    -> fusion and reranking
    -> context construction
    -> model queue and generation
    -> citation and policy validation
    -> response
```

### Minimum Trace Fields

| Field | Why It Matters |
| --- | --- |
| `request_id` and trace ID | Join events without guessing |
| Tenant and user authorization version | Reproduce permission behavior safely |
| Query type and cohort | Find failures hidden by an average |
| Source, parser, chunk, embedding, and index versions | Reproduce retrieval |
| Rewrite, reranker, prompt, model, and policy versions | Reproduce ranking and generation |
| Candidate chunk IDs, ranks, and scores | See where expected evidence disappeared |
| Final context chunk IDs and token count | Verify what the model could actually use |
| Output token count and finish reason | Explain generation time and truncation |
| Queue and service time for every remote stage | Separate capacity from slow computation |
| Cache decision and cache namespace | Find stale or cross-scope behavior |
| Timeout, retry, fallback, and error events | Explain long tails and partial results |

Do not automatically log raw questions, document text, or model output. Apply
data minimization, redaction, tenant controls, retention limits, and authorized
debug access. A trace that creates a privacy incident is not good observability.

## 4. Build a Golden Evaluation Set

Production complaints are useful examples, but they are not a complete test
strategy. Build a versioned set before tuning.

Each example should contain:

- the user question and relevant conversation state,
- the user or permission persona,
- whether the question is answerable,
- expected source and passage IDs when answerable,
- required answer claims,
- unacceptable or forbidden claims,
- acceptable citations and fallback behavior,
- tags for tenant, language, domain, document type, risk, and difficulty,
- a human-reviewed label and reason.

Include normal, hard, and negative examples:

- exact product IDs and error codes,
- paraphrases and ambiguous wording,
- answers spanning two sources,
- tables, scanned pages, and nested headings,
- current and superseded versions,
- conflicting approved documents,
- no-answer questions,
- permission-denied documents,
- prompt injection inside retrieved text,
- long conversations and multilingual questions.

A small set of carefully reviewed real examples is more useful than a large set
of weak labels. Grow it from production failures and customer workflows. Keep a
held-out portion so repeated tuning does not merely memorize the development set.

### Retrieval Measures in Plain Language

Suppose 10 answerable questions each have one required passage:

```text
8 questions include that passage somewhere in the top 20

Recall@20 = 8 / 10 = 80%
```

If the correct passage exists at rank 18, recall at 20 passes, but users may
still get poor context. Also inspect rank, precision, and final-context coverage.

| Measure | What It Reveals |
| --- | --- |
| Recall at K | Whether candidate retrieval found needed evidence |
| Precision at K | Whether candidates contain too much unrelated material |
| Mean reciprocal rank | Whether the first useful result appears early |
| Context evidence coverage | Whether every required passage reached the model |
| Permission precision | Whether every result was authorized; any miss is a security failure |
| Freshness coverage | Whether results use the active approved source version |

### Answer Measures in Plain Language

Score dimensions separately:

- **Correctness:** Are the answer's factual claims right?
- **Groundedness:** Does supplied evidence support each factual claim?
- **Completeness:** Does it include the information required for the task?
- **Citation correctness:** Does each citation point to supporting text?
- **Abstention:** Does it refuse or qualify when evidence is insufficient?
- **Instruction compliance:** Does it obey format and policy?
- **Usefulness:** Can the target user complete the workflow with it?

Automated graders can help with volume, but calibrate them against trusted human
labels. Inspect disagreements. Do not hide six dimensions inside one unexplained
"quality score."

## 5. Repair Accuracy by Layer

### 5.1 Source, Parsing, and Freshness Failures

**Symptoms**

- The expected source is absent from the active catalog.
- Search returns an old policy after an update.
- A table has values but no column headers.
- Scanned pages produce empty or scrambled chunks.

**Checks**

1. Open the authoritative source and verify its version.
2. Follow its ingestion event, parse status, chunk count, and index activation.
3. Compare raw content, normalized content, and final chunks.
4. Check deletion, permission, and freshness caches.
5. Compare failed cohorts by file type, parser version, and connector.

**Targeted fixes**

- Add parser quality gates before index activation.
- Preserve headings, table headers, lists, and page locations.
- Use OCR only where needed and flag low-confidence extraction.
- Retry transient ingestion failures through a durable queue and dead-letter path.
- Activate a complete version atomically; keep the prior complete version for rollback.
- Reconcile source inventory periodically so missed change events are repaired.

**Proof**

Reparse the failed files, verify expected passages directly, run file-type
regressions, and confirm the active index contains the correct source versions.

### 5.2 Candidate Recall Failures

This layer failed when the expected passage exists in the index but is absent
from the candidate set.

Investigate in this order:

1. **Filters:** Is a valid source removed by a mistaken tenant, group, date,
   language, or document-type filter?
2. **Exact language:** Does the question contain an error code, product name, or
   quoted phrase that keyword search handles better than semantic search?
3. **Chunk boundaries:** Is the answer split from its heading, table header, or
   qualifying sentence?
4. **Query mismatch:** Does conversation shorthand or an acronym need a safe
   rewrite using earlier context?
5. **Embedding fit:** Does the embedding version work for this language and domain?
6. **Multi-part question:** Must the query be decomposed into two retrieval needs?
7. **Index settings:** Did approximate search settings trade away too much recall?

Targeted fixes include hybrid keyword and vector candidates, structure-aware or
parent-child chunks, tested query rewriting, metadata repair, domain-appropriate
embeddings, and multi-query retrieval for genuinely multi-part questions.

Increasing K is an experiment, not a complete solution. It can improve recall
while increasing latency, reranking cost, context noise, and the chance of
including conflicting evidence. Measure all of those effects.

### 5.3 Ranking and Precision Failures

This layer failed when the needed passage is in the candidate set but ranks too
low to enter final context.

Check:

- duplicate or near-duplicate chunks occupying the top ranks,
- stale or low-authority sources outranking approved canonical sources,
- vector and keyword scores being combined on incompatible scales,
- reranker input truncating the important part of a chunk,
- missing language, product, recency, or source-quality signals,
- a broad query whose intent was never identified.

Possible fixes:

- deduplicate candidates by source and passage identity,
- use a tested fusion method for independent candidate lists,
- rerank only a bounded candidate set,
- add explicit source authority and freshness features,
- preserve enough local context for the reranker,
- diversify final evidence when several parts of the answer are required.

Prove the change with rank distributions, precision, context evidence coverage,
latency, and subgroup results. One attractive example is not a release gate.

### 5.4 Context Construction Failures

The correct passage can be retrieved and still become unusable.

Inspect the exact final model input, not the intended template. Look for:

- token trimming that drops a heading or qualifying sentence,
- duplicated chunks consuming the context budget,
- a table row separated from its column names,
- citations whose IDs no longer match reordered chunks,
- conflicting versions with no date or authority label,
- important evidence buried among unrelated text,
- conversation history crowding out current evidence.

Fixes include a strict token budget, source-aware deduplication, structure
preservation, explicit source labels, conflict rules, and deterministic citation
mapping. Long context is capacity, not a guarantee that the model will use every
piece of evidence equally well.

### 5.5 Generation and Validation Failures

Only investigate this layer after proving that complete evidence reached the model.

Check:

1. Does the instruction clearly say to answer from supplied evidence?
2. Is insufficient or conflicting evidence behavior explicit?
3. Does output length or truncation remove qualifications or citations?
4. Did prompt, model, decoding, or policy versions change?
5. Does each citation actually support its neighboring claim?
6. Does a deterministic rule or database tool belong in the workflow instead?

Targeted fixes include a clearer answer contract, claim-level citations,
abstention, structured output, deterministic validation, a better-suited model,
or an application tool for exact facts. Fine-tuning may help stable behavior, but
it does not repair missing or stale evidence.

### 5.6 Security Is Part of Accuracy

An unauthorized answer is not "accurate enough." Never improve apparent recall
by weakening permission filters.

Test:

- cross-tenant source IDs and guessed citation links,
- users whose group membership just changed,
- cached results before and after permission revocation,
- deleted and superseded source versions,
- retrieved text containing malicious instructions,
- debug traces and evaluation exports containing private content.

Identity-derived filters must be enforced during candidate retrieval, source
fetch, citation opening, and cache lookup. The model is not the authorization
boundary.

## 6. Build a Latency Budget

Measure three user-visible times:

```text
time to first useful output
time to complete output
time to recover or return a safe fallback
```

For each stage, record queue time and service time separately. A fast model
behind a long queue still creates a slow product.

### Example p95 Budget

This illustrative budget totals 2,500 milliseconds:

| Stage | Budget |
| --- | ---: |
| Identity and policy | 50 ms |
| Query planning | 120 ms |
| Query embedding | 80 ms |
| Keyword and vector candidate retrieval | 180 ms |
| Fusion and reranking | 220 ms |
| Context construction | 50 ms |
| Model queue | 200 ms |
| Inference until first token | 500 ms |
| Remaining token generation | 800 ms |
| Citation and policy validation | 100 ms |
| Network and deadline headroom | 200 ms |
| **Total allocation** | **2,500 ms** |

Keyword and vector searches can run concurrently, so their budget is the slower
branch plus orchestration overhead, not both times added together.

Stage p95 values do not mathematically add up to end-to-end p95. Use the table as
an engineering allocation, then measure the actual end-to-end distribution under
representative load.

## 7. Locate Latency Before Optimizing

| Slow Stage | What to Inspect First | Targeted Options |
| --- | --- | --- |
| Identity and policy | Remote calls, repeated group lookup, policy-store health | Request-scoped reuse, indexed policy data, safe short-lived cache |
| Query planning | LLM rewrite on every query, long prompt, retries | Rules for simple queries, conditional rewrite, smaller model, strict timeout |
| Embedding | Network distance, batching mismatch, cold workers | Regional placement, connection reuse, right-sized batching, warm capacity |
| Retrieval | Filter selectivity, index health, shard fan-out, hot partition | Better partitioning, indexed filters, replicas, locality, capacity |
| Reranking | Too many candidates, large chunks, slow model | Smaller tested R, shorter inputs, batch scoring, conditional rerank |
| Context | Repeated source fetches, serialization, token counting | Store required metadata with chunks, deduplicate once, bounded construction |
| Model queue | Saturation, tenant burst, low quota, cold start | Admission control, fair queues, autoscaling, reserved enterprise capacity |
| Generation | Large context, long output, slow model | Compact evidence, lower output limit, routing, faster model if quality passes |
| Validation | Another full model call, sequential independent checks | Deterministic checks, parallel checks, smaller calibrated judge |
| End-to-end tail | Retries, dependency timeouts, synchronized bursts | Deadline propagation, retry budget, jitter, circuit breaker, backpressure |

### Fast Changes That Preserve Quality

Evaluate these before accepting a quality loss:

- Run independent keyword and vector searches concurrently.
- Precompute parsing and embeddings during ingestion.
- Reuse network connections and keep dependent services regionally close.
- Skip rewriting when the query is already explicit.
- Skip reranking when exact search returns one high-confidence canonical result.
- Deduplicate before reranking and context construction.
- Bound conversation history, evidence, and output length.
- Stream output after required pre-generation safety checks.
- Use a safe timeout and fallback instead of waiting through repeated failures.
- Route simple and complex questions differently when evaluation proves the gate.

Streaming improves perceived latency and time to first token. It does not reduce
the total computation by itself.

### Caching Without Breaking Correctness

Cache only when the key and invalidation policy preserve:

- tenant and user authorization scope,
- source and index version,
- prompt, model, and policy version,
- freshness requirements,
- deletion and permission revocation,
- language and relevant conversation state.

Useful candidates include immutable source parsing, embeddings, authorized query
transformations, and carefully scoped retrieval results. A globally cached final
answer for private or rapidly changing data is dangerous.

### Capacity in Plain Language

Use Little's Law for a first estimate:

```text
concurrent work = arrival rate * average time in the system
```

At 20 requests per second and 2.5 seconds per request:

```text
20 * 2.5 = about 50 in-flight request workflows
```

If model work takes 1.5 seconds on average:

```text
20 * 1.5 = about 30 simultaneous model operations before headroom
```

This is a starting estimate, not a capacity guarantee. Load test burstiness,
output lengths, tenant concentration, worker limits, and p95/p99 behavior.

## 8. Optimize Accuracy, Latency, and Cost Together

Every proposed improvement is a configuration to evaluate, not a belief.

### Configuration Worksheet

| Version | Candidate Method | Candidate K | Rerank R | Context Tokens | Generator | Recall | Supported Answers | p95 | Cost per Accepted Answer |
| --- | --- | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: |
| Baseline |  |  |  |  |  |  |  |  |  |
| A |  |  |  |  |  |  |  |  |  |
| B |  |  |  |  |  |  |  |  |  |

Apply hard gates first:

1. No permission or policy regression.
2. Freshness and deletion contracts still pass.
3. Required high-risk cohorts meet quality thresholds.
4. p95 and p99 meet the user deadline under load.
5. Cost per useful outcome is sustainable.

Among versions that pass, choose a sensible point on the quality-latency-cost
frontier. The version with the highest offline quality is not automatically the
best product if it misses the workflow deadline.

### Route by Demonstrated Need

A tested router can use a fast path for explicit, single-source questions and a
deeper path for ambiguous or multi-source questions:

```text
explicit exact lookup -> keyword/hybrid retrieval -> compact answer
ambiguous question    -> rewrite -> broader candidates -> rerank -> answer
multi-part question   -> decompose -> retrieve per part -> synthesize
no supported evidence -> safe fallback or source search
```

The routing decision needs its own evaluation. A misrouted hard question can be
fast and wrong.

## 9. Production Incident Runbook

When quality or latency regresses:

1. **Contain:** Stop unauthorized exposure immediately. Disable a broken cache,
   revoke access, or roll back the serving version when needed.
2. **Confirm:** State the symptom with a metric, start time, cohort, and baseline.
3. **Segment:** Compare tenant, region, language, query type, source type, and version.
4. **Inspect changes:** List recent source, parser, index, embedding, reranker,
   prompt, model, policy, infrastructure, and traffic changes.
5. **Trace one request:** Find the first stage whose output or timing differs
   from a known-good request.
6. **Reproduce:** Replay saved examples in a protected environment with the same versions.
7. **Mitigate:** Roll back, bypass one optional stage, reduce load, or return a
   clear fallback. Preserve authorization and evidence requirements.
8. **Verify:** Check end-to-end and stage metrics, security tests, and important cohorts.
9. **Prevent recurrence:** Add the failure to the golden set, alert, runbook, and release gate.

Change one major variable at a time during diagnosis. Five simultaneous tuning
changes can hide the cause and make rollback unclear.

### Worked Accuracy and Latency Incident

Assume Monday's release activated a new parser/index and a new LLM query rewriter.
Users report missing policy answers and six-second waits.

**Step 1: State the regression**

```text
Recall@20 fell from 91% to 68% for PDF policy questions.
End-to-end p95 rose from 2.1 seconds to 5.8 seconds.
Other document types retained normal recall.
```

**Step 2: Inspect accuracy by layer**

Failed-query traces show the expected passage is absent from every candidate.
The source is approved and current, but parsed PDF output lost text after nested
tables. The active index contains 30% fewer PDF chunks than the prior version.

This is an ingestion failure. Changing the generator cannot recover absent text.

**Step 3: Inspect latency by stage**

Stage traces show query planning p95 increased from 120 ms to 2.0 seconds. The new
rewriter runs for every query and retries once on timeout. Retrieval and generation
service time remain near baseline.

This is a query-planning and retry failure, separate from the parser failure.

**Step 4: Mitigate**

- Atomically reactivate the last complete index version.
- Disable the new rewriter or use it only for queries that need rewriting.
- Enforce one deadline-aware attempt and fall back to the original query.
- Keep permission filters and citation requirements unchanged.

**Step 5: Repair and prove**

- Add nested-table PDFs and expected passages to parser release tests.
- Add an index completeness gate by source type.
- Compare conditional rewrite quality against the golden set.
- Load test with rewriter failures and bursts.
- Canary parser and rewriter changes separately next time.
- Confirm recall, answer support, p95/p99, security, freshness, and cost before rollout.

The lesson is not merely "roll back." It is to isolate two independent causes
using source evidence and stage timings.

## 10. Complexity and Scale Aloud

Define:

- `N`: total indexed chunks,
- `d`: embedding dimensions,
- `K`: retrieved candidates,
- `R`: candidates sent to the reranker,
- `C`: context tokens sent to the generator,
- `O`: output tokens generated.

### Ingestion

Storing dense vectors alone takes roughly `O(N * d)` numeric values, plus source
text, metadata, search-index overhead, and replicas. Creating embeddings processes
the corpus once per embedding version. Incremental ingestion avoids recomputing
unchanged chunks.

### Query

Exact dense comparison against every vector is roughly `O(N * d)` work per query.
Production approximate-nearest-neighbor indexes avoid a full scan, but their true
latency and recall depend on index type, settings, filters, data, and hardware.
Do not claim that every vector search is simply `O(log N)`.

Reranking is roughly proportional to `R` candidate pairs and their text length.
Context construction is proportional to selected evidence size. Model latency
usually grows with processed input and generated output, so `C` and `O` are
important operating variables even though model internals differ.

### Interview Explanation

> Offline storage is dominated by source content, metadata, and approximately
> N times d vector values before index overhead and replicas. Online retrieval
> depends on the selected approximate index, so I would benchmark recall and
> p95 latency with real filters instead of promising a universal Big-O. Reranking
> grows with the number and length of candidates, while generation cost and
> latency grow with context and output. I bound K, R, C, and O, then load test the
> complete pipeline under representative traffic.

## 11. Edge Cases to Test Aloud

- No approved source answers the question.
- Two current approved sources disagree.
- The answer needs two distant passages.
- An exact error code has little semantic meaning.
- A table row is separated from its header.
- A scanned PDF has poor OCR confidence.
- The user's group changes after a retrieval result was cached.
- A source is deleted while an answer is streaming.
- The question and source use different languages.
- Conversation history contains a misleading earlier assumption.
- Retrieved text contains instructions intended to manipulate the model.
- One tenant sends a burst that could delay every other tenant.
- The vector service is down while keyword search is healthy.
- The reranker times out after retrieval succeeds.
- A retry finishes after the user's deadline.
- A new model gives shorter but less complete answers.

For each edge case, say the expected behavior, observable signal, fallback, and
test. Naming the case without defining correct behavior is incomplete.

## 12. Testing Strategy

| Test Level | What to Test | Example Release Gate |
| --- | --- | --- |
| Unit | Parser structure, filters, token budgets, citation mapping | Headers and permissions survive transformations |
| Integration | Connector through active index; query through final context | Expected passage and versions appear |
| Offline retrieval | Recall, precision, rank, permission, freshness by cohort | No critical cohort regresses beyond threshold |
| Offline answer | Correctness, support, completeness, citation, abstention | Human-calibrated score meets target |
| Security | Cross-tenant, revoked access, cache scope, prompt injection | Zero unauthorized evidence or action |
| Failure | Timeouts, partial outage, retries, stale index, rollback | Explicit fallback arrives before deadline |
| Load | Steady, burst, hot tenant, long output, dependency slowdown | p95/p99 and error rate meet SLO |
| Shadow | New version on copied representative traffic | No hidden cohort or cost regression |
| Canary | Small controlled production share with rollback | Guardrails remain healthy before expansion |

### Speak the Test Plan Aloud

> I would first replay a versioned golden set and score retrieval separately
> from generation. I would segment by answerability, tenant, language, document
> type, and risk. Then I would run permission and freshness tests, inject stage
> failures, and load test p50, p95, p99, queue time, and service time. I would
> shadow the complete version, canary one change at a time, and automatically
> stop or roll back when a hard guardrail fails.

## 13. Possible Follow-up Questions

| Follow-up | Strong Answer Direction |
| --- | --- |
| Recall is low. Do you increase K? | First find misses by filter, parser, chunks, exact terms, query, embedding, and index. Test K as one bounded tradeoff. |
| Recall is high but answers are wrong. What next? | Verify final-context coverage, conflicts, ordering, prompt contract, model behavior, citations, and abstention. |
| How do you cut latency in half? | Start from stage traces and output length; optimize the dominant critical path, then rerun quality and load gates. |
| Can you cache RAG answers? | Only with authorization, source, policy, model, conversation, freshness, deletion, and invalidation in the design. |
| Does streaming solve latency? | It improves first-visible-output time, not total work; pre-stream safety and post-stream validation still matter. |
| Would a larger context fix quality? | Not necessarily. Improve evidence selection and structure; longer context adds latency, cost, and possible distraction. |
| When should you use a larger model? | When complete evidence reaches the model and a representative evaluation proves the smaller model misses required behavior. |
| How do you support enterprise tenants? | Identity-derived retrieval filters, scoped caches and logs, quotas, fair scheduling, audit, revocation, and dedicated tiers where required. |
| What do you alert on? | Permission failures, freshness lag, retrieval and answer regressions, stage p95/p99, queue depth, errors, fallback rate, and unit cost. |
| How do you handle a vector outage? | Use an approved keyword or source-search fallback where quality permits, or abstain clearly; do not fabricate an answer. |

## 14. Concise Interview Summary

> I define accuracy as a chain from source availability through parsing,
> retrieval, ranking, final context, and grounded generation. I build a golden
> set with expected passages, answer claims, unanswerable cases, permissions,
> and cohorts. Every request records version IDs, candidate and context IDs, and
> queue and service time by stage. For a wrong answer, I stop at the first failed
> layer and make a targeted change. For latency, I set an end-to-end budget,
> inspect the critical path and tail, then consider parallel retrieval,
> conditional stages, bounded candidates and tokens, routing, safe caching,
> capacity, deadlines, and fallbacks. Every release must pass quality, security,
> freshness, p95/p99, reliability, and cost gates, with canary and rollback.

## Check Your Understanding

### Question 1: Retrieval Passes but the Product Still Fails

Your dashboard shows Recall@20 at 94%, but reviewers accept only 55% of answers.
Complete-answer p95 is 6 seconds against a 2.5-second target. What do you inspect
and change?

<details>
<summary>Show answer and detailed explanation</summary>

Do not conclude that retrieval is healthy from one aggregate number.

1. Segment Recall@20 by answerability, language, tenant, document type, and risk.
2. Check whether all required evidence reaches final context, not merely the top 20.
3. Review candidate precision, ranks, duplication, context trimming, source
   authority, freshness, and conflicts.
4. For cases with complete context, label correctness, support, completeness,
   citations, abstention, and instruction compliance separately.
5. Inspect exact prompts and version IDs for failed cases. Only then test prompt,
   validation, model, or tool changes.
6. Break p95 into queue and service time for planning, embedding, retrieval,
   reranking, context, generation, and validation.
7. Inspect context and output token distributions, retry counts, model queue, and
   slow cohorts. End-to-end p95 alone does not identify the cause.
8. Optimize the dominant stage. Examples include conditional rewriting,
   deduplication before reranking, smaller tested R, compact evidence, bounded
   output, a safe model route, parallel independent checks, or more capacity.
9. Rerun golden-set, permission, freshness, failure, and representative load tests.
10. Canary one version with rollback gates for answer support, p95/p99, and cost.

Recall@20 can pass while the right passage ranks too low, final context drops it,
the model misuses it, or one important cohort fails. The six-second latency is a
separate symptom until tracing proves a shared cause such as excessive candidates
creating both noisy context and slow reranking.

</details>

### Question 2: A New Enterprise Tenant Doubles p95

After onboarding a large tenant, overall p95 doubles and smaller tenants report
timeouts. Accuracy is unchanged for completed requests. Design the diagnosis,
mitigation, and permanent fix.

<details>
<summary>Show answer and detailed explanation</summary>

1. Confirm the start time and segment p95, p99, queue time, error rate, output
   length, and throughput by tenant and stage.
2. Compare arrival rate, burst pattern, query complexity, source size, filters,
   candidate counts, context tokens, and model tokens against capacity assumptions.
3. Check for a hot retrieval partition, model queue saturation, one tenant's long
   outputs, synchronized retries, or a quota/configuration change.
4. Protect the service with per-tenant admission limits, fair queues, deadline
   propagation, bounded retries, and a clear fallback. Do not weaken permissions
   or silently give low-quality answers.
5. If needed, temporarily reduce that tenant's optional expensive path, add
   approved capacity, or place it in a dedicated pool while preserving its SLO.
6. Use Little's Law to recalculate expected in-flight workflows and model
   operations, then include burst and utilization headroom.
7. Fix the demonstrated bottleneck: repartition a hot index, add replicas, reserve
   model concurrency, autoscale earlier, cap output, or route expensive queries.
8. Load test the observed tenant distribution, burst, long-output cases, and
   dependency slowdown. Verify fairness and p95/p99 for every tenant tier.
9. Add tenant saturation, queue age, throttling, and retry-storm alerts. Record
   capacity and isolation expectations in the onboarding checklist.

The key enterprise principle is noisy-neighbor isolation. One customer's burst
must not consume every shared retrieval worker or model slot. Quotas, fair
scheduling, capacity planning, and optional dedicated pools make that contract
operational.

</details>

## Primary References

- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
- [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172)
- [OpenAI latency optimization guide](https://developers.openai.com/api/docs/guides/latency-optimization)
- [OpenAI evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
