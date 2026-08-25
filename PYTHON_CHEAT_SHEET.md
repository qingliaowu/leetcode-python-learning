# Python Interview Cheat Sheet

[Repository home](./README.md) | [Python course](./python_basics/README.md) | [Setup and errors](./python_basics/00_setup_and_errors.md) | [Pattern map](./ALGORITHM_PATTERN_MAP.md) | [Interview playbook](./INTERVIEW_PLAYBOOK.md)

This is a lookup page, not a memorization assignment. When syntax blocks your
algorithm, find the smallest matching section, use it, then return to the
problem.

## 1. Read the Symbols

| Syntax | Read It As |
| --- | --- |
| `name = value` | Assign `value` to the name `name` |
| `a == b` | Ask whether `a` and `b` are equal |
| `a != b` | Ask whether they differ |
| `items[i]` | Read the item at index `i` |
| `mapping[key]` | Read the value stored under `key` |
| `function(x)` | Call `function` with argument `x` |
| `obj.name` | Read an attribute or method from `obj` |
| `condition:` | Begin an indented block controlled by `condition` |
| `-> int` | Type hint: the function returns an integer |
| `x is None` | Ask whether no object is present |

Python uses indentation to show which lines belong to a function, loop,
condition, or class.

## 2. Basic Values

```python
count = 3                 # int
price = 4.5               # float
word = "apple"            # str
is_ready = True           # bool
missing = None            # no value
```

```python
total = 7 + 2             # 9
difference = 7 - 2        # 5
product = 7 * 2           # 14
decimal = 7 / 2           # 3.5
whole = 7 // 2            # 3
remainder = 7 % 2         # 1
```

## 3. Choose a Collection

| Need | Use | Example |
| --- | --- | --- |
| Ordered values and indexes | List | `[10, 20, 30]` |
| Fixed small record or hashable key | Tuple | `(row, column)` |
| Key to value lookup | Dictionary | `{value: index}` |
| Unique membership only | Set | `{"a", "b"}` |
| First-in-first-out processing | `deque` | BFS queue |
| Repeated smallest-item access | `heapq` | Min-heap |

For the beginner explanation, operation costs, and quick checks, open
[Python Data Structures Made Simple](./python_basics/12_python_data_structures.md).

## 4. Strings

```python
text = "python"

first = text[0]           # "p"
last = text[-1]           # "n"
part = text[1:4]          # "yth"
length = len(text)        # 6
```

```python
words = "learn python".split()       # ["learn", "python"]
sentence = " ".join(words)           # "learn python"
lower = "ABC".lower()                 # "abc"
starts = "apple".startswith("app")   # True
```

Strings cannot be changed at one index. Build a new string or collect characters
in a list and join them.

## 5. Lists and Tuples

```python
values = [3, 1, 2]
values.append(4)          # [3, 1, 2, 4]
last = values.pop()       # removes and returns 4
values[0] = 9             # [9, 1, 2]
```

```python
sorted_copy = sorted(values)  # returns a new list
values.sort()                  # changes values itself
copied = values[:]             # shallow list copy
```

Tuple values cannot be changed:

```python
position = (2, 5)
row, column = position
```

## 6. Dictionaries

```python
indexes = {}
indexes[7] = 0

if 7 in indexes:
    saved_index = indexes[7]
```

Counting pattern:

```python
counts = {}

for value in values:
    counts[value] = counts.get(value, 0) + 1
```

Loop through key-value pairs:

```python
for key, value in counts.items():
    print(key, value)
```

`key in mapping` checks keys. Reading `mapping[key]` raises `KeyError` when the
key is missing; `.get(key, default)` returns the chosen default instead.

## 7. Sets

```python
seen = set()
seen.add("a")

if "a" in seen:
    print("already seen")

seen.remove("a")           # error if missing
seen.discard("a")          # safe if missing
```

Use `{}` for an empty dictionary and `set()` for an empty set.

## 8. Conditions

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
```

```python
if left <= right and target != 0:
    print("both conditions are true")
```

Common empty checks:

```python
if not values:
    return []

if node is None:
    return None
```

## 9. Loops

Visit values:

```python
for value in values:
    print(value)
```

Visit indexes and values:

```python
for index, value in enumerate(values):
    print(index, value)
```

Visit integer indexes:

```python
for index in range(len(values)):
    print(values[index])
```

Repeat while a condition is true:

```python
while left <= right:
    middle = (left + right) // 2
    # Update left or right so the loop makes progress.
```

`continue` starts the next iteration. `break` exits the nearest loop.

## 10. Functions

```python
def add(first: int, second: int) -> int:
    result = first + second
    return result
```

- Parameters are names in the function definition.
- Arguments are values supplied during a call.
- `return` sends a value back and stops the function.
- `print` only displays; it does not replace `return`.

```python
answer = add(2, 3)         # answer is 5
```

## 11. Type Hints

Modern Python style:

```python
def total(values: list[int]) -> int:
    return sum(values)
