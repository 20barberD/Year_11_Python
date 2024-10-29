import random

numbers = []
for x in range(1, 5):
    numbers.append(random.randint(1, 10))

total = 0
for number in numbers:
    total += number
print(f"Total: {total} ")