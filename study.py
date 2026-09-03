"""Small command-line study coach for this repository.

The goal is to turn the repo into something you can use every day:

    python3 study.py next --track sierra
    python3 study.py mock --kind coding --seed 1
    python3 study.py scorecard --kind system
    python3 study.py plan
"""

from __future__ import annotations

import argparse
import random
from dataclasses import dataclass
from pathlib import Path
from textwrap import wrap


ROOT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class StudyTask:
    priority: str
    title: str
    minutes: int
    file_path: str
    outcome: str


@dataclass(frozen=True)
class MockPrompt:
    title: str
    timebox: str
    prompt: str
    deliverables: tuple[str, ...]
    follow_ups: tuple[str, ...]
    source_file: str


CORE_TASKS = (
    StudyTask(
        "High",
        "Python dicts and sets refresher",
        25,
        "python_basics/05_dictionaries_and_sets.md",
        "Explain when to use a dict, set, list, tuple, and Counter.",
    ),
    StudyTask(
        "High",
        "Two Sum",
        30,
        "arrays_strings/0001_two_sum.md",
        "Solve with a complement map and explain the invariant.",
    ),
    StudyTask(
        "High",
        "Group Anagrams",
        35,
        "arrays_strings/0049_group_anagrams.md",
        "Choose a stable grouping key and handle empty strings.",
    ),
    StudyTask(
        "High",
        "Longest Substring Without Repeating Characters",
        40,
        "arrays_strings/0003_longest_substring_without_repeating_characters.md",
        "Use a sliding window and update the left boundary safely.",
    ),
    StudyTask(
        "High",
        "LRU Cache",
        45,
        "design_data_structures/0146_lru_cache.md",
        "Explain O(1) get/put and why order must be updated on access.",
    ),
)


FDE_TASKS = (
    StudyTask(
        "High",
        "Filter Duplicates",
        20,
        "fde_interview/08_high_priority_practical_coding_questions.md",
        "Solve without running code; preserve first-seen order.",
    ),
    StudyTask(
        "High",
        "Count Word Frequencies",
        20,
        "fde_interview/08_high_priority_practical_coding_questions.md",
        "Count with a dictionary and return counts in sorted word order.",
    ),
    StudyTask(
        "High",
        "Merge Person Data",
        35,
        "fde_interview/08_high_priority_practical_coding_questions.md",
        "Parse, group, merge, sort, and format deterministic output.",
    ),
    StudyTask(
        "High",
        "Customer discovery drill",
        30,
        "fde_interview/02_customer_discovery_and_solutioning.md",
        "Turn a vague customer problem into requirements and acceptance tests.",
    ),
    StudyTask(
        "High",
        "Enterprise AI adoption case",
        45,
        "fde_interview/05_enterprise_ai_adoption.md",
        "Connect workflow, architecture, rollout, ownership, metrics, and cost.",
    ),
)


GOOGLE_TASKS = (
    StudyTask(
        "Critical",
        "Hash map and sliding-window core",
        75,
        "GOOGLE_SIERRA_INTERVIEW_MASTERY.md",
        "Solve Two Sum, Group Anagrams, or Longest Substring with a full dry run.",
    ),
    StudyTask(
        "Critical",
        "Binary search and intervals",
        60,
        "GOOGLE_SIERRA_INTERVIEW_MASTERY.md",
        "Practice the monotonic condition, sorted invariant, and boundary updates.",
    ),
    StudyTask(
        "Critical",
        "Trees and graphs",
        75,
        "GOOGLE_SIERRA_INTERVIEW_MASTERY.md",
        "Solve BFS/DFS/topological sorting and explain visited state clearly.",
    ),
    StudyTask(
        "High",
        "Heaps, top-k, and stateful data structures",
        60,
        "GOOGLE_SIERRA_INTERVIEW_MASTERY.md",
        "Explain operation guarantees and why the chosen structure fits.",
    ),
    StudyTask(
        "High",
        "Dynamic programming",
        50,
        "dynamic_programming/README.md",
        "State the recurrence, base cases, iteration order, and complexity.",
    ),
    StudyTask(
        "High",
        "Distributed system design",
        45,
        "system_design/README.md",
        "Cover requirements, estimates, APIs, storage, caching, queues, failures.",
    ),
    StudyTask(
        "Medium",
        "Behavioral and leadership stories",
        30,
        "fde_interview/04_behavioral_story_workbook.md",
        "Prepare concise stories for ownership, conflict, failure, and learning.",
    ),
)


