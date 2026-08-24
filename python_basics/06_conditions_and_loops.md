# Lesson 6: Conditions and Loops

[Run this lesson](./06_conditions_and_loops.py) | [Course home](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## Goal

Make decisions with `if` and repeat work with `for` and `while`.

## Indentation

Python uses indentation to show which lines belong together:

```python
if score >= 80:
    print("Passed")
    print("Good work")

print("Finished")
```

The two indented lines run only when the condition is true. `print("Finished")` is outside the block and always runs.

Use four spaces for each indentation level. The colon `:` starts a block.

## If, Elif, and Else

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
```

Python checks from top to bottom and runs the first matching block.

- `if` checks the first condition.
- `elif` means "else if" and checks another condition.
- `else` handles everything not already matched.

## Truthy and Falsy Values

These values behave like `False` in a condition:

```python
False
None
0
""
[]
{}
set()
```

Most other values behave like `True`. This lets you write:

```python
if numbers:
    print("The list is not empty")
```

## For Loops

A `for` loop visits each item:

```python
for number in [10, 20, 30]:
    print(number)
```

The variable `number` receives one list item on every repetition.

Strings are also sequences:

```python
for character in "cat":
    print(character)
```

## Range

`range` creates a sequence of integers:

```python
range(4)       # 0, 1, 2, 3
range(2, 5)    # 2, 3, 4
```

The stop value is not included. Use indexes when you need positions:

```python
for index in range(len(numbers)):
    print(index, numbers[index])
```

## Enumerate

`enumerate` is clearer when you need both index and value:

```python
for index, number in enumerate(numbers):
    print(index, number)
```

It produces pairs such as `(0, first_value)` and unpacks each pair into two variables.

## While Loops

A `while` loop repeats while a condition remains true:

```python
count = 3

while count > 0:
    print(count)
    count -= 1
```

Always make progress toward making the condition false. Otherwise, the loop can run forever.

## Continue and Break

```python
for number in [1, 2, 3, 4]:
    if number == 2:
        continue  # skip the rest of this repetition
    if number == 4:
        break     # stop the whole loop
    print(number)
```

This prints `1` and `3`.

## Try It

What is `total`?

```python
total = 0
for number in [2, 4, 6]:
    if number > 2:
        total += number
```

Answer: `10`, because only `4` and `6` are added.

## Common Mistakes

- Forgetting the colon after `if`, `for`, or `while`.
- Mixing indentation widths.
- Expecting the stop value from `range` to be included.
- Changing a list while looping through it without planning carefully.
- Writing a `while` loop whose condition never becomes false.
- Using `break` when you only mean to skip one item.

## Remember

Conditions choose a path. `for` visits items. `while` repeats based on a condition. Indentation defines every block.
