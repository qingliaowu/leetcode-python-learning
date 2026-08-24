# 207. Course Schedule

[LeetCode problem](https://leetcode.com/problems/course-schedule/) | [Python solution](./0207_course_schedule.py) | [Topic guide](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

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

## Why It Is Correct

The queue contains exactly the courses with no remaining prerequisites. Taking
one is safe, and reducing the in-degree of each dependent course models
finishing that prerequisite. In an acyclic graph, this process eventually
unlocks and completes every course. A directed cycle never reaches in-degree
zero, so at least its courses remain uncompleted. Therefore `completed ==
numCourses` is true exactly when all courses can be finished.

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

Let `V` be courses and `E` be prerequisite pairs.

- Time: `O(V + E)` because each course and edge is processed once.
- Space: `O(V + E)` for the graph, counts, and queue.

## Assumptions to Say Aloud

- Courses are numbered from `0` through `numCourses - 1`.
- Each pair is `[course, prerequisite]`, which creates a directed edge from the
  prerequisite to the course.
- Only feasibility is required, not one valid course order.
- Input course IDs are valid; duplicate edges, if allowed, are counted and
  removed consistently.

## Edge Cases

- Zero courses or courses with no prerequisites.
- One self-dependency.
- A two-course or longer directed cycle.
- Several disconnected dependency chains.
- Many courses depend on the same prerequisite.

## Common Mistakes

- Reversing the edge direction while keeping the wrong in-degree update.
- Using a normal list with `pop(0)`, which shifts all remaining items.
- Adding a course to the queue before its in-degree reaches zero.
- Returning `True` just because some courses were completed.

## Possible Follow-up Questions

| Follow-up | Answer Direction |
| --- | --- |
| Return one valid course order. | Append each popped zero-in-degree course and return the list if it contains all courses; this is LeetCode 210. |
| Return the actual cycle when completion is impossible. | Use DFS colors and parent pointers; a back edge to a currently visiting node identifies a cycle path. |
| Find the minimum number of semesters with unlimited parallel courses. | Process topological BFS one queue layer per semester and count layers. |
| Only a limited number of courses can be taken each semester. | Available-course selection becomes a harder scheduling problem; discuss constraints and possibly state-search DP. |
| Prerequisites are added dynamically. | Rechecking from scratch is simplest; maintaining a dynamic topological order requires more advanced graph structures. |

## Interview Explanation

> This is cycle detection in a directed graph. I use Kahn's topological sort: count each course's prerequisites, queue all zero-in-degree courses, and remove edges as courses complete. If I process every node, no cycle blocks the schedule.

## Test Aloud

For two courses and `[[1, 0]]`, course `0` starts in the queue. Completing it
reduces course `1` to in-degree zero, so both courses finish and the result is
`True`. Add `[0, 1]`; now neither course starts at zero in-degree, the queue is
empty, and the result is `False`.

## Check Your Understanding

Try each question before opening its answer. Write every course's in-degree before starting the queue.

### Question 1: Is This Schedule Possible?

For `num_courses = 4` and prerequisites `[[1, 0], [2, 0], [3, 1], [3, 2]]`, can every course be completed? Give one valid order.

<details>
<summary>Show answer and explanation</summary>

**Answer:** Yes. One valid order is `[0, 1, 2, 3]`; `[0, 2, 1, 3]` is also valid.

Course `0` has in-degree zero, so it begins in the queue. Completing it removes one prerequisite from courses `1` and `2`, making both available. Course `3` becomes available only after both `1` and `2` are processed.

Different queue orders can produce different valid schedules. The requirement is that every prerequisite appears before the course that needs it.

**Complexity:** `O(V + E)` time and `O(V + E)` space for the graph, in-degrees, and queue.

**Edge case:** A pair such as `[[0, 1], [1, 0]]` is a cycle, so neither course ever reaches in-degree zero.

</details>

### Question 2: Return a Valid Course Order

Return one valid ordering, or an empty list if a cycle makes completion impossible.

<details>
<summary>Show answer and detailed solution</summary>

```python
from collections import deque


def find_course_order(
    num_courses: int, prerequisites: list[list[int]]
) -> list[int]:
    graph = [[] for _ in range(num_courses)]
    in_degree = [0] * num_courses

    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        in_degree[course] += 1

    queue = deque(
        course for course in range(num_courses) if in_degree[course] == 0
    )
    order = []

    while queue:
        course = queue.popleft()
        order.append(course)

        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)

    return order if len(order) == num_courses else []
```

The graph edge points from prerequisite to unlocked course. In-degree counts how many requirements remain. A course enters the queue exactly when that count becomes zero. If a cycle exists, its courses keep positive in-degree, so the final order is shorter than `num_courses`.

**Complexity:** `O(V + E)` time and `O(V + E)` extra space.

**Tests:** The example can return `[0, 1, 2, 3]`; prerequisites `[[0, 1], [1, 0]]` return `[]`.

</details>
