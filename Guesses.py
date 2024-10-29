import random

answer = random.randint(1, 20)
attempts = 0
guessed = False
while not guessed:
    guess = int(input("Guess what my number between 1 and 20 is! "))
    attempts += 1
    if guess == answer:
        guessed = True
    else:
        print("WRONG!")
print(f"You guessed the correct answer, {answer} in {attempts} attempts!")