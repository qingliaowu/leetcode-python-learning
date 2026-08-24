# 3. Longest Substring Without Repeating Characters

[LeetCode problem](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Python solution](./0003_longest_substring_without_repeating_characters.py) | [Topic guide](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## What the Question Asks

Return the length of the longest continuous substring containing no repeated character.

- A substring is continuous. Characters cannot be skipped.
- Return a length, not the substring itself.

For `"pwwkew"`, the answer is `3` from `"wke"` (or `"kew"`). `"pwke"` is not a substring because its characters are not continuous.

## Python Used Here

```python
for right, char in enumerate(s):
```

`right` is the current character index and `char` is the character.

```python
best_length = max(best_length, window_length)
```

`max(a, b)` returns the larger value.

The expression `right - left + 1` gives an inclusive window length. For indexes `2` through `4`, the length is `4 - 2 + 1 = 3`.

## Sliding Window Idea

Use two indexes to describe a current valid substring:

```text
s[left : right + 1]
```

`right` moves forward one step on every loop. When a duplicate enters the window, move `left` just past the previous copy.

The dictionary `last_seen` maps each character to its most recent index. This lets `left` jump directly instead of moving one step at a time.

## Step-by-Step Approach

1. Start `left = 0`, `best_length = 0`, and an empty `last_seen` dictionary.
2. Move `right` across the string.
3. If the current character was seen inside the current window, move `left` to one index after that old occurrence.
4. Record the character's new index.
5. Calculate the current window length.
6. Update the best length.

The check `last_seen[char] >= left` matters. An old occurrence before `left` is already outside the window and should not move `left` backward.

## Dry Run: `abba`

| Right | Character | Left before | Action | Window | Best |
| ---: | --- | ---: | --- | --- | ---: |
| 0 | `a` | 0 | Save `a:0` | `a` | 1 |
| 1 | `b` | 0 | Save `b:1` | `ab` | 2 |
| 2 | `b` | 0 | Move left to 2 | `b` | 2 |
| 3 | `a` | 2 | Old `a` is before left; do not move | `ba` | 2 |

Without the `>= left` condition, the last step would incorrectly move `left` backward from `2` to `1`.

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

- Time: `O(N)`. `right` visits every character once, and `left` only moves forward.
- Space: `O(U)`, where `U` is the number of distinct characters stored in the dictionary.

## Common Mistakes

- Confusing substring with subsequence.
- Moving `left` backward because of an old duplicate outside the window.
- Using `right - left` and forgetting the inclusive `+ 1`.
- Clearing the whole dictionary after a duplicate, which repeats work.
- Returning the best substring when the question asks for its length.

## Possible Follow-up Questions

| Follow-up | Answer Direction |
| --- | --- |
| Return the substring instead of only its length. | Save `best_start` whenever a longer window is found, then return `s[best_start:best_start + best_length]`. |
| Find the longest substring with at most `K` distinct characters. | Store character frequencies and shrink the left side while the map has more than `K` keys. |
| Can the input arrive as a stream? | Keep the latest index map, left boundary, current index, and best length. The full text is unnecessary when only length is required. |
| What if characters are Unicode? | The dictionary-based algorithm already works because Python string iteration produces Unicode characters. Clarify whether normalization or case folding is required. |

## Interview Explanation

> I maintain a sliding window with no duplicate characters. A map stores each character's latest index. When the current character already appears inside the window, I jump the left boundary past that occurrence. Each character is processed once, so the solution runs in linear time.

## Check Your Understanding

Try each question before opening its answer. Say the approach, complexity, and one edge case aloud.

### Question 1: Trace `abba`

What answer should the algorithm return for `s = "abba"`? When it reads the final `a`, should the left boundary move backward?

<details>
<summary>Show answer and explanation</summary>

**Answer:** The longest length is `2`, from either `"ab"` or `"ba"`. The left boundary must never move backward.

After reading the second `b`, the window moves past the earlier `b`, so `left` becomes `2`. The final `a` was last seen at index `0`, which is outside the current window. Moving `left` to `1` would incorrectly make the window larger by including duplicate `b` values.

The safe update is:

```python
left = max(left, last_seen[character] + 1)
```

**Complexity:** `O(N)` time and up to `O(U)` extra space, where `U` is the number of distinct characters.

**Edge case:** The empty string has answer `0`.

</details>

### Question 2: At Most Two Distinct Characters

Find the length of the longest substring containing at most two distinct characters. For example, `"eceba"` should return `3` for `"ece"`.

<details>
<summary>Show answer and detailed solution</summary>

```python
def longest_with_at_most_two_distinct(s: str) -> int:
    counts: dict[str, int] = {}
    left = 0
    best = 0

    for right, character in enumerate(s):
        counts[character] = counts.get(character, 0) + 1

        while len(counts) > 2:
            left_character = s[left]
            counts[left_character] -= 1
            if counts[left_character] == 0:
                del counts[left_character]
            left += 1

        best = max(best, right - left + 1)

    return best
```

The window may contain repeated characters, so the map stores counts rather than only latest indexes. When a third distinct character enters, the left side shrinks until only two dictionary keys remain. After that repair, the window is valid and can update `best`.

Each character enters the window once and leaves at most once.

**Complexity:** `O(N)` time and `O(U)` extra space; because this version keeps at most two keys, its working map is `O(1)`.

**Tests:** `"eceba"` returns `3`, `"aaaa"` returns `4`, and `""` returns `0`.

</details>
