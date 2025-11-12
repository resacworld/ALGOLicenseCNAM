import json
import os
import datetime

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
    print(os.path.exists(fichier))
    if os.path.exists(fichier):
        with open(fichier, "r") as f:
            scores = json.load(f)
    else:
        scores = []

    date_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    
    scores.insert(0, {"pseudo": pseudo, "score": score, "date": date_time})

    print(scores)

    with open(fichier, "w+") as f:
        json.dump(scores, f)

def get3bestScores(fichier="scores.json"):
    if os.path.exists(fichier):
        with open(fichier, "r") as f:
            scores = json.load(f)
    else:
        scores = []

    return sorted(scores, key=lambda x: x["score"], reverse=True)[:3]

def getUserRank(pseudo, score, fichier="scores.json"):
    if os.path.exists(fichier):
        with open(fichier, "r") as f:
            scores = json.load(f)
    else:
        return -1  # Fichier inexistant, pas de classement possible

    scores_sorted = sorted(scores, key=lambda x: x["score"], reverse=True)

    rank = 1
    for entry in scores_sorted:
        if entry["pseudo"] == pseudo and entry["score"] == score:
            return rank
        rank += 1

    return -1  # Pseudo et score non trouvés


# if __name__ == "__main__":
#     saveBestScore("victor", 1100)
#     saveBestScore("ben", 2500)
#     saveBestScore("hugo", 1200)
#     saveBestScore("aurore", 400)
#     saveBestScore("pascal", 900)

#     print(get3bestScores())
#     print(getUserRank("hugo", 1200))