SIERRA_TASKS = (
    StudyTask(
        "Critical",
        "Three practical coding drills",
        75,
        "fde_interview/08_high_priority_practical_coding_questions.md",
        "Finish all three with example, edge cases, implementation, trace, tests.",
    ),
    StudyTask(
        "Critical",
        "API client with retry",
        45,
        "fde_interview/09_sierra_ai_agent_interview_mastery.md",
        "Handle timeout, 429, 5xx, backoff, jitter, and idempotency.",
    ),
    StudyTask(
        "Critical",
        "Nested JSON flatten or traversal",
        40,
        "fde_interview/09_sierra_ai_agent_interview_mastery.md",
        "Use recursion or a stack with clear path-building and type handling.",
    ),
    StudyTask(
        "High",
        "Connected components or dependency graph",
        45,
        "trees_graphs/0207_course_schedule.md",
        "Build adjacency, track visited state, and explain cycles.",
    ),
    StudyTask(
        "Critical",
        "Customer-service AI agent system design",
        45,
        "fde_interview/09_sierra_ai_agent_interview_mastery.md",
        "Cover state, tools, auth, context, safety, evaluation, handoff, latency.",
    ),
    StudyTask(
        "High",
        "Multilingual voice agent design",
        45,
        "fde_interview/09_sierra_ai_agent_interview_mastery.md",
        "Separate ASR, turn-taking, tool latency, TTS, and task-success metrics.",
    ),
    StudyTask(
        "High",
        "Plan-Build-Review rehearsal",
        120,
        "fde_interview/09_sierra_ai_agent_interview_mastery.md",
        "Scope a tiny product, build it, demo it, and critique production gaps.",
    ),
    StudyTask(
        "Medium",
        "Behavioral story pass",
        30,
        "fde_interview/04_behavioral_story_workbook.md",
        "Prepare concise stories for ambiguity, incident, ownership, and learning.",
    ),
)


GOOGLE_SIERRA_TASKS = (
    StudyTask(
        "Critical",
        "Read the combined mastery map",
        20,
        "GOOGLE_SIERRA_INTERVIEW_MASTERY.md",
        "Understand which skills overlap and which company-specific spikes remain.",
    ),
    StudyTask(
        "Critical",
        "Google coding core",
        75,
        "GOOGLE_SIERRA_INTERVIEW_MASTERY.md",
        "Solve one hash/sliding-window/binary-search problem with full explanation.",
    ),
    StudyTask(
        "Critical",
        "Graph or trie strength",
        60,
        "GOOGLE_SIERRA_INTERVIEW_MASTERY.md",
        "Solve one traversal or prefix-structure prompt and prove correctness.",
    ),
    StudyTask(
        "Critical",
        "Sierra practical implementation",
        60,
        "fde_interview/08_high_priority_practical_coding_questions.md",
        "Solve one practical parser/dict/set prompt without AI or compiler help.",
    ),
    StudyTask(
        "High",
        "System design fundamentals",
        45,
        "system_design/foundational_patterns.md",
        "Practice requirements, estimates, APIs, data model, cache, queue, failure.",
    ),
    StudyTask(
        "High",
        "AI agent and voice design",
        45,
        "fde_interview/09_sierra_ai_agent_interview_mastery.md",
        "Design tool use, context, evals, guardrails, handoff, and voice latency.",
    ),
    StudyTask(
        "High",
        "Plan-Build-Review rehearsal",
        120,
        "fde_interview/09_sierra_ai_agent_interview_mastery.md",
        "Build a small usable workflow, then review tests and production gaps.",
    ),
    StudyTask(
        "Medium",
        "Behavioral repair pass",
        30,
        "fde_interview/04_behavioral_story_workbook.md",
        "Tell six two-minute stories: ownership, ambiguity, conflict, failure, impact, learning.",
    ),
)


