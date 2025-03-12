#SOFTWARE SUBSYSTEM
# Q1: Minimizing Moves to Complete a Round

#Input Section
#The below code takes the matrix as input for any matrix that is given as input
#for the testcase the height of the matrix would be the number of rows i.e. 14 for the given qn
h = int(input("Enter the height of the matrix: "))
Input = []#matrix taken as input 
for i in range(h):
    L = list(map(int, input(f'Enter row {i+1}: ').split()))#to take the rows as list
    Input.append(L)                                        #And to append it to the Input List

w = len(Input[0])
row, col = -1, -1  # Initialize start position

# Find starting position (3) by going through each row
flag = 0
for i in range(h):
    if flag == 0:
        for j in range(1,len(Input[0])+1):
            if Input[i][j] == 3:
                col = j
                row = i
                print(f'Starting at position: {row}, {col}')
                flag = 1 #flag is used here because break would not break out of the outer for loop
                break

# Determine section based on starting position
# The given matrix is divided into 8 sections shown in the below image
# Reference Image: https://github.com/Adithya-Vishnu/IGVC_101/blob/main/Pic_1.jpg

# This division is done to make sure the direction of the path is with minimum distance to the centre
# of the matrix to minimize the turns made and also to specify the directions in which the path should
# continue which is different for each section and the favourable direction is marked with the arrow.

section = 0
if 4 < row < h - 3 and 1 < col < 5:
    section = 1
elif 1 < row < 5 and 1 < col < 5:
    section = 2
elif 1 < row < 5 and 4 < col < w - 3:
    section = 3
elif 1 < row < 5 and w - 4 < col < w:
    section = 4
elif 4 < row < h - 3 and w - 4 < col < w:
    section = 5
elif h - 4 < row < h and w - 4 < col < w:
    section = 6
elif h - 4 < row < h and 4 < col < w - 3:
    section = 7
elif h - 4 < row < h and 1 < col < 5:
    section = 8

# Define the check function for movement
def check(i, j):
    '''This function is used to check where the next empty path in the preference order
    1. preferrable diagonal path
    2. straight
    3. less preferred diagonal path

    NOTE: Diagonal path is possible because it is specified in the question that going straight and
    taking a turn is allowed
    '''
    ''' i here represents the row number
        j here represents the column number'''
    if(4<i<h-3 and 1<j<5):
        #First if to check if diagonally movement is possible
        if(Input[i-1][j+1]==0):
            i=i-1
            j=j+1
        #Second if to check if forward path is possible
        elif(Input[i-1][j]==0):
            i=i-1
            j=j
        #Third If to check if other diagonal path is possible to avoid obstacle in front and first diagonal
        elif(Input[i-1][j-1]==0):
            i=i-1
            j=j-1




        
    elif(1<i<5 and 1<j<5):
        #First if to check if favourable diagonally movement is possible
        if(Input[i+1][j+1]==0):
            i=i+1
            j=j+1
        #Second if to check if forward path is possible
        elif(Input[i][j+1]==0):
            i=i
            j=j+1
        #Third If to check if unfavourable diagonal path is possible to avoid obstacle in front and first diagonal
        elif(Input[i-1][j+1]==0):
            i=i-1
            j=j+1


        
    
    elif(1<i<5 and 4<j<w-3):
        #First if to check if favourable diagonally movement is possible
        if(Input[i+1][j+1]==0):
            i=i+1
            j=j+1
        #Second if to check if forward path is possible
        elif(Input[i][j+1]==0):
            i=i
            j=j+1
        #Third If to check if unfavourable diagonal path is possible to avoid obstacle in front and first diagonal
        elif(Input[i-1][j+1]==0):
            i=i-1
            j=j+1






    elif(1<i<5 and w-4<j<w):
        #First if to check if favourable diagonally movement is possible
        if(Input[i+1][j-1]==0):
            i=i+1
            j=j-1
        #Second if to check if forward path is possible
        elif(Input[i+1][j]==0):
            i=i+1
            j=j
        #Third If to check if unfavourable diagonal path is possible to avoid obstacle in front and first diagonal
        elif(Input[i+1][j+1]==0):
            i=i+1
            j=j+1



        
    elif(4<i<h-3 and w-4<j<w):
        #First if to check if favourable diagonally movement is possible
        if(Input[i+1][j-1]==0):
            i=i+1
            j=j-1
        #Second if to check if forward path is possible
        elif(Input[i+1][j]==0):
            i=i+1
            j=j
        #Third If to check if unfavourable diagonal path is possible to avoid obstacle in front and first diagonal
        elif(Input[i+1][j+1]==0):
            i=i+1
            j=j+1





        
    elif(h-4<i<h and w-4<j<w):
        #First if to check if favourable diagonally movement is possible
        if(Input[i-1][j-1]==0):
            i=i-1
            j=j-1
        #Second if to check if forward path is possible
        elif(Input[i][j-1]==0):
            i=i
            j=j-1
        #Third If to check if unfavourable diagonal path is possible to avoid obstacle in front and first diagonal
        elif(Input[i+1][j-1]==0):
            i=i+1
            j=j-1




    elif(h-4<i<h and 4<j<w-3):
        #First if to check if favourable diagonally movement is possible
        if(Input[i-1][j-1]==0):
            i=i-1
            j=j-1
        #Second if to check if forward path is possible
        elif(Input[i][j-1]==0):
            i=i
            j=j-1
        #Third If to check if unfavourable diagonal path is possible to avoid obstacle in front and first diagonal
        elif(Input[i+1][j-1]==0):
            i=i+1
            j=j-1





    elif(h-4<i<h and 1<j<5):
        #First if to check if diagonally movement is possible
        if(Input[i-1][j+1]==0):
            i=i-1
            j=j+1
        #Second if to check if forward path is possible
        elif(Input[i-1][j]==0):
            i=i-1
            j=j
        #Third If to check if other diagonal path is possible to avoid obstacle in front and first diagonal
        elif(Input[i-1][j-1]==0):
            i=i-1
            j=j-1

    Input[i][j] = '3'  # Mark path in the matrix
    return i, j


