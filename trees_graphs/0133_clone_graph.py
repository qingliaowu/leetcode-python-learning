"""
LeetCode 133: Clone Graph

Create a deep copy of every node and edge in a connected undirected graph.

Beginner lesson:
See 0133_clone_graph.md for object references, BFS, the clone map, a dry run,
and interview notes.

Complexity:
- time: O(V + E)
- space: O(V)
"""

from collections import deque


class Node:
    """Simple graph node matching the class supplied by LeetCode."""

    def __init__(self, val=0, neighbors=None):
        self.val = val
        # Create a new list for each node when no list was supplied.
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        """Return a deep copy of the connected graph starting at node."""
        if node is None:
            return None

        # Each original node maps to exactly one newly created clone.
        clones = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            current = queue.popleft()

            for neighbor in current.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                clones[current].neighbors.append(clones[neighbor])

        return clones[node]


if __name__ == "__main__":
    first = Node(1)
    second = Node(2)
    first.neighbors = [second]
    second.neighbors = [first]

    clone = Solution().cloneGraph(first)

    assert clone is not first
    assert clone.val == 1
    assert clone.neighbors[0] is not second
    assert clone.neighbors[0].val == 2
    assert clone.neighbors[0].neighbors[0] is clone
    assert Solution().cloneGraph(None) is None
