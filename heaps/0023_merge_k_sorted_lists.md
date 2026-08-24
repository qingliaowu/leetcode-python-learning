# 23. Merge K Sorted Lists

[LeetCode problem](https://leetcode.com/problems/merge-k-sorted-lists/) | [Python solution](./0023_merge_k_sorted_lists.py)

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

## Interview Explanation

> Each sorted list exposes its smallest remaining node at its head. I keep those at most `K` candidates in a min-heap, pop the smallest into the result, and replace it with its successor. A dummy head simplifies result construction. Every node performs `O(log K)` heap work, for `O(N log K)` total time.
