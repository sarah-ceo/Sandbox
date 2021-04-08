import numpy as np
import random
import os
import cv2
from collections import OrderedDict 

def LoadImage(image_name):
    image_path = os.path.join("../Images/Contours", image_name)
    image = cv2.imread(image_path, 0).astype(np.int16)
    image = np.pad(image, (1,1), constant_values=0)
    image[np.where(image<100)] = 0
    image[np.where(image>=100)] = 1
    #print("Length of path : ", np.count_nonzero(image == 1))
    return image

def FirstPosition(figure):
    for i in range(figure.shape[1]-1, -1, -1):
        for j in range(len(figure[i])):
            if figure[i,j]==1:
                ratio = int(j/figure.shape[0]*100)
                first_moves = [(0, 1)]*ratio
                return (i, j), first_moves

def FirstPosition_bis(figure):
    for i in range(figure.shape[0]):
        for j in range(figure.shape[1]):
            if figure[i,j]==1:
                return (i, j), [(0,0)]

def availablePositions(grille, x, y):
    positions = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (grille[x+i, y+j] == 1):
                positions.append((i,j))
    return positions

def SimulationPartie(GrilleTemp, x, y):
    nb_cases = 0
    while True:
        L = availablePositions(GrilleTemp, x, y)
        
        if (len(L)==0):
            return nb_cases
        randomMove = random.randint(0, len(L)-1)
        direction = L[randomMove]
        GrilleTemp[x, y] = -1
        x += direction[0]
        y += direction[1]
        nb_cases += 1

def MonteCarlo(Grille, x, y, nombreParties):
    Total = 0
    for i in range(nombreParties):
        Grille2 = np.copy(Grille)
        Total += SimulationPartie(Grille2, x, y)
    return Total

def Play(figure, firstPos):
    sequence = []
    PosJ1 = firstPos

    while True:
        figure[PosJ1[0], PosJ1[1]] = -1
        positions = availablePositions(figure, PosJ1[0], PosJ1[1])
        if (len(positions) > 0):
            MCT_scores = []
            for i in range(len(positions)):
                MCT_scores.append(MonteCarlo(figure, PosJ1[0] + positions[i][0], PosJ1[1] + positions[i][1], 100))

            best_index = MCT_scores.index(max(MCT_scores))

            sequence.append(positions[best_index])
            PosJ1 = (PosJ1[0] + positions[best_index][0], PosJ1[1] + positions[best_index][1])

        if (figure[PosJ1[0], PosJ1[1]] != 1):
            #print("Max path : ", len(sequence))
            return addLastMove(sequence, PosJ1, firstPos)

def addLastMove(sequence, currentPos, firstPos):
    if (abs(currentPos[0]-firstPos[0]) <= 1 and abs(currentPos[1]-firstPos[1]) <= 1):
        sequence = np.vstack((sequence,(firstPos[0]-currentPos[0], firstPos[1]-currentPos[1])))
    return sequence

def ExportGCode(moves, gcode_destination):
    with open(gcode_destination, "w") as f:
        f.writelines("G91\n")
        for i in range(len(moves)):
            f.writelines("G0" + " X" + str(moves[i][1]) + "Y" + str(moves[i][0])+"\n")
