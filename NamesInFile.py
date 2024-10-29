namesFile = "Names.txt"
with open(namesFile, 'r') as names:
    for name in names.readlines():
        print(name.replace("\n", ""))