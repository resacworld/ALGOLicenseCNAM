from grid import globalNbCol, globalNbRow

def cellNameToIndex(grid, cellName):
    if len(cellName) < 2:
        raise ValueError("Position de cellule invalide")

    colLetter = cellName[0].upper()
    rowIndex = int(cellName[1:]) - 1

    colIndex = ord(colLetter) - ord('A')

    if rowIndex < 0 or rowIndex >= globalNbRow(grid):
        raise ValueError("Index de ligne hors de la grille")
    if colIndex < 0 or colIndex >= globalNbCol(grid):
        raise ValueError("Index de colonne hors de la grille")

    return (rowIndex, colIndex)

def sendMissileAt(grid, row, col):
    if (row < 0) or (col < 0) or (row > globalNbRow(grid)) or (col > globalNbCol(grid)):
        return "Hors de la grille"
    
    if grid[row][col] == 'h' or grid[row][col] == 'm':
        print("Déja tiré sur cette case")
        return False

    elif grid[row][col] == 'b':
        grid[row][col] = 'h'
        return True
    
    else:
        grid[row][col] = 'm'
        return False
    
def askSendMissile(grid):
    row = None
    col = None

    while row == None and col == None:
        try :
            (row, col) = cellNameToIndex(grid, input("Entrez la position du missile (ex: A5): "))
        except ValueError as e:
            print("Erreur : " + str(e))

    result = sendMissileAt(grid, row, col)

    if result:
        print("Touché !")
    else:
        print("Manqué !")

def isGameOver(grid):
    for row in grid:
        for cell in row:
            if cell == 'b':
                return False
    return True