# 23. Merge K Sorted Lists

[LeetCode problem](https://leetcode.com/problems/merge-k-sorted-lists/) | [Python solution](./0023_merge_k_sorted_lists.py) | [Topic guide](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## What the Question Asks

Merge `K` sorted linked lists into one sorted linked list.

```text
1 -> 4 -> 5
1 -> 3 -> 4
2 -> 6

becomes

1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
```

## Linked-List Refresher

Each node stores a value and a reference to the next node:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

Changing `tail.next` connects one node to another. This solution reuses and reconnects the existing input nodes rather than copying every value into new nodes.

LeetCode supplies `ListNode`; this repository includes it so the file runs locally.

## Main Idea

Because every input list is sorted, its first unmerged node is its smallest remaining value. Put one available node from each list in a min-heap.

Repeatedly:

1. Pop the smallest available node.
2. Attach it to the result.
3. Push its next node from the same list.

The heap never needs more than one node from each input list, so its size is at most `K`.

## Python Heap Tuple

The heap stores:

```python
(node.val, list_index, node)
```

Python compares tuples from left to right. The value gives the desired priority. When two values tie, `list_index` breaks the tie so Python never needs to compare `ListNode` objects, which do not define an ordering.

## Dummy Node Pattern

```python
dummy = ListNode()
tail = dummy
```

The dummy node is a temporary node before the real output. It removes the need for special logic when attaching the first result node. `tail` always points to the last output node, and the real head is `dummy.next`.

## Dry Run

For heads `1`, `1`, and `2`:

- Heap initially contains all three heads.
- Pop the first `1`; attach it and push its next value `4`.
- Pop the second `1`; attach it and push its next value `3`.
- Pop `2`; attach it and push `6`.
- Continue until the heap is empty.

At every step, the heap contains the smallest unmerged node from each non-empty list, so its minimum is the smallest remaining node overall.

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

Let `N` be the total number of nodes and `K` the number of lists.

- Every node enters and leaves the heap once.
- Each heap operation costs `O(log K)`.
- Time: `O(N log K)`.
- Extra space: `O(K)` for the heap, excluding the output links.

## Common Mistakes

- Putting all `N` nodes in the heap instead of only one per list.
- Omitting a tie-breaker and causing Python to compare node objects on equal values.
- Forgetting to push the popped node's successor.
- Returning `dummy` instead of `dummy.next`.
- Advancing `tail` incorrectly and losing part of the result.

## Possible Follow-up Questions

| Follow-up | Answer Direction |
| --- | --- |
| Can you solve it without a heap? | Merge lists in pairs using divide and conquer, still taking `O(N log K)` time with `O(log K)` recursive stack space. |
| Inputs are sorted arrays instead of linked lists. | Store `(value, array_index, element_index)` in the heap and push the next index from the popped array. |
| Lists are infinite streams. | Keep one available item per active stream; define blocking, stream completion, and how output is consumed. |
| Must the input nodes remain unchanged? | Create new output nodes instead of reconnecting existing nodes, using `O(N)` additional output-node space. |
| Some input lists are empty or arrive later. | Skip empty heads and define whether later lists may contain values smaller than output already emitted. |

## Interview Explanation

> Each sorted list exposes its smallest remaining node at its head. I keep those at most `K` candidates in a min-heap, pop the smallest into the result, and replace it with its successor. A dummy head simplifies result construction. Every node performs `O(log K)` heap work, for `O(N log K)` total time.

## Check Your Understanding

Try each question before opening its answer. List the one candidate contributed by every non-empty input.

### Question 1: Merge by Heap Order

What sequence is produced by merging `[1, 4]`, `[1, 3]`, and `[2, 6]`? Why does a Python heap entry need a tie-breaker when the first two values are equal?

<details>
<summary>Show answer and explanation</summary>

**Answer:** `[1, 1, 2, 3, 4, 6]`.

Initially the heap exposes `1`, `1`, and `2`, one value from each list. After a value is removed, only its successor from the same list is added. Therefore the heap always contains the smallest not-yet-used candidate from each active list.

Tuples are compared from left to right. If two entries contain the same value and the next tuple item is a `ListNode`, Python may try to compare node objects and raise `TypeError`. A unique integer counter or list index resolves the tie before Python reaches the node.

**Complexity:** `O(N log K)` time and `O(K)` heap space.

**Edge case:** Empty input lists contribute no heap entry.

</details>

### Question 2: Merge Sorted Arrays

Return one sorted list from `K` sorted arrays. Do not place every value in the heap at once.

<details>
<summary>Show answer and detailed solution</summary>

```python
import heapq


def merge_sorted_arrays(arrays: list[list[int]]) -> list[int]:
    heap = []

    for array_index, array in enumerate(arrays):
        if array:
            heapq.heappush(heap, (array[0], array_index, 0))

    merged = []

    while heap:
        value, array_index, element_index = heapq.heappop(heap)
        merged.append(value)

        next_index = element_index + 1
        if next_index < len(arrays[array_index]):
            next_value = arrays[array_index][next_index]
            heapq.heappush(heap, (next_value, array_index, next_index))

    return merged
```

Each tuple says which value is available and where its successor lives. Because every array is sorted, no later value from an array can be needed before its current candidate. The heap therefore needs at most one entry per array.

**Complexity:** `O(N log K)` time for `N` total values and `O(K)` heap space, plus the required output.

**Test:** `[[1, 4], [1, 3], [], [2, 6]]` returns `[1, 1, 2, 3, 4, 6]`.

</details>
