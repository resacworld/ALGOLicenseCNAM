# -*- coding: utf-8 *-`
from grid import createGrid, printGrid, askUserCreateGrid
from scores import calculScore, saveBestScore, get3bestScores, getUserRank
from game import askSendMissile, isGameOver, reinitFile
from AI import SendIAMissile
import random

"""
Créer par VIDALOT victor 
License 3 Robotique CNAM
"""

userGrid = askUserCreateGrid()
iaGrid = createGrid(len(userGrid), len(userGrid[0]))

pseudo = input("Entrez votre pseudo : ")

def main():
    # Réinitialisation du fichier de jeu
    reinitFile()

    # Affichage des meilleurs scores
    bestScores = get3bestScores()
    print("Meilleurs scores :")
    for score in bestScores:
        print(f"{score[0]} : {score[1]} points")
    
    # Affichage des grilles de jeu
    printGrid(userGrid, True, pseudo)
    printGrid(iaGrid, gridName="Ordinateur")

    # Boucle principale du jeu
    while not isGameOver(userGrid) and not isGameOver(iaGrid):
        # Tour de l'utilisateur
        askSendMissile(iaGrid)

        # Tour de l'ordinateur
        print("Tour de l'ordinateur...")
        SendIAMissile(userGrid)

        # Affichage des grilles de jeu
        printGrid(userGrid, True, pseudo)
        printGrid(iaGrid, gridName="Ordinateur")

    # Calcul et affichage du gagant et du résultat final
    print("partie terminée !")

    if isGameOver(userGrid):
        print("L'ordinateur a gagné !")
    else :
        print("Vous avez gagné !")

        score = calculScore(iaGrid)
        print(f"Votre score est de {score} points.")

        saveBestScore(
            pseudo,
            score,
        )

        print(f"Vous êtes au rang n°{getUserRank(pseudo, score)}")

if __name__ == "__main__":
    main()