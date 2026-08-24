# 200. Number of Islands

[LeetCode problem](https://leetcode.com/problems/number-of-islands/) | [Python solution](./0200_number_of_islands.py) | [Topic guide](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

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

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

- Time: `O(ROWS * COLS)` because each cell is processed at most a constant number of times.
- Space: up to `O(ROWS * COLS)` for the stack when one island is very large.

## Common Mistakes

- Counting every land cell instead of every connected component.
- Including diagonal neighbors.
- Accessing a neighbor before checking its bounds.
- Marking visited only after popping, allowing duplicate stack entries.
- Forgetting that this version modifies the input grid.

## Possible Follow-up Questions

| Follow-up | Answer Direction |
| --- | --- |
| Do not modify the input grid. | Keep a separate set of visited `(row, column)` tuples, using up to `O(R * C)` extra space. |
| Count diagonal connections too. | Add the four diagonal direction pairs, giving eight possible neighbors per cell. |
| Return the largest island area. | Count cells during each DFS and update a maximum after completing the component. |
| Islands are added one cell at a time. | Use Union-Find to connect new land with existing neighboring components and maintain a running island count. |
| The grid is too large for recursion. | Use the explicit stack solution shown here, or process chunks when the full grid cannot fit in memory. |

## Interview Explanation

> I scan the grid. Each unvisited land cell begins a new connected component, so I increment the answer and run DFS to mark its entire island. Every cell is visited at most once, giving linear time in the grid size.

## Check Your Understanding

Try each question before opening its answer. Mark every cell reached by one traversal before counting again.

### Question 1: Count Components by Hand

How many islands are in this grid when only up, down, left, and right connections count?

```text
1 1 0 0
0 1 0 0
0 0 1 1
```

<details>
<summary>Show answer and explanation</summary>

**Answer:** `2` islands.

The top-left land cells `(0, 0)`, `(0, 1)`, and `(1, 1)` are connected and form one island. The two land cells in the final row form the second island. They touch the first group only diagonally, which does not count under the stated rules.

The outer scan increments the answer only when it finds land that no earlier traversal visited. The traversal then marks that island's complete component.

**Complexity:** `O(R * C)` time because each cell is processed at most once, with up to `O(R * C)` stack space in the worst case.

**Edge case:** A grid containing only water has `0` islands.

</details>

### Question 2: Find the Largest Island Area

Return the number of cells in the largest island. This version may change land from `1` to `0` as its visited mark.

<details>
<summary>Show answer and detailed solution</summary>

```python
def largest_island_area(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    columns = len(grid[0])
    largest = 0

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] != 1:
                continue

            area = 0
            stack = [(row, column)]
            grid[row][column] = 0

            while stack:
                current_row, current_column = stack.pop()
                area += 1

                for row_change, column_change in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row = current_row + row_change
                    next_column = current_column + column_change
                    inside = 0 <= next_row < rows and 0 <= next_column < columns

                    if inside and grid[next_row][next_column] == 1:
                        grid[next_row][next_column] = 0
                        stack.append((next_row, next_column))

            largest = max(largest, area)

    return largest
```

Each new land component starts an area counter. Marking a neighbor when it enters the stack prevents the same cell from being added more than once. After one component finishes, its area can update the global maximum.

**Complexity:** `O(R * C)` time and up to `O(R * C)` stack space.

**Tests:** The grid in Question 1 returns `3`; an all-water grid returns `0`.

</details>
