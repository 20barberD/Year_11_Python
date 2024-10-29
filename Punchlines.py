import random

jokes = [
    ["Why can't a car play football? ", "Because it has only one boot! "],
    ["What music does a mummy listen to? ", "WRAP music! "],
    ["Why did the chicken cross the road? ", "Because his car was on the other side! "],
    ["Why was the chicken sad? ", "He had to write 4 punchlines for a python project! "],
    ["Knock Knock", "Who's there?"],
]

jokeSet = jokes[random.randint(0, len(jokes)-1)]
input(jokeSet[0])
print(jokeSet[1])