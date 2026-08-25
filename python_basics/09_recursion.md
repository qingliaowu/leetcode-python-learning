# Lesson 9: Recursion

[Run this lesson](./09_recursion.py) | [Course home](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## Goal

Understand a function that calls itself, how it stops, and why recursion is useful for trees, graphs, and backtracking.

## The Two Required Parts

Every recursive function needs:

1. A base case that returns without another recursive call.
2. A recursive case that moves toward the base case.

```python
def sum_to(number):
    if number == 0:             # base case
        return 0
    return number + sum_to(number - 1)  # recursive case
```

The recursive call receives `number - 1`, so it gets closer to zero.

## Trace the Calls

For `sum_to(3)`:

```text
sum_to(3)
= 3 + sum_to(2)
= 3 + 2 + sum_to(1)
= 3 + 2 + 1 + sum_to(0)
= 3 + 2 + 1 + 0
= 6
```

Calls wait for smaller calls to return. Python remembers each waiting call on the call stack.

## Factorial Example

Factorial means multiplying downward:

```text
4! = 4 * 3 * 2 * 1 = 24
```

```python
def factorial(number):
    if number <= 1:
        return 1
    return number * factorial(number - 1)
```

## Why Interviews Use Recursion

Recursive structure matches problems that contain smaller versions of themselves:

- A tree contains smaller child trees.
- DFS explores a path, then another path.
- A wildcard may branch into several smaller searches.
- Backtracking chooses one option and recursively handles what remains.

Problem 211 uses recursive DFS for `.` wildcard searches. Problem 79 uses recursive DFS and restores board state after each path.

## Backtracking Shape

Backtracking adds one important step: undo the choice after exploration.

```python
choose()
found = search_smaller_problem()
undo_choice()
return found
```

The Word Search lesson temporarily marks a board cell, explores neighbors, and restores the original character.

## Recursion Versus a Loop

Simple counting is usually clearer with a loop. Recursion is helpful when the data or choices naturally branch.

Python limits recursion depth. For a very deep graph, an explicit list stack may be safer.

## Try It

What does `power(2, 3)` return?

```python
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)
```

<details>
<summary>Show answer and explanation</summary>

The answer is `8`:

```text
power(2, 3)
= 2 * power(2, 2)
= 2 * 2 * power(2, 1)
= 2 * 2 * 2 * power(2, 0)
= 2 * 2 * 2 * 1
= 8
```

Every call reduces `exponent` by one. At zero, the base case returns `1` and
the waiting multiplications complete.

</details>

## Common Mistakes

- Forgetting the base case.
- Making a recursive call that does not move toward the base case.
- Losing the value returned by the recursive call.
- Sharing mutable state without restoring it during backtracking.
- Using recursion where one simple loop would be clearer.

## How to Debug Recursion

Write down each call's argument. Ask:

1. What is the base case?
2. Is this call closer to it?
3. What value does the smaller call return?
4. What does the current call do with that value?

## Remember

Recursion solves a problem using a smaller version of the same problem. It must have a stopping rule and make progress toward it.

---

[Previous: Lesson 8, Classes and Objects](./08_classes_and_objects.md) | [Next: Lesson 10, Python for LeetCode](./10_python_for_leetcode.md)
