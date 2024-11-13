#word = ""
#for x in range(0, 5):
    #inputValue = int(input("Enter an integer between 65 and 122: "))
    #word += chr(inputValue)
#print(word)

import importlib

inputFile = input("Enter the name of the python file you want to run: ")
file = importlib.import_module(inputFile)