# Start pathfinding from (row, col)
i, j = row, col
visited = set()

def check_2(i,j):
    '''purpose is to check if i,j has come back into the section with 3 in order to change the
    point of interest from the origin to 3 '''
    if(len(visited)>1):
        if(4<i<h-3 and 1<j<5):
            #--1
            if(0<i-row<2):
                return 0
            else:
                return 1
        elif(1<i<5 and 1<j<5):
            #--2
            if(0<col-j<2):
                return 0
            else:
                return 1
        elif(1<i<5 and 4<j<w-3):
            #--3
            if(0<col-j<2):
                return 0
            else:
                return 1
        elif(1<i<5 and w-4<j<w):
            #--4
            if(0<row-i<2):
                return 0
            else:
                return 1
        elif(4<i<h-3 and w-4<j<w):
            #--5
            if(0<row-i<2):
                return 0
            else:
                return 1
        elif(h-4<i<h and w-4<j<w):
            #--6
            if(0<j-col<2):
                return 0
            else:
                return 1
        elif(h-4<i<h and 4<j<w-3):
            #--7
            if(0<j-col<2):
                return 0
            else:
                return 1
        elif(h-4<i<h and 1<j<5):
            #--8
            if(0<i-row<2):
                return 0
            else:
                return 1

#The while command is used to run as long as the path has not reached back within two rows or columns
# in the forward direction depending on the sections

while check_2(i, j): 
    new_i, new_j = check(i, j)
    visited.add((new_i, new_j))
    i, j = new_i, new_j

def move_towards_3(i, j):
    # Move towards the point where 3 is located (row, col)
    # Adjusting the movement logic according to the position of 3 and ensuring we stay within bounds
    if i < row:
        if Input[i + 1][j] == 0:  # Move down if possible
            i += 1
        elif j < col and Input[i + 1][j + 1] == 0:  # Diagonal down-right if possible
            i += 1
            j += 1
        elif j > col and Input[i + 1][j - 1] == 0:  # Diagonal down-left if possible
            i += 1
            j -= 1
        Input[i][j]='3'
    elif i > row:
        if Input[i - 1][j] == 0:  # Move up if possible
            i -= 1
        elif j < col and Input[i - 1][j + 1] == 0:  # Diagonal up-right if possible
            i -= 1
            j += 1
        elif j > col and Input[i - 1][j - 1] == 0:  # Diagonal up-left if possible
            i -= 1
            j -= 1
        Input[i][j]='3'
    elif j < col:  # If we need to move left
        if Input[i][j - 1] == 0:  # Move left if possible
            j -= 1
        elif i < row and Input[i + 1][j - 1] == 0:  # Diagonal down-left if possible
            i += 1
            j -= 1
        elif i > row and Input[i - 1][j - 1] == 0:  # Diagonal up-left if possible
            i -= 1
            j -= 1
            Input[i][j]='3'
    elif j > col:  # If we need to move right
        if Input[i][j + 1] == 0:  # Move right if possible
            j += 1
        elif i < row and Input[i + 1][j + 1] == 0:  # Diagonal down-right if possible
            i += 1
            j += 1
        elif i > row and Input[i - 1][j + 1] == 0:  # Diagonal up-right if possible
            i -= 1
            j += 1
            Input[i][j]='3'
    return i, j

while True:
    new_i, new_j = move_towards_3(i, j)
    if (new_i, new_j) == (row, col) and len(visited) > 1:
        break  # Stop when we return to the start position
    visited.add((new_i, new_j))
    i, j = new_i, new_j

# Print final path matrix
for row in Input:
    print(row)
