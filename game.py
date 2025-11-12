from grid import globalNbCol, globalNbRow
from scores import calculScore

def cellNameToIndex(grid, cellName):
    """
    Retourne les indices (ligne, colonne) d'une cellule à partir de son nom (ex: A5)
    """
    if len(cellName) < 2:
        raise ValueError("Position de cellule invalide")

    colLetter = cellName[0].upper()
    rowIndex = int(cellName[1:]) - 1

    colIndex = ord(colLetter) - ord('A')

    if rowIndex < 0 or rowIndex >= globalNbRow(grid):
        raise ValueError("Index de ligne hors de la grille")
    if colIndex < 0 or colIndex >= globalNbCol(grid):
        raise ValueError("Index de colonne hors de la grille")

    return (rowIndex, colIndex)

def checkIfBoatSinked(grid, position):
    """
    Vérifie si le bateau touché en (x, y) est entièrement coulé.
    Renvoie true si coulé, sinon faux
    """
    (x, y) = position

    n = len(grid)
    if grid[x][y] != 'h':
        return False  # pas un tir réussi, donc pas concerné

    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    pile = [(x, y)]
    visites = set()
    cases_bateau = []

    while pile:
        i, j = pile.pop()
        if (i, j) in visites or not (0 <= i < n and 0 <= j < n):
            continue
        if grid[i][j] not in ('b', 'h'):
            continue

        visites.add((i, j))
        cases_bateau.append((i, j))

        for dx, dy in directions:
            pile.append((i + dx, j + dy))

    # Il est coulé si toutes les cases du bateau sont 'h', touchées
    return all(grid[i][j] == 'h' for i, j in cases_bateau)

def sendMissileAt(grid, position):
    """
    Envoie un missile à la position donnée sur la grille.
    Retourne True si touché, False si manqué, ou False et print un message d'erreur si hors de la grille.
    """

    (row, col) = position

    if (row < 0) or (col < 0) or (row > globalNbRow(grid)) or (col > globalNbCol(grid)):
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
    
def askSendMissile(grid, play_duration):
    """
    Demande a l'utilisateur d'entrer une position pour envoyer un missile sur la grille.
    """

    position = None
    strPosition = ""

    while position == None:
        try :
            strPosition = input("Entrez la position du missile (ex: A5): ")
            position = cellNameToIndex(grid, strPosition)
        except ValueError as e:
            print("Erreur : " + str(e))

    result = sendMissileAt(grid, position)

    if result:
        if checkIfBoatSinked(grid, position):
            print("Coulé")
        else:
            print("Touché !")
    else:
        print("Manqué !")

    saveTurnInFile(grid, play_duration, "Utilisateur", strPosition, grid[position[0]][position[1]])

def isGameOver(grid):
    """
    Retourne True si tous les bateaux ont été coulés (donc que la partie est finie), False sinon.
    """

    for row in grid:
        for cell in row:
            if cell == 'b':
                return False
    return True

def reinitFile():
    """
    Réinitialise le fichier de jeu
    """

    with open("game.txt", "w", encoding="utf-8") as file:
        file.truncate(0)
        file.write("Début de la partie\n")
        file.write("========================\n")

def saveTurnInFile(grid, play_duration, gridName, cellName, value):
    """
    Sauvegarde les gilles de jeux et les mouvments dans le fichier game.txt
    """

    (row, col) = cellNameToIndex(grid, cellName)

    with open("game.txt", "a", encoding="utf-8") as file:
        file.write(f"Tour de l'{gridName}\n")

        if value == "h":
            file.write(f"Cible en {cellName} touchée !\n")
        elif value == "m":
            file.write(f"Cible en {cellName} manquée.\n")
        
        file.write(f"Score : {calculScore(grid, play_duration)}\n")

        for row in grid:
            text = ""
            for cell in row:
                if cell == "":
                    text += " "
                else:
                    text += cell

            file.write(text + "\n")
        
        file.write("========================\n")