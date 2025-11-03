# -*- coding: utf-8 *-`
import random

"""
Créer par VIDALOT victor 
License 3 Robotique CNAM
"""

'''
grid = [
    ['', 'b', 'b', 'b', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', 'b', '', '', '', '', '', ''],
    ['', 'b', '', '', '', '', '', ''],
    ['', '', '', 'b', 'b', 'b', 'b', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
]
'''

'''
palcer 3 bateau de 2, 3 et 4 de longueur (caractère b)
'''

'''
==> NOTE après correction

ord('A') => Retourne le code ASCII de la lettre A
chr(65) => Retourne le caractère correspondant au code ASCII 65

Si on fait ord(lettre) - ord('A') on obtient l'index de la lettre dans l'alphabet (A=0, B=1, C=2, ...)

'''

rowlabel = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
globalNbRow = 0
globalNbCol = 0


def createGrid(nbRow, nbColumn):
    global globalNbRow, globalNbCol
    globalNbRow = nbRow
    globalNbCol = nbColumn

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
                        print(i, j)
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

grid = createGrid(10, 10)

def printGrid():
    global grid, rowlabel

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
                text += "⛵"
            elif cell == 'h':
                text += "💥"
            elif cell == 'm':
                text += "💦"
        
        print(text)
        i += 1

def sendMissileAt(row, col):
    global grid

    if (row < 0) or (col < 0) or (row > globalNbRow) or (col > globalNbCol):
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
    
def cellNameToIndex(cellName):
    if len(cellName) < 2:
        raise ValueError("Position de cellule invalide")

    colLetter = cellName[0].upper()
    rowIndex = int(cellName[1:]) - 1

    colIndex = ord(colLetter) - ord('A')

    if rowIndex < 0 or rowIndex >= globalNbRow:
        raise ValueError("Index de ligne hors de la grille")
    if colIndex < 0 or colIndex >= globalNbCol:
        raise ValueError("Index de colonne hors de la grille")

    return (rowIndex, colIndex)


def askSendMissile():
    global globalNbCol, globalNbRow

    row = None
    col = None

    while row == None and col == None:
        try :
            (row, col) = cellNameToIndex(input("Entrez la position du missile (ex: A5): "))
        except ValueError as e:
            print("Erreur : " + e)

    result = sendMissileAt(row, col)

    if result:
        print("Touché !")
    else:
        print("Manqué !")

def isGameOver():
    for row in grid:
        for cell in row:
            if cell == 'b':
                return False
    return True

def main():
    printGrid()

    while not isGameOver():
        askSendMissile()
        printGrid()

    print("partie terminée !")

if __name__ == "__main__":
    main()