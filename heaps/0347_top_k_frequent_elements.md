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

## Interview Explanation

> First I count values with a hash map. Then I keep a min-heap of at most `k` `(frequency, value)` pairs. If the heap grows too large, I remove its smallest frequency. The remaining values are the top `k`, using `O(N log K)` time.
