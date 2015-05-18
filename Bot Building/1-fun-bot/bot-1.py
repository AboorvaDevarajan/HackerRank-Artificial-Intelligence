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
    num = pX - mX
    if(num > 0):
        dir = "DOWN"
    else:
        dir = "UP"
    for _ in range(0,abs(num)):
        print(dir)
        
    num = pY - mY
    if(num > 0):
        dir = "RIGHT"
    else:
        dir = "LEFT"
    for _ in range(0,abs(num)):
        print(dir)  
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)

