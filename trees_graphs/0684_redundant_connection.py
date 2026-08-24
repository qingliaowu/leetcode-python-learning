"""
LeetCode 684: Redundant Connection

Find the edge that creates a cycle in an otherwise tree-shaped graph.

Beginner lesson:
See 0684_redundant_connection.md for union-find, path compression, union by
size, a dry run, and interview notes.

Complexity:
- time: O(N * alpha(N)), which is almost O(N)
- space: O(N)
"""


class UnionFind:
    """Track which numbered nodes belong to the same connected group."""

    def __init__(self, size: int):
        self.parent = list(range(size + 1))
        self.group_size = [1] * (size + 1)

    def find(self, node: int) -> int:
        """Return the group's representative and shorten the path to it."""
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, first: int, second: int) -> bool:
        """Join two groups; return False if they were already connected."""
        first_root = self.find(first)
        second_root = self.find(second)

        if first_root == second_root:
            return False

        if self.group_size[first_root] < self.group_size[second_root]:
            first_root, second_root = second_root, first_root

        self.parent[second_root] = first_root
        self.group_size[first_root] += self.group_size[second_root]
        return True


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        """Return the first edge whose endpoints are already connected."""
        groups = UnionFind(len(edges))

        for first, second in edges:
            if not groups.union(first, second):
                return [first, second]

        return []


if __name__ == "__main__":
    solution = Solution()

    assert solution.findRedundantConnection(
        [[1, 2], [1, 3], [2, 3]]
    ) == [2, 3]
    assert solution.findRedundantConnection(
        [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    ) == [1, 4]
    assert solution.findRedundantConnection([[1, 2], [2, 3], [1, 3]]) == [1, 3]