```

Many interview templates use the older spelling:

```python
from typing import List


def total(values: List[int]) -> int:
    return sum(values)
```

For this course, `list[int]` and `List[int]` communicate the same idea: a list
whose items are integers. Type hints help readers and tools; Python does not
automatically reject every wrong runtime value.

## 12. Classes and Node References

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

```python
first = ListNode(1)
second = ListNode(2)
first.next = second
```

`first.next` stores a reference to the same `second` object. It does not copy
that node.

## 13. Stack, Queue, and Heap

Stack, last in first out:

```python
stack = []
stack.append("a")
stack.append("b")
item = stack.pop()         # "b"
```

Queue, first in first out:

```python
from collections import deque

queue = deque(["a", "b"])
item = queue.popleft()     # "a"
queue.append("c")
```

Min-heap, smallest first:

```python
import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
smallest = heapq.heappop(heap)  # 2
```

## 14. Sorting With a Key

```python
intervals = [[5, 8], [1, 3]]
intervals.sort(key=lambda interval: interval[0])
```

Read the lambda as: "for each interval, use its item at index zero as the sort
key."

Tuple heap entries are compared left to right:

```python
heapq.heappush(heap, (priority, tie_breaker, item))
```

A numeric tie-breaker prevents Python from trying to compare custom node objects.

## 15. Recursion and Backtracking

Recursion needs a stopping condition and progress toward it:

```python
def countdown(number):
    if number == 0:
        return
    countdown(number - 1)
```

Backtracking temporarily changes state, explores, then restores:

```python
saved = board[row][column]
board[row][column] = "#"
found = search_next_step()
board[row][column] = saved
```

## 16. Copy or Mutate?

| Code | Effect |
| --- | --- |
| `alias = values` | Both names refer to the same list |
| `copy = values[:]` | New outer list with the same inner objects |
| `sorted(values)` | New sorted list |
| `values.sort()` | Changes the original list |
| `grid_copy = [row[:] for row in grid]` | New outer list and new row lists |

Say input mutation aloud during an interview.

## 17. Common Operation Costs

Let `N` be the collection size.

| Operation | Typical Time |
| --- | --- |
| List index read/write | `O(1)` |
| List append/pop at end | `O(1)` average |
| List membership | `O(N)` |
| Dictionary/set lookup | `O(1)` average |
| `deque.popleft()` | `O(1)` |
| Heap push/pop with `K` items | `O(log K)` |
| Sort `N` items | `O(N log N)` |
| String/list slice of length `K` | `O(K)` |

Read [Time and Space Complexity](./python_basics/11_time_and_space_complexity.md)
for the reasoning behind these costs.

## 18. Local LeetCode Template

```python
class Solution:
    def solve(self, values: list[int]) -> int:
        # 1. Handle a meaningful boundary case.
        # 2. Initialize state with one clear meaning.
        # 3. Traverse while preserving the invariant.
        # 4. Return the requested value.
        return 0


if __name__ == "__main__":
    solution = Solution()
    assert solution.solve([]) == 0
```

LeetCode supplies the class call. The local test block lets you run the same
logic yourself.

## 19. Say Complexity Aloud

Use a complete explanation:

```text
Let N be the number of values. I visit each value once. Each dictionary lookup
is O(1) on average, so total time is O(N). The dictionary may store N values, so
extra space is O(N).
```

Do not say only "O(N)." Name `N`, count the repeated work, and name stored data.

## 20. Where to Relearn

| If You Forgot | Open |
| --- | --- |
| Running files or reading errors | [Lesson 0](./python_basics/00_setup_and_errors.md) |
| Variables and basic values | [Lesson 2](./python_basics/02_variables_and_values.md) |
| Strings | [Lesson 3](./python_basics/03_strings.md) |
| Lists and tuples | [Lesson 4](./python_basics/04_lists_and_tuples.md) |
| Dictionaries and sets | [Lesson 5](./python_basics/05_dictionaries_and_sets.md) |
| Conditions and loops | [Lesson 6](./python_basics/06_conditions_and_loops.md) |
| Functions | [Lesson 7](./python_basics/07_functions.md) |
| Classes and nodes | [Lesson 8](./python_basics/08_classes_and_objects.md) |
| Recursion | [Lesson 9](./python_basics/09_recursion.md) |
| LeetCode format and tools | [Lesson 10](./python_basics/10_python_for_leetcode.md) |
| Big-O | [Lesson 11](./python_basics/11_time_and_space_complexity.md) |
| Choosing and combining data structures | [Lesson 12](./python_basics/12_python_data_structures.md) |

The goal is fluency, not perfect memory. Use the reference, write the line, and
return to reasoning about the problem.
