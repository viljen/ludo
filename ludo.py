import numpy as np
import random
import time

board = np.zeros((4,6,3))
goal = np.zeros((4,4))
start = np.array([[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]])
atStart = [0,0,0,0]
die = 0

def rolldie():
    return random.randint(1,6)

def findplace(i):
    k = i - 1
    while i not in board[k]:
        if k == 0:
            k = 3
        else:
            k -= 1
    j = 5
    while i not in board[k][j]:
        j -= 1
    g = 2
    while board[k][j][g] != i:
        g -= 1
    return k, j, g

def newmove(k, j, g, die, i):
    new_g = g
    new_j = j
    new_k = k
    if g == 0:
        move = j - die
        if move < 0:
            index = die - j
            if index > 1:
                index -= 1
                new_j = 0
                new_g = 1
                print(index)
                newmove(k, new_j, new_g, index, i)
            else:
                new_j = 0
                new_g = index
        else:
            new_j = move
    elif g == 1:
        if k == i-1:
            print("Vi nærmer oss mål")
            print(board)
            if j + die <= 5:
                new_j = j + die
            else:
                t = 0
                print(goal)
                while goal[i-1][t] == i:
                    t += 1
                goal[i-1][t] = i
                new_g = 8
                new_j = 8
                new_k = 8
        else:
            if die > 1:
                moves = die - 1
                new_g = 2
                new_j = moves
            else:
                new_j = 0
                new_g = 2
    else:
        moves = j + die
        if moves > 5:
            index = moves - 6
            if k == 3:
                new_k = 0
            else:
                new_k = k + 1
            new_g = 0
            new_j = 5 - index
        else:
            new_j = moves
    return new_k, new_j, new_g

def kick(k, j, g, i, die, old_k, old_j, old_g):
    kicked = int(board[k][j][g])
    if kicked == i:
        new_k, new_j, new_g = newmove(k,j,g,die,i)
        if board[new_k][new_j][new_g] != 0:
            kick(new_k, new_j, new_g, i, die, k, j, g)
        else:
            board[k][j][g] = 0
            board[new_k][new_j][new_g] = i
    else:
        print(kicked)
        index = 0
        print(start[kicked-1])
        while start[kicked-1][index] != 0:
            index += 1
        start[kicked-1][index] = kicked
        board[old_k, old_j, old_g] = 0
        board[k][j][g] = i

def moveboard(i, die):
    #print("Moving board")
    if i in board:
        print(f"{i} moving")
        k, j, g = findplace(i)
        new_k, new_j, new_g = newmove(k,j,g,die,i)
        if new_k != 8:
            if board[new_k][new_j][new_g] != 0:
                kick(new_k, new_j, new_g, i, die, k, j, g)
            else:
                board[k][j][g] = 0
                board[new_k][new_j][new_g] = i
        else:
            board[k][j][g] = 0
    if atStart[i-1] != 0:
        print(atStart)
        if board[i-1][1][2] == 0:
            atStart[i-1] -= 1
            if atStart[i-1] != 0:
                board[i-1][1][2] = i
    #print(board)

def makemove(i):
    print(f"Rolling for {i}")
    die = rolldie()
    print(f"Rolled {die}")
    if die == 6:
        if i in start:
            j = 0
            while start[i-1][j] != i:
                j += 1
            start[i-1][j] = 0
            print(f"{i} Got out of start")
            board[i-1][1][2] = i
            #print(board)
            atStart[i-1] += 1
        else:
            moveboard(i, die)
        makemove(i)
    else:
        moveboard(i, die)

won = False
winner = 0
while won == False:
#for i in range(85):
    for i in range(1,5):
        makemove(i)
        if 0 not in goal[i-1]:
            won = True
            winner = i
            #exit()
        print(board)
        #time.sleep(10)

print("End")
print(board)
print(start)
print(goal)
print(atStart)
print(won)
print(winner)