CODING_PROMPTS = (
    MockPrompt(
        "Google-Style Grid Traversal",
        "45 minutes",
        (
            "Given a grid of 0s and 1s, return the size of the largest connected "
            "component of 1s. Cells connect up, down, left, and right."
        ),
        (
            "Clarify empty grid behavior and whether diagonal cells connect.",
            "Use DFS or BFS with a visited set or in-place marking.",
            "Track component size correctly.",
            "Explain O(rows * cols) time and space.",
        ),
        (
            "Return all component sizes in sorted order.",
            "Treat the grid as immutable.",
            "Support blocked cells with value -1.",
        ),
        "trees_graphs/0200_number_of_islands.md",
    ),
    MockPrompt(
        "Google-Style Binary Search on Answer",
        "45 minutes",
        (
            "Given job durations and k workers, return the minimum possible maximum "
            "worker load if jobs must stay in input order."
        ),
        (
            "Identify the monotonic feasibility condition.",
            "Set correct low and high bounds.",
            "Write a helper that counts required workers.",
            "Explain why binary search finds the minimum valid answer.",
        ),
        (
            "Return one valid partition.",
            "Handle k greater than the number of jobs.",
            "Discuss what changes if jobs can be reordered.",
        ),
        "intervals_search/0875_koko_eating_bananas.md",
    ),
    MockPrompt(
        "Google-Style Dynamic Programming",
        "45 minutes",
        (
            "Given a list of non-negative rewards, choose rewards with no adjacent "
            "indices to maximize total value."
        ),
        (
            "Define dp[i] in plain English.",
            "State base cases before coding.",
            "Optimize to O(1) extra space after the clear version.",
            "Dry-run an example with adjacent high values.",
        ),
        (
            "Return the chosen indices.",
            "Make the list circular.",
            "Handle negative values if the business rule allows skipping all items.",
        ),
        "dynamic_programming/0198_house_robber.md",
    ),
    MockPrompt(
        "Accept-Language Parser",
        "40 minutes",
        (
            "Implement choose_language(header, supported) -> str | None. Parse an "
            "HTTP Accept-Language header and return the best supported language."
        ),
        (
            "Ask how exact language tags and base languages should match.",
            "Handle q values, missing q values, unsupported languages, and empty input.",
            "Explain why sorting or incremental best tracking is correct.",
            "Add manual tests before running anything.",
        ),
        (
            "Support wildcards.",
            "Ignore malformed q values instead of crashing.",
            "Prefer exact match over base-language match.",
        ),
        "fde_interview/09_sierra_ai_agent_interview_mastery.md",
    ),
    MockPrompt(
        "API Client With Retry",
        "45 minutes",
        (
            "Implement fetch_with_retry(call, max_retries, base_delay). The call "
            "function may return a response object or raise a timeout/error."
        ),
        (
            "Separate retryable and non-retryable failures.",
            "Stop after the maximum retry count.",
            "Use exponential backoff and explain jitter.",
            "State when idempotency keys are required.",
        ),
        (
            "Retry HTTP 429 and 5xx only.",
            "Return partial diagnostic information after final failure.",
            "Add a timeout budget for the whole request.",
        ),
        "fde_interview/09_sierra_ai_agent_interview_mastery.md",
    ),
    MockPrompt(
        "Merge Person Data",
        "35 minutes",
        (
            "Implement merge_data(data_strings). Each string contains semicolon "
            "separated Key=Value fields and each record has Name."
        ),
        (
            "Parse records without losing values that contain spaces.",
            "Group by Name.",
            "Merge fields and output Name first, then other keys alphabetically.",
            "Sort people by Name.",
        ),
        (
            "Handle duplicate repeated fields.",
            "Preserve values that contain printable ASCII characters.",
            "Discuss what to do if contradictory records appear.",
        ),
        "fde_interview/08_high_priority_practical_coding_questions.md",
    ),
    MockPrompt(
        "Nested JSON Flatten",
        "40 minutes",
        (
            "Implement flatten_json(obj) -> dict[str, object]. Convert nested "
            "dictionaries into dotted paths."
        ),
        (
            "Define behavior for empty dictionaries.",
            "Handle scalar values.",
            "Explain recursion depth and stack tradeoffs.",
            "Test a normal case, an empty object, and mixed types.",
        ),
        (
            "Support lists with numeric path segments.",
            "Allow a custom separator.",
            "Stop at max_depth and leave the remaining object unflattened.",
        ),
        "fde_interview/09_sierra_ai_agent_interview_mastery.md",
    ),
    MockPrompt(
        "Dependency Graph",
        "45 minutes",
        (
            "Implement deployment_order(services, dependencies) -> list[str]. "
            "Return a valid build order or raise an error for a cycle."
        ),
        (
            "Build adjacency and indegree maps.",
            "Include services with no dependencies.",
            "Detect cycles.",
            "Explain why topological sorting fits.",
        ),
        (
            "Return all blocked services when a cycle exists.",
            "Make output deterministic.",
            "Support dependencies that mention missing services.",
        ),
        "trees_graphs/0207_course_schedule.md",
    ),
)


