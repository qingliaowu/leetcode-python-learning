# 215. Kth Largest Element in an Array

[LeetCode problem](https://leetcode.com/problems/kth-largest-element-in-an-array/) | [Python solution](./0215_kth_largest_element.py)

## What the Question Asks

Return the value that would appear in position `k` if the values were sorted from largest to smallest. Duplicates count as separate positions.

```text
nums = [3, 2, 1, 5, 6, 4], k = 2
descending = [6, 5, 4, 3, 2, 1]
answer = 5
```

## Python Used Here

Python's `heapq` is a min-heap:

```python
import heapq

heapq.heappush(min_heap, number)
smallest = heapq.heappop(min_heap)
```

The smallest stored value is always available at `min_heap[0]`. The list itself is not fully sorted, so only rely on its first item.

## Main Idea

Keep only the `k` largest values seen so far in a min-heap.

After pushing a number, if the heap has more than `k` items, remove its smallest value. That removed value cannot be among the overall `k` largest values seen so far.

At the end:

- the heap contains exactly the `k` largest array elements,
- the smallest among them is at index `0`, and
- that smallest is the kth largest overall.

This maintained truth is called an invariant.

## Dry Run

For `[3, 2, 1, 5, 6, 4]`, `k = 2`:

| Read | Heap after limiting to size 2 | Meaning |
| ---: | --- | --- |
| 3 | `[3]` | Top values so far |
| 2 | `[2,3]` | Top two so far |
| 1 | `[2,3]` | Push 1, then remove 1 |
| 5 | `[3,5]` | Push 5, then remove 2 |
| 6 | `[5,6]` | Push 6, then remove 3 |
| 4 | `[5,6]` | Push 4, then remove 4 |

`heap[0]` is `5`, the second largest.

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

- Each of `N` numbers performs a heap push and possibly a pop, each `O(log K)`.
- Time: `O(N log K)`.
- Space: `O(K)`.

Sorting the whole array is simpler but costs `O(N log N)` time.

## Common Mistakes

- Building a size-`k` max-heap when a min-heap naturally exposes the boundary value.
- Returning the largest heap value instead of `heap[0]`.
- Removing values when heap size is `k` instead of greater than `k`.
- Removing duplicate values as though only distinct values counted.
- Assuming the internal heap list is completely sorted.

## Interview Explanation

> I maintain a min-heap containing the largest `k` values seen. Whenever its size exceeds `k`, I remove the smallest. At the end, the heap's minimum is the kth largest overall. This uses `O(N log K)` time and `O(K)` space.
