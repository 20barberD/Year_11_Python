word = ""
for x in range(0, 5):
    inputValue = int(input("Enter an integer between 65 and 122: "))
    word += chr(inputValue)
print(word)