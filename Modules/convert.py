'''
Module containing functions -
    image2matrix
    matrix2image
'''


def image2matrix(source,pixels=1,Start='S',End='E',Path=' ',Wall='X'):
    '''
    Converts a maze image to a matrix.\n 
        -Green is considered Start    \n
        -Red is considered as End     \n
        -White is considered as paths \n
        -Black is considered as walls \n

    Parameters
    ----------
        source: Image Path \n
        pixels: Pixel size of start/end/path/wall (Required to be square) \n
        Start : To display start location to console                      \n
        End   : To display end location to console                        \n
        Path  : To display path location to console                       \n
        Wall  : To display wall location to console                       \n
    '''

    from imageio import imread
    try:
        pic = imread(source)
    except:
        print('Image could not be converted. Check Path.')
        exit()
    matrix=[]
    for i in range(0,len(pic),pixels):
        row=[]
        for j in range(0,len(pic),pixels):
            if pic[i][j][0] <= 125 and pic[i][j][1] <= 125 and pic[i][j][2] <= 125:
                X = Wall
            elif pic[i][j][0] >= 125 and pic[i][j][1] >= 125 and pic[i][j][2] >= 125:
                X = Path
            elif pic[i][j][0] > pic[i][j][1] and pic[i][j][0] > pic[i][j][2]:
                X = End
            elif pic[i][j][1] > pic[i][j][0] and pic[i][j][1] > pic[i][j][2]:
                X = Start
            row.append(X) 
        matrix.append(row)
    return matrix

def matrix2image(source,destination,matrix,pixels=1,):
    '''
    Converts a matrix to a maze image. \n
        -Blue is solution Path         \n
        -Green is considered Start     \n
        -Red is considered as End      \n
        -White is considered as paths  \n
        -Black is considered as walls  \n

    Parameters
    ----------
        source     : Image Path \n
        destination: Image Path \n
        matrix     : matrix to convert \n
        pixels     : Pixel size of start/end/path/wall (Required to be square) \n
    '''
    from imageio import imread,imwrite
    try:
        pic = imread(source)
    except:
        print('Image could not be converted. Check Path.')
        exit()
    # for i in range(0,len(matrix)):
    #     for j in range(0,len(matrix[0])):
    #         if matrix[i][j]==1:
    #             x=i+pixels;y=j+pixels
    #             if not(pic[x][y][0] > pic[x][y][1] and pic[x][y][0] > pic[x][y][2]) and\
    #             not(pic[x][y][1] > pic[x][y][0] and pic[x][y][1] > pic[x][y][2]):
    #                 pic[x][y][0]=30
    #                 pic[x][y][1]=144
    #                 pic[x][y][2]=255
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if matrix[i][j]==1:
                x=i*pixels;y=j*pixels
                if not(pic[x][y][0] > pic[x][y][1] and pic[x][y][0] > pic[x][y][2]) and\
                not(pic[x][y][1] > pic[x][y][0] and pic[x][y][1] > pic[x][y][2]):
                    for I in range(pixels):
                        for J in range(pixels):
                            pic[x+I][y+J][0]=30
                            pic[x+I][y+J][1]=144
                            pic[x+I][y+J][2]=255
    imwrite(destination,pic)
    return 0

if __name__=="__main__":
    print('\n\nMATRIX')
    source = "Images/Unsolved/img.png"
    for i in image2matrix(source):
            for j in i:
                print(j,end=' ')
            print()  