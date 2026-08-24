# Design Data Structures for Beginners

Design questions ask you to create a class that supports several operations efficiently. The important skill is choosing stored state that makes every required operation fast.

Use the [Python 3 Basics course](../python_basics/) if classes or dictionaries feel unfamiliar. Read the [complexity guide](../python_basics/11_time_and_space_complexity.md) for Big-O help and the [Interview Playbook](../INTERVIEW_PLAYBOOK.md) for solve-aloud practice.

## Recommended Order

| LeetCode | Lesson | Python Solution | Main Design |
| ---: | --- | --- | --- |
| 981 | [Time Based Key-Value Store](./0981_time_based_key_value_store.md) | [Code](./0981_time_based_key_value_store.py) | Hash map of sorted histories plus binary search |
| 146 | [LRU Cache](./0146_lru_cache.md) | [Code](./0146_lru_cache.py) | Hash map plus doubly linked list |

## How to Approach a Design Question

1. Write the exact public operations and return values.
2. State the required time for each operation.
3. Decide what information must be remembered between calls.
4. Choose one data structure for each kind of work.
5. State an invariant that must always remain true.
6. Trace several operations in sequence, especially updates and eviction.

## Invariants in This Folder

TimeMap:

```text
Every key maps to entries stored in increasing timestamp order.
```

LRU Cache:

```text
The dictionary and linked list contain the same real nodes. List order always
runs from least recently used to most recently used.
```

When an operation changes state, check that the invariant is still true before moving on.
