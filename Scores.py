scores = [
    [2,4,5,8],
    [3,5,8,9],
]

total = 0
for set in scores:
    print(set[0])
    for number in set:
        total += number

print(total)