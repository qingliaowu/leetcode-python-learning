# Lesson 0: Setup, Running Files, and Reading Errors

[Run this lesson](./00_setup_and_errors.py) | [Course home](./README.md) | [Python cheat sheet](../PYTHON_CHEAT_SHEET.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## Goal

Run one course file successfully and learn what to do when Python shows an
error. You do not need to understand the lesson script yet.

## 1. What You Need

This repository needs:

- Python `3.10` or newer,
- a terminal,
- a text editor or IDE,
- no external Python packages.

Why `3.10`? Some solutions use modern type hints such as:

```python
head: ListNode | None
```

The type hint means `head` may be a `ListNode` object or `None`. Lesson 7
explains type hints; for now, only the Python version matters.

Check your version.

macOS or Linux:

```bash
python3 --version
```

Windows PowerShell:

```powershell
py -3 --version
```

`Python 3.10`, `3.11`, `3.12`, or a later `3.x` version is suitable. If the
command is missing or the version is older, install a current Python 3 release
from [python.org](https://www.python.org/downloads/), then open a new terminal.

## 2. Terminal Command or Python Code?

A terminal command tells the computer what program to run:

```bash
python3 python_basics/00_setup_and_errors.py
```

Python code belongs inside a `.py` file:

```python
print("Hello")
```

Do not type `python3 python_basics/...` inside a Python file. Do not type
`print("Hello")` directly into a normal shell prompt unless you first opened the
interactive Python interpreter.

## 3. Find the Repository Root

The **repository root** is the folder containing these names:

```text
README.md
python_basics/
verify_solutions.py
```

In a terminal, `cd` means "change directory."

```bash
cd /path/to/leetcode-python-learning
```

On macOS or Linux, list the current folder with:

```bash
pwd
ls
```

In Windows PowerShell, use:

```powershell
Get-Location
Get-ChildItem
```

If you can see `README.md` and `python_basics`, you are in the right place.

## 4. Run the Setup Check

From the repository root, run one command.

macOS or Linux:

```bash
python3 python_basics/00_setup_and_errors.py
```

Windows PowerShell:

```powershell
py -3 python_basics/00_setup_and_errors.py
```

Expected output looks like this:

```text
Python 3.x detected.
Repository files found.
Tiny assertion passed.
Setup is ready. Continue to Lesson 1.
```

Your exact version replaces `3.x`.

## 5. What `assert` Success Looks Like

An assertion checks an expected fact:

```python
assert 2 + 3 == 5
```

When the assertion is true, Python normally prints nothing for that line. Silence
means the check passed. When it is false, Python raises `AssertionError`.

Course solution files use assertions as tiny repeatable tests. The final printed
message is friendly confirmation; the assertions do the actual checking.

## 6. Read a Traceback From the Bottom

Python errors usually include a **traceback**: a path showing where the error
happened. Start with the final line.

```text
Traceback (most recent call last):
  File "practice.py", line 4, in <module>
    print(values[3])
IndexError: list index out of range
```

Read it in this order:

1. `IndexError` is the error type.
2. `list index out of range` explains the immediate problem.
3. `practice.py`, line `4` tells you where to look.
4. `print(values[3])` is the line Python could not complete.

Then inspect the values and indexes used on that line.

## 7. Common Error Decoder

| Error | Plain-English Meaning | First Thing to Check |
| --- | --- | --- |
| `SyntaxError` | Python could not understand the code's shape | Missing quote, parenthesis, colon, or indentation |
| `IndentationError` | A block does not line up | Spaces before `if`, loop, function, or class code |
| `NameError` | A name does not exist yet | Spelling or use before assignment |
| `TypeError` | An operation received the wrong kind of value | Print or inspect each value's type |
| `IndexError` | A list/string index is outside its valid range | Length and boundary conditions |
| `KeyError` | A dictionary key is missing | Membership check or `.get(...)` |
| `AttributeError` | An object does not have that method or attribute | Object type and spelling |
| `AssertionError` | Actual behavior differed from the expected test | Inputs, returned value, and assumption |
| `ModuleNotFoundError` | Python cannot find an import | Import spelling and environment; this course needs no packages |

An error type is a category, not a verdict. It narrows the search.

## 8. The Five-Step Debugging Loop

Use the same small loop every time:

1. Reproduce the error with the smallest input you can.
2. Read the traceback's final line and reported code line.
3. State what each variable should mean at that line.
4. Print or trace the actual values just before the failure.
5. Change one cause, rerun, and keep the new test after it passes.

Do not change five unrelated lines at once. You would not know which change
fixed the problem.

## 9. When the Command Fails Before Python Starts

### "No such file" or "cannot open file"

You are probably in the wrong folder or typed the path incorrectly. Find the
repository root again and list its files.

### "command not found"

Try the command for your operating system. If neither `python3` nor `py -3`
works, install Python 3 and reopen the terminal.

### The terminal appears to wait forever

Press `Ctrl+C` once to interrupt the program. Look for a `while` loop that never
changes its condition or recursion that never reaches a base case.

## 10. A Calm Stuck Ladder

When you do not know what to do next, climb one rung at a time:

```text
Can I run Lesson 0?
    -> Can I run the current lesson's .py file?
        -> Can I explain the error's last line?
            -> Can I reproduce it with a tiny input?
                -> Can I state what each variable should mean?
```

Return to the first rung that is not yet true. That is the current problem.

## Check Your Understanding

### Question 1: Which Line Do You Read First?

A traceback is 12 lines long. The final line says:

```text
KeyError: 'apple'
```

What does it mean, and what should you inspect first?

<details>
<summary>Show answer and explanation</summary>

Python tried to read the key `'apple'` from a dictionary that did not contain
that key. Find the file and line shown immediately above the error, then inspect
the dictionary and the key used there.

If the key is optional, check membership first or use a suitable default:

```python
count = counts.get("apple", 0)
```

If the key should always exist, do not hide the error with a default. Find why
the earlier code failed to create it.

</details>

### Question 2: Why Can a Passing File Be Quiet?

You run a solution file and see no error. Several `assert` lines printed
nothing. Did those lines run?

<details>
<summary>Show answer and explanation</summary>

Yes. A true assertion is silent. Python only displays an assertion traceback
when the checked condition is false.

For example:

```python
assert 2 + 3 == 5  # runs and passes silently
```

In this repository, `python3 verify_solutions.py` runs every lesson in a fresh
process and prints an explicit `PASS` line for each file.

</details>

## Common Mistakes

- Running a command from a folder where its relative path does not exist.
- Reading only the first traceback line instead of the final error message.
- Treating silent assertions as skipped tests.
- Editing many lines before rerunning.
- Installing random packages even though this course uses only the standard
  library.

## Remember

Use Python 3.10 or newer. Run commands from the repository root. Read tracebacks
from the bottom, fix one cause, and rerun the smallest failing example.

---

Next: [Lesson 1, Your First Python Program](./01_first_program.md)
