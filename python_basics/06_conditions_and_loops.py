"""Lesson 6: make decisions and repeat work."""

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

assert grade == "B"

# A for loop visits every item.
total = 0
for number in [1, 2, 3, 4]:
    total += number

assert total == 10

# range(3) produces 0, 1, 2.
indexes = []
for index in range(3):
    indexes.append(index)

assert indexes == [0, 1, 2]

# enumerate provides an index and its value together.
indexed_letters = []
for index, letter in enumerate(["a", "b"]):
    indexed_letters.append((index, letter))

assert indexed_letters == [(0, "a"), (1, "b")]

# A while loop repeats while its condition remains True.
count = 3
countdown = []
while count > 0:
    countdown.append(count)
    count -= 1

assert countdown == [3, 2, 1]

print("Lesson 6 checks passed.")
