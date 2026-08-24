# Prefix Sums and Backtracking

[Repository home](../README.md) | [Study plans](../INTERVIEW_STUDY_PLANS.md) | [Interview playbook](../INTERVIEW_PLAYBOOK.md) | [Progress tracker](../PROGRESS_TRACKER.md) | [System design](../system_design/README.md)

These medium-priority problems practice two different ways to carry state: a running prefix sum for numeric ranges and recursive backtracking for a board search.

Use the [interview playbook](../INTERVIEW_PLAYBOOK.md) for the solve-out-loud process. Review the [Python 3 Basics course](../python_basics/), especially dictionaries and recursion, before starting. The course includes a plain-English [time and space complexity lesson](../python_basics/11_time_and_space_complexity.md).

## Recommended Order

| LeetCode | Lesson | Python Solution | Main Pattern |
| ---: | --- | --- | --- |
| 560 | [Subarray Sum Equals K](./0560_subarray_sum_equals_k.md) | [Code](./0560_subarray_sum_equals_k.py) | Prefix sum frequency map |
| 79 | [Word Search](./0079_word_search.md) | [Code](./0079_word_search.py) | DFS backtracking |

## Recognize the Pattern

- A prefix sum stores the total from the beginning through the current position.
- Two prefix sums can describe the sum of a continuous subarray.
- Backtracking makes a choice, explores it, and then restores state before trying another choice.

## Ready to Move On

You are ready when you can derive the needed earlier prefix sum and restore every backtracking choice before exploring another branch. Continue to [Trie Interview Practice](../trie/README.md).
