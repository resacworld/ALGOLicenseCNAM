import random

rowlabel = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def globalNbRow(grid):
    if grid != None:
        return len(grid)
    return None

def globalNbCol(grid):
    if grid != None:
        return len(grid[0]) 
    return None

def createGrid(nbRow, nbColumn):
    boatsToPlace = [5, 4, 3, 3, 2]

    grid = [['' for _ in range(nbColumn)] for _ in range(nbRow)]

    for boatLength in boatsToPlace:
        placed = False

        while not placed:
            orientation = random.choice(['horizontal', 'vertical'])
            if orientation == 'horizontal':

                row = random.randint(0, nbRow - 1)
                col = random.randint(0, nbColumn - boatLength)

                zoneOk = True

                for i in range(-1, boatLength + 1):
                    for j in range(-1, 2):
                        print(i, j)
                        if ((row + j) < 0) or ((row + j) >= (nbRow)) or ((col + i) < 0) or ((col + i) >= (nbColumn)):
                            continue

                        if grid[row + j][col + i] != '':
                            zoneOk = False
                            break

                if zoneOk:
                    for i in range(boatLength):
                        grid[row][col + i] = 'b'
                    placed = True
            else:
                row = random.randint(0, nbRow - boatLength)
                col = random.randint(0, nbColumn - 1)

                zoneOk = True

                for i in range(-1, boatLength + 1):
                    for j in range(-1, 2):
                        if ((row + i) < 0) or ((row + i) >= (nbColumn)) or ((col + j) < 0) or ((col + j) >= (nbRow)):
                            continue

                        if grid[row + i][col + j] != '':
                            zoneOk = False
                            break

                if zoneOk:
                    for i in range(boatLength):
                        grid[row + i][col] = 'b'
                    placed = True

    return grid

def printGrid(grid):
    global rowlabel

    toplabel = "  "
    for label in rowlabel[:len(grid[0])]:
        toplabel += " " + label
    print(toplabel)

    i = 1
    for row in grid:
        text = str(i).zfill(2)

        for cell in row:
            if cell == '':
                text += "🌊"
            elif cell == 'b':
                text += "⛵"
            elif cell == 'h':
                text += "💥"
            elif cell == 'm':
                text += "💦"
        
        print(text)
        i += 1