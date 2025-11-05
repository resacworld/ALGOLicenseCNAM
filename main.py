# -*- coding: utf-8 *-`
from grid import createGrid, printGrid, askUserCreateGrid
from game import askSendMissile, sendMissileAt, isGameOver, saveTurnInFile, reinitFile
from AI import SendIAMissile
import random

"""
Créer par VIDALOT victor 
License 3 Robotique CNAM
"""

userGrid = askUserCreateGrid()
iaGrid = createGrid(len(userGrid), len(userGrid[0]))

def main():
    reinitFile()

    printGrid(userGrid, True, "Utilisateur")
    printGrid(iaGrid, gridName="Ordinateur")

    while not isGameOver(userGrid) and not isGameOver(iaGrid):
        askSendMissile(iaGrid)

        print("Tour de l'ordinateur...")

        SendIAMissile(userGrid)

        printGrid(userGrid, True, "Utilisateur")
        printGrid(iaGrid, gridName="Ordinateur")

    print("partie terminée !")

    if isGameOver(userGrid):
        print("L'ordinateur a gagné !")
    else :
        print("Vous avez gagné !")

if __name__ == "__main__":
    main()