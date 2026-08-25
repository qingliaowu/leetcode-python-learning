# Trees and Graphs

[Repository home](../README.md) | [Study plans](../INTERVIEW_STUDY_PLANS.md) | [Interview playbook](../INTERVIEW_PLAYBOOK.md) | [Pattern map](../ALGORITHM_PATTERN_MAP.md) | [Progress tracker](../PROGRESS_TRACKER.md) | [System design](../system_design/README.md) | [FDE track](../fde_interview/README.md) | [AI engineering](../ai_engineering/README.md)

These lessons cover tree levels, grid traversal and propagation, object-graph copying, dynamic connectivity, and directed dependency ordering.

Use the [interview playbook](../INTERVIEW_PLAYBOOK.md) for the solve-out-loud process. Review the [Python 3 Basics course](../python_basics/) before starting if classes, dictionaries, or loops feel rusty. The course includes a plain-English [time and space complexity lesson](../python_basics/11_time_and_space_complexity.md).

## Recommended Order

| LeetCode | Lesson | Python Solution | Main Pattern |
| ---: | --- | --- | --- |
| 102 | [Binary Tree Level Order Traversal](./0102_binary_tree_level_order_traversal.md) | [Code](./0102_binary_tree_level_order_traversal.py) | Tree BFS with saved level size |
| 200 | [Number of Islands](./0200_number_of_islands.md) | [Code](./0200_number_of_islands.py) | Grid DFS with a stack |
| 994 | [Rotting Oranges](./0994_rotting_oranges.md) | [Code](./0994_rotting_oranges.py) | Multi-source BFS by minute |
| 133 | [Clone Graph](./0133_clone_graph.md) | [Code](./0133_clone_graph.py) | BFS plus original-to-copy map |
| 684 | [Redundant Connection](./0684_redundant_connection.md) | [Code](./0684_redundant_connection.py) | Union-find connectivity |
| 207 | [Course Schedule](./0207_course_schedule.md) | [Code](./0207_course_schedule.py) | Topological sort with BFS |

## Recognize the Pattern

- A graph contains nodes connected by edges.
- DFS explores deeply before returning; BFS explores in layers.
- Multi-source BFS begins with every distance-zero source in the queue.
- A `visited` set or similar state prevents processing the same node forever.
- Union-find supports repeated connectivity checks while undirected edges arrive.
- Directed dependency problems often use an in-degree count and topological sorting.

## Ready to Move On

You are ready when you can choose DFS, BFS, multi-source BFS, union-find, or topological sort; name the state that prevents repeated work; and explain traversal cost in nodes and edges. Continue to [Heaps and Top-K](../heaps/README.md).
