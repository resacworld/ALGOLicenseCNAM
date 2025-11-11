import random
from grid import globalNbCol, globalNbRow
from game import sendMissileAt, saveTurnInFile

# poshistory = []
# localposhistory = []

poslist = []

def SendIAMissile(grid):
    """
    IA simple qui envoie un missile à une position aléatoire non encore touchée
    """
    row = None
    col = None

    while row is None or col is None or (row, col) in poslist:
        row = random.randint(0, len(grid) - 1)
        col = random.randint(0, len(grid[0]) - 1)

    poslist.append((row, col))

    sendMissileAt(grid, (row, col))
    
    saveTurnInFile(grid, "Ordinateur", chr(col + ord('A')) + str(row + 1), grid[row][col])

    """
    # Début non finit d'une IA plus intelligente qui cible les positions autour d'un coup réussi
    
    sendpos = None

    if len(poshistory) > 0 and poshistory[len(poshistory)-1][2]:
        localpos = None

        if localposhistory[len(localposhistory) - 1][2]:
            if len(localposhistory) - 1 == 0:
                localpos = (localposhistory[len(localposhistory)-1][0]-1, localposhistory[len(localposhistory)-1][1])
            elif len(localposhistory) - 1 == 1:
                localpos = (localposhistory[len(localposhistory)-1][0], localposhistory[len(localposhistory)-1][1]-1)
            elif len(localposhistory) - 1 == 2:
                localpos = (localposhistory[len(localposhistory)-1][0]+1, localposhistory[len(localposhistory)-1][1])
            elif len(localposhistory) - 1 == 3:
                localpos = (localposhistory[len(localposhistory)-1][0]-1, localposhistory[len(localposhistory)-1][1]+1)
        
        else:
            if len(localposhistory) == 0:
                localpos = (poshistory[len(poshistory)-1][0]-1, poshistory[len(poshistory)-1][1])
            elif len(localposhistory) == 1:
                localpos = (poshistory[len(poshistory)-1][0], poshistory[len(poshistory)-1][1]-1)
            elif len(localposhistory) == 2:
                localpos = (poshistory[len(poshistory)-1][0]+1, poshistory[len(poshistory)-1][1])
            elif len(localposhistory) == 3:
                localpos = (poshistory[len(poshistory)-1][0]-1, poshistory[len(poshistory)-1][1]+1)

        localposhistory.append((localpos[0], localpos[1], sendMissileAt(localpos)))

    while sendpos is None or sendpos in poshistory:
        sendpos = (random.randint(0, globalNbRow(grid) - 1), random.randint(0, globalNbCol(grid[0]) - 1))

    poshistory.append(sendpos)

    return sendpos
    """