''''
Minesweeper is a popular single-player computer game. The goal is to locate mines within a rectangular grid of cells. At the start of the game, all of the cells are concealed. On each turn, the player clicks on a blank cell to reveal its contents, leading to the following result:

If there's a mine on this cell, the player loses and the game is over;
Otherwise, a number appears on the cell, representing how many mines there are within the 8 neighbouring cells (up, down, left, right, and the 4 diagonal directions);
If the revealed number is 0, each of the 8 neighbouring cells are automatically revealed in the same way.
'''
def solution(field, x, y):
    res = []
    for item in field:
        temp = []
        for j in item:
            temp.append(-1)
        res.append(temp)
        
    counter = 0
      
       
    for i in range(x-1, x+2):
        if 0 <= i < len(field):
            for j in range(y-1,y+2):
                if 0 <= j < len(field[i]):
                    if field[i][j] == True:
                        counter += 1
    res[x][y] = counter
    
    return res