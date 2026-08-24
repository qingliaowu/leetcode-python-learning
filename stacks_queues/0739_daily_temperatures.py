"""
LeetCode 739: Daily Temperatures

For each day, return how many days pass before a warmer temperature.

Beginner lesson:
See 0739_daily_temperatures.md for monotonic stacks, index storage, a dry run,
and interview notes.

Complexity:
- time: O(N)
- space: O(N)
"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """Return the wait for a warmer day at every index."""
        waits = [0] * len(temperatures)
        unresolved = []

        for day, temperature in enumerate(temperatures):
            while (
                unresolved
                and temperatures[unresolved[-1]] < temperature
            ):
                colder_day = unresolved.pop()
                waits[colder_day] = day - colder_day

            unresolved.append(day)

        return waits


if __name__ == "__main__":
    solution = Solution()

    assert solution.dailyTemperatures(
        [73, 74, 75, 71, 69, 72, 76, 73]
    ) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert solution.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert solution.dailyTemperatures([60, 50, 40]) == [0, 0, 0]
    assert solution.dailyTemperatures([50, 50, 60]) == [2, 1, 0]
    assert solution.dailyTemperatures([]) == []
