# -*- coding: utf-8 *-`
from grid import createGrid, printGrid, askUserCreateGrid
from scores import calculScore, saveBestScore
from game import askSendMissile, isGameOver, reinitFile
from AI import SendIAMissile
import random

"""
Créer par VIDALOT victor 
License 3 Robotique CNAM
"""

userGrid = askUserCreateGrid()
iaGrid = createGrid(len(userGrid), len(userGrid[0]))

saveBestScore("Orditest", 100)

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

    scores = [
        ['Utilisateur', calculScore(iaGrid)], 
        ['Ordinateur', calculScore(userGrid)]
    ]

    if scores[0][1] > scores[1][1]:
        saveBestScore(
            scores[0][0],
            scores[0][1],
        )
    else:
        saveBestScore(
            scores[1][0],
            scores[1][1],
        )


    
    

if __name__ == "__main__":
    main()