SYSTEM_PROMPTS = (
    MockPrompt(
        "Google-Style Global File Metadata Service",
        "45 minutes",
        (
            "Design a service that stores file metadata, supports lookups by ID, "
            "updates sharing permissions, and serves global traffic reliably."
        ),
        (
            "Clarify users, objects, permissions, read/write ratio, and consistency needs.",
            "Define APIs, metadata schema, indexes, cache, storage, and replication.",
            "Deep-dive on consistency for permission changes.",
            "Cover monitoring, abuse prevention, migration, and disaster recovery.",
        ),
        (
            "Support search by owner and filename prefix.",
            "Make permission revocation take effect quickly.",
            "Handle a regional outage.",
        ),
        "system_design/foundational_patterns.md",
    ),
    MockPrompt(
        "Customer-Service AI Agent",
        "45 minutes",
        (
            "Design a production AI agent for a large enterprise. It supports chat, "
            "calls CRM/billing/order tools, answers policy questions, and hands off "
            "to humans when needed."
        ),
        (
            "Clarify tenant, channels, workflows, latency, compliance, and success metrics.",
            "Draw the request flow from user to orchestrator to tools to response.",
            "Deep-dive on state, permissions, retrieval, validation, and handoff.",
            "Define evals, traces, alerts, rollout gates, and failure handling.",
        ),
        (
            "Add voice support.",
            "Reduce P95 latency by half.",
            "Handle a tool outage without unsafe answers.",
        ),
        "fde_interview/09_sierra_ai_agent_interview_mastery.md",
    ),
    MockPrompt(
        "Multilingual Voice Agent",
        "45 minutes",
        (
            "Design a voice agent for customer support in 20 languages. It must "
            "understand noisy calls, use account context, and complete tasks safely."
        ),
        (
            "Separate ASR, endpointing, orchestration, tools, TTS, and logging.",
            "Create a latency budget for the full voice turn.",
            "Discuss language switching, names, domain vocabulary, and recovery.",
            "Measure ASR accuracy, task success, escalation, and user experience.",
        ),
        (
            "Support barge-in.",
            "Handle ambiguous customer names.",
            "Route low-confidence turns to clarification or a human.",
        ),
        "fde_interview/09_sierra_ai_agent_interview_mastery.md",
    ),
    MockPrompt(
        "Agent Evaluation Platform",
        "45 minutes",
        (
            "Design an evaluation system for AI agents before and after release. "
            "It should detect regressions in task completion, safety, tool usage, "
            "and customer experience."
        ),
        (
            "Define offline test sets, simulations, and online metrics.",
            "Version prompts, tools, policies, models, and datasets.",
            "Tie traces to failures and rollout decisions.",
            "Explain rollback, canarying, and owner workflows.",
        ),
        (
            "Add voice-specific evaluation.",
            "Compare two model versions.",
            "Handle sparse human labels.",
        ),
        "ai_engineering/03_model_delivery_and_evaluation.md",
    ),
    MockPrompt(
        "Context Engineering Layer",
        "45 minutes",
        (
            "Design a context engineering layer that gives an agent the right "
            "journeys, policies, tools, memory, and knowledge at the right time."
        ),
        (
            "Define context blocks and activation conditions.",
            "Control tenant isolation, stale data, and permission boundaries.",
            "Handle progressive disclosure and token budget pressure.",
            "Log why context was selected for audit and debugging.",
        ),
        (
            "Add per-customer customization.",
            "Handle conflicting policies.",
            "Reduce hallucination without doubling latency.",
        ),
        "fde_interview/09_sierra_ai_agent_interview_mastery.md",
    ),
)


