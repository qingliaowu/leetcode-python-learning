# 49. Group Anagrams

[LeetCode problem](https://leetcode.com/problems/group-anagrams/) | [Python solution](./0049_group_anagrams.py)

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

## Interview Explanation

> Anagrams become identical when their characters are sorted. I use that immutable sorted tuple as a hash-map key and append each original word to the corresponding list. The solution is dominated by sorting each word, giving `O(N * K log K)` time.
