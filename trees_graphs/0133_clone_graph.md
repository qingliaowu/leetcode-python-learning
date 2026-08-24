# 133. Clone Graph

[LeetCode problem](https://leetcode.com/problems/clone-graph/) | [Python solution](./0133_clone_graph.py) | [Topic guide](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## What the Question Asks

Given one node in a connected undirected graph, return a deep copy of the entire graph.

A deep copy means:

- every clone has the same value as its original,
- every edge is reproduced, and
- no returned node is an original node.

Copying only the starting node or reusing original neighbors is not enough.

## Python Used Here

Python variables hold references to objects:

```python
copy = original       # same object, not a clone
copy = Node(original.val)  # new object
```

Objects can be dictionary keys. The solution maps each original node object to its new clone object:

```python
clones[original] = copied_node
```

`deque([node])` creates a queue already containing `node`.

## Why a Clone Map Is Necessary

Graphs can contain cycles and can reach the same node through multiple paths. Without remembered state, traversal could loop forever or create multiple copies of one original node.

The `clones` dictionary serves two purposes:

1. It marks which original nodes have been discovered.
2. It gives immediate access to the one correct clone for each original.

## Step-by-Step Approach

1. Return `None` if the input is `None`.
2. Create the starting node's clone and store it in `clones`.
3. Put the original starting node in a BFS queue.
4. Remove one original node from the queue.
5. For each original neighbor, create and queue its clone if needed.
6. Append the neighbor's clone to the current node's clone neighbor list.
7. Return the clone mapped from the original start node.

Traverse originals, but build all edges between clones.

## Dry Run

For two connected nodes:

```text
original 1 <-> original 2
```

- Create `clone 1`; map `original 1 -> clone 1`.
- Visit original 1. Original 2 is new, so create `clone 2` and queue original 2.
- Add clone 2 to clone 1's neighbors.
- Visit original 2. Original 1 is already mapped, so do not create it again.
- Add clone 1 to clone 2's neighbors.

The copied cycle is complete and contains no original nodes.

## The Node Class

LeetCode supplies the `Node` class. This repository includes it so the file can run locally. During an interview, use the class definition provided by the platform.

The constructor avoids `neighbors=[]` as a default argument because a mutable default list would be shared by multiple objects.

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

- Time: `O(V + E)` because each node and edge is processed once.
- Space: `O(V)` for the map and BFS queue, excluding the required cloned output.

## Common Mistakes

- Returning the original node.
- Copying node values but attaching original neighbor objects.
- Creating a new clone every time a node is encountered.
- Marking a node only when it leaves the queue, allowing duplicate clones.
- Failing to handle `None` input.

## Possible Follow-up Questions

| Follow-up | Answer Direction |
| --- | --- |
| The graph may be disconnected and all nodes must be cloned. | Start BFS or DFS from every unvisited node supplied in the full node list. |
| Edges have weights or labels. | Copy edge objects or metadata while connecting the already mapped clone nodes. |
| Can you use DFS instead of BFS? | Yes. The same original-to-clone map prevents cycles; recursive DFS adds `O(V)` worst-case call-stack space. |
| How do self-loops and duplicate edges behave? | Append the mapped clone for every original neighbor entry, including the node itself, preserving exact adjacency. |
| Clone only nodes within distance `K`. | Add BFS depth to queue entries and stop expanding neighbors at depth `K`. |

## Interview Explanation

> I run BFS over the original graph and keep a map from each original node to its single clone. When I inspect an edge, I create the neighbor clone if necessary, then connect the two cloned nodes. The map also prevents cycles from causing repeated work.

## Check Your Understanding

Try each question before opening its answer. Draw the original-to-clone map as it grows.

### Question 1: Clone a Cycle

Three nodes form the undirected cycle `1 - 2 - 3 - 1`. How many clone objects should be created, and why does BFS stop instead of circling forever?

<details>
<summary>Show answer and explanation</summary>

**Answer:** Exactly `3` clone objects should be created, one for each original node.

The map starts with `original 1 -> clone 1`. When node `1` discovers nodes `2` and `3`, each receives one clone and enters the queue. Later, edges back to node `1` or between nodes `2` and `3` find originals already present in the map, so the algorithm reuses their clones instead of creating or queuing them again.

The map has two jobs: it finds the correct clone for every edge and also acts as the visited set.

**Complexity:** `O(V + E)` time and `O(V)` extra space.

**Edge case:** A self-loop must connect the cloned node to itself, not to the original node.

</details>

### Question 2: Clone While Transforming Values

Clone a graph, but make every cloned node's value twice its original value. Assume the lesson's `Node` class is available.

<details>
<summary>Show answer and detailed solution</summary>

```python
from collections import deque


def clone_with_doubled_values(node: "Node | None") -> "Node | None":
    if node is None:
        return None

    clones = {node: Node(node.val * 2)}
    queue = deque([node])

    while queue:
        original = queue.popleft()

        for neighbor in original.neighbors:
            if neighbor not in clones:
                clones[neighbor] = Node(neighbor.val * 2)
                queue.append(neighbor)

            clones[original].neighbors.append(clones[neighbor])

    return clones[node]
```

Only node construction changes; the graph-copying invariant stays the same. Each original has exactly one mapped clone. Every original edge `original -> neighbor` becomes the clone edge `clones[original] -> clones[neighbor]`.

Cycles are safe because a mapped node is never created or queued a second time.

**Complexity:** `O(V + E)` time and `O(V)` extra space, excluding the required cloned output.

**Test:** A two-node cycle with values `2` and `5` becomes a separate two-node cycle with values `4` and `10`.

</details>
