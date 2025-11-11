import json
import os

def calculScore(grid):
    score = 0

    for row in grid:
        for cell in row:
            if cell == "h":
                score += 700
            elif cell == "m":
                score -= 100
    
    return score

def saveBestScore(pseudo, score, fichier="scores.json"):
    # lit le fichier scores.json, y ajoute le nouveau score a la suite des autres osus forme [['pseudo', score1], ['pseudo2', score2], ...], puis réecrit le fichier ave la nouvelle liste
    if os.path.exists(fichier):
        with open(fichier, "r") as f:
            scores = json.load(f)
    else:
        scores = []
    
    scores.insert(0, [pseudo, score])

    with open(fichier, "w+") as f:
        json.dump(scores, f)

def get3bestScores(fichier="scores.json"):
    if os.path.exists(fichier):
        with open(fichier, "r") as f:
            scores = json.load(f)
    else:
        scores = []

    return sorted(scores, key=lambda x: x[1], reverse=True)[:3]

def getUserRank(pseudo, score, fichier="scores.json"):
    if os.path.exists(fichier):
        with open(fichier, "r") as f:
            scores = json.load(f)
    else:
        return -1  # Fichier inexistant, pas de classement possible

    scores_sorted = sorted(scores, key=lambda x: x[1], reverse=True)

    rank = 1
    for entry in scores_sorted:
        if entry[0] == pseudo and entry[1] == score:
            return rank
        rank += 1

    return -1  # Pseudo et score non trouvés