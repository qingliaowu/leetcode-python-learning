"""
LeetCode 15: 3Sum

Return every unique triplet whose values add to zero.

Beginner lesson:
See 0015_3sum.md for the two-pointer pattern, duplicate handling, a dry run,
and interview notes.

Complexity:
- time: O(N^2)
- space: O(N) for the sorted copy, excluding returned triplets
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """Return unique value triplets that sum to zero."""
        values = sorted(nums)
        triplets = []

        for first in range(len(values) - 2):
            if first > 0 and values[first] == values[first - 1]:
                continue

            if values[first] > 0:
                break

            left = first + 1
            right = len(values) - 1

            while left < right:
                total = values[first] + values[left] + values[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    triplets.append(
                        [values[first], values[left], values[right]]
                    )
                    left += 1
                    right -= 1

                    while left < right and values[left] == values[left - 1]:
                        left += 1
                    while left < right and values[right] == values[right + 1]:
                        right -= 1

        return triplets


if __name__ == "__main__":
    solution = Solution()

    assert solution.threeSum([-1, 0, 1, 2, -1, -4]) == [
        [-1, -1, 2],
        [-1, 0, 1],
    ]
    assert solution.threeSum([0, 0, 0, 0]) == [[0, 0, 0]]
    assert solution.threeSum([1, 2, -2, -1]) == []
    assert solution.threeSum([]) == []
    assert solution.threeSum([-2, 0, 0, 2, 2]) == [[-2, 0, 2]]
