#Task 15
def playGame(numberOfPlayers, target, maximumInput):
    currentNumber = 0
    if numberOfPlayers > 0 and target > 0 and maximumInput > 0:
        alivePlayers = list(range(1, numberOfPlayers+1))
        print(f"There are {len(alivePlayers)} players. \nYou will take turns entering numbers between 1 and {maximumInput}. \nIf the total of the numbers reaches {target}, the last person who entered a number loses.")
        while target > currentNumber:
            for player in alivePlayers:
                validNumberEntered = False
                playerInput = 1
                while not validNumberEntered:
                    playerInput = input(f"Player {player}, enter in a number between 1 and {maximumInput}: ")
                    if len(playerInput) > 0:
                        playerInput = int(playerInput)
                        if maximumInput >= playerInput and playerInput > 0:
                            validNumberEntered = True
                    if validNumberEntered == False:
                        print(f"You need to enter a number between 1 and {maximumInput}! ")
                currentNumber += int(playerInput)
                print(f"The total is now {currentNumber}... ")
                if currentNumber >= target:
                    print("The target has been reached! ")
                    del alivePlayers[alivePlayers.index(player)]
                    print(f"Player {player} has been eliminated! ")
                    if len(alivePlayers) == 1:
                        print(f"Player {alivePlayers[0]} wins! ")
                        return
                    else:
                        currentNumber = 0
                        print(f"There are now {len(alivePlayers)} players. The total has been reset. ")


playGame(2, 15, 3)