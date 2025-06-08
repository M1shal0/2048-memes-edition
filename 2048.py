#penis
import cv2 as cv
import numpy as np
from enum import IntFlag, auto
import random

HEIGHT = 400
WIDE = 400
img = np.zeros((HEIGHT, WIDE, 3), np.uint8)
img.fill(255)

full = cv.imread('C:/Rabota/PythonSamples/Programming/To_write_smth/Python/2048 memes edition/2048.png') #add your own path to the picture

class CellType(IntFlag):
    empty = 0
    two = auto()
    four = auto()
    eight = auto()
    sixteen = auto()
    thirtytwo = auto()
    sixtyfour = auto()
    hurnder28 = auto()
    twohundred56 = auto()
    fivehunderd12 = auto()
    a1024 = auto()

def draw_game(game):
    xs = 0
    xe = 100
    ys = 0
    ye = 100
    for x in range(0, 4):
        for y in range(0, 4):
            a = game[y][x]
            if a == 0:
                img[ys:ye, xs:xe, :] = tiles[CellType.empty]
            elif a == 2:
                img[ys:ye, xs:xe, :] = tiles[
                    CellType.two]
            elif a == 4:
                img[ys:ye, xs:xe, :] = tiles[CellType.four]
            elif a == 8:
                img[ys:ye, xs:xe, :] = tiles[CellType.eight]
            elif a == 16:
                img[ys:ye, xs:xe, :] = tiles[CellType.sixteen]
            elif a == 32:
                img[ys:ye, xs:xe, :] = tiles[CellType.thirtytwo]
            elif a == 64:
                img[ys:ye, xs:xe, :] = tiles[CellType.sixtyfour]
            elif a == 128:
                img[ys:ye, xs:xe, :] = tiles[CellType.hurnder28]
            elif a == 256:
                img[ys:ye, xs:xe, :] = tiles[CellType.twohundred56]
            elif a == 512:
                img[ys:ye, xs:xe, :] = tiles[CellType.fivehunderd12]
            elif a == 1024:
                img[ys:ye, xs:xe, :] = tiles[CellType.a1024]
            else:
                img[ys:ye, xs:xe, :] = tiles[CellType.empty]
                cv.putText(img, str(a), (ys, xs), 0, 1, (0,0,0))
            ys += 100
            ye += 100
        xs += 100
        xe += 100
        ys = 0
        ye = 100


 
tiles = {}
tiles[CellType.empty] = full[:, 400:500, :]
tiles[CellType.two] = full[:, 0:100, :]
tiles[CellType.four] = full[:, 100:200, :]
tiles[CellType.eight] = full[:, 200:300, :]
tiles[CellType.sixteen] = full[:, 300:400, :]
tiles[CellType.thirtytwo] = full[:, 500:600, :]
tiles[CellType.sixtyfour] = full[:, 600:700, :]
tiles[CellType.hurnder28] = full[:, 700:800, :]
tiles[CellType.twohundred56] = full[:, 800:900, :]
tiles[CellType.fivehunderd12] = full[:, 900:1000, :]
tiles[CellType.a1024] = full[:, 1000:1100, :]






# a1 = ["t","f","t","f","t","f","t","f","t","f","t","f","t","f","t","f", "t", "s","ei","s","ei","s","ei","s","ei","s","ei","s","ei","s","ei","s","ei"]
# i=0

import random
game = [
    [2, 4, 8, 16],
    [32, 64, 128, 256],
    [512, 1024, 0, 2],
    [2, 0, 4, 2]
]

def move(game):
     for stolb in range(4):
            
            for strok in range(3, 0, -1):
                if game[strok][stolb] == game[strok-1][stolb]:
                    game[strok][stolb] = game[strok][stolb] *2
                    game[strok-1][stolb] = 0
            
            
            
            for strok in range(3):
                if game[strok+1][stolb] == 0:
                    game[strok+1][stolb] = game[strok][stolb]
                    game[strok][stolb] = 0

            for strok in range(2, 0, -1):
                if game[strok][stolb] == 0:
                    game[strok][stolb] = game[strok-1][stolb]
                    game[strok-1][stolb] = 0

            
            for strok in range(3, 0, -1):
                if game[strok][stolb] == game[strok-1][stolb]:
                    game[strok][stolb] = game[strok][stolb] *2
                    game[strok-1][stolb] = 0


            for strok in range(2, 0, -1):
                if game[strok][stolb] == 0:
                    game[strok][stolb] = game[strok-1][stolb]
                    game[strok-1][stolb] = 0
     

while True:
    for i in game:
        print(i)
    img[...] = 0
    draw_game(game)
    cv.imshow('2048', img)
    command = cv.waitKeyEx(0)
    print('-------------------------------')
    # command = input()

    if command == ord('s'):
        move(game)
        
    if command == ord('w'):
        game.reverse()
        move(game)
            
        game.reverse()


    if command == ord('d'):
        
        a = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                a[j][i] = game[i][j]

        game = a
        
        move(game)
            
    
        
        b = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                b[j][i] = game[i][j]

        game = b




    if command == ord('a'):
        
        a = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                a[j][i] = game[i][j]

        game = a
        
        game.reverse()
        move(game)
            
        game.reverse()
    
        
        b = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                b[j][i] = game[i][j]

        game = b


    count = 0
    for i in game:
        if 0 not in i:
            count += 1

    if count == 4:
        print("gg")
        cv.putText(img, 'YOU are LOSER', (200, 100), 0, 2, (255, 0,0 ))
    else:
        randx = random.randint(0, 3)
        randy = random.randint(0, 3)

        while game[randy][randx] != 0:
            randx = random.randint(0, 3)
            randy = random.randint(0, 3)


        game[randy][randx] = 2
