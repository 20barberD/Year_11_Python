def hexChar(denary):
    hexNumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    return hexNumbers[denary]

def denaryToHex(denary):
    hex = ""
    length = 0
    while (denary >= 16 ** (length+1)):
        length += 1
    for x in range(length, -1, -1):
        hex += hexChar((denary // (16 ** x)) % 16)
    return hex

print(denaryToHex(256))