from cell import Cell
class Grid():
    xSize:int
    ySize:int
    grid:list[list[Cell]]

    def __init__(self, x, y, emptyCell = "[ ]"):
        self.grid = [[Cell(xPos, yPos, emptyCell) for xPos in range(x)] for yPos in range(y)]
        self.xSize = x
        self.ySize = y
        

    def GetCell(self, x, y):
        return self.grid[y][x]

    def SetCell(self, x, y, cell):
        self.grid[y][x].text = cell

    def Render(self):
        for line in self.grid:
            newLine = ""
            for cell in line:
                newLine += cell.text
            print(newLine)


