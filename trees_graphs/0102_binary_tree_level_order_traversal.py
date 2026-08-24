"""
LeetCode 102: Binary Tree Level Order Traversal

Return a binary tree's values one depth level at a time.

Beginner lesson:
See 0102_binary_tree_level_order_traversal.md for tree nodes, breadth-first
search, level boundaries, a dry run, and interview notes.

Complexity:
- time: O(N)
- space: O(W), where W is the tree's maximum width
"""

from collections import deque


class TreeNode:
    """Binary-tree node matching the class supplied by LeetCode."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        """Return node values grouped from the root level downward."""
        if root is None:
            return []

        levels = []
        queue = deque([root])

        while queue:
            level_values = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            levels.append(level_values)

        return levels


if __name__ == "__main__":
    solution = Solution()
    tree = TreeNode(
        3,
        TreeNode(9),
        TreeNode(20, TreeNode(15), TreeNode(7)),
    )

    assert solution.levelOrder(tree) == [[3], [9, 20], [15, 7]]
    assert solution.levelOrder(TreeNode(1)) == [[1]]
    assert solution.levelOrder(None) == []
    assert solution.levelOrder(TreeNode(1, TreeNode(2), None)) == [[1], [2]]