BUILD_PROMPTS = (
    MockPrompt(
        "Support Agent Review Console",
        "2 hours",
        (
            "Build a small local tool that loads customer messages, labels intent, "
            "shows suggested tool calls, and lets a reviewer approve or reject them."
        ),
        (
            "Spend 15 minutes writing scope and acceptance tests.",
            "Build the smallest useful workflow.",
            "Include sample data and at least one failure state.",
            "Prepare a review explaining production gaps.",
        ),
        (
            "Add tenant-specific policy rules.",
            "Add audit log output.",
            "Explain what AI-generated code you manually verified.",
        ),
        "fde_interview/09_sierra_ai_agent_interview_mastery.md",
    ),
    MockPrompt(
        "Voice Transcript Debugger",
        "2 hours",
        (
            "Build a local tool that compares a voice transcript, expected task, "
            "agent answer, and tool-call trace to classify the failure."
        ),
        (
            "Define a small failure taxonomy.",
            "Support at least five sample conversations.",
            "Show task success and latency fields.",
            "Prepare a demo and code review.",
        ),
        (
            "Add multilingual examples.",
            "Add a confidence score.",
            "Explain how this would become a production eval pipeline.",
        ),
        "fde_interview/09_sierra_ai_agent_interview_mastery.md",
    ),
)


SEVEN_DAY_PLAN = (
    ("Day 1", "Practical Python: sets, dicts, strings, sorted output."),
    ("Day 2", "Parsing and follow-ups: person data, logs, nested JSON."),
    ("Day 3", "APIs: retries, timeouts, pagination, idempotency."),
    ("Day 4", "System design: customer-service AI agent."),
    ("Day 5", "Voice agent: ASR, turn-taking, latency, evaluation."),
    ("Day 6", "Plan-Build-Review: build a tiny agent workflow tool."),
    ("Day 7", "Full mock: coding, system design, behavioral review."),
)


SCORECARDS = {
    "coding": (
        "Clarifies input, output, constraints, and edge cases before coding.",
        "States the simplest correct approach before optimizing.",
        "Uses the right Python data structures deliberately.",
        "Keeps state names clear enough to explain aloud.",
        "Handles empty, single-item, duplicate, malformed, and boundary inputs.",
        "Dry-runs a normal example and one edge case.",
        "Explains time and space complexity in complete sentences.",
        "Handles one follow-up without rewriting from scratch.",
    ),
    "system": (
        "Clarifies customer, workflow, scale, latency, compliance, and success metrics.",
        "Defines APIs, state, data model, and normal request flow.",
        "Separates orchestration, retrieval, tools, policy, validation, and handoff.",
        "Covers auth, tenant isolation, PII, audit, and permission boundaries.",
        "Handles retries, idempotency, dependency failure, and fallback.",
        "Defines observability, offline evals, online metrics, and rollout gates.",
        "Deep-dives on the hardest tradeoff instead of staying too high-level.",
        "Adapts when one assumption changes.",
    ),
    "build": (
        "Scopes a small product with a crisp user workflow.",
        "Builds a usable first version within the timebox.",
        "Includes sample data, tests, and at least one failure state.",
        "Keeps code readable enough to review under pressure.",
        "Explains data model and abstractions.",
        "Names what AI helped with and what was manually verified.",
        "Describes path to production: security, scale, evals, deploy, ownership.",
        "Responds calmly to critique and proposes next changes.",
    ),
    "behavioral": (
        "Uses a real story with context, action, result, and learning.",
        "Explains tradeoffs without blaming other people.",
        "Shows customer impact and engineering judgment.",
        "Names one specific mistake or uncertainty.",
        "Keeps the story under two minutes.",
        "Connects the story back to the role.",
    ),
}


TRACKS = {
    "core": CORE_TASKS,
    "fde": FDE_TASKS,
    "google": GOOGLE_TASKS,
    "google_sierra": GOOGLE_SIERRA_TASKS,
    "sierra": SIERRA_TASKS,
    "all": SIERRA_TASKS + FDE_TASKS + CORE_TASKS,
}


PROMPTS = {
    "coding": CODING_PROMPTS,
    "system": SYSTEM_PROMPTS,
    "build": BUILD_PROMPTS,
}


def absolute(relative_path: str) -> Path:
    """Return a stable absolute path for files in this repository."""
    return ROOT / relative_path


def print_wrapped(text: str, indent: str = "") -> None:
    """Print readable terminal text without needing external packages."""
    for line in wrap(text, width=88, subsequent_indent=indent, initial_indent=indent):
        print(line)


def print_list(items: tuple[str, ...]) -> None:
    for item in items:
        print_wrapped(f"- {item}", indent="")


