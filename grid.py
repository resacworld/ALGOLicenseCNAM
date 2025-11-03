import random

rowlabel = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def globalNbRow(grid):
    if grid != None:
        return len(grid)
    return None

def globalNbCol(grid):
    if grid != None:
        return len(grid[0]) 
    return None

def askUserCreateGrid():
    nbRow = None
    nbColumn = None

    while nbRow == None or nbColumn == None:
        try:
            
            if nbRow == None:
                nbRow = int(input("Entrez le nombre de lignes de la grille: "))

                if nbRow < 7:
                    print("Valeur trop petite !!")
                    nbRow = None

            if nbColumn == None:
                nbColumn = int(input("Entrez le nombre de colonnes de la grille: "))

                if nbColumn < 7:
                    print("Valeur trop petite !!")
                    nbColumn = None

                elif nbColumn > len(rowlabel):
                    print("Nombre trop grand !!")
                    nbColumn = None

        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier valide.")

    return createGrid(nbRow, nbColumn)

def createGrid(nbRow, nbColumn):
    boatsToPlace = [5, 4, 3, 3, 2]

    grid = [['' for _ in range(nbColumn)] for _ in range(nbRow)]

    for boatLength in boatsToPlace:
        placed = False

        while not placed:
            orientation = random.choice(['horizontal', 'vertical'])
            if orientation == 'horizontal':

                row = random.randint(0, nbRow - 1)
                col = random.randint(0, nbColumn - boatLength)

                zoneOk = True

                for i in range(-1, boatLength + 1):
                    for j in range(-1, 2):
                        if ((row + j) < 0) or ((row + j) >= (nbRow)) or ((col + i) < 0) or ((col + i) >= (nbColumn)):
                            continue

                        if grid[row + j][col + i] != '':
                            zoneOk = False
                            break

                if zoneOk:
                    for i in range(boatLength):
                        grid[row][col + i] = 'b'
                    placed = True
            else:
                row = random.randint(0, nbRow - boatLength)
                col = random.randint(0, nbColumn - 1)

                zoneOk = True

                for i in range(-1, boatLength + 1):
                    for j in range(-1, 2):
                        if ((row + i) < 0) or ((row + i) >= (nbColumn)) or ((col + j) < 0) or ((col + j) >= (nbRow)):
                            continue

                        if grid[row + i][col + j] != '':
                            zoneOk = False
                            break

                if zoneOk:
                    for i in range(boatLength):
                        grid[row + i][col] = 'b'
                    placed = True

    return grid

def printGrid(grid, showBoats=False, gridName=None):
    global rowlabel

    if gridName != None:
        print("\nGrille : " + str(gridName))

    toplabel = "  "
    for label in rowlabel[:len(grid[0])]:
        toplabel += " " + label
    print(toplabel)

    i = 1
    for row in grid:
        text = str(i).zfill(2)

        for cell in row:
            if cell == '':
                text += "🌊"
            elif cell == 'b':
                text += "⛵" if showBoats else "🌊"
            elif cell == 'h':
                text += "💥"
            elif cell == 'm':
                text += "💦"
        
        print(text)
        i += 1