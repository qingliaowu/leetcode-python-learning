# Trees and Graphs

[Repository home](../README.md) | [Study plans](../INTERVIEW_STUDY_PLANS.md) | [Interview playbook](../INTERVIEW_PLAYBOOK.md) | [Progress tracker](../PROGRESS_TRACKER.md) | [System design](../system_design/README.md)

These high-priority problems practice graph traversal in three forms: exploring a grid, ordering directed dependencies, and copying an object graph.

Use the [interview playbook](../INTERVIEW_PLAYBOOK.md) for the solve-out-loud process. Review the [Python 3 Basics course](../python_basics/) before starting if classes, dictionaries, or loops feel rusty. The course includes a plain-English [time and space complexity lesson](../python_basics/11_time_and_space_complexity.md).

## Recommended Order

| LeetCode | Lesson | Python Solution | Main Pattern |
| ---: | --- | --- | --- |
| 200 | [Number of Islands](./0200_number_of_islands.md) | [Code](./0200_number_of_islands.py) | Grid DFS with a stack |
| 133 | [Clone Graph](./0133_clone_graph.md) | [Code](./0133_clone_graph.py) | BFS plus original-to-copy map |
| 207 | [Course Schedule](./0207_course_schedule.md) | [Code](./0207_course_schedule.py) | Topological sort with BFS |

## Recognize the Pattern

- A graph contains nodes connected by edges.
- DFS explores deeply before returning; BFS explores in layers.
- A `visited` set or similar state prevents processing the same node forever.
- Directed dependency problems often use an in-degree count and topological sorting.

## Ready to Move On

You are ready when you can choose DFS or BFS, name the visited state, avoid repeated work in cycles, and explain `O(V + E)` time. Continue to [Heaps and Top-K](../heaps/README.md).
