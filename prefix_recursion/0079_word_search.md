# 79. Word Search

[LeetCode problem](https://leetcode.com/problems/word-search/) | [Python solution](./0079_word_search.py) | [Topic guide](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## What the Question Asks

Find whether a word can be formed by moving horizontally or vertically through a character board. One board cell cannot be used more than once in the same path.

```text
A B C E
S F C S
A D E E
```

`ABCCED` exists. `ABCB` does not because its path would need to reuse the first `B` cell.

## Python Used Here

A function can be defined inside another function:

```python
def exist(...):
    rows = len(board)

    def dfs(...):
        print(rows)
```

The inner `dfs` function can read `board`, `word`, `rows`, and `cols` from the surrounding `exist` call.

Python's `or` short-circuits: it stops as soon as one expression is true. Therefore, the four recursive calls stop after finding one successful direction.

## Recursive DFS State

`dfs(row, col, index)` asks:

> Can I match `word[index:]` if the current character must come from this board cell?

Each call needs three pieces of state:

- current row,
- current column,
- index of the next required word character.

The index increases on every successful step, so recursion moves toward completion.

## Step-by-Step Approach

1. Try every board cell as the word's first position.
2. Reject a DFS call if its cell is outside the board.
3. Reject it if the cell does not match `word[index]`.
4. Return `True` if the final word character just matched.
5. Temporarily replace the current cell with `"#"` to mark it used.
6. Recursively try down, up, right, and left for the next character.
7. Restore the original character.
8. Return whether any direction succeeded.

## Backtracking

Backtracking is the sequence:

```text
choose -> explore -> undo the choice
```

Here:

```python
saved_character = board[row][col]
board[row][col] = "#"       # choose / mark used
found = ...                  # explore
board[row][col] = saved_character  # undo / restore
```

Restoration is required even when a path succeeds so the caller receives its board unchanged and other starting positions remain valid.

## Dry Run: `ABCCED`

Starting at top-left `A`:

1. Match `A`, mark its cell.
2. Move right and match `B`.
3. Move right and match `C`.
4. Move down and match the second `C`.
5. Move down and match `E`.
6. Move left and match final `D`; return `True`.
7. As recursive calls return, each marked cell is restored.

A wrong direction returns `False`, then another direction is tried from the previous call.

## Why It Is Correct

`dfs(row, col, index)` returns true exactly when a path starting at that cell
can spell `word[index:]`. It rejects out-of-bounds cells and wrong characters,
then temporarily marks a matching cell so the same path cannot use it twice.
The four recursive calls try every legal next direction. Restoring the cell
afterward leaves the board correct for other starting paths. Trying DFS from
every cell therefore finds a valid path if and only if one exists.

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

Let `L` be word length.

- Up to every board cell is a start.
- Each character can try up to four directions.
- Worst-case time: `O(ROWS * COLS * 4^L)`.
- Recursion stack space: `O(L)`.

The no-reuse rule reduces actual branching after the first step, and mismatches often stop paths early.

## Assumptions to Say Aloud

- Consecutive letters must be horizontally or vertically adjacent, not diagonal.
- One board cell cannot be reused within the same path.
- The board is rectangular and mutable; `#` is not a valid board character.
- This implementation treats an empty word as found.

## Edge Cases

- An empty word or empty board.
- One board cell and a one-letter word.
- The word is longer than the number of cells.
- Repeated letters tempt the search to reuse a cell.
- A failed early path must not block a later valid path.

## Common Mistakes

- Allowing diagonal movement.
- Reusing a cell in one path.
- Marking a cell permanently and breaking later starting positions.
- Returning immediately before restoring changed board state.
- Forgetting bounds checks before indexing the board.
- Passing the same `index` to the next recursive call.

## Possible Follow-up Questions

| Follow-up | Answer Direction |
| --- | --- |
| Return the path of board coordinates. | Append each chosen coordinate, copy or return the path on success, and pop it while backtracking on failure. |
| Search for many words in one board. | Build a Trie of all words and run board DFS once while following Trie paths; this is Word Search II. |
| Allow diagonal movement. | Add four diagonal directions, increasing each call's possible branches from four to eight. |
| Allow each cell to be reused up to `K` times. | Replace the temporary marker with a per-cell usage count and backtrack the count. |
| How can you prune faster? | Reject words longer than the board, compare board/word character counts, or start from the rarer end of the word. |

## Interview Explanation

> I try each cell as a starting point and use DFS to match one word character per step. I temporarily mark a matched cell so the current path cannot reuse it, explore four neighbors, and restore it while backtracking. The recursion depth is at most the word length.

## Test Aloud

On the sample board, trace `ABCCED`: mark each chosen cell, move only to an
adjacent matching cell, and restore all marks as recursive calls return. Then
test `ABCB`; reaching the final `B` would require reusing the first row's `B`,
which is marked, so the result is `False`. Confirm the board matches its
original contents after both searches.

## Check Your Understanding

Try each question before opening its answer. Trace both the choice and the undo step.

### Question 1: Can This Path Be Reused?

Given this board, does the word `"ABA"` exist?

```text
A B
C A
```

Why must a visited mark be restored after an unsuccessful path?

<details>
<summary>Show answer and explanation</summary>

**Answer:** Yes. One path is `(0, 0) -> (0, 1) -> (1, 1)`.

The first `A` matches at the top left, `B` is directly to its right, and the second `A` is directly below that `B`. No cell is reused within this path.

A visited mark belongs only to the current candidate path. If that path fails, another starting position or branch must be allowed to use the cell. Failing to restore it would make later valid searches see a board that was never part of the original input.

**Complexity:** For `R * C` cells and word length `L`, a common upper bound is `O(R * C * 4^L)` time and `O(L)` recursion space.

**Edge case:** If the word is longer than the number of board cells, it cannot fit without reuse.

</details>

### Question 2: Allow Diagonal Steps

Write a version that allows all eight neighboring directions while still forbidding cell reuse in one path.

<details>
<summary>Show answer and detailed solution</summary>

```python
def exists_with_diagonals(board: list[list[str]], word: str) -> bool:
    if not word:
        return True
    if not board or not board[0]:
        return False

    rows = len(board)
    columns = len(board[0])
    used = set()
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),            (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    def dfs(row: int, column: int, index: int) -> bool:
        if board[row][column] != word[index]:
            return False
        if index == len(word) - 1:
            return True

        used.add((row, column))
        found = False

        for row_change, column_change in directions:
            next_row = row + row_change
            next_column = column + column_change
            inside = 0 <= next_row < rows and 0 <= next_column < columns

            if inside and (next_row, next_column) not in used:
                if dfs(next_row, next_column, index + 1):
                    found = True
                    break

        used.remove((row, column))
        return found

    for row in range(rows):
        for column in range(columns):
            if dfs(row, column, 0):
                return True

    return False
```

The state is the current cell, the next word index, and the cells already used by this path. The function adds a cell before exploring and removes it before returning, which is the backtracking step. The only structural change from four-direction search is the direction list.

**Complexity:** A simple upper bound is `O(R * C * 8^L)` time and `O(L)` path and recursion space.

**Test:** On `[['A', 'X'], ['X', 'B']]`, the word `"AB"` is found diagonally.

</details>
