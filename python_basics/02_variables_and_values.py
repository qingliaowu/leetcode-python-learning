"""Lesson 2: variables, numbers, booleans, None, and operators."""

# = gives a value a name. This is called assignment.
age = 30
price = 4.5
name = "Ada"
is_learning = True
missing_answer = None

print(name, age, price, is_learning, missing_answer)

# Basic arithmetic
total = 7 + 3
difference = 7 - 3
product = 7 * 3
division = 7 / 2
whole_division = 7 // 2
remainder = 7 % 2

assert total == 10
assert difference == 4
assert product == 21
assert division == 3.5
assert whole_division == 3
assert remainder == 1

# Comparisons create True or False.
assert 5 > 2
assert 5 != 2
assert (5 == 5) is True

# Boolean operators combine or reverse conditions.
has_time = True
knows_python = False
can_practice = has_time and not knows_python
assert can_practice is True

print("Lesson 2 checks passed.")
