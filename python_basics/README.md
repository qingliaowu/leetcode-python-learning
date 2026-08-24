# Python 3 Basics for Complete Beginners

[Repository home](../README.md) | [Study plans](../INTERVIEW_STUDY_PLANS.md) | [Interview playbook](../INTERVIEW_PLAYBOOK.md) | [Progress tracker](../PROGRESS_TRACKER.md) | [System design](../system_design/README.md)

This course assumes you have forgotten Python or have never used it. It teaches only one small group of ideas at a time, using examples related to LeetCode.

You do not need to install any package. Python 3 and a terminal are enough.

## Before You Start

From the repository root, check Python:

```bash
python3 --version
```

You should see `Python 3` followed by a version number. Run the first lesson:

```bash
python3 python_basics/01_first_program.py
```

The file prints examples and checks its answers with `assert`. If no error appears, the checks passed.

## Learning Path

Complete the lessons in order. Most should take about 15 to 25 minutes. Lesson 11 is longer, so its page divides the material into three short passes.

| Lesson | Read | Run | You Will Learn |
| ---: | --- | --- | --- |
| 1 | [Your First Program](./01_first_program.md) | [Code](./01_first_program.py) | `print`, comments, and running a file |
| 2 | [Variables and Basic Values](./02_variables_and_values.md) | [Code](./02_variables_and_values.py) | Numbers, booleans, `None`, and operators |
| 3 | [Strings](./03_strings.md) | [Code](./03_strings.py) | Text, indexes, slices, and string methods |
| 4 | [Lists and Tuples](./04_lists_and_tuples.md) | [Code](./04_lists_and_tuples.py) | Ordered collections and mutation |
| 5 | [Dictionaries and Sets](./05_dictionaries_and_sets.md) | [Code](./05_dictionaries_and_sets.py) | Fast lookup, counting, and unique values |
| 6 | [Conditions and Loops](./06_conditions_and_loops.md) | [Code](./06_conditions_and_loops.py) | Decisions, repetition, `range`, and `enumerate` |
| 7 | [Functions](./07_functions.md) | [Code](./07_functions.py) | Parameters, `return`, and type hints |
| 8 | [Classes and Objects](./08_classes_and_objects.md) | [Code](./08_classes_and_objects.py) | `class`, `self`, `__init__`, and nodes |
| 9 | [Recursion](./09_recursion.md) | [Code](./09_recursion.py) | Base cases, recursive calls, and backtracking |
| 10 | [Python for LeetCode](./10_python_for_leetcode.md) | [Code](./10_python_for_leetcode.py) | Solution classes, tests, and common tools |
| 11 | [Time and Space Complexity](./11_time_and_space_complexity.md) | [Code](./11_time_and_space_complexity.py) | Big-O explained with simple counting |

## The Best Way to Study

For every lesson:

1. Read one section.
2. Type the small example yourself.
3. Predict the result before running it.
4. Run the lesson file.
5. Change one value and predict what changes.
6. Explain the example in your own words.

Do not try to memorize every method. Learn what each data type is good for, then look up exact syntax when needed.

## Tiny Symbol Guide

| Symbol | Meaning |
| --- | --- |
| `=` | Assign a value to a variable |
| `==` | Ask whether two values are equal |
| `!=` | Ask whether two values are different |
| `:` | Start an indented block |
| `()` | Call a function or group an expression |
| `[]` | Create/access a list, or access by index/key |
| `{}` | Create an empty dictionary |
| `#` | Start a comment |
| `->` | Show a function's return type hint |

## Ready to Move On

You are ready to start the problem folders when you can:

- read and change a list,
- look up and save dictionary values,
- write an `if` statement and a loop,
- write a function that returns a value,
- explain what a class object stores,
- trace a short recursive function,
- explain how time and memory grow as input grows.

Record your progress in the [tracker](../PROGRESS_TRACKER.md), then continue to [Arrays, Strings, Hash Maps, and Sliding Window](../arrays_strings/README.md). Use the [Interview Problem-Solving Playbook](../INTERVIEW_PLAYBOOK.md) to practice solving aloud.

## Getting Help From Errors

An error is information, not failure. Read the last line first:

```text
NameError: name 'score' is not defined
```

This usually means the variable name is misspelled or used before assignment. The lines above it show the file and line number. Fix one error, run again, and repeat.
