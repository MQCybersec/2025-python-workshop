from grid import Grid

cellEmpty:str = "[ ]"
cellPlayer1:str = "[X]"
cellPlayer2:str = "[O]"
grid = Grid(3, 3, cellEmpty)

def GameLogic():
    grid.SetCell(0, 1, cellPlayer1)
    grid.SetCell(grid.xSize-1, grid.ySize-1, cellPlayer2)
    grid.Render()

    # using grid.SetCell(x,y) means we dont have to do this:
    tempCell = grid.GetCell(1,1)
    tempCell.text = "[W]"
    print(f"Cell(1,1) is: {grid.GetCell(1,1).text}")

GameLogic()



