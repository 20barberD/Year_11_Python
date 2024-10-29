namesFile = "Names.txt"
with open(namesFile, 'r') as names:
    lines = names.readlines()
    print(lines[0].replace("\n", ""))
    print(lines[1].replace("\n", ""))