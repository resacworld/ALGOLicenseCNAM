# -*- coding: utf-8 *-`
from grid import createGrid, printGrid, askUserCreateGrid
from scores import calculScore, saveBestScore, get3bestScores, getUserRank
from game import askSendMissile, isGameOver, reinitFile
from AI import SendIAMissile
import time

"""
Créer par VIDALOT victor 
License 3 Robotique CNAM
"""

# Création des deux grilles de jeu
userGrid = askUserCreateGrid()
iaGrid = createGrid(len(userGrid), len(userGrid[0]))

pseudo = input("Entrez votre pseudo : ")

playerTimeCounter = 0
iaTimeCounter = 0

def main():
    global playerTimeCounter, iaTimeCounter
    """
    Fonction principale 
    """
    # Réinitialisation du fichier de jeu
    reinitFile()

    # Affichage des meilleurs scores
    bestScores = get3bestScores()
    print("Meilleurs scores :")
    for score in bestScores:
        print(f"{score["date"]} - {score["pseudo"]} : {score["score"]} points")

    # Boucle principale du jeu
    while not isGameOver(userGrid) and not isGameOver(iaGrid):
        # Affichage des grilles de jeu
        printGrid(userGrid, calculScore(userGrid, play_duration=playerTimeCounter), True, pseudo)
        printGrid(iaGrid, calculScore(iaGrid, play_duration=iaTimeCounter) ,gridName="Ordinateur")

        # Tour de l'utilisateur
        startTimer = time.time()
        askSendMissile(iaGrid, playerTimeCounter)
        playerTimeCounter += time.time() - startTimer

        # Tour de l'ordinateur
        print("Tour de l'ordinateur...")

        startTimer = time.time()
        SendIAMissile(userGrid, iaTimeCounter)
        iaTimeCounter += time.time() - startTimer

    # Calcul et affichage du gagant et du résultat final
    print("partie terminée !")

    if isGameOver(userGrid):
        print("L'ordinateur a gagné !")

        """ 
        Aucun affichage de score ni sauvegarde
        Afin de respecter les consignes données dans le TD 3

        TD3 2/ je cite : "..., mais si c'est le joueur qu i a perdu le score sera None " => donc pas calcul de score dans mon cas (et donc pas de sauvegarde non plus)
        TD3 3/ je cite : "Pour ceux qui ont fait l'IA dans le TP2, si le joueur a perdu on quitte la partie et on ne récupère pas son pseudo" => pas de sauvegarde
        """
    else :
        print("Vous avez gagné !")

        # Calcul du score
        score = calculScore(iaGrid, playerTimeCounter)
        print(f"Votre score est de {score} points.")

        # Sauvegarde du score
        saveBestScore(
            pseudo,
            score,
        )

        # Affichage du rang de l'utilisateur
        print(f"Vous êtes au rang n°{getUserRank(pseudo, score)}")

if __name__ == "__main__":
    main()