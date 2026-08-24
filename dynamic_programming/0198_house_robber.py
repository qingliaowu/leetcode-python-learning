"""
LeetCode 198: House Robber

Find the most money that can be taken without choosing adjacent houses.

Beginner lesson:
See 0198_house_robber.md for the DP state, take-or-skip recurrence, dry run,
complexity, edge cases, and interview explanation.

Complexity:
- time: O(N), because each house is processed once
- space: O(1), because only two previous answers are stored
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """Return the maximum money from non-adjacent houses."""
        # best_two_back: best answer before the previous house
        # best_one_back: best answer through the previous house
        best_two_back = 0
        best_one_back = 0

        for money in nums:
            take_current = best_two_back + money
            skip_current = best_one_back
            best_current = max(take_current, skip_current)

            # Move the saved states forward for the next house.
            best_two_back = best_one_back
            best_one_back = best_current

        return best_one_back


if __name__ == "__main__":
    solution = Solution()

    assert solution.rob([1, 2, 3, 1]) == 4
    assert solution.rob([2, 7, 9, 3, 1]) == 12
    assert solution.rob([5]) == 5
    assert solution.rob([]) == 0
    assert solution.rob([2, 1, 1, 2]) == 4
