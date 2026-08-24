# 994. Rotting Oranges

[LeetCode problem](https://leetcode.com/problems/rotting-oranges/) | [Python solution](./0994_rotting_oranges.py) | [Topic guide](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## What the Question Asks

A grid contains:

```text
0 = empty cell
1 = fresh orange
2 = rotten orange
```

Each minute, every rotten orange rots its fresh up, down, left, and right
neighbors. Return the minutes until no fresh orange remains, or `-1` if some
fresh orange can never be reached.

## Recognize the Pattern

Look for:

- several starting points act at the same time,
- something spreads in equal time steps,
- shortest unweighted distance from any source,
- grid neighbors processed layer by layer.

This is **multi-source BFS**. Put every initial source into one queue before the
search begins.

## Why One Source at a Time Is Wrong

If each rotten orange runs a separate search, the same cells may be visited many
times, and simulated minutes can become confused.

One shared queue represents real parallel spread:

```text
all cells currently rotten -> process one minute -> newly rotten cells
```

## Track Fresh Oranges

Count fresh oranges during the initial scan.

Whenever a fresh cell becomes rotten:

1. Change it to `2` immediately.
2. Decrease the fresh count.
3. Add it to the queue.

Immediate marking prevents two neighbors from queueing the same cell twice.

At the end:

- `fresh == 0` means every fresh orange was reached.
- `fresh > 0` means walls or empty cells isolated at least one orange.

## The Invariant

At the start of each BFS layer, the queue contains exactly the rotten oranges
that can spread during the current minute.

Newly rotten neighbors are queued for the next layer, so one completed queue
layer equals one elapsed minute.

## Step by Step

1. Scan the grid.
2. Queue every rotten cell and count every fresh cell.
3. While the queue and fresh cells both remain, save the current queue size.
4. Process exactly that many rotten cells.
5. Rot each valid fresh neighbor, mark it, decrement `fresh`, and queue it.
6. Increase minutes after finishing the layer.
7. Return minutes if `fresh` is zero; otherwise return `-1`.

## Dry Run

For:

```text
2 1 1
1 1 0
0 1 1
```

| Minute | Newly Rotten Cells |
| ---: | --- |
| 0 | `(0, 0)` is initially rotten |
| 1 | `(0, 1)`, `(1, 0)` |
| 2 | `(0, 2)`, `(1, 1)` |
| 3 | `(2, 1)` |
| 4 | `(2, 2)` |

Every fresh orange is reached in four minutes.

## Python Used Here

```python
directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
```

Each pair is a row and column change.

```python
0 <= next_row < rows and 0 <= next_column < columns
```

This checks that a neighbor stays inside the grid before reading it.

## Why It Is Correct

All initial rotten cells enter the queue at distance zero. BFS processes every
cell at distance `d` before any cell at distance `d + 1`. Therefore a fresh cell
is first marked at the earliest minute any rotten path can reach it.

Every reachable fresh cell is eventually marked because all four valid neighbors
of every reached cell are examined. Any remaining fresh cell has no path from an
initial rotten source, so `-1` is correct.

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

Let `R` be rows and `C` columns.

- The initial scan is `O(R * C)`.
- Each orange enters the queue at most once and checks four neighbors.
- Total time is `O(R * C)`.
- The queue can hold `O(R * C)` cells in the worst case.

## Assumptions to Say Aloud

- The grid is non-empty and rectangular under the problem constraints.
- Spread uses only four directions, not diagonals.
- All initial rotten oranges spread simultaneously.
- This implementation mutates fresh cells to rotten in the supplied grid.

## Edge Cases

- No fresh oranges returns `0`.
- Fresh oranges but no rotten source returns `-1`.
- One isolated fresh orange.
- Empty cells divide the grid into unreachable regions.
- Several initial rotten oranges meet in the middle.
- One row or one column.

## Common Mistakes

- Starting BFS from only one rotten orange.
- Increasing minutes after every cell instead of every queue layer.
- Marking a cell only when it leaves the queue, allowing duplicate entries.
- Returning the number of BFS layers when no fresh orange existed initially.
- Forgetting to check whether fresh oranges remain at the end.
- Allowing diagonal spread.

## Possible Follow-up Questions

| Follow-up | Answer Direction |
| --- | --- |
| Return the minute each cell rots. | Store a distance grid and assign parent distance plus one. |
| Do not mutate the input. | Copy the grid or keep a separate visited set. |
| Different cells take different times. | Use Dijkstra's algorithm with a min-heap instead of ordinary BFS. |
| Add walls. | Treat walls as cells that are never entered. |
| New sources appear over time. | Add timestamped events and process them in time order. |

## Interview Explanation

> This is multi-source BFS because all rotten oranges spread simultaneously. I
> queue every initial rotten cell, count fresh cells, and process the queue one
> saved level per minute. I mark a fresh neighbor when enqueueing it so it enters
> once. If fresh reaches zero I return elapsed minutes; otherwise an isolated
> orange remains and I return `-1`. Time and space are `O(rows * columns)`.

## Test Aloud

```text
For [[0, 2]], there are no fresh oranges. The BFS loop never needs to run and
the correct elapsed time is zero, not one.
```

## Check Your Understanding

### Question 1: Find an Unreachable Orange

Why does this grid return `-1`?

```text
2 1 1
0 1 1
1 0 1
```

<details>
<summary>Show answer and explanation</summary>

The fresh orange at the bottom-left `(2, 0)` is separated by empty cells above
and to the right. No four-direction path connects it to the initial rotten
orange. Other fresh cells rot, but the final fresh count remains one, so the
algorithm returns `-1`.

Diagonal contact does not count.

</details>

### Question 2: Distance to the Nearest Source

Given a rectangular grid containing `0` and `1`, return each cell's shortest
four-direction distance to any cell containing `0`.

<details>
<summary>Show answer and detailed solution</summary>

```python
from collections import deque


def nearest_zero(grid: list[list[int]]) -> list[list[int]]:
    rows = len(grid)
    columns = len(grid[0])
    distance = [[-1] * columns for _ in range(rows)]
    queue = deque()

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == 0:
                distance[row][column] = 0
                queue.append((row, column))

    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while queue:
        row, column = queue.popleft()

        for row_change, column_change in directions:
            next_row = row + row_change
            next_column = column + column_change

            if (
                0 <= next_row < rows
                and 0 <= next_column < columns
                and distance[next_row][next_column] == -1
            ):
                distance[next_row][next_column] = distance[row][column] + 1
                queue.append((next_row, next_column))

    return distance
```

Every zero is a distance-zero source. Multi-source BFS reaches each other cell
through the shortest number of unweighted steps.

**Complexity:** `O(R * C)` time and `O(R * C)` space.

</details>
