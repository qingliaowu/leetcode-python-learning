"""
LeetCode 200: Number of Islands

Count connected groups of "1" cells in a grid.

Beginner lesson:
See 0200_number_of_islands.md for grid indexing, stack-based DFS, a dry run,
and interview notes.

Complexity:
- time: O(ROWS * COLS)
- space: O(ROWS * COLS) in the worst case for the DFS stack
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """Return the number of horizontal/vertical land groups."""
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        island_count = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != "1":
                    continue

                # A new unvisited land cell starts a new island.
                island_count += 1
                grid[row][col] = "0"
                stack = [(row, col)]

                # DFS changes every connected land cell to visited water.
                while stack:
                    current_row, current_col = stack.pop()

                    for row_change, col_change in directions:
                        next_row = current_row + row_change
                        next_col = current_col + col_change

                        is_inside = (
                            0 <= next_row < rows and 0 <= next_col < cols
                        )
                        if is_inside and grid[next_row][next_col] == "1":
                            # Mark before pushing so it cannot be pushed twice.
                            grid[next_row][next_col] = "0"
                            stack.append((next_row, next_col))

        return island_count


if __name__ == "__main__":
    solution = Solution()

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert solution.numIslands(grid) == 3
    assert solution.numIslands([["0"]]) == 0
    assert solution.numIslands([["1"]]) == 1
    assert solution.numIslands([["1", "0"], ["0", "1"]]) == 2
