"""
LeetCode 300: Longest Increasing Subsequence

Find the longest strictly increasing subsequence length.

Beginner lesson:
See 0300_longest_increasing_subsequence.md for the ending-at-index DP state,
transition, dry run, complexity, edge cases, and interview explanation.

Complexity:
- time: O(N squared), because every index checks earlier indexes
- space: O(N), for one saved answer per index
"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """Return the longest strictly increasing subsequence length."""
        if not nums:
            return 0

        # One number by itself is an increasing subsequence of length 1.
        dp = [1] * len(nums)

        for current in range(len(nums)):
            for previous in range(current):
                if nums[previous] < nums[current]:
                    dp[current] = max(
                        dp[current],
                        dp[previous] + 1,
                    )

        return max(dp)


if __name__ == "__main__":
    solution = Solution()

    assert solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert solution.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
    assert solution.lengthOfLIS([7, 7, 7, 7]) == 1
    assert solution.lengthOfLIS([5]) == 1
    assert solution.lengthOfLIS([]) == 0
