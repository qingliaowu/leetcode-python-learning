# Stacks and Queues for Beginners

[Repository home](../README.md) | [Study plans](../INTERVIEW_STUDY_PLANS.md) | [Interview playbook](../INTERVIEW_PLAYBOOK.md) | [Progress tracker](../PROGRESS_TRACKER.md) | [System design](../system_design/README.md) | [FDE track](../fde_interview/README.md) | [AI engineering](../ai_engineering/README.md)

A stack removes the most recently added item first. A queue removes the earliest added item first.

```text
stack: last in, first out
queue: first in, first out
```

Use the [Python 3 Basics course](../python_basics/) if lists or loops feel unfamiliar. The [complexity guide](../python_basics/11_time_and_space_complexity.md) explains stack memory, and the [Interview Playbook](../INTERVIEW_PLAYBOOK.md) helps with solve-aloud practice.

## Recommended Order

| LeetCode | Lesson | Python Solution | Main Pattern |
| ---: | --- | --- | --- |
| 394 | [Decode String](./0394_decode_string.md) | [Code](./0394_decode_string.py) | Stack of paused outer strings and repeat counts |
| 739 | [Daily Temperatures](./0739_daily_temperatures.md) | [Code](./0739_daily_temperatures.py) | Monotonic stack of unresolved indexes |

## Recognize a Stack Problem

Consider a stack when:

- brackets or parentheses are nested,
- the latest unfinished work must resume first,
- the next greater or smaller item resolves previous unanswered items,
- you need undo behavior,
- you are doing iterative depth-first search.

Python uses a list as a stack:

```python
stack = []
stack.append(item)  # push
item = stack.pop()  # remove the most recent item
```

## Ready to Move On

You are ready when you can explain why nested work closes in last-in-first-out order, maintain a monotonic unresolved stack, and count why every item is pushed and popped at most once. Continue to [Linked Lists](../linked_lists/README.md).
