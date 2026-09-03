# High-Priority Practical Coding Questions

[FDE track](./README.md) | [Supplemental syllabus](./07_genai_fde_syllabus_and_questions.md) | [Study plans](../INTERVIEW_STUDY_PLANS.md) | [Interview playbook](../INTERVIEW_PLAYBOOK.md) | [Progress tracker](../PROGRESS_TRACKER.md) | [Python data structures](../python_basics/12_python_data_structures.md)

## Purpose

These three questions are high-priority practice for a practical Python coding
interview. They emphasize lists, strings, dictionaries, sets, sorting, parsing,
and clean implementation under a no-autocomplete, no-compiler environment.

Practice each question as if it were live:

1. Restate the input and output.
2. Ask about edge cases and constraints.
3. Explain the data structures before coding.
4. Write clean Python without running it.
5. Dry-run the sample and at least two edge cases.
6. State time and space complexity.

## Priority Order

| Priority | Question | Main Skill | Target |
| --- | --- | --- | --- |
| High | [1. Filter Duplicates](#1-filter-duplicates) | Set membership while preserving order | 10-15 minutes |
| High | [2. Count Word Frequencies](#2-count-word-frequencies) | Dictionary counting plus sorted output | 15-20 minutes |
| High | [3. Merge Person Data](#3-merge-person-data) | Parsing, grouping, merging, and deterministic formatting | 25-35 minutes |

Do them in this order. The third problem combines the ideas from the first two
with string parsing and output formatting.

## 1. Filter Duplicates

### Function

```python
from typing import List

def filter_duplicates(data: List[int]) -> List[int]:
    ...
```

### Problem

You are given a list of integers, `data`.

Return a new list with duplicate values removed.

The original order must be preserved. If the same value appears multiple times,
keep only its first occurrence.

### Example

```text
Input:
[7, 6, 4, 3, 3, 4, 9]

Output:
[7, 6, 4, 3, 9]
```

### Constraints

- `data` is always defined.
- `data` does not contain undefined values.
- `data` may be empty.
- Values may be positive, negative, or zero.

### Clarifying Questions to Ask

- Should the output preserve the first occurrence order?
- Should duplicates be removed by exact integer equality?
- Can the input list be empty?
- Should the original list be modified or should I return a new list?

### Expected Direction

Use a set to remember values already seen and a list to store the result.

Target complexity:

- Time: `O(n)`, where `n` is the length of `data`.
- Extra space: `O(k)`, where `k` is the number of unique values.

### Edge Cases

- `[]` -> `[]`
- `[5]` -> `[5]`
- `[1, 1, 1]` -> `[1]`
- `[0, -1, 0, -1, 2]` -> `[0, -1, 2]`

### Follow-up

What would change if the interviewer asked you to keep the last occurrence
instead of the first occurrence?

## 2. Count Word Frequencies

### Function

```python
from typing import List

def count_frequencies(words: List[str]) -> List[int]:
    ...
```

### Problem

You are given a list of strings, `words`, representing tokenized text.

Count how many times each unique word appears.

Return a list of integers containing the frequencies of the unique words after
the unique words are sorted in alphabetical order.

All words contain only lowercase letters.

The number of integers returned must match the number of unique words.

### Example

```text
Input:
["the", "dog", "got", "the", "bone"]

Unique words in alphabetical order:
bone
dog
got
the

Frequencies:
bone -> 1
dog  -> 1
got  -> 1
the  -> 2

Output:
[1, 1, 1, 2]
```

### Constraints

- `words` is always defined.
- `words` may be empty.
- Every word contains only lowercase English letters.
- Sorting should use normal lexicographic order.

### Clarifying Questions to Ask

- Should the output include only counts, or should it include the words too?
- Should words be sorted alphabetically before producing the counts?
- Are words case-sensitive?
- Can the list be empty?

### Expected Direction

Use a dictionary to count each word, then iterate over the sorted dictionary
keys to build the output counts.

Target complexity:

- Time: `O(n + k log k)`, where `n` is the number of words and `k` is the number
  of unique words.
- Extra space: `O(k)`.

### Edge Cases

- `[]` -> `[]`
- `["a"]` -> `[1]`
- `["a", "a", "a"]` -> `[3]`
- `["b", "a", "b", "c", "a"]` -> `[2, 2, 1]`

### Follow-up

What would change if the interviewer asked for pairs like
`[["bone", 1], ["dog", 1], ["got", 1], ["the", 2]]` instead of only counts?

## 3. Merge Person Data

### Function

```python
from typing import List

def merge_data(data_strings: List[str]) -> List[str]:
    ...
```

### Problem

You are given a list of strings, `data_strings`.

Each string contains information about one person in this format:

```text
Key=Value;Key=Value;Key=Value
```

Every string contains a `Name` field. A person is uniquely identified by the
value of the `Name` field.

If multiple strings have the same `Name`, they describe the same person. Merge
all information for that person into one output string.

The same field may appear more than once, but conflicting information will not
be provided.

### Input Format Rules

- Fields are separated by `;`.
- Each field is split into a key and value by `=`.
- Every input string contains a `Name` field.
- Empty names, empty keys, and empty values do not appear.
- Keys and values may contain printable ASCII characters except `=` and `;`.
- Input strings do not contain `\r` or `\n`.

### Required Output

Return one string per person.

The output must follow these rules:

- Sort people alphabetically by `Name`.
- In each person's output string, place the `Name` field first.
- Sort all fields except `Name` alphabetically by key.
- Join fields with `;`.
- The input data is not guaranteed to already be in this order.

### Example

```text
Input:
[
    "Name=John;Age=15;Likes=Apples",
    "Name=Mary;Age=16;Likes=Baked potatoes;Team=Basketball",
    "Name=Adam;Age=17;Score=133;Likes=Jellied eels",
    "Name=John;Score=283.5;City=NYC"
]

Output:
[
    "Name=Adam;Age=17;Likes=Jellied eels;Score=133",
    "Name=John;Age=15;City=NYC;Likes=Apples;Score=283.5",
    "Name=Mary;Age=16;Likes=Baked potatoes;Team=Basketball"
]
```

### Constraints

- `data_strings` contains at most 100 strings.
- Each input string has length at most 10,000.
- Each output string has length at most 10,000.
- Empty `Name`, key, and value fields do not appear.
- Conflicting values for the same person's same key do not appear.

### Clarifying Questions to Ask

- Is `Name` the only identity key?
- Can the same key appear multiple times for the same person with the same value?
- Should conflicting values be ignored, overwritten, or treated as invalid?
- Should output people and fields be sorted exactly as specified?
- Can keys or values contain spaces?

### Expected Direction

Parse each record into key-value pairs. Use a dictionary from person name to
that person's merged field dictionary. After all records are processed, build
the output in sorted name order.

Target complexity:

- Time: `O(total_chars + p log p + f log f)`, where `p` is the number of people
  and `f` is the total number of field keys sorted across people.
- Extra space: `O(total_fields)`.

### Edge Cases

- One person with one field: `["Name=Ana"]`
- One person split across many records.
- Fields repeated with the same value.
- Input records already sorted versus completely shuffled.
- Values containing spaces, such as `Likes=Baked potatoes`.

### Follow-up

What would change if conflicting values could appear and the function had to
return an error instead of silently choosing one?

## Final Drill

After solving all three, explain the shared pattern:

```text
Use a dictionary or set to remember what has already appeared, then produce a
deterministic output order only when the problem requires it.
```

If you can solve these without running code, you are much closer to the live
coding environment described in the GenAI FDE prep material.

## Check Your Understanding

Try each question before opening its answer. Say the data structure, invariant,
complexity, and one edge case aloud.

### Question 1: Pick the Data Structure

For each of the three problems, what is the main dictionary or set state you
would maintain while scanning the input?

<details>
<summary>Show answer and explanation</summary>

For `Filter Duplicates`, keep a `seen` set and a `result` list. The invariant is
that `seen` contains every value already added to `result`.

For `Count Word Frequencies`, keep a `counts` dictionary from word to count. The
invariant is that after scanning the first `i` words, `counts` stores the exact
frequency for those words.

For `Merge Person Data`, keep a dictionary from person name to that person's
merged field dictionary. The invariant is that each person's dictionary contains
all non-conflicting fields seen so far for that `Name`.

</details>

### Question 2: Explain the Output Order

Which of the three problems requires sorting, and where does the sorting happen?

<details>
<summary>Show answer and explanation</summary>

`Filter Duplicates` does not sort because it must preserve first occurrence
order.

`Count Word Frequencies` sorts the unique words alphabetically after counting,
then returns counts in that sorted word order.

`Merge Person Data` sorts people by `Name`, places `Name` first inside each
output string, and sorts all other field keys alphabetically before joining the
fields.

</details>
