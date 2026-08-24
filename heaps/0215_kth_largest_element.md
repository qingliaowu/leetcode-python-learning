# 215. Kth Largest Element in an Array

[LeetCode problem](https://leetcode.com/problems/kth-largest-element-in-an-array/) | [Python solution](./0215_kth_largest_element.py) | [Topic guide](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

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

## Possible Follow-up Questions

| Follow-up | Answer Direction |
| --- | --- |
| Can you achieve `O(N)` average time? | Use Quickselect to partition around a pivot and continue only in the section containing the target rank. |
| Values arrive as a stream. | Keep the same size-`K` min-heap; after each arrival, `heap[0]` is the kth largest seen when at least `K` values exist. |
| Find the kth smallest instead. | Keep a size-`K` max-heap, or Quickselect index `k - 1` in ascending order. Python can simulate a max-heap with negative values. |
| Support deletions as well as insertions. | A plain heap cannot delete arbitrary values efficiently; use lazy deletion with counts or an ordered multiset. |
| What if `K` is close to `N`? | A heap of the smaller side or Quickselect may be preferable; explain the time-space tradeoff. |

## Interview Explanation

> I maintain a min-heap containing the largest `k` values seen. Whenever its size exceeds `k`, I remove the smallest. At the end, the heap's minimum is the kth largest overall. This uses `O(N log K)` time and `O(K)` space.

## Check Your Understanding

Try each question before opening its answer. Remember that duplicates occupy separate ranks.

### Question 1: Keep the Largest Four

What is the fourth largest value in `[3, 2, 3, 1, 2, 4, 5, 5, 6]`? Which four values remain in a size-`4` min-heap?

<details>
<summary>Show answer and explanation</summary>

**Answer:** The fourth largest value is `4`. The retained values are `4`, `5`, `5`, and `6`.

Duplicates count as separate elements, so descending order begins `6, 5, 5, 4`. The heap does not have to store these values in fully sorted list order. It guarantees only that its smallest retained value, `heap[0]`, is at the root.

Whenever a fifth value enters, removing the smallest restores the invariant: the heap contains the largest four values seen so far.

**Complexity:** `O(N log K)` time and `O(K)` extra space.

**Edge case:** Valid input requires `1 <= k <= len(nums)`.

</details>

### Question 2: Kth Largest in a Stream

Build a class for a positive integer `k` that receives numbers one at a time. After at least `k` values have been seen, `add` returns the current kth largest value; otherwise it returns `None`.

<details>
<summary>Show answer and detailed solution</summary>

```python
import heapq


class KthLargestStream:
    def __init__(self, k: int):
        self.k = k
        self.heap: list[int] = []

    def add(self, value: int) -> int | None:
        heapq.heappush(self.heap, value)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        if len(self.heap) < self.k:
            return None
        return self.heap[0]
```

The class never needs values below the largest `k` seen so far. Once the heap has `k` items, its root is the boundary between retained and discarded values, which is exactly the kth largest.

Each new value causes one push and at most one pop.

**Complexity:** `O(log K)` time per `add` and `O(K)` space.

**Test:** With `k = 3`, adding `4, 1, 7, 5` returns `None, None, 1, 4`.

</details>
