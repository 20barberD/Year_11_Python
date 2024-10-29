#print("ooooooooooo\no         o\no  #   #  o\no    #    o\no  #   #  o\no         o\nooooooooooo")

#name = input("Enter your name: ")
#age = int(input("Enter your age: "))

#print(f"Hello {name}! You are {age} years old! ")

#number1 = float(input("Enter a number: "))
#number2 = float(input("Enter another number: "))
#print(number1 + number2)

#favouriteSportsTeam = input("What is your favourite sports team? ")
#gamesWon = int(input("How many games have they won? "))
#gamesDrawn = int(input("How many games have they drawn? "))
#print(gamesWon * 3 + gamesDrawn)

#firstName = input("Enter your first name: ")
#surname = input("Enter your surname: ")
#print(f"{firstName[0]}{surname[:2]}".upper())

#favouriteColour = input("Enter your favourite colour: ")
#print(f"There are {len(favouriteColour)} letters in that word. ")

#word = ""
#for x in range(0, 5):
    #inputValue = int(input("Enter an integer between 65 and 122: "))
    #word += chr(inputValue)
#print(word)

import importlib

inputFile = input("Enter the name of the python file you want to run: ")
file = importlib.import_module(inputFile)