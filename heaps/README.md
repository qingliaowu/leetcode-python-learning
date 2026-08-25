# Heaps and Top-K

[Repository home](../README.md) | [Study plans](../INTERVIEW_STUDY_PLANS.md) | [Interview playbook](../INTERVIEW_PLAYBOOK.md) | [Pattern map](../ALGORITHM_PATTERN_MAP.md) | [Progress tracker](../PROGRESS_TRACKER.md) | [System design](../system_design/README.md) | [FDE track](../fde_interview/README.md) | [AI engineering](../ai_engineering/README.md)

These medium-priority problems use a heap when only the smallest, largest, or next available item matters. Python's `heapq` module implements a min-heap.

Use the [interview playbook](../INTERVIEW_PLAYBOOK.md) for the solve-out-loud process. Review the [Python 3 Basics course](../python_basics/) when needed. The course includes a plain-English [time and space complexity lesson](../python_basics/11_time_and_space_complexity.md).

## Recommended Order

| LeetCode | Lesson | Python Solution | Main Pattern |
| ---: | --- | --- | --- |
| 215 | [Kth Largest Element](./0215_kth_largest_element.md) | [Code](./0215_kth_largest_element.py) | Min-heap of size `k` |
| 347 | [Top K Frequent Elements](./0347_top_k_frequent_elements.md) | [Code](./0347_top_k_frequent_elements.py) | Frequency map plus heap |
| 23 | [Merge K Sorted Lists](./0023_merge_k_sorted_lists.md) | [Code](./0023_merge_k_sorted_lists.py) | Heap-based multiway merge |

## Recognize the Pattern

Use a heap when you repeatedly need the smallest available item, only the best `K` items, or one current candidate from each sorted source. State exactly what belongs in the heap and why everything else can be ignored.

## Python Heap Reminder

```python
import heapq

heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 2)
smallest = heapq.heappop(heap)  # 2
```

The smallest item is always at `heap[0]`. Push and pop each take `O(log K)` time for a heap containing `K` items.

## Ready to Move On

You are ready when you can explain the heap invariant, include a safe tuple tie-breaker, and derive `O(N log K)` from the number of pushes and pops. Continue to [Prefix Sums and Backtracking](../prefix_recursion/README.md).
