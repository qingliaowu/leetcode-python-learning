# 3. Longest Substring Without Repeating Characters

[LeetCode problem](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Python solution](./0003_longest_substring_without_repeating_characters.py)

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

- Time: `O(N)`. `right` visits every character once, and `left` only moves forward.
- Space: `O(U)`, where `U` is the number of distinct characters stored in the dictionary.

## Common Mistakes

- Confusing substring with subsequence.
- Moving `left` backward because of an old duplicate outside the window.
- Using `right - left` and forgetting the inclusive `+ 1`.
- Clearing the whole dictionary after a duplicate, which repeats work.
- Returning the best substring when the question asks for its length.

## Interview Explanation

> I maintain a sliding window with no duplicate characters. A map stores each character's latest index. When the current character already appears inside the window, I jump the left boundary past that occurrence. Each character is processed once, so the solution runs in linear time.
