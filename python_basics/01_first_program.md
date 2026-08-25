# Lesson 1: Your First Python Program

[Run this lesson](./01_first_program.py) | [Course home](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## Goal

Learn what a Python file is, run it, and display information.

## A Python File

A Python file is a text file ending in `.py`. Python reads it from top to bottom.

```python
print("Hello, Python!")
print(2 + 3)
```

`print(...)` is a function. A function performs a task. Here, its task is displaying a value.

- `print` is the function name.
- `(` and `)` surround the value sent to the function.
- `"Hello, Python!"` is text, also called a string.
- `2 + 3` is calculated before it is printed.

Expected output:

```text
Hello, Python!
5
```

## Run the File

From the repository root:

```bash
python3 python_basics/01_first_program.py
```

`python3` starts Python 3. The path after it tells Python which file to run.

## Quotes

Text needs matching quotes:

```python
print("apple")
print('banana')
```

Single and double quotes both work. This course usually uses double quotes. Do not mix the opening and closing quote.

## Comments

A comment begins with `#`. Python ignores everything after it on that line:

```python
# This explains the next line.
print("Visible")  # This comment is also ignored.
```

Comments should explain something useful. They are not printed.

## Multiple Values

A comma separates values passed to `print`:

```python
print("Score:", 10)
```

Output:

```text
Score: 10
```

Python adds a space between the values.

## Your First Check

`assert` checks whether something is true:

```python
assert 2 + 3 == 5
```

If it is true, nothing happens. If it is false, Python shows an `AssertionError`. The double equals sign `==` asks "are these equal?"

## Try It

Before running, predict the output:

```python
print("LeetCode", 1 + 2)
print(10 - 4)
```

<details>
<summary>Show answer and explanation</summary>

```text
LeetCode 3
6
```

Python evaluates each arithmetic expression before `print` displays it. The
comma in the first call separates two displayed values, so Python places a
space between `LeetCode` and `3`.

</details>

## Common Mistakes

- Forgetting a closing quote or parenthesis.
- Writing `Print` instead of `print`; Python names are case-sensitive.
- Running the command from the wrong folder.
- Expecting comments to appear in the output.

## Remember

Python runs from top to bottom. `print` displays a value. `#` starts a comment. `assert` checks an expected result.

---

[Previous: Lesson 0, Setup and Errors](./00_setup_and_errors.md) | [Next: Lesson 2, Variables and Values](./02_variables_and_values.md)
