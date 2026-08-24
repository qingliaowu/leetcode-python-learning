# 133. Clone Graph

[LeetCode problem](https://leetcode.com/problems/clone-graph/) | [Python solution](./0133_clone_graph.py)

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

- Time: `O(V + E)` because each node and edge is processed once.
- Space: `O(V)` for the map and BFS queue, excluding the required cloned output.

## Common Mistakes

- Returning the original node.
- Copying node values but attaching original neighbor objects.
- Creating a new clone every time a node is encountered.
- Marking a node only when it leaves the queue, allowing duplicate clones.
- Failing to handle `None` input.

## Interview Explanation

> I run BFS over the original graph and keep a map from each original node to its single clone. When I inspect an edge, I create the neighbor clone if necessary, then connect the two cloned nodes. The map also prevents cycles from causing repeated work.
