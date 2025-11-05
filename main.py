# -*- coding: utf-8 *-`
from grid import createGrid, printGrid, askUserCreateGrid
from game import askSendMissile, sendMissileAt, isGameOver
from AI import SendIAMissile
import random

"""
Créer par VIDALOT victor 
License 3 Robotique CNAM
"""

poslist = []

userGrid = askUserCreateGrid()
iaGrid = createGrid(len(userGrid), len(userGrid[0]))

def main():
    printGrid(userGrid, True, "Utilisateur")
    printGrid(iaGrid, gridName="Ordinateur")

    while not isGameOver(userGrid) and not isGameOver(iaGrid):
        askSendMissile(iaGrid)

        print("Tour de l'ordinateur...")

        row = None
        col = None

        while row is None or col is None or (row, col) in poslist:
            row = random.randint(0, len(userGrid) - 1)
            col = random.randint(0, len(userGrid[0]) - 1)

        poslist.append((row, col))

        sendMissileAt(userGrid, (row, col))

        #SendIAMissile(iaGrid)

        printGrid(userGrid, True, "Utilisateur")
        printGrid(iaGrid, gridName="Ordinateur")

    print("partie terminée !")

    if isGameOver(userGrid):
        print("L'ordinateur a gagné !")
    else :
        print("Vous avez gagné !")

if __name__ == "__main__":
    main()