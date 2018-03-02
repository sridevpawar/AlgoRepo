def printMatrix(matrix):
    for row in matrix:
        print(" {0} {1} {2} {3} {4}".format(*[col for col in row]))
            
def scanMatrix(matrix):
    for row in range(1,len(matrix[0])):
        for col in range(1,len(matrix[0])):
            if matrix[row][col] == 0:
                matrix[row][0] = 0
                matrix[0][col] = 0

    return matrix

def fillRowOrCol(matrix, row, col):
    for i in range(1,len(matrix[0])):
        if row >= 0 and col == -1:
            matrix[row][i] = 0
        elif row == -1 and col >= 0:
            matrix[i][col] = 0

    return matrix


def fillMatrix(matrix, rowZero, colZero):
    for i in range(1,len(matrix[0])):
        if matrix[0][i] == 0:
                fillRowOrCol(matrix, -1, i)

        if matrix[i][0] == 0:
                fillRowOrCol(matrix, i, -1)
    if rowZero:
        matrix[0][0] = 0
        fillRowOrCol(matrix, 0, -1)

    if colZero:
        matrix[0][0] = 0
        fillRowOrCol(matrix, -1, 0)

    return matrix

def zeroMatrix(matrix):
    if len(matrix) <= 0 or len(matrix[0]) <= 0:
        return
    
    rowZero = False
    colZero = False

    if matrix[0][0] == 0:
        rowZero = colZero = True
    else:
        for i in range(1,len(matrix[0])):
            if matrix[0][i] == 0:
                rowZero = True

            if matrix[i][0] == 0:
                colZero = True

    return fillMatrix(scanMatrix(matrix), rowZero, colZero)

val1 = [[2,5,4,8,3],[8,7,3,0,6],[3,4,5,2,1],[3,0,5,2,4],[3,4,0,2,4]]
val2 = [[2,5,0,8,3],[8,7,3,1,6],[3,4,5,2,1],[3,1,5,2,4],[3,4,1,2,4]]
val3 = [[2,5,4,8,3],[8,7,3,1,6],[0,4,5,2,1],[3,1,5,2,4],[3,4,1,2,4]]
val4 = [[0,5,4,8,3],[8,7,3,1,6],[3,4,5,2,1],[3,1,5,2,4],[3,4,1,2,4]]
val5 = [[2,1,4,8,3],[8,7,3,0,6],[3,4,0,2,1],[3,0,5,2,4],[0,4,0,2,4]]
printMatrix(val1)
print("-"*20)
printMatrix(zeroMatrix(val1))
print("-"*50)
printMatrix(val2)
print("-"*20)
printMatrix(zeroMatrix(val2))
print("-"*50)
printMatrix(val3)
print("-"*20)
printMatrix(zeroMatrix(val3))
print("-"*50)
printMatrix(val4)
print("-"*20)
printMatrix(zeroMatrix(val4))
print("-"*50)
printMatrix(val5)
print("-"*20)
printMatrix(zeroMatrix(val5))
print("-"*50)