def printMatrix(matrix):
    for row in matrix:
        print((" {} "*len(row)).format(*[col for col in row]))


def rotateMatrix(matrix):
    if len(matrix) <= 0 or len(matrix[0]) <= 0:
        return

    resMatrix = [[0 for i in matrix] for i in matrix[0]]

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            resMatrix[col][(len(matrix) - 1) - row] = matrix[row][col]

    return resMatrix





val1 = [[2,5,4],[8,7,3],[3,4,5],[3,0,5],[3,4,0]]
val2 = [[2,5,0,8,3],[8,7,3,1,6],[3,4,5,2,1]]
val3 = [[2,5,4,8,3],[8,7,3,1,6],[0,4,5,2,1],[3,1,5,2,4],[3,4,1,2,4]]
val4 = [[0,5,4,8,3],[8,7,3,1,4],[3,4,2,4,3],[3,1,5,2,4],[3,4,1,2,4]]
val5 = [[8,3],[3,3],[3,0],[2,4],[8,3],[3,3],[3,0],[2,4],[8,3],[3,3],[3,0],[2,4],[8,3],[3,3],[3,0],[2,4]]
printMatrix(val1)
print("-"*20)
printMatrix(rotateMatrix(val1))
print("-"*50)
printMatrix(val2)
print("-"*20)
printMatrix(rotateMatrix(val2))
print("-"*50)
printMatrix(val3)
print("-"*20)
printMatrix(rotateMatrix(val3))
print("-"*50)
printMatrix(val4)
print("-"*20)
printMatrix(rotateMatrix(val4))
print("-"*50)
printMatrix(val5)
print("-"*20)
printMatrix(rotateMatrix(val5))
print("-"*50)