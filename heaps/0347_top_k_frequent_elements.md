# 347. Top K Frequent Elements

[LeetCode problem](https://leetcode.com/problems/top-k-frequent-elements/) | [Python solution](./0347_top_k_frequent_elements.py)

## What the Question Asks

Return the `k` distinct values that occur most often. The answer order does not matter.

```text
nums = [1, 1, 1, 2, 2, 3], k = 2
frequencies: 1 -> 3, 2 -> 2, 3 -> 1
answer: [1, 2]
```

## Python Used Here

Count with a dictionary:

```python
frequencies[number] = frequencies.get(number, 0) + 1
```

`get(number, 0)` returns the current count or zero when the number has not appeared before.

Loop over keys and values together:

```python
for number, frequency in frequencies.items():
```

A list comprehension builds the answer:

```python
[number for frequency, number in min_heap]
```

It loops through each tuple, unpacks it, and keeps only `number`.

## Why Heap Tuples Work

Store `(frequency, number)` in the min-heap. Python compares tuple items from left to right, so frequency controls heap priority. The number only breaks a frequency tie.

Keep the heap at size `k`. When a new pair makes it too large, remove the smallest frequency. The remaining pairs represent the most frequent values seen so far.

## Step-by-Step Approach

1. Count every value in a frequency dictionary.
2. Create an empty min-heap.
3. Push each `(frequency, number)` pair.
4. Pop when heap size exceeds `k`.
5. Extract and return the numbers from the remaining pairs.

The final heap order is not the answer ranking order, but the problem allows any output order.

## Dry Run

For frequencies `{1: 3, 2: 2, 3: 1}` and `k = 2`:

- Push `(3, 1)`.
- Push `(2, 2)`. Two items are allowed.
- Push `(1, 3)`. Size is now three, so pop the smallest frequency `(1, 3)`.
- Values `1` and `2` remain.

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

Let `N` be input length and `U` be unique values.

- Counting: `O(N)`.
- Heap work: `O(U log K)`.
- Total time: `O(N log K)` as a simple upper bound because `U <= N`.
- Space: `O(U + K)`.

## Common Mistakes

- Pushing raw numbers instead of `(frequency, number)` pairs.
- Keeping the least frequent `k` values by reversing the pop logic.
- Counting distinct values only once.
- Requiring a specific answer order when the problem does not.
- Sorting all unique values without discussing the higher `O(U log U)` cost.

## Possible Follow-up Questions

| Follow-up | Answer Direction |
| --- | --- |
| Can you improve beyond `O(U log K)` heap work? | Use frequency buckets indexed from `1` through `N`, then scan buckets backward for `O(N)` total time. |
| Values arrive continuously. | Maintain counts and update ranking structures; exact top-k updates are more complex because frequencies change repeatedly. |
| The stream is too large for exact counts. | Discuss approximate heavy-hitter algorithms such as Count-Min Sketch, with an accuracy-memory tradeoff. |
| Return results in frequency order. | Sort the final `K` pairs or pop them and reverse the order, adding `O(K log K)`. |
| Frequencies tie at the boundary. | Clarify whether any `K` values are accepted or whether a deterministic value-based tie rule is required. |

## Interview Explanation

> First I count values with a hash map. Then I keep a min-heap of at most `k` `(frequency, value)` pairs. If the heap grows too large, I remove its smallest frequency. The remaining values are the top `k`, using `O(N log K)` time.

## Check Your Understanding

Try each question before opening its answer. Separate the counting phase from the selection phase.

### Question 1: Count Before Selecting

For `nums = [1, 1, 1, 2, 2, 3]` and `k = 2`, which values are returned? What frequency pairs are compared?

<details>
<summary>Show answer and explanation</summary>

**Answer:** Values `1` and `2` are returned, in either order unless sorted output is requested.

The frequency map is `{1: 3, 2: 2, 3: 1}`. Selection compares `(3, 1)`, `(2, 2)`, and `(1, 3)` conceptually, where frequency is the priority. A size-`2` min-heap discards the pair with frequency `1` and keeps the two higher frequencies.

Counting occurrences and finding the largest values are separate jobs. Pushing each raw occurrence would do unnecessary heap work.

**Complexity:** `O(N log K)` time with the heap approach and `O(U + K)` extra space for `U` unique values.

**Edge case:** Ask how ties should be handled when several values have the same boundary frequency.

</details>

### Question 2: Solve With Frequency Buckets

Assume `1 <= k <= number of unique values`. Return the top `k` frequent values in `O(N)` time using buckets instead of a heap.

<details>
<summary>Show answer and detailed solution</summary>

```python
def top_k_frequent_bucket(nums: list[int], k: int) -> list[int]:
    counts: dict[int, int] = {}
    for number in nums:
        counts[number] = counts.get(number, 0) + 1

    buckets = [[] for _ in range(len(nums) + 1)]
    for number, frequency in counts.items():
        buckets[frequency].append(number)

    answer = []
    for frequency in range(len(buckets) - 1, 0, -1):
        for number in buckets[frequency]:
            answer.append(number)
            if len(answer) == k:
                return answer

    return answer
```

No value can occur more than `N` times, so frequency itself can be used as a bucket index. Scanning from the largest index visits values from highest to lowest frequency and stops after collecting `k` values.

Building counts, filling buckets, and scanning all bucket positions each take linear time.

**Complexity:** `O(N)` time and `O(N)` extra space.

**Test:** `[1, 1, 1, 2, 2, 3]` with `k = 2` returns `[1, 2]`.

</details>
