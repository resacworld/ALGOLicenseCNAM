import random
from scores import calculScore
import copy

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

def placeBoat(boatSize, grid, nbColumn, nbRow):

    #on copie la grille
    copiedGrid = copy.deepcopy(grid)
    orientation = random.randint(0, 1)
    placed = False

    nbTour = 0

    while not placed:
        if orientation == 0:

            row = random.randint(0, nbRow - 1)
            col = random.randint(0, nbColumn - boatSize)

            zoneOk = True

            for i in range(-1, boatSize + 1):
                for j in range(-1, 2):
                    if ((row + j) < 0) or ((row + j) >= (nbRow)) or ((col + i) < 0) or ((col + i) >= (nbColumn)):
                        continue

                    if copiedGrid[row + j][col + i] != '':
                        zoneOk = False
                        break

            if zoneOk:
                for i in range(boatSize):
                    copiedGrid[row][col + i] = 'b'
                placed = True
        else:
            row = random.randint(0, nbRow - boatSize)
            col = random.randint(0, nbColumn - 1)

            zoneOk = True

            for i in range(-1, boatSize + 1):
                for j in range(-1, 2):
                    if ((row + i) < 0) or ((row + i) >= (nbColumn)) or ((col + j) < 0) or ((col + j) >= (nbRow)):
                        continue

                    if copiedGrid[row + i][col + j] != '':
                        zoneOk = False
                        break

            if zoneOk:
                for i in range(boatSize):
                    copiedGrid[row + i][col] = 'b'
                placed = True

        nbTour += 1

        if nbTour > 50:
            raise Exception("Impossible de placer tous les bateaux sur la grille (augementer la taille de la grille ou relancer).")

    return copiedGrid

def createGrid(nbRow, nbColumn):
    boatsToPlace = [5, 4, 3, 3, 2]

    grid = [['' for _ in range(nbColumn)] for _ in range(nbRow)]

    for boatLength in boatsToPlace:
        grid = placeBoat(boatLength, grid, nbColumn, nbRow)

    return grid

def printGrid(grid, showBoats=False, gridName=None):
    global rowlabel

    if gridName != None:
        print("\nGrille : " + str(gridName))
    
    print(f"Score : {calculScore(grid)}")

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
