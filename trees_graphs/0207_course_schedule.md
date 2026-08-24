# 207. Course Schedule

[LeetCode problem](https://leetcode.com/problems/course-schedule/) | [Python solution](./0207_course_schedule.py)

## What the Question Asks

There are `numCourses` courses numbered from `0`. A pair `[course, prerequisite]` means the prerequisite must be completed first. Return whether every course can be finished.

The impossible case is a directed cycle:

```text
0 requires 1, and 1 requires 0
```

Neither course can be taken first.

## Python Used Here

Create one separate list for each course:

```python
graph = [[] for _ in range(numCourses)]
```

`_` is a conventional name for a loop value that is not used. Avoid `[[]] * numCourses` here because that repeats references to the same inner list.

Create a list of zeros:

```python
in_degree = [0] * numCourses
```

Use a queue from `collections`:

```python
from collections import deque

queue.append(course)       # add to the right
course = queue.popleft()   # remove from the left
```

Both queue operations are efficient.

## Graph Vocabulary

- A node is a course.
- A directed edge goes from a prerequisite to the course it unlocks.
- `graph[x]` is the adjacency list of courses reached from `x`.
- A course's in-degree is the number of prerequisites still pointing into it.

## Topological Sort Idea

Any course with in-degree zero can be completed now. Completing it removes its outgoing prerequisite edges. This may reduce another course's in-degree to zero.

Process available courses with BFS. If every course is processed, a valid order exists. If some remain, they are trapped in a cycle.

## Step-by-Step Approach

1. Build the adjacency list and in-degree list.
2. Add every zero-in-degree course to the queue.
3. Remove one available course and count it as completed.
4. For each course it unlocks, subtract one from that course's in-degree.
5. Add a newly zero-in-degree course to the queue.
6. Return whether the completed count equals `numCourses`.

## Dry Run

For `[[1, 0], [2, 0], [3, 1], [3, 2]]`:

```text
0 -> 1 -> 3
 \-> 2 -/
```

- Initial in-degrees: `[0, 1, 1, 2]`; queue contains `0`.
- Complete `0`; courses `1` and `2` become available.
- Complete `1` and `2`; together they reduce course `3` to zero.
- Complete `3`. All four courses were processed, so return `True`.

For `0 -> 1 -> 0`, no node starts with in-degree zero. The queue is empty and completed remains zero, so return `False`.

## Complexity

Let `V` be courses and `E` be prerequisite pairs.

- Time: `O(V + E)` because each course and edge is processed once.
- Space: `O(V + E)` for the graph, counts, and queue.

## Common Mistakes

- Reversing the edge direction while keeping the wrong in-degree update.
- Using a normal list with `pop(0)`, which shifts all remaining items.
- Adding a course to the queue before its in-degree reaches zero.
- Returning `True` just because some courses were completed.

## Interview Explanation

> This is cycle detection in a directed graph. I use Kahn's topological sort: count each course's prerequisites, queue all zero-in-degree courses, and remove edges as courses complete. If I process every node, no cycle blocks the schedule.
