"""
LeetCode 79: Word Search

Determine whether a word can be formed from adjacent board cells without
reusing a cell.

Beginner lesson:
See 0079_word_search.md for recursive DFS, short-circuit logic, backtracking,
a dry run, and interview notes.

Complexity:
- time: O(ROWS * COLS * 4^L), where L is the word length
- space: O(L) for the recursion stack
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """Return True when one valid board path spells word."""
        if word == "":
            return True
        if not board or not board[0]:
            return False

        rows = len(board)
        cols = len(board[0])

        def dfs(row: int, col: int, index: int) -> bool:
            """Match word[index:] starting at board[row][col]."""
            is_outside = row < 0 or row >= rows or col < 0 or col >= cols
            if is_outside or board[row][col] != word[index]:
                return False

            # The final required character matched successfully.
            if index == len(word) - 1:
                return True

            saved_character = board[row][col]
            # Temporarily mark this cell so the current path cannot reuse it.
            board[row][col] = "#"

            found = (
                dfs(row + 1, col, index + 1)
                or dfs(row - 1, col, index + 1)
                or dfs(row, col + 1, index + 1)
                or dfs(row, col - 1, index + 1)
            )

            # Restore the cell for searches that follow a different path.
            board[row][col] = saved_character
            return found

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False


if __name__ == "__main__":
    solution = Solution()
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]

    assert solution.exist(board, "ABCCED") is True
    assert solution.exist(board, "SEE") is True
    assert solution.exist(board, "ABCB") is False
    # Successful and failed searches both restore the original board.
    assert board[0] == ["A", "B", "C", "E"]
