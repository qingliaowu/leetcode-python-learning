"""
LeetCode 994: Rotting Oranges

Return the minutes needed for rot to reach every fresh orange in a grid.

Beginner lesson:
See 0994_rotting_oranges.md for multi-source BFS, minute boundaries, fresh-item
counting, a dry run, and interview notes.

Complexity:
- time: O(ROWS * COLS)
- space: O(ROWS * COLS)
"""

from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        """Return elapsed minutes, or -1 when a fresh orange is unreachable."""
        rows = len(grid)
        columns = len(grid[0])
        queue = deque()
        fresh = 0

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 2:
                    queue.append((row, column))
                elif grid[row][column] == 1:
                    fresh += 1

        minutes = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while queue and fresh > 0:
            for _ in range(len(queue)):
                row, column = queue.popleft()

                for row_change, column_change in directions:
                    next_row = row + row_change
                    next_column = column + column_change

                    if (
                        0 <= next_row < rows
                        and 0 <= next_column < columns
                        and grid[next_row][next_column] == 1
                    ):
                        grid[next_row][next_column] = 2
                        fresh -= 1
                        queue.append((next_row, next_column))

            minutes += 1

        return minutes if fresh == 0 else -1


if __name__ == "__main__":
    solution = Solution()

    assert solution.orangesRotting(
        [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    ) == 4
    assert solution.orangesRotting(
        [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    ) == -1
    assert solution.orangesRotting([[0, 2]]) == 0
    assert solution.orangesRotting([[1]]) == -1
    assert solution.orangesRotting([[2, 2], [2, 2]]) == 0
