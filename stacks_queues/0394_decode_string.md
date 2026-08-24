# 394. Decode String

[LeetCode problem](https://leetcode.com/problems/decode-string/) | [Python solution](./0394_decode_string.py) | [Topic guide](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## What the Question Asks

Decode strings written as:

```text
count[encoded_text]
```

Repeat the bracketed text `count` times. Patterns can be nested.

```text
3[a]       -> aaa
2[ab]      -> abab
3[a2[c]]   -> accaccacc
```

The input is valid, so brackets and counts are correctly formed.

## Why a Stack Fits

When `[` begins an inner pattern, the outer text is not finished. It must pause until the matching `]` completes the inner text.

With nested brackets, the most recently paused pattern finishes first. That is exactly last-in-first-out stack behavior.

## State While Reading

The solution maintains:

- `current_characters`: decoded characters for the current bracket level,
- `repeat_count`: the number being read before `[`,
- `stack`: paused outer character lists and their repeat counts.

Each stack item is:

```python
(previous_characters, saved_count)
```

## Four Character Cases

### 1. A digit

Build the repeat number:

```python
repeat_count = repeat_count * 10 + int(character)
```

For `12`:

```text
read 1 -> 0 * 10 + 1 = 1
read 2 -> 1 * 10 + 2 = 12
```

Using only `repeat_count = int(character)` would incorrectly read `12` as `2`.

### 2. An opening bracket

Save the outer work:

```python
stack.append((current_characters, repeat_count))
current_characters = []
repeat_count = 0
```

The empty list begins decoding the bracket's inner text.

### 3. A closing bracket

The inner text is complete:

```python
previous_characters, saved_count = stack.pop()
current_characters = (
    previous_characters + current_characters * saved_count
)
```

Repeat the inner characters and attach them to the paused outer characters.

### 4. A letter

```python
current_characters.append(character)
```

The letter belongs to the current bracket level.

## Dry Run: `3[a2[c]]`

| Read | Action | Current | Stack idea |
| --- | --- | --- | --- |
| `3` | Build count 3 | `""` | empty |
| `[` | Save outer and 3 | `""` | `[("", 3)]` |
| `a` | Append letter | `"a"` | unchanged |
| `2` | Build count 2 | `"a"` | unchanged |
| `[` | Save `"a"` and 2 | `""` | outer 3, then `"a"` 2 |
| `c` | Append letter | `"c"` | unchanged |
| `]` | Pop and expand | `"acc"` | outer 3 remains |
| `]` | Pop and expand | `"accaccacc"` | empty |

Return the joined current characters.

## Python Used Here

```python
character.isdigit()
```

This string method returns whether the character is a digit.

```python
int(character)
```

This converts a digit string such as `"7"` to integer `7`.

```python
current_characters * saved_count
```

Multiplying a list repeats its items. Adding lists creates one combined list.

## Why It Is Correct

Before every opening bracket, the stack saves exactly the state needed after its matching closing bracket. Because nested brackets close in reverse opening order, stack pop retrieves the correct outer state. Every closing bracket repeats its fully decoded inner text before returning to the outer level.

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

Let:

- `N` be encoded input length,
- `D` be final decoded length,
- `H` be maximum nesting depth.

The input is read once, and the decoded output must be created. A common interview summary is `O(N + D)` time. In Python, closing nested levels can copy intermediate character lists more than once, so a safe worst-case bound for this implementation is `O(N + D * H)`.

Space is `O(N + D)` for paused stack buffers and decoded characters. The final output itself already requires `O(D)` space.

State which interpretation you are using. For most interviews, emphasizing that work and memory must include decoded output size is the important point.

## Edge Cases

- Text with no encoded section stays unchanged.
- Multi-digit repeat counts such as `10[a]`.
- Several encoded sections next to each other.
- Letters before or after a bracketed section.
- Deeply nested patterns.
- Count `1` still follows the same logic.

## Common Mistakes

- Reading only one digit of a multi-digit count.
- Saving the inner text instead of the outer text at `[`.
- Forgetting to reset current characters and repeat count after `[`.
- Using a queue when the newest nested level must finish first.
- Appending expanded text in the wrong order.
- Analyzing complexity using only encoded length while ignoring a much larger decoded output.

## Possible Follow-up Questions

| Follow-up | Answer Direction |
| --- | --- |
| What if the encoded input may be invalid? | Detect missing counts, unmatched brackets, illegal characters, and leftover stack entries; return an error instead of assuming validity. |
| What if decoded output is too large for memory? | Produce characters incrementally with an iterator or writer, though nested repeats still require storing or replaying inner sections. |
| Support escaped brackets such as `\[` as literal text. | Add an escape state so the character after `\` is appended without being treated as syntax. |
| Can you solve it recursively? | Write a parser that decodes one bracket level and returns both its text and the next unread index. Recursion depth becomes nesting depth. |

## Interview Explanation

> I scan once and use a stack for paused outer states. Digits build a possibly multi-digit repeat count. At `[`, I save the current characters and count, then start a fresh inner buffer. At `]`, I pop the outer state, repeat the completed inner text, and combine them. The stack correctly handles nested brackets because the latest opened level closes first.

## Test Aloud

```text
For 3[a2[c]], the inner 2[c] becomes cc, so the current level becomes acc.
The outer count then repeats acc three times, producing accaccacc.
```

## Check Your Understanding

Try each question before opening its answer. Write down the stack whenever a bracket opens or closes.

### Question 1: Decode a Nested String

What does `2[ab3[c]]x` decode to? Which section is completed first?

<details>
<summary>Show answer and explanation</summary>

**Answer:** `abcccabcccx`.

The innermost section closes first: `3[c]` becomes `ccc`. Its surrounding level is now `abccc`. The outer count repeats that whole section twice, producing `abcccabccc`, and the final literal `x` is appended.

This inside-out order is exactly why a stack fits nested brackets: the most recently opened unfinished level is the first one completed.

**Complexity:** It is commonly described as `O(N + D)` time for encoded length `N` and decoded length `D`. With repeated rebuilding across `H` nested levels, `O(N + D * H)` is a safer worst-case bound for this implementation. Space is `O(N + D)`.

**Edge case:** Repeat counts may have more than one digit, as in `12[a]`.

</details>

### Question 2: Validate Brackets

Return `True` when a string containing only `()[]{}` has correctly matched and nested brackets.

<details>
<summary>Show answer and detailed solution</summary>

```python
def has_valid_brackets(text: str) -> bool:
    matching_open = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    stack = []

    for character in text:
        if character in "([{":
            stack.append(character)
        else:
            if not stack or stack[-1] != matching_open[character]:
                return False
            stack.pop()

    return not stack
```

Opening brackets are unfinished work, so they are pushed. A closing bracket must match the latest unfinished opener at the top. An empty stack on closing means there is no opener; a non-empty stack after scanning means some openers never closed.

**Complexity:** `O(N)` time and `O(N)` extra space in the worst case.

**Tests:** `"([]){}"` is valid, `"([)]"` is invalid, and the empty string is valid.

</details>
