# -*- coding: utf-8 *-`
import random
from grid import createGrid, printGrid, askUserCreateGrid
from game import askSendMissile, sendMissileAt, isGameOver

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

userGrid = askUserCreateGrid()
iaGrid = createGrid(len(userGrid), len(userGrid[0]))


def main():
    printGrid(userGrid, True, "Utilisateur")
    printGrid(iaGrid, gridName="Ordinateur")

    while not isGameOver(userGrid) and not isGameOver(iaGrid):
        askSendMissile(iaGrid)

        print("Tour de l'ordinateur...")

        sendMissileAt(userGrid, (row, col))

        printGrid(userGrid, True, "Utilisateur")
        printGrid(iaGrid, gridName="Ordinateur")

    print("partie terminée !")

    if isGameOver(userGrid):
        print("L'ordinateur a gagné !")
    else :
        print("Vous avez gagné !")

if __name__ == "__main__":
    main()