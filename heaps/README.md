# Heaps and Top-K

These medium-priority problems use a heap when only the smallest, largest, or next available item matters. Python's `heapq` module implements a min-heap.

Use the [interview playbook](../INTERVIEW_PLAYBOOK.md) for the solve-out-loud process. Review the [Python 3 Basics course](../python_basics/) when needed.

| LeetCode | Lesson | Python Solution | Main Pattern |
| ---: | --- | --- | --- |
| 215 | [Kth Largest Element](./0215_kth_largest_element.md) | [Code](./0215_kth_largest_element.py) | Min-heap of size `k` |
| 347 | [Top K Frequent Elements](./0347_top_k_frequent_elements.md) | [Code](./0347_top_k_frequent_elements.py) | Frequency map plus heap |
| 23 | [Merge K Sorted Lists](./0023_merge_k_sorted_lists.md) | [Code](./0023_merge_k_sorted_lists.py) | Heap-based multiway merge |

## Python Heap Reminder

```python
import heapq

heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 2)
smallest = heapq.heappop(heap)  # 2
```

The smallest item is always at `heap[0]`. Push and pop each take `O(log K)` time for a heap containing `K` items.
