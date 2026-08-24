"""
LeetCode 207: Course Schedule

Determine whether all courses can be completed given prerequisite edges.

Beginner lesson:
See 0207_course_schedule.md for adjacency lists, in-degree, BFS, a dry run,
and interview notes.

Complexity:
- time: O(V + E), for courses V and prerequisite edges E
- space: O(V + E)
"""

from collections import deque
from typing import List


class Solution:
    def canFinish(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> bool:
        """Return False when prerequisite relationships contain a cycle."""
        # graph[x] contains courses unlocked after completing course x.
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            in_degree[course] += 1

        # Courses with no remaining prerequisites can be taken immediately.
        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)

        completed = 0

        while queue:
            prerequisite = queue.popleft()
            completed += 1

            for course in graph[prerequisite]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    queue.append(course)

        return completed == numCourses


if __name__ == "__main__":
    solution = Solution()

    assert solution.canFinish(2, [[1, 0]]) is True
    assert solution.canFinish(2, [[1, 0], [0, 1]]) is False
    assert solution.canFinish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) is True
