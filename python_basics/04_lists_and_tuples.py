"""Lesson 4: store ordered items in lists and tuples."""

numbers = [10, 20, 30]

assert numbers[0] == 10
assert numbers[-1] == 30

# Lists can change.
numbers.append(40)
assert numbers == [10, 20, 30, 40]

removed = numbers.pop()
assert removed == 40
assert numbers == [10, 20, 30]

numbers[1] = 25
assert numbers == [10, 25, 30]
assert numbers[0:2] == [10, 25]

unsorted_numbers = [3, 1, 2]
sorted_copy = sorted(unsorted_numbers)
assert sorted_copy == [1, 2, 3]
assert unsorted_numbers == [3, 1, 2]

point = (4, 7)
x, y = point
assert x == 4
assert y == 7

print("Lesson 4 checks passed.")
