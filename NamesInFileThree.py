namesFile = "Names.txt"
with open(namesFile, 'a') as names:
    names.writelines(["Name!!!!!\n", "Jonathan\n"])
    names.close()

with open(namesFile, 'r') as names:
    for name in names.readlines():
        print(name.replace("\n", ""))