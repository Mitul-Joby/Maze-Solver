'''
Module to solve maze matrix with recursion 
*More effective algorithm can be used to solve the maze
'''

def Check(maze,Start,End,Path,Wall):
    '''
    Checks if matrix is properly defined \n

    Parameters
    ----------
        maze  : Maze matrix to be solved\n
        Start : To display start location to console  \n
        End   : To display end location to console    \n
        Path  : To display path location to console   \n
        Wall  : To display wall location to console   \n
    '''

    #======================= ERROR CHECKING ============================#
    l = len(maze[0])
    erval = []
    errFlag = 0
    for x in maze:
        #Checks if matrix is a square matrix    
        if len(x)!= l:
            print('\nBad Maze. Error: Dimension')
            exit()
        
        #Checks if matrix has proper values
        for i in x:
            if  (i!= Path) and (i!= Wall) and (i!= Start) and (i!= End):
                errFlag+=1
                erval.append([maze.index(x),x.index(i),i])

    if errFlag != 0:
        print('\nBad Maze. Error: Values')
        print(errFlag,'errors found')
        for x in erval:
            print('Index:',x[0],x[1],' Value:',x[2])
        exit()

    #Checking how many start and end points has been defined
    StartX=-1;StartY=-1;StartCount=0
    EndX=-1;EndY=-1;EndCount=0
    for i in maze:
        for j in i:
            if j == Start:
                StartX = maze.index(i)
                StartY = maze[StartX].index(j)
                StartCount+=1
            if j == End:
                EndX = maze.index(i)
                EndY = maze[EndX].index(j)
                EndCount+=1
    
    if StartX == -1 or EndX == -1 or StartY == -1 or EndY == -1 or StartCount != 1 or EndCount != 1:
        print('\n\nStart/End definition error\n')
        exit()
    return StartX,StartY,EndX,EndY

def SOLVE(maze,Start='S',End='E',Path=' ',Wall='X'):
    '''
    Solves maze matrix with recursion  \n

    Parameters
    ----------
        maze  : Maze matrix to be solved\n
        Start : To display start location to console  \n
        End   : To display end location to console    \n
        Path  : To display path location to console   \n
        Wall  : To display wall location to console   \n
    '''
    #=======================     SOLVING     ============================#
    from copy import deepcopy
    StartX,StartY,EndX,EndY=Check(maze,Start,End,Path,Wall)
    sol=0
    check = deepcopy(maze)
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            check[i][j] = 0

    def move(lastmove,x,y):
        if lastmove==1:
            if y-1>=0 and (maze[x][y-1] == Path or maze[x][y-1] == End) and check[x][y-1] != 1:
                check[x][y]=1
                solve(x,y-1)
                check[x][y]=0
                lastmove = 1
        elif lastmove==2:
            if  x+1<len(maze) and (maze[x+1][y] == Path or maze[x+1][y] == End) and check[x+1][y] != 1:
                check[x][y]=1
                solve(x+1,y)
                check[x][y]=0
                lastmove=2
        elif lastmove==3:
            if y+1<len(maze[x]) and (maze[x][y+1] == Path or maze[x][y+1] == End) and check[x][y+1] != 1:
                check[x][y]=1
                solve(x,y+1)
                check[x][y]=0
                lastmove=3
        elif lastmove==4:    
            if x-1>=0 and (maze[x-1][y] == Path or maze[x-1][y] == End) and check[x-1][y] != 1:
                check[x][y]=1
                solve(x-1,y)    
                check[x][y]=0
                lastmove=4
        else: 
            lastmove=0
        return lastmove

    def solve(x,y):
        lastmove=0
        if x == EndX and y == EndY:
            check[x][y] = 1
            nonlocal sol
            sol = deepcopy(check)

        lastmove = move(lastmove,x,y)
        move(1,x,y)
        move(2,x,y)
        move(3,x,y)
        move(4,x,y)
        
    solve(StartX,StartY)
    return sol
    