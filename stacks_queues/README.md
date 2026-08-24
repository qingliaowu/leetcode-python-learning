# Stacks and Queues for Beginners

[Repository home](../README.md) | [Study plans](../INTERVIEW_STUDY_PLANS.md) | [Interview playbook](../INTERVIEW_PLAYBOOK.md) | [Progress tracker](../PROGRESS_TRACKER.md)

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

## Recognize a Stack Problem

Consider a stack when:

- brackets or parentheses are nested,
- the latest unfinished work must resume first,
- you need undo behavior,
- you are doing iterative depth-first search.

Python uses a list as a stack:

```python
stack = []
stack.append(item)  # push
item = stack.pop()  # remove the most recent item
```

## Ready to Move On

You are ready when you can explain why nested work closes in last-in-first-out order, trace the stack after every bracket, and test malformed or deeply nested input. Continue to [Intervals, Sorting, and Binary Search](../intervals_search/README.md).
