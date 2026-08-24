# Lesson 7: Functions

[Run this lesson](./07_functions.py) | [Course home](./README.md)

## Goal

Give reusable code a name, send values into it, and receive a result.

## Define a Function

```python
def add(left, right):
    result = left + right
    return result
```

- `def` begins a function definition.
- `add` is the function name.
- `left` and `right` are parameters.
- The colon starts the indented function body.
- `return` sends a value back and ends the function call.

Defining a function does not run its body. Call it with parentheses:

```python
answer = add(2, 3)
```

`2` and `3` are arguments supplied to the parameters. `answer` becomes `5`.

## Return Is Not Print

```python
def add_and_print(a, b):
    print(a + b)

result = add_and_print(2, 3)
```

This displays `5`, but `result` is `None` because the function did not return a value.

LeetCode usually needs `return`, not `print`.

## Type Hints

```python
def add(left: int, right: int) -> int:
    return left + right
```

- `left: int` says `left` should be an integer.
- `-> int` says the function should return an integer.

Type hints explain intent to readers and tools. Python does not normally enforce them while running.

## Boolean Function

```python
def is_even(number: int) -> bool:
    return number % 2 == 0
```

The comparison already produces a boolean, so an extra `if` is unnecessary.

## Early Return

`return` stops the function immediately:

```python
def find_first_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return number
    return None
```

The final `return None` runs only if the loop finds no even number.

## Default Arguments

```python
def greet(name="friend"):
    return f"Hello, {name}!"

greet("Ada")  # "Hello, Ada!"
greet()       # "Hello, friend!"
```

Use immutable defaults such as numbers, strings, booleans, or `None`. Avoid a mutable default such as `items=[]` because one list would be shared across calls.

## Local Variables

A variable created inside a function is usually local to that function:

```python
def calculate():
    result = 10
    return result
```

Code outside cannot directly use this local `result`. This keeps functions independent.

## Try It

What does this return?

```python
def larger(a, b):
    if a > b:
        return a
    return b

larger(4, 7)
```

Answer: `7`.

## Common Mistakes

- Forgetting to call a function with parentheses.
- Printing when the caller needs a returned value.
- Writing code after an unconditional `return` and expecting it to run.
- Mixing up parameters in the definition and arguments in the call.
- Using a mutable list or dictionary as a default argument.
- Assuming type hints automatically reject a wrong type.

## Remember

A function has a name, parameters, a body, and usually a return value. Small functions make logic easier to test and explain.
