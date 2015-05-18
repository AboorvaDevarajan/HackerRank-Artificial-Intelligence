#!/usr/bin/python
def displayPathtoPrincess(n,grid):
    count = 0
    for i in range(0,n):
        for j in range(0,n):
            if(grid[i][j] == 'm'):
                mX = i
                mY = j
                count += 1
            if(grid[i][j] == 'p'):
                pX = i
                pY = j
                count += 1
            if(count == 2):
                break
        if(count == 2):
            break
    #code down
    flag = 0
    num = pX - mX
    if(num > 0):
        dir = "DOWN"
    else:
        dir = "UP"
    for _ in range(0,abs(num)):
        flag = 1
        print(dir)
        break
    if(flag != 1):    
        num = pY - mY
        if(num > 0):
            dir = "RIGHT"
        else:
            dir = "LEFT"
        for _ in range(0,abs(num)):
            print(dir) 
            break
m = int(input())
input()
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())
displayPathtoPrincess(m,grid)
