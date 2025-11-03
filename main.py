# -*- coding: utf-8 *-`
import random
from grid import createGrid, printGrid
from game import askSendMissile, isGameOver

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

grid = createGrid(10, 10)

def main():
    printGrid(grid)

    while not isGameOver(grid):
        askSendMissile(grid)
        printGrid(grid)

    print("partie terminée !")

if __name__ == "__main__":
    main()