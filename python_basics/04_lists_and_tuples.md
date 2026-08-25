# Lesson 4: Lists and Tuples

[Run this lesson](./04_lists_and_tuples.py) | [Course home](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## Goal

Store several ordered values, read them by index, and understand which collections can change.

## Lists

A list stores values in order:

```python
numbers = [10, 20, 30]
names = ["Ada", "Grace"]
empty = []
```

A list may contain any value type. In interview problems, lists usually contain values of one type.

## Read and Change Items

Lists use the same zero-based indexes and slices as strings:

```python
numbers[0]     # 10
numbers[-1]    # 30
numbers[0:2]   # [10, 20]
```

Unlike strings, lists are mutable, meaning they can change:

```python
numbers[1] = 25
# [10, 25, 30]
```

## Add and Remove

```python
numbers.append(40)  # add one item at the end
last = numbers.pop()  # remove and return the last item
```

`append` and `pop()` at the end are commonly used to make a stack.

## Length and Membership

```python
len(numbers)       # number of items
20 in numbers      # True or False
99 not in numbers  # True or False
```

List membership may scan many items. A dictionary or set is usually faster for repeated lookups.

## Sorting

These operations are different:

```python
values = [3, 1, 2]

new_values = sorted(values)
# values is still [3, 1, 2]
# new_values is [1, 2, 3]

values.sort()
# values itself is now [1, 2, 3]
```

`sorted` returns a new list. `.sort()` changes the existing list and returns `None`.

## Tuples

A tuple is ordered but cannot be changed:

```python
point = (4, 7)
point[0]  # 4
```

Tuples are useful for fixed groups such as `(row, column)` or heap entries.

Tuple unpacking gives each item a name:

```python
row, column = (2, 5)
```

Because tuples cannot change, they can be dictionary keys. Lists cannot.

## Copying a List

```python
first = [1, 2]
same_list = first
copy = first.copy()

first.append(3)
```

`same_list` also sees the new `3` because both names refer to one list. `copy` remains `[1, 2]`.

## Try It

What is left in `stack`?

```python
stack = []
stack.append("a")
stack.append("b")
item = stack.pop()
```

<details>
<summary>Show answer and explanation</summary>

`item` is `"b"`, and `stack` is `["a"]`.

The two appends place `"a"` and then `"b"` at the list's end. `pop()` removes
and returns the final item, which is why a list works as a last-in-first-out
stack.

</details>

## Common Mistakes

- Accessing index `len(items)`, which is one past the last valid index.
- Expecting `.sort()` to return the sorted list.
- Confusing `append(value)` with adding every item from another list.
- Using a list as a dictionary key.
- Writing `copy = original` and expecting two independent lists.

## Remember

Lists are ordered and mutable. Tuples are ordered and immutable. Both use zero-based indexes.

---

[Previous: Lesson 3, Strings](./03_strings.md) | [Next: Lesson 5, Dictionaries and Sets](./05_dictionaries_and_sets.md)
