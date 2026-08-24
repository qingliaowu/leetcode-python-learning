# 102. Binary Tree Level Order Traversal

[LeetCode problem](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [Python solution](./0102_binary_tree_level_order_traversal.py) | [Topic guide](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## What the Question Asks

Return a binary tree's values grouped by depth from top to bottom.

```text
        3
       / \
      9  20
         / \
        15  7

answer: [[3], [9, 20], [15, 7]]
```

Each inner list contains one horizontal level.

## Binary Tree Refresher

A node stores:

```text
value
left child reference
right child reference
```

A child reference may be `None`, meaning that child does not exist.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

## Recognize the Pattern

Look for:

- values grouped by depth,
- nearest level before deeper levels,
- shortest number of unweighted steps,
- processing a tree one layer at a time.

This suggests **breadth-first search**, or BFS. A queue keeps nodes in the order
they should be visited.

## Why a Queue Works

The queue starts with the root. When one node leaves the front, its children join
the back. Therefore all nodes already waiting at the current depth leave before
the newly added next-depth nodes.

Python's `collections.deque` removes from the left in `O(1)` time. A normal list's
`pop(0)` shifts remaining values and can cost `O(N)`.

## Preserve Level Boundaries

At the beginning of a loop, `len(queue)` is exactly the number of nodes in the
current level.

Save that count before adding children:

```python
level_size = len(queue)

for _ in range(level_size):
    node = queue.popleft()
    # Append children for the next level.
```

If the loop used the queue's changing length, children could be mixed into the
same output level as their parents.

## The Invariant

At the start of each outer loop, the queue contains exactly the next tree level
from left to right.

After processing its saved size, all children of that level are queued in
left-to-right order, so the invariant holds for the next iteration.

## Step by Step

1. Return an empty list if the root is `None`.
2. Put the root in a queue.
3. Save the current queue length.
4. Remove exactly that many nodes and collect their values.
5. Add each existing left and right child to the queue.
6. Append the completed level to the answer.
7. Repeat until the queue is empty.

## Dry Run

For the sample tree:

| Start Queue | Saved Size | Output Level | Queue After Children |
| --- | ---: | --- | --- |
| `[3]` | 1 | `[3]` | `[9, 20]` |
| `[9, 20]` | 2 | `[9, 20]` | `[15, 7]` |
| `[15, 7]` | 2 | `[15, 7]` | `[]` |

## Python Used Here

```python
from collections import deque

queue = deque([root])
node = queue.popleft()
queue.append(node.left)
```

`popleft` removes the oldest queued node. `append` adds a node to the newest end.

The annotation `TreeNode | None` means the value may be a node or `None`.

## Why It Is Correct

The queue begins with exactly depth zero. Assume it begins an iteration with
exactly one level. The algorithm removes every node in that saved level from
left to right and appends only their children. Those children are exactly the
next level and are appended in left-to-right parent and child order. By
induction, every output group contains exactly one depth in the required order.

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

Let `N` be the node count and `W` the maximum number of nodes at one level.

- Every node enters and leaves the queue once: `O(N)` time.
- The queue holds at most one or two adjacent levels: `O(W)` auxiliary space.
- The returned values use `O(N)` output space.

## Assumptions to Say Aloud

- This is a valid binary tree with no cycles or shared child nodes.
- Values may repeat; nodes are identified by references, not unique values.
- Left-to-right order within a level matters.
- An empty tree returns an empty list.

## Edge Cases

- Empty tree.
- One node.
- Only left children or only right children.
- A wide complete level.
- Repeated node values.
- An unbalanced tree with missing children.

## Common Mistakes

- Appending `None` children and later trying to read their values.
- Using a stack, which explores depth before completing a level.
- Recalculating `len(queue)` while adding children.
- Using `list.pop(0)` and accidentally making queue operations expensive.
- Claiming space is always `O(log N)`; a wide tree can hold `O(N)` nodes.

## Possible Follow-up Questions

| Follow-up | Answer Direction |
| --- | --- |
| Return levels from bottom to top. | Build normal levels, then reverse the outer answer. |
| Return a zigzag order. | Reverse every second level or write into a deque by direction. |
| Return the right-side view. | Save the last value processed at each BFS level. |
| Find maximum depth. | Count completed levels instead of storing their values. |
| Use DFS instead. | Pass depth recursively and append into `levels[depth]`, accepting recursion-stack space. |

## Interview Explanation

> I use BFS because the output is grouped by depth. At the start of each outer
> loop, the queue contains one complete level. I save its size, remove exactly
> those nodes, and enqueue their children for the next level. Every node is
> processed once, so time is `O(N)`, and queue space is `O(W)` for maximum width.

## Test Aloud

```text
For a root 1 with only a left child 2, the first saved queue size is one and
produces [1]. Child 2 is then the complete next queue and produces [2]. The
answer is [[1], [2]].
```

## Check Your Understanding

### Question 1: Trace an Uneven Tree

What is the level order of this tree?

```text
        1
       / \
      2   3
       \   \
        4   5
```

<details>
<summary>Show answer and explanation</summary>

**Answer:** `[[1], [2, 3], [4, 5]]`.

Missing children do not add placeholders. When processing level `[2, 3]`, node
2 appends only child 4 and node 3 appends only child 5. Their queue order remains
left to right.

**Complexity:** `O(N)` time and `O(W)` auxiliary queue space.

</details>

### Question 2: Binary Tree Right-Side View

Return the value visible from the right side at each depth.

<details>
<summary>Show answer and detailed solution</summary>

```python
from collections import deque


def right_side_view(root: TreeNode | None) -> list[int]:
    if root is None:
        return []

    visible = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for position in range(level_size):
            node = queue.popleft()

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

            if position == level_size - 1:
                visible.append(node.val)

    return visible
```

Because each level is processed left to right, its last removed node is the
rightmost visible one.

**Complexity:** `O(N)` time and `O(W)` extra queue space.

**Edge cases:** Empty tree returns `[]`; a left-only tree still has one visible
node per depth.

</details>
