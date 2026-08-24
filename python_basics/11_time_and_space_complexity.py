"""Lesson 11: see how operation counts grow with input size."""


def constant_steps(numbers):
    """Read at most one item: O(1) time."""
    steps = 1
    first = numbers[0] if numbers else None
    return first, steps


def logarithmic_steps(size):
    """Repeatedly cut size in half: O(log N) time."""
    steps = 0
    remaining = size

    while remaining > 1:
        remaining //= 2
        steps += 1

    return steps


def linear_steps(numbers):
    """Visit every item once: O(N) time."""
    steps = 0

    for number in numbers:
        steps += 1

    return steps


def quadratic_steps(numbers):
    """Visit every ordered pair: O(N squared) time."""
    steps = 0

    for first in numbers:
        for second in numbers:
            steps += 1

    return steps


def copy_numbers(numbers):
    """Create N new stored items: O(N) extra space."""
    copied = []

    for number in numbers:
        copied.append(number)

    return copied


if __name__ == "__main__":
    print("N | O(1) | O(log N) | O(N) | O(N squared)")
    print("--|------|----------|------|-------------")

    for size in [1, 2, 4, 8, 16]:
        numbers = list(range(size))
        _, constant = constant_steps(numbers)
        logarithmic = logarithmic_steps(size)
        linear = linear_steps(numbers)
        quadratic = quadratic_steps(numbers)
        print(
            f"{size:2} | {constant:4} | {logarithmic:8} | "
            f"{linear:4} | {quadratic:11}"
        )

    assert constant_steps(list(range(100)))[1] == 1
    assert logarithmic_steps(16) == 4
    assert linear_steps(list(range(16))) == 16
    assert quadratic_steps(list(range(16))) == 256
    assert copy_numbers([1, 2, 3]) == [1, 2, 3]

    print("Lesson 11 checks passed.")
