"""
LeetCode 704: Binary Search

Find a target in a sorted array by repeatedly discarding half.

Beginner lesson:
See 0704_binary_search.md for inclusive boundaries, midpoint calculation,
dry run, correctness, complexity, edge cases, and interview explanation.

Complexity:
- time: O(log N), because each iteration keeps at most half
- space: O(1), because only three indexes are stored
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Return target's index, or -1 when target is absent."""
        left = 0
        right = len(nums) - 1

        # Both left and right indexes are included in the search range.
        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            if nums[middle] < target:
                # Middle is too small, so discard it and everything left.
                left = middle + 1
            else:
                # Middle is too large, so discard it and everything right.
                right = middle - 1

        return -1


if __name__ == "__main__":
    solution = Solution()

    assert solution.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert solution.search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert solution.search([5], 5) == 0
    assert solution.search([5], 3) == -1
    assert solution.search([1, 2, 3, 4], 1) == 0
    assert solution.search([1, 2, 3, 4], 4) == 3
    assert solution.search([], 1) == -1
