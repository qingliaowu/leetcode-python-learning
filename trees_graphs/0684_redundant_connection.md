# 684. Redundant Connection

[LeetCode problem](https://leetcode.com/problems/redundant-connection/) | [Python solution](./0684_redundant_connection.py) | [Topic guide](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## What the Question Asks

An undirected graph began as a tree, then one extra edge was added. Return the
edge that creates a cycle. If more than one answer could be removed, return the
one appearing last in the input under the problem's guarantee.

```text
edges:  [1, 2], [1, 3], [2, 3]
answer: [2, 3]
```

Before `[2, 3]`, nodes 2 and 3 are already connected through node 1.

## Recognize the Pattern

Look for:

- edges arrive one at a time,
- repeatedly ask whether two nodes are already connected,
- merge separate groups,
- find the edge that introduces a cycle.

This suggests **union-find**, also called a **disjoint set union** or DSU.

## The Group Idea

Each connected component chooses one representative called its **root**.

Union-find supports:

```text
find(node)       -> which group's root contains node?
union(a, b)      -> merge their groups if different
```

When an edge's endpoints already have the same root, a path already connects
them. Adding that edge closes a cycle.

## Parent References From Scratch

At first, every node is its own parent:

```text
parent[1] = 1
parent[2] = 2
parent[3] = 3
```

After joining 1 and 2, one root points to the other. `find` follows parents until
a node is its own parent.

## Two Speed Improvements

### Path Compression

While finding a root, point visited nodes closer to that root. Future searches
become shorter.

```python
self.parent[node] = self.parent[self.parent[node]]
```

This line makes a node skip one level at a time.

### Union by Size

Attach the smaller group's root under the larger group's root. This prevents
tall parent chains.

Path compression and union by size make operations almost constant time in
practice.

## The Invariant

After processing an edge prefix, two nodes have the same union-find root exactly
when the processed edges connect them.

Therefore the first edge whose endpoints already share a root is precisely the
edge that creates a cycle.

## Step by Step

1. Give each numbered node its own parent and group size one.
2. Read edges in input order.
3. Find each endpoint's root.
4. If the roots match, return that edge.
5. Otherwise attach the smaller group under the larger one.
6. Continue until the redundant edge is found.

## Dry Run

Edges are `[[1, 2], [1, 3], [2, 3]]`:

| Edge | Roots Before | Action |
| --- | --- | --- |
| `[1, 2]` | 1 and 2 | Join their groups |
| `[1, 3]` | 1 and 3 | Join their groups |
| `[2, 3]` | 1 and 1 | Already connected; return this edge |

## Python Used Here

```python
self.parent = list(range(size + 1))
```

For `size = 3`, this creates `[0, 1, 2, 3]`. Index zero is unused because node
labels begin at one.

```python
first_root, second_root = second_root, first_root
```

Python can swap two values without a temporary variable.

## Why It Is Correct

Initially, each union-find group matches one isolated graph node. Whenever an
edge connects different roots, merging those groups makes union-find connectivity
match graph connectivity after that edge.

If an edge has equal roots, its endpoints already have a path through earlier
edges. Adding the new edge creates a cycle. If roots differ, no earlier path
connects them, so joining the groups cannot create a cycle. Processing in order
therefore returns the required redundant edge.

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

Let `N` be the edge count. With path compression and union by size:

- Total time is `O(N * alpha(N))`.
- `alpha` is the inverse Ackermann function, which grows so slowly that it is
  below five for practical input sizes. Say "almost linear time" to a beginner.
- Parent and size arrays use `O(N)` space.

Without the optimizations, a badly shaped parent chain could make operations
linear.

## Assumptions to Say Aloud

- The graph is undirected.
- Node labels are integers from `1` through `N` under the problem constraints.
- The input is a tree plus exactly one extra edge, so an answer exists.
- Edges are processed in their supplied order.

## Edge Cases

- The extra edge completes a three-node triangle.
- The cycle appears only at the final edge.
- A long chain is connected back to its first node.
- The redundant edge connects nodes whose roots require path compression.
- Group sizes are equal; either root may become parent consistently.

## Common Mistakes

- Treating an undirected edge as one-way.
- Checking only whether direct parents match instead of calling `find`.
- Updating a node parent instead of its root parent during union.
- Forgetting node label `N` by allocating only `N` array positions.
- Using DFS from scratch for every edge and creating `O(N^2)` work.
- Calling `alpha(N)` exactly `O(1)` without explaining the standard bound.

## Possible Follow-up Questions

| Follow-up | Answer Direction |
| --- | --- |
| Count connected components. | Start with `N`; decrement once for every successful union. |
| Answer online connectivity queries. | Keep the DSU and compare roots for each query. |
| Nodes use string labels. | Map labels to parent dictionaries or assign integer IDs. |
| Edges can be deleted. | Basic DSU cannot split groups; consider offline processing, rollback DSU, or another dynamic-connectivity structure. |
| The graph is directed. | DSU does not capture directed cycles; use DFS coloring or topological reasoning. |

## Interview Explanation

> I process edges with union-find. Each component has a representative root.
> If an edge's endpoints already have the same root, an earlier path connects
> them and this edge creates the cycle. Otherwise I union their groups. Path
> compression and union by size make all edges almost linear overall, with
> `O(N)` parent and size storage.

## Test Aloud

```text
For [1,2], [2,3], [3,4], [1,4], the first three edges build one component. By
the time [1,4] arrives, both endpoints have the same root, so [1,4] is returned.
```

## Check Your Understanding

### Question 1: Follow the Groups

After successful unions `(1, 2)`, `(3, 4)`, and `(2, 3)`, are nodes 1 and 4
connected? What should `union(1, 4)` return?

<details>
<summary>Show answer and explanation</summary>

Yes. `(1, 2)` creates one group, `(3, 4)` creates another, and `(2, 3)` merges
those groups. Nodes 1 and 4 now have the same root. `union(1, 4)` returns `False`
because no merge is needed; in a cycle-detection use case, that edge is redundant.

</details>

### Question 2: Count Connected Components

Given `node_count` numbered from zero and undirected edges, return the number of
connected components.

<details>
<summary>Show answer and detailed solution</summary>

```python
def count_components(node_count: int, edges: list[list[int]]) -> int:
    parent = list(range(node_count))
    sizes = [1] * node_count

    def find(node: int) -> int:
        while node != parent[node]:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    components = node_count

    for first, second in edges:
        first_root = find(first)
        second_root = find(second)

        if first_root == second_root:
            continue

        if sizes[first_root] < sizes[second_root]:
            first_root, second_root = second_root, first_root

        parent[second_root] = first_root
        sizes[first_root] += sizes[second_root]
        components -= 1

    return components
```

Begin with one component per isolated node. Only a union between different roots
reduces the component count.

**Complexity:** `O((V + E) * alpha(V))` time and `O(V)` space.

**Test:** Four nodes with edges `[[0, 1], [2, 3]]` have two components.

</details>
