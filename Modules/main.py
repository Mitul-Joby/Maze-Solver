from solve import SOLVE
from convert import image2matrix,matrix2image 

import sys
sys.setrecursionlimit(1500)

#Set according to requirement
source = 'Images/Unsolved/maze_5px.png'
solved = 'Images/Solved/Sol-maze_5px.png'
pixels = 5

#Not required to set
Start  = 'S'
End    = 'E'
Path   = ' '
Wall   = 'X'

maze = image2matrix(source,pixels,Start,End,Path,Wall)
sol  = SOLVE(maze,Start,End,Path,Wall)

if sol!=0:
    print('\nSolution:')
    for x in sol:
        for y in x:
            if y == 1:
                print('X',end=' ')
            else:
                print('-',end=' ')
        print()
    print('\nSOLVED')
    matrix2image(source,solved,sol,pixels)    