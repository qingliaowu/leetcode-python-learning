"""
LeetCode 322: Coin Change

Find the fewest coins needed to make an amount, or return -1 if impossible.

Beginner lesson:
See 0322_coin_change.md for the DP state, base case, transition, dry run,
complexity, edge cases, and interview explanation.

Complexity:
- time: O(A * C), for amount A and C coin choices
- space: O(A), for the saved answer to every amount
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """Return the minimum number of coins needed to make amount."""
        impossible = amount + 1
        dp = [impossible] * (amount + 1)

        # Making amount 0 requires no coins.
        dp[0] = 0

        for current_amount in range(1, amount + 1):
            for coin in coins:
                if coin <= current_amount:
                    smaller_answer = dp[current_amount - coin]
                    dp[current_amount] = min(
                        dp[current_amount],
                        smaller_answer + 1,
                    )

        if dp[amount] == impossible:
            return -1
        return dp[amount]


if __name__ == "__main__":
    solution = Solution()

    assert solution.coinChange([1, 2, 5], 11) == 3
    assert solution.coinChange([2], 3) == -1
    assert solution.coinChange([1], 0) == 0
    assert solution.coinChange([2, 5, 10, 1], 27) == 4
    assert solution.coinChange([3, 4], 6) == 2