def command_next(args: argparse.Namespace) -> None:
    tasks = TRACKS[args.track]
    print(f"Next study queue: {args.track}")
    print("=" * 28)
    for index, task in enumerate(tasks[: args.limit], start=1):
        print(f"{index}. [{task.priority}] {task.title} ({task.minutes} min)")
        print(f"   File: {absolute(task.file_path)}")
        print_wrapped(f"Goal: {task.outcome}", indent="   ")
        print()


def choose_prompt(kind: str, seed: int | None, index: int | None) -> MockPrompt:
    prompts = PROMPTS[kind]
    if index is not None:
        if not 1 <= index <= len(prompts):
            raise SystemExit(f"--index must be between 1 and {len(prompts)}")
        return prompts[index - 1]

    chooser = random.Random(seed)
    return chooser.choice(prompts)


def command_mock(args: argparse.Namespace) -> None:
    prompt = choose_prompt(args.kind, args.seed, args.index)
    print(f"Mock interview: {prompt.title}")
    print("=" * 32)
    print(f"Timebox: {prompt.timebox}")
    print(f"Source: {absolute(prompt.source_file)}")
    print()
    print("Prompt")
    print("-" * 6)
    print_wrapped(prompt.prompt)
    print()
    print("Deliverables")
    print("-" * 12)
    print_list(prompt.deliverables)
    print()
    print("Follow-ups")
    print("-" * 10)
    print_list(prompt.follow_ups)
    print()
    print("Afterward")
    print("-" * 9)
    print_wrapped(
        "Score yourself with `python3 study.py scorecard --kind "
        f"{args.kind}` and record the result in PROGRESS_TRACKER.md."
    )


def command_plan(_: argparse.Namespace) -> None:
    print("Seven-day Sierra mastery plan")
    print("=" * 31)
    for day, focus in SEVEN_DAY_PLAN:
        print(f"{day}: {focus}")
    print()
    print("Daily rule: Example -> Edge cases -> Implementation -> Manual trace -> Tests.")
    print("Use `python3 study.py next --track sierra` to choose the next block.")


def command_scorecard(args: argparse.Namespace) -> None:
    checks = SCORECARDS[args.kind]
    print(f"{args.kind.title()} scorecard")
    print("=" * (len(args.kind) + 10))
    for index, check in enumerate(checks, start=1):
        print(f"{index}. {check}")
    print()
    print("Scoring: 0 = absent, 1 = weak, 2 = acceptable, 3 = strong.")


def command_links(args: argparse.Namespace) -> None:
    print(f"Useful files for track: {args.track}")
    print("=" * 30)
    seen = set()
    for task in TRACKS[args.track]:
        if task.file_path in seen:
            continue
        seen.add(task.file_path)
        print(absolute(task.file_path))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Pick focused study tasks, mock prompts, and scorecards."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    next_parser = subparsers.add_parser("next", help="Show the next study queue.")
    next_parser.add_argument(
        "--track",
        choices=sorted(TRACKS),
        default="sierra",
        help="Curriculum focus. Default: sierra.",
    )
    next_parser.add_argument(
        "--limit",
        type=int,
        default=8,
        help="Number of tasks to show. Default: 8.",
    )
    next_parser.set_defaults(func=command_next)

    mock_parser = subparsers.add_parser("mock", help="Generate a mock prompt.")
    mock_parser.add_argument(
        "--kind",
        choices=sorted(PROMPTS),
        default="coding",
        help="Mock type. Default: coding.",
    )
    mock_parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Optional seed for repeatable random selection.",
    )
    mock_parser.add_argument(
        "--index",
        type=int,
        default=None,
        help="Optional 1-based prompt number for deterministic selection.",
    )
    mock_parser.set_defaults(func=command_mock)

    plan_parser = subparsers.add_parser("plan", help="Show the Sierra 7-day plan.")
    plan_parser.set_defaults(func=command_plan)

    scorecard_parser = subparsers.add_parser(
        "scorecard",
        help="Show a self-grading checklist.",
    )
    scorecard_parser.add_argument(
        "--kind",
        choices=sorted(SCORECARDS),
        default="coding",
        help="Scorecard type. Default: coding.",
    )
    scorecard_parser.set_defaults(func=command_scorecard)

    links_parser = subparsers.add_parser("links", help="Show key files for a track.")
    links_parser.add_argument(
        "--track",
        choices=sorted(TRACKS),
        default="sierra",
        help="Curriculum focus. Default: sierra.",
    )
    links_parser.set_defaults(func=command_links)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
