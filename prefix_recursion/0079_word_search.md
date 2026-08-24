# 79. Word Search

[LeetCode problem](https://leetcode.com/problems/word-search/) | [Python solution](./0079_word_search.py)

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

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

Let `L` be word length.

- Up to every board cell is a start.
- Each character can try up to four directions.
- Worst-case time: `O(ROWS * COLS * 4^L)`.
- Recursion stack space: `O(L)`.

The no-reuse rule reduces actual branching after the first step, and mismatches often stop paths early.

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
