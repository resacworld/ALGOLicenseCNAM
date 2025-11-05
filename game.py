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

def sendMissileAt(grid, position):
    (row, col) = position

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
    position = None
    strPosition = ""

    while position == None:
        try :
            strPosition = input("Entrez la position du missile (ex: A5): ")
            position = cellNameToIndex(grid, strPosition)
        except ValueError as e:
            print("Erreur : " + str(e))

    result = sendMissileAt(grid, position)

    if result:
        print("Touché !")
    else:
        print("Manqué !")

    saveTurnInFile(grid, "Utilisateur", strPosition, grid[position[0]][position[1]])

def isGameOver(grid):
    for row in grid:
        for cell in row:
            if cell == 'b':
                return False
    return True

def reinitFile():
    with open("game.txt", "w", encoding="utf-8") as file:
        file.truncate(0)
        file.write("Début de la partie\n")
        file.write("========================\n")

def saveTurnInFile(grid, gridName, cellName, value):
    """
    Sauvegarde les gilles de jeux
    """

    (row, col) = cellNameToIndex(grid, cellName)

    with open("game.txt", "a", encoding="utf-8") as file:
        file.write(f"Tour de l'{gridName}\n")

        if value == "h":
            file.write(f"Cible en {cellName} touchée !\n")
        elif value == "m":
            file.write(f"Cible en {cellName} manquée.\n")

        for row in grid:
            text = ""
            for cell in row:
                if cell == "":
                    text += " "
                else:
                    text += cell

            file.write(text + "\n")
        
        file.write("========================\n")