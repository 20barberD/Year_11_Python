def findAllCombinations(list):
    combinations = []
    for digit in list:
        
    return combinations

digits = []
for x in range(1, 4):
    digit = int(input(f"Enter a{'nother' if x != 1 else ''} number: "))
    digits.append(digit)

for combination in findAllCombinations(digits):
    print(combination)