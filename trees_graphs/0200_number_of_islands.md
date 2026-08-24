# 200. Number of Islands

[LeetCode problem](https://leetcode.com/problems/number-of-islands/) | [Python solution](./0200_number_of_islands.py)

## What the Question Asks

A grid contains land (`"1"`) and water (`"0"`). Count groups of land connected horizontally or vertically. Diagonal cells are not connected.

Treat each land cell as a graph node and each horizontal or vertical connection as an edge.

## Python Used Here

`grid[row][col]` accesses one cell. Indexes start at zero.

```python
for row in range(rows):
    for col in range(cols):
```

`range(rows)` produces `0` through `rows - 1`. Nested loops visit every cell.

A list can act as a stack:

```python
stack.append(item)  # push
item = stack.pop()  # remove the most recently added item
```

`current_row, current_col = stack.pop()` unpacks a two-item tuple into two variables.

## DFS Idea

When an unvisited land cell is found, it begins one new island. Use depth-first search (DFS) to visit and mark all land connected to it. Later, the outer loops will skip those marked cells.

This solution marks visited land by changing `"1"` to `"0"`. That avoids a separate `visited` set, but it modifies the input grid.

## Step-by-Step Approach

1. Return `0` for an empty grid.
2. Visit every cell.
3. Skip water.
4. When unvisited land is found, add one to the island count.
5. Put that cell on a stack and mark it visited.
6. Pop cells and inspect their four neighbors.
7. Push each valid unvisited land neighbor after marking it.
8. When the stack empties, that complete island has been explored.

Mark a cell before adding it to the stack. Otherwise, two neighbors could add the same cell twice.

## Bounds Check

```python
0 <= next_row < rows and 0 <= next_col < cols
```

Python allows chained comparisons. The expression means the row and column are both inside the grid. Check bounds before accessing the cell to avoid an `IndexError` or unintended negative indexing.

## Dry Run

```text
1 1 0
1 0 0
0 0 1
```

- The top-left `1` starts island 1. DFS also marks the cells to its right and below.
- Those marked cells are skipped later.
- The bottom-right `1` is still unvisited, so it starts island 2.
- Final answer: `2`.

## Complexity

- Time: `O(ROWS * COLS)` because each cell is processed at most a constant number of times.
- Space: up to `O(ROWS * COLS)` for the stack when one island is very large.

## Common Mistakes

- Counting every land cell instead of every connected component.
- Including diagonal neighbors.
- Accessing a neighbor before checking its bounds.
- Marking visited only after popping, allowing duplicate stack entries.
- Forgetting that this version modifies the input grid.

## Interview Explanation

> I scan the grid. Each unvisited land cell begins a new connected component, so I increment the answer and run DFS to mark its entire island. Every cell is visited at most once, giving linear time in the grid size.
