# Lesson 2: Variables and Basic Values

[Run this lesson](./02_variables_and_values.py) | [Course home](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## Goal

Give values names, use basic data types, calculate numbers, and create true/false conditions.

## Variables

A variable is a name that refers to a value:

```python
score = 10
name = "Ada"
```

Read `score = 10` as "assign the value 10 to the name score." A single `=` assigns. It does not compare.

Names may contain letters, numbers, and underscores, but cannot start with a number:

```python
search_word = "mouse"  # clear Python style
item2 = "banana"       # allowed
```

## Basic Value Types

```python
count = 3           # int: whole number
price = 4.5         # float: decimal number
word = "apple"      # str: text
is_ready = True     # bool: True or False
answer = None       # no value yet
```

`True`, `False`, and `None` begin with capital letters.

You can ask Python for a value's type:

```python
print(type(3))        # <class 'int'>
print(type("apple"))  # <class 'str'>
```

## Arithmetic

| Code | Meaning | Result |
| --- | --- | ---: |
| `7 + 2` | Add | `9` |
| `7 - 2` | Subtract | `5` |
| `7 * 2` | Multiply | `14` |
| `7 / 2` | Regular division | `3.5` |
| `7 // 2` | Whole-number floor division | `3` |
| `7 % 2` | Remainder | `1` |
| `2 ** 3` | Power | `8` |

Binary search uses `//` to create a whole-number index. `% 2` is often used to check whether a number is even.

## Comparisons

Comparisons produce `True` or `False`:

| Code | Question |
| --- | --- |
| `a == b` | Are they equal? |
| `a != b` | Are they different? |
| `a < b` | Is `a` smaller? |
| `a <= b` | Is `a` smaller or equal? |
| `a > b` | Is `a` larger? |
| `a >= b` | Is `a` larger or equal? |

Remember: `=` assigns; `==` compares.

## Boolean Operators

```python
is_weekend = True
has_time = False

print(is_weekend and has_time)  # False: both must be True
print(is_weekend or has_time)   # True: at least one is True
print(not is_weekend)           # False: not reverses a boolean
```

## None

`None` means no value is present:

```python
result = None

if result is None:
    print("No result yet")
```

Use `is None` or `is not None` for this special value.

## Try It

What are the values?

```python
number = 11
is_even = number % 2 == 0
half = number // 2
```

Answer: `is_even` is `False`, and `half` is `5`.

## Common Mistakes

- Using `=` when you mean `==`.
- Writing lowercase `true`, `false`, or `none`.
- Expecting `7 / 2` to return a whole number.
- Using a variable before assigning it.
- Choosing unclear names such as `x1` when `left_index` would explain more.

## Remember

Variables name values. Every value has a type. Comparisons create booleans. `None` represents no value.
