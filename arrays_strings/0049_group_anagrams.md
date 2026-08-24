# 49. Group Anagrams

[LeetCode problem](https://leetcode.com/problems/group-anagrams/) | [Python solution](./0049_group_anagrams.py) | [Topic guide](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## What the Question Asks

Anagrams use the same characters the same number of times, but possibly in a different order. Group all anagrams together.

```text
["eat", "tea", "tan", "ate", "nat", "bat"]
->
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

The order of groups and words inside groups does not matter.

## Python Used Here

`sorted(word)` returns a new list of sorted characters:

```python
sorted("tea")  # ["a", "e", "t"]
```

A list cannot be a dictionary key because it can change. A tuple is ordered like a list but cannot be changed, so it can be a key:

```python
key = tuple(sorted("tea"))
# ("a", "e", "t")
```

`list(groups.values())` gets all dictionary values and turns the result into a normal list.

## Main Idea

All words in one anagram group have the same sorted characters:

```text
eat -> aet
tea -> aet
ate -> aet
```

Use the sorted character tuple as a dictionary key. The dictionary value is a list of original words with that key.

## Step-by-Step Approach

1. Create an empty `groups` dictionary.
2. For each word, sort its characters and convert them to a tuple.
3. Create an empty list when this key appears for the first time.
4. Append the original word to that key's list.
5. Return all dictionary values.

Keep the original word in the output. The sorted form is only an internal grouping key.

## Dry Run

| Word | Key | Groups after insertion |
| --- | --- | --- |
| `eat` | `(a, e, t)` | `{(a,e,t): [eat]}` |
| `tea` | `(a, e, t)` | `{(a,e,t): [eat, tea]}` |
| `tan` | `(a, n, t)` | Add a second group |
| `ate` | `(a, e, t)` | Append to the first group |

An empty string has an empty tuple key `()`, so empty strings correctly group together.

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

Let `N` be the number of words and `K` the maximum word length.

- Sorting one word costs `O(K log K)`.
- Total time is `O(N * K log K)`.
- Space is `O(N * K)` for keys and grouped words.

A character-count key can reduce sorting work to `O(N * K)`, but the sorted-key solution is often the clearest first interview solution.

## Common Mistakes

- Using the sorted list directly as a dictionary key; lists are unhashable.
- Returning sorted words instead of the original words.
- Making one list and accidentally sharing it between every group.
- Assuming the output group order must match one exact arrangement.

## Possible Follow-up Questions

| Follow-up | Answer Direction |
| --- | --- |
| Can you avoid sorting every word? | For lowercase English letters, use a 26-number character-count tuple as the key. This changes time to `O(N * K)`. |
| What if words contain Unicode characters? | Sorting remains simple, or build a sorted tuple of `(character, count)` pairs rather than assuming 26 letters. |
| What if output groups must be sorted? | Sort words inside each group and then sort groups by the required rule, adding sorting cost. |
| Can groups be produced from a stream? | Update the grouping dictionary as words arrive, but complete groups cannot be finalized until the stream ends unless later updates are allowed. |

## Interview Explanation

> Anagrams become identical when their characters are sorted. I use that immutable sorted tuple as a hash-map key and append each original word to the corresponding list. The solution is dominated by sorting each word, giving `O(N * K log K)` time.

## Check Your Understanding

Try each question before opening its answer. Say the approach, complexity, and one edge case aloud.

### Question 1: Build the Groups

Ignoring the order of groups, what groups should be produced from `['eat', 'tea', 'tan', 'ate', 'nat', 'bat']`? What key does `"tea"` use?

<details>
<summary>Show answer and explanation</summary>

**Answer:** The groups are `['eat', 'tea', 'ate']`, `['tan', 'nat']`, and `['bat']`.

Sorting `"tea"` produces the characters `['a', 'e', 't']`. A list cannot be a dictionary key, so the implementation uses the tuple `('a', 'e', 't')`. The words `"eat"` and `"ate"` produce the same key and therefore enter the same list.

The exact order of groups normally does not matter unless the problem explicitly requires one.

**Complexity:** For `N` words of maximum length `K`, sorting keys takes `O(N * K log K)` time. The groups and keys use `O(N * K)` space.

**Edge case:** Empty strings are anagrams of one another because each has the same empty key.

</details>

### Question 2: Check Two Words

Write a function that decides whether two lowercase or Unicode strings are anagrams without sorting them.

<details>
<summary>Show answer and detailed solution</summary>

```python
def are_anagrams(first: str, second: str) -> bool:
    if len(first) != len(second):
        return False

    counts: dict[str, int] = {}

    for character in first:
        counts[character] = counts.get(character, 0) + 1

    for character in second:
        if character not in counts:
            return False
        counts[character] -= 1
        if counts[character] == 0:
            del counts[character]

    return not counts
```

The first loop records how many copies of every character are required. The second loop removes those requirements. A missing character fails immediately. Deleting zero counts makes an empty dictionary mean that every required character was matched exactly.

**Complexity:** `O(A + B)` average time and `O(U)` extra space, where `U` is the number of distinct characters.

**Tests:** `are_anagrams("listen", "silent")` is `True`; `are_anagrams("rat", "car")` is `False`.

</details>
