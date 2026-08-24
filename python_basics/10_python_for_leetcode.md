# Lesson 10: Python for LeetCode

[Run this lesson](./10_python_for_leetcode.py) | [Course home](./README.md)

## Goal

Understand the code format LeetCode expects and review the Python tools used most often in interviews.

## The Solution Class

LeetCode usually gives a method signature:

```python
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        pass
```

LeetCode creates `Solution()` and calls the method for you. Replace `pass` with your code. Keep the required class and method names exactly.

`pass` means "do nothing." It is a temporary placeholder that keeps an empty block syntactically valid.

## Read the Type Hints

```python
nums: List[int]
```

`nums` should be a list of integers.

```python
-> bool
```

The method should return `True` or `False`.

Other common shapes:

| Type hint | Meaning |
| --- | --- |
| `str` | One string |
| `List[str]` | List of strings |
| `List[List[int]]` | List of integer lists, often a grid |
| `int` | One integer |
| `None` | No returned value |

## A Complete Small Solution

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for number in nums:
            if number in seen:
                return True
            seen.add(number)

        return False
```

Approach:

1. A set remembers values already visited.
2. Return `True` when the current value is already present.
3. Otherwise, add it.
4. Return `False` after the loop if no duplicate appeared.

Time is `O(N)` average. Space is `O(N)` in the worst case.

## Useful Standard-Library Tools

### Stack

```python
stack = []
stack.append(item)
item = stack.pop()
```

Last in, first out. Used for iterative DFS and matching brackets.

### Queue

```python
from collections import deque

queue = deque()
queue.append(item)
item = queue.popleft()
```

First in, first out. Used for BFS.

### Min-Heap

```python
import heapq

heap = []
heapq.heappush(heap, value)
smallest = heapq.heappop(heap)
```

Used for top-k values, meeting end times, and merging sorted inputs.

## Local Test Block

Repository files include:

```python
if __name__ == "__main__":
    solution = Solution()
    assert solution.containsDuplicate([1, 2, 1]) is True
```

This block runs when the file is executed directly. LeetCode ignores it when using the imported class. Assertions turn examples into repeatable checks.

## A Simple Solve Order

Before coding:

1. Restate input and output.
2. Confirm assumptions and constraints.
3. Show a small example.
4. Give a direct approach.
5. Identify repeated work and choose a better data structure.

After coding:

1. Trace a normal example through the actual code.
2. Test the smallest input.
3. Test the problem's special edge case.
4. Explain time and extra space.

Use the full [Interview Problem-Solving Playbook](../INTERVIEW_PLAYBOOK.md) for solve-aloud sentence templates.

## Complexity Basics

| Complexity | Typical meaning |
| --- | --- |
| `O(1)` | One constant amount of work |
| `O(log N)` | Discard about half each step |
| `O(N)` | Visit every item once |
| `O(N log N)` | Often sorting |
| `O(N^2)` | Compare many pairs with nested loops |

Always explain why, not only the notation.

## Common Mistakes

- Printing an answer instead of returning it.
- Changing a required method name.
- Forgetting an import such as `heapq` or `deque`.
- Using a list for repeated membership tests when a set or dictionary fits.
- Ignoring empty input or boundary indexes.
- Saying complexity without defining `N`.
- Memorizing code without understanding the invariant.

## Final Beginner Checklist

You can now read the syntax used throughout this repository:

- variables and basic values,
- strings, lists, tuples, dictionaries, and sets,
- conditions and loops,
- functions and return values,
- classes and node references,
- recursion and backtracking,
- standard LeetCode class format.

Next, start with [Two Sum](../arrays_strings/0001_two_sum.md), then follow the interview roadmap in the main README.
