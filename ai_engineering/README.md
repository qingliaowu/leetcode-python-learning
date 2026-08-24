# AI Engineering for Beginners

[Repository home](../README.md) | [FDE track](../fde_interview/README.md) | [Study plans](../INTERVIEW_STUDY_PLANS.md) | [System design](../system_design/README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

AI engineering turns a model into a useful, safe, measurable product. Calling a
model is one step. Production work also includes data, retrieval, evaluation,
identity, policy, latency, reliability, rollout, monitoring, and cost.

No machine-learning package is required for these lessons. They teach the mental
models and interview decisions first.

## Learning Path

| Order | Lesson | Main Skill |
| ---: | --- | --- |
| 1 | [LLM Product Fundamentals](./01_llm_product_fundamentals.md) | Explain tokens, context, embeddings, prompting, tools, and adaptation choices |
| 2 | [RAG Systems](./02_rag_systems.md) | Design authorized ingestion, retrieval, generation, citations, and evaluation |
| 3 | [Model Delivery and Evaluation](./03_model_delivery_and_evaluation.md) | Ship versions safely and monitor quality, drift, latency, reliability, and cost |

Then apply the material to [Design an Image-Generation Platform](../system_design/image_generation_platform.md).

## The Product Decision Map

| Need | Start With | Why |
| --- | --- | --- |
| Clearer instructions or output shape | Prompt and validation | Fastest, cheapest change with no model training |
| Current private knowledge with sources | Retrieval-augmented generation | Fetches changing evidence at request time |
| Stable repeated behavior or style | Fine-tuning after evaluation | Changes learned behavior when examples justify the cost |
| Current facts plus specialized behavior | Retrieval plus optional fine-tuning | Knowledge and behavior are separate problems |
| Exact deterministic rule | Normal code or database query | A probabilistic model adds unnecessary risk |
| External action | Tool call behind authorization and validation | The application, not free-form text, controls side effects |

Do not begin with the most advanced method. Begin with the smallest method that
can be evaluated against the customer outcome.

## Beginner Vocabulary

| Term | Plain-English Meaning |
| --- | --- |
| Token | A piece of text processed by a language model |
| Context window | Maximum token budget available to one request and response |
| Embedding | A numeric representation used to compare semantic similarity |
| Inference | Running a trained model to produce an output |
| Prompt | Instructions and input sent to a model |
| Tool call | Structured request from a model for application-controlled code to act |
| RAG | Retrieve relevant evidence, then generate using that evidence |
| Fine-tuning | Continue training a model on selected examples to change behavior |
| Grounding | Connecting an answer to supplied evidence or a trusted system |
| Hallucination | Fluent output that is unsupported or incorrect |
| Offline evaluation | Test a version on a saved, labeled set before serving users |
| Online evaluation | Measure behavior and outcomes in real product traffic |
| Shadow | Run a new version on copied traffic without showing its output |
| Canary | Show a new version to a small controlled share of real traffic |
| Drift | Production data or behavior changes relative to a reference period |

## Recommended Study Method

1. Explain every vocabulary term without using another undefined AI term.
2. Turn one customer request into a baseline, prompt, retrieval, and fine-tuning option.
3. Draw the ingestion and query paths of a RAG system separately.
4. Define a small evaluation set before choosing a model.
5. Practice one model rollout and one quality incident aloud.
6. Complete all transfer questions before reading their answers.
7. Record a system or AI mock in the [progress tracker](../PROGRESS_TRACKER.md).

## Ready to Move On

You are ready when you can:

- explain what a model predicts and what the surrounding application must own,
- estimate token, latency, throughput, storage, and unit-cost budgets,
- choose among code, prompting, RAG, tools, and fine-tuning with tradeoffs,
- design tenant-safe retrieval with citations and deletion,
- separate retrieval failure from generation failure,
- define offline sets, online outcomes, and safety guardrails,
- release a model through versioning, shadowing, canary, and rollback,
- diagnose data, model, application, infrastructure, and measurement failures,
- say what happens when the model or a dependency is slow, wrong, or unavailable.
