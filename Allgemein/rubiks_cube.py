import numpy as np

def initCube():
    rubics_cube = np.empty((6,3,3), dtype=str)
    colors = ["W","B","Y","G","O","R"]

    for i in range(6):
        rubics_cube[i] = colors[i]

    print(rubics_cube)
    print("")

    return rubics_cube


def moveRowHorizon(cube, row, direct):
    moved = cube.copy()

    faces = [0,3,2,1]

    rows = moved[faces,row,:].copy()

    if direct == 0:
        moved[faces,row,:] = np.roll(rows, shift=1, axis=0) #Rotiere die Reihen der seitlichen Flächen gegen den Uhrzeiger
        if row == 0:                                        #row = 0 bedeutet obere Querreihe + Oberseite
            topBot = moved[4].copy()
            moved[4] = np.rot90(topBot)                     #Oberseite ird gedreht
        else:                                               #row = 2 (oder alles andere) bedeutet untere Querreihe +Unterseite wird gedreht
            topBot = moved[5].copy()
            moved[5] = np.rot90(topBot)                     #Unterseite wird gedreht
    else:
        moved[faces,row,:] = np.roll(rows, shift=-1, axis=0)    #Rotiere die Reihen der seitlichen Flächen im Uhrzeiger
        if row == 0:
            topBot = moved[4].copy()
            moved[4] = np.rot90(topBot,3)
        else:
            topBot = moved[5].copy()
            moved[5] = np.rot90(topBot,3)

    return moved
    

def moveRowVerti(cube, col, direct):
    moved = cube.copy()

    faces = [0,4,2,5]

    cols = moved[faces, :, col].copy()

    if direct == 0:
        moved[faces,:,col] = np.roll(cols, shift=1, axis=0)
        if col == 0:
            leftRight = moved[3].copy()
            moved[3] = np.rot90(leftRight,3)
        elif col == 2:
            leftRight = moved[1].copy()
            moved[1] = np.rot90(leftRight,3)
    else:
        moved[faces,:,col] = np.roll(cols, shift=-1, axis=0)
        if col == 0:
            leftRight = moved[3].copy()
            moved[3] = np.rot90(leftRight)
        elif col == 2:
            leftRight = moved[1].copy()
            moved[1] = np.rot90(leftRight)

    return moved


def moveRowSideway(cube, depth, direct):
    moved = cube.copy()

    faces = [1,5,3,4]

    depths = moved[faces, :, depth].copy()

    if direct == 0:
        moved[faces,:,depth] = np.roll(depths, shift=1, axis=0)
        if depth == 0:
            frontBack = moved[0].copy()
            moved[0] = np.rot90(frontBack)
        elif depth == 2:
            frontBack = moved[2].copy()
            moved[2] = np.rot90(frontBack)
    else:
        moved[faces,:,depth] = np.roll(depths, shift=-1, axis=0)
        if depth == 0:
            frontBack = moved[0].copy()
            moved[0] = np.rot90(frontBack,3)
        elif depth == 2:
            frontBack = moved[2].copy()
            moved[2] = np.rot90(frontBack,3)

    return moved



def shuffleCube(cube):
    
    shuffledCube = cube
    
    return shuffledCube

cube1 = initCube()

cube1 = moveRowHorizon(cube1, 0, 0)

print(cube1)
print("")

cube1 = moveRowHorizon(cube1, 2, 1)

print(cube1)
print("Horizontal")
print("")

cube1 = moveRowVerti(cube1, 0, 0)

print(cube1)
print("")

cube1 = moveRowVerti(cube1, 2, 1)

print(cube1)
print("Vertikal")
print("")

cube1 = moveRowSideway(cube1, 0, 0)

print(cube1)
print("")

cube1 = moveRowSideway(cube1, 2, 0)

print(cube1)
print("Seitlich")
print("")