# Trees and Graphs

These high-priority problems practice graph traversal in three forms: exploring a grid, ordering directed dependencies, and copying an object graph.

Use the [interview playbook](../INTERVIEW_PLAYBOOK.md) for the solve-out-loud process. Review the [Python 3 Basics course](../python_basics/) before starting if classes, dictionaries, or loops feel rusty. The course includes a plain-English [time and space complexity lesson](../python_basics/11_time_and_space_complexity.md).

| LeetCode | Lesson | Python Solution | Main Pattern |
| ---: | --- | --- | --- |
| 200 | [Number of Islands](./0200_number_of_islands.md) | [Code](./0200_number_of_islands.py) | Grid DFS with a stack |
| 207 | [Course Schedule](./0207_course_schedule.md) | [Code](./0207_course_schedule.py) | Topological sort with BFS |
| 133 | [Clone Graph](./0133_clone_graph.md) | [Code](./0133_clone_graph.py) | BFS plus original-to-copy map |

## Pattern Summary

- A graph contains nodes connected by edges.
- DFS explores deeply before returning; BFS explores in layers.
- A `visited` set or similar state prevents processing the same node forever.
- Directed dependency problems often use an in-degree count and topological sorting.
