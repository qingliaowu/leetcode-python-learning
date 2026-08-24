# 322. Coin Change

[LeetCode problem](https://leetcode.com/problems/coin-change/) | [Python solution](./0322_coin_change.py) | [DP guide](./README.md)

## What the Question Asks

You have unlimited coins of each listed value. Return the fewest coins needed to make the exact amount. Return `-1` when it is impossible.

```text
coins = [1, 2, 5], amount = 11
5 + 5 + 1 uses 3 coins
answer = 3
```

This asks for the minimum number of coins, not the number of different combinations.

## The DP State

Define one saved answer clearly:

```text
dp[x] = the minimum number of coins needed to make amount x
```

The final answer should be `dp[amount]`.

## Base Case

```python
dp[0] = 0
```

Making amount zero requires zero coins. This known answer lets larger amounts build from it.

## Transition

Suppose the last coin used is `coin`. Before adding it, the smaller amount was:

```text
current_amount - coin
```

If that smaller answer is known, using this coin creates:

```text
dp[current_amount - coin] + 1
```

Try every coin and keep the smallest result:

```python
dp[current_amount] = min(
    dp[current_amount],
    dp[current_amount - coin] + 1,
)
```

## Why Fill Amounts From Small to Large?

When calculating `dp[current_amount]`, every `current_amount - coin` is smaller. Filling amounts from `1` upward guarantees those smaller answers are already available.

## The Impossible Marker

At first, unknown amounts receive:

```python
impossible = amount + 1
dp = [impossible] * (amount + 1)
```

Why is `amount + 1` safe? If a solution exists and the smallest coin is at least `1`, no solution needs more than `amount` coins. Therefore, `amount + 1` is worse than every possible real answer.

If the final value is still this marker, return `-1`.

## Python Used Here

```python
[impossible] * (amount + 1)
```

This creates a list with one entry for every amount from `0` through `amount`.

```python
range(1, amount + 1)
```

`range` stops before its second value, so `amount + 1` makes the loop include `amount`.

## Dry Run

Use coins `[1, 3, 4]` and amount `6`:

| Amount `x` | Best construction | `dp[x]` |
| ---: | --- | ---: |
| 0 | Use no coins | 0 |
| 1 | `1` | 1 |
| 2 | `1 + 1` | 2 |
| 3 | `3` | 1 |
| 4 | `4` | 1 |
| 5 | `4 + 1` | 2 |
| 6 | `3 + 3` | 2 |

The greedy choice of taking `4` first would leave `2`, producing three coins: `4 + 1 + 1`. DP finds the better answer `3 + 3`.

## Why It Is Correct

Every solution for a positive amount has one final coin. The algorithm tries every possible final coin. For each one, it combines that coin with the already optimal answer for the remaining smaller amount. Taking the minimum covers every valid final choice.

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

Let:

- `A` be the target amount,
- `C` be the number of coin values.

For every amount from `1` through `A`, the algorithm tries all `C` coins.

- Time: `O(A * C)`.
- Extra space: `O(A)` for the `dp` list.

This is pseudo-polynomial time because it depends on the numeric amount, not only the number of digits used to write that amount. In most interviews, clearly stating `O(amount * number_of_coins)` is sufficient.

## Edge Cases

- Amount `0`: return `0` without using a coin.
- No combination can make the amount: return `-1`.
- One coin equals the target: return `1`.
- Coin order should not affect the answer.
- A greedy largest-coin choice may be wrong, as `[1, 3, 4]`, amount `6` shows.

## Common Mistakes

- Using greedy choice without proving that the coin system supports it.
- Forgetting `dp[0] = 0`.
- Accessing `dp[current_amount - coin]` when the result is negative.
- Returning the impossible marker instead of `-1`.
- Counting combinations instead of minimizing coin count.
- Saying time is only `O(A)` while ignoring the inner coin loop.

## Interview Explanation

> I define `dp[x]` as the minimum coins needed for amount `x`, with `dp[0] = 0`. For every amount, I try each coin as the final coin and use one plus the saved answer for the remaining amount. There are `A` amounts and `C` coin choices, so time is `O(A * C)` and space is `O(A)`.

## Test Aloud

For coins `[2]`, amount `3`, say:

```text
Amount 1 stays impossible. Amount 2 becomes one coin using dp[0]. Amount 3
cannot use a saved reachable remainder, so its marker never changes. The code
returns -1.
```
