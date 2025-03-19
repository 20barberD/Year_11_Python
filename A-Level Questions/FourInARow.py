#Task 3
def generateEmptyGrid(length, height):
    grid = []
    length = 0
    for x in range(length):
        grid.append([])
        for y in range(height):
            grid[-1].append("X")
            length += 1
    return grid, length

def convertColumnInput(letter: str):
    letters = ["a", "b", "c", "d", "e", "f", "g"]
    lowerLetter = letter.lower()
    if lowerLetter in letters:
        return letters.index(lowerLetter)
    else:
        return False

def rowWinCheck(grid, players):
    for row in grid:
        playerCounter = ""
        samePlayerCount = 0 #Count consecutive spaces of the same player
        for space in row:
            if samePlayerCount == 0:
                playerCounter = space
                samePlayerCount += 1
            elif samePlayerCount >= 4:
                return playerCounter
            elif space == playerCounter:
                samePlayerCount += 1
    return False

def columnWinCheck(grid):
    return

def checkIfGridFull(grid):
    numberOfBlankSpaces = 0 #Count number of blank spaces so we can see if the grid is full
    for row in grid:
        for space in row:
            if space == "X":
                numberOfBlankSpaces += 1
    if numberOfBlankSpaces == 0:
        return True

def endCheck(grid, players):
    winner = False
    #Row check
    rowCheck = rowWinCheck(grid, players)
    
    return winner

def dropInGrid(grid, column, player):
    if len(grid[0]) >= column:
        if grid[0][column] == "X":
            lastSafePlace = 0
            for i in range(1, len(grid)):
                print(i, grid[i][column])
                if grid[i][column] == "X":
                    lastSafePlace = i
                else:
                    break
            grid[lastSafePlace][column] = player #Put disc at lowest possible position in column
            return grid #Return modified grid
    return False

def outputGrid(grid):
    text = f"A B C D E F G\n-------------"
    for row in grid:
        text += "\n"
        for square in row:
            if square == "X":
                square = "."
            text += square + " "
    return text

def playGame():
    players = ["R", "Y"]
    playerNames = ["Red", "Yellow"]
    grid = [
        ["X", "X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X", "X"],
    ]
    grid, lengthOfGrid = generateEmptyGrid(7, 6)
    winner = False
    turn = 1
    while lengthOfGrid > turn: #Keep looping turns until a winner is decided
        for i in range(0, len(players)):
            currentPlayer = players[i]
            print(f"Player {playerNames[i]}, it's your turn! ")
            validMove = False
            while not validMove: #Keep asking where to move until a valid move is entered
                columnInput = convertColumnInput(input("Enter the column you want to drop a disc down: (A-G) ")) #Convert letter to column number
                if columnInput == False and columnInput != 0: #When A is entered the columnInput is 0, which counts as false
                    print("Enter in a letter from A-G! ")
                else:
                    newGrid = dropInGrid(grid, columnInput, currentPlayer) #Get new grid with the disc dropped down
                    if newGrid != False: #If the grid is valid
                        validMove = True #Valid move so the loop is broken and the next player can play
                        grid = newGrid #Replace grid with new grid
                        print(outputGrid(grid)) #Print out grid

                    else:
                        print("You can't move there! ")
    winCheck = endCheck(grid, players)
            

sampleGrid = [
        ["X", "X", "X"],
        ["X", "X", "R"],
        ["X", "X", "R"],
        ["X", "X", "R"],
        ["X", "X", "R"],
        ["X", "X", "R"],
]

playGame()