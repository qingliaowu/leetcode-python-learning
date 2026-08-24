# 206. Reverse Linked List

[LeetCode problem](https://leetcode.com/problems/reverse-linked-list/) | [Python solution](./0206_reverse_linked_list.py) | [Topic guide](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## What the Question Asks

Reverse a singly linked list and return its new first node.

```text
before: 1 -> 2 -> 3 -> None
after:  3 -> 2 -> 1 -> None
```

The nodes already exist. The goal is to change their `next` references, not to
sort values or return a Python list.

## Linked List Refresher

A node stores a value and a reference to the next node:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

`head` is a reference to the first node. `None` marks the end.

Unlike a Python list, a linked list has no instant index access. To reach the
fourth node, follow three `next` references.

## Recognize the Pattern

Look for:

- changing links in place,
- reversing or reconnecting a chain,
- preserving the unprocessed remainder before changing a pointer.

The core pattern uses three references:

```text
previous <- current    next_node -> remaining list
```

## The Dangerous Line

This reversal is necessary:

```python
current.next = previous
```

But it destroys the only forward link from `current` to the remaining list. Save
that link first:

```python
next_node = current.next
current.next = previous
```

Forgetting `next_node` loses access to every unprocessed node.

## The Invariant

Before each loop iteration:

- `previous` is the head of a fully reversed processed prefix.
- `current` is the first node of the untouched remaining suffix.
- Every original node is reachable from exactly one of those references.

One iteration moves `current` from the untouched suffix to the reversed prefix
without losing the rest.

## Step by Step

1. Set `previous = None` because the original head becomes the final tail.
2. Set `current = head`.
3. Save `current.next` as `next_node`.
4. Point `current.next` backward to `previous`.
5. Move `previous` to `current`.
6. Move `current` to the saved `next_node`.
7. Repeat until `current` is `None`.
8. Return `previous`, which now points to the new head.

## Dry Run

Reverse `1 -> 2 -> 3 -> None`:

| Before Iteration | Saved Next | Link Changed | After Movement |
| --- | --- | --- | --- |
| `previous=None`, `current=1` | 2 | `1 -> None` | `previous=1`, `current=2` |
| `previous=1`, `current=2` | 3 | `2 -> 1` | `previous=2`, `current=3` |
| `previous=2`, `current=3` | `None` | `3 -> 2` | `previous=3`, `current=None` |

Return node 3.

## Python References in Plain Language

```python
previous = current
```

This does not copy a node. Both names can refer to objects, and the assignment
changes which object `previous` refers to.

```python
current.next = previous
```

This mutates the current node's stored reference. It changes the linked-list
structure.

## Why It Is Correct

Initially, the reversed prefix is empty and the untouched suffix is the complete
list, so the invariant holds. Each loop saves the suffix's next node, reverses
the current link, and moves the boundary one node forward. Thus the processed
prefix is correctly reversed and no unprocessed node is lost.

When `current` becomes `None`, the untouched suffix is empty and `previous`
contains every original node in reverse order. Returning it is correct.

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

Let `N` be the node count.

- Each node is visited once: `O(N)` time.
- Only three changing references are stored: `O(1)` extra space.
- The existing nodes are reused.

## Assumptions to Say Aloud

- The input is a valid acyclic singly linked list.
- Reusing and mutating the supplied nodes is allowed.
- Node values need not be unique.
- An empty list has `head = None` and returns `None`.

## Edge Cases

- Empty list.
- One node.
- Two nodes, where pointer order is easy to inspect.
- Repeated values, which do not affect reference changes.
- A long list; the iterative version avoids recursion depth.

## Common Mistakes

- Reversing `current.next` before saving the original next node.
- Returning `current`, which is `None` after the loop.
- Moving `current` before moving `previous` and losing the processed node.
- Creating new nodes when in-place reversal was expected.
- Comparing values instead of changing references.
- Claiming recursive reversal uses `O(1)` space; call frames use `O(N)`.

## Possible Follow-up Questions

| Follow-up | Answer Direction |
| --- | --- |
| Reverse recursively. | Reverse the suffix, point the next node back, and clear the old forward link. |
| Reverse only positions `left` through `right`. | Save the node before the segment and reconnect both segment boundaries. |
| Reverse nodes in groups of `k`. | Verify a full group exists, reverse it, then connect to the next group. |
| Detect a cycle first. | Use slow and fast pointers; reversing a cyclic list would never reach `None`. |
| Use a doubly linked list. | Swap each node's `next` and `previous`, then update the head. |

## Interview Explanation

> I maintain `previous` as the reversed prefix and `current` as the untouched
> suffix. Before changing `current.next`, I save it so the remaining list is not
> lost. Then I reverse one link and advance both references. When current becomes
> null, previous is the new head. Every node is visited once, so time is `O(N)`
> and extra space is `O(1)`.

## Test Aloud

```text
For one node 7, I save next as None, point 7.next to previous None, move previous
to 7, and current to None. Returning previous returns the same one-node list.
```

## Check Your Understanding

### Question 1: Find the Lost-List Bug

What is wrong with this order?

```python
current.next = previous
current = current.next
```

<details>
<summary>Show answer and explanation</summary>

After the first line, `current.next` points backward to `previous`. The second
line therefore walks backward into the already processed prefix instead of
forward into the unprocessed suffix. The original next node is lost.

Save it first:

```python
next_node = current.next
current.next = previous
previous = current
current = next_node
```

</details>

### Question 2: Recursive Reversal

Write a recursive reverse and explain its extra space.

<details>
<summary>Show answer and detailed solution</summary>

```python
def reverse_recursive(head: ListNode | None) -> ListNode | None:
    if head is None or head.next is None:
        return head

    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head
```

The recursive call reverses everything after `head`. The old next node is now
the tail of that reversed suffix, so `head.next.next = head` points it back to
the current node. Clearing `head.next` prevents a two-node cycle.

**Complexity:** `O(N)` time and `O(N)` call-stack space. Unlike the iterative
version, recursion is not constant space and may hit Python's recursion limit on
a very long list.

**Tests:** Empty, one node, two nodes, and a normal multi-node list.

</details>
