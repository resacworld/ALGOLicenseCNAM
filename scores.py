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
    
    scores.append([pseudo, score])
    with open(fichier, "w") as f:
        json.dump(scores, f)