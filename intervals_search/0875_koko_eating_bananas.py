"""
LeetCode 875: Koko Eating Bananas

Find the smallest integer eating speed that finishes all piles on time.

Beginner lesson:
See 0875_koko_eating_bananas.md for binary search on an answer range,
ceiling division, a dry run, and interview notes.

Complexity:
- time: O(N log M), where M is the largest pile
- space: O(1)
"""


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """Return the smallest feasible bananas-per-hour speed."""
        left = 1
        right = max(piles)

        while left < right:
            speed = (left + right) // 2
            hours = 0

            for pile in piles:
                hours += (pile + speed - 1) // speed

            if hours <= h:
                right = speed
            else:
                left = speed + 1

        return left


if __name__ == "__main__":
    solution = Solution()

    assert solution.minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert solution.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert solution.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
    assert solution.minEatingSpeed([1], 1) == 1
    assert solution.minEatingSpeed([1, 1, 1, 1], 10) == 1
