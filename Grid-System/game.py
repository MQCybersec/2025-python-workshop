# this file is like main.py but more advanced

from grid import Grid

cellEmpty:str = "[ ]"
cellPlayer1:str = "[X]"
cellPlayer2:str = "[O]"
grid = Grid(6, 6, cellEmpty)


def GetMove(player, axis) -> int:
    plyInput = input(f"Player {player}: Enter move (in {axis} axis) ") 
    while (len(plyInput) != 1 or plyInput.isnumeric() is False): # filter invalid inputs
        plyInput = input(f"Incorrect Input! Try again:\nPlayer {player}: Enter move (in {axis} axis) ") 
    return int(plyInput) # return plyInput as an integer

def GetPlayerCell(playerTurn):
    cell = "[?]"
    match playerTurn:
        case 1:
            cell = cellPlayer1
        case 2:
            cell = cellPlayer2
        #case _: # we declare cell above to act as the default case 
        #    return "[?]"
    return cell

def Move(playerTurn):
    grid.Render()
    xPos = GetMove(playerTurn, "X")
    yPos = GetMove(playerTurn, "Y")
    playerCell = GetPlayerCell(playerTurn)
    grid.SetCell(xPos, yPos, playerCell)

def GetNextPlayerTurn(lastPlayer) -> int:
    # return the number of which player's turn it is
    # i.e. lastPlayer = 1 then return 2
    nextPlayer:int
    match(lastPlayer):
        case 1:
            nextPlayer = 2
        case 2:
            nextPlayer = 1
        case _:
            nextPlayer = 1   
    return nextPlayer     

def GameLogic():
    playerTurn:int = 1 # will contain whos turn it is
    gameInProgress:bool = True

    while(gameInProgress):
        Move(playerTurn)
        #CheckIfMoveWins() TODO IF TIME PERMITS
        playerTurn = GetNextPlayerTurn(playerTurn)


GameLogic()



