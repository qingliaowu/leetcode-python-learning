# Lesson 3: Strings

[Run this lesson](./03_strings.py) | [Course home](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## Goal

Create text, read individual characters, take parts of a string, and use common string methods.

## Create a String

```python
word = "python"
empty = ""
```

A string is an ordered sequence of characters. An empty string contains zero characters.

## Indexes

Each character has a position called an index. The first index is `0`:

```text
character: p  y  t  h  o  n
index:     0  1  2  3  4  5
```

```python
word[0]   # "p"
word[2]   # "t"
word[-1]  # "n", the last character
```

Accessing an index outside the string causes `IndexError`.

## Length

`len` returns the number of characters:

```python
len("python")  # 6
len("")        # 0
```

The last valid positive index is `len(word) - 1`.

## Slices

A slice takes part of a string:

```python
word[start:stop]
```

It includes `start` but stops before `stop`:

```python
word[0:3]  # "pyt"
word[:2]   # "py"; start defaults to 0
word[2:]   # "thon"; stop defaults to the end
```

## Useful Methods

```python
"Python".lower()         # "python"
"python".upper()         # "PYTHON"
"  hello  ".strip()     # "hello"
"apple".startswith("app")  # True
```

Methods are functions attached to a value. The dot in `word.lower()` means "use the lower method belonging to this string."

## Split and Join

```python
sentence = "learn python today"
words = sentence.split()
# ["learn", "python", "today"]

new_sentence = " ".join(words)
# "learn python today"
```

`split` turns one string into a list. `join` turns a list of strings into one string.

A list is an ordered collection of values. Lists are the subject of Lesson 4.

## Formatted Strings

An f-string places values inside text:

```python
name = "Ada"
score = 10
message = f"{name} scored {score}"
```

The `f` before the opening quote activates `{...}` replacement.

## Strings Cannot Be Changed in Place

This causes an error:

```python
word = "cat"
word[0] = "b"
```

Create a new string instead:

```python
word = "b" + word[1:]  # "bat"
```

## Try It

For `text = "interview"`, predict:

```python
text[0]
text[-1]
text[0:5]
len(text)
```

<details>
<summary>Show answer and explanation</summary>

The answers are `"i"`, `"w"`, `"inter"`, and `9`.

- Index `0` is the first character.
- Index `-1` is the final character.
- Slice `0:5` includes indexes `0` through `4`; the stop index `5` is excluded.
- `interview` contains nine characters.

</details>

## Common Mistakes

- Starting indexes at `1` instead of `0`.
- Expecting the slice stop index to be included.
- Calling `split` when you need `join`, or the reverse.
- Forgetting the `f` before an f-string.
- Trying to change one string character directly.

## Remember

Strings are ordered and immutable. Indexes read one character. Slices read a range. String methods return useful new values.

---

[Previous: Lesson 2, Variables and Values](./02_variables_and_values.md) | [Next: Lesson 4, Lists and Tuples](./04_lists_and_tuples.